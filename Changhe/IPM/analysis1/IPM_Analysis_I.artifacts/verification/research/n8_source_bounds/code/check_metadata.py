from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];E=D/'evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
fine=json.loads((E/'cert_n8_fine0165.json').read_text());full=json.loads((E/'cert_n8_full.json').read_text())
assert fine['done'] and full['done']
pmin=F(fine['x_star_bracket'][0]);rmax=F(fine['r_cover'][1]);rows=[]
for d in ['0.05','0.1','0.2']:
 radius=pmin+2*F(d);assert d in fine['deltas'] and radius>rmax
 rows.append({'delta':d,'missing_point_radius_lower':str(radius),'radial_cover_upper':str(rmax),'positive_gap':str(radius-rmax)})
assert F(fine['deltas']['0.0165']['C_V'])<F('13.34')
assert F(full['deltas']['0.05']['C_V'])<F('18.634')
assert F(33,2000)*F(667,50)==F(22011,100000)
assert F(1687,500)-F(22011,100000)==F(315389,100000)
assert F(100000,315389)<F(159,500)
assert F(1,20)*F(9317,500)==F(9317,10000)
assert F(1687,500)-F(9317,10000)==F(24423,10000)
assert F(10000,24423)<F(41,100)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_METADATA_OBSTRUCTION_AND_CONDITIONAL_ARITHMETIC','missing_disc_coverage':rows,'counts':{'missing_disc_witnesses':3,'reported_scalar_upper_comparisons':2,'conditional_exact_identities_and_inequalities':6},'scope':'No numerical coefficient supremum accepted.','files':{str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',Path(__file__),E/'proof_first.json',E/'cert_n8.py',E/'cert_n8_full.json',E/'cert_n8_fine0165.json']}}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k!='files'}))
