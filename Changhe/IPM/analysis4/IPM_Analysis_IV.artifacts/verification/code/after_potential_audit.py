from pathlib import Path
from datetime import datetime,timezone
import time,sys,subprocess,json
while True:
 try:
  if Path('/proc/4022967/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(3)
with open('logs/tuned_algebraic_certificate.log','w') as out:
 r=subprocess.run([sys.executable,'-u','code/tuned_algebraic_certificate.py'],stdout=out,stderr=subprocess.STDOUT)
print(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),returncode=r.returncode)),flush=True)
