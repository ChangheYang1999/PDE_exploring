"""Exact rational integrals only; global candidate limit remains unproved."""
from pathlib import Path
from datetime import datetime,timezone
import itertools,json
import sympy as s
x,y=s.symbols('x y',real=True);rr=x*x+y*y
G=-2*y*s.log(1+rr);H=-4*y*rr/(1+rr)
def ordered3sq(f):
 return s.factor(sum(s.diff(f,*axes)**2 for axes in itertools.product([x,y],repeat=3)))
def integral(f):
 num,den=s.fraction(s.cancel(f));poly=s.Poly(den,x,y)
 m=s.degree(den,x)//2
 scale=s.expand(den).coeff(x,2*m)
 assert s.expand(den-scale*(1+rr)**m)==0
 total=0
 for (i,j),c in s.Poly(num,x,y).terms():
  if i%2 or j%2:continue
  a=s.Rational(i,2);b=s.Rational(j,2)
  assert m-a-b-1>0
  total+=c/scale*s.gamma(a+s.Rational(1,2))*s.gamma(b+s.Rational(1,2))*s.gamma(m-a-b-1)/s.gamma(m)
 return s.simplify(total)
# An independent radial Gaussian-free calibration of the integration formula.
assert integral(1/(1+rr)**2)==s.pi
assert integral(x*x/(1+rr)**3)==s.pi/4
E=integral(ordered3sq(G));F=integral(ordered3sq(H))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS rational integrals only','G':'-2y log(1+r^2)','H':'-4y r^2/(1+r^2)','norm_G_squared':str(E),'norm_H_squared':str(F),'ratio_squared':str(s.simplify(F/E)),'scope':'Exact ordered derivative tensor integrals. Does NOT prove global L2 convergence of the D-dependent family. See OPEN_STEPS.md.'}
p=Path('research/global_derivative_residual/verification/formal_limit_integrals.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
