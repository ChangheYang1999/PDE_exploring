"""Wait for the sole weak worker, then run the next serial local audit."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,json,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_dyadic_probes'
pid=2664587
print(datetime.now(timezone.utc).isoformat(),'waiting for',pid,flush=True)
while True:
    p=Path(f'/proc/{pid}')
    if not p.exists():break
    try:
        stat=(p/'stat').read_text().split();cmd=(p/'cmdline').read_bytes()
        if stat[2]=='Z' or b'successor_weak_probes/code/check.py' not in cmd:break
    except FileNotFoundError:break
    time.sleep(5)
print(datetime.now(timezone.utc).isoformat(),'previous process finished; starting calibration and008/009',flush=True)
cmd=['python3','-B',str(BASE/'code/check.py'),
     'C1-N1-007-d2w-j7-e2bal','C1-N1-008-d2w-j7-x3bal','C1-N1-009-d2w-j7-x3balk']
run=subprocess.run(cmd,env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(ROOT/'tmp')})
with (BASE/'verification/queue01_finished.json').open('x') as f:json.dump({'utc':datetime.now(timezone.utc).isoformat(),'returncode':run.returncode},f,indent=2);f.write('\n')
print(datetime.now(timezone.utc).isoformat(),'queue finished',run.returncode,flush=True)
