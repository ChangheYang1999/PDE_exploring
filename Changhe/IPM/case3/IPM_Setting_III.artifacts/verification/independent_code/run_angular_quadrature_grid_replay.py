import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,traceback,resource
import numpy as np
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_quadrature_grid_audit';V=R/'verification';OLD=ROOT/'research/angular_evaluator_sensitivity/verification'
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 t=Path(p).with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
def load(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
sys.path.insert(0,str(ROOT/'independent_code'))
from angular_evaluator_sensitivity import point,gaussian,EPS
from node_export_inverse_stage import RULES
from independent_hydrostatic import CartesianQJet
from q_local_checkpoint import QLocalCheckpoint
SOURCES=[__file__,R/'PROOF.md',R/'REPLAY_PROTOCOL.md',ROOT/'independent_code/run_angular_quadrature_grid.py',ROOT/'independent_code/angular_evaluator_sensitivity.py',ROOT/'independent_code/node_export_inverse_stage.py',ROOT/'independent_code/independent_hydrostatic.py',ROOT/'independent_code/q_local_checkpoint.py',ROOT/'independent_code/q_checkpoint_reader.py']
def grid(jet,x,y,p,rule,progress=None):
 if len(x)!=len(y)or len(x)==0:raise ValueError('invalid coordinate lengths')
 velocities=[];tails=[];metas=[]
 for i,(xx,yy)in enumerate(zip(x,y)):
  vel,tail,meta=point(jet,float(xx),float(yy),p,rule);velocities.append(vel);tails.append(tail);metas.append(meta)
  if progress and((i+1)%16==0 or i+1==len(x)):progress(i+1)
 return dict(velocity=np.asarray(velocities),tail=np.asarray(tails),meta=np.asarray(metas))
def origins():
 names=['angular_evaluator_sensitivity','node_export_inverse_stage','independent_hydrostatic','q_local_checkpoint','q_checkpoint_reader']
 out={n:str(Path(sys.modules[n].__file__).resolve())for n in names}
 if any(p!=str(ROOT/'independent_code'/(n+'.py'))for n,p in out.items()):raise RuntimeError('imported module origin mismatch')
 return out
def manufacture():
 module_paths=origins();checks=[]
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise AssertionError(n)
 x=np.array([.7,-.7,.7]);y=np.array([.3,.3,-.3])
 for label in ['A','B','C']:
  z=grid(gaussian,x,y,.5,RULES[label]);ck('shape '+label,z['velocity'].shape==(3,4,2)and z['tail'].shape==(3,4)and z['meta'].shape==(3,10));ck('finite '+label,all(np.isfinite(a).all()for a in z.values()))
  ck('x parity '+label,np.array_equal(z['velocity'][1],z['velocity'][0]*np.array([-1,1])))
  ck('y parity '+label,np.array_equal(z['velocity'][2],z['velocity'][0]*np.array([1,-1])))
  ck('unchanged v1 '+label,np.array_equal(z['velocity'][:,:,0],np.repeat(z['velocity'][:,0:1,0],4,axis=1)))
  exact=.7*np.exp(-.7**2-.3**2);ck('Gaussian exact v1 '+label,abs(z['velocity'][0,0,0]-exact)<8e-13)
  for i in range(3):
   a,t,m=point(gaussian,x[i],y[i],.5,RULES[label]);ck('grid ordering '+str((label,i)),np.array_equal(z['velocity'][i],a)and np.array_equal(z['tail'][i],t)and np.array_equal(z['meta'][i],m))
 for xx,yy in [([],[]),([1],[])]:
  try:grid(gaussian,xx,yy,.5,RULES['A']);failed=False
  except ValueError:failed=True
  ck('invalid grid rejected '+str((xx,yy)),failed)
 out=dict(status='PASS_FULL_GRID_REPLAY_MANUFACTURES',utc=now(),module_paths=module_paths,argv=sys.argv,executable=sys.executable,numpy_version=np.__version__,count=len(checks),checks=checks,bindings={str(Path(p).resolve()):sha(p)for p in SOURCES});save(V/'REPLAY_MANUFACTURES.json',out);print(json.dumps({k:out[k]for k in ['status','utc','count']}),flush=True)
def candidate():
 module_paths=origins();checks=[];bindings={};started=now()
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise AssertionError(n)
 def bind(p,h=None):
  p=Path(p).resolve();a=sha(p);ck('binding '+str(p),h is None or h==a);bindings[str(p)]=a;return p
 O=V/'candidate2';O.mkdir(exist_ok=False)
 try:
  ck('nice19',os.getpriority(os.PRIO_PROCESS,0)==19);ck('memory cap',resource.getrlimit(resource.RLIMIT_AS)==(14*1024**3,14*1024**3))
  m=json.loads(bind(V/'REPLAY_MANUFACTURES.json').read_text());ck('manufactures passed',m['status']=='PASS_FULL_GRID_REPLAY_MANUFACTURES'and m['count']==29 and all(c['passed']for c in m['checks']))
  ck('actual manufacture module identity',m['module_paths']==module_paths)
  for p,h in m['bindings'].items():bind(p,h)
  old=json.loads(bind(OLD/'CHECKS.json').read_text());ck('327checked',old['status']=='PASS_FINITE_ANGULAR_SENSITIVITY_CHECKS_REVIEW_PENDING'and old['count']==191 and all(c['passed']for c in old['checks']))
  for p,h in old['bindings'].items():bind(p,h)
  for p,h in old['outputs'].items():bind(p,h)
  prior=json.loads(bind(OLD/'candidate/COMPLETE.json').read_text())
  for p,h in prior['bindings'].items():bind(p,h)
  for p,h in prior['outputs'].items():bind(p,h)
  latest=json.loads(bind(OLD/'MANUFACTURES_LATEST.json').read_text());op=json.loads(bind(latest['path'],latest['sha256']).read_text());ck('160 operator manufactures',op['status']=='PASS_MANUFACTURES'and op['count']==160 and op['source_sha256']==sha(ROOT/'independent_code/angular_evaluator_sensitivity.py')and op['proof_sha256']==sha(OLD.parent/'PROOF.md'))
  import torch
  torch.set_num_threads(1)
  sp=bind(ROOT/'research/accurate_map_final_audit/verification/hsQ_c2.0_N128_acc.pt','f8b2b6ef3d926e6af94b4a36e6d62102cdb85a4501284a5b6c2a43ce001fdc37')
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(sp)
  ck('exact state parameters',q.N==128 and q.M==32 and q.cl==2 and q.p==.5 and q.L==1 and q.kappa==2)
  jet=CartesianQJet(q).jet;records=[]
  for radius in [3,30]:
   b=load(OLD/'candidate'/('R'+str(radius)+'_B.npz'));theta=np.linspace(0,np.pi/2,257)[1:-1];x=radius*np.cos(theta);y=radius*np.sin(theta);j=jet(x,y)
   ck('all points and jets '+str(radius),np.array_equal(b['theta'],theta)and np.array_equal(b['eps'],EPS)and np.array_equal(b['x'],x)and np.array_equal(b['y'],y)and np.array_equal(b['jet'],j))
   for label in ['A','C']:
    z=grid(jet,x,y,q.p,RULES[label],lambda n:print(json.dumps(dict(utc=now(),radius=radius,rule=label,completed=n,total=255)),flush=True))
    oldz=load(OLD/'candidate'/('R'+str(radius)+'_'+label+'.npz'));ids=oldz['indices'];ck('selected schema '+str((radius,label)),ids.ndim==1 and len(ids)>0 and np.issubdtype(ids.dtype,np.integer) and np.all(np.diff(ids)>0)and min(ids)>=0 and max(ids)<255 and all(oldz[k].shape[0]==len(ids)for k in ['velocity','tail','meta']));ck('selected bitwise replay '+str((radius,label)),all(np.array_equal(z[k][ids],oldz[k])for k in ['velocity','tail','meta']))
    path=O/('R'+str(radius)+'_'+label+'.npz');tmp=path.with_suffix('.tmp.npz');np.savez_compressed(tmp,x=x,y=y,theta=theta,eps=EPS,jet=j,**z);tmp.replace(path);records.append(dict(radius=radius,rule=label,points=255,selected_replayed=len(ids)))
  for p,h in bindings.items():ck('final stable '+p,sha(p)==h)
  out=dict(status='COMPLETE_FULL_ANGULAR_GRID_REPLAY_REQUIRES_FRACTION_CHECK_AND_REVIEW',module_paths=module_paths,argv=sys.argv,executable=sys.executable,versions=dict(python=sys.version,numpy=np.__version__,torch=torch.__version__),started_utc=started,finished_utc=now(),count=len(checks),checks=checks,bindings=bindings,outputs={str(p.resolve()):sha(p)for p in O.iterdir()if p.is_file()},records=records,scope='Three finite quadrature rules; no continuum enclosure or producer historical causation.')
  save(O/'COMPLETE.json',out);print(json.dumps({k:out[k]for k in ['status','started_utc','finished_utc','count','records']}),flush=True)
 except Exception:
  save(O/'FAILURE.json',dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
if __name__=='__main__':
 if len(sys.argv)!=2 or sys.argv[1]not in ['manufacture','candidate']:raise ValueError('mode')
 (manufacture if sys.argv[1]=='manufacture'else candidate)()
