"""Reproducible tolerance and frozen native-source identity check."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
root=Path(sys.argv[1]);leaves=[root/q['label'] for q in json.loads((root/'manifest.json').read_text())['states']]
states=[]
for leaf in leaves:
 m=json.loads((leaf/'manifest.json').read_text());s=R2State(leaf/m['snapshot']);assert s.sha256==m['sha256'];states.append(s)
s=states[0];fields=['bb','L','K','Nt','degree','grade'];same=all(all(getattr(s.seed_field,k)==getattr(t.seed_field,k)for k in fields)and np.array_equal(s.seed_field.rawG,t.seed_field.rawG)for t in states);assert same
source=R2ModeSource(s,kind='native_seed');values=[]
for tol in [1e-10,1e-11,3e-12,1e-12]:
 inv=AdaptiveModalInverse(source,source.count,ModalSettings(1/s.seed_field.bb,tol,tol));p,dp=inv.radial(.5);values.append({'tol':tol,'pr':p.tolist(),'dp':dp.tolist(),'evidence':inv.evidence})
base=np.r_[values[-1]['pr'],values[-1]['dp']]
for v in values:v['max_absolute_modal_difference_from_tightest']=float(np.max(np.abs(np.r_[v['pr'],v['dp']]-base)))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE','archive_sha256s':[s.sha256 for s in states],'same_seed_between_states':same,'seed_geometry':{k:getattr(s.seed_field,k)for k in fields},'seed_coefficients_sha256':hashlib.sha256(s.seed_field.rawG.tobytes()).hexdigest(),'values':values,'scope':'Source identity checked coefficientwise and geometrically. Floating-point tolerance study, not a proof. Tightest unsuccessful flag retained.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'seed_roundoff_study.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],[(v['tol'],v['max_absolute_modal_difference_from_tightest'],v['evidence'][0]['outer_success'])for v in values])
