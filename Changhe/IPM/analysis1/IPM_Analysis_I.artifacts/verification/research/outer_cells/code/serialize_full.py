"""Run the exterior certificate with the middle worker paused and resumed."""
import os,sys,signal,subprocess,json,time
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];os.chdir(B);E=B/'research/outer_cells/evidence';MID=4116796;child=None
record={'start_utc':datetime.now(timezone.utc).isoformat(),'controller_pid':os.getpid(),'paused_worker':MID,'tag':'full_q16','run_timeout_seconds':1800,'status':'PREPARING'}
def save():
 record['last_utc']=datetime.now(timezone.utc).isoformat();(E/'full_serialized_run.json').write_text(json.dumps(record,indent=2)+'\n')
def stop(signum,frame):raise InterruptedError('controller signal '+str(signum))
for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,stop)
assert b'research/middle_residual/code/run_cells.py' in Path('/proc/'+str(MID)+'/cmdline').read_bytes()
os.kill(MID,signal.SIGSTOP);record['status']='MIDDLE_PAUSED';save()
try:
 for stage,args,seconds in [('covering',['research/outer_cells/code/run_covering.py','--tag','full_q16'],1800),('audit',['research/outer_cells/code/audit_covering.py','--tag','full_q16'],120)]:
  with (E/('full_'+stage+'.log')).open('w') as log:
   child=subprocess.Popen([sys.executable]+args,stdout=log,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
   record['status']='RUNNING_'+stage.upper();record['child_pid']=child.pid;save();rc=child.wait(timeout=seconds);record[stage+'_returncode']=rc;save();child=None
   if rc:raise RuntimeError(stage+' failed: '+str(rc))
 record['status']='COMPLETED'
except BaseException as exc:
 record['status']='FAILED';record['error']=repr(exc)
finally:
 if child is not None and child.poll() is None:
  child.terminate()
  try:child.wait(timeout=10)
  except subprocess.TimeoutExpired:child.kill();child.wait(timeout=10)
 os.kill(MID,signal.SIGCONT);record['resumed_middle']=True;record['end_utc']=datetime.now(timezone.utc).isoformat();save();print(json.dumps(record),flush=True)
