from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
r=Path('verification/native_axis_beta305_20261021T1641Z');d=r/'blamB40ext_beta3.05'
m=json.loads((d/'manifest.json').read_text());s=R2State(d/m['snapshot']);q=R2ModeSource(s,kind='native_seed');vals=[]
for tol in [1e-10,1e-11,3e-12,1e-12]:
 inv=AdaptiveModalInverse(q,q.count,ModalSettings(1/s.seed_field.bb,tol,tol));p,dp=inv.radial(.5);vals.append({'tol':tol,'pr':p.tolist(),'dp':dp.tolist(),'evidence':inv.evidence})
base=np.r_[vals[-1]['pr'],vals[-1]['dp']]
for v in vals:v['max_absolute_modal_difference_from_tightest']=float(np.max(np.abs(np.r_[v['pr'],v['dp']]-base)))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE','archive_sha256':s.sha256,'values':vals,'scope':'Floating point tolerance study only. The tightest request preserves its roundoff success flag, not replaced by a proof of its tolerance.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(r/'seed_roundoff_study.json').write_text(json.dumps(out,indent=2)+'\n');print([(v['tol'],v['max_absolute_modal_difference_from_tightest'],v['evidence'][0]['outer_success'])for v in vals])
