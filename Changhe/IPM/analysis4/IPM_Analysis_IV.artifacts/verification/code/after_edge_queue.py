"""Serialize the next audits after the existing core18 job exits."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys,time
P=1901816
cmdfile=Path('/proc')/str(P)/'cmdline'
while cmdfile.exists() and b'one_step_edge_audit.py' in cmdfile.read_bytes():time.sleep(20)
python=sys.executable
for name,args in [('all_order_pole_response',[]),('boundary_sensitivity_audit',['--through','340']),('boundary_input_audit',[])]:
    start=datetime.now(timezone.utc).isoformat(timespec='seconds')
    print(json.dumps(dict(stage=name,event='start',utc=start)),flush=True)
    with Path('scratch',name+'.log').open('wb') as out:
        p=subprocess.run([python,'-B','code/'+name+'.py']+args,stdout=out,stderr=subprocess.STDOUT)
    print(json.dumps(dict(stage=name,event='exit',returncode=p.returncode,utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
