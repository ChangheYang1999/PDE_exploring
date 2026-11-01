"""Bounded sequential prime batches after the two short CPU17 checks."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,sys,subprocess,json
while True:
 try:os.kill(3498863,0)
 except ProcessLookupError:break
 time.sleep(5)
assert '"step": "edge_top_comparison_check", "returncode": 0' in Path('logs/after_prime_batch5.log').read_text()
for batch in range(6,18):
 complete=set()
 for path in Path('research/80_compatibility_size_criterion/verification').glob('cartesian_arb_scan_*/checks.json'):
  for row in json.loads(path.read_text())['rows']:complete.add((row['p'],row['a']))
 pairs=[(r['p'],r['a']) for r in map(json.loads,Path('../a4-num/notes/kappa_scan_arb.jsonl').read_text().splitlines())]
 remaining=[v for v in pairs if v not in complete]
 print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),batch=batch,complete=len(set(pairs)&complete),remaining=len(remaining))),flush=True)
 if not remaining:break
 args=['code/cartesian_arb_prime_scan.py','--pairs',','.join(str(p)+':'+str(a) for p,a in remaining),'--seconds','480']
 with open('logs/prime_batch'+str(batch)+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=590)
 print(json.dumps(dict(batch=batch,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
