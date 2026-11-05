#!/usr/bin/env python3
"""FLOAT Phi_a=R J^(-delta) psi_a for psi_a=a*h0(ax)*h1(ay).

Heat quadrature uses generalized Gauss-Laguerre; this numerical field evaluator
is NOT a certificate. Its Fourier L2 Gram is independently enclosed by Arb.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.special import roots_genlaguerre,roots_legendre,gammaln,hyp1f1
from flint import arb,ctx


def radial_modes(r,alpha=1.,delta=.1,nodes=128,method='power-gauss'):
 r=np.asarray(r,dtype=float)
 if method=='laguerre':
  t,w=roots_genlaguerre(nodes,delta/2-1);w=w*np.exp(-gammaln(delta/2))
 else:
  z,w=roots_legendre(nodes);z=z+1
  # t=z^(2/delta), with dt*t^(delta/2-1)=2/delta dz.
  # For delta=.1 the transformed integrand is analytic at z=0.
  t=z**(2/delta);w=w*np.exp(-t-gammaln(1+delta/2))
 d=1+2*alpha*alpha*t
 s=alpha*r[...,None]/np.sqrt(d)
 x=-s*s/2;pref=alpha*d**(-1.5)*w
 c0=np.sum(pref*.5*hyp1f1(1.5,1,x),axis=-1)
 c2=np.sum(pref*(3*s*s/16)*hyp1f1(2.5,3,x),axis=-1)
 return {('r1','s',2):-c2,('r2','c',0):c0,('r2','c',2):c2}


def radial_modes_width(r,width=1.,delta=.1,nodes=128,method='power-gauss'):
 return radial_modes(r,alpha=1/width,delta=delta,nodes=nodes,method=method)


def fields(x,y,alpha=1.,delta=.1,nodes=128,method='power-gauss'):
 x,y=np.broadcast_arrays(np.asarray(x),np.asarray(y));r=np.sqrt(x*x+y*y);theta=np.arctan2(y,x)
 z=radial_modes(r,alpha,delta,nodes,method)
 return z['r1','s',2]*np.sin(2*theta),z['r2','c',0]+z['r2','c',2]*np.cos(2*theta)


def laguerre_radial_modes(r,width=.015,m=1,k=1,delta=.1,nodes=256):
 """FLOAT R J^-delta of normalized polar Laguerre Gaussian.
 psi=sqrt(2*k!/(pi*(k+m)!))*width^(-m-1)*r^m
      *L_k^m(r²/width²)*exp(-r²/(2width²))*sin(m theta).
 """
 import math
 r=np.asarray(r,dtype=float)
 z,w=roots_legendre(nodes);z=z+1;t=z**(2/delta)
 w=w*np.exp(-t-gammaln(1+delta/2))
 beta=width*width/2+t
 N=np.exp((np.log(2/np.pi)+gammaln(k+1)-gammaln(k+m+1))/2)
 out={}
 for ell in [m-1,m+1]:
  val=np.zeros(r.shape)
  for j in range(k+1):
   p=m+2*j;A=(p+ell+2)/2
   coeff=(-1)**j*math.comb(k+m,k-j)/math.factorial(j)*width**(m+1+2*j)*N
   pre=np.exp(gammaln(A)-(ell+1)*np.log(2)-A*np.log(beta)-gammaln(ell+1))
   rr=r[...,None]
   radial=rr**ell*pre*hyp1f1(A,ell+1,-rr*rr/(4*beta))
   val+=coeff*np.sum(w*radial,axis=-1)/2
  if ell==m-1:
   if ell>0:out['r1','s',ell]=(-1)**k*val
   out['r2','c',ell]=(-1)**k*val
  else:
   out['r1','s',ell]=(-1)**(k+1)*val
   out['r2','c',ell]=(-1)**k*val
 return out


def gram(alphas,delta='1/10',bits=256):
 ctx.prec=bits;dd=Q(delta);dd=arb(dd.numerator)/dd.denominator
 aa=[arb(Q(a).numerator)/Q(a).denominator for a in alphas]
 B=[]
 for a in aa:
  row=[]
  for b in aa:
   beta=(1/(a*a)+1/(b*b))/2
   v=beta.hypgeom_u(2,3-dd)/(a*a*b*b)
   row.append(v.str(70))
  B.append(row)
 return {'status':'RIGOROUS_ARB_L2_GRAM','definition':'B_ij=<R J^-delta psi_ai,R J^-delta psi_aj>, psi_a=a*h0(ax)*h1(ay)','delta':str(delta),'alphas':list(alphas),'B':B,'formula':'B_ij=U(2,3-delta,(ai^-2+aj^-2)/2)/(ai²aj²)','bits':bits}

def laguerre_gram(tests,delta='1/10',bits=256):
 """Rigorous L2 Gram for (physical_width,m,k) polar Laguerre tests."""
 import math
 ctx.prec=bits;dd=Q(delta);dd=arb(dd.numerator)/dd.denominator
 def aq(x):x=Q(x);return arb(x.numerator)/x.denominator
 B=[]
 for width,m,k in tests:
  a=aq(width);Ni=(2*arb(math.factorial(k))/(arb.pi()*math.factorial(k+m))).sqrt();row=[]
  for widthj,mj,kj in tests:
   if mj!=m:row.append('0');continue
   b=aq(widthj);Nj=(2*arb(math.factorial(kj))/(arb.pi()*math.factorial(kj+m))).sqrt();beta=(a*a+b*b)/2
   v=arb(0)
   for i in range(k+1):
    for j in range(kj+1):
     A=m+i+j+1
     ci=Q((-1)**i*math.comb(k+m,k-i),math.factorial(i));cj=Q((-1)**j*math.comb(kj+m,kj-j),math.factorial(j))
     v+=aq(ci*cj)*a**(2*i)*b**(2*j)*math.factorial(A-1)*beta.hypgeom_u(A,A+1-dd)
   v*=(-1)**(k-kj)*arb.pi()/2*Ni*Nj*a**(m+1)*b**(m+1)
   row.append(v.str(70))
  B.append(row)
 return {'status':'RIGOROUS_ARB_L2_GRAM','delta':str(delta),'tests':[list(t)for t in tests],'B':B,'bits':bits}


if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 rr=np.geomspace(1e-5,1000,200)
 errors={}
 for a in [10.,5.,2.5]:
  u=radial_modes(rr,a,nodes=128);v=radial_modes(rr,a,nodes=256)
  errors[str(a)]=max(float(np.max(np.abs(u[k]-v[k]))) for k in u)
 z=gram(['10','5','5/2']);z['FLOAT_power_Gauss_n128_n256_max_difference']=errors
 args.output.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
