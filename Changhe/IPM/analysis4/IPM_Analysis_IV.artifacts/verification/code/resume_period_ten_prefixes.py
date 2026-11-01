"""Resume only the audited Q10 prefix and replay stages."""
from pathlib import Path
from datetime import datetime,timezone
import fcntl,json,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
STOP=datetime.fromisoformat('2026-11-01T00:30:00+00:00')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
for index in range(1,15):
 for script in ['period_ten_prefix.py','period_ten_prefix_replay.py','period_ten_polar_replay.py']:
  if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
  assert shutil.disk_usage('.').free>20_000_000_000
  args=['--Q','10','--root',str(index)]
  if script=='period_ten_prefix.py':args+=['--N','80','--bits','1536']
  if script=='period_ten_polar_replay.py':args+=['--bits','2048']
  label=f'{script.removesuffix(".py")}_root{index}'
  with Path('scratch/core18.lock').open('a') as lock,Path('scratch/'+label+'.log').open('a') as log:
   fcntl.flock(lock,fcntl.LOCK_EX);begin=time.monotonic()
   p=subprocess.Popen(['taskset','-c','18','nice','-n','19',sys.executable,'-B','code/'+script]+args,stdout=log,stderr=subprocess.STDOUT)
   print(json.dumps(dict(at=stamp(),stage='start',script=script,root=index,pid=p.pid)),flush=True)
   rc=p.wait()
  print(json.dumps(dict(at=stamp(),stage='end',script=script,root=index,exit_code=rc,elapsed_s=time.monotonic()-begin)),flush=True)
  if rc:raise SystemExit(rc)
print(json.dumps(dict(at=stamp(),stage='COMPLETE')),flush=True)
