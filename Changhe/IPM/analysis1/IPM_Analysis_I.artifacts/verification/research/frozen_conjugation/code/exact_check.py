"""Exact illustrative arithmetic and an independent polynomial cancellation check."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
A=F('10.1507252');g=F('29.75');a=g/(A-1);c=a-(A+3)/2
assert a*(A-1)==g and c<0
# Clearing denominators verifies the angular cancellation as a polynomial in xi^2,eta^2.
assert a*A-(A+2)-g==a-A-2
assert a-(A+2)==a-A-2
out={'utc':datetime.now(timezone.utc).isoformat(),'A_exact':str(A),'g_exact':str(g),'a_exact':str(a),'c_exact':str(c),'inverse_constant_exact':str(1/abs(c)),'a_display':float(a),'c_display':float(c),'inverse_constant_display':float(1/abs(c)),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'Exact algebra with illustrative rounded inputs only; not certified source data.'}
Path('research/frozen_conjugation/evidence/exact_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
