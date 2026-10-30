from pathlib import Path
from datetime import datetime, timezone
import os, time, subprocess, json, shutil
R=Path(__file__).resolve().parents[3]
D=R/'research/rational_pole_moments'
def now():return datetime.now(timezone.utc).isoformat()
def alive(pid):
 p=Path(f'/proc/{pid}/stat')
 try:return p.read_text().split()[2] != 'Z'
 except FileNotFoundError:return False
pid=3283465
print(now(),'waiting for derivative stage',pid,flush=True)
while alive(pid):time.sleep(2)
assert shutil.disk_usage(R).free>=20*10**9
jobs=[('triangular_tail_audit','code/check.py',120),('rational_pole_moments','code/check.py',540)]
for topic,script,limit in jobs:
 base=R/'research'/topic;(base/'logs').mkdir(exist_ok=True)
 log=base/'logs/run01.log';start=now();tick=time.monotonic()
 with log.open('x') as f:
  p=subprocess.Popen(['python3','-B',str(base/script)],stdout=f,stderr=subprocess.STDOUT,cwd=R)
  print(now(),'started',topic,p.pid,flush=True)
  try:rc=p.wait(timeout=limit);timed=False
  except subprocess.TimeoutExpired:p.terminate();rc=p.wait(timeout=10);timed=True
 record={'started_utc':start,'ended_utc':now(),'pid':p.pid,'exit':rc,'timed_out':timed,'elapsed_seconds':time.monotonic()-tick}
 with (base/'verification/queue_exit01.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
 print(now(),'completed',topic,record,flush=True)
 if rc:break
