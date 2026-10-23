"""Exact local jets and rational infinite Jacobi-tail certificates at weight five."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
import numpy as np
checks=[]
x,y,a,ell,b,e,q1,q2,D=s.symbols('x y a ell b e q1 q2 D',real=True)
A=2*ell-1
rho=a*y+b*x*x*y+e*y**3
psi=-D*x*y+q1*x**3*y+q2*x*y**3
u1=-s.diff(psi,y);u2=s.diff(psi,x)
R=s.expand((ell*x+u1)*s.diff(rho,x)+(ell*y+u2)*s.diff(rho,y)-rho).subs(D,ell-1)
def check(name,v):
 assert s.factor(v)==0,(name,s.factor(v))
 checks.append(name)
check('x2y transport coefficient',R.coeff(x,2).coeff(y,1)-(2*A*b+3*a*q1))
check('y3 transport coefficient',R.coeff(x,0).coeff(y,3)-(2*e+a*q2))
P=s.expand(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(rho,x))
check('xy Poisson coefficient',P.coeff(x,1).coeff(y,1)+6*(q1+q2)+2*b)
S11=s.diff(u1,x);S12=(s.diff(u1,y)+s.diff(u2,x))/2
strain=s.Poly(s.expand(S11*S11+S12*S12-D*D),x,y)
quad=sum(c*x**i*y**j for (i,j),c in strain.terms() if i+j==2)
check('strain norm quadratic term',quad+6*D*(q1*x*x+q2*y*y))
qs={q1:-2*A*b/(3*a),q2:-2*e/a}
check('jet compatibility',s.together((q1+q2+b/3).subs(qs))-((a-2*A)*b-6*e)/(3*a))
check('vertical compression quadratic coefficient',(-u2.subs(x,0)/y).expand().coeff(y,2)+q2)

m=s.symbols('m',positive=True)
cert=[]
for sg,lam in [(1,F(2363,1000)),(-1,F(1367,1000))]:
 N=8;bb=lambda j:F(4*j*j+25,4*abs(4*j*j-25));tau=F(sg,2)+2*bb(N+1)
 assert lam>tau
 pp=[]
 for j in range(1,N+1):
  val=lam-sg*(F(1,4) if j==1 else F(1,2))
  if j>1:val-=bb(j-1)**2/pp[-1]
  if j==N:val-=bb(j)**2/(lam-tau)
  assert val>0
  pp.append(val)
 cert.append({'m':5,'sign':sg,'N':N,'lambda_upper':str(lam),'tail_upper':str(tau),'pivots':list(map(str,pp))})
bs=[F(4*j*j+8,4*abs(4*j*j-8)) for j in range(1,10)]
assert bs[0]==bs[1]==F(3,4) and bs[2]==F(11,28)
assert F(1,4)+bs[0]==1 and F(1,2)+bs[0]+bs[1]==2
assert max(F(1,2)+bs[j-1]+bs[j] for j in range(2,9))<2
checks.append('sqrt8 row-sum bound exact links')
for mv in range(3,102,2):
 ratios=[F(n+mv,abs(n-mv)) for n in range(2,2*mv+4,2)]
 assert max(ratios)==2*mv+1
checks.append('odd-weight shift maximum for 50 supporting integers')
# Direct spectra are supporting diagnostics only; bounds above are exact.
spectra=[]
for mv in (3.,4.2,4.5,5.,5.5,5.8,7.):
 for N in (32,64,128):
  ns=2*np.arange(1,N);bb=(ns*ns+mv*mv)/(4*abs(ns*ns-mv*mv))
  dd=np.full(N,.5);dd[0]=.25
  qm=np.linalg.eigvalsh(np.diag(dd)+np.diag(bb,1)+np.diag(bb,-1))[-1]
  qp=np.linalg.eigvalsh(np.diag(-dd)+np.diag(bb,1)+np.diag(bb,-1))[-1]
  spectra.append({'m':mv,'N':N,'Qminus_finite':float(qm),'Qplus_finite':float(qp)})
  if mv==5:assert qm<2.363 and qp<1.367
bounds=[]
for lv in (F(1),F(3,2),F(2),F(3)):
 p=min(4*lv-2,(4-lv)*1000/F(2363));n=(4-lv)*1000/F(1367)
 bounds.append({'ell':str(lv),'ell1_is_limit_only':lv==1,'positive_lower_exact':str(p),'negative_magnitude_lower_exact':str(n),'positive_decimal':float(p),'negative_decimal':float(n)})
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_jet_and_shift_checks':checks,'infinite_tail_certificates':cert,'certified_single_weight_bounds':bounds,'finite_spectrum_support':spectra,'scope':'Conditional on global sigma<=D. The local jet signs, extra weighted integrability and infinite-tail argument are proved in PROOF.md. Sampled strain never supplies a cap. Finite spectra do not certify bounds.'}
out=Path('research/strain_cap_jet_gap/verification/checks.json');out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'certificates':len(cert),'spectra':len(spectra)}))
