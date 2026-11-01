from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
os.sched_setaffinity(0,{18})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
while Path('/proc/3349408').exists():
 try:
  if Path('/proc/3349408/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(15)
start=time.monotonic()
with Path('scratch/period_necessary_radii.log').open('a') as f:
 p=subprocess.Popen([sys.executable,'-B','code/period_necessary_radii.py'],stdout=f,stderr=subprocess.STDOUT)
 print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),pid=p.pid)),flush=True)
 rc=p.wait()
print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
raise SystemExit(rc)
