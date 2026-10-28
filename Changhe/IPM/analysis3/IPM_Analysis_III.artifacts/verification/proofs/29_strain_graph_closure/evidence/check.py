from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
p=Path(__file__).resolve().parents[1]
t=s.symbols('t',real=True)
a=s.integrate(s.cos(t)**2*s.sin(t)*s.sin(3*t),(t,0,2*s.pi))/s.pi
assert a==s.Rational(1,4)
e,k=s.symbols('eta k',real=True)
assert s.simplify(1+(e+2)/2-(2+e/2))==0
far=-s.Rational(5,4)+2*(k-1)-6+1
assert far==2*k-s.Rational(33,4)
assert s.solve(far+1,k)==[s.Rational(29,8)]
assert s.Rational(1,4)>-4
res={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','scope':'angular moment and exact scaling/integrability algebra; analytic packet proof checked separately','angular_moment':str(a),'far_radial_exponent':str(far),'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
