"""Rational correction rectangle excluded by the certified p=2 probe."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parents[3]
src=ROOT/'research/weak_probe/verification/d2_1024.json'
data=json.loads(src.read_text());row=next(x for x in data['probes'] if x['p']==2)
pair=abs(arb(row['pairing']));base=arb(row['denominator_without_d']);N=arb(row['N'])
m=arb(27)/10000;d=arb(3)/100;upper=m*(base+d*N);gap=pair-upper
assert gap>0 and pair>arb(288)/10000 and base+d*N<arb(10603)/1000
assert all(arb(b['d'])<d and arb(b['m'])<m for b in row['boxes'])
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'d2','m_exact':'27/10000','gradient_cap_exact':'3/100',
     'pairing_absolute':pair.str(80),'denominator_upper_at_cap':(base+d*N).str(80),'necessary_rhs':upper.str(80),'strict_gap':gap.str(80),
     'excluded':True,'five_recorded_boxes_contained':True,'parent_sha256':sha256(src.read_bytes()).hexdigest(),
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':ctx.prec,
     'scope':'No fixed-c correction with both stated caps. The gradient cap is essential; all values remain N4-ORIGIN pending reproduction.'}
(ROOT/'research/weak_probe/verification/d2_uniform_rectangle.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
