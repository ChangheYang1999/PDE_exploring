from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as s
T=Path(__file__).resolve().parents[1]
A,a,b,be,q,c,ell,d,c0,cK,k=s.symbols('A a b beta q c ell d c0 cK k', real=True)
D=2*A+1; b0=(A+3)/2
kap=b0+a*A-b*D+(a+b-be)*q
assert s.expand(kap.subs(q,-A)-(b0-(A+D)*b+A*be))==0
assert s.expand(kap.subs(q,D)-(b0+(A+D)*a-D*be))==0
assert s.expand(kap.subs({q:-A,a:s.Rational(5,2),b:0,be:3})-b0-3*A)==0
assert s.expand(kap.subs({q:D,a:s.Rational(5,2),b:0,be:3})-D)==0
assert s.simplify(ell*d+k*(c0+d*cK)/3).subs(d,-k*c0/(3*ell+k*cK)).simplify()==0
x,y=s.symbols('x y',real=True)
u,v,g,r,j,U=s.symbols('u v g r j U', cls=s.Function)
h=x*x*g(y);rho=x*x*r(y)
L=(x*u(y)*s.diff(h,x)+v(y)*s.diff(h,y)-h+x*j(y)*s.diff(rho,x)+U(y)*s.diff(rho,y)+c*(x*s.diff(rho,x)+y*s.diff(rho,y))/3)
row=v(y)*s.diff(g(y),y)+(2*u(y)-1)*g(y)+2*r(y)*j(y)+s.diff(r(y),y)*U(y)+c*(2*r(y)+y*s.diff(r(y),y))/3
assert s.expand(L-x*x*row)==0
B=s.Function('B');t=s.symbols('t',real=True)
lead=row.subs({u(y):-A,v(y):D*y,r(y):y,j(y):-c,U(y):c*y,g(y):y*B(s.log(y))}).doit()
assert s.simplify(lead-D*y*s.Subs(s.diff(B(t),t),t,s.log(y)))==0
p=s.Function('p');P=s.Function('P');Q=s.Function('Q')
psi=p(x)*Q(y);dens=-s.diff(p(x),x)*Q(y)-P(x)*s.diff(Q(y),y,2)
assert s.expand(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(dens,x)).subs(s.diff(P(x),x),p(x)).expand()==0
out={'status':'PASS','date':datetime.now(timezone.utc).isoformat(),'checks':['product-conic endpoints','positive borderline a=5/2','compensation with full strain','full x2 jet row','normalized leading cancellation','compact stream counterexample PDE'], 'proof_sha256':hashlib.sha256((T/'PROOF.md').read_bytes()).hexdigest(),'lead_snapshot_sha256':hashlib.sha256((T/'../20_frozen_origin_global/evidence/lead_snapshot.md').read_bytes()).hexdigest()}
(T/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
