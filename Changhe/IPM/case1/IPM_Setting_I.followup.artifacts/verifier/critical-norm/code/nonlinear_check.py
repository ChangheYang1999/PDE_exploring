"""Independent floating check of the nonlinear critical-norm construction.
No finite-part samples or linearized B response are substituted for B[wN]-B[w0].
The convergent difference of the exact integrands is evaluated in logarithmic coordinates.
This is a diagnostic calculation, not the proof in PROOF.md.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math,time
from functools import lru_cache
import numpy as np
from scipy.special import expit,roots_jacobi
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
A=4.;beta=2/A;r0=.125;p=7+beta

def chi(t):
 t=np.asarray(t);c=np.zeros_like(t);d=np.zeros_like(t);dd=np.zeros_like(t)
 c[t>=1]=1.;inside=(t>0)&(t<1);u=t[inside]
 h=expit(1/(1-u)-1/u);v=h*(1-h);l1=1/(1-u)**2+1/u**2;l2=2/(1-u)**3-2/u**3
 c[inside]=h;d[inside]=v*l1;dd[inside]=v*(l2+(1-2*h)*l1*l1)
 return c,d,dd

def cutoff(t,N):
 a,ap,app=chi(t);b,bp,bpp=chi(N+2-np.asarray(t))
 return a*b,ap*b-a*bp,app*b-2*ap*bp+a*bpp

@lru_cache(None)
def nodes(order):return np.polynomial.legendre.leggauss(order)

def gauss(f,a,b,order):
 if b<=a:return 0.
 z,w=nodes(order);u=(a+b)/2+(b-a)*z/2
 return (b-a)/2*float(w@f(u))

def eta(t,N,order):
 x=r0*math.exp(-t);an=float(cutoff(t,N)[0]);f=(1-x*x)/(1+x*x)
 sigma=-x**(6+beta)*an/(N*A*f)
 end=min(18.,max(0.,N+2-t));breaks=sorted(set([0.,end]+[a for a in [1-t,N+1-t] if 0<a<end]))
 def integrand(s):
  u=x*np.exp(-s);aa=cutoff(t+s,N)[0];ff=(1-u*u)/(1+u*u);sig=-u**(6+beta)*aa/(N*A*ff)
  return np.exp(-(6+beta)*s)*aa/(ff*ff*(1+sig))
 J=sum(gauss(integrand,a,b,order) for a,b in zip(breaks,breaks[1:]))
 # This is the exact density-ratio formula, with a numerically negligible
 # exponential tail only if the optional cutoff at s=18 was used.
 e=math.log1p(sigma)+x**(6+beta)*J/(N*A)
 return e,sigma

def compute(N,order):
 start=time.monotonic();e0,_=eta(0,N,order)
 qL=2-4*A;dqL=2*math.expm1(-2*e0)-4*A*math.expm1(-3*e0)
 def inner_scalar(t):
  x=r0*math.exp(-t);a,at,att=(float(z) for z in cutoff(t,N));v=x**p*a/N;vp=x**(p-1)*(p*a-at)/N;vpp=x**(p-2)*(p*(p-1)*a-(2*p-1)*at+att)/N
  w0=-A*x*(1-x*x)/(1+x*x);wp=-A*(1-4*x*x-x**4)/(1+x*x)**2
  e,sig=eta(t,N,order);sp=vp/w0-v*wp/(w0*w0);ep=sp/(1+sig)+A*v/(w0*w0*(1+sig))
  g=x*x/(1+x*x);gp=(1+x*x)/x**5;wpiece=-2*A*(3-x*x)/x**5;q0=gp+wpiece
  dq=gp*math.expm1(-2*e)+wpiece*math.expm1(-3*e)+ep*math.exp(-2*e)/(2*g*g)-vpp*math.exp(-3*e)/(2*g**3)
  omega=(beta-2)*math.log1p(sig)-(beta-1)*e
  W=A**(beta-2)*x**(-beta)*(1-x*x)**(beta-2)*(1+x*x)
  # The integrable source-value difference at x=0 is integrated separately.
  return x*W*(dq*math.exp(omega)+(q0-qL-dqL)*math.expm1(omega))
 points=[0.,1.,float(N+1),float(N+2)]
 inner=sum(gauss(lambda ts:np.array([inner_scalar(t) for t in ts]),a,b,order) for a,b in zip(points,points[1:]))
 Wint=quad(lambda x:A**(beta-2)*x**(-beta)*(1-x*x)**(beta-2)*(1+x*x),0,r0,epsabs=1e-12,epsrel=1e-12,limit=150)[0]
 inner-=dqL*Wint
 # Factored endpoint differences avoid cancellation and leave the known
 # integrable source weight (1-x)^(beta-1) for Gauss-Jacobi quadrature.
 z,w=roots_jacobi(order,beta-1,0);x=(1+r0)/2+(1-r0)*z/2
 Wregular=A**(beta-2)*x**(-beta)*(1+x)**(beta-2)*(1+x*x)
 gp=(1+x+2*x*x+2*x**3+2*x**4)/x**5
 wpiece=-2*A*(3+3*x+2*x*x+2*x**3+2*x**4)/x**5
 f=Wregular*(gp*math.expm1(-(beta+1)*e0)+wpiece*math.expm1(-(beta+2)*e0))
 tail=((1-r0)/2)**beta*float(w@f)
 Bdiff=(beta-1)*A**(1-beta)*(inner+tail)/3
 kappa=(1-beta)*(6+beta)*(7+beta)/(6*A)
 grid=np.linspace(0,N+2,10001);a,at,att=cutoff(grid,N);seminorm=(np.max(abs(a))+np.max(abs(p*a-at))+np.max(abs(p*(p-1)*a-(2*p-1)*at+att)))/N
 return {'N':N,'order':order,'nonlinear_B_difference':Bdiff,'kappa':kappa,'ratio_to_kappa':Bdiff/kappa,'leading_ratio':1+1/N,'N_times_error_from_log_leading':N*(Bdiff-kappa*(1+1/N)),'sampled_critical_norm':seminorm,'source_log_density_ratio':e0,'seconds':time.monotonic()-start}

if __name__=='__main__':
 out={'date_start':datetime.now(timezone.utc).isoformat(),'A':A,'beta':beta,'L':1,'r0':r0,'scope':'Floating evaluation of the convergent nonlinear integrand difference, not a certificate. The theorem is proved independently in PROOF.md.','rows':[]}
 for N in [4,8,16,32]:
  pair=[compute(N,o) for o in [48,80]];out['rows'].append({'passes':pair,'difference':pair[1]['nonlinear_B_difference']-pair[0]['nonlinear_B_difference']});print(json.dumps(out['rows'][-1]),flush=True)
  (ROOT/'verification/nonlinear.json').write_text(json.dumps(out,indent=2)+'\n')
 out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat();(ROOT/'verification/nonlinear.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['date_end'],flush=True)
