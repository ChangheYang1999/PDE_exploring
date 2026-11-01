"""Audit order390 after the root2/root3 replacement jobs finish on core18."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/561508/cmdline')
while p.exists():
 try:
  if b'replacement_root2_queue.py' not in p.read_bytes():break
 except FileNotFoundError:break
 time.sleep(10)
for name in ['reset390_conditional_audit','shifted_drift390_audit']:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'.log').open('wb') as log:
  result=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=result.returncode)),flush=True)
 if result.returncode:break
