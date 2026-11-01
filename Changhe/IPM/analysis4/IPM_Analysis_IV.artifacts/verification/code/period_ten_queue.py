"""Serialized Q10 verification after the exact obstruction worker exits."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time,fcntl,shutil
sys.dont_write_bytecode=True
STOP=datetime.fromisoformat('2026-11-01T00:30:00+00:00')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def live(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
 except FileNotFoundError:return False
while live(3778292):time.sleep(15)
assert Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json').exists()
# The old coordinator is stopped and has no child. Replace it with the locked code.
if live(1404965):
 os.kill(1404965,15);os.kill(1404965,18)
with Path('scratch/later_conditional_queue_locked.log').open('a') as out:
 p=subprocess.Popen(['taskset','-c','18','nice','-n','19',sys.executable,'-B','code/later_conditional_queue.py'],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
 print(json.dumps(dict(at=stamp(),stage='locked_later_queue',pid=p.pid)),flush=True)
def run(script,args=None,label=None):
 if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
 assert shutil.disk_usage('.').free>20_000_000_000
 with Path('scratch/core18.lock').open('a') as lock,Path('scratch/'+(label or script.removesuffix('.py'))+'.log').open('a') as f:
  fcntl.flock(lock,fcntl.LOCK_EX);start=time.monotonic();p=subprocess.Popen(['taskset','-c','18','nice','-n','19',sys.executable,'-B','code/'+script]+(args or []),stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=stamp(),stage='start',script=script,label=label,pid=p.pid)),flush=True);rc=p.wait()
 print(json.dumps(dict(at=stamp(),stage='end',script=script,label=label,exit_code=rc,elapsed_s=time.monotonic()-start)),flush=True)
 if rc:raise SystemExit(rc)
for script in ['period_ten_lead_comparison.py','period_ten_potential_log.py','period_ten_symbolic_response.py','period_ten_response_bounds.py','period_ten_response_bounds_replay.py']:
 run(script)
run('full_polar_response_comparison.py',['--Q','10'],'full_polar_response_Q10')
for i in range(1,15):
 for script in ['period_ten_prefix.py','period_ten_prefix_replay.py','period_ten_polar_replay.py']:
  args=['--Q','10','--root',str(i)]
  if script=='period_ten_prefix.py':args+=['--N','80','--bits','1536']
  if script=='period_ten_polar_replay.py':args+=['--bits','2048']
  run(script,args,f'{script.removesuffix(".py")}_root{i}')
print(json.dumps(dict(at=stamp(),stage='COMPLETE')),flush=True)
