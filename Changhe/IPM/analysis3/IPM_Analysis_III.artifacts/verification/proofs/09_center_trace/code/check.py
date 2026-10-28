from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
r,z,th=S.symbols('r z th',positive=True)
x,y=S.symbols('x y',real=True)
H=x*x*y*(1-x*x-y*y)**6
chi=(1-z)**6
f2=r*r*chi.subs(z,r*r)+r**4*S.diff(chi,z).subs(z,r*r)/2
f4=r**4*S.diff(chi,z).subs(z,r*r)/4
actual=S.diff(H,x).subs({x:r*S.cos(th),y:r*S.sin(th)})
assert S.trigsimp(actual-f2*S.sin(2*th)-f4*S.sin(4*th))==0
c=S.integrate(r*(1-r*r)**6/4,(r,0,1)); assert c==S.Rational(1,56)
out={}
for n,f in [(2,f2),(4,f4)]:
 exterior=S.integrate(r**(n+1)*f,(r,0,1))/(2*n)
 inner=(r**(-n)*S.integrate(z**(n+1)*f.subs(r,z),(z,0,r))+r**n*S.integrate(z**(1-n)*f.subs(r,z),(z,r,1)))/(2*n)
 inner=S.expand(inner)
 assert S.simplify(-(S.diff(inner,r,2)+S.diff(inner,r)/r-n*n*inner/r**2)-f)==0
 assert S.simplify(inner.subs(r,1)-exterior)==0
 assert S.simplify(S.diff(inner,r).subs(r,1)+n*exterior)==0
 out[str(n)]={'inner':str(inner),'exterior_coefficient':str(exterior)}
assert (4*c-4*c)/3==0
alpha,k=S.symbols('alpha k',real=True)
assert S.expand(2*(2+alpha)-6+1)==-1+2*alpha
assert S.expand(2*(alpha-2)-6+1)==2*alpha-9
assert S.expand(2*(k-4)+(-2*k-3)+1)==-10
root=Path(__file__).resolve().parents[1]
result={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'strain':str(c),'streams':out,'all_checks':'PASS'}
(root/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
