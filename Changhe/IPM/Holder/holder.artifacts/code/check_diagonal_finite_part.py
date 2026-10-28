"""Exact symbolic checks for the fixed-direction second asymptotic term."""
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
from flint import arb,ctx
ctx.prec=256
t,a=s.symbols('t a',positive=True)
y2=4*a*a*t*(t*t+t+1)/(t*t-1)**2
b2=a*a*(t*t+1)**2/(t*t-1)**2
zero=s.factor((b2+y2)*(3*b2-y2)-2*a*a*(b2+y2)-a**4)
D=(t**3-1)/((t+1)*(t*t+1))
dlogy=1/(2*t)+(2*t+1)/(2*(t*t+t+1))-2*t/(t*t-1)
rat=s.factor(-2*D*dlogy)
expected=1/t+2/(t*t+1)-2/(t+1)**2
residual=s.factor(rat-expected)
antiderivative=s.log(t)+2*s.atan(t)+2/(t+1)
derivative_residual=s.factor(s.diff(antiderivative,t)-expected)
assert zero==0 and residual==0 and derivative_residual==0
c0=arb(1)/2+(arb(2).log()-1)/arb.pi()
out={'generated_utc':datetime.now(timezone.utc).isoformat(),'status':'Exact symbolic identities plus an Arb enclosure of the proved constant.',
     'zero_curve_residual':str(zero),'integrand_residual':str(residual),'antiderivative_residual':str(derivative_residual),
     'diagonal_circular_finite_part':'1/2','second_term_exact':'1/2 + (log(2)-1)/pi','second_term_interval':str(c0)}
Path('data/diagonal_finite_part_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
