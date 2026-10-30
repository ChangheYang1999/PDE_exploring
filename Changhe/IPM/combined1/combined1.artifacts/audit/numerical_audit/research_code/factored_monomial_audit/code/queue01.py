from pathlib import Path
from datetime import datetime,timezone
import os,signal,subprocess,json,time
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/factored_monomial_audit';PID=3919081
now=lambda:datetime.now(timezone.utc).isoformat()
start=time.monotonic();paused=resumed=False;rows=[]
env=os.environ.copy();env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(ROOT/'tmp'))
try:
 cmd=Path(f'/proc/{PID}/cmdline').read_bytes();assert b'weak_v3.py' in cmd
 assert Path(f'/proc/{PID}/cwd').resolve()==ROOT
 os.kill(PID,signal.SIGSTOP);paused=True
 print('START',now(),'paused',PID,flush=True)
 for i,script in enumerate(['research/rational_pole_moments/code/accept_t4.py','research/factored_monomial_audit/code/check.py'],1):
  tick=time.monotonic();stamp=now();log=BASE/f'logs/serial01_{i}.log'
  argv=['taskset','-c','57','nice','-n','19','python3','-B',script]
  with log.open('x') as stream:r=subprocess.run(argv,cwd=ROOT,env=env,stdout=stream,stderr=subprocess.STDOUT,timeout=540)
  row={'start_utc':stamp,'finish_utc':now(),'argv':argv,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-tick,'log':str(log.relative_to(ROOT))};rows.append(row);print(json.dumps(row),flush=True)
  if r.returncode:break
finally:
 if paused:
  try:os.kill(PID,signal.SIGCONT);resumed=True
  except ProcessLookupError:pass
 out={'utc':now(),'paused_pid':PID,'pause_applied':paused,'resumed':resumed,'jobs':rows,'elapsed_seconds':time.monotonic()-start}
 with (BASE/'verification/queue01_finished.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('FINISHED',now(),'resumed',resumed,'seconds',out['elapsed_seconds'],flush=True)
