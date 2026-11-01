"""Run the independent global-infimum check after the symbolic data finishes."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
p=Path('research/282_period_ten_symbolic_response/verification/checks.json')
while datetime.now(timezone.utc)<datetime(2026,11,1,0,20,tzinfo=timezone.utc):
 if p.exists():
  try:
   if json.loads(p.read_bytes())['all_checks_pass']:break
  except (ValueError,KeyError):pass
 time.sleep(15)
else:raise SystemExit('Cutoff before symbolic certificate')
with Path('scratch/period_ten_response_infima.log').open('w') as f:
 result=subprocess.run(['taskset','-c','17','nice','-n','19','flock','scratch/core17.lock',sys.executable,'code/period_ten_response_infima.py'],env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'),stdout=f,stderr=subprocess.STDOUT)
 print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),returncode=result.returncode)),flush=True)
 raise SystemExit(result.returncode)
