"""Compare packet93 stable source moments with own full-plane inverse at high radii."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
start=time.monotonic();root=Path('research/93_stable_constant_of_serialized_inverse/verification')
results=json.loads((root/'results.json').read_text());out={'started_utc':datetime.now(timezone.utc).isoformat(),'states':[],'scope':'Independent full-plane numerical inverse check of a source constant, not transport/PDE validation.'}
for item in results['states']:
 state=R2State(item['source_archive']);b=state.bb;s=1/b
 self_modes=R2ModeSource(state);eps=float(state.meta.get('eps',1.));ext_modes=R2ModeSource(state,kind='external') if state.Es is not None else None
 def mixed(r):return eps*self_modes(r)+(1-eps)*ext_modes(r)
 row={'label':item['label'],'sources':{}}
 for kind,func,sp in [('self',self_modes,state.Gs),('transport',mixed,None)]:
  inv=AdaptiveModalInverse(func,state.K,ModalSettings(decay=s,epsabs=1e-10,epsrel=2e-12))
  obj=item['sources'][kind];B0=obj['B0_first_cosine'];B1=obj['B1_first_cosine'];C=obj['evaluations'][-1]['C2']
  if sp is not None:ends=sp.derivative(2)(1.)
  else:ends=eps*state.Gs.derivative(2)(1.)+(1-eps)*state.Es.derivative(2)(1.)
  B2=state.L**(1+3*s)*(ends[0]-.5*ends[2])/2
  values=[]
  for radius in [1e2,1e3,1e4,1e5,1e6,1e7]:
   pr,dp=inv.radial(radius);mean=float((pr[0]+dp[0])/2)
   remainder=mean+B0*radius**(1-s)/(2*(1-s))+B1*radius**(1-2*s)/(2*(1-2*s))
   corrected=remainder-B2*radius**(1-3*s)/(2*(3*s-1))
   rec={'radius':radius,'velocity_vertical_angular_mean':mean,'subtract_first_two':float(remainder),'constant_moment':C,'raw_error':float(remainder-C),'subtract_third':float(corrected),'third_corrected_error':float(corrected-C)};values.append(rec)
   print(item['label'],kind,radius,'raw',rec['raw_error'],'corrected',rec['third_corrected_error'],flush=True)
  row['sources'][kind]={'B2':float(B2),'values':values,'inverse_quadrature_evidence':inv.evidence}
 out['states'].append(row)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'high_radius_crosscheck.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
