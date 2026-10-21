from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import sys
import numpy as np
import torch
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root.parent/'inverse/code'))
from split_kernel import SplitKernel,radial_rule,outer_weight
class MultiSplit(SplitKernel):
 @torch.no_grad()
 def velocity(self,point):
  x,y=map(float,point);X2=x*x+y*y;a=np.sqrt(1+X2/64);tx=x/self.rad[:,None];ty=y/self.rad[:,None];ex,ey=self.cx,self.sy
  ax=1+tx*tx+ty*ty;b=2*(tx*ex+ty*ey);dm=(tx-ex)**2+(ty-ey)**2;dp=(tx+ex)**2+(ty+ey)**2
  wm=outer_weight(self.rad[:,None]*torch.sqrt(dm)/a);wp=outer_weight(self.rad[:,None]*torch.sqrt(dp)/a)
  denm=torch.clamp(dm*dm,min=1e-100);denp=torch.clamp(dp*dp,min=1e-100)
  d1=-(tx-ex)*(ty-ey)*wm/denm+(tx+ex)*(ty+ey)*wp/denp
  d2=.5*(((tx-ex)**2-(ty-ey)**2)*wm/denm-((tx+ex)**2-(ty+ey)**2)*wp/denp)
  far=self.rad[:,None]>max(2*np.sqrt(X2)+4*a,1.);den=torch.clamp((ax*ax-b*b)**2,min=1e-100)
  m1=tx*ty+ex*ey;n1=tx*ey+ty*ex;m2=.5*(tx*tx-ty*ty+ex*ex-ey*ey);n2=tx*ex-ty*ey
  d1=torch.where(far,(-4*m1*ax*b+2*n1*(ax*ax+b*b))/den,d1)
  d2=torch.where(far,(4*m2*ax*b-2*n2*(ax*ax+b*b))/den,d2)
  grows=torch.einsum('rak,rai->rki',self.rh,torch.stack([d1,d2],dim=-1))*self.rw[:,None,None]/self.nang
  ed,rr,rw=radial_rule(self.rmin,2*a,self.order,self.panel);dx=rr[:,None]*ex;dy=rr[:,None]*ey;f0=self.f(x,y)
  loc=.5*(self.f(x+dx,y+dy)+self.f(x-dx,y-dy))-f0
  lrows=torch.einsum('rak,ia->rki',loc,self.kk)*(1-outer_weight(rr/a))[:,None,None]*rw[:,None,None]
  return (grows.sum(0)+lrows.sum(0)+torch.stack([torch.zeros_like(f0),-.5*f0],dim=-1)).cpu().numpy()

def tail_constants(d,V):
 H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
 ceil=lambda v:(v.numerator+v.denominator-1)//v.denominator
 B=ceil(max(abs(F(float(v))) for v in d.b.ravel()));eps=F(1,5)-1/F(d.cl);assert eps>0 and d.L==8
 out=[]
 for j in range(V.shape[1]):
  Bd=ceil(max(abs(F(float(v))) for v in V[:-2,j]));dc=abs(F(float(V[-2,j])));C=512*H*(Bd+dc/(2*F(d.cl)**2)*B*(1+2*d.N*d.N)*(1+2/eps));out.append(C)
 return 512*H*B,out

