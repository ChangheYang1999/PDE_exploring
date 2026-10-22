"""Manufactured controls with independent 70-digit incomplete-beta values."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json
import mpmath as mp
import numpy as np
from axis_cutoff_functional import functional
mp.mp.dps=70;start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'states':[]}
root=Path('research/112_axis_cutoff_normalization/verification');root.mkdir(exist_ok=True)
for beta in [2.1,3.,7.]:
 mu=1.5*beta+1.;a0=1.3
 for rel in [.98,1.,1.02]:
  k=mu*rel
  def v_ratio(t):
   z=np.exp(2*t);return k*(1+z)/(1+(k/beta)*z)
  for eps in [1e-3,1e-6,1e-9]:
   radii=[1.,1e3,1e6,1e12]
   num=functional(v_ratio,beta,a0,eps,radii)
   b=mp.mpf(str(beta));m=mp.mpf(str(mu));kk=mp.mpf(str(k));ee=mp.mpf(str(eps));a=mp.mpf(str(a0))
   ell=m/b;rho=(b+1)/m;P=(2*b+1)/m;e=1-m/kk;tau=(m/b-m/kk)/2
   Ce=ee**e*(1+ee**2)**(-tau);aa=(1-(b+1)/kk)/2;bb=1/(2*b)
   vals=[]
   for rr0 in radii:
    rr=mp.mpf(str(rr0));cr=Ce*(1+rr**(-2))**tau
    lo=ee**2/(1+ee**2);hi=rr**2/(1+rr**2)
    ir=ee**(1-rho)/(1-rho)+Ce**(-rho)/2*mp.betainc(aa,bb,lo,hi)
    val=2*a*b/m**2*cr**(-P)*ir;vals.append(val)
   errors=[abs(float(y)/x-1) for x,y in zip(num['Q_raw'],vals)]
   assert max(errors)<2e-9,(beta,k,eps,errors)
   infI=ee**(1-rho)/(1-rho)+Ce**(-rho)/2*mp.betainc(aa,bb,ee**2/(1+ee**2),1)
   qinf=2*a*b/m**2*Ce**(-P)*infI
   out['states'].append({'beta':beta,'k':k,'epsilon':eps,'h':float(2-2*m/kk),'max_relative_error':max(errors),
    'exact_Q_finite':[mp.nstr(z,32) for z in vals],'exact_Q_infinite':mp.nstr(qinf,32),'computed':num})
# At smaller inner cutoffs the exact normalized diagnostic has power epsilon^-h.
for beta in [2.1,3.,7.]:
 for rel in [.98,1.02]:
  data=[a for a in out['states'] if a['beta']==beta and abs(a['k']/(1.5*beta+1)-rel)<1e-12]
  observed=np.log(float(data[-1]['exact_Q_infinite'])/float(data[-2]['exact_Q_infinite']))/np.log(data[-1]['epsilon']/data[-2]['epsilon'])
  expected=-data[-1]['h']
  # Analytic fill error is lower order; its finite-epsilon convergence can be slow.
  out.setdefault('power_controls',[]).append({'beta':beta,'relative_slope':rel,'observed':observed,'expected_limit':expected,'difference':observed-expected})
out.update(status='CONFIRMED',elapsed_seconds=time.monotonic()-start)
(root/'manufactured_tests.json').write_text(json.dumps(out,indent=2)+'\n')
print('CONFIRMED',len(out['states']),'finite-cutoff manufactures; max relative',max(s['max_relative_error'] for s in out['states']),'seconds',out['elapsed_seconds'])
