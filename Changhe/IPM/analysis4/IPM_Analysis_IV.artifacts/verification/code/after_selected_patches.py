from pathlib import Path
from datetime import datetime,timezone
import time,subprocess,sys,json
pid=107953
while True:
 try:state=Path(f'/proc/{pid}/stat').read_text().split()[2]
 except FileNotFoundError:break
 if state=='Z':break
 time.sleep(2)
for name in ['sharper_tuned_radius_check','amplitude_probe_audit','selected_recipe_restore_check']:
 print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),step=name)),flush=True)
 with open('logs/'+name+'.log','w') as out:
  result=subprocess.run([sys.executable,'-u','code/'+name+'.py'],stdout=out,stderr=subprocess.STDOUT,timeout=570)
 print(json.dumps(dict(step=name,returncode=result.returncode)),flush=True)
 if result.returncode:break
