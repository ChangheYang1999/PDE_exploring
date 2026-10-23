"""Exact independent polynomial check of residual jets and Green moments.

Local only. No JS/TS, servers/listeners or RLScience cluster.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import factorial
import hashlib, json
rows=[]
def check(name,a,b,**values):
    assert a==b,(name,a,b)
    rows.append({'name':name,**{k:str(v)for k,v in values.items()}})
def add(*polys):
    out={}
    for poly in polys:
        for k,v in poly.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items()if v}
def scale(poly,c):return {k:c*v for k,v in poly.items()}
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),F(0))+v*w
    return out
def diff(a,index):
    out={}
    for key,v in a.items():
        d=key[index]
        if d and v:
            nk=list(key);nk[index]-=1;out[tuple(nk)]=v*d
    return out
for ell in [F(6,5),F(3,2),F(2),F(3),F(8)]:
 for a in [F(-7),F(1,3),F(13)]:
  for C0 in [F(-2,7),F(0),F(3,11)]:
   for b,e,q1 in [(F(-3),F(5),F(4,9)),(F(0),F(2),F(-1,3)),(F(7,5),F(-3,4),F(5,13))]:
    s0=C0+1-ell;A=2*ell-1;q2=-b/3-q1
    rho={(0,1):a,(2,1):b,(0,3):e};psi={(1,1):s0,(3,1):q1,(1,3):q2}
    U1=scale(diff(psi,1),-1);U2=diff(psi,0)
    W1=add({(1,0):ell},U1);W2=add({(0,1):ell},U2)
    R=add(mul(W1,diff(rho,0)),mul(W2,diff(rho,1)),scale(rho,-1))
    minus_lap=scale(add(diff(diff(psi,0),0),diff(diff(psi,1),1)),-1)
    check('Poisson polynomial',minus_lap,diff(rho,0))
    r01=R.get((0,1),F(0));r21=R.get((2,1),F(0));r03=R.get((0,3),F(0))
    check('linear residual',r01,a*C0)
    check('mixed cubic residual',r21,(2*A-C0)*b+3*a*q1)
    check('pure cubic residual',r03,(2+3*C0)*e+a*q2)
    check('T1 defect',6*e-(a-2*A)*b,r21+3*r03-C0*(9*e-b))
    check('T2 defect',q1-q2-(a-4*A)*b/(3*a),F(2,3)/a*(r21+C0*b))
# Integral int_0^infty r^(2k+1)/(1+r^2)^p dr, obtained by t=r^2
# followed by w=t/(1+t), then elementary polynomial beta integration.
def beta(k,p):return F(factorial(k)*factorial(p-k-2),2*factorial(p-1))
for p in range(4,13):
 for B in [F(-3),F(0),F(2,7)]:
  for E in [F(-2,3),F(0),F(5)]:
   # b3=B r^3 (1+r^2)^(-p), b5=E r^5 (1+r^2)^(-p).
   # Differentiate these source modes before radial integration.
   source_moment=-p*B*beta(0,p+1)+5*E*beta(0,p)-p*E*beta(1,p+1)
   # Independently take the r^4 coefficient from the integrated-by-parts
   # density Green formula P4=.5[r^4 int_r^inf b5/s^4-r^-4 int_0^r s^4 b3].
   stream_coefficient=F(1,2)*E*beta(0,p)-B/F(16)
   check('frequency-four source moment vs canonical quartic stream',source_moment,8*stream_coefficient,p=p,B=B,E=E)
   check('closed rational moment',source_moment,-B/2+2*E/(p-1))
for ell in [F(6,5),F(3,2),F(2),F(3),F(4),F(8)]:
 a=4*(ell-1);A=2*ell-1
 for t in [F(1,7),F(1),F(100)]:
  check('canonical compact perturbation mixed cubic',2*A*t+3*a*(-t/6),2*ell*t,ell=ell,t=t)
  check('canonical compact perturbation pure cubic',2*t+a*(-t/6),(8-2*ell)*t/3,ell=ell,t=t)
  check('canonical compact perturbation T1',6*t-(a-2*A)*t,8*t)
now=datetime.now(timezone.utc).isoformat();proof=Path('research/residual_center_jets/PROOF.md')
record={'utc':now,'status':'PASS','count':len(rows),'checks':rows,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebraic checks. Analytic cutoff estimates are justified in PROOF.md, not certified by these tests.'}
Path('research/residual_center_jets/verification/exact_checks.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:record[k]for k in ['utc','status','count','proof_sha256','checker_sha256']}))
