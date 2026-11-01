from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,sys
os.sched_setaffinity(0,{18});os.nice(19)
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
for args,log in [([], 'sharp_radii'),(['--replay'],'sharp_radii_replay')]:
 with Path('scratch/four_sevenths_'+log+'.log').open('a') as out:
  code=subprocess.call([sys.executable,'-B','code/four_sevenths_sharp_radii.py']+args,stdout=out,stderr=subprocess.STDOUT)
 print(datetime.now(timezone.utc).isoformat(),log,code,flush=True)
 if code:raise SystemExit(code)
