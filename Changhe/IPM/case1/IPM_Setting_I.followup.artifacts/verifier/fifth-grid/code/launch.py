"""Freeze a future final state and launch only this lane's prescribed audit."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,hashlib,io,json,os,signal,subprocess
import numpy as np
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--prepare-only',action='store_true');a=p.parse_args()
source=Path(a.source).resolve();allowed=[BASE/'numerics'/d/'dnB_n108m44S.npz' for d in ['data','runs']]
if source not in allowed:raise ValueError('Only the prescribed final dnB state is accepted')
raw=source.read_bytes();dest=ROOT/'data'/source.name
with np.load(io.BytesIO(raw),allow_pickle=False)as z:
 assert int(z['N'])==108 and int(z['M'])==44 and float(z['L'])==8 and float(z['beta'])==.9
 assert z['b'].shape==(109,44) and z['b'].dtype==np.float64 and np.isfinite(z['b']).all() and np.all(z['b'][0]==1)
 assert 5<float(z['c_l'])<10 and np.isfinite(z['C'])
 assert z['q'].shape==(109,) and z['theta'].shape==(44,)
if dest.exists():assert dest.read_bytes()==raw
else:dest.write_bytes(raw)
paths=[ROOT/'PROOF.md',dest,BASE/'verifier/sampled-physical-actions/verification/points.json']
paths+=list((ROOT/'code').glob('*.py'))+list((ROOT/'code').glob('*.sh'))
for rel in ['inverse/code/strain.py','inverse/code/collocation.py','inverse/code/density.py','inverse/code/gpu.py','inverse/code/split_kernel.py','center-regularity/code/axis_jet_balls.py','center-moment/code/certify.py','center-moment-trapezoid/code/certify.py','inner-cutoff/code/hessian.py','exact-data/code/nodal_input.py']:
 paths.append(BASE/'verifier'/rel)
for f in paths:
 if f.suffix=='.py':ast.parse(f.read_text(),filename=str(f))
pins={str(f.relative_to(BASE)):sha(f)for f in paths}
record={'utc':utc(),'original_source':str(source),'source_sha256':sha(dest),'source_md5':hashlib.md5(raw).hexdigest(),'pins':pins,'complete':False,'scope':'Frozen108x44 ideal-node binary interpolant. Future audit may refute this field, never the whole coupled class.'}
prepared=ROOT/'verification/prepared.json'
if prepared.exists():assert json.loads(prepared.read_text())['pins']==pins
else:prepared.write_text(json.dumps(record,indent=2)+'\n')
if a.prepare_only:print('PREPARED',utc(),sha(dest));raise SystemExit
remaining=(datetime(2026,10,21,0,46,23,tzinfo=timezone.utc)-datetime.now(timezone.utc)).total_seconds()
assert remaining>60,'Insufficient time before actual run cap'
env=dict(os.environ);env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(BASE/'tmp'))
def interrupted(sig,frame):raise SystemExit(128+sig)
signal.signal(signal.SIGTERM,interrupted)
signal.signal(signal.SIGINT,interrupted)
def stage(command,seconds):
 proc=subprocess.Popen(command,cwd=BASE,env=env,start_new_session=True)
 try:
  code=proc.wait(timeout=seconds)
  if code:raise subprocess.CalledProcessError(code,command)
 finally:
  if proc.poll()is None:
   os.killpg(proc.pid,signal.SIGTERM)
   try:proc.wait(timeout=5)
   except subprocess.TimeoutExpired:
    os.killpg(proc.pid,signal.SIGKILL);proc.wait(timeout=5)
start=utc()
try:
 stage(['bash','verifier/fifth-grid/code/run.sh'],min(3600,remaining-10))
 stage(['python3','verifier/fifth-grid/code/audit_summary.py'],30)
 for rel,h in pins.items():assert sha(BASE/rel)==h
 record.update(complete=True,end_utc=utc(),start_utc=start)
except BaseException as exc:
 record.update(end_utc=utc(),start_utc=start,error=type(exc).__name__+': '+str(exc))
 (ROOT/'verification/completion.json').write_text(json.dumps(record,indent=2)+'\n');raise
(ROOT/'verification/completion.json').write_text(json.dumps(record,indent=2)+'\n');print('COMPLETE_WRAPPER',utc())
