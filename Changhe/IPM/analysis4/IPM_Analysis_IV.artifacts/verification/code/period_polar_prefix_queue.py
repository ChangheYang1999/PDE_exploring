from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,time,json
for Q in [7,8]:
 with Path(f'scratch/Q{Q}_root3_polar_prefix_replay.log').open('w') as out:
  start=time.monotonic();p=subprocess.Popen([sys.executable,'-B','code/period_polar_prefix_replay.py','--Q',str(Q),'--root','3'],stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),Q=Q,pid=p.pid)),flush=True);code=p.wait()
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),Q=Q,exit_code=code,actual_elapsed_s=time.monotonic()-start)),flush=True)
  if code:raise SystemExit(code)
