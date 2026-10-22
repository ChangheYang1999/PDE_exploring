"""Exact polynomial contracts and independent integral power-series bounds."""
import json,math,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
import cell_iv as c
BASE=Path(__file__).resolve().parents[3]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def overlap(x,y):
 a,b=c.ends(x);d,e=c.ends(y);assert max(a,d)<=min(b,e)
def integral_series(p,H,lam,K=160):
 out=iv.mpf(0);tail=iv.mpf(0);x=abs(lam*H);assert x<F(K+2)
 for j,pj in enumerate(p):
  finite=sum((lam**q*H**(q+j+1)/F(math.factorial(q)*(q+j+1)) for q in range(K+1)),F(0))
  radius=abs(pj)*H**(j+1)*x**(K+1)/F(math.factorial(K+1)*(K+j+2))/(1-x/F(K+2))
  out+=c.iq(pj*finite);tail+=c.iq(radius)
 rad=c.ends(tail)[1];lo,hi=c.ends(out);return c.hull(lo-rad,hi+rad)
checks=[]
for lam,H in [(F(0),F(1,9)),(F(0),F(0)),(F(2),F(1,1024)),(F(-2),F(1,1024)),(F(526),F(1,100)),(F(-526),F(1,100)),(F(4),F(1,100000))]:
 p=[F((-1)**j*(j+2),j+1) for j in range(8)]
 actual=c.integrate_exp_poly([c.iq(v) for v in p],H,lam);oracle=integral_series(p,H,lam)
 overlap(actual,oracle);checks.append({'lambda':str(lam),'H':str(H),'kind':'complete_integral_vs_series','actual':c.out(actual),'oracle':c.out(oracle)})
 if lam:
  # Symbolic antiderivative identity Q'+lambda Q=P, independent exact arithmetic.
  q=[sum(((-1)**(j-l)*F(math.factorial(j),math.factorial(l))*p[j]/lam**(j-l+1) for j in range(l,8)),F()) for l in range(8)]
  assert all(lam*q[l]+((l+1)*q[l+1] if l<7 else 0)==p[l] for l in range(8))
polynomial_checks=0
for lam,sig,h in [(F(-526),1,F(1,100)),(F(518),-1,F(1,100)),(F(0),-1,F(1,17))]:
 # Prescribe an exact polynomial y(v), derive its physical-t forcing G.
 y=[F((-1)**q,q+1) for q in range(8)];g=[((q+1)*y[q+1]/h if q<7 else 0)-lam*y[q] for q in range(8)];g=[z/sig for z in g]
 p,r=c.closed_ode(c.iq(y[0]),lam,sig,[c.iq(z) for z in g],h,16)
 for q,x in enumerate(p):
  lo,hi=c.ends(x);target=y[q] if q<8 else F(0);assert lo<=target<=hi;polynomial_checks+=1
 assert c.ends(r)[0]>=0
# Translation law checked against direct rational binomial expansion.
raw=[F(j+1,j+2) for j in range(8)];delta=F(-3,17)
s=c.shift([c.iq(x) for x in raw],delta)
for l,v in enumerate(s):
 expected=sum((raw[j]*math.comb(j,l)*delta**(j-l) for j in range(l,8)),F())
 lo,hi=c.ends(v);assert lo<=expected<=hi;polynomial_checks+=1
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CONTRACTS','integral_checks':len(checks),'polynomial_coefficient_checks':polynomial_checks,'source_sha256':sha(Path(__file__)),'cell_iv_sha256':sha(Path(c.__file__)),'iv_dps':iv.dps,'integrals':checks}
out=BASE/'research/middle_second/evidence/contracts.json';tmp=out.with_suffix('.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
print(json.dumps({k:v for k,v in result.items() if k!='integrals'}))
