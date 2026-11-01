"""Run finite Q9 comparisons when the independent obstruction is available."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
os.sched_setaffinity(0,{18});os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
source=Path('research/267_period_nine_tuning/verification/obstruction_checks.json')
while not source.exists():
 if datetime.now(timezone.utc)>=datetime(2026,11,1,0,15,tzinfo=timezone.utc):raise SystemExit('new-work cutoff')
 time.sleep(5)
assert json.loads(source.read_text())['all_checks_pass']
for name in ['period_nine_lead_comparison','period_nine_potential_log']:
 start=time.monotonic()
 with Path('scratch',name+'.log').open('a') as out:
  child=subprocess.Popen([sys.executable,'-B','code/'+name+'.py'],stdout=out,stderr=subprocess.STDOUT)
  print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),script=name,pid=child.pid)),flush=True)
  rc=child.wait()
 print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),script=name,exit_code=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
 if rc:raise SystemExit(rc)
