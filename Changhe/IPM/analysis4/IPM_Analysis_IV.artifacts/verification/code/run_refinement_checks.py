"""Sequential bounded calculations on core18 while its long symbolic job is paused."""
import os,signal,subprocess,sys,time,json
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
pid=3269327;start=time.monotonic();out=Path('research/168_certified_initial_majorants/verification')
record={'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'paused_pid':pid,'jobs':[]}
jobs=[('sharp_rational_poisson.py','169_sharp_rational_poisson','producer.log',[]),('certified_initial_majorants.py','168_certified_initial_majorants','poisson_two_mode.log',['--improved-kappa','--improved-poisson']),('certified_initial_majorants.py','168_certified_initial_majorants','poisson_candidate.log',['--family','candidate','--roots','2,3','--improved-kappa','--improved-poisson']),('tuned_top_mode_bounds.py','170_tuned_top_mode_obstruction','producer.log',[]),('four_ninths_finite_audit.py','167_four_ninths_finite_audit','producer.log',['--roots','5','--N','90','--bits','3072'])]
os.kill(pid,signal.SIGSTOP)
try:
    for script,topic,logname,args in jobs:
        begin=time.monotonic();folder=Path('research')/topic/'verification'
        with (folder/logname).open('w') as log:
            result=subprocess.run([sys.executable,'code/guarded_run.py','code/'+script,str(folder/'FAILURE.json')]+args,stdout=log,stderr=subprocess.STDOUT,timeout=500)
        record['jobs'].append({'script':script,'returncode':result.returncode,'actual_elapsed_s':time.monotonic()-begin})
        (out/'refinement_progress.json').write_text(json.dumps(record,indent=2)+'\n')
except Exception as exc:record['error']=type(exc).__name__+': '+str(exc)
finally:
    os.kill(pid,signal.SIGCONT)
    record['resumed_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds');record['actual_paused_s']=time.monotonic()-start
    (out/'refinement_scheduling.json').write_text(json.dumps(record,indent=2)+'\n')
