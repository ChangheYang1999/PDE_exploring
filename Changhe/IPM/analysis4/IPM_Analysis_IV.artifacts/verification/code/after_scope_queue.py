"""Probe a second high-harmonic profile after earlier core17 checks finish."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3811246/cmdline')
while p.exists():
    try:
        if b'after_structure_queue.py' not in p.read_bytes():break
    except FileNotFoundError:break
    time.sleep(10)
name='extremal_single_probe'
print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='start',job=name)),flush=True)
with Path('scratch',name+'.log').open('wb') as log:
    r=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='exit',job=name,code=r.returncode)),flush=True)
