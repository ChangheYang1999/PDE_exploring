"""Check the new high-harmonic branch after the root-4 tail replay."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3249860/cmdline')
while p.exists() and b'tail_response_recompute.py' in p.read_bytes():time.sleep(10)
for script,args,label in [('single_eleven_probe',[],'single_eleven_probe'),('high_harmonic_tuning',['--mode','11','--blocks','3'],'high_harmonic_sin11')]:
 print(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='start',job=label)),flush=True)
 with Path('scratch',label+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+script+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='exit',job=label,code=r.returncode)),flush=True)
 if r.returncode:break
