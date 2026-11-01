"""Check every displayed strict finite-residual decimal bound."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=768
p=Path('research/16_certified_residuals/verification/reference_sin_residuals.json')
d=json.loads(p.read_text())
bounds=[('2.3629e-5','2.4340e-5'),('1.0920e-6','1.1249e-6'),('5.0055e-8','5.1558e-8'),('2.2818e-9','2.3503e-9'),('6.7799e-9','7.1880e-9'),('1.4081e-11','1.4931e-11'),('2.9011e-14','3.0762e-14'),('5.9416e-17','6.3003e-17')]
rows=[]
for r,(lo,hi) in zip(d['rows'],bounds,strict=True):
 b=r['bounds']['residual']
 assert arb(lo)<arb(b['sup_lower']) and arb(hi)>arb(b['sup_upper'])
 rows.append({'N':r['N'],'R':r['R'],'strict_lower':lo,'strict_upper':hi,'verified':True})
out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'source_sha256':sha256(p.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
Path('research/16_certified_residuals/verification/displayed_table.json').write_text(json.dumps(out,indent=2)+'\n')
print('All eight displayed strict interval bounds pass.')
