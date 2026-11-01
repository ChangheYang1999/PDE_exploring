"""Continue independent finite audits sequentially on CPU17."""
from pathlib import Path
import subprocess,sys,time,json
pid=3335842
while Path(f'/proc/{pid}/stat').exists():
 text=Path(f'/proc/{pid}/stat').read_text()
 if text.split(') ',1)[1].startswith('Z'):break
 time.sleep(5)
root='research/102_edge_recurrence_reference/verification/arb_edge1_20261031T084803Z'
assert Path(root,'checks.json').exists() and Path(root,'MANIFEST.json').exists()
for tag,args in [('stream_mode_share_audit',['code/stream_mode_share_audit.py']),('edge1_nonlinear',['code/edge_nonlinear_audit.py',root])]:
 with open('logs/'+tag+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=1200)
 print(json.dumps(dict(step=tag,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
