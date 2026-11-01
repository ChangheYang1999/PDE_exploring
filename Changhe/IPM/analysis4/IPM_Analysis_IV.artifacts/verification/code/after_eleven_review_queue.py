"""Run the independent structure check after the active core-17 queue ends."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3471573/cmdline')
while p.exists():
    try:
        if b'after_single_eleven_queue.py' not in p.read_bytes():break
    except FileNotFoundError:break
    time.sleep(10)
for name,args in [('single_eleven_structure',[]),('modular_grid_audit',[])]:
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
    with Path('scratch',name+'.log').open('wb') as log:
        result=subprocess.run([sys.executable,'-B','code/'+name+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=result.returncode)),flush=True)
    if result.returncode:break
