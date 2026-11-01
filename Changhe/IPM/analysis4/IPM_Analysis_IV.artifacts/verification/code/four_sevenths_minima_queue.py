from pathlib import Path
from datetime import datetime,timezone
import os,sys,subprocess,json
os.sched_setaffinity(0,{18})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
for args in [[],['--replay']]:
 print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),args=args)),flush=True)
 p=subprocess.run([sys.executable,'-B','code/four_sevenths_minima.py',*args])
 if p.returncode:raise SystemExit(p.returncode)
