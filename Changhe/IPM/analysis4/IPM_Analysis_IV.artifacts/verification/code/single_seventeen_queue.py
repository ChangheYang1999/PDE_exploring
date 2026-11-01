from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,json,sys
os.sched_setaffinity(0,{17})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
while Path('/proc/1280282').exists():
 try:
  if Path('/proc/1280282/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(15)
probe=json.loads(Path('research/231_extremal_single_harmonics/verification/h3_Q13_probe.json').read_text())
assert probe['all_checks_pass'] and probe['all_separated']
for name in ['single_seventeen_certificate','single_seventeen_replay']:
 start=time.monotonic()
 with Path(f'scratch/{name}.log').open('a') as f:
  p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py'],stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,pid=p.pid)),flush=True)
  rc=p.wait()
 print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
 if rc:raise SystemExit(rc)
