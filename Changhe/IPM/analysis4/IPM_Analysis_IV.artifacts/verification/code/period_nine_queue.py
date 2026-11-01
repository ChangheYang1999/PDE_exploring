"""Pinned sequential Q9 certificate queue, leaving core18 for late numerics."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time,shutil
os.sched_setaffinity(0,{17});os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
root=Path('research/267_period_nine_tuning/verification')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
while Path('/proc/683001').exists():
 try:
  if Path('/proc/683001/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(10)
p=root/'obstruction_checks.json';assert p.exists();d=json.loads(p.read_text());assert d['all_checks_pass']
for index in range(1,len(d['real_roots'])+1):
 for name in ('period_nine_certificate','period_nine_replay'):
  assert shutil.disk_usage('.').free>20*10**9
  if datetime.now(timezone.utc)>=datetime(2026,11,1,0,0,tzinfo=timezone.utc):raise SystemExit('Q9 new-work cutoff')
  start=time.monotonic()
  with Path(f'scratch/{name}_root{index}.log').open('a') as f:
   p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py','--root',str(index)],stdout=f,stderr=subprocess.STDOUT)
   print(json.dumps(dict(at=stamp(),root=index,script=name,pid=p.pid)),flush=True);rc=p.wait()
  print(json.dumps(dict(at=stamp(),root=index,script=name,exit_code=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
  if rc:raise SystemExit(rc)
