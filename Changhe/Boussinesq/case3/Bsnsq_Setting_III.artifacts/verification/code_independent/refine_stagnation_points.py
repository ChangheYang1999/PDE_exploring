from pathlib import Path
from datetime import datetime,timezone
import json,time
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings,R2ModeSource
v=Path('research/194_stagnation_grid_audit/verification');old=json.loads((v/'evaluation.json').read_text());out=[];start=time.monotonic()
for row in old['states']:
 if row['reported_max_absolute_difference']<1e-9:continue
 s=R2State(v/row['archive']);a=R2ModeSource(s);b=R2ModeSource(s,kind='native_seed');N=max(a.count,b.count);lam=row['lam'];decay=min(1/s.bb,1/s.seed_field.bb)
 def source(rad):
  aa=a(rad);bb=b(rad);z=np.zeros(N);z[:len(aa)]+=aa;z[:len(bb)]+=lam*bb;return z
 p=max(row['reported_points'],key=lambda p:abs(p['difference']));point=np.array(p['point']);rad=np.linalg.norm(point);res=[]
 for tol in [2e-12,2e-13]:
  inv=AdaptiveModalInverse(source,N,ModalSettings(decay,tol,tol));W=s.beta*point+inv.relative([point])[0];q=float(np.linalg.norm(W)/(s.beta*rad));rr=float(W@point/(s.beta*rad**2));val=q if p['kind']=='q'else rr;res.append({'tolerance':tol,'value':val,'difference_from_initial_own':val-p['own_value'],'difference_from_NUM':val-p['NUM_value'],'quadrature':inv.evidence})
 out.append({'state':row['file'],'point':p,'refined':res});print(row['file'],res,flush=True)
z={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'status':'COMPLETE','results':out,'scope':'Adaptive floating-point tolerance consistency only, not interval certification.'};(v/'refinement.json').write_text(json.dumps(z,indent=2)+'\n')
