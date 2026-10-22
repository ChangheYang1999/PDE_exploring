from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
from scipy.integrate import quad
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings
root=Path('verification/near_center_inverse');root.mkdir(exist_ok=True)
nu=1/3;b=nu/2;amplitude=.3
def modes(r):
 h=amplitude*r*r*(1+r*r)**(-b)*(12*b/(1+r*r)-4*b*(b+1)*r*r/(1+r*r)**2)
 return np.array([0.,h])
def exact_v1_over_r(r):return 2*amplitude*(1+r*r)**(-b)
out={'started_utc':datetime.now(timezone.utc).isoformat(),'source':'p2=0.3 r^2 (1+r^2)^(-1/6), p1=0','expected_center_strain':-2*amplitude,'tests':[]}
for tol in [1e-8,2e-11]:
 inv=AdaptiveModalInverse(modes,2,ModalSettings(nu,tol,tol))
 rows=[]
 for r in np.logspace(-3,-30,28):
  pr,dp=inv.radial(r);val=2*pr[1]/r;want=exact_v1_over_r(r)
  rows.append({'r':float(r),'computed_V1_over_x':float(val),'exact_V1_over_x':float(want),'strain_error':float(abs(val-want)),'quadrature':inv.evidence[-1]})
 out['tests'].append({'tolerance':tol,'rows':rows})
 # A separate origin moment directly in physical radius, no shrinking endpoint layer.
 moment,error=quad(lambda s:modes(s)[1]/s,0.,np.inf,epsabs=tol,epsrel=tol,limit=500)
 out['tests'][-1]['moment']={'computed_strain':-.5*moment,'estimated_error':.5*error,'actual_error':abs(-.5*moment+2*amplitude)}
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for t in out['tests']:
 bad=[q for q in t['rows'] if q['strain_error']>1e-4]
 print('tol',t['tolerance'],'first_bad',bad[0] if bad else None,'moment',t['moment'])
