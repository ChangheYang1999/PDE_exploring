"""One-thread manufactured compact canonical extension, independent quadrature.
Polynomial cutoffs have enough global regularity for the admissible class and
are identically analytic near the center; the proof also permits C-infinity.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math,time
import numpy as np
from scipy.special import betainc,beta,eval_jacobi,roots_legendre
root=Path(__file__).resolve().parents[1]
class Field:
 def __init__(self,A=4.,X=5.,Y=2.,m=8):
  self.A=A;self.cl=(A+1)/2;self.k=np.sqrt(2/A);self.X=X;self.Y=Y;self.m=m;self.B=beta(m+1,m+1);self.H0=self.cl+A
  self.gn,self.gw=roots_legendre(32)
  self.HX=self.cl*X*X/2+A/self.k**2*(1-np.cos(self.k*X))
  self.I=float(self.HX+self._integrate_h(np.array([2*X]))[0])
 def power_derivative(self,t,n):
  m=self.m
  return (-1)**n*math.factorial(n)*t**(m-n)*(1-t)**(m-n)*eval_jacobi(n,m-n,m-n,2*t-1)
 def cutoff(self,x,R,d=0):
  x=np.asarray(x);a=np.abs(x);t=np.clip(2-a/R,0,1)
  if d==0:return betainc(self.m+1,self.m+1,t)
  val=self.power_derivative(t,d-1)/self.B*(-np.sign(x)/R)**d
  return np.where((a>R)&(a<2*R),val,0.)
 def h(self,x,d=0):
  x=np.asarray(x);k=self.k;A=self.A;c=self.cl
  f=[c*x+A/k*np.sin(k*x),c+A*np.cos(k*x),-A*k*np.sin(k*x)]
  return sum(math.comb(d,j)*f[j]*self.cutoff(x,self.X,d-j) for j in range(d+1))
 def J(self,y,d=0):
  y=np.asarray(y);ps=[y**3/6,y*y/2,y,np.ones_like(y)]
  return sum(math.comb(d,j)*ps[j]*self.cutoff(y,self.Y,d-j) for j in range(min(d,3)+1))
 def q(self,x,d=0):
  x=np.asarray(x);a=np.abs(x);t=np.clip(a/self.X-2,0,1)
  v=np.sign(x)**(d+1)*self.power_derivative(t,d)/(self.X**(d+1)*self.B)
  return np.where((a>2*self.X)&(a<3*self.X),v,0.)
 def Q(self,x):return betainc(self.m+1,self.m+1,np.clip(np.abs(x)/self.X-2,0,1))
 def _integrate_h(self,a):
  xx=self.X+(a[:,None]-self.X)*(self.gn[None,:]+1)/2
  return np.sum(self.h(xx)*self.gw[None,:],axis=1)*(a-self.X)/2
 def H(self,x):
  shape=np.shape(x);a=np.abs(x).ravel();o=np.empty_like(a)
  inner=a<=self.X;outer=a>=2*self.X;mid=~(inner|outer)
  o[inner]=self.cl*a[inner]**2/2+self.A/self.k**2*(1-np.cos(self.k*a[inner]))
  o[outer]=self.I
  ix=np.flatnonzero(mid)
  for n in range(0,len(ix),2048):
   jj=ix[n:n+2048];o[jj]=self.HX+self._integrate_h(a[jj])
  return o.reshape(shape)
 def rho(self,x,y):
  x,y=np.broadcast_arrays(np.asarray(x),np.asarray(y))
  shape=x.shape;xx=x.ravel();yy=y.ravel();out=np.zeros(xx.size)
  good=np.flatnonzero((abs(xx)<3*self.X)&(abs(yy)<2*self.Y))
  for a in range(0,len(good),32768):
   ii=good[a:a+32768];u=xx[ii];v=yy[ii];Q=self.Q(u);qp=self.q(u,1)
   out[ii]=(self.H0*(1-Q)-self.h(u,1)+self.I*qp)*self.J(v,2)+(self.I*Q-self.H(u))*self.J(v,4)-self.H0*qp*self.J(v)
  return out.reshape(shape)
 def U(self,x,y):
  j=self.H0*self.J(y)-self.I*self.J(y,2)
  jy=self.H0*self.J(y,1)-self.I*self.J(y,3)
  return np.array([-self.h(x)*self.J(y,3)-self.q(x)*jy,self.h(x,1)*self.J(y,2)+self.q(x,1)*j])
 def rho_x(self,x,y):
  j=self.H0*self.J(y)-self.I*self.J(y,2);jyy=self.H0*self.J(y,2)-self.I*self.J(y,4)
  return -self.h(x,2)*self.J(y,2)-self.h(x)*self.J(y,4)-self.q(x,2)*j-self.q(x)*jyy
 def rho_y(self,x,y):
  Q=self.Q(x);qp=self.q(x,1)
  return (self.H0*(1-Q)-self.h(x,1)+self.I*qp)*self.J(y,3)+(self.I*Q-self.H(x))*self.J(y,5)-self.H0*qp*self.J(y,1)
