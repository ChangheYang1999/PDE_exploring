"""Exact, separately implemented polar/Laurent audit of formal result36."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
z=s.symbols('z',nonzero=True);i=s.I
h,F,hp,Fp=s.symbols('h F hp Fp');C=F-1
sn=lambda n:(z**n-z**(-n))/(2*i)
cs=lambda n:(z**n+z**(-n))/2
dt=lambda f:s.expand(i*z*s.diff(f,z))
def coef(f,n):return s.expand(2*i*s.expand(f).coeff(z,n))
checks=[]
for j in range(1,18,2):
 actual=s.expand(-cs(2)*sn(j)+sn(2)*dt(sn(j)))
 wanted=(j-1)*sn(j+2)/2-(j+1)*sn(j-2)/2
 assert s.expand(actual-wanted)==0
checks.append('source strain trigonometric operator, all j=1..17 odd')
for j in range(1,18,2):
 b,bp,D=s.symbols('b bp D')
 actual=s.expand(cs(1)*(b+D*bp)*sn(j)-sn(1)*b*dt(sn(j)))
 wanted=(D*bp+(1-j)*b)*sn(j+1)/2+(D*bp+(1+j)*b)*sn(j-1)/2
 assert s.expand(actual-wanted)==0
checks.append('direct density x derivative, all j=1..17 odd')
M=8
js=list(range(3,2*M+2,2));a={j:s.symbols('h'+str(j)) for j in js};a[1]=0
H=sum(a[j]*sn(j) for j in js)
Phi=0
for m in range(4,2*M+3,2):
 phi=a.get(m+1,0)/s.Integer(2*(m-2))-a.get(m-1,0)/s.Integer(2*(m+2))
 source=((2-m)*a.get(m-1,0)+(m+2)*a.get(m+1,0))/2
 assert s.expand((m*m-4)*phi-source)==0
 Phi+=phi*sn(m)
G=-C*hp/2+h*Fp/4
res=s.expand(H+C*(-cs(2)*H+sn(2)*dt(H))+h*(2*Phi*cs(1)-dt(Phi)*sn(1))+G*sn(3))
res=res.subs({hp:-h*F,Fp:h*F/4-a[3]})
for j in js:
 actual=s.expand(-coef(res,j))
 if j==3:
  wanted=-(1-h/2)*a[j]+(3*C-3*h/4)*a.get(5,0)+h*F*(s.Rational(1,2)-F/2-h/16)
 else:
  wanted=-(1-h/2)*a[j]-(j-3)*(C/2+h/s.Integer(4*(j+1)))*a[j-2]+(j+3)*(C/2-h/s.Integer(4*(j-1)))*a.get(j+2,0)
 assert s.expand(actual-wanted)==0,(j,s.factor(actual-wanted))
checks.append('nonresonant Poisson and every projected row through mode17, including boundary coupling')
# Build the finite invariant linear blocks directly from the verified residual coefficients.
finite=[]
lam=s.symbols('lam')
for N in range(0,8):
 alpha=8+4*N
 fvar=s.symbols('f')
 variables=[fvar]+[a[j] for j in range(3,2*N+2,2)]
 rhs=[h*F/4-a[3]]
 for j in range(3,2*N+2,2):rhs.append(-coef(res,j))
 sub={h:alpha,F:0,**{a[j]:0 for j in js}}
 matrix=s.Matrix([[s.diff(row,F if k==0 else variables[k]).subs(sub) for k in range(N+1)] for row in rhs])
 # The first omitted row receives no forcing from the last retained mode.
 if N==0:
  assert s.simplify(s.diff(-coef(res,3),F).subs(sub))==0
 else:
  omitted=2*N+3
  assert s.simplify(s.diff(-coef(res,omitted),a[omitted-2]).subs(sub))==0
 poly=matrix.charpoly(lam).as_expr();expected=s.prod(lam-(2+4*k) for k in range(N+1))
 assert s.expand(poly-expected)==0,(N,matrix,s.factor(poly))
 finite.append({'alpha':alpha,'N':N,'eigenvalues':[2+4*k for k in range(N+1)],'exact_characteristic_polynomial':str(s.factor(poly))})
checks.append('invariant linear source blocks and exact spectra for alpha=8,12,...,36; finite tests only')
# The omitted fifth-mode equation prevents a nonconstant exact two-mode orbit.
ht=-h*(1-h/12);kt=h*(1-h/12)/6
actual=s.diff(kt,h)*ht
wanted=-(1-h/2)*kt+h*(1-h/12)*(s.Rational(1,2)-(1-h/12)/2-h/16)
assert s.expand(actual-wanted-5*h*ht/144)==0
checks.append('two-mode incompatibility factor 5 h hprime/144 from the omitted fifth harmonic')
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':checks,'finite_block_checks':finite,'scope':'Exact formal coefficient identities. No small-D asymptotic theorem or nonlinear PDE existence inference. The displayed finite spectrum tests alone do not prove an all-N formula.'}
Path('research/slow_radius_hierarchy/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
