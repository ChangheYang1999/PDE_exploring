"""Serialize this lane's finite audit with the existing heavy residual process."""
import os,sys,signal,subprocess,json,time,resource
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/flow_scalars/evidence'
def now():return datetime.now(timezone.utc).isoformat()
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env.pop('PYTHONOPTIMIZE',None)
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):env[name]='1'
worker=2005442;assert b'run_full.py' in Path('/proc/'+str(worker)+'/cmdline').read_bytes()
rec={'utc_start':now(),'wrapper_pid':os.getpid(),'paused_pid':worker,'steps':[]}
os.kill(worker,signal.SIGSTOP);rec['pause_utc']=now();(E/'serial_runtime.json').write_text(json.dumps(rec,indent=2)+'\n')
try:
 for name in ('check_scalars','audit_saved'):
  with (E/(name+'.log')).open('w') as log:
   result=subprocess.run([sys.executable,str(B/'research/flow_scalars/code'/ (name+'.py'))],cwd=B,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1800)
  rec['steps'].append({'name':name,'returncode':result.returncode,'utc':now()});(E/'serial_runtime.json').write_text(json.dumps(rec,indent=2)+'\n')
  if result.returncode:break
finally:
 os.kill(worker,signal.SIGCONT);rec['resume_utc']=now();rec['resumed']=True;(E/'serial_runtime.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
