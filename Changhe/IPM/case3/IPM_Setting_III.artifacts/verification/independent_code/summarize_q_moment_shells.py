import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
mp.mp.dps=100
records=[]
for N in [64,96,128,160,192]:
 p=Path('evidence/q_canonical_moment_shells')/f'R1C_CL3P0_N{N}'/'diagnostic.json'
 if p.exists():
  o=json.loads(p.read_text());records.append(dict(N=N,record=str(p),record_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_sha256=o['source_sha256'],radii_physical=o['radii_physical'],evaluated=o['evaluated']))
out=dict(utc=datetime.now(timezone.utc).isoformat(),records=records,scope='Signed canonical source moments on common physical radial shells; finite formula diagnostics, not convergence or profile claims.')
dest=Path('evidence/q_canonical_moment_shells');dest.mkdir(parents=True,exist_ok=True)
(dest/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Signed canonical moment comparison','',out['utc'],'',out['scope'],'','| N | I2 total | I4 total | I6 total |','|---:|---:|---:|---:|']
for r in records:lines.append('| '+str(r['N'])+' | '+' | '.join(mp.nstr(mp.mpf(e['total']),14)for e in r['evaluated'])+' |')
for j in [1,2]:
 lines+=['',f'Frequency {2*(j+1)} signed source moment contributions. The final column includes the infinite exterior.','', '| N | 0 to .001 | .001 to .01 | .01 to .1 | .1 to 1 | 1 to 100 | 100 to infinity |','|---:|---:|---:|---:|---:|---:|---:|']
 for r in records:
  ss=[mp.mpf(x)for x in r['evaluated'][j]['shells']]
  pieces=[mp.fsum(ss[a:b])for a,b in [(0,4),(4,6),(6,8),(8,10),(10,13),(13,14)]]
  lines.append('| '+str(r['N'])+' | '+' | '.join(mp.nstr(x,14)for x in pieces)+' |')
lines+=['','All partitions use common physical radii. The individual records retain every shell, infinite tail, exact polynomial, source hash and precision comparison. Strong cancellation between shells must be read together with their signs.']
(dest/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'utc':out['utc'],'states':len(records)}))
