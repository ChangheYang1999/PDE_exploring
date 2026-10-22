"""Run short checks while the one heavy background worker is stopped."""
import os,subprocess,signal,json
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/frozen_holder/evidence';utc=lambda:datetime.now(timezone.utc).isoformat();worker=2005442
meta={'start_utc':utc(),'wrapper_pid':os.getpid(),'paused_worker':worker,'commands':[]};os.kill(worker,signal.SIGSTOP)
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env.pop('PYTHONOPTIMIZE',None)
try:
 for name in ['check_exponents','audit_output']:
  row={'name':name,'start_utc':utc()}
  with (E/(name+'_run.log')).open('w') as f:
   p=subprocess.Popen(['timeout','8m','python3',str(B/f'research/frozen_holder/code/{name}.py')],env=env,stdout=f,stderr=subprocess.STDOUT);row['timeout_pid']=p.pid;meta['commands'].append(row);(E/'local_run.json').write_text(json.dumps(meta,indent=2)+'\n');ret=p.wait()
  row.update(end_utc=utc(),returncode=ret)
  if ret:break
finally:
 os.kill(worker,signal.SIGCONT);meta.update(end_utc=utc(),resumed_worker=True);(E/'local_run.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta),flush=True)
