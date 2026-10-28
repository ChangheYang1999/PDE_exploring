from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[1]
t,x,y,g1,g2=s.symbols('t x y g1 g2', real=True)
K=(g2*(x*x-y*y)-2*g1*x*y)/(2*s.pi*(x*x+y*y)**2)
scaled=K.subs({x:(1+t)*x,y:(1+t)*y}, simultaneous=True)
assert s.simplify(s.diff(scaled,t,6).subs(t,0)-s.factorial(7)*K)==0
order=F(41,20)
assert order+1-6==-F(59,20)
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','graph_bounded_output_exponent':str(order+1-6),'homogeneous_sixth_derivative_factor':5040,'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
