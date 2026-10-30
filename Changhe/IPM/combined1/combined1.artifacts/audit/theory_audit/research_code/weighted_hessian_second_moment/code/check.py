"""Symbolic checks supplementing the preceding standalone Hessian proof."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sympy as S,json,time
start=time.monotonic();base=Path(__file__).resolve().parents[1]
m,u=S.symbols('m u',real=True)
q=lambda n:n**4+10*n**2+5+(2*n**2+6)*u+u**2
expanded=((m+1)**2+u)*((m+3)**2+u)+2*((m-1)**2+u)*((m+1)**2+u)+((m-1)**2+u)*((m-3)**2+u)
assert S.expand(expanded-4*q(m))==0
certificate=(m-1)*(10*m**3+2*m**2+78*m+6)+(20*m**2-8*m+52)*u+10*u**2
assert S.expand(11*q(m)-q(m+2)-certificate)==0
# Positive-coefficient form on M>=1, u>=0.
z=S.symbols('z',nonnegative=True)
p=S.Poly(S.expand(certificate.subs(m,z+1)),z,u)
assert all(c>=0 for c in p.coeffs())
assert q(1).subs(u,0)==16 and q(3).subs(u,0)==176
assert S.simplify((q(1)+q(3))/(2*q(1))).subs(u,0)==6
# All ordered Cartesian versus complex-Hessian coefficients.
a,b,c=S.symbols('a b c',real=True)
d2=(a-2*S.I*b-c)/4;db=(a+c)/4;bar2=(a+2*S.I*b-c)/4
assert S.expand(4*(d2*S.conjugate(d2)+2*db**2+bar2*S.conjugate(bar2))-(a*a+2*b*b+c*c))==0
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':H(base/'PROOF.md'),'code_sha256':H(__file__),'quartic_identity':True,'mode_bound_certificate':True,'certificate_nonnegative_on_M_ge_1_u_ge_0':True,'real_pair_sharp_squared_factor':6,'ordered_tensor_identity':True,'elapsed_seconds':time.monotonic()-start,'scope':'Exact algebraic checks only; theorem awaits independent Opus review'}
with (base/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
