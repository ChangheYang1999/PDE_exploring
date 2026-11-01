"""Sequential storage maintenance and independent modular checks on core17."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,time,json
p=Path('/proc/2720852/cmdline')
while p.exists() and b'after_top_mode_queue.py' in p.read_bytes():time.sleep(20)
jobs=[('local_fit_ambiguity',[],'local_fit_ambiguity_v3'),('compress_closed_selected_evidence',[],'compress_closed_selected_evidence'),('modular_cartesian_scan',['--profile','cand007','--pairs','9:2,13:3,17:4'],'modular_candidate_smoke'),('modular_cartesian_scan',['--profile','sin1','--pairs','9:2,13:3,17:4'],'modular_sin1_smoke'),('modular_cartesian_scan',['--profile','cand007','--Qmax','120'],'modular_candidate_grid'),('modular_cartesian_scan',['--profile','sin1','--Qmax','120'],'modular_sin1_grid')]
for script,args,label in jobs:
    print(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),job=label,event='start')),flush=True)
    with Path('scratch',label+'.log').open('wb') as log:r=subprocess.run([sys.executable,'-B','code/'+script+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),job=label,event='exit',code=r.returncode)),flush=True)
    if r.returncode:break
