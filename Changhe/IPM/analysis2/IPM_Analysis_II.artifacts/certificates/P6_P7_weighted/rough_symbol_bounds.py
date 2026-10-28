"""Exact high derivative symbol bounds for the original checkpoint."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb,factorial
from datetime import datetime,timezone
import json
HERE=Path(__file__).resolve().parent
s=json.loads((HERE.parents[1]/'source_audit/state131_exact.json').read_text())
gamma=1/Q(s['exact_parameters']['cl']);delta=1-gamma

def fall(t,n):
 ans=Q(1)
 for i in range(n):ans*=t-i
 return ans

def one(k,t,d):
 ans=Q(0)
 for ell in range(min(d,2*k)+1):
  n=d-ell
  ans+=comb(d,ell)*fall(Q(2*k),ell)*sum((Q(factorial(n)*2**(n-2*b),factorial(n-2*b)*factorial(b))*abs(fall(t,n-b)) for b in range(n//2+1)),Q(0))
 return ans
sums={d:Q(0) for d in range(3,13)}
for (j,m,k),a in zip(s['canonical_order'],s['canonical_coefficients']):
 p=(3+gamma-j*delta)/2
 for d in sums:sums[d]+=abs(Q(a))*one(k,p-k,d)
# 2*2^j is an integer upper bound for both rho and vector-U Frobenius tensors.
bounds={j:2**(j+1)*sums[j+3] for j in range(10)}
M=max(bounds.values());pow2=1
while Q(pow2)<M:pow2*=2
# Smoothstep P with P'=t^6(1-t)^6/B(7,7), exact coefficients.
norm=Q(factorial(13),factorial(6)**2)
P={7+k:norm*Q((-1)**k*comb(6,k),7+k) for k in range(7)}
# q=(4-r^2)/3 on 1<=r<=2. |Dq|<=4/3, |D2q|<=2/3.
cut={}
for d in range(7):
 total=Q(0)
 for b in range(d//2+1):
  a=d-2*b;n=a+b
  pd=sum(abs(v)*fall(Q(k),n) for k,v in P.items() if k>=n)
  total+=Q(factorial(d),factorial(a)*factorial(b)*2**b)*(Q(4,3)**a)*(Q(2,3)**b)*pd
 cut[d]=total
assert all(v<2**80 for v in cut.values())
assert gamma<Q(3,5) and delta>Q(2,5)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':s['canonical_serialization_sha256'],'scope':'For j=0..9, <r>^(j-gamma) times the full ordered derivative tensor of rho or U is at most the listed exact bound.','gamma':str(gamma),'tensor_bounds':{str(k):str(v) for k,v in bounds.items()},'uniform_power_two_exponent':pow2.bit_length()-1,'uniform_bound':str(pow2),'cutoff_coefficients':{str(k):str(v) for k,v in P.items()},'cutoff_derivative_bounds':{str(k):str(v) for k,v in cut.items()},'cutoff_bound':'2^80'}
(HERE/'rough_symbol_bounds.json').write_text(json.dumps(out,indent=2)+'\n');print('Uniform symbol bound: 2^'+str(pow2.bit_length()-1));print('Cutoff derivatives: all <2^80')
