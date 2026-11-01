"""Sequential core-17 Q9 prefixes and independent replays; no parallel children."""
from pathlib import Path
from datetime import datetime, timezone
import os,time,subprocess,sys,json
sys.dont_write_bytecode=True
ROOT=Path('research/280_period_nine_prefixes')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def run(script,index):
 cmd=[sys.executable,'code/'+script,'--Q','9','--root',str(index)]
 if script=='period_nine_prefix.py':cmd+=['--N','72']
 path=Path('scratch')/f'Q9_root{index}_{script[:-3]}.log'
 print(json.dumps(dict(at=stamp(),stage='start',root=index,script=script)),flush=True)
 with path.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 print(json.dumps(dict(at=stamp(),stage='end',root=index,script=script,returncode=r.returncode)),flush=True)
 assert r.returncode==0,(script,index)
while Path('/proc/3581631').exists():
 try:
  if Path('/proc/3581631/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(1)
for index in [3,4,5,6,7,8,9,2,10,1]:
 if index!=3:run('period_nine_prefix.py',index)
 run('period_nine_prefix_replay.py',index)
 run('period_nine_polar_replay.py',index)
print(json.dumps(dict(at=stamp(),complete=True)),flush=True)
