"""Run small fit and specified-norm audits after the core17 job completes."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/2509080/cmdline')
while p.exists() and b'after_root3_queue.py' in p.read_bytes():time.sleep(20)
for name in ['local_fit_ambiguity','sample_amplification']:
    print(json.dumps(dict(job=name,event='start',time=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
    with Path('scratch',name+'_v2.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(job=name,event='exit',code=r.returncode,time=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
