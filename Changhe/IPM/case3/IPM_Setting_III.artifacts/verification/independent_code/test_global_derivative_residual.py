"""Independent Gaussian moment test of the residual energy identity and scaling."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
from functools import lru_cache
import json
import sympy as s
x,y,ell,D=s.symbols('x y ell D',real=True);xs=[x,y]
P=y*(4-2*(x*x+y*y));psi=-x*y
Q=[-s.diff(psi,y)+2*y*psi,s.diff(psi,x)-2*x*psi]
def gd(p,i,k=1):return s.expand(s.diff(p,xs[i])-2*k*xs[i]*p)
def gds(p,ids,k=1):
 for i in ids:p=gd(p,i,k)
 return p
@lru_cache(None)
def moment(n,k):
 if n%2:return s.S.Zero
 m=n//2
 return s.factorial2(2*m-1)*s.sqrt(s.pi)/(2**m*s.Integer(k)**(s.Rational(2*m+1,2)))
def integral(poly,k):
 return s.simplify(sum(c*moment(i,k)*moment(j,k) for (i,j),c in s.Poly(s.expand(poly),x,y).terms()))
assert s.expand(gd(Q[0],0)+gd(Q[1],1))==0
assert s.expand(gd(Q[1],0)-gd(Q[0],1)+gd(P,0))==0
assert s.expand(-gd(gd(psi,0),0)-gd(gd(psi,1),1)-gd(P,0))==0
linear=s.expand(ell*(x*gd(P,0)+y*gd(P,1))-P)
nonlinear=s.expand(sum(Q[i]*gd(P,i) for i in range(2)))
E=s.S.Zero;inner=s.S.Zero;comm=s.S.Zero;FF=s.S.Zero
for ids in product(range(2),repeat=3):
 t=gds(P,ids);a=gds(linear,ids);b=gds(nonlinear,ids,2)
 E+=integral(t*t,2)
 inner+=integral(t*a,2)+D*integral(t*b,3)
 comm+=D*integral(t*(b-sum(Q[i]*gd(t,i) for i in range(2))),3)
 FF+=integral(a*a,2)+2*D*integral(a*b,3)+D*D*integral(b*b,4)
assert s.simplify((2*ell-1)*E+comm-inner)==0
assert E>0
eta_squared=s.factor(FF.subs(ell,1+D)/E)
limit=s.simplify(eta_squared.subs(D,0));assert limit>=1
# The exact profile scaling gives norm factors lambda^(-1) on each side.
lam=s.symbols('lam',positive=True)
assert s.simplify(s.sqrt(lam**(-4)*lam**2)-lam**(-1))==0
R=s.Rational(1,1000);V=s.sqrt(2)/5;A=s.Rational(7,5);C=6+3*s.sqrt(2)/2
full=3*V+R+3*(2+s.sqrt(2))*s.sqrt(V*R)
assert float(full)<1.022<1.4
assert float(C*(R+V))>1.4
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','canonical_gaussian':'rho=D*y*(4-2*r^2)*exp(-r^2), psi=-D*x*y*exp(-r^2), ell=1+D; non-profile','E_over_D_squared':str(E),'residual_energy_identity':'exact for symbolic ell,D with all eight ordered derivative slots','eta3_squared_at_ell_1_plus_D':str(eta_squared),'eta3_limit_squared':str(limit),'eta3_samples':[{'D':d,'eta3':float(s.sqrt(eta_squared.subs(D,s.Rational(d))))} for d in ['0.0001','0.01','0.1']],'full_vs_sum_counterexample':{'ell':1.2,'a':.001,'R':float(R),'V':float(V),'full_rhs':float(full),'A':1.4,'coarsened_rhs':float(C*(R+V))},'scope':'Exact Gaussian integration and algebra support the separate general proof; no exact IPM profile, global norm certificate or distance theorem.'}
p=Path('research/global_derivative_residual/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
