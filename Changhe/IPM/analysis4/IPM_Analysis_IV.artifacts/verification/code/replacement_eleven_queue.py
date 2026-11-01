"""Finish the replacement certificate and saved-prefix replay before releasing dependents."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,signal,subprocess,sys,time
for name,args in [('single_eleven_certificate',[]),('single_eleven_replay',[]),('tail_response_recompute',['--roots','1'])]:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'_replacement.log').open('wb') as log:
  result=subprocess.run([sys.executable,'-B','code/'+name+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=result.returncode)),flush=True)
 if result.returncode:
  raise SystemExit(result.returncode)
p=Path('/proc/3492014/cmdline')
if p.exists() and b'single_eleven_certificate.py' in p.read_bytes():
 os.kill(3492014,signal.SIGKILL)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='released_dependents',old_direct_attempt_pid=3492014)),flush=True)
