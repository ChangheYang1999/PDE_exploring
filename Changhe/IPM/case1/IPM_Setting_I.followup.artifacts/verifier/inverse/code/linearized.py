"""Own continuum transport linearization on nodal candidate directions.
The density variation is differentiated algebraically, velocity by a separate
full-plane kernel, and spatial gradients by Cartesian eighth-order differences.
No solver or evaluator from another lane is imported.
"""
import json,sys,time,hashlib,argparse
from pathlib import Path
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebder,chebval2d
import torch
from collocation import NodalDensity
from density import gradient_fd
from gpu import Kernel,GPUField,tensor,DTYPE,DEV


def direction_coefficients(source,vecs):
 b=np.zeros((source.N+1,source.M,vecs.shape[1]));b[1:]=vecs[:-2].reshape(source.N,source.M,-1)
 co=dct(b[::-1],type=1,axis=0)/source.N;co[[0,-1]]*=.5
 co=dct(co,type=2,axis=1)/source.M;co[:,0]*=.5
 return co

class LinearDensity:
 def __init__(self,source,co,dcl):
  self.source=source;self.co=co;self.dcl=dcl
  self.bqco=2*chebder(source.co,axis=0)
 def __call__(self,x,y):
  f=self.source;x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));r2=x*x+y*y
  lb=np.log1p(r2/f.L**2);q=-np.expm1(-.5*(1-f.k)*lb)
  cs=np.cos(2*f.map_inverse(np.arctan2(np.abs(y),np.abs(x))));z=2*q-1
  db=chebval2d(z,cs,self.co);b=chebval2d(z,cs,f.co);bq=chebval2d(z,cs,self.bqco)
  return x*x*y*np.exp(.5*(f.k-3)*lb)*(db-self.dcl/f.cl**2*.5*lb*(b-(1-q)*bq))

class MultiLinearGPU:
 def __init__(self,source,co,dcl,block=32768):
  self.base=GPUField(source);self.source=source;self.K=co.shape[-1];self.block=block
  self.dcl=tensor(dcl);self.kdot=-self.dcl/source.cl**2
  cq=np.zeros_like(source.co);cq[:-1]=2*chebder(source.co,axis=0)
  # Each channel is a separate tensor-product interpolant.
  allco=np.concatenate((co.transpose(2,0,1),source.co[None],cq[None]),axis=0)
  self.co=tensor(allco.transpose(0,2,1).reshape(-1,source.N+1));self.nchan=self.K+2
 @torch.no_grad()
 def __call__(self,x,y):
  x,y=torch.broadcast_tensors(tensor(x),tensor(y));shape=x.shape
  xx,yy=x.reshape(-1),y.reshape(-1);out=torch.empty((xx.numel(),self.K),dtype=DTYPE,device=DEV)
  f=self.source
  for start in range(0,xx.numel(),self.block):
   sl=slice(start,min(start+self.block,xx.numel()));xp,yp=xx[sl],yy[sl];r2=xp*xp+yp*yp
   lb=torch.log1p(r2/f.L**2);q=-torch.expm1(-.5*(1-f.k)*lb);z=2*q-1
   basis=torch.empty((f.N+1,q.numel()),dtype=DTYPE,device=DEV);basis[0]=1.;basis[1]=z
   for j in range(2,f.N+1):basis[j]=2*z*basis[j-1]-basis[j-2]
   ac=(self.co@basis).reshape(self.nchan,f.M,-1)
   ct=torch.cos(2*self.base.map_inverse(torch.atan2(torch.abs(yp),torch.abs(xp))))
   b1=torch.zeros((self.nchan,q.numel()),dtype=DTYPE,device=DEV);b2=torch.zeros_like(b1)
   for j in range(f.M-1,0,-1):b0=ac[:,j]+2*ct*b1-b2;b2,b1=b1,b0
   values=ac[:,0]+ct*b1-b2
   val=values[:self.K]+self.kdot[:,None]*(.5*lb*(values[-2]-(1-q)*values[-1]))
   out[sl]=(xp*xp*yp*torch.exp(.5*(f.k-3)*lb)*val).T
  return out.reshape(*shape,self.K)

class MultiKernel(Kernel):
 @torch.no_grad()
 def velocity(self,point,return_pieces=False):
  x,y=map(float,point);f0=self.f(x,y)
  d=.5*(self.f(x+self.dx,y+self.dy)+self.f(x-self.dx,y-self.dy))
  d-=torch.where(self.rad[:,None,None]<1.,f0,0.)
  angular=torch.einsum('rak,ia->rki',d,self.kk)
  rows=angular*self.rw[:,None,None]
  local=torch.stack((torch.zeros_like(f0),-.5*f0),dim=-1)
  u=rows.sum(0)+local
  if not return_pieces:return u.cpu().numpy()
  p=rows.reshape(-1,self.order,self.f.K,2).sum(1).cpu().numpy()
  return u.cpu().numpy(),p


def main():
 p=argparse.ArgumentParser();p.add_argument('density');p.add_argument('directions');p.add_argument('output')
 p.add_argument('--points-file',required=True);p.add_argument('--base-velocities')
 p.add_argument('--nang',type=int,default=2048);p.add_argument('--order',type=int,default=20)
 p.add_argument('--panel',type=float,default=.19);p.add_argument('--rmax',type=float,default=1e14)
 p.add_argument('--check-only',action='store_true');a=p.parse_args()
 source=NodalDensity(a.density)
 with np.load(a.directions) as z:V=z['V'];labels=z['labels'].tolist()
 co=direction_coefficients(source,V);cpu=[LinearDensity(source,co[:,:,i],V[-2,i]) for i in range(V.shape[1])]
 gpu=MultiLinearGPU(source,co,V[-2]);ker=MultiKernel(gpu,a.nang,a.order,a.panel,rmax=a.rmax)
 pts=json.loads(Path(a.points_file).read_text());base={}
 if a.base_velocities:
  for row in json.loads(Path(a.base_velocities).read_text())['rows']:base[tuple(row['point'])]=np.array(row['U'])
 bk=Kernel(GPUField(source),a.nang,a.order,a.panel,rmax=a.rmax)
 out={'configuration':vars(a),'source_md5':source.md5,'directions_md5':hashlib.md5(Path(a.directions).read_bytes()).hexdigest(),
      'labels':labels,'domain_euclidean_norms':np.linalg.norm(V,axis=0).tolist(),'dcl':V[-2].tolist(),'dC':V[-1].tolist(),'rows':[]}
 # Cheap numerical check of algebraic parameter differentiation at physical points.
 errors=[]
 for pt in [(1.,.5),(8.6,.1),(1.,100.)]:
  gv=gpu(*pt).cpu().numpy();cv=np.array([f(*pt) for f in cpu]);errors.append(float(np.max(np.abs(gv-cv))))
 out['cpu_gpu_density_difference']=errors
 if a.check_only:Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(out);return
 for pt in pts:
  start=time.monotonic();u=base.get(tuple(pt));u=bk.velocity(pt) if u is None else u
  du,pieces=ker.velocity(pt,True);g=gradient_fd(source,*pt,relative_step=.0005);rho=float(source(*pt));W=source.cl*np.array(pt)+u
  dr=np.array([float(f(*pt)) for f in cpu]);dg=np.array([gradient_fd(f,*pt,relative_step=.0005) for f in cpu]);dg2=np.array([gradient_fd(f,*pt,relative_step=.001) for f in cpu])
  answer=V[-2]*(np.array(pt)@g)+dg@W+du@g-dr
  answer2=V[-2]*(np.array(pt)@g)+dg2@W+du@g-dr
  nf=abs(rho)+abs(np.array(pt)@g)+abs(u@g);nv=abs(rho)+np.sum(np.abs(W*g))
  row={'point':pt,'base_U':u.tolist(),'base_R':float(W@g-rho),'Nf':float(nf),'Nv':float(nv),
       'density_action':dr.tolist(),'velocity_action':du.tolist(),'gradient_action':dg.tolist(),'transport_action':answer.tolist(),
       'transport_action_over_Nv':(answer/nv).tolist(),'gradient_step_spread':np.abs(answer-answer2).tolist(),'seconds':time.monotonic()-start}
  out['rows'].append(row);Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
  np.savez_compressed(Path(a.output).with_suffix('.pieces'+str(len(out['rows'])-1)+'.npz'),panels=pieces,edges=ker.edges)

if __name__=='__main__':main()
