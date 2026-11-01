"""One-core queue after the single-harmonic minimum check."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,time,json
sys.dont_write_bytecode=True
def active(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
 except FileNotFoundError:return False
while active(3076886):time.sleep(5)
for Q in [8,7]:
 for script,args in [('period_tail_prefix.py',[]),('period_tail_polar_replay.py',['--root','3','--bits','3072']),('period_tail_certificate.py',[]),('period_tail_replay.py',[])]:
  start=time.monotonic()
  with Path(f'scratch/Q{Q}_{script[:-3]}.log').open('w') as log:
   p=subprocess.Popen([sys.executable,'-B','code/'+script,'--Q',str(Q)]+args,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT)
   print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),Q=Q,script=script,pid=p.pid)),flush=True);code=p.wait()
   print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),Q=Q,script=script,exit_code=code,actual_elapsed_s=time.monotonic()-start)),flush=True)
  if code:break
