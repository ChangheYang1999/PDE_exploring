from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
g1,g2,xi,eta,chi=s.symbols('g1 g2 xi eta chi',real=True)
a=s.Rational(17,4)
b=(s.sqrt(g1*g1+g2*g2)-g2)/2
M=s.Matrix([[-g2,g1/2],[g1/2,0]])
checks={
 'max_eigenvalue_equation':s.det(b*s.eye(2)-M),
 'eigenvalue_trace':2*b+g2-s.sqrt(g1*g1+g2*g2),
 'principal_symbol':(s.Matrix([[xi,eta]])*M*s.Matrix([xi,eta]))[0]-(g1*xi*eta-g2*xi*xi),
 'edge_norm_exponent':s.Rational(9,2)-a-s.Rational(1,4),
 'edge_squared_integral_exponent':9-2*a-s.Rational(1,2),
 'near_schur_radial_power':(-1)+1,
 'far_squared_kernel_radial_power':(-4)+1+3,
}
result={k:str(s.simplify(v)) for k,v in checks.items()}
assert all(v=='0' for v in result.values()),result
# The two diagonal entries of b I-M are (sqrt(g1^2+g2^2)+g2)/2 and
# (sqrt(g1^2+g2^2)-g2)/2, nonnegative by the ordinary real square-root inequality.
assert s.simplify((b+g2)*b-g1*g1/4)==0
out={'date_utc':datetime.now(timezone.utc).isoformat(),'checks':result,'status':'PASS','scope':'Exact algebra and power checks. Compactness and the weighted-domain argument are proved in PROOF.md.'}
p=Path(__file__).resolve().parents[1]/'evidence'/'check.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
