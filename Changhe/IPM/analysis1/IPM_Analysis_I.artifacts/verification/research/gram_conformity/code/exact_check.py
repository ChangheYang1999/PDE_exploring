from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb,factorial
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conformity'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(x,s):
 if not x:raise ValueError(s)
old=B/'research/gram_reference_space/evidence/verdict.json';v=json.loads(old.read_text());check(len(v['files'])==40,'prior pins')
for n,h in v['files'].items():check(sha(B/n)==h,n)
# Expanded multivariate polynomial of a, at, atheta.
def add(p,q):
 r=p.copy()
 for i,v in q.items():r[i]=r.get(i,F(0))+v
 return {i:v for i,v in r.items() if v}
def mul(p,q):
 r={}
 for i,v in p.items():
  for j,w in q.items():k=tuple(x+y for x,y in zip(i,j));r[k]=r.get(k,F(0))+v*w
 return {i:v for i,v in r.items() if v}
a={(1,0,0):F(1)};t={(0,1,0):F(1)};ang={(0,0,1):F(1)};rad=add({k:3*v for k,v in a.items()},t)
energy=add(add(mul(a,a),mul(rad,rad)),mul(ang,ang));expected={(2,0,0):F(10),(1,1,0):F(6),(0,2,0):F(1),(0,0,2):F(1)};check(energy==expected,'energy polynomial')
# Affine exponents in variables(1,k,d,j), constructed from the a formula.
def plus(*args):return tuple(sum(x) for x in zip(*args))
def scale(n,a):return tuple(n*x for x in a)
inn=(0,0,0,2);outer=(-3,1,-1,0);center=plus((2,0,0,0),scale(2,inn));far=plus((5,-2,0,0),scale(2,outer));check(center==(2,0,0,4) and far==(-1,0,-2,0),'exponents')
moments={q:sum(comb(2*q,j)*factorial(j) for j in range(2*q+1)) for q in range(7)};check(moments[0]==1 and moments[1]==5,'tail moments')
# Compact reference radial constants, explicit expanded coefficient integration.
chi=[F((-1)**j*comb(6,j)) for j in range(7)] # polynomial in z=s^2
chi2=[sum((chi[i]*chi[n-i] for i in range(7) if 0<=n-i<7),F(0)) for n in range(13)]
I0=sum((c/F(2*j+2) for j,c in enumerate(chi2)),F(0));Icross=sum((F(j)*c/F(2*j+2) for j,c in enumerate(chi2)),F(0))
d=[F(j+1)*chi[j+1] for j in range(6)];dd=[sum((d[i]*d[n-i] for i in range(6) if 0<=n-i<6),F(0)) for n in range(11)];I2=sum((4*c/F(2*j+6) for j,c in enumerate(dd)),F(0));check((I0,Icross,I2)==(F(1,26),F(-1,26),F(12,143)),'radial constants')
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPANDED_POLYNOMIAL_AND_AFFINE_EXPONENT_CHECKS','prior_verdict_sha256':sha(old),'prior_pins_rechecked':40,'energy_coefficients':{str(k):str(v) for k,v in energy.items()},'variables':['1','k','d','j'],'center_t_exponent':center,'exterior_t_exponent':far,'log_tail_integral_constants':moments,'compact_reference_radial_integrals':list(map(str,[I0,Icross,I2])),'bracket_integral':str(15*I0+6*Icross+I2),'files':{str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'evidence/proof_first.json',old,Path(__file__)]},'scope':'Exact arithmetic identities only. Weak-derivative and asymptotic proofs require the stated analytic hypotheses; no actual floating section or spectrum is certified.'}
p=D/'evidence/exact_check.json';check(not p.exists(),'immutable');p.write_text(json.dumps(r,indent=2)+'\n');print(r['utc'],r['status'],sha(p))
