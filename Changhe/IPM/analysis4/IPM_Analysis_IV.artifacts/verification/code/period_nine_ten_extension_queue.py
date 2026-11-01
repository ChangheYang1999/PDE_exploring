"""Audit new completed floating outputs; ledger admission remains a separate step."""
from pathlib import Path
from datetime import datetime, timezone
import fcntl, json, os, subprocess, sys, time
STOP = datetime.fromisoformat('2026-11-01T00:45:00+00:00')
BASE = Path('research/303_period_nine_ten_floating_extensions/verification')
ENV = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')
seen = set()
while datetime.now(timezone.utc) < STOP:
    ready = set()
    for Q, N, count in [(10, 600, 14), (9, 612, 10)]:
        for root in range(1, count+1):
            src = Path('../a4-lead/code/tuned') / f'hhf_Q{Q}h1_root{root}_N{N}_f64.out'
            if src.exists() and '# done,' in src.read_text():
                ready.add((Q, root))
    if ready != seen:
        with Path('scratch/core17.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            for script in ['period_nine_ten_extension_audit.py', 'verify_floating_maxima.py']:
                started = time.monotonic()
                result = subprocess.run([sys.executable, 'code/'+script], env=ENV, timeout=120)
                print(json.dumps(dict(at=stamp(), script=script, exit_code=result.returncode,
                                      actual_elapsed_s=time.monotonic()-started)), flush=True)
                if result.returncode:
                    raise SystemExit(result.returncode)
        seen = ready
        (BASE/'queue_status.json').write_text(json.dumps(dict(at=stamp(), completed=len(ready),
            pid=os.getpid(), status='complete' if len(ready)==24 else 'waiting',
            scope='Completed finite arithmetic only; new cases still require explicit ledger admission.'), indent=2)+'\n')
    if len(ready)==24:
        break
    time.sleep(45)
print(json.dumps(dict(at=stamp(), status='queue ended', completed=len(seen))), flush=True)
