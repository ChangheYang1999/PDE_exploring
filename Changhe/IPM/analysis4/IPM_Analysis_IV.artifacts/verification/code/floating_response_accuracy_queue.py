from pathlib import Path
from datetime import datetime,timezone
import os,time,subprocess,json,sys
while True:
 try:
  state=Path('/proc/37956/stat').read_text().split()[2]
  if state=='Z':break
 except FileNotFoundError:break
 time.sleep(10)
with Path('scratch/floating_response_accuracy.log').open('w') as f:
 p=subprocess.run(['taskset','-c','18','nice','-n','19',sys.executable,'code/floating_response_accuracy.py'],stdout=f,stderr=subprocess.STDOUT,env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'))
print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),exit_code=p.returncode)),flush=True)
