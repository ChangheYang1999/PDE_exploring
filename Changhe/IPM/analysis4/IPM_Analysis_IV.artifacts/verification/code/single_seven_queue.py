from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,time,json,sys
os.sched_setaffinity(0,{17})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
for name in ['single_seven_certificate','single_seven_replay']:
    start=time.monotonic()
    with Path(f'scratch/{name}.log').open('a') as f:
        p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py'],stdout=f,stderr=subprocess.STDOUT)
        print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,pid=p.pid)),flush=True)
        rc=p.wait()
    print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
    if rc:raise SystemExit(rc)
