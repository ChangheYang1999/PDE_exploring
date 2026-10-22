"""Exact proof constants, native weights/powers, and an underflow counterexample."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import numpy as np
from flint import arb,ctx
from mpmath import iv
D=Path(__file__).resolve().parents[1];u=F(1,2**53);eta=F(1,2**1074);ctx.prec=256;iv.dps=100
checks=0
for n in range(1,4097):
 A=F.from_float(float(np.nextafter(1+(n+2)*float(u),np.inf)))
 assert 1+(n+2)*u<=A<=1+(n+5)*u
 assert (1+(n+2)*u)*(1-(n+1)*u)>=1
 assert A*n/(1-(n-1)*u)<n+1
 assert (1+(n+1)*u)*(1-n*u)>=1
 checks+=4
geo=json.loads((D/'evidence/geometry_arb.json').read_text());w=geo['w_up'];pw=[1.0]+[float(np.nextafter(w**j*(1+2*j*float(u)),np.inf)) for j in range(1,19)]
weights=0;min_product=F(1)
for c in geo['cells']:
 h=c['h_up'];ph=[1.0]+[float(np.nextafter(h**j*(1+2*j*float(u)),np.inf)) for j in range(1,27)]
 assert all(0<x<=1 for x in pw+ph)
 for i in range(25):
  for j in range(17):
   exact=F.from_float(ph[i])*F.from_float(pw[j]);assert exact>=F(2)**-1022
   assert F.from_float(float(ph[i]*pw[j]))>=exact*(1-u);weights+=1;min_product=min(min_product,exact)
n=523;freq=2*np.arange(n,dtype=float)+1;powers=0
for j in range(5):
 for N,x in enumerate(freq**j):assert F.from_float(float(x))==(2*N+1)**j and (2*N+1)**j<2**53;powers+=1
# Reproduce exactly the frozen r2 expression, not an invented sum algorithm.
x=np.full(n,float.fromhex('0x0.0000000000001p-1022')); y=np.full(n,0.5)
products=x*y;s=float(products.sum());fac=float(np.nextafter(1+(n+1)*float(u),np.inf));r=float(np.nextafter(s*fac,np.inf))
assert np.all(products==0) and F.from_float(r)==eta
exact=n*eta/2;assert exact>F.from_float(r)
# Separate interval engines recover the exact sum ratio, above the returned1eta.
a=arb(n)/2;v=iv.mpf(n)/2;assert a.lower()>1 and v.a>1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_BiTM_REMAINDER_LEMMA_AND_GENERIC_r2_COUNTEREXAMPLE','exact_constant_checks':checks,'normal_power_products':weights,'minimum_exact_weight_product':str(min_product),'exact_native_integer_powers':powers,'r2_counterexample':{'n':n,'first_factor':'eta','second_factor':'1/2','returned_over_eta':'1','exact_over_eta':str(F(n,2)),'arb_exact_over_eta':str(a),'iv_exact_over_eta':str(v)},'scope':'BiTM scalar arithmetic and weights conditional on input validity and scalar rounding. Actual r2 values, library trees, radial/TM inputs and physical forcing remain OPEN.'}
(D/'evidence/positive_sums.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks,weights,powers)
