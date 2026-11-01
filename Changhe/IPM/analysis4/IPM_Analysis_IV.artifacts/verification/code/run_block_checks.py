"""Run bounded block checks after the independent finite audit relinquishes core18."""
import os,signal,subprocess,sys,time,json
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
out=Path('research/171_resonance_block_majorant/verification')
record={'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'waited_for_pid':3369564,'paused_pid':3269327,'jobs':[]}
while Path('/proc/3369564').exists():time.sleep(10)
start=time.monotonic();os.kill(3269327,signal.SIGSTOP)
record['paused_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
try:
    for family,roots in [('generic','1'),('two_mode','1,2,3,4,5'),('candidate','2,3')]:
        begin=time.monotonic()
        with (out/(family+'_producer.log')).open('w') as log:
            result=subprocess.run([sys.executable,'code/guarded_run.py','code/resonance_block_majorant.py',str(out/'FAILURE.json'),'--family',family,'--roots',roots],stdout=log,stderr=subprocess.STDOUT,timeout=500)
        record['jobs'].append({'family':family,'returncode':result.returncode,'actual_elapsed_s':time.monotonic()-begin})
        (out/'progress.json').write_text(json.dumps(record,indent=2)+'\n')
        if result.returncode:break
except Exception as exc:record['error']=type(exc).__name__+': '+str(exc)
finally:
    os.kill(3269327,signal.SIGCONT)
    record['resumed_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds');record['actual_paused_s']=time.monotonic()-start
    (out/'scheduling.json').write_text(json.dumps(record,indent=2)+'\n')
