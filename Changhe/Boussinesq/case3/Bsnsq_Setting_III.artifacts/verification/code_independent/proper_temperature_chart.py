"""Independent global chart evaluator from a temperature, for checks only.

Uses scalar root inversion, adaptive physical-y quadrature, analytic first
field derivatives and Cartesian seven-point differences of q_x. It imports
no fitting-lane code and imposes no full-plane inverse closure.
"""
from functools import lru_cache
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad_vec
from finite_difference import stencil

class TemperatureChart:
 def __init__(self,state=None,gamma=0.):
  self.state=state;self.gamma=gamma;self.L=1. if state is None else state.L
  self.a0=1. if state is None else float(state.Fs(0.)[0]);assert self.a0>0
  if state is not None:
   assert state.bb==3.;self.spline=state.Fs;self.dspline=state.Fs.derivative()
  self.nodes,self.weights=stencil();self.max_quad_error=0.;self.quad_failures=0;self.max_root_error=0.;self.integral_calls=0
 def qdata(self,x,y):
  r=np.hypot(x,y)
  if r==0:return np.array([0.,1.,0.])
  z=np.exp(-np.log1p((r/self.L)**2)/6);t=-np.expm1(-np.log1p((r/self.L)**2)/6);rho=r/np.hypot(r,self.L);eta=-y/r;cx=x/r;sy=y/r
  if self.state is None:P=np.ones(1);DP=np.zeros(1)
  else:P=self.spline(t);DP=self.dspline(t)
  T=np.ones(len(P));D=np.zeros(len(P))
  if len(P)>1:T[1]=eta;D[1]=1.
  for k in range(2,len(P)):T[k]=2*eta*T[k-1]-T[k-2];D[k]=2*T[k-1]+2*eta*D[k-1]-D[k-2]
  E=P[::2]@T[::2];O=P[1::2]@T[1::2];A=E+rho*O
  At=DP[::2]@T[::2]+rho*(DP[1::2]@T[1::2]);Ae=P[::2]@D[::2]+rho*(P[1::2]@D[1::2])
  F=z**5*A;assert F>0
  rFr=z**5*(z*(1-z**6)*At/3+rho*z**6*O-5*(1-z**6)*A/3)
  Fe=z**5*Ae;Fx=cx*(rFr-eta*Fe)/r;Fy=(sy*rFr-cx*cx*Fe)/r
  sqrtF=np.sqrt(F/self.a0);return np.array([x*sqrtF,sqrtF*(1+x*Fx/(2*F)),x*sqrtF*Fy/(2*F)])
 @lru_cache(maxsize=20000)
 def X(self,q,y):
  if q==0:return 0.
  if q<0:return -self.X(-q,y)
  hi=max(1.,q)
  for k in range(100):
   if self.qdata(hi,y)[0]>=q:break
   hi*=2
  else:raise RuntimeError('No root bracket')
  x=brentq(lambda xx:self.qdata(xx,y)[0]-q,0.,hi,xtol=1e-12,rtol=3e-14)
  self.max_root_error=max(self.max_root_error,abs(self.qdata(x,y)[0]-q)/(1+q));return float(x)
 def mixed_data(self,q,y):
  x=self.X(float(q),float(y));v=self.qdata(x,y);assert v[1]>0
  J=1/v[1];Xy=-v[2]/v[1]
  if q==0:Xqq=0.
  else:
   h=1e-4*max(1.,np.hypot(x,y));qxx=sum(w*self.qdata(x+h*z,y)[1] for z,w in zip(self.nodes,self.weights))/h;Xqq=-qxx/v[1]**3
  return np.array([x,J,Xqq,Xy])
 @lru_cache(maxsize=4096)
 def integrals(self,q,y):
  if y==0:return np.zeros(3)
  def integrand(v):return self.mixed_data(q,float(v))[:3]
  ans,err,info=quad_vec(integrand,0.,y,epsabs=2e-9,epsrel=2e-9,limit=160,full_output=True)
  self.max_quad_error=max(self.max_quad_error,float(err));self.quad_failures+=int(not info.success);self.integral_calls+=1
  if not info.success:raise RuntimeError('Chart integral failed')
  return ans
 def S_eta(self,q,y):
  ans=self.integrals(float(q),float(y));return ans+np.array([self.gamma*q**3,3*self.gamma*q*q,6*self.gamma*q])
 def physical(self,x,y,beta=3.):
  q,qx,qy=self.qdata(x,y);S,eta,etaq=self.S_eta(q,y);_,J,_,Xy=self.mixed_data(q,y);p=beta/2-1;mu=3*beta/2+1
  V=(mu*eta-p*q*etaq)/J;W=np.array([p*q*J+Xy*V,V]);psi=2*beta*S-p*q*eta-beta*y*x
  return {'q':q,'eta':eta,'S':S,'J':J,'W':W,'psi':psi,'Theta':self.a0*q*q}
