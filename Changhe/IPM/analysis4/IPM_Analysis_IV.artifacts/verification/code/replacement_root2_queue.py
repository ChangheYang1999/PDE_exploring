"""Complete root2 replacement before releasing root3 in the original queue."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,signal,subprocess,sys,time
for name in ['tail_response_radii','tail_response_replay','tail_response_recompute']:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'_root2_replacement.log').open('wb') as log:
  result=subprocess.run([sys.executable,'-B','code/'+name+'.py','--roots','2'],stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
p=Path('/proc/3311940/cmdline')
if p.exists() and b'tail_response_radii.py' in p.read_bytes():
 os.kill(3311940,signal.SIGKILL)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='released_root3',old_direct_attempt_pid=3311940)),flush=True)
p=Path('/proc/2720854/cmdline')
while p.exists():
 try:
  if b'after_prefix_queue.py' not in p.read_bytes():break
 except FileNotFoundError:break
 time.sleep(10)
with Path('scratch/tail_response_recompute_root3.log').open('wb') as log:
 result=subprocess.run([sys.executable,'-B','code/tail_response_recompute.py','--roots','3'],stdout=log,stderr=subprocess.STDOUT)
print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='root3_recompute_exit',code=result.returncode)),flush=True)
