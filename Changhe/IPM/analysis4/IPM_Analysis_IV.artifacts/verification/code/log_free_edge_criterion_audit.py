"""Exact grid check of constants in the general rational edge criterion."""
from fractions import Fraction as Q
from math import gcd
from datetime import datetime,timezone
from pathlib import Path
from hashlib import sha256
import time,json

def main():
 start=time.monotonic();count=0;cases=0
 for b in range(2,13):
  for a in range(1,b):
   if gcd(a,b)!=1:continue
   delta=Q(a,b);c=1/(1-delta);d=Q(gcd(a,2),b);CP=2/d
   assert d<=delta and c*d/2 <= (c-1)/2
   for K in range(1,6):
    if K*delta>=4:continue
    for n in range(2*K+1,35):
     inv=1/((c-1)*(n-Q(3,2)))
     assert inv>=1/((c-1)*(n-1)-c*d/2)>0
     for i in range(1,K+1):
      j=n-i;Pi=2-i*delta;pi=1-i*delta;Pj=2-j*delta;pj=1-j*delta
      assert j>=2 and abs(pj)<=j and abs(Pj)<=(2-delta)*j
      for L in (1,3,19):
       B=L+1
       exact_Q=(abs(Pi)*(B*j-1)+B*i*(abs(pj)+d/2))*inv
       exact_H=((abs(Pj)+d/2)*(B*i-1)+B*j*abs(pi))*CP*inv
       bound_Q=Q(4,3)*B/(c-1)*(abs(Pi)+i*(1+d/4))
       bound_H=Q(4,3)*B/(c-1)*CP*((2-delta+d/4)*i+abs(pi))
       assert exact_Q<=bound_Q and exact_H<=bound_H
       count+=2;cases+=1
 root=Path('research/107_log_free_edge_criterion');src=Path('code/log_free_edge_criterion_audit.py').read_bytes();(root/'sources/log_free_edge_criterion_audit.py.txt').write_bytes(src)
 result={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':sha256(src).hexdigest(),'tested_parameters':'all reduced a/b with2<=b<=12,1<=a<b','edge_widths':'1<=K<=5 and K delta<4','orders':'2K+1<=n<=34','leading_top_frequencies':[1,3,19],'cases':cases,'paired_coefficient_inequalities':count,'all_passed':True,'scope':'Finite rational checks of elementary majorant constants; no generated high-order data and no proof of the unrestricted recurrence.','actual_elapsed_s':time.monotonic()-start}
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
