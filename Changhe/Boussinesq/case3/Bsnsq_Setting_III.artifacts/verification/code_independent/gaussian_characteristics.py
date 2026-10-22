"""Independent exact-Gaussian velocity and adaptive two-pass characteristics.
No numerics-lane code, modal inverse, fixed-step RK4, or spline fit is used.
The forcing parameter is epsilon=0. These are NOT self-consistent B2 profiles.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

class GaussianFlow:
 def __init__(self,c=2.5,y0=2.85,s=1.):
  self.c=c;self.beta=2*(c-1);self.y0=y0;self.s=s;self.a=1/(2*s*s)
  _,bp,bpp=self.B(y0*y0);self.A=c/(-2*s**4*y0*bp);self.fac=self.A*s**4
  self.u0=self.fac*self.B(y0*y0)[0];self.lam=(self.beta-2)/2;self.mu=1+1.5*self.beta
  if self.beta<=2:raise ValueError('This source-seeded construction requires beta>2.')
  self.ax_y0=-2*self.fac*(bp+2*y0*y0*bpp)
  self.f01=-2*self.ax_y0/self.mu;self.b0=4/self.beta;self.g01=(2*self.f01-self.ax_y0*self.b0)/(2*self.beta+1)
 def B(self,S):
  z=self.a*S
  if z<.03:
   # b(z)=(1-exp(-z))/z, with twelve Taylor powers.
   val=first=second=0.
   for k in range(12,-1,-1):
    val=val*z+(-1.)**k/math.factorial(k+1)
   for k in range(12,0,-1):
    first=first*z+k*(-1.)**k/math.factorial(k+1)
   for k in range(12,1,-1):
    second=second*z+k*(k-1)*(-1.)**k/math.factorial(k+1)
   return self.a*val,self.a**2*first,self.a**3*second
  e=math.exp(-z);return -math.expm1(-z)/S,((z+1)*e-1)/S**2,(2-(z*z+2*z+2)*e)/S**3
 def field(self,X):
  x,y=map(float,X);Y=y-self.y0;B,bp,bpp=self.B(x*x+Y*Y);a=self.fac
  u=np.array([-2*a*x*Y*bp,a*(B+2*x*x*bp)])
  J=np.array([[-2*a*Y*(bp+2*x*x*bpp),-2*a*x*(bp+2*Y*Y*bpp)],
              [a*(6*x*bp+4*x**3*bpp),2*a*Y*(bp+2*x*x*bpp)]])
  W=self.beta*np.array([x,y])+u-np.array([0.,self.u0]);DW=J+self.beta*np.eye(2)
  return u,W,J,DW
 def velocity(self,points):
  return np.array([self.field(q)[0]-np.array([0.,self.u0]) for q in np.asarray(points)])
 def external_omega(self,x,y):
  x,y=np.broadcast_arrays(x,y);return self.A*x*np.exp(-(x*x+(y-self.y0)**2)/(2*self.s*self.s))
 def psi(self,x,y):
  x,y=np.broadcast_arrays(x,y);v=np.array([self.fac*xx*self.B(xx*xx+(yy-self.y0)**2)[0]-self.u0*xx for xx,yy in zip(x.ravel(),y.ravel())]);return v.reshape(x.shape)
 def evaluate(self,point,r_in=1e-3,rtol=2e-9,max_time=220.):
  X=np.asarray(point,dtype=float);sgn=1. if X[0]>=0 else -1.;X=X.copy();X[0]=abs(X[0]);radius=float(np.linalg.norm(X))
  if radius<=r_in:
   x,y=X;theta=x*x*(1+self.f01*y);grad=np.array([2*x*(1+self.f01*y),x*x*self.f01]);om=x*(self.b0+self.g01*y)
   return {'Theta':theta,'Omega':sgn*om,'gradient':(grad*np.array([sgn,1.])).tolist(),'T':0.,'endpoint':X.tolist(),'back_nfev':0,'forward_nfev':0,'status':'LOCAL_JET'}
  def backward(t,z):return -self.field(z)[1]
  def event(t,z):return np.linalg.norm(z)-r_in
  event.terminal=True;event.direction=-1
  back=solve_ivp(backward,(0,max_time),X,method='DOP853',rtol=rtol,atol=max(1e-15,r_in*rtol*.01),events=event,dense_output=True)
  if not back.success or len(back.t_events[0])!=1:return {'status':'UNFINISHED','message':back.message,'last':back.y[:,-1].tolist(),'T':float(back.t[-1]),'back_nfev':back.nfev}
  T=float(back.t[-1]);xe,ye=back.y[:,-1]
  initial=np.array([2*(1+self.f01*ye),xe*self.f01,self.b0+self.g01*ye])
  def forward(t,z):
   q=back.sol(T-t);DW=self.field(q)[3];dg=(self.beta-2)*z[:2]-DW.T@z[:2]
   return np.array([dg[0],dg[1],-z[2]+z[0]])
  front=solve_ivp(forward,(0,T),initial,method='DOP853',rtol=rtol,atol=rtol*.001)
  grad=xe*front.y[:2,-1];om=xe*front.y[2,-1];theta=xe*xe*(1+self.f01*ye)*math.exp((self.beta-2)*T)
  return {'Theta':float(theta),'Omega':float(sgn*om),'gradient':(grad*np.array([sgn,1.])).tolist(),'T':T,'endpoint':[float(xe),float(ye)],'back_nfev':back.nfev,'forward_nfev':front.nfev,'status':'COMPLETE' if front.success else 'FORWARD_FAILED'}
