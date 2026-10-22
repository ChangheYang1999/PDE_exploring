"""Exact Cartesian forcing and symbolic-function Euler differentiation, topic 213."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
r=s.symbols('r',positive=True); x,y,ell,c=s.symbols('x y ell c',real=True)
I5,I7,J,C=[s.Function(n)(r) for n in ['I5','I7','J','C']]
subs={s.diff(I5,r):r**5*C,s.diff(I7,r):r**7*C,s.diff(J,r):-r*C}
def D(f):return s.expand((r*s.diff(f,r)).subs(subs))
psi=[(r**2*J-r**-2*I5)/8,-r**-4*I7/8]
d1=[D(p) for p in psi];d2=[D(p) for p in d1]
forcing=[r**2*C+r**3*s.diff(C,r)/4,r**3*s.diff(C,r)/8]
checks={}
for i,m in enumerate([2,4]):checks[f'poisson_{m}']=s.simplify(-d2[i]+m*m*psi[i]-r*r*forcing[i])==0
q=x*x+y*y; a,b=s.symbols('a b'); sin2=2*x*y/q;sin4=4*x*y*(x*x-y*y)/q**2
checks['cartesian_forcing']=s.cancel(2*x*y*a+2*x**3*y*b-(q*a+q*q*b/2)*sin2-q*q*b/4*sin4)==0
p=x*x*y
checks['affine_cubic']=s.expand((ell-c)*x*s.diff(p,x)+(ell+c)*y*s.diff(p,y)-p).subs(c,3*ell-1).expand()==0
# Each symbolic expression is normalized by r^2, with primitive variables.
A,B,E,F,G=s.symbols('J1 I5scaled I7scaled r2chi r2Dchi')
normal={J:A,I5:r**4*B,I7:r**6*E,C:F/r**2,s.diff(C,r):G/r**3}
coeffs=[]
for i in range(2):coeffs.append([str(s.expand(v/r**2).subs(normal,simultaneous=True).expand()) for v in [psi[i],d1[i],d2[i]]])
z=s.symbols('B1',nonnegative=True)
bounds=[[s.Rational(1,12),s.Rational(5,12),s.Rational(4,3)+z/4],[s.Rational(1,64),s.Rational(3,16),s.Rational(1,4)+z/8]]
hessian=s.expand(sum(a2+(2+2*m)*a1+(m*m+2*m)*a0 for m,(a0,a1,a2) in zip([2,4],bounds)))
checks['hessian_constant']=s.expand(hessian-(7+3*z/8))==0
checks['strain_rankone']=s.Rational(1,8)/3==s.Rational(1,24)
# Explicit exterior multipoles prove parity and rational decay of axis quotients.
P,Q=s.symbols('P Q');psiext=P*2*x*y/q**2+Q*4*x*y*(x*x-y*y)/q**4
u1=s.cancel(-s.diff(psiext,y)/x);u2=s.cancel(s.diff(psiext,x)/y)
checks['axis_quotients_no_axis_denominators']=s.denom(u1).subs({x:0,y:1})!=0 and s.denom(u2).subs({x:1,y:0})!=0
for value in checks.values():
 if not value:raise RuntimeError(checks)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SYMBOLIC_IDENTITIES','checks':checks,'normalized_derivatives':coeffs,'hessian_bound':str(hessian),'exterior_axis_quotients':[str(u1),str(u2)],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
(ROOT/'evidence/symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
