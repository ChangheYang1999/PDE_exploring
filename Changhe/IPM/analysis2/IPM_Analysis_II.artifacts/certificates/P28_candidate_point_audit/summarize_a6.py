from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
p=HERE/'nb_A6dpen_exact.json';d=json.loads(p.read_text())
assert d['precision_bits']==768
assert d['code_sha256']==sha256((HERE/'point_contract.py').read_bytes()).hexdigest()
for rel,digest in d['dependencies'].items():assert sha256((BASE/rel).read_bytes()).hexdigest()==digest,rel
source=Path('numerics/data/nb_A6dpen_exact.json')
assert sha256(source.read_bytes()).hexdigest()==d['source_sha256']
P={tuple(row['point']):row for row in d['points']}
for row in d['points']:
 assert row['all_derivatives_and_fields_overlap']
 for key,value in row['cartesian'].items():
  a,b=arb(value),arb(row['polar'][key]);assert a.is_finite() and b.is_finite() and a.overlaps(b)
 assert arb(row['cartesian']['M1_min'])>arb(1)/2
 assert arb(row['cartesian']['M2_min'])>arb(1)/2
checks=[(('0','1/5'),'r2_D4rho','551.5248'),(('0','4/5'),'r2_D4rho','631.6766'),(('6','8'),'N_point_bound','0.00732')]
for point,key,bound in checks:assert arb(P[point]['cartesian'][key])>arb(bound)
assert arb(P['6','8']['cartesian']['N_point_bound'])*2**35>2**27
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED point bounds and exact admissibility; W3 fourth-derivative requirement and sufficient residual smallness REFUTED','candidate':'nb_A6dpen_exact','source_sha256':d['source_sha256'],'canonical_sha256':d['canonical_sha256'],'record_sha256':sha256(p.read_bytes()).hexdigest(),'strict_lower_bounds':[{'point':list(point),'quantity':key,'lower':bound} for point,key,bound in checks],'selected_point_W2':True,'global_positivity':'OPEN','code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'summarize_a6.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
