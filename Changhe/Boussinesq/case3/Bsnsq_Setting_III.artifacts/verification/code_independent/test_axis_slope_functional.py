"""Independent axis ODE integration and tail functional, packet107."""
from pathlib import Path
from fractions import Fraction as Q
import time,json,math
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
start=time.monotonic();mp.mp.dps=60;out={'exact':[],'states':[]}
for beta0 in ['2.01','2.5','3','8','100']:
 bq=Q(beta0);muq=3*bq/2+1;ellq=muq/bq;Pq=(2*bq+1)/muq;rhoq=(bq+1)/muq
 assert Pq+rhoq==2 and ellq*rhoq==1+1/bq and Pq*(ellq-1)+1-rhoq==1+1/bq
 out['exact'].append({'beta':beta0,'exponent_identities':True})
 b=mp.mpf(beta0);mu=3*b/2+1;ell=mu/b;alpha=1/b;P=(2*b+1)/mu;rho=(b+1)/mu;tau=(ell-1)/2;a0=mp.mpf('1.3');m=1/(2*ell)
 qbase=a0*b/mu**2*mp.beta(m/2,alpha/2)
 for L0 in ['.5','1','3']:
  L=mp.mpf(L0);Qexact=qbase*L**(1+alpha)
  # Independent integral using s=exp(t), removes endpoint singularities.
  def zeta(r):return r*(1+(r/L)**2)**tau
  fun=lambda t:mp.exp((1-rho)*t)*(1+mp.exp(2*t)/L**2)**(-tau*rho)
  integ=mp.quad(fun,[-mp.inf,-2,0,2,mp.inf]);C=L**(1-ell);Qquad=2*a0*b/mu**2*C**(-P)*integ
  assert abs(Qquad/Qexact-1)<mp.mpf('1e-35'),(beta0,L0,Qquad,Qexact)
  bf=float(b);muf=float(mu);lf=float(ell);Lfloat=float(L);a0f=float(a0)
  def rhs(t,Y):
   r=math.exp(t);z=(r/Lfloat)**2;v=muf*r*(1+z)/(1+lf*z);vp=muf*((1+z)/(1+lf*z)+2*z*(1-lf)/(1+lf*z)**2);a,g=Y
   return [r/v*(2*vp-2*muf)*a,r/v*(2*a-(2*bf+1-vp)*g)]
  ts=np.log(np.array([1e-5,.01,.2,1,10,1e3,1e6])*Lfloat)
  sol=solve_ivp(rhs,(math.log(1e-8*Lfloat),float(ts[-1])),[a0f,4*a0f/bf],method='DOP853',t_eval=ts,rtol=2e-11,atol=1e-15);assert sol.success
  discrepancies=[]
  for tt,ag in zip(sol.t,sol.y.T):
   rr=mp.exp(float(tt));v=mu*rr*(1+(rr/L)**2)/(1+ell*(rr/L)**2);ze=zeta(rr);aa=a0*(v/(mu*ze))**2
   # regularize s^(-rho) by s=r*u^(1/(1-rho)).
   ii=rr**(1-rho)/(1-rho)*mp.quad(lambda u:(1+(rr/L)**2*u**(2/(1-rho)))**(-tau*rho),[0,mp.mpf('.5'),1])
   gg=2*a0/mu**2*v*ze**(-P)*ii;err=max(abs(float(aa)-ag[0])/max(1e-14,abs(float(aa))),abs(float(gg)-ag[1])/max(1e-14,abs(float(gg))));discrepancies.append(err)
  # Tail states can be below absolute tolerance; retain absolute and scaled errors.
  maxerr=max(discrepancies);assert maxerr<2e-5,(beta0,L0,maxerr)
  out['states'].append({'beta':beta0,'L':L0,'Q_exact_beta_integral':mp.nstr(Qexact,40),'Q_quadrature':mp.nstr(Qquad,40),'max_ODE_relative_error':maxerr,'nfev':sol.nfev,'rmax':math.exp(sol.t[-1]),'scaled_last_axis_g':float(sol.y[1,-1])*math.exp((1+float(alpha))*sol.t[-1])})
 for k in range(len(out['states'])-2,len(out['states'])):assert float(out['states'][k]['Q_exact_beta_integral'])>float(out['states'][k-1]['Q_exact_beta_integral'])
out['elapsed_seconds']=time.monotonic()-start;out['status']='CONFIRMED';Path('research/107_axis_slope_functional/verification/own_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(out['exact']),'exact identities',len(out['states']),'ODE/functional states','elapsed',out['elapsed_seconds'],flush=True)
