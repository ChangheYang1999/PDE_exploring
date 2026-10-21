from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json
ROOT=Path(__file__).resolve().parents[1]
b,A,g=s.symbols('b A g',positive=True)
lead=(b-1)*A**(1-b)/3*(-A**(b-2)/(2*g**(b+2)))
assert s.simplify(lead-(1-b)/(6*A*g**(b+2)))==0
p=3-b;I=s.simplify((b-2)*(b-3)+(g/A)*(b-3));assert s.simplify(I-(3-b)*(2-b-g/A))==0
x=s.symbols('x');v=s.Function('v')(x);w=s.Function('w')(x)
eta_prime=s.diff(s.log(1+v/w),x)-A*(1/(w+v)-1/w)
assert s.simplify(eta_prime-(s.diff(v,x)/(w+v)+(A-s.diff(w,x))*v/(w*(w+v))))==0
k=(1-b)*(3-b)*(2-b-g/A)/(6*A*g**(b+2))
out={'date':datetime.now(timezone.utc).isoformat(),'coefficient_residual':'0','integration_by_parts_coefficient_residual':'0','density_ratio_derivative_residual':'0','kappa_A4_L1':str(k.subs({A:4,b:s.Rational(1,2),g:s.Rational(1,2)})),'scope':'Exact algebra supporting the full informal proof. No nonlinear candidate calculation or global profile conclusion.'}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
