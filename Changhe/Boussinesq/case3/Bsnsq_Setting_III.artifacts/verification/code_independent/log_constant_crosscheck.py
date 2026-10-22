"""Independent physical-radius inverse check of packet95 constants."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
start=time.monotonic();root=Path('research/95_serialized_beta_three_log_constant/verification')
results=json.loads((root/'results.json').read_text());out={'started_utc':datetime.now(timezone.utc).isoformat(),'states':[],'scope':'Independent full-plane inverse values, not a PDE or interval certificate.'}
for item in results['states']:
 state=R2State(item['archive']);self_modes=R2ModeSource(state);eps=float(state.meta.get('eps',1.))
 ext=R2ModeSource(state,kind='external') if state.Es is not None else None
 defect=R2ModeSource(state,kind='defect') if state.Ds is not None else None
 def mixed(r):
  val=eps*self_modes(r)
  if eps!=1:val+=(1-eps)*ext(r)
  if defect is not None:val+=defect(r)
  return val
 row={'label':item['label'],'sources':{}}
 for kind,func in [('self',self_modes),('transport',mixed)]:
  inv=AdaptiveModalInverse(func,state.K,ModalSettings(decay=1/3,epsabs=1e-10,epsrel=2e-12))
  obj=item['sources'][kind];B0=obj['B0_first_cosine'];B1=obj['B1_first_cosine'];B3=obj['B3_first_cosine'];C=obj['evaluations'][-1]['C'];alpha=obj['evaluations'][-1]['alpha'];values=[]
  for r in [1e3,1e4,1e5,1e6,1e7,1e8,1e9]:
   pr,dp=inv.radial(r);mean=float((pr[0]+dp[0])/2)
   inferred=mean+.75*B0*r**(2/3)+1.5*B1*r**(1/3)+alpha/2*np.log(r)+alpha/4
   corrected=inferred-1.5*B3*r**(-1/3)
   values.append({'r':r,'mean_V2':mean,'inferred_C':float(inferred),'C_formula':C,'raw_error':float(inferred-C),'subtract_next_source_term':float(corrected),'corrected_error':float(corrected-C)})
  row['sources'][kind]={'values':values,'inverse_evidence':inv.evidence}
  print(item['label'],kind,'raw_last',values[-1]['raw_error'],'corrected_last',values[-1]['corrected_error'],'flags',sum(not e['inner_success'] or not e['outer_success'] for e in inv.evidence),flush=True)
 out['states'].append(row)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'high_radius_crosscheck.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
