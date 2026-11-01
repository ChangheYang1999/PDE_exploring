from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,time,json,os
sys.dont_write_bytecode=True
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
env=os.environ.copy();env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
for Q,index,N in [(7,3,56),(8,3,64)]:
 for script,args in [('period_high_prefix.py',['--Q',str(Q),'--root',str(index),'--N',str(N)]),('period_high_prefix_replay.py',['--Q',str(Q),'--root',str(index)])]:
  path=Path('scratch',f'Q{Q}_root{index}_{script[:-3]}.log');start=time.monotonic()
  with path.open('w') as f:p=subprocess.Popen([sys.executable,'-B','code/'+script]+args,stdin=subprocess.DEVNULL,stdout=f,stderr=subprocess.STDOUT,env=env)
  print(json.dumps(dict(at=stamp(),script=script,Q=Q,root=index,pid=p.pid)),flush=True)
  code=p.wait();print(json.dumps(dict(at=stamp(),script=script,Q=Q,root=index,exit_code=code,actual_elapsed_s=time.monotonic()-start)),flush=True)
  if code:raise SystemExit(code)
