from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import factorial
import json,hashlib
p=Path(__file__).resolve().parents[1]
a=Q(17,4);eta=Q(5,4)
assert 0<a<Q(9,2) and eta<2
assert Q(factorial(4),factorial(3))==4
assert Q(factorial(3),factorial(2))==3
assert all(eta<2*b-2 for b in (2,3,4,5))
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','output_axis_exponent':str(8-2*a),'slowest_input_radial_exponent_dr':str(eta-3),'scope':'algebra and integrability arithmetic; Hilbert-Schmidt proof is analytic','proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
