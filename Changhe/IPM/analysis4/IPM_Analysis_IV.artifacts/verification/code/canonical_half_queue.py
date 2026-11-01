"""Wait for the final half-exponent checkpoint; run audits on one locked core."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
PYTHON=sys.executable
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
log=Path('../a4-num/logs/log_sin1_c2_p512.jsonl');checkpoint=Path('../a4-num/ckpt/log_sin1_c2_p512.pkl')
while datetime.now(timezone.utc)<datetime(2026,11,1,0,20,tzinfo=timezone.utc):
 try:
  rows=[json.loads(x) for x in log.read_bytes().splitlines() if x.strip()];last=max(x.get('n',0) for x in rows)
 except (ValueError,FileNotFoundError):last=0
 if last>=300 and any(r.get('done') and r.get('N')==300 for r in rows):break
 time.sleep(15)
else:raise SystemExit('Cutoff reached before complete checkpoint')
for script in ['canonical_half_audit.py','canonical_half_nonlinear.py']:
 with Path('scratch',script.replace('.py','.log')).open('w') as output:
  print(json.dumps(dict(at=now(),stage='start',script=script)),flush=True)
  env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
  run=subprocess.run(['taskset','-c','17','nice','-n','19','flock','scratch/core17.lock',PYTHON,'code/'+script],env=env,stdout=output,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=now(),stage='end',script=script,exit_code=run.returncode)),flush=True)
  if run.returncode:raise SystemExit(run.returncode)
