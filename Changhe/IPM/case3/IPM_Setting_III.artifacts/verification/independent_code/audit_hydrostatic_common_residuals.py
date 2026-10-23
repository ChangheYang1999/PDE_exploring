"""Result287: independent analytic jets and complete vertical inverse,333points."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,resource,time,traceback,math
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3));torch.set_num_threads(1)
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def dump():
 out['updated_utc']=utc();(V/'RUN.json').write_text(json.dumps(out,indent=2)+'\n')
input_hash=sha(V/'INPUTS.json');rules=[(32,96,16),(48,160,64),(64,192,128)];radii=np.logspace(-3,6,37);angles=np.linspace(0,np.pi/2,9);points=np.array([(0. if j==8 else r*np.cos(theta),0. if j==0 else r*np.sin(theta),r,j)for r in radii for j,theta in enumerate(angles)])
np.savez_compressed(V/'POINTS.npz',points=points,radii=radii,angles=angles)
mods=['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_power_tail.py']
out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),states=[],checks=checks,rules=rules,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),input_sha256=input_hash,points_sha256=sha(V/'POINTS.npz'),modules={m:sha(Path('independent_code')/m)for m in mods});dump()
try:
 for path,key,module in [('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json','evaluator_sha256','independent_hydrostatic.py'),('research/hydrostatic_power_tail_inverse/verification/GATE.json','module_sha256','hydrostatic_power_tail.py')]:
  g=json.loads(Path(path).read_text());ck('manufactured '+module,g['status']=='PASS'and all(c['passed']for c in g['checks'])and g[key]==sha(Path('independent_code')/module));out.setdefault('manufactures',[]).append(dict(path=path,sha256=sha(path),count=len(g['checks'])))
 inp=json.loads((V/'INPUTS.json').read_text())
 for f in inp['files']:ck('frozen '+f['path'],sha(f['path'])==f['sha256'])
 items=sorted(inp['states'],key=lambda i:(i['c'],i['N']));ck('seven states',len(items)==7);x,y=points[:,0],points[:,1]
 for item in items:
  tag=item['tag'];ck('coefficients '+tag,sha(item['state']['path'])==item['state']['sha256']);start=time.monotonic()
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
  jet=CartesianQJet(q);jets=jet.jet(x,y);ck(tag+' finite jets',np.isfinite(jets).all());ck(tag+' jet parity on axes',np.all(jets[y==0,:2]==0) and np.all(jets[x==0,1]==0));row=dict(tag=tag,c=q.cl,p=q.p,N=item['N'],M=q.M,status='RUNNING',source_sha256=item['state']['sha256'],a0=float(jet.jet(0.,0.)[2]),started_utc=utc(),levels=[]);out['states'].append(row);dump()
  for order,tail,split in rules:
   inv=PowerVerticalInverse(jet.jet,q.p,order=order,tail_order=tail,tail_scale=split);vel=np.empty((len(points),2));aux=np.empty((len(points),5));lev=dict(order=order,tail_order=tail,split=split,status='RUNNING',started_utc=utc());row['levels'].append(lev);print('START',tag,order,utc(),flush=True);dump()
   for j,pt in enumerate(points):
    val=inv.at(pt[0],pt[1]);vel[j]=val['V'];aux[j]=[val['Phi'],val['dV2_dy'],*val['tail_V'],val['R_split']]
    if j%60==0:lev['completed_points']=j+1;dump();print('POINT',tag,order,j+1,utc(),flush=True)
   W=vel+q.cl*points[:,:2];parts=W*jets[:,1:3];res=np.array([math.fsum([a,b,-g])for (a,b),g in zip(parts,jets[:,0])]);nf=np.sum(abs(parts),axis=1)+abs(jets[:,0]);nv=abs(jets[:,0])+abs(np.sum(points[:,:2]*jets[:,1:3],axis=1))+abs(np.sum(vel*jets[:,1:3],axis=1));nb=np.hypot(W[:,0],W[:,1])*np.hypot(jets[:,1],jets[:,2])+abs(jets[:,0]);rf=np.divide(abs(res),nf,out=np.full_like(nf,np.nan),where=nf>0);rv=np.divide(abs(res),nv,out=np.full_like(nv,np.nan),where=nv>0);rb=np.divide(abs(res),nb,out=np.full_like(nb,np.nan),where=nb>0)
   ck(tag+f' finite {order}',np.isfinite(vel).all()and np.isfinite(aux).all()and np.isfinite(res).all());ck(tag+f' inverse parity {order}',np.all(vel[y==0,1]==0)and np.all(vel[x==0,0]==0));ck(tag+f' zero residual xaxis {order}',np.all(res[y==0]==0)and np.all(nf[y==0]==0)and np.all(nv[y==0]==0));ck(tag+f' positive denominator offaxis {order}',np.all(nf[y>0]>0)and np.all(nv[y>0]>0));ck(tag+f' Cauchy Schwarz denominator {order}',np.all(nf<=nb+32*np.finfo(float).eps*np.maximum(nf,nb)));ck(tag+f' triangle ratio bounds {order}',np.nanmax(rf)<=1+1e-14 and np.nanmax(rb)<=1+1e-14 and np.nanmax(rv)<=q.cl+1e-14)
   file=V/f'{tag}_order{order}.npz';np.savez_compressed(file,jets=jets,velocity=vel,auxiliary=aux,W=W,parts=parts,Rh=res,Nf=nf,Nv=nv,Nbound=nb,Rf=rf,Rv=rv,Rbound=rb);lev.update(status='DONE',completed_points=len(points),path=str(file),sha256=sha(file),finished_utc=utc(),zero_nf=int(np.sum(nf==0)),zero_nv=int(np.sum(nv==0)),zero_nbound=int(np.sum(nb==0)));dump();print('LEVEL DONE',tag,order,float(np.nanmax(rf)),utc(),flush=True)
  row.update(status='DONE',finished_utc=utc(),seconds=time.monotonic()-start);dump();print('STATE DONE',tag,row['seconds'],utc(),flush=True)
 ck('inputs unchanged',sha(V/'INPUTS.json')==input_hash);out.update(status='PASS',finished_utc=utc(),count=len(checks));dump();print('PASS',len(checks),utc(),flush=True)
except Exception:
 out.update(status='FAIL',finished_utc=utc(),traceback=traceback.format_exc());dump();raise
