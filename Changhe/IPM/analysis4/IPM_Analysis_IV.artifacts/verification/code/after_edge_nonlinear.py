"""CPU17 one independent prime batch after the edge nonlinear audit succeeds."""
from pathlib import Path
import os,subprocess,sys,time,json
while True:
 try:os.kill(3385134,0)
 except ProcessLookupError:break
 time.sleep(5)
assert '"step": "edge1_nonlinear", "returncode": 0' in Path('logs/after_edge1_audit.log').read_text()
complete=set()
for path in Path('research/80_compatibility_size_criterion/verification').glob('cartesian_arb_scan_*/checks.json'):
 for row in json.loads(path.read_text())['rows']:complete.add((row['p'],row['a']))
pairs=[(r['p'],r['a']) for r in map(json.loads,Path('../a4-num/notes/kappa_scan_arb.jsonl').read_text().splitlines())]
remaining=[pair for pair in pairs if pair not in complete]
args=['code/cartesian_arb_prime_scan.py','--pairs',','.join(str(p)+':'+str(a) for p,a in remaining),'--seconds','500']
with open('logs/prime_batch5.jsonl','w') as out:
 result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=580)
print('prime_batch5',result.returncode,flush=True)
raise SystemExit(result.returncode)
