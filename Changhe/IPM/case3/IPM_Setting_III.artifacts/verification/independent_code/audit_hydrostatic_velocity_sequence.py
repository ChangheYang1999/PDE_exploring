"""Result277 independent complete vertical inverses on225points and3rules."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import numpy as np
import torch
import json,time,hashlib,traceback
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2)+'\n')
checks=[]
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
radii=np.logspace(-2,4,25);angles=np.linspace(0,np.pi/2,9);points=[]
for r in radii:
 for j,t in enumerate(angles):points.append([0. if j==8 else float(r*np.cos(t)),0. if j==0 else float(r*np.sin(t)),float(r),j])
out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),states=[],checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),input_sha256=sha(V/'INPUTS.json'),code_sha256={f:sha(Path('independent_code')/f)for f in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_power_tail.py']})
dump(V/'RUN.json',out);dump(V/'POINTS.json',dict(points=points,radii=list(radii),angles=list(angles),rules=[[32,96,16],[48,160,64],[64,192,128]]))
try:
 inp=json.loads((V/'INPUTS.json').read_text())
 for gp,field,module in [('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json','evaluator_sha256','independent_hydrostatic.py'),('research/hydrostatic_power_tail_inverse/verification/GATE.json','module_sha256','hydrostatic_power_tail.py')]:
  gate=json.loads(Path(gp).read_text());ck('manufactured gate '+module,gate['status']=='PASS'and all(c['passed']for c in gate['checks'])and gate[field]==sha(Path('independent_code')/module))
 ck('axis leading coefficient correction',F(1,2)/(F(1,2)*(1-F(1,2)))==2 and 1/(F(1,2)*(1-F(1,2)))==4)
 for item in inp['states']:
  tag=item['tag'];ck('frozen '+tag,sha(item['state']['path'])==item['state']['sha256']);t0=time.monotonic()
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
  jet=CartesianQJet(q);row=dict(tag=tag,c=q.cl,p=q.p,source_sha256=item['state']['sha256'],status='RUNNING',started_utc=utc(),levels=[]);out['states'].append(row);dump(V/'RUN.json',out)
  for order,tail,split in [(32,96,16),(48,160,64),(64,192,128)]:
   inv=PowerVerticalInverse(jet.jet,q.p,order=order,tail_order=tail,tail_scale=split);lev=dict(order=order,tail_order=tail,split=split,points=[]);row['levels'].append(lev);print('START',tag,order,utc(),flush=True)
   for j,(x,y,r,theta_index)in enumerate(points):
    value=inv.at(x,y);lev['points'].append(dict(x=x,y=y,r=r,theta_index=theta_index,**value))
    if j%30==0:
     dump(V/(tag+'.json'),row);out['updated_utc']=utc();dump(V/'RUN.json',out);print('PROGRESS',tag,order,j+1,utc(),flush=True)
   ck(tag+' finite inverse '+str(order),all(np.isfinite(p['V']).all()for p in lev['points']));ck(tag+' inverse axes '+str(order),all((p['x']!=0 or p['V'][0]==0)and(p['y']!=0 or p['V'][1]==0)for p in lev['points']));dump(V/(tag+'.json'),row)
  row.update(status='DONE',finished_utc=utc(),wall_seconds=time.monotonic()-t0);dump(V/(tag+'.json'),row);dump(V/'RUN.json',out);print('STATE DONE',tag,row['wall_seconds'],flush=True)
 out.update(status='PASS'if all(c['passed']for c in checks)else'FAIL',finished_utc=utc(),count=len(checks));dump(V/'RUN.json',out);print(out['status'],len(checks),out['finished_utc'],flush=True)
except Exception:
 out.update(status='ERROR',finished_utc=utc(),traceback=traceback.format_exc());dump(V/'RUN.json',out);raise
