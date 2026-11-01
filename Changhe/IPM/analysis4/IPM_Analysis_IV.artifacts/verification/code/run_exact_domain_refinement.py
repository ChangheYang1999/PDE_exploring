"""Try an exact domain specialization; preserve and resume on any failure."""
import os,signal,subprocess,sys,time,json
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
oldpid=3269327;out=Path('research/164_four_ninths_response_minima/verification')
record={'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'old_pid':oldpid}
start=time.monotonic();os.kill(oldpid,signal.SIGSTOP)
try:
    with (out/'fast_domain_producer.log').open('w') as log:
        run=subprocess.run([sys.executable,'code/guarded_run.py','code/four_ninths_exact_polynomial_fast.py',str(out/'fast_domain_FAILURE.json')],stdout=log,stderr=subprocess.STDOUT,timeout=500)
    record['returncode']=run.returncode
    if run.returncode==0:
        os.kill(oldpid,signal.SIGTERM);os.kill(oldpid,signal.SIGCONT)
        for _ in range(50):
            if not Path(f'/proc/{oldpid}').exists():break
            time.sleep(.1)
        assert not Path(f'/proc/{oldpid}').exists(),'Previous symbolic process did not exit'
        (out/'producer_before_domain_refinement.log').write_bytes((out/'producer.log').read_bytes())
        with (out/'producer.log').open('w') as log:
            process=subprocess.Popen([sys.executable,'code/four_ninths_response_minima.py'],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        record['new_pid']=process.pid
    else:os.kill(oldpid,signal.SIGCONT)
except Exception as exc:
    record['error']=type(exc).__name__+': '+str(exc)
    if Path(f'/proc/{oldpid}').exists():os.kill(oldpid,signal.SIGCONT)
finally:
    record['finished_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds');record['actual_elapsed_s']=time.monotonic()-start
    (out/'domain_refinement_scheduling.json').write_text(json.dumps(record,indent=2)+'\n')
