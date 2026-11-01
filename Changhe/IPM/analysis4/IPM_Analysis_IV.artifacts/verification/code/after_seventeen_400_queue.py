from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
os.sched_setaffinity(0,{17})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
while Path('/proc/2274290').exists():
    try:
        if Path('/proc/2274290/stat').read_text().split()[2]=='Z':break
    except FileNotFoundError:break
    time.sleep(15)
for name in ['reset400_conditional_audit','shifted_drift400_audit']:
    start=time.monotonic()
    with Path(f'scratch/{name}.log').open('a') as f:
        p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py'],stdout=f,stderr=subprocess.STDOUT)
        print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,pid=p.pid)),flush=True)
        rc=p.wait()
    print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),name=name,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
    if rc:raise SystemExit(rc)
