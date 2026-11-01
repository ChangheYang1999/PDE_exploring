from pathlib import Path
from datetime import datetime,timezone
import os,time,subprocess,json,sys
while True:
 try:
  if Path('/proc/3869052/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(15)
with Path('scratch/floating_period_audit.log').open('w') as f:
 p=subprocess.run(['taskset','-c','18','nice','-n','19',sys.executable,'code/floating_period_audit.py'],stdout=f,stderr=subprocess.STDOUT,env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'))
print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),exit_code=p.returncode)),flush=True)
