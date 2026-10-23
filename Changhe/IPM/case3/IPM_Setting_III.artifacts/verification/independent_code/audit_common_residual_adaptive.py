"""Result287: independent adaptive inverse on explicitly selected witnesses."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource,math
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from adaptive_hydrostatic_velocity import AdaptiveVerticalVelocity
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));torch.set_num_threads(1)
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';O=Path('research/hydrostatic_velocity_sequence_audit/verification');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def dump():
 out['updated_utc']=utc();(V/'ADAPTIVE.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),states=[],checks=checks,proof_sha256=sha(R/'ADAPTIVE_PROOF.md'),driver_sha256=sha(__file__),module_sha256=sha('independent_code/adaptive_hydrostatic_velocity.py'),summary_sha256=sha(V/'SUMMARY.json'),run_sha256=sha(V/'RUN.json'),points_sha256=sha(V/'POINTS.npz'),input_sha256=sha(V/'INPUTS.json'));dump()
try:
 summary=json.loads((V/'SUMMARY.json').read_text());run=json.loads((V/'RUN.json').read_text());ck('complete summary',summary['status']=='PASS'and all(c['passed']for c in summary['checks']));ck('complete base run',run['status']=='PASS'and all(c['passed']for c in run['checks']));ck('summary driver',summary['driver_sha256']==sha('independent_code/summarize_hydrostatic_common_residuals.py'));ck('summary proof',summary['proof_sha256']==sha(R/'SUMMARY_PROOF.md'))
 for f,num in [('ADAPTIVE_MANUFACTURE.json',54),('ADAPTIVE_POWER_MANUFACTURE.json',243)]:
  g=json.loads((O/f).read_text());ck(f+' complete',g['status']=='PASS'and len(g['checks'])==num and all(c['passed']for c in g['checks']));ck(f+' module',g['module_sha256']==sha('independent_code/adaptive_hydrostatic_velocity.py'));out.setdefault('manufactures',[]).append(dict(path=str(O/f),sha256=sha(O/f)))
 for m,h in run['modules'].items():ck('base jet module '+m,sha(Path('independent_code')/m)==h)
 inp=json.loads((V/'INPUTS.json').read_text());items={s['tag']:s for s in inp['states']};points=np.load(V/'POINTS.npz')['points'];out['selection']=summary['witnesses'];dump()
 for selected in summary['witnesses']:
  tag=selected['tag'];item=items[tag];ck('input hash '+tag,sha(item['state']['path'])==item['state']['sha256'])
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
  jet=CartesianQJet(q);inv=AdaptiveVerticalVelocity(jet.jet,q.p,split=37,epsabs=2e-11,epsrel=2e-11);row=dict(tag=tag,p=q.p,c=q.cl,status='RUNNING',points=[]);out['states'].append(row)
  for index in selected['indices']:
   x,y,r,j=points[index];print('START',tag,index,utc(),flush=True);value=inv.at(x,y);jj=jet.jet(np.array([x]),np.array([y]))[0];g,gx,gy=map(float,jj[:3]);u,v=value['V'];a=(q.cl*x+u)*gx;b=(q.cl*y+v)*gy;rh=math.fsum([a,b,-g]);nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(math.fsum([x*gx,y*gy]))+abs(math.fsum([u*gx,v*gy]));nb=math.hypot(q.cl*x+u,q.cl*y+v)*math.hypot(gx,gy)+abs(g)
   ck(tag+' finite '+str(index),np.isfinite(value['V']).all()and np.isfinite(value['estimated_error']).all()and np.isfinite(jj).all());ck(tag+' no warnings '+str(index),not value['messages'],value['messages']);row['points'].append(dict(index=int(index),x=float(x),y=float(y),radius=float(r),angle_index=int(j),jet=list(map(float,jj)),Rh=float(rh),Nf=float(nf),Nv=float(nv),Nbound=float(nb),Rf=float(abs(rh)/nf)if nf>0 else None,Rv=float(abs(rh)/nv)if nv>0 else None,Rbound=float(abs(rh)/nb)if nb>0 else None,**value));dump();print('DONE',tag,index,'Rf',abs(rh)/nf if nf else None,utc(),flush=True)
  row.update(status='DONE',finished_utc=utc());dump()
 ck('selection unchanged',out['summary_sha256']==sha(V/'SUMMARY.json'));out.update(status='PASS',count=len(checks),finished_utc=utc());dump();print('PASS',len(checks),sum(len(s['points'])for s in out['states']),utc(),flush=True)
except Exception:
 out.update(status='FAIL',count=len(checks),finished_utc=utc(),traceback=traceback.format_exc());dump();raise
