from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
p=Path(__file__).resolve().parents[1]
z=s.symbols('z',real=True)
angular=s.integrate(s.cos(z)**4*s.sin(z)*s.sin(3*z),(z,0,2*s.pi))/s.pi
assert angular==s.Rational(3,16)
a=s.Rational(17,4);eta=s.Rational(5,4)
assert 8-2*a>-1 and 4-2*a<-1
assert 12-2*a>0 and 2*a-5>-1 and eta-5<-1
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','angular_strain_coefficient':str(angular),'angular_remainder_exponent':str(8-2*a),'angular_forbidden_jet_exponent':str(4-2*a),'near_squared_radial_dt_exponent':str(12-2*a),'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
