from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,json,sys
pid=182576
while True:
 try:state=Path(f'/proc/{pid}/stat').read_text().rsplit(')',1)[1].split()[0]
 except FileNotFoundError:break
 if state=='Z':break
 time.sleep(2)
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='period_five')),flush=True)
with open('logs/period_five_exact.log','w') as out:
 result=subprocess.run([sys.executable,'-u','code/period_five_exact.py'],stdout=out,stderr=subprocess.STDOUT)
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),returncode=result.returncode)),flush=True)
