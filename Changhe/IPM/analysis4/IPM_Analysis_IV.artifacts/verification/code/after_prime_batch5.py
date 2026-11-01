"""Run two small independent checks on CPU17 after the current prime batch."""
from pathlib import Path
import os,time,sys,subprocess,json
while True:
 try:os.kill(3417633,0)
 except ProcessLookupError:break
 time.sleep(5)
assert 'prime_batch5 0' in Path('logs/after_edge_nonlinear.log').read_text()
for name in ['density_band_offset_audit','edge_top_comparison_check']:
 with open('logs/'+name+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u','code/'+name+'.py'],stdout=out,stderr=subprocess.STDOUT,timeout=300)
 print(json.dumps(dict(step=name,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
