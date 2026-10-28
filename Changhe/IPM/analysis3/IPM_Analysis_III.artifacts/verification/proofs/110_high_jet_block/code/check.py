from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[1]
z=s.symbols('z');p=-1/(z+2);q=1/(z+6);v=1/(z+8)
V=p/4-q/4+v/2
assert s.simplify((z+2)*V-(q-3*v))==0
assert s.degree(s.fraction(s.factor(V))[0],z)==1
assert s.degree(s.fraction(s.factor(V))[1],z)==3
k=F(1615536043799051,9007199254740992)
assert 2-F(27,8)==-F(11,8)
assert k-3-F(11,8)==k-F(35,8)
assert 2*(k-F(35,8))+F(27,4)==2*k-2<0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','trace_multiplier':str(s.factor(V)),'derivative_multiplier':str(s.factor(q-3*v)),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
