"""Sequential storage and exact compatibility work on core18."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,json
for name in ['compress_closed_low_order','four_sevenths_obstruction']:
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='start',job=name)),flush=True)
 with Path('scratch',name+'_1731.log').open('wb') as f:r=subprocess.run([sys.executable,'-B','code/'+name+'.py'],stdout=f,stderr=subprocess.STDOUT)
 print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(timespec='seconds'),stage='exit',job=name,code=r.returncode)),flush=True)
 if r.returncode:break
