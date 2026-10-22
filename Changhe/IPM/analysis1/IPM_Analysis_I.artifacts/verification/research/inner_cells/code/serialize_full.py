"""Serialize the inner covering with the only other verifier heavy worker."""
import os,sys,signal,subprocess,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];os.chdir(B);E=B/'research/inner_cells/evidence';MID=4116796;child=None
assert sys.flags.optimize==0 and os.environ.get('PYTHONOPTIMIZE') is None
r={'start_utc':datetime.now(timezone.utc).isoformat(),'controller_pid':os.getpid(),'paused_worker':MID,'tag':'full_q16','status':'PREPARING','stages':[],'controller_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
def save():r['last_utc']=datetime.now(timezone.utc).isoformat();(E/'full_serialized_run.json').write_text(json.dumps(r,indent=2)+'\n')
def stop(sig,frame):raise InterruptedError('signal '+str(sig))
for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,stop)
assert b'research/middle_residual/code/run_cells.py' in Path('/proc/'+str(MID)+'/cmdline').read_bytes()
os.kill(MID,signal.SIGSTOP);r['status']='MIDDLE_PAUSED';save()
try:
 for stage,args,seconds in [('covering',['research/inner_cells/code/run_covering.py','--tag','full_q16'],1800),('audit',['research/inner_cells/code/audit_covering.py','--tag','full_q16'],120)]:
  with (E/('full_'+stage+'.log')).open('w') as log:
   child=subprocess.Popen([sys.executable]+args,stdout=log,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
   rec={'stage':stage,'child_pid':child.pid,'start_utc':datetime.now(timezone.utc).isoformat(),'expected_argv':[sys.executable]+args};r['stages'].append(rec);r['status']='RUNNING_'+stage.upper();save()
   for attempt in range(100):
    observed=Path('/proc/'+str(child.pid)+'/cmdline').read_bytes().split(b'\0');cmd=[x.decode() for x in observed if x]
    if cmd[1:]==args:break
    time.sleep(.01)
   assert cmd[1:]==args and '-O' not in cmd and '-OO' not in cmd
   env=Path('/proc/'+str(child.pid)+'/environ').read_bytes().split(b'\0');opt=[x for x in env if x.startswith(b'PYTHONOPTIMIZE=')];assert not opt
   rec['observed_cmdline']=cmd;rec['PYTHONOPTIMIZE']='unset';rec['observed_executable']=os.readlink('/proc/'+str(child.pid)+'/exe');save()
   rc=child.wait(timeout=seconds);rec['returncode']=rc;rec['end_utc']=datetime.now(timezone.utc).isoformat();save();child=None
   if rc:raise RuntimeError(stage+' failed: '+str(rc))
 r['status']='COMPLETED'
except BaseException as exc:r['status']='FAILED';r['error']=repr(exc)
finally:
 if child is not None and child.poll() is None:
  child.terminate()
  try:child.wait(timeout=10)
  except subprocess.TimeoutExpired:child.kill();child.wait(timeout=10)
 os.kill(MID,signal.SIGCONT);r['resumed_middle']=True;r['end_utc']=datetime.now(timezone.utc).isoformat();save();print(json.dumps(r),flush=True)
