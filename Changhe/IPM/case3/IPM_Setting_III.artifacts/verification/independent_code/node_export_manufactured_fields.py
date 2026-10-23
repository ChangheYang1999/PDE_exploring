"""Closed inverse formulas and an independent algebraic Q-basis reference."""
import math
from fractions import Fraction
import numpy as np
import mpmath as mp
from scipy.special import erf
from q_checkpoint_reader import QCheckpoint
from independent_hydrostatic import CartesianQJet

def rational(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));a=1+x*x+y*y
 return np.stack([y/a,-2*x*y/a**2,1/a-2*y*y/a**2,-2*y/a**2+8*x*x*y/a**3],axis=-1)
def gaussian(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));e=np.exp(-x*x-y*y)
 return np.stack([y*e,-2*x*y*e,(1-2*y*y)*e,(4*x*x-2)*y*e],axis=-1)
def closed_inverse(family,x,y,R):
 if family=='rational':
  a=math.sqrt(1+x*x);A=1+x*x+y*y;B=1+x*x+R*R
  return dict(V=[x/A,x*x*y/(a*a*A)-math.atan(y/a)/a**3],Phi=-x*math.atan(y/a)/a,dV2_dy=(x*x-1-y*y)/A**2,tail_V=[x/B,y*(x*x-1-R*R)/B**2])
 e=math.exp(-x*x-y*y);er=math.exp(-x*x-R*R);q=math.exp(-x*x)*math.sqrt(math.pi)*erf(y)/2
 return dict(V=[x*e,(2*x*x-1)*q],Phi=-x*q,dV2_dy=(2*x*x-1)*e,tail_V=[x*er,y*(2*x*x-1)*er])
def basis_object(data):
 q=QCheckpoint.__new__(QCheckpoint);q.coeff=[np.array([float(Fraction(z))for z in row])for row in data['coefficients']];q.M=len(q.coeff);q.N=2;q.L=float(Fraction(data['L']));q.kappa=float(Fraction(data['Pmap']));q.p=1-1/q.kappa;q.basis='cheb'
 return q,CartesianQJet(q)
def algebraic_reference(x,y,dps=80):
 with mp.workdps(dps):
  x=mp.mpf(float(x));y=mp.mpf(float(y));s=x*x+y*y
  lo=mp.mpf(0);hi=mp.mpf(1)
  for unused in range(mp.mp.prec+24):
   w=(lo+hi)/2
   if 16*s*w**4+w-1>0:hi=w
   else:lo=w
  w=(lo+hi)/2
  if s==0:w=mp.mpf(1)
  d=1+64*s*w**3;ws=-16*w**4/d;wss=-(128*w**3*ws+192*s*w*w*ws*ws)/d
  def G(a,b,c):
   t=1-2*c;D=a*a-b*b;H=a**4-6*a*a*b*b+b**4
   p0=1+t/4-(2*t*t-1)/8;p1=mp.mpf(3)/8-t/4;p2=-mp.mpf(1)/16
   return b*c*(p0+16*c**4*D*p1+(16*c**4)**2*H*p2)
  args=(x,y,w);gw=mp.diff(G,args,(0,0,1));gx=mp.diff(G,args,(1,0,0))+2*x*ws*gw;gy=mp.diff(G,args,(0,1,0))+2*y*ws*gw
  gxx=mp.diff(G,args,(2,0,0))+4*x*ws*mp.diff(G,args,(1,0,1))+4*x*x*ws*ws*mp.diff(G,args,(0,0,2))+(2*ws+4*x*x*wss)*gw
  values=[G(*args),gx,gy,gxx]
  return dict(values=[float(z)for z in values],decimal=[mp.nstr(z,dps-10)for z in values],root_residual=mp.nstr(16*s*w**4+w-1,12),w=mp.nstr(w,dps-10))
