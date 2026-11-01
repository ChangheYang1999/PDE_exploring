"""Bounded sequential certificate refinements on the lane's second core."""
import os,signal,subprocess,sys,time,json
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
out=Path('research/172_certified_prefix_majorant/verification')
record={'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'paused_pid':3269327,'jobs':[]}
while Path('/proc/3425757').exists():time.sleep(2)
start=time.monotonic();os.kill(3269327,signal.SIGSTOP)
record['paused_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds')
jobs=[('certified_prefix_majorant.py','172_certified_prefix_majorant','generic_producer.log',['--family','generic']),('certified_prefix_majorant.py','172_certified_prefix_majorant','two_mode5_producer.log',['--family','two_mode5']),('certified_initial_majorants.py','168_certified_initial_majorants','root4_producer.log',['--family','candidate','--roots','4','--improved-kappa','--improved-poisson']),('resonance_block_majorant.py','171_resonance_block_majorant','root4_producer.log',['--family','candidate','--roots','4'])]
try:
    for script,topic,logname,args in jobs:
        begin=time.monotonic();folder=Path('research')/topic/'verification'
        with (folder/logname).open('w') as log:
            result=subprocess.run([sys.executable,'code/guarded_run.py','code/'+script,str(folder/'FAILURE.json')]+args,stdout=log,stderr=subprocess.STDOUT,timeout=500)
        record['jobs'].append({'script':script,'arguments':args,'returncode':result.returncode,'actual_elapsed_s':time.monotonic()-begin})
        (out/'progress.json').write_text(json.dumps(record,indent=2)+'\n')
        if result.returncode:break
except Exception as exc:record['error']=type(exc).__name__+': '+str(exc)
finally:
    os.kill(3269327,signal.SIGCONT)
    record['resumed_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds');record['actual_paused_s']=time.monotonic()-start
    (out/'scheduling.json').write_text(json.dumps(record,indent=2)+'\n')
