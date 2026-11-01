"""Tail-only response and radius checks sequentially after core18 prefix work."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/2412324/cmdline')
while p.exists() and b'after_sensitivity_queue.py' in p.read_bytes():time.sleep(20)
for index in [4,1,2,3]:
    for name in ['tail_response_radii','tail_response_replay']:
        label=name+'_root'+str(index)
        print(json.dumps(dict(job=label,event='start',time=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
        with Path('scratch',label+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+name+'.py','--roots',str(index)],stdout=log,stderr=subprocess.STDOUT)
        print(json.dumps(dict(job=label,event='exit',code=r.returncode,time=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
        if r.returncode:break
