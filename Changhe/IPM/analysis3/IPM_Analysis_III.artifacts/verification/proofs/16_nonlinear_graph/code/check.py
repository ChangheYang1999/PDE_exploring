"""Exact independent unit-packet PDE, strain and quadratic energy check."""
from pathlib import Path
from datetime import datetime,timezone
from math import factorial
import hashlib,json
import sympy as s
x,y,r,v,t=s.symbols('x y r v t',real=True)
u=x*x+y*y
H=s.Poly(x*x*y*(1-u)**6,x,y,domain=s.QQ)
chi=(1-v)**6
f2=r*r*chi.subs(v,r*r)+r**4*s.diff(chi,v).subs(v,r*r)/2
f4=r**4*s.diff(chi,v).subs(v,r*r)/4
psis=[];external=[]
for n,f in [(2,f2),(4,f4)]:
    inner=s.expand((r**(-n)*s.integrate(v**(n+1)*f.subs(r,v),(v,0,r))+r**n*s.integrate(v**(1-n)*f.subs(r,v),(v,r,1)))/(2*n))
    ext=s.integrate(r**(n+1)*f,(r,0,1))/(2*n)
    assert s.simplify(-(s.diff(inner,r,2)+s.diff(inner,r)/r-n*n*inner/r**2)-f)==0
    assert inner.subs(r,1)==ext and s.diff(inner,r).subs(r,1)==-n*ext
    angular=2*x*y if n==2 else 4*x*y*(x*x-y*y)
    pol=s.Poly(s.expand(inner/r**n),r)
    assert all(i[0]%2==0 for i,c in pol.terms())
    psis.append(s.Poly(angular*sum(c*u**(i[0]//2) for i,c in pol.terms()),x,y,domain=s.QQ))
    external.append(ext*angular/u**n)
psi=psis[0]+psis[1]
assert -psi.diff(x).diff(x)-psi.diff(y).diff(y)==H.diff(x)
W1=-psi.diff(y);W2=psi.diff(x)
assert W1.coeff_monomial(x)==-s.Rational(1,56) and W2.coeff_monomial(y)==s.Rational(1,56)
Q=W1*H.diff(x)+W2*H.diff(y)
assert Q.coeff_monomial(x*x*y)==-s.Rational(1,56)
energy=Q.diff(x)**2+Q.diff(y)**2
E=s.Rational(0)
for (i,j),c in energy.terms():
    if i%2 or j%2:continue
    a,b=i//2,j//2
    E+=c*s.Rational(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b+1))*s.Rational(1,2)**(i+j+2)
assert E>0
exterior=external[0]+external[1]
axis=s.factor(s.diff(exterior,x,y).subs(y,0))
assert s.simplify(axis-(x**-4+x**-6)/672)==0
assert E==s.Rational(1552530047839457441465148479,23683970648207968389305777258496000)
root=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','unit_energy_over_pi':str(E),'unit_Q_lowest_term':'-x^2*y/56','translated_axis_strain':str(axis),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'exact polynomial identities; asymptotic and whole-plane membership proof is PROOF.md'}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
