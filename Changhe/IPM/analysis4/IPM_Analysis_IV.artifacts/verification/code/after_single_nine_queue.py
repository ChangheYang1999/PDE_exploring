"""Check a real response crossing and another finite high-mode probe."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/4053575/cmdline')
while p.exists():
 try:
  if b'after_extremal_probe_queue.py' not in p.read_bytes():break
 except FileNotFoundError:break
 time.sleep(10)
for name,args in [('noninteger_response_zero',[]),('extremal_single_probe',['--h','2','--Q','5'])]:
 label=name+('_h2Q5' if args else '')
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=label)),flush=True)
 with Path('scratch',label+'.log').open('wb') as log:
  result=subprocess.run([sys.executable,'-B','code/'+name+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=label,code=result.returncode)),flush=True)
