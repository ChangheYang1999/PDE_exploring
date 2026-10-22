"""Independent shifted-power forcing and transported fields, NOT a B2 profile.
The exact analytic argument was written first in research/29. Only verifier
code is reused: adaptive two-pass characteristics, never fitting-lane code.
"""
import math
import numpy as np
from gaussian_characteristics import GaussianFlow

class ShiftedPowerFlow(GaussianFlow):
 def __init__(self,beta=3.):
  if beta<=2:raise ValueError('Strict source beta>2 required')
  self.beta=float(beta);self.c=1+beta/2;self.lam=(beta-2)/2;self.mu=1+1.5*beta
  self.p=(beta-1)/(2*beta);self.L=3*self.c*math.sqrt(beta)/4;self.h=math.sqrt(beta)*self.L
  self.S0=self.L**2+self.h**2;self.Bamp=self.c/(2*self.p*self.h*self.S0**(self.p-1))
  self.u0=-self.Bamp*self.S0**self.p;self.b0=4/beta;self.f01=self.g01=self.ax_y0=0.
 def field(self,X):
  x,y=map(float,X);z=y-self.h;S=self.L**2+x*x+z*z;p=self.p;B=self.Bamp
  F=2*B*p*S**(p-1)
  u=np.array([F*x*z,-B*S**p-F*x*x])
  dS=x*x+y*y-2*y*self.h
  diff=self.S0**p*math.expm1(p*math.log1p(dS/self.S0))
  W=np.array([x*(self.beta+F*z),self.beta*y-B*diff-F*x*x])
  J11=F*z*(1+2*(p-1)*x*x/S)
  J=np.array([[J11,F*x*(1+2*(p-1)*z*z/S)],[-F*x*(3+2*(p-1)*x*x/S),-J11]])
  return u,W,J,J+self.beta*np.eye(2)
 def velocity(self,points):
  points=np.atleast_2d(np.asarray(points,dtype=float))
  return np.array([self.field(q)[1]-self.beta*q for q in points])
 def psi(self,x,y):
  x,y=np.broadcast_arrays(x,y);dS=x*x+y*y-2*self.h*y
  return -self.Bamp*x*self.S0**self.p*np.expm1(self.p*np.log1p(dS/self.S0))
 def external_omega(self,x,y):
  x,y=np.broadcast_arrays(x,y);ss=x*x+(y-self.h)**2;S=self.L**2+ss
  return 4*self.Bamp*self.p*x*S**(self.p-2)*(2*self.L**2+(self.p+1)*ss)
 def external_qprime0(self):
  return 8*self.Bamp*self.p*(1-self.p)*self.h*self.S0**(self.p-3)*(3*self.L**2+(self.p+1)*self.h**2)
