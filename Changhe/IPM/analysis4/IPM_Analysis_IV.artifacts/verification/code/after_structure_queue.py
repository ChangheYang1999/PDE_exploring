"""Finish a summary redundancy check and compact closed evidence on core17."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3629897/cmdline')
while p.exists():
    try:
        if b'after_eleven_review_queue.py' not in p.read_bytes():break
    except FileNotFoundError:break
    time.sleep(10)
for name in ['summary_scope_check','compress_closed_low_order']:
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='start',job=name)),flush=True)
    with Path('scratch',name+'.log').open('wb') as log:
        r=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='exit',job=name,code=r.returncode)),flush=True)
    if r.returncode:break
