"""One pinned worker for the ten independently isolated period-eight roots."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
os.sched_setaffinity(0,{18})
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
while Path('/proc/3098024').exists():
    try:
        if Path('/proc/3098024/stat').read_text().split()[2]=='Z':break
    except FileNotFoundError:break
    time.sleep(15)
checks=Path('research/256_period_eight_tuning/verification/obstruction_checks.json')
assert checks.exists() and json.loads(checks.read_text())['all_checks_pass']
for index in range(1,11):
    for name in ['period_eight_certificate','period_eight_replay']:
        start=time.monotonic()
        with Path(f'scratch/{name}_root{index}.log').open('a') as f:
            p=subprocess.Popen([sys.executable,'-B',f'code/{name}.py','--root',str(index)],stdout=f,stderr=subprocess.STDOUT)
            print(json.dumps(dict(started=datetime.now(timezone.utc).isoformat(timespec='seconds'),root=index,name=name,pid=p.pid)),flush=True)
            rc=p.wait()
        print(json.dumps(dict(finished=datetime.now(timezone.utc).isoformat(timespec='seconds'),root=index,name=name,returncode=rc,actual_elapsed_s=time.monotonic()-start)),flush=True)
        if rc:raise SystemExit(rc)
