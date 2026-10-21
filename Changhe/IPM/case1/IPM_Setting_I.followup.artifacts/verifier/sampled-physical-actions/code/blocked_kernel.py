"""Evaluate the same split-kernel finite sums in bounded radial blocks."""
import numpy as np
import torch
from multi_kernel import MultiSplit
from split_kernel import radial_rule,outer_weight
class BlockedMultiSplit(MultiSplit):
 @torch.no_grad()
 def velocity(self,point):
  x,y=map(float,point);X2=x*x+y*y;a=np.sqrt(1+X2/64);ex,ey=self.cx,self.sy
  global_total=torch.zeros((self.f.K,2),dtype=self.rh.dtype,device=self.rh.device)
  for start in range(0,len(self.rad),128):
   sl=slice(start,start+128);rad=self.rad[sl,None];tx=x/rad;ty=y/rad
   ax=1+tx*tx+ty*ty;b=2*(tx*ex+ty*ey);dm=(tx-ex)**2+(ty-ey)**2;dp=(tx+ex)**2+(ty+ey)**2
   wm=outer_weight(rad*torch.sqrt(dm)/a);wp=outer_weight(rad*torch.sqrt(dp)/a)
   denm=torch.clamp(dm*dm,min=1e-100);denp=torch.clamp(dp*dp,min=1e-100)
   d1=-(tx-ex)*(ty-ey)*wm/denm+(tx+ex)*(ty+ey)*wp/denp
   d2=.5*(((tx-ex)**2-(ty-ey)**2)*wm/denm-((tx+ex)**2-(ty+ey)**2)*wp/denp)
   far=rad>max(2*np.sqrt(X2)+4*a,1.);den=torch.clamp((ax*ax-b*b)**2,min=1e-100)
   m1=tx*ty+ex*ey;n1=tx*ey+ty*ex;m2=.5*(tx*tx-ty*ty+ex*ex-ey*ey);n2=tx*ex-ty*ey
   d1=torch.where(far,(-4*m1*ax*b+2*n1*(ax*ax+b*b))/den,d1)
   d2=torch.where(far,(4*m2*ax*b-2*n2*(ax*ax+b*b))/den,d2)
   grows=torch.einsum('rak,rai->rki',self.rh[sl],torch.stack([d1,d2],dim=-1))*self.rw[sl,None,None]/self.nang
   global_total+=grows.sum(0)
  _,rr,rw=radial_rule(self.rmin,2*a,self.order,self.panel);f0=self.f(x,y);local_total=torch.zeros_like(global_total)
  for start in range(0,len(rr),128):
   sl=slice(start,start+128);rad=rr[sl];dx=rad[:,None]*ex;dy=rad[:,None]*ey
   loc=.5*(self.f(x+dx,y+dy)+self.f(x-dx,y-dy))-f0
   rows=torch.einsum('rak,ia->rki',loc,self.kk)*(1-outer_weight(rad/a))[:,None,None]*rw[sl,None,None]
   local_total+=rows.sum(0)
  return (global_total+local_total+torch.stack([torch.zeros_like(f0),-.5*f0],dim=-1)).cpu().numpy()
