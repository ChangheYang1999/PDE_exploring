from pathlib import Path
import sympy as s
from flint import arb,ctx
from datetime import datetime,timezone
import json
r,t=s.symbols('r t',positive=True)
p=1-126*t**5+420*t**6-540*t**7+315*t**8-70*t**9
assert all(s.diff(p,t,j).subs(t,0)==(1 if j==0 else 0) for j in range(5))
assert all(s.diff(p,t,j).subs(t,1)==0 for j in range(5))
low=s.expand(1-p.subs(t,2*r-1));high=s.expand(p.subs(t,r-1))
J=0
for f,a,b in [(low,s.Rational(1,2),s.Integer(1)),(high,s.Integer(1),s.Integer(2))]:
    expr=s.expand(r*(f-s.diff(f,r,2)-s.diff(f,r)/r)**2)
    J+=s.integrate(expr,(r,a,b))
J=s.expand(J)
ctx.prec=256
# This expression has rational and log(2) parts only.
rat=s.expand(J).coeff(s.log(2),0);logcoef=s.expand(J).coeff(s.log(2),1)
def aa(q):return arb(int(s.numer(q)))/arb(int(s.denom(q)))
ball=aa(rat)+aa(logcoef)*arb(2).log()
C=(ball/2).sqrt()
output={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
'eta_transition':str(p),'phi_low':str(low),'phi_high':str(high),
'J_exact':str(J),'L1_kernel_upper_bound_sqrt_J_over_2':C.str(50),
'argument':'Cauchy-Schwarz with (1+|x|^2)^-1 and Plancherel gives ||check(phi)||_1 <= sqrt(J/2).',
'constants':{}}
for state in [88,131]:
 d=json.loads((Path(__file__).resolve().parents[2]/'source_audit'/f'state{state:03d}_exact.json').read_text())
 sigma=s.Rational(d['exact_parameters']['sigma'])
 output['constants'][state]={}
 for alpha in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
  beta=aa(alpha-sigma)
  Cb=C*arb(2)**(-2*beta)/(1-arb(2)**beta)
  output['constants'][state][str(alpha)]={'semigroup_bound':Cb.str(40),'inverse_bound':(Cb/(1-aa(alpha))).str(40)}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
