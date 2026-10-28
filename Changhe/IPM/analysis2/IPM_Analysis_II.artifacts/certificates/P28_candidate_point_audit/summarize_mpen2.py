"""Independent provenance, overlap and strict endpoint audit of Mpen2."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
p=HERE/'nb_Mpen2_exact.json';d=json.loads(p.read_text())
assert d['precision_bits']==768
assert d['code_sha256']==sha256((HERE/'point_contract.py').read_bytes()).hexdigest()
for rel,digest in d['dependencies'].items():assert sha256((BASE/rel).read_bytes()).hexdigest()==digest,rel
source=Path('numerics/data/nb_Mpen2_exact.json')
assert sha256(source.read_bytes()).hexdigest()==d['source_sha256']
P={tuple(row['point']):row for row in d['points']}
limits={'Du':'2.8','Drho':'16','r1_D2u':'3','r1_D3u':'16','D2rho':'3','r1_D2rho':'8','r2_D3rho':'32','r2_D4rho':'512'}
for row in d['points']:
 assert row['all_derivatives_and_fields_overlap']
 for key,value in row['cartesian'].items():
  a,b=arb(value),arb(row['polar'][key]);assert a.is_finite() and b.is_finite() and a.overlaps(b)
 for key in ['M1_min','M2_min']:assert arb(row['cartesian'][key])>arb(1)/2
 for key,limit in limits.items():assert arb(row['cartesian'][key])<arb(limit)
 assert arb(row['cartesian']['M_min'])>arb(19)/5
checks=[(('6','8'),'N_point_bound','0.0048729'),(('0','1'),'r2_D4rho','449.0303')]
for point,key,bound in checks:assert arb(P[point]['cartesian'][key])>arb(bound)
assert arb(P['6','8']['cartesian']['N_point_bound'])*2**35>2**27
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED point bounds and exact admissibility; sufficient residual smallness REFUTED; global W1,W2,W3 OPEN','candidate':'nb_Mpen2_exact','source_sha256':d['source_sha256'],'canonical_sha256':d['canonical_sha256'],'record_sha256':sha256(p.read_bytes()).hexdigest(),'strict_lower_bounds':[{'point':list(point),'quantity':key,'lower':bound} for point,key,bound in checks],'selected_point_W1_W2_W3':True,'global_coefficient_contract':'OPEN','code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'summarize_mpen2.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
