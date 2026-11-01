"""Serialize Q10 long-prefix construction on the verifier's second allocated core."""
from pathlib import Path
from datetime import datetime,timezone
import fcntl,json,os,subprocess,sys,time
sys.dont_write_bytecode=True
steps=[('q10_tail_prefix.py',['cartesian']),('q10_tail_prefix.py',['polar']),('q10_tail_bound.py',[])]
for script,args in steps:
 if datetime.now(timezone.utc)>=datetime(2026,10,31,23,30,tzinfo=timezone.utc):raise SystemExit('No new stages after cutoff')
 with Path('scratch/core17.lock').open('a') as lock,Path('scratch/q10_tail_'+(args[0] if args else 'bound')+'.log').open('w') as output:
  fcntl.flock(lock,fcntl.LOCK_EX);start=time.monotonic()
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',script=script,args=args)),flush=True)
  result=subprocess.run(['taskset','-c','17','nice','-n','19',sys.executable,'-B','code/'+script]+args,stdout=output,stderr=subprocess.STDOUT,env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'))
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='end',script=script,args=args,returncode=result.returncode,elapsed_s=time.monotonic()-start)),flush=True)
  if result.returncode:raise SystemExit(result.returncode)
