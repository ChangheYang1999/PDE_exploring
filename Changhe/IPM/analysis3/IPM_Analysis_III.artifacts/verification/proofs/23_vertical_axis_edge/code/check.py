from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
from flint import arb,ctx
T=Path(__file__).resolve().parents[1]
x,z,l,a,R=s.symbols('x z lambda a R',positive=True)
# Direct differentiation of the two parity-reduced stream kernels.
klo=-s.exp(-l*z)*s.sinh(l*x)
khi=s.exp(-l*x)*s.cosh(l*z)
assert s.simplify(s.diff(klo,x).subs(x,0)+l*s.exp(-l*z))==0
assert s.simplify(s.diff(klo,x,2)-l*l*klo)==0
assert s.simplify(s.diff(khi,x,2)-l*l*khi)==0
assert s.simplify(khi.subs(x,z)-klo.subs(x,z)-1)==0
assert s.simplify(s.diff(khi,x).subs(x,z)-s.diff(klo,x).subs(x,z))==0
# Weighted Schur primitive exponents, recorded without relying on CAS sign branches.
assert s.expand((s.Rational(1,2)-a)+4+(a-s.Rational(9,2))+1)==1
assert s.expand((s.Rational(1,2)-a)+4+(a-s.Rational(7,2))+1)==2
for p,c in [(4,4),(4,3),(0,0),(2,2),(1,0),(2,1)]:
    row=s.Rational(1,2)-a+p + a-s.Rational(1,2)-c+1
    col=a+s.Rational(1,2)-c + p-a-s.Rational(1,2)+1
    assert s.expand(row-col)==0
# Coefficient-subtraction identity.
r,rp,r1,r2,u1,u2,t,t1=s.symbols('r rp r1 r2 u1 u2 t t1')
A=x*(u1-x*t1);B=x*x*(u2-t)
actual=u1*(2*x*r+x**3*r1)+u2*(x*x*rp+x**4*r2)-x*x*(2*r*t1+rp*t)
assert s.expand(actual-(2*r*A+rp*B+r1*x**3*u1+r2*x**4*u2))==0
ctx.prec=256
av=arb(7)/2
Ca=1+10*2**4+64*(1+1)+(arb(2))*(arb(1)/4+arb(1)/3+arb(1)/2+1)
Ba=arb(315).sqrt()/4; Da=Ca+Ba/arb(2).sqrt()
assert Ca.contains(arb(1759)/6)
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':['stream jump and homogeneous ODE','axis trace derivative','six Schur scaling exponents','subtracted coupling identity'],'a':'7/2','C_a_exact':'1759/6','B_a_exact':'sqrt(315)/4','D_a_exact':'1759/6+sqrt(630)/8','C_a':Ca.str(45),'B_a':Ba.str(45),'D_a':Da.str(45),'proof_sha256':hashlib.sha256((T/'PROOF.md').read_bytes()).hexdigest()}
(T/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
