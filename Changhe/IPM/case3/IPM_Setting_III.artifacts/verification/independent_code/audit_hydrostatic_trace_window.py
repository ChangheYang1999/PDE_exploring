"""Result208 independent finite-radius window using analytic Cartesian derivatives."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet,VerticalInverse
v=Path('research/hydrostatic_trace_compatibility_diagnostic/verification');dest=v/'comparison'
assert json.loads(Path('research/hydrostatic_extended_state_audit/verification/PIPELINE.json').read_text())['status']=='DONE','Queue after206'
inputs={r['tag']:r for r in json.loads((v/'INPUTS.json').read_text())['states']}
tags=['hsA_c3.0_N64','hsA_c3.0_N128','hsE_c2.0_N128_hr']
settings=[(14,64,16.),(20,112,64.),(28,192,256.),(36,320,1024.)]
rs=np.r_[np.logspace(1,4,13),1e5,1e6,1e8];deltas=[0.,.001,.003,.01,.03,.05]
def utc():return datetime.now(timezone.utc).isoformat()
report=dict(started_utc=utc(),pid=os.getpid(),status='RUNNING',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),states=[],settings=settings)
def save():(dest/'WINDOWS.json').write_text(json.dumps(report,indent=2)+'\n')
for tag in tags:
 inp=inputs[tag];assert hashlib.sha256(Path(inp['file']).read_bytes()).hexdigest()==inp['sha256']
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(inp['file'])
 field=CartesianQJet(q);row=dict(tag=tag,sha256=inp['sha256'],c=q.cl,p=q.p,N=q.N,M=q.M,levels=[]);report['states'].append(row)
 points=[]
 for delta in deltas:
  for r in rs:
   x=0. if delta==0 else r*np.cos(np.pi/2-delta);y=r if delta==0 else r*np.sin(np.pi/2-delta)
   points.append((delta,r,x,y))
 X=np.array([p[2]for p in points]);Y=np.array([p[3]for p in points]);jets=field.jet(X,Y)
 for order,tail_order,split in settings:
  t0=time.monotonic();inv=VerticalInverse(field.jet,q.p,order,tail_order,split,.125);level=dict(order=order,tail_order=tail_order,split=split,points=[],slopes=[])
  for (delta,r,x,y),jet in zip(points,jets):
   iv=inv.at(x,y);g,gx,gy,gxx=map(float,jet);V1,V2=iv['V'];A=(q.cl*x+V1)*gx;B=(q.cl*y+V2)*gy;R=A+B-g;Nf=abs(A)+abs(B)+abs(g);assert Nf>0
   level['points'].append(dict(delta=delta,r=r,x=x,y=y,g=g,gx=gx,gy=gy,gxx=gxx,V1=V1,V2=V2,R=R,Nf=Nf,signed_ratio=R/Nf,ratio=abs(R)/Nf,tail_V=iv['tail_V']))
  for delta in deltas:
   selected=[p for p in level['points']if p['delta']==delta and 100 <= p['r'] <= 1e4]
   assert len(selected)==9
   if all(p['ratio']>0 for p in selected):
    slope,logA=np.polyfit(np.log([p['r']for p in selected]),np.log([p['ratio']for p in selected]),1);level['slopes'].append(dict(delta=delta,slope=float(slope),prefactor=float(np.exp(logA)),window=[100.,1e4]))
  level.update(utc=utc(),seconds=time.monotonic()-t0);row['levels'].append(level);save();print(utc(),tag,order,tail_order,split,'seconds',level['seconds'],flush=True)
 row['refinement_changes']=[dict(from_level=i,to_level=i+1,max_absolute_ratio_change=max(abs(a['signed_ratio']-b['signed_ratio'])for a,b in zip(row['levels'][i]['points'],row['levels'][i+1]['points'])),max_velocity_change=max(max(abs(a[k]-b[k])for k in ['V1','V2'])for a,b in zip(row['levels'][i]['points'],row['levels'][i+1]['points'])))for i in range(len(settings)-1)]
 save()
report.update(status='DONE',finished_utc=utc());save();print(utc(),'DONE',flush=True)
