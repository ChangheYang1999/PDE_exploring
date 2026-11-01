"""Sequential second-core prefix and independent replay campaign."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,time,json,os,gzip
sys.dont_write_bytecode=True
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def active(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
 except FileNotFoundError:return False
while active(3836920):time.sleep(2)
for Q in [7,8]:
 for index in [1,2,4,5,6,7,8,9,10]:
  for script,extra in [('period_high_prefix.py',['--N',str(8*Q)]),('period_polar_prefix_replay.py',[]),('period_high_prefix_replay.py',[])]:
   start=time.monotonic()
   with Path(f'scratch/Q{Q}_root{index}_{script[:-3]}.log').open('w') as log:
    p=subprocess.Popen([sys.executable,'-B','code/'+script,'--Q',str(Q),'--root',str(index)]+extra,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(at=stamp(),Q=Q,root=index,script=script,pid=p.pid)),flush=True);code=p.wait()
    print(json.dumps(dict(at=stamp(),Q=Q,root=index,script=script,exit_code=code,actual_elapsed_s=time.monotonic()-start)),flush=True)
   if code:break
