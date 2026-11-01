"""Run a bounded finite audit while suspending the other core18 job."""
import os, signal, subprocess, sys, time, json
from pathlib import Path
from datetime import datetime, timezone
sys.dont_write_bytecode=True
root=Path('research/167_four_ninths_finite_audit/verification')
pid=int(sys.argv[1]); started=time.monotonic()
record={'paused_pid':pid,'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'reason':'Independent finite audit uses core18; maintain at most two busy computations.'}
os.kill(pid,signal.SIGSTOP)
try:
    with (root/'producer.log').open('w') as log:
        result=subprocess.run([sys.executable,'code/four_ninths_finite_audit.py','--roots','5','--N','90'],stdout=log,stderr=subprocess.STDOUT,timeout=540)
        record['returncode']=result.returncode
except Exception as exc:
    record['error']=type(exc).__name__+': '+str(exc)
finally:
    os.kill(pid,signal.SIGCONT)
    record['resumed_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
    record['actual_paused_s']=time.monotonic()-started
    (root/'scheduling.json').write_text(json.dumps(record,indent=2)+'\n')
