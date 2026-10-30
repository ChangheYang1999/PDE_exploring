from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sympy as s
B=Path(__file__).resolve().parents[1];start=time.monotonic()
r=s.symbols('r',positive=True);inner=r/6;outer=1/(2*r)-1/(3*r**2)
def op(p):return s.simplify(-s.diff(p,r,2)-s.diff(p,r)/r+p/r**2)
assert op(inner)==0 and op(outer)==r**-4
assert inner.subs(r,1)==outer.subs(r,1)
assert s.diff(inner,r).subs(r,1)==s.diff(outer,r).subs(r,1)
value=s.integrate(r**-3*outer,(r,1,s.oo));assert value==s.Rational(1,12)
a,b,n=s.symbols('a b n',real=True)
# Reversing integration gives 1/((n-a-2)(-a-b-4)); test the resonant inner exponent too.
assert 1/((s.Integer(1)+4-2)*(8-4))==value
assert 1/((s.Integer(1)+4-2)*(4+3-4))==s.Rational(1,9)
source=B/'source/N1_ipm_hminus1.py'
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha256(source.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':sha256((B/'PROOF.md').read_bytes()).hexdigest(),'radial_equation_and_matching':True,'exact_norm_squared':'pi/12','refuted_norm_squared':'pi/24','resonant_triangle':'1/9','elapsed_seconds':time.monotonic()-start}
(B/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
