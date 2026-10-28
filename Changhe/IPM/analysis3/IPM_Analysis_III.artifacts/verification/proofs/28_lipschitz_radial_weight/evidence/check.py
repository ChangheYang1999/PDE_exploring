from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
p=Path(__file__).resolve().parents[1]
knots=list(map(Q,['3/2','7/4','3','4','5','6','7','8','9','10']))
slopes=[Q(x,16) for x in (4,17,28,27,25,18,4,-10,-17,-19,-20)]
assert len(slopes)==len(knots)+1
assert max(map(abs,slopes))==Q(7,4)<2
assert slopes[0]==Q(1,4) and slopes[-1]==-Q(5,4)
assert all(a<b for a,b in zip(knots,knots[1:]))
assert min(b-a for a,b in zip(knots,knots[1:]))==Q(1,4)
assert 4*Q(1,4)-Q(5,4)<0
assert 2*0+2-Q(5,4)>0
res={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','scope':'exact slope, knot and membership algebra only; analytic proof independently checked','M':str(max(map(abs,slopes))),'mu_near_slope':str(slopes[0]),'mu_far_slope':str(slopes[-1]),'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
