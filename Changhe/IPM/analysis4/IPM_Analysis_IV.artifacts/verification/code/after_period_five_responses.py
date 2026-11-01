from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,json,sys
pid=388965
while True:
 try:state=Path(f'/proc/{pid}/stat').read_text().rsplit(')',1)[1].split()[0]
 except FileNotFoundError:break
 if state=='Z':break
 time.sleep(2)
if not Path('research/130_period_five_tuning/verification/obstruction_checks.json').exists():raise SystemExit('No completed obstruction calculation')
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='period_five_responses')),flush=True)
with open('logs/period_five_responses.log','w') as out:
 result=subprocess.run([sys.executable,'-u','code/period_five_responses.py'],stdout=out,stderr=subprocess.STDOUT)
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),returncode=result.returncode)),flush=True)
