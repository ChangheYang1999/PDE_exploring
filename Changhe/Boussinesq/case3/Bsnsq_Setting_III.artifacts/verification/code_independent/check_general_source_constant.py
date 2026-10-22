"""Checks of the noninteger finite-part source identity, independent implementation."""
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp,numpy as np,json,time,hashlib
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings
root=Path('research/98_constant_above_three/verification');start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'algebraic_checks':[],'inverse_checks':[]};mp.mp.dps=180
for bs in ['1.4','2.3','2.8','3.1','3.5','3.9','4.2','4.7']:
 b=mp.mpf(bs);N=int(mp.floor(b));L=mp.mpf('1.3');f=[mp.mpf(v) for v in ['1','.3','-.2','.07','-.011','.005','.0003']]
 C=-b*L**2/2*sum(a/(j+1-b) for j,a in enumerate(f))
 rem=mp.quad(lambda z:sum(a*z**(j-b) for j,a in enumerate(f) if j>=N),[0,mp.mpf('.01'),1])
 via=-b*L**2/2*(rem+sum(f[j]/(j+1-b) for j in range(N)))
 # Avoid endpoint-singular quadrature loss by an independent power variable.
 e=mp.mpf(1)/(N+1-b)
 rem2=mp.quad(lambda t:e*sum(a*t**(e*(j+1-b)-1) for j,a in enumerate(f) if j>=N),[0,1])
 via2=-b*L**2/2*(rem2+sum(f[j]/(j+1-b) for j in range(N)))
 err=abs(via2-C);assert err<mp.mpf('1e-140'),str(err)
 # Finite physical cutoff integral minus full homogeneous moments.
 z=mp.mpf('1e-20');R=L*z**(-b)*mp.sqrt(1-z**(2*b))
 primitive=b*L**2*sum(a*(1-z**(j+1-b))/(j+1-b) for j,a in enumerate(f))
 homog=sum(L**(1+(j+1)/b)*f[j]*R**(1-(j+1)/b)/(1-(j+1)/b) for j in range(N))
 estimate=-(primitive-homog)/2
 # Exact missing combined integral is O(z^(N+1-b)); this is a bound test, not exact equality at finite R.
 scaled=abs(estimate-C)/z**(N+1-b)
 assert scaled<100, str(scaled)
 out['algebraic_checks'].append(dict(b=bs,N=N,C=str(C),power_quadrature_error=str(err),unregularized_quadrature_error=str(abs(via-C)),cutoff_scaled_error=str(scaled)))
for b in [2.5,3.1,3.5,3.9]:
 N=int(b);a=np.array([1.,.3,-.2][:N]);L=1.3
 C=-b*L*L/2*sum(v/(j+1-b) for j,v in enumerate(a))
 def modes(r):
  z=np.exp(-np.log1p((r/L)**2)/(2*b));q=r*z**(b+1)*sum(v*z**j for j,v in enumerate(a));return np.array([q,0.])
 inv=AdaptiveModalInverse(modes,2,ModalSettings(1/b,3e-11,3e-11));rows=[]
 for R in [1e2,1e3,1e4,1e5]:
  actual=inv.relative([[R,0.]])[0,1];u=0.
  for j,v in enumerate(a):
   aa=(j+1)/b;pp=2-aa;u+=pp*L**(1+aa)*v/(1-pp*pp)*R**(1-aa)
  rows.append(dict(R=R,inferred_C=float(actual-u),error=float(abs(actual-u-C))))
 assert rows[-1]['error']<3e-5,rows
 out['inverse_checks'].append(dict(b=b,C=C,rows=rows,all_inverse_flags_zero=all(q['inner_success'] and q['outer_success'] for q in inv.evidence)))
 print('inverse',b,rows[-1],flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,precision_digits=mp.mp.dps,limitations='Source-only manufactures. Finite-precision quadrature and finite cutoff checks, not a rigorous certificate or coupled PDE result.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
