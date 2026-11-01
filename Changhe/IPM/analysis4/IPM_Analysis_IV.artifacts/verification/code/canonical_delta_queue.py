from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,sys,json
wait_pid=131133
while True:
 try:state=Path(f'/proc/{wait_pid}/stat').read_text().split()[2]
 except FileNotFoundError:break
 if state=='Z':break
 time.sleep(2)
def run(name,args,timeout=570):
 print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),step=name)),flush=True)
 with open('logs/canonical_delta_'+name+'.log','w') as out:r=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=timeout)
 print(json.dumps(dict(step=name,returncode=r.returncode)),flush=True)
 if r.returncode:raise SystemExit(r.returncode)
run('freeze',['code/freeze_checkpoint_delta.py','../a4-num/ckpt/log_sin1_c3_p512.pkl','research/82_weighted_loss_criterion/update_N329_20261031T093225Z/verification/input_checkpoint.pkl.gz','--result-file','logs/canonical_delta_input.json'])
r=json.loads(Path('logs/canonical_delta_input.json').read_text());cp=r['input_path'];N=r['maximum_order']
run('precision',['code/log_precision_snapshot.py','log_sin1_c3_p512','--checkpoint',cp,'--select','330','--selected-gzip'])
run('diagnostics330',['code/canonical330_diagnostics.py',cp])
run('plain',['code/canonical_post_audit.py'])
run('weighted',['code/weighted_loss_audit.py','--checkpoint',cp,'--output',r['root']])
run('poisson',['code/poisson_prefix_audit.py','--checkpoint',cp,'--max-order',str(N)])
