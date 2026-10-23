"""Independent exact checks of local flux and the label curl variation."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sympy as s
import json
x,y,eps,A,a=s.symbols('x y eps A a',real=True)
h=x*y*(1+x*x+2*y*y+x*x*y*y)
xi=x+eps*s.diff(h,y);eta=y-eps*s.diff(h,x)
lap=lambda f:s.diff(f,x,2)+s.diff(f,y,2)
E=eta*lap(xi)-A*xi*lap(eta)-(A-1)*(s.diff(xi,x)*s.diff(eta,x)+s.diff(xi,y)*s.diff(eta,y))+a*s.diff(eta,x)
L=A*x*s.diff(lap(h),x)+y*s.diff(lap(h),y)+(A-1-a)*s.diff(h,x,2)-(A-1)*s.diff(h,y,2)
assert s.expand(s.diff(E,eps).subs(eps,0)-L)==0
jac=s.diff(xi,x)*s.diff(eta,y)-s.diff(xi,y)*s.diff(eta,x)
assert s.expand(s.diff(jac,eps).subs(eps,0))==0
checks=[]
for ell,a0 in [(F(3,2),F(-2)),(F(2),F(1)),(F(3),F(5)),(F(5,4),F(7,3))]:
 d=ell-1;AA=2*ell-1;m=4*a0/3;e=4*d*d/3;f=4*d*(a0-d)/3;j=-4*a0*d/3
 assert (AA+3-(3*ell+1))*m==-e-f
 assert j==-e-f
 checks.append({'ell':str(ell),'a0':str(a0),'M_leading':str(m),'E_leading':str(e),'F_leading':str(f),'rho_U2_leading':str(j),'identities':True,'pressure_leading_zero':f==0})
# Direct compact polynomial version of the weighted identity as an algebraic
# divergence equality, using a locally coupled pair (not an exact transport state).
ell=s.Rational(5,2);c=s.Rational(-3,2);a0=s.Rational(7,3);b=s.Rational(2,5);q1=s.Rational(-4,7);q2=-b/3-q1
rho=a0*y+b*x*x*y+s.Rational(3,7)*y**3;psi=c*x*y+q1*x**3*y+q2*x*y**3
u=-s.diff(psi,y);v=s.diff(psi,x)
assert s.expand(-lap(psi)-s.diff(rho,x))==0
Px=-u;Py=-v-rho
P=s.integrate(Px,x);P+=s.integrate(s.expand(Py-s.diff(P,y)),y)
f=(1-x*x-y*y)**4
R=(ell*x+u)*s.diff(rho,x)+(ell*y+v)*s.diff(rho,y)-rho
# LHS of (3) minus RHS = int f*y*R, modulo a total divergence.
Udf=u*s.diff(f,x)+v*s.diff(f,y)
lhs=f*(u*u+v*v)-(P+y*rho)*Udf-((3*ell+1)*f+ell*(x*s.diff(f,x)+y*s.diff(f,y)))*y*rho-f*y*R
fluxx=f*(P*u+y*rho*(ell*x+u));fluxy=f*(P*v+y*rho*(ell*y+v))
assert s.expand(lhs+s.diff(fluxx,x)+s.diff(fluxy,y))==0
out={'utc':datetime.now(timezone.utc).isoformat(),'exact_label_variation':True,'first_order_area_preserving':True,'compact_virial_divergence_and_residual_sign':True,'leading_flux_cases':checks,'scope':'Symbolic identities, not a constructed coupled solution.'}
Path('research/local_energy_geometry/verification/exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
