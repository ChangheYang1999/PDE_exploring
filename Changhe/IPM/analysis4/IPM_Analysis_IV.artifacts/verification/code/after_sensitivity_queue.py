"""Sequential follow-up audits on core18; no competing compute jobs."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/2180164/cmdline')
while p.exists() and b'after_edge_queue.py' in p.read_bytes():time.sleep(20)
def run(name,args,label=None):
    label=label or name
    print(json.dumps(dict(job=label,event='start',utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
    with Path('scratch',label+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+name+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(job=label,event='exit',returncode=r.returncode,utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
    return r.returncode
for name in ['local_fit_ambiguity','reset380_conditional_audit','shifted_drift380_audit']:run(name,[])
for index in [4,1,2,3]:
    receipt=Path(f'research/209_three_fifths_high_order/verification/root{index}_checks.json')
    while not receipt.exists():time.sleep(20)
    if run('high_prefix_three_fifths_radii',['--roots',str(index)],f'high_prefix_radii_root{index}')==0:
        run('high_prefix_three_fifths_replay',['--roots',str(index)],f'high_prefix_replay_root{index}')
