"""Run reported late checkpoints sequentially after the floating audit ends."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,time,subprocess,sys,shutil,fcntl
STOP=datetime.fromisoformat('2026-11-01T00:50:00+00:00')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def live(pid):
    try:return Path(f'/proc/{pid}/stat').read_text().split()[2]!='Z'
    except FileNotFoundError:return False
for n in [410,420,430,440]:
    table=Path(f'../a4-num/notes/table_511b_{n-9}_{n}.md')
    while not table.exists():
        if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
        time.sleep(30)
    # Let an in-flight atomic checkpoint write finish before the first read.
    while time.time()-table.stat().st_mtime<120:
        time.sleep(min(30,120-(time.time()-table.stat().st_mtime)))
    for script in ['later_conditional_audit.py','later_shifted_drift_audit.py','later_radius_metadata_audit.py']:
        if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
        assert shutil.disk_usage('.').free>20_000_000_000
        receipt=Path('research/266_later_conditional_continuations')/f'N{n}'/'verification'/{'later_conditional_audit.py':'checks.json','later_shifted_drift_audit.py':'drift_fit_checks.json','later_radius_metadata_audit.py':'radius_metadata_checks.json'}[script]
        if receipt.exists() and json.loads(receipt.read_text()).get('all_checks_pass'):continue
        out=Path('scratch')/f'{Path(script).stem}_{n}.log'
        start=time.monotonic()
        with Path('scratch/core18.lock').open('a') as lock, out.open('a') as f:
            fcntl.flock(lock,fcntl.LOCK_EX)
            if datetime.now(timezone.utc)>=STOP:raise SystemExit(0)
            p=subprocess.Popen(['taskset','-c','18','nice','-n','19',sys.executable,'code/'+script,'--N',str(n)],stdout=f,stderr=subprocess.STDOUT,env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1'))
            print(json.dumps(dict(at=stamp(),N=n,script=script,pid=p.pid)),flush=True)
            code=p.wait()
        print(json.dumps(dict(at=stamp(),N=n,script=script,exit_code=code,actual_elapsed_s=time.monotonic()-start)),flush=True)
        if code:raise SystemExit(code)
