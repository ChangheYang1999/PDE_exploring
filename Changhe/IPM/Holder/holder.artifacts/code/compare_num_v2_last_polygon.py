"""Independent same-shape check of the last corrected polygon certificate."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx
import json,hashlib
ctx.prec=256
root=Path(__file__).resolve().parents[1]
p=root/'numerics_data/cert2/a910_a15_v2.json'
q=root/'data/num_v2_layercake_a20.json'
x=json.loads(p.read_text());y=json.loads(q.read_text());r=y['rows'][0]
assert Fraction(x['alpha'])==Fraction(r['alpha'])==Fraction(9,10)
assert Fraction(x['a'])==Fraction(y['a'])==Fraction(1,5)
lo=arb(r['safe_decimal_lower_10_places']);hi=arb(r['safe_decimal_upper_10_places'])
assert lo>arb(x['I_lower']) and hi<arb(x['I_upper'])
assert lo>arb('4.83247')
dest=root/'05_team_audit/numerical_certificate_v2/verification/a910_a15_v2.json'
dest.write_bytes(p.read_bytes())
paths=[dest,q,Path(__file__),root/'05_team_audit/numerical_certificate_v2/PROOF.md']
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha='9/10',shape='1/5',numerics_lower=x['I_lower'],numerics_upper=x['I_upper'],independent_lower=r['safe_decimal_lower_10_places'],independent_upper=r['safe_decimal_upper_10_places'],independent_interval_contained=True,reported_rounded_lower_independently_proved=True,source_hashes={str(s.relative_to(root)):hashlib.sha256(s.read_bytes()).hexdigest() for s in paths},note='The numerical report rounded its own lower endpoint upward by about 4.94e-7. Its displayed 4.83247 is nevertheless proved by the independent lower endpoint 4.8453038319. The correct source is a910_a15_v2.json; the earlier file has a useless far-field enclosure.')
(root/'data/num_v2_last_polygon_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
