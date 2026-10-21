"""CUDA acceleration of this lane's own real-space kernel and density readers.
No other lane code is imported. No compilation, service, or cache is required.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
import torch
from density import X3Density,gradient_fd
from collocation import NodalDensity

DTYPE=torch.float64
DEV='cuda:0'
torch.set_num_threads(1)


def tensor(x):return torch.as_tensor(x,dtype=DTYPE,device=DEV)


class GPUField:
 def __init__(self,source,block=131072):
  self.source=source;self.block=block
  if isinstance(source,NodalDensity):
   self.kind='nodal';self.co=tensor(source.co)
   self.N=source.N;self.M=source.M;self.beta=source.beta
  elif isinstance(source,X3Density):
   self.kind='spline';self.co=tensor(source.spline.c)
   self.knots=tensor(source.knots);self.degree=source.order
   self.singular=tensor(source.singular)
  else:self.kind=source
  if not isinstance(source,str):
   self.L=source.L;self.cl=source.cl;self.k=source.k

 def map_inverse(self,theta):
  s=theta.clone();lo=torch.zeros_like(s);hi=torch.full_like(s,np.pi/2)
  for _ in range(32):
   f=s+.5*self.beta*torch.sin(2*s)-theta
   lo=torch.where(f<0,s,lo);hi=torch.where(f>0,s,hi)
   nxt=s-f/(1+self.beta*torch.cos(2*s))
   nxt=torch.where((nxt<lo)|(nxt>hi),(lo+hi)/2,nxt)
   s=torch.where(torch.abs(f)<2e-15,s,nxt)
  return s

 def nodal(self,q,theta):
  z=2*q-1
  pol=torch.empty((self.N+1,q.numel()),dtype=DTYPE,device=DEV)
  pol[0]=1.;pol[1]=z
  for j in range(2,self.N+1):pol[j]=2*z*pol[j-1]-pol[j-2]
  ac=self.co.T@pol
  ct=torch.cos(2*self.map_inverse(theta))
  b1=torch.zeros_like(q);b2=torch.zeros_like(q)
  for j in range(self.M-1,0,-1):
   b0=ac[j]+2*ct*b1-b2;b2,b1=b1,b0
  return ac[0]+ct*b1-b2

 def spline_values(self,q):
  p=self.degree;nb=self.co.shape[0]
  span=torch.searchsorted(self.knots,q,right=True)-1
  span=torch.clamp(span,p,nb-1)
  n=torch.zeros((q.numel(),p+1),dtype=DTYPE,device=DEV);n[:,0]=1.
  left=torch.zeros_like(n);right=torch.zeros_like(n)
  for j in range(1,p+1):
   left[:,j]=q-self.knots[span+1-j]
   right[:,j]=self.knots[span+j]-q
   saved=torch.zeros_like(q)
   for r in range(j):
    den=right[:,r+1]+left[:,j-r]
    tmp=torch.where(den!=0,n[:,r]/den,torch.zeros_like(den))
    n[:,r]=saved+right[:,r+1]*tmp;saved=left[:,j-r]*tmp
   n[:,j]=saved
  idx=span[:,None]-p+torch.arange(p+1,device=DEV)[None,:]
  basis=torch.zeros((q.numel(),nb),dtype=DTYPE,device=DEV)
  basis.scatter_(1,idx,n)
  return basis@self.co

 def __call__(self,x,y):
  x,y=torch.broadcast_tensors(tensor(x),tensor(y));shape=x.shape
  xx,yy=x.reshape(-1),y.reshape(-1);out=torch.empty_like(xx)
  for start in range(0,xx.numel(),self.block):
   sl=slice(start,min(start+self.block,xx.numel()));xp,yp=xx[sl],yy[sl]
   r2=xp*xp+yp*yp
   if self.kind=='manufactured':out[sl]=(8-4*r2)*yp*torch.exp(-r2);continue
   lb=torch.log1p(r2/self.L**2);q=-torch.expm1(-.5*(1-self.k)*lb)
   if self.kind=='nodal':
    bv=self.nodal(q,torch.atan2(torch.abs(yp),torch.abs(xp)))
    out[sl]=xp*xp*yp*torch.exp(.5*(self.k-3)*lb)*bv
   else:
    ac=self.spline_values(torch.minimum(q,torch.ones_like(q)))
    u2=r2/self.L**2;chi=u2/(u2+self.source.origin_radius**2)
    power=torch.ones_like(q)
    for m in range(2,ac.shape[1]):power=power*chi;ac[:,m]*=power
    ct=torch.where(r2!=0,(xp*xp-yp*yp)/r2,torch.ones_like(r2))
    b1=torch.zeros_like(q);b2=torch.zeros_like(q)
    for m in range(ac.shape[1]-1,0,-1):b0=ac[:,m]+2*ct*b1-b2;b2,b1=b1,b0
    h=ac[:,0]+ct*b1-b2+.5*(self.k-3)*lb
    z=2*q-1;b1=torch.zeros_like(q);b2=torch.zeros_like(q)
    for j in range(self.singular.numel()-1,0,-1):b0=self.singular[j]+2*z*b1-b2;b2,b1=b1,b0
    sg=self.singular[0]+z*b1-b2
    rc=torch.sqrt(r2)
    cosine=torch.where(rc!=0,torch.abs(xp)/rc,torch.zeros_like(rc))
    sine=torch.where(rc!=0,yp/rc,torch.zeros_like(rc))
    h+=(u2/(1+u2))**(.5*self.source.p3)*sg*cosine**(self.source.p3-2)*sine*sine
    out[sl]=xp*xp*yp*torch.exp(h)
  return out.reshape(shape)


class Kernel:
 def __init__(self,field,nang=1024,order=16,panel=.24,rmin=1e-7,rmax=1e12,offset=.37):
  self.f=field;self.params=dict(nang=nang,order=order,panel=panel,rmin=rmin,rmax=rmax,offset=offset)
  self.edges=np.unique(np.r_[np.linspace(np.log(rmin),np.log(rmax),int(np.ceil(np.log(rmax/rmin)/panel))+1),0.])
  z,w=leggauss(order);l=self.edges[:-1,None];r=self.edges[1:,None]
  self.logr=((l+r)/2+(r-l)*z/2).ravel();self.rweights=((r-l)*w/2).ravel()
  angles=(np.arange(nang)+offset)*2*np.pi/nang
  self.rad=tensor(np.exp(self.logr))
  self.dx=self.rad[:,None]*tensor(np.cos(angles))[None,:]
  self.dy=self.rad[:,None]*tensor(np.sin(angles))[None,:]
  self.kk=tensor(np.stack((-np.sin(2*angles),np.cos(2*angles)))/nang)
  self.rw=tensor(self.rweights)
  self.order=order

 @torch.no_grad()
 def velocity(self,point,return_pieces=False):
  x,y=map(float,point);f0=self.f(x,y)
  d=.5*(self.f(x+self.dx,y+self.dy)+self.f(x-self.dx,y-self.dy))
  d-=torch.where(self.rad[:,None]<1.,f0,0.)
  angular=d@self.kk.T
  rows=angular*self.rw[:,None]
  local=torch.stack((torch.zeros_like(f0),-.5*f0))
  u=rows.sum(0)+local
  if not return_pieces:return u.cpu().numpy()
  p=rows.reshape(-1,self.order,2).sum(1).cpu().numpy()
  pieces=np.column_stack((self.edges[:-1],self.edges[1:],p))
  return u.cpu().numpy(),pieces


def load_source(path):
 if path=='manufactured':return path
 with np.load(path) as f:nodal='b' in f
 return NodalDensity(path) if nodal else X3Density(path)


def main():
 p=argparse.ArgumentParser();p.add_argument('density');p.add_argument('output')
 p.add_argument('--nang',type=int,default=1024);p.add_argument('--order',type=int,default=16)
 p.add_argument('--panel',type=float,default=.24);p.add_argument('--rmax',type=float,default=1e12)
 p.add_argument('--rmin',type=float,default=1e-7);p.add_argument('--offset',type=float,default=.37)
 p.add_argument('--points',default='1,.5;8.6,.1;8.6,1;2,1');p.add_argument('--block',type=int,default=131072)
 a=p.parse_args();source=load_source(a.density);field=GPUField(source,a.block)
 ker=Kernel(field,a.nang,a.order,a.panel,a.rmin,a.rmax,a.offset)
 rows=[];out={'configuration':vars(a),'source_md5':getattr(source,'md5',None),'rows':rows}
 for i,point in enumerate([tuple(map(float,s.split(','))) for s in a.points.split(';')]):
  start=time.monotonic();u,pp=ker.velocity(point,True)
  row={'point':point,'U':u.tolist(),'seconds':time.monotonic()-start}
  if not isinstance(source,str):
   g=gradient_fd(source,*point);rv=float(source(*point));W=source.cl*np.array(point)+u
   R=float(W@g-rv);Nf=abs(rv)+abs(np.array(point)@g)+abs(u@g);Nv=abs(rv)+np.sum(np.abs(W*g))
   row.update(rho=rv,gradient=g.tolist(),R=R,R_Nf=abs(R)/Nf if Nf else None,R_Nv=abs(R)/Nv if Nv else None)
  rows.append(row);print(json.dumps(row),flush=True)
  Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
  np.savez_compressed(Path(a.output).with_suffix('.pieces'+str(i)+'.npz'),panels=pp)

if __name__=='__main__':main()
