from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
p=Path(__file__).resolve().parents[1]
a=Q(17,4);eta=Q(5,4);sigma=Q(1,4)
assert 8-2*a==-2*sigma and 8-eta==Q(27,4)
assert 8-2*a>-1 and 4-2*a<-1
assert 4-2*sigma>0
# General symbols are checked algebraically: d+2(2ell-d-dprime)-1 = 4ell-1-d-2dprime.
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','origin_G_exponent':str(8-2*a),'far_G_exponent':str(8-eta),'angular_lift_error_exponent':str(8-2*a),'scope':'scalar and radial exponent arithmetic; the conditional operator proof is analytic','proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
