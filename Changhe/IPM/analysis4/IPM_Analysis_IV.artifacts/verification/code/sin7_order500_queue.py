"""Serialize the finite sin7 extension after its producer closes the checkpoint."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
sys.dont_write_bytecode=True
log=Path('../a4-num/logs/single_sin7_45_p1024_N500.jsonl')
while datetime.now(timezone.utc)<datetime(2026,11,1,0,15,tzinfo=timezone.utc):
 try:rows=[json.loads(s) for s in log.read_bytes().splitlines() if s.strip()]
 except (ValueError,FileNotFoundError):rows=[]
 if rows and rows[-1].get('done') and rows[-1].get('N')==500:break
 time.sleep(20)
else:raise SystemExit('Checkpoint not complete before cutoff')
for script,args in [('sin7_order500_audit.py',[]),('sin7_order500_fits.py',['--M','7']),('sin7_order500_overlap.py',[])]:
 with Path('scratch',script.replace('.py','.log')).open('w') as out:
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',script=script)),flush=True)
  run=subprocess.run(['taskset','-c','17','nice','-n','19','flock','scratch/core17.lock',sys.executable,'-B','code/'+script]+args,env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'),stdout=out,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='end',script=script,returncode=run.returncode)),flush=True)
  if run.returncode:raise SystemExit(run.returncode)
