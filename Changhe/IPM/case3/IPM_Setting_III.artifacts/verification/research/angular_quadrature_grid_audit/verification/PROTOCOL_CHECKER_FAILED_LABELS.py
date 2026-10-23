from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_quadrature_grid_audit';V=R/'verification';checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest()
 if h is not None:ck('binding '+str(p),h==a)
 bindings[str(p)]=a;return b
parse=datetime.fromisoformat
for p in [__file__,R/'PROTOCOL_CHECK_PROOF.md',R/'RESULTS_DRAFT.md']:bind(p)
d=json.loads(bind(V/'CHECKS.json'));ck('main finite acceptance',d['status']=='PASS_COMPLETE_FINITE_ANGULAR_QUADRATURE_AUDIT_REVIEW_PENDING' and d['count']==107 and d['scalar_values_recomputed']==30600 and all(c['passed']for c in d['checks']))
for p,h in {**d['bindings'],**d['outputs']}.items():bind(p,h)
first_exit=None
for label,prefix,folder,script,manustatus in [('first','','candidate','launch_332.sh','PASS_FULL_GRID_DRIVER_MANUFACTURES'),('replay','REPLAY_','candidate2','launch_332_replay.sh','PASS_FULL_GRID_REPLAY_MANUFACTURES')]:
 job=json.loads(bind(V/(prefix+'JOB.json')));end=json.loads(bind(V/(prefix+'JOB_EXIT.json')));c=json.loads(bind(V/folder/'COMPLETE.json'));wrapper=bind(ROOT/'runs'/script,job['wrapper_sha256']).decode();logpath=Path(job['log']);logpath=logpath if logpath.is_absolute()else ROOT/logpath;log=bind(logpath).decode()
 ck('job pid recorded '+label,type(job['pid'])is int and job['pid']>0)
 ck('ordered launch/start/finish/exit '+label,parse(job['utc'])<=parse(c['started_utc'])<=parse(c['finished_utc'])<=parse(end['utc'])and end['returncode']==0)
 if label=='first':first_exit=end['utc']
 else:ck('replay after first exit',parse(first_exit)<parse(job['utc'])<=parse(c['started_utc']))
 summaries=[]
 for line in log.splitlines():
  try:z=json.loads(line)
  except json.JSONDecodeError:continue
  if isinstance(z,dict)and z.get('status')==c['status']:summaries.append(z)
 ck('unique matching completion log '+label,len(summaries)==1 and all(summaries[0][k]==c[k]for k in ['status','started_utc','finished_utc','count']))
 ck('exact complete directory '+label,{str(p.resolve())for p in (V/folder).iterdir()}==set(c['outputs'])|{str((V/folder/'COMPLETE.json').resolve())}and all(p.is_file()for p in(V/folder).iterdir()))
 ck('four raw outputs '+label,len(c['outputs'])==4 and all(Path(p).suffix=='.npz'for p in c['outputs']))
 for p,h in c['outputs'].items():bind(p,h)
 ck('runtime constraints '+label,all(any(g['name']==n and g['passed']for g in c['checks'])for n in ['nice19','memory14GiB','one thread OMP_NUM_THREADS','one thread OPENBLAS_NUM_THREADS','one thread MKL_NUM_THREADS','one thread NUMEXPR_NUM_THREADS']))
 ck('wrapper limits '+label,'ulimit -v 14680064'in wrapper and'timeout --signal=TERM --kill-after=5s 1h python3'in wrapper and'export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1'in wrapper)
 manu=json.loads(bind(V/(prefix+'MANUFACTURES.json')));ck('29 manufactures '+label,manu['status']==manustatus and manu['count']==len(manu['checks'])==29 and all(c['passed']for c in manu['checks'])and parse(manu['utc'])<parse(c['started_utc']))
 for p,h in manu['bindings'].items():bind(p,h)
 if label=='replay':
  cache=json.loads(bind(V/'REPLAY_CACHE_PREPARATION.json'));names=['angular_evaluator_sensitivity','node_export_inverse_stage','independent_hydrostatic','q_local_checkpoint','q_checkpoint_reader'];want={str(ROOT/'independent_code/__pycache__'/(n+'.cpython-312.pyc'))for n in names}
  ck('recorded cache-removal set',set(cache['removed'])==want and len(cache['removed'])==5 and cache['mode']=='python -B, no new bytecode')
  ck('cache preparation ordered',parse(job['utc'])<=parse(cache['utc'])<parse(c['started_utc']))
  ck('bound wrapper removes caches and invokes -B',"p.unlink()"in wrapper and".glob(name+'.*.pyc')"in wrapper and'1h python3 -B independent_code/run_angular_quadrature_grid_replay.py candidate'in wrapper)
  ck('replay argv',c['argv']==['independent_code/run_angular_quadrature_grid_replay.py','candidate'])
old=json.loads(bind(ROOT/'research/angular_evaluator_sensitivity/verification/CHECKS.json'));ck('327 exact status',old['status']=='PASS_FINITE_ANGULAR_SENSITIVITY_EXACT_ARITHMETIC_REVIEW_PENDING')
for i,z in enumerate(d['records']):ck('finite spread implies common signs '+str(i),0<=z['spreads']['over_abs_R_B']['maximum']<1 and all(not p['sign_class_disagreement_indices']for p in z['pairs'].values()))
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_ANGULAR_GRID_PROTOCOL_RECORDS_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Recorded wrappers, logs, source hashes, timing and complete directory contents; no retrospective PID/bytecode attestation and no continuum accuracy estimate.')
(V/'PROTOCOL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']},indent=2))
