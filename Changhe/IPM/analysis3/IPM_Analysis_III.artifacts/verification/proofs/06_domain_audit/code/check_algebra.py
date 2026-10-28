from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import gcd
import hashlib,json
import sympy as S
TOP=Path(__file__).resolve().parents[1]
r,th,ell=S.symbols('r th ell',positive=True,real=True)
A=2*ell-1;D=4*ell-1
angular=S.cos(th)**2*S.sin(th)
h=r**S.Rational(31,10)*angular*S.sin(r**(-S.Rational(2,5)))
ar=-A*S.cos(th)**2+D*S.sin(th)**2
br=(A+D)*S.sin(th)*S.cos(th)
image=S.expand(ar*r*S.diff(h,r)+br*S.diff(h,th)-h)
expected=r**3*angular*ar*(S.Rational(1,10)*r**S.Rational(1,10)*S.sin(r**(-S.Rational(2,5)))-S.Rational(2,5)*r**(-S.Rational(3,10))*S.cos(r**(-S.Rational(2,5))))
assert S.trigsimp(S.expand(image-expected))==0
assert S.simplify(ar.subs(th,S.pi/4)-ell)==0
n=1615536043799051;M=2**54-n
assert gcd(M,n)==1 and M==16398862465682933 and M%2==n%2==1
p=5+S.Rational(3,2)/A;q=S.Rational(5,2)
assert S.simplify(-A*p+D*q-1)==0
assert S.simplify((9+2/A)-(p+q)-S.Rational(3,2)-1/(2*A))==0
D2power=F(31,10)-2*(1+F(2,5));D3power=F(31,10)-3*(1+F(2,5))
assert D2power==F(3,10) and D3power==-F(11,10)
assert D3power+F(7,5)*F(9,10)==F(4,25)
assert 2*F(23,10)-6+1==-F(2,5)>-1
x,y,ap,bp,power=S.symbols('x y ap bp power',positive=True,real=True)
w=x**(-ap*power)*y**(-bp*power)
div=S.diff(-A*x*w,x)+S.diff(D*y*w,y)
assert S.simplify(div/w-(D-A+power*(A*ap-D*bp)))==0
res={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'identities':['full polar T_0 of oscillatory counterexample','positive ray coefficient ell','Hessian and third-derivative exponents','Holder split exponent 4/25','image X integrability exponent -2/5','noninteger-y frozen homogeneous counterexample','integer resonance gcd and parity','anisotropic energy divergence'],
 'scope':'Symbolic and exact-rational support for the complete proofs in PROOF.md; no sampled numerical claim.'}
(TOP/'evidence/algebra.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
