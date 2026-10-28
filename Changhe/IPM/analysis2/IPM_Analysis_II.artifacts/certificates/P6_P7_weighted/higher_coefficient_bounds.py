"""Exact global derivative bounds from generator product rules."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb,factorial
from datetime import datetime,timezone
import json
HERE=Path(__file__).resolve().parent
s=json.loads((HERE.parents[1]/'source_audit'/'state131_exact.json').read_text())
gamma=1/Q(s['exact_parameters']['cl']);delta=1-gamma

def fall(t,n):
 z=Q(1)
 for i in range(n):z*=t-i
 return z

def bound(k,t,d):
 ans=Q(0)
 for ell in range(min(d,2*k)+1):
  n=d-ell
  poly=fall(Q(2*k),ell)
  rad=Q(0)
  for b in range(n//2+1):
   a=n-2*b
   rad+=Q(factorial(n)*2**a,factorial(a)*factorial(b))*abs(fall(t,a+b))
  ans+=comb(d,ell)*poly*rad
 return ans

sums={d:Q(0) for d in [5,6,7]}
for (j,m,k),a in zip(s['canonical_order'],s['canonical_coefficients']):
 p=(3+gamma-j*delta)/2
 for d in sums:sums[d]+=abs(Q(a))*bound(k,p-k,d)
# D4rho uses two seventh potential derivatives per component,16 components.
B4=8*sums[7]
power=1
while Q(power)<B4:power*=2
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_sha256':s['canonical_serialization_sha256'],'method':'Exact Cartesian product rule, polynomial falling factorial bound and <r> homogeneity. No sampling.','potential_component_bounds':{str(k):str(v) for k,v in sums.items()},'D4rho_weight_r2_bound_exact':str(B4),'D4rho_weight_r2_power_two_bound':str(power),'power_two_exponent':power.bit_length()-1}
(HERE/'higher_coefficient_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
print('D4rho weighted by <r>^2 bounded by 2^'+str(power.bit_length()-1))
