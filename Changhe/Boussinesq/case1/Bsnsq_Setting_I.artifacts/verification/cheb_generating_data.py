"""Data-only beta3 G evaluator using scalar Chebyshev derivative recurrences.

Independent of the authors' multivariate Taylor jets. Intended rational beta3
exponents are used with long-double arithmetic. A global positive chart is not
assumed from finite evaluations; failed inverse queries are reported.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import numpy as np
LD=np.longdouble

def cheb_derivatives(z,n):
 z=np.asarray(z);T=np.zeros((3,n+1,z.size),dtype=z.dtype);T[0,0]=1
 if n:
  T[0,1]=z;T[1,1]=1
 for k in range(2,n+1):
  T[0,k]=2*z*T[0,k-1]-T[0,k-2]
  T[1,k]=2*T[0,k-1]+2*z*T[1,k-1]-T[1,k-2]
  T[2,k]=4*T[1,k-1]+2*z*T[2,k-1]-T[2,k-2]
 return T

class Model:
 def __init__(self,source):
  self.source=str(source);self.sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest()
  with np.load(source,allow_pickle=False) as d:
   self.J=int(d['J']);self.K=int(d['Kw']);self.c=np.asarray(d['c'],dtype=LD).reshape(self.J+1,self.K+1)
   self.a=LD(d['a0']);self.alpha=LD(d['alpha']) if 'alpha' in d.files else LD(0);self.alpha_recorded='alpha' in d.files
   if float(d['beta'])!=3 or int(d['m'])!=3:raise ValueError('beta3 only')
  self.h=sum(((-1)**k)*Fraction.from_float(float(v)) for row in self.c for k,v in enumerate(row))
  if self.h<=0:raise ValueError('Nonpositive center chart')
 def polynomial(self,t,w):
  tr=cheb_derivatives(2*t-1,self.J);tw=cheb_derivatives(2*w-1,self.K)
  D=[self.c.T@tr[k]*(2**k) for k in range(3)]
  return dict(P=np.sum(D[0]*tw[0],axis=0),Pt=np.sum(D[1]*tw[0],axis=0),Pw=2*np.sum(D[0]*tw[1],axis=0),Ptt=np.sum(D[2]*tw[0],axis=0),Ptw=2*np.sum(D[1]*tw[1],axis=0),Pww=4*np.sum(D[0]*tw[2],axis=0))
 def mixed(self,x,e):
  x,e=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD));shape=x.shape;x=x.ravel();e=e.ravel()
  E=1+x*x+e**6;q=LD(1)/3;T=E**(-LD(1)/6);w=e*e*E**(-q)
  if self.alpha==0:t=T;ell=-T/6;ell2=T/36
  else:
   aa=self.alpha;ea=np.expm1(aa);D=1+(1-T)*ea;t=1-np.log1p((1-T)*ea)/aa
   ell=-ea*T/(6*aa*D);ell2=ea*np.exp(aa)*T/(36*aa*D*D)
  z=self.polynomial(t,w);P,Pt,Pw,Ptt,Ptw,Pww=[z[k] for k in ['P','Pt','Pw','Ptt','Ptw','Pww']]
  H1=q*P+ell*Pt-w*Pw/3
  LH1=q*(ell*Pt-w*Pw/3)+ell2*Pt+ell*ell*Ptt-2*ell*w*Ptw/3+w*Pw/9+w*w*Pww/9
  f=E**q*P;fE=E**(q-1)*H1;fEE=E**(q-2)*((q-1)*H1+LH1)
  fe=2*e*Pw;fEe=2*e/E*((q-LD(1)/3)*Pw+ell*Ptw-w*Pww/3)
  y=e*(f+2*x*x*fE);A=f+2*x*x*fE+e*(6*e**5*(fE+2*x*x*fEE)+fe+2*x*x*fEe)
  B=e*(6*x*fE+4*x**3*fEE)
  Psi=x*e*E**q*(6*ell*(1-1/E)*Pt-2*P/E+2*w*Pw/E)
  out=dict(x=x,eta=e,y=y,A=A,B0=B,Psi=Psi,G=x*e*f,Theta=self.a*e,Theta_x=-self.a*B/A,Theta_y=self.a/A,normalized_A=A/E**q)
  return {k:np.asarray(v).reshape(shape) for k,v in out.items()}
 def invert(self,x,y,tol=LD('3e-17'),maxiter=90):
  x,y=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(y,dtype=LD));shape=x.shape;xx=abs(x.ravel());target=abs(y.ravel());sign=np.sign(y.ravel())
  lo=np.zeros_like(target);hi=np.maximum(LD(1),2*np.cbrt(target));bracket=np.zeros_like(target,dtype=bool)
  for _ in range(35):
   z=self.mixed(xx,hi);bracket=z['y']>=target
   if np.all(bracket):break
   hi[~bracket]*=2
  if not np.all(bracket):raise RuntimeError('Could not bracket physical y')
  eta=np.minimum(target/LD(float(self.h)),hi/2);ok=np.zeros_like(target,dtype=bool)
  for it in range(maxiter):
   z=self.mixed(xx,eta);err=z['y']-target
   if np.any(z['A']<=0):raise RuntimeError('Nonpositive chart encountered in local inverse query')
   ok=abs(err)<=tol*(1+target)
   if np.all(ok):break
   lo=np.where(err<0,eta,lo);hi=np.where(err>=0,eta,hi)
   trial=eta-err/z['A'];trial=np.where((trial>lo)&(trial<hi),trial,(lo+hi)/2)
   eta=np.where(ok,eta,trial)
  if not np.all(ok):raise RuntimeError('Physical inverse tolerance not reached: '+str(float(np.max(abs(err)/(1+target)))))
  eta=(eta*sign).reshape(shape);return eta,{'iterations':it+1,'max_scaled_y_defect':float(np.max(abs(err)/(1+target)))}
 def physical(self,x,y):
  eta,diagnostic=self.invert(x,y);z=self.mixed(x,eta);return z,diagnostic
