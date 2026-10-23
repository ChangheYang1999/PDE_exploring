"""Independent exact checks after the standalone proof; no producer code."""
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
x,y,ell,k,t,w=s.symbols('x y ell k t w', real=True)
A=2*ell-1;D=ell-1
rho=A*y*(1+s.cos(k*x));psi=y*(ell*x-A*s.sin(k*x)/k)
ux=-s.diff(psi,y);uy=s.diff(psi,x)
checks=[]
def check(name,expr):
    assert s.factor(s.trigsimp(s.expand(expr)))==0,name
    checks.append(name)
check('elliptic',-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(rho,x))
check('transport',(ell*x+ux)*s.diff(rho,x)+(ell*y+uy)*s.diff(rho,y)-rho)
s11=s.diff(ux,x);s12=(s.diff(ux,y)+s.diff(uy,x))/2
fac=A*(1-s.cos(k*x))*(-2*D+A*(1-s.cos(k*x))+A*k*k*y*y*(1+s.cos(k*x))/4)
check('strain_factorization',s11*s11+s12*s12-D*D-fac)
Aa=s.symbols('Aa',positive=True)
d=-5*(Aa+1)*w+3*t*t/(2*Aa);e=10*Aa*w;f=-Aa*w/2
u=2*(Aa+1)*w-3*t*t/(10*Aa);v=-s.Rational(10,3)*(Aa+1)*w
h5=d*x**4*y+e*x*x*y**3+f*y**5;phi6=u*x**5*y+v*x**3*y**3+w*x*y**5
check('fifth_transport',Aa*x*s.diff(h5,x)+y*s.diff(h5,y)-h5+2*Aa*s.diff(phi6,x)-3*t*t*x**4*y)
check('fifth_poisson',-s.diff(phi6,x,2)-s.diff(phi6,y,2)-s.diff(h5,x))
z,al=s.symbols('z al',positive=True)
H=(s.exp(-al*z)-al*s.exp(-z))/(1-al)
check('radial_first_expression',H+s.diff(H,z)-s.exp(-al*z))
G=((1-al/2+al*al/4)*s.exp(-al*z)-3*al*s.exp(-z)/4)/(1-al)
check('radial_second_expression',H+s.diff(H,z)/2+s.diff(H,z,2)/4-G)
b,L=s.symbols('b L',positive=True);F=s.Function('F');K=s.Function('K');g=s.Function('g')
pr=b/L*F(x/L)*g(y);rr=-b/L**2*s.diff(F(x/L),x)*L*g(y)-b*K(x/L)*s.diff(g(y),y,2)
identity=-s.diff(pr,x,2)-s.diff(pr,y,2)-s.diff(rr,x)
identity=identity.subs(s.Subs(s.Derivative(K(z),z),z,x/L),F(x/L))
# Subs variable names can differ; replacing the derivative through an explicit
# abstract primitive is independent of any cutoff coefficient values.
rr2=-b/L**2*s.diff(F(z),z).subs(z,x/L)*g(y)-b*K(x/L)*s.diff(g(y),y,2)
expr=-s.diff(pr,x,2)-s.diff(pr,y,2)-s.diff(rr2,x)
expr=expr.replace(lambda q:isinstance(q,s.Subs) and q.expr==s.Derivative(K(q.variables[0]),q.variables[0]),lambda q:F(q.point[0]))
check('remote_poisson',expr)
assert 1458*974+(29160*s.Rational(4,3)+729*4862)/2==3211731
assert 3211731<4000000
checks.append('exact_remote_bound')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':checks,'scope':'Exact local PDE, strain factorization, fifth-degree identities, radial formulas and remote elliptic identity. Global positivity, support and cap bounds are proved in PROOF.md.'}
p=Path('research/capped_local_and_ball_examples/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
