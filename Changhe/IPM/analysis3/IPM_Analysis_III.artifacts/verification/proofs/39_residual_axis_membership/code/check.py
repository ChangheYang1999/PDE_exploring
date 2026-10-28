from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
x,y,ell,c,J=s.symbols('x y ell c J')
a20,a02,b30,b12,d21,d03=s.symbols('a20 a02 b30 b12 d21 d03')
rho=x*x*y*(1+J+a20*x*x+a02*y*y)
v1=(ell-c)*x+b30*x**3+b12*x*y*y
v2=(ell+c)*y+d21*x*x*y+d03*y**3
F=s.expand(v1*s.diff(rho,x)+v2*s.diff(rho,y)-rho)
B=s.cancel(F/(x*x*y))
lead=s.expand(B.subs({x:0,y:0}))
assert s.expand(lead-(1+J)*(3*ell-c-1))==0
assert s.cancel((B-B.subs(x,0))/x**2).is_polynomial(x,y)
a=s.Rational(17,4); eta=s.Rational(5,4)
assert 8-2*a == -s.Rational(1,2)
assert 12-2*a == s.Rational(7,2)
assert 8-eta == s.Rational(27,4)
assert 8-2*a > -1
P=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS',
   'cubic_coefficient':str(s.factor(lead)),
   'remainder_angular_exponent':str(8-2*a),
   'near_radial_exponent':str(12-2*a),
   'far_radial_exponent':'4*k-5/4',
   'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps(o,indent=2))
