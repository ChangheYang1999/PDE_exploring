"""One-core follow-up of the finite extremal-harmonic probe."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/3852126/cmdline')
while p.exists():
    try:
        if b'after_scope_queue.py' not in p.read_bytes():break
    except FileNotFoundError:break
    time.sleep(10)
probe=Path('research/231_extremal_single_harmonics/verification/h2_Q7_probe.json')
assert probe.exists() and json.loads(probe.read_text())['all_separated']
for name in ['single_nine_certificate','single_nine_replay']:
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='start',job=name)),flush=True)
    with Path('scratch',name+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),event='exit',job=name,code=r.returncode)),flush=True)
    if r.returncode:break
