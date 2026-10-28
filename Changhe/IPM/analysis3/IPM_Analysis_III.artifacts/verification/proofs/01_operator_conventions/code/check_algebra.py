"""Independent exact identities. No imported project evaluator. Outputs in this topic."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
x,y,ell,c=s.symbols('x y ell c', real=True)
r2=x*x+y*y
G=-s.log(r2)/(4*s.pi)
kern=-s.diff(x*y/r2**2,x)
assert s.factor(kern-y*(3*x*x-y*y)/r2**3)==0
assert s.factor(s.diff(G,x,x,y)+kern/s.pi)==0
p=x*x*y
assert s.expand((-s.Rational(2,3)*c*x)*s.diff(p,x)+(s.Rational(4,3)*c*y)*s.diff(p,y))==0
assert s.expand((ell-c)*x*s.diff(p,x)+(ell+c)*y*s.diff(p,y)-(3*ell-c)*p)==0
assert (1+2*ell-c).subs(c,3*ell-1)==2-ell
assert (1+2*ell+c).subs(c,3*ell-1)==5*ell
A,D,nu=s.symbols('A D nu', positive=True)
a=(D*nu-1)/(A+D);b=(1+A*nu)/(A+D)
assert s.simplify(a+b-nu)==0
assert s.simplify(-A*a+D*b-1)==0
th=s.symbols('th', real=True)
phi=s.cos(th)**2*s.sin(th)
assert s.integrate(phi**2,(th,0,2*s.pi))==s.pi/8
assert s.integrate(s.diff(phi,th)**2,(th,0,2*s.pi))==5*s.pi/8
q=s.symbols('q', real=True)
assert s.integrate(q*(1-q*q)**6,(q,0,1))/4==s.Rational(1,56)
result={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_EXACT_ALGEBRA','checks':['density kernel sign','third Newtonian derivative','normalization coefficient','leading cancellation','origin energy diagonal','general critical exponents','bump angular integrals','bump strain 1/56'],'scope':'Exact symbolic identities only; all analytic and domain arguments are in PROOF.md.'}
out=Path(__file__).resolve().parents[1]/'evidence/algebra.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
