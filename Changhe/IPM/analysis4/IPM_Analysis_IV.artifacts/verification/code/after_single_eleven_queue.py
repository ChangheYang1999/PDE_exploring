"""Complete and replay the single-harmonic certificate after exact tuning."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3371905/cmdline')
while p.exists() and b'after_tail_recompute_queue.py' in p.read_bytes():time.sleep(10)
for name,args in [('single_eleven_certificate',[]),('single_eleven_replay',[]),('tail_response_recompute',['--roots','1'])]:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+name+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=r.returncode)),flush=True)
 if r.returncode:break
