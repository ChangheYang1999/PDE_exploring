"""Independent partitioned real-space inverse.
An origin-centered polar integral resolves the density core even when the
observation point is far away. A compact local polar integral handles its PV.
Only this lane's field reconstruction and quadrature utilities are imported.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
import torch
from gpu import tensor,DTYPE,DEV,GPUField,load_source
from density import gradient_fd

def radial_rule(rmin,rmax,order,panel):
 edges=np.linspace(np.log(rmin),np.log(rmax),int(np.ceil(np.log(rmax/rmin)/panel))+1)
 z,w=leggauss(order)
 t=((edges[:-1,None]+edges[1:,None])/2+np.diff(edges)[:,None]*z/2).ravel()
 weights=(np.diff(edges)[:,None]*w/2).ravel()
 return edges,tensor(np.exp(t)),tensor(weights)

def outer_weight(t):
 u=torch.clamp(t-1.,1e-10,1.-1e-10)
 left=torch.exp(-1/u);right=torch.exp(-1/(1-u))
 ans=left/(left+right)
 return torch.where(t<=1.,0.,torch.where(t>=2.,1.,ans))

class SplitKernel:
 def __init__(self,field,nang=1024,order=20,panel=.16,rmin=1e-7,rmax=1e16,offset=.37):
  self.f=field;self.params=dict(nang=nang,order=order,panel=panel,rmin=rmin,rmax=rmax,offset=offset)
  self.nang=nang;self.order=order;self.panel=panel;self.rmin=rmin
  angles=(np.arange(nang)+offset)*2*np.pi/nang
  self.cx=tensor(np.cos(angles))[None,:];self.sy=tensor(np.sin(angles))[None,:]
  self.kk=tensor(np.stack((-np.sin(2*angles),np.cos(2*angles)))/nang)
  self.edges,self.rad,self.rw=radial_rule(rmin,rmax,order,panel)
  self.rh=self.f(self.rad[:,None]*self.cx,self.rad[:,None]*self.sy)
 @torch.no_grad()
 def velocity(self,point,return_pieces=False):
  x,y=map(float,point);X2=x*x+y*y;a=np.sqrt(1+X2/64)
  tx=x/self.rad[:,None];ty=y/self.rad[:,None];ex,ey=self.cx,self.sy
  ax=1+tx*tx+ty*ty;b=2*(tx*ex+ty*ey)
  dm=(tx-ex)**2+(ty-ey)**2;dp=(tx+ex)**2+(ty+ey)**2
  wm=outer_weight(self.rad[:,None]*torch.sqrt(dm)/a)
  wp=outer_weight(self.rad[:,None]*torch.sqrt(dp)/a)
  denm=torch.clamp(dm*dm,min=1e-100);denp=torch.clamp(dp*dp,min=1e-100)
  d1=-(tx-ex)*(ty-ey)*wm/denm+(tx+ex)*(ty+ey)*wp/denp
  d2=.5*(((tx-ex)**2-(ty-ey)**2)*wm/denm-((tx+ex)**2-(ty+ey)**2)*wp/denp)
  far=self.rad[:,None]>max(2*np.sqrt(X2)+4*a,1.)
  den=torch.clamp((ax*ax-b*b)**2,min=1e-100)
  m1=tx*ty+ex*ey;n1=tx*ey+ty*ex
  m2=.5*(tx*tx-ty*ty+ex*ex-ey*ey);n2=tx*ex-ty*ey
  stable1=(-4*m1*ax*b+2*n1*(ax*ax+b*b))/den
  stable2=(4*m2*ax*b-2*n2*(ax*ax+b*b))/den
  d1=torch.where(far,stable1,d1);d2=torch.where(far,stable2,d2)
  # Half-pairing, angular measure 2*pi/n; the raw kernels above omit 1/pi.
  global_rows=torch.stack(((self.rh*d1).sum(1),(self.rh*d2).sum(1)),dim=1)*self.rw[:,None]/self.nang
  ed,rr,rw=radial_rule(self.rmin,2*a,self.order,self.panel)
  dx=rr[:,None]*ex;dy=rr[:,None]*ey;f0=self.f(x,y)
  local_density=.5*(self.f(x+dx,y+dy)+self.f(x-dx,y-dy))-f0
  local_rows=(local_density@self.kk.T)*(1-outer_weight(rr/a))[:,None]*rw[:,None]
  result=global_rows.sum(0)+local_rows.sum(0)+torch.stack((torch.zeros_like(f0),-.5*f0))
  if not return_pieces:return result.cpu().numpy()
  return result.cpu().numpy(),{'origin_panels':global_rows.reshape(-1,self.order,2).sum(1).cpu().numpy(),
       'origin_edges':self.edges,'local_panels':local_rows.reshape(-1,self.order,2).sum(1).cpu().numpy(),
       'local_edges':ed,'local_radius':a}

def main():
 p=argparse.ArgumentParser();p.add_argument('density');p.add_argument('output')
 p.add_argument('--nang',type=int,default=1024);p.add_argument('--order',type=int,default=20)
 p.add_argument('--panel',type=float,default=.16);p.add_argument('--rmax',type=float,default=1e16)
 p.add_argument('--offset',type=float,default=.37);p.add_argument('--points',default='1,.5;8.6,.1;8.6,1;1,100;1000,1;10000,10')
 a=p.parse_args();source=load_source(a.density);start=time.monotonic()
 ker=SplitKernel(GPUField(source),a.nang,a.order,a.panel,rmax=a.rmax,offset=a.offset)
 out={'configuration':vars(a),'source_md5':getattr(source,'md5',None),'preparation_seconds':time.monotonic()-start,'rows':[]}
 for i,pt in enumerate([list(map(float,t.split(','))) for t in a.points.split(';')]):
  start=time.monotonic();u,pp=ker.velocity(pt,True);row={'point':pt,'U':u.tolist(),'seconds':time.monotonic()-start}
  if not isinstance(source,str):
   g=gradient_fd(source,*pt,relative_step=.0005);rho=float(source(*pt));W=source.cl*np.array(pt)+u
   R=float(W@g-rho);nf=abs(rho)+abs(np.array(pt)@g)+abs(u@g);nv=abs(rho)+np.sum(np.abs(W*g))
   row.update(rho=rho,R=R,R_Nf=abs(R)/nf,R_Nv=abs(R)/nv)
  else:
   x,y=pt;e=np.exp(-x*x-y*y);exact=np.array([2*x*(1-2*y*y),y*(4*x*x-2)])*e
   row['analytic_U']=exact.tolist();row['max_error']=float(np.max(np.abs(u-exact)))
  out['rows'].append(row);Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
  np.savez_compressed(Path(a.output).with_suffix('.pieces'+str(i)+'.npz'),**pp)
if __name__=='__main__':main()
