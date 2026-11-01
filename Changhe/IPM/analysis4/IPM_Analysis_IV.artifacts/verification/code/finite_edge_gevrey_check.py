"""Exact finite checks of the inequalities in topic111, not a proof by testing."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,gcd
from datetime import datetime,timezone
from hashlib import sha256
import json,time
start=time.monotonic();count_product=count_tail=count_gevery=count_bound=0
for n in range(1,81):
 for l in range(n+1):
  for q in range(n-l+1):
   assert comb(q+l,l)<=n**l
   count_product+=1
for b in range(2,16):
 for a in range(1,b):
  if gcd(a,b)!=1:continue
  delta=Q(a,b);c=1/(1-delta);star=Q(gcd(a,2),b);r=star/2
  for K in [1,3,10,30]:
   for n in range(2*K+1,2*K+10):
    for i in range(1,K+1):
     j=n-i;Pi=2-i*delta;pi=1-i*delta;Pj=2-j*delta;pj=1-j*delta
     lowg=(abs(Pi)+r)*j+i*(abs(pj)+r)
     lowf=(abs(Pj)+r)*i+j*(abs(pi)+r)
     bg=(abs(Pi)+r+i*(1+r))*j
     bf=(i*(2-delta+r)+abs(pi)+r)*j
     assert lowg<=bg and lowf<=bf
     assert Q(j,1)/(n-Q(3,2))<=Q(4,3)
     count_tail+=3
for q0 in range(3,13):
 for K in range(1,61):
  ds={i:max(0,i//q0-1) for i in range(1,K+1)}
  sigma=max(Q(d,i) for i,d in ds.items())
  m=K//q0
  asserted=Q(0) if K<2*q0 else Q(m-1,q0*m)
  assert sigma==asserted and sigma<Q(1,q0)
  count_bound+=1
  for n in range(2*K+1,2*K+5):
   for i,d in ds.items():
    fall=factorial(n)//factorial(n-i)
    # Raise (12) to the positive denominator of sigma.
    p,q=sigma.numerator,sigma.denominator
    assert n**(d*q)<=2**(p*i)*fall**p
    count_gevery+=1
root=Path('research/111_finite_edge_gevrey');raw=Path(__file__).read_bytes()
(root/'sources/finite_edge_gevrey_check.py.txt').write_bytes(raw)
res=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source_sha256=sha256(raw).hexdigest(),product_inequalities=count_product,tail_inequalities=count_tail,gevrey_inequalities=count_gevery,explicit_order_checks=count_bound,all_passed=True,actual_elapsed_s=time.monotonic()-start,scope='Finite exact rational/integer checks; all-order proof is in PROOF.md and awaits independent review.')
(root/'verification/checks.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
