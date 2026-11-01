from pathlib import Path
from datetime import datetime,timezone
import os,signal,subprocess,sys,time,json
parent=4168281
children=[]
for p in Path('/proc').iterdir():
 if not p.name.isdigit():continue
 try:
  stat=p.joinpath('stat').read_text().rsplit(')',1)[1].split()
  if int(stat[1])==parent and stat[0]!='Z':children.append(int(p.name))
 except (FileNotFoundError,PermissionError,ProcessLookupError):continue
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),waiting_for=children)),flush=True)
for pid in children:
 while True:
  try:status=Path(f'/proc/{pid}/stat').read_text().split()[2]
  except FileNotFoundError:break
  if status=='Z':break
  time.sleep(2)
try:
 with open('logs/tuned_checkpoint_audit.log','w') as out:
  p=subprocess.run([sys.executable,'-u','code/tuned_checkpoint_audit.py'],stdout=out,stderr=subprocess.STDOUT)
 print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),tuned_audit_returncode=p.returncode)),flush=True)
finally:
 os.kill(parent,signal.SIGCONT)
 print(json.dumps(dict(resumed_prime_parent=parent)),flush=True)
