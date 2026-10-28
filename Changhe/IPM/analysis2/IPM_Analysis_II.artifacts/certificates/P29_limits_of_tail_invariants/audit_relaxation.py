"""Independent dilation constants, exact polar derivative identities and upper bound."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from itertools import product
from math import comb
import json,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1];start=time.monotonic()
def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q):return clean({k:p.get(k,Q(0))+q.get(k,Q(0)) for k in p.keys()|q.keys()})
def scale(p,a):return clean({k:v*a for k,v in p.items()})
def mul(p,q):
 out={}
 for i,v in p.items():
  for j,w in q.items():out[i+j]=out.get(i+j,Q(0))+v*w
 return clean(out)
def der(p):return {k-1:k*v for k,v in p.items() if k}
def transform(p,k):
 # u^k P((1-u)/u)
 out={}
 for i,v in p.items():
  for j in range(i+1):out[k-i+j]=out.get(k-i+j,Q(0))+v*comb(i,j)*(-1)**j
 return clean(out)
identities=0
for m in [1,5,39,139]:
 for b in [Q(2,3),Q(5,4)]:
  alpha=Q(2,5);beta=Q(m,2)+4;eta=alpha+beta+b
  for signs in product([-1,1],repeat=4):
   pr={0:Q(1)};pu={0:Q(1)};n=m
   for k,sgn in enumerate(signs):
    # Direct differentiation in r, with z=r^2 and a separate denominator.
    d0=2*beta-k-sgn*n
    pr=add(mul({0:d0,1:d0-2*(eta+k)},pr),mul({1:Q(2),2:Q(2)},der(pr)))
    # Independently differentiate the u prefactor and q=u^b.
    ak=alpha+b+Q(k,2);bk=beta-Q(k,2)
    pu=add(mul({0:-2*ak-sgn*n,1:2*(ak+bk)},pu),mul({1:Q(-2),2:Q(2)},der(pu)))
    assert pu==transform(pr,k+1),(m,b,signs,k)
    n+=sgn;identities+=1
assert identities==512
p=HERE/'relaxation_bound.json';first=json.loads(p.read_text())
for rel,h in first['dependencies'].items():assert sha256((BASE/rel).read_bytes()).hexdigest()==h,rel
assert first['code_sha256']==sha256((HERE/'relaxation_bound.py').read_bytes()).hexdigest()
annp=BASE/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json';ann=json.loads(annp.read_text());es={int(m):Q(v) for m,v in ann['leading_sine_coefficients'].items()}
c=Q(4076476460239181,2251799813685248);delta=1-1/c;a0=7*delta/2-2;mu=Q(11,10)
Bessel=(1+4*arb(mu))*(89+20*arb.pi());assert Bessel<821
rows=[];S=arb(0)
for row in first['rows']:
 m=row['m'];M=(m+1)//2+4;degree=154-M
 A=sorted({ell*delta/2+k-2 for ell in range(1,13) for k in range(degree+1) if ell*delta/2+k-2>=a0})
 assert len(A)==row['dimension'] and M==row['M'] and degree==row['K']
 logD=-arb(2*(a0+mu)+1).log()/2
 for x in A[1:]:logD+=arb(x-a0).log()-arb(x+a0+2*mu+1).log()
 D=logD.exp();Z=[x+mu for x in A]
 total=sum((2*z+1 for z in Z),Q(0));sq=sum(((2*z+1)**2 for z in Z),Q(0))
 C=arb(sum((z*z for z in Z),Q(0))+(total*total-sq)/2).sqrt()
 assert D.overlaps(arb(row['D'])) and C.overlaps(arb(row['C']))
 A1=4*C+2*m+arb(Q(48,5));A2=A1*(A1+6);A3=A2*(A1+12);A4=A3*(A1+18)
 radius=(arb(2)**31)**(2*arb(mu))
 top=arb(4)**arb(Q(2,5))*(2*A2+4*arb(2).sqrt()*A4)
 middle=2**11*(arb(2).sqrt()*A1+4*A3)
 low=arb(2)**arb(Q(53,2))*radius*(1+2*arb(2).sqrt()*A2)
 U=821*arb.pi().sqrt()*arb(abs(es[m]))*D*(top+middle+low)
 assert U.overlaps(arb(row['norm_upper']))
 S+=U;rows.append({'m':m,'agrees':True})
assert S.overlaps(arb(first['N_upper'])) and S<arb('3.460197e-13') and S*2**35<arb('0.01189')<1
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED independent constants and exact derivative recurrence; lead analytical review CORRECT 07:41Z','precision_bits':ctx.prec,'exact_radial_derivative_identities':identities,'norm_upper':S.str(75),'strict_rounded_upper':'3.460197e-13','ratio_to_eta_upper':'0.01189','Bessel_negative_bound':Bessel.str(50),'all_70_mode_bounds_agree':True,'dependencies':{str(q.relative_to(BASE)):sha256(q.read_bytes()).hexdigest() for q in [p,HERE/'relaxation_bound.py',HERE.parent/'PROOF.md',annp,BASE/'26_uniform_family_gap/verification/audit_algebra.json']},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
(HERE/'audit_relaxation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
