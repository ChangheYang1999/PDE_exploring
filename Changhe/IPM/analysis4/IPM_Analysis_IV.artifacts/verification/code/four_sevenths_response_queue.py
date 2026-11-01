from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,json,sys
os.sched_setaffinity(0,{18})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
for i in range(1,4):
    for name in ['four_sevenths_certificate','four_sevenths_replay']:
        start=time.monotonic()
        with Path(f'scratch/{name}_root{i}.log').open('a') as f:
            p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py','--root',str(i)],stdout=f,stderr=subprocess.STDOUT)
            print(json.dumps(dict(started=stamp(),name=name,root=i,pid=p.pid)),flush=True)
            rc=p.wait()
        print(json.dumps(dict(finished=stamp(),name=name,root=i,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
        if rc:raise SystemExit(rc)
