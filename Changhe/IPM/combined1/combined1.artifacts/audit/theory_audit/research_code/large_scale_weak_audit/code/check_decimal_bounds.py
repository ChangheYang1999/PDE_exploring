from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime, timezone
import json
from flint import arb,ctx
ctx.prec=512
base=Path(__file__).resolve().parents[1]
source=base/'verification/results.json'
d=json.loads(source.read_text())
checks=[]
for a,k,safe,unsafe in [('13/10',2**28,'0.000436835013298882','0.000436835013298883'),('7/5',2**26,'0.000163823854295506','0.000163823854295507')]:
 row=next(v for v in d['rows'] if v['a']==a and v['k']==k)
 val=arb(row['weighted_L2_radius_lower'])
 def dec(s):
  q=Fraction(s);return arb(q.numerator)/q.denominator
 assert val>dec(safe)
 assert val<dec(unsafe)
 checks.append({'a':a,'k':k,'safe_strict_lower':safe,'unsafe_upward_decimal':unsafe,'value':val.str(90)})
sqrt10pi=(10*arb.pi()).sqrt()
assert sqrt10pi>dec('5.604991')
assert sqrt10pi<dec('5.604992')
result={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha256(source.read_bytes()).hexdigest(),'checks':checks,'sqrt10pi':sqrt10pi.str(90),'safe_sqrt10pi_upper':'5.604992'}
p=base/'verification/decimal_bounds.json'
assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
