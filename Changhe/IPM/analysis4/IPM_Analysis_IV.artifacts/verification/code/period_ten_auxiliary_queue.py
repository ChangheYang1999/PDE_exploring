"""Run the short necessary-radius audit after the exact prefix is available."""
from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,sys,time,json
sys.dont_write_bytecode=True
stop=datetime.fromisoformat('2026-11-01T00:30:00+00:00')
source=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
while not source.exists():
 if datetime.now(timezone.utc)>=stop:raise SystemExit('cutoff before input')
 time.sleep(15)
env=os.environ.copy();env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
cmd=['flock','scratch/core17.lock','taskset','-c','17','nice','-n','19',sys.executable,'-B','code/period_ten_necessary_radii.py']
print(json.dumps(dict(at=stamp(),stage='waiting_for_core17',script='period_ten_necessary_radii.py')),flush=True)
with Path('scratch/period_ten_necessary_radii.log').open('ab') as log:
 p=subprocess.Popen(cmd,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,env=env);r=p.wait()
print(json.dumps(dict(at=stamp(),stage='end',exit_code=r)),flush=True)
