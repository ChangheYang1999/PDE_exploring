"""Alternative physical panels for the independently derived vertical inverse."""
import numpy as np
from independent_hydrostatic import VerticalInverse,finite_rule

def ratio_nodes(lo,hi,order,scale):
 if hi<=lo:return np.empty(0),np.empty(0)
 cuts=[float(lo),float(hi)];v=float(scale)/64
 while v<hi:
  if lo<v:cuts.append(v)
  nv=v*1.5
  if not nv>v:raise ArithmeticError('partition stagnation')
  v=nv
 cuts=np.unique(cuts);a=cuts[:-1];b=cuts[1:];z,w=finite_rule(order)
 return (a[:,None]+(b-a)[:,None]*(z[None,:]+1)/2).ravel(),((b-a)[:,None]*w[None,:]/2).ravel()

class RatioPowerVerticalInverse(VerticalInverse):
 def at(self,x,y):
  x,y=float(x),float(y);xx,yy=abs(x),abs(y);sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
  R=self.tail_scale*max(self.inner_scale,xx,yy,1.);P=1/(1-self.p)
  a,aw=ratio_nodes(0.,yy,self.order,self.inner_scale);b,bw=ratio_nodes(yy,R,self.order,self.inner_scale);z,w=finite_rule(self.tail_order);u=(z+1)/2;t=R/u**P;tw=w/2*P*R*u**(-P-1)
  ja,jb,jt=self.jet(xx,a),self.jet(xx,b),self.jet(xx,t);tailx=float(tw@jt[:,1]);tailxx=float(tw@jt[:,3]);Ix=float(bw@jb[:,1])+tailx;Ixx=float(bw@jb[:,3])+tailxx;Jx=float((aw*a)@ja[:,1]);Jxx=float((aw*a)@ja[:,3]);V1=-sx*Ix;V2=sy*(Jxx+yy*Ixx);Phi=sx*sy*(Jx+yy*Ix)
  if x==0:V1=0.;Phi=0.
  if y==0:V2=0.;Phi=0.
  return dict(V=[V1,V2],Phi=Phi,dV2_dy=Ixx,tail_V=[-sx*tailx,sy*yy*tailxx],R_split=R,finite_order=self.order,tail_order=self.tail_order,tail_power=P,partition='ratio3/2 from inner_scale/64',tail_method='t=R/u**P, ordinary Gauss-Legendre')
