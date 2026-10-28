"""Audit numerical-summary scope and rounding, without endorsing its enclosures."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,math
src=Path('numerics/data/certSups_131.jsonl')
rows=[json.loads(s) for s in src.read_text().splitlines() if s.strip()]
assert len(rows)==40081 and len({(r['i'],r['k']) for r in rows})==40081
keys=['Frob_D1_rho','Frob_D1_U','Frob_D2_rho','wFrob_D2_rho','Frob_D2_U','wFrob_D2_U']
summary={}
for k in keys:
 good=[r for r in rows if isinstance(r.get(k), (float,int)) and math.isfinite(r[k])]
 bad=[r for r in rows if r not in good] if not good else [r for r in rows if not isinstance(r.get(k),(float,int)) or not math.isfinite(r[k])]
 best=max(good,key=lambda r:r[k])
 summary[k]={'finite_rows':len(good),'nonfinite_or_missing_rows':len(bad),'largest_recorded_upper_bound':best[k],'largest_bound_cell':[best['i'],best['k']],'nonfinite_r_range':None if not bad else [min(r['r_lo'] for r in bad),max(r['r_hi'] for r in bad)]}
assert Q(summary['Frob_D1_rho']['largest_recorded_upper_bound'])>Q('10.3003')
assert Q(summary['Frob_D1_U']['largest_recorded_upper_bound'])>Q('1.1459')
origin=next(r for r in rows if (r['i'],r['k'])==(-1,-1))
code=Path('numerics/code/cert_sups.py')
text=code.read_text()
assert '(Fr(0), Fr(0), Fr(r_hi), Fr(r_hi))' in text
assert 'w_hi = (1 + 4*arb(r_hi)**2)**arb(0.4)' in text
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SUMMARY_AUDIT','scope':'Aggregation and code-path audit only. It does not independently certify the numerical enclosures.','input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),'rows':len(rows),'summary':summary,'origin_r_hi':origin['r_hi'],'issues':['The claims 10.3003 and 1.1459 are below recorded enclosure upper bounds. Their certification does not follow from this artifact.','A uniform upper bound greater than the origin value does not prove the exact supremum equals the origin value.','For the origin square [-r_hi,r_hi]^2 the radial weight maximum is (1+8r_hi^2)^(2/5), not (1+4r_hi^2)^(2/5). The latter remains valid on the inscribed disk only.','Nonfinite rows do not certify their respective fields; a full-plane statement also needs the exterior certificate.']}
dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
