#!/usr/bin/env python3
"""Fresh continuum certificate for H_2.1(t)<=1.06(t-1)^2.1.

No inherited script is executed or modified. Monotonicity supplies a
rigorous containing upper on each interval; endpoints are analytic.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=256
q=arb(21)/10;target=arb(53)/50
def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)
def H(t):return t**q-t**(-q)-q*(t-1/t)
assert F(27,6)*F(1,10)<F(53,50) # near t−1<=.01: delta^.9<=delta^.5<=.1.
qr=F(21,10)
assert qr*((qr-1)*(qr-2)+(qr+1)*(qr+2))<27
assert F(64,63)**3<F(53,50)
subdiv=256;count=0;maximum=arb(0);worst=None
for j in range(13):
    base=F(2)**j/100
    for k in range(subdiv):
        lo=base*(1+F(k,subdiv));hi=min(base*(1+F(k+1,subdiv)),F(63))
        if lo>=63:break
        # H is increasing for t>=1; proof is the exact factorization
        # H'=q*t^(-q-1)*(t^(q-1)-1)*(t^(q+1)-1).
        bound=H(1+aa(hi))/aa(lo)**q
        assert bound.is_finite() and bound<target,(j,k,str(bound))
        if bound>maximum:maximum=bound;worst=[str(lo),str(hi)]
        count+=1
out={'status':'NONLINEAR_CORE_SCALAR_CONTINUUM_PASS','q':'21/10','target':'53/50','precision_bits':ctx.prec,
     'near_endpoint':'1<=t<=101/100: H triple derivative<=27, H<=9/2(t-1)^3 and normalized bound<=9/20',
     'compact_domain':['101/100','64'],'intervals':count,'compact_largest_upper_arb':str(maximum),'worst_delta_interval':worst,
     'tail_endpoint':'t>=64: H< t^q and (t/(t-1))^q<=(64/63)^3<53/50',
     'method':'monotonic H endpoint divided by exact lower delta^q; complete closed interval cover',
     'stationary_existence':'NOT CLAIMED'}
dest=Path(__file__).resolve().parent/'nonlinear_core_scalar_result.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
