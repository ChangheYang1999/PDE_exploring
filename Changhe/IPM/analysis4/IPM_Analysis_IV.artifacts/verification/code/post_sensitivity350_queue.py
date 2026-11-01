from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,json,sys
os.sched_setaffinity(0,{18});os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
while Path('/proc/1527590').exists():
 try:
  if Path('/proc/1527590/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(10)
for name in ['sensitivity_rounding350','single_seven_polar_comparison','extremal_necessary_radii']:
 with Path(f'scratch/{name}.log').open('a') as f:
  p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py'],stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,pid=p.pid)),flush=True);rc=p.wait()
 print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,returncode=rc)),flush=True)
 if rc:raise SystemExit(rc)
