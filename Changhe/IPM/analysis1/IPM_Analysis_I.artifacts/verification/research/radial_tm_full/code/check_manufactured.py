"""Finite diagnostics for exact weights, endpoint directions and rational exp."""
from common import *
from fractions import Fraction as F
from math import factorial,comb
from collections import Counter
import engine_arb as A
import engine_iv as B
import engine_particular as C
from check_full import floor_endpoint_units,ceil_endpoint_units

def main():
 counts=Counter();A.setup();B.setup()
 for n in range(1,262):
  aa,bb=A.weights(n),B.weights(n)
  for j in range(21):
   for fam in range(2):
    for x,y in zip(aa[j][fam],bb[j][fam]):assert x==y;counts['integer_weight_equalities']+=1
  if n in (1,2,3,64,261):
   cc=C.weights(n)
   for j in range(21):
    for fam in range(2):
     for k in range(8):assert F(aa[j][fam][k+2],2*factorial(j))==cc[j][fam][k];counts['particular_weight_equalities']+=1
 for m in (-(1<<1400)-17,-9,-1,0,1,9,(1<<1400)+17):
  for radius in (0,1,31):
   A.setup();B.setup()
   for bounds in (arb_endpoints(A.box(m,radius)),iv_endpoints(B.endpoint_interval(m-radius,m+radius))):
    assert compare_to_units(bounds[0],m-radius)<=0 and compare_to_units(bounds[1],m+radius)>=0;counts['directed_conversion_contains']+=1
 for m in (-33,-1,0,1,33):
  for e in (-1500,-1075,-1074,-1073,0,17):
   q=F(m)*F(2)**e;scaled=q*(1<<1074)
   lo=scaled.numerator//scaled.denominator;hi=-((-scaled.numerator)//scaled.denominator)
   assert floor_endpoint_units((m,e))==lo and ceil_endpoint_units((m,e))==hi
   for target in (lo-1,lo,hi,hi+1):assert compare_to_units((m,e),target)==(scaled>target)-(scaled<target);counts['signed_endpoint_directions']+=1
 for x in (F(0),F(1,10**8),F(1,3),F(99,100),F(-5,2),F(14)):
  A.setup();B.setup();a=arb_endpoints(rational_arb(x).exp());b=iv_endpoints(B.exponential_rational(x))
  assert compare_dyadics(a[0],b[1])<=0 and compare_dyadics(b[0],a[1])<=0;counts['rational_exp_vs_arb_overlap']+=1
 for width in (F(1,1000000),F(1,1000)):
  for k in range(8):
   poly=[F(int(j==k)) for j in range(8)]
   for d in range(21):
    by_polynomial=sum((v*width**j for j,v in enumerate(poly)),F())
    by_leibniz=sum((F(comb(d,v)*(1<<(d-v))*factorial(k),factorial(k-v))*width**(k-v) for v in range(min(d,k)+1)),F())
    assert by_polynomial==by_leibniz;counts['positive_derivative_weights']+=1
    poly=[2*v+(j+1)*poly[j+1] if j<7 else 2*v for j,v in enumerate(poly)]
 # Exact homogeneous family q_plus=exp(4u), q_minus=0, E=1.
 # Each interval engine independently rejects zero coefficient/radius and zero remainder budgets.
 for engine,ends in ((A,arb_endpoints),(B,iv_endpoints)):
  engine.setup();coefs=engine.coefficients(3,SCALE,0,0,0,SCALE,0,[0]*8,[0]*8)
  assert inside(ends(coefs[0][0]),SCALE//2,SCALE//2)
  assert not inside(ends(coefs[0][0]),0,0);counts['deflated_coefficient_rejected']+=1
  # An inflated containing interval is valid. Provenance rejects changed candidates separately.
  assert inside(ends(coefs[0][0]),0,SCALE);counts['inflated_containing_interval_accepted']+=1
  rems=engine.remainder(3,F(1,1000),SCALE,0,0,0,SCALE,0,[0]*8,[0]*8,coefs)
  for rem in rems:
   assert not positive_upper_within(ends(rem),0);counts['zero_remainder_budget_rejected']+=1
 for engine,ends in ((A,arb_endpoints),(B,iv_endpoints)):
  engine.setup();small=engine.box(1,0) if engine is A else engine.endpoint_interval(1,1)
  assert positive_upper_within(ends(small),1) and not positive_upper_within(ends(small),0)
  assert inside(ends(small),1,1);counts['subnormal_budget_direction']+=1
 result={'utc':utc(),'status':'PASS_FINITE_MANUFACTURED_DIAGNOSTICS','counts':dict(counts),'source_sha256':sha(__file__),'scope':'Finite implementation diagnostics, not whole input coverage and not a substitute for the analytic proof.'}
 (OUT/'manufactured_checks.json').write_text(canonical(result)+'\n');print(canonical(result))
if __name__=='__main__':main()
