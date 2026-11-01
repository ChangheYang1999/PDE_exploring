"""Compute the top-mode radius after the two order390 audits, on core18."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/594951/cmdline')
while p.exists():
 try:
  if b'after_root2_replacement_queue.py' not in p.read_bytes():break
 except FileNotFoundError:break
 time.sleep(10)
for name in ['candidate_top_radius']:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'.log').open('wb') as log:
  result=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=result.returncode)),flush=True)
