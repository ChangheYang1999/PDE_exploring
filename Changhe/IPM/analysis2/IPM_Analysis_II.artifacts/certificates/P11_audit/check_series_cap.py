from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
from flint import arb, arb_series, ctx
import json
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'initial_cap':ctx.cap}
ctx.prec=192
for cap in (10,61):
 ctx.cap=cap
 x=arb_series([1,1],61).log()
 true=-arb(1)/20
 out[str(cap)]={'result_precision':x.prec,'coefficient20':x[20].str(30), 'contains_exact_minus_one_twentieth':x[20].contains(true)}
assert not out['10']['contains_exact_minus_one_twentieth']
assert out['61']['contains_exact_minus_one_twentieth']
p=Path(__file__).resolve().parents[3]/'s1-num'/'research'/'code'/'rtm.py'
if p.is_file(): out['inspected_rtm_sha256']=sha256(p.read_bytes()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
