from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,time
import sympy as s
started=time.monotonic()
x,y,r,t,beta=s.symbols('x y r theta beta',real=True)
b=s.Function('b')(y);A=s.Function('A')(y);q=s.Function('q')(y)
W1=x*(2*beta-s.diff(b,y));W2=b
T=x*x*A;O=x*q
RT=W1*s.diff(T,x)+W2*s.diff(T,y)-(beta-2)*T
RO=W1*s.diff(O,x)+W2*s.diff(O,y)+O-s.diff(T,x)
checks={
 'theta_axis_equation':s.simplify(RT/x**2-(b*s.diff(A,y)+(3*beta+2-2*s.diff(b,y))*A)),
 'omega_axis_equation':s.simplify(RO/x-(b*s.diff(q,y)+(2*beta+1-s.diff(b,y))*q-2*A)),
 'A_tail_exponent':s.simplify((2*beta-(3*beta+2))/beta+1+2/beta),
 'q_h_tail_exponent':s.simplify((beta-(2*beta+1))/beta+1+1/beta),
 'R_prime_exponent':s.simplify((-1-2/beta)-1-(-1-1/beta)+1+1/beta),
}
F=s.Function('F')(r,t)
def dx(expr):return s.cos(t)*s.diff(expr,r)-s.sin(t)/r*s.diff(expr,t)
d1=dx(F);d2=s.expand(dx(d1))
for name,angle,sgn in [('upper',s.pi/2,-1),('lower',-s.pi/2,1)]:
 checks[name+'_first_polar_derivative']=s.simplify((d1-sgn*s.diff(F,t)/r).subs(t,angle))
 checks[name+'_second_polar_derivative']=s.simplify((d2-s.diff(F,r)/r-s.diff(F,t,2)/r**2).subs(t,angle))
checks['temperature_axis_scaled_exponent']=s.simplify(2-(1-2/beta)-(1+2/beta))
obj={'written_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'sympy':s.__version__,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':{k:str(v) for k,v in checks.items()},'passed':all(v==0 for v in checks.values()),'scope':'Exact algebra only, not a PDE existence or nonexistence proof.'}
Path('research/65_axis_angular_tail_matching/verification/symbolic_results.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2));assert obj['passed']
