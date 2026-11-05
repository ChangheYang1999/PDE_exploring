#!/usr/bin/env python3
"""Exact rational verification of the Picone 49/10 coefficient."""
from fractions import Fraction as F
from pathlib import Path
import json,math
from flint import arb,ctx
ctx.prec=256
P=[2640,510,21120,-46096,17152,5024]
def shift(poly,a):
    out=[F(0)]*len(poly)
    for n,c in enumerate(poly):
        for j in range(n+1):out[j]+=c*math.comb(n,j)*a**(n-j)
    return out
up=shift(P,F(1));assert up==[350,-1810,35984,72752,42272,5024]
vm=[x*(-1)**j for j,x in enumerate(up)]
assert vm==[350,1810,35984,-72752,42272,-5024]
qmin=F(350)-F(1810**2,4*35984);assert qmin==F(11775375,35984)>0
bmin=F(35984)-F(72752**2,4*37248);assert bmin==F(267479,582)>0
c=arb(4076476460239181)/2251799813685248;q=arb(21)/10
out={'status':'EXACT_RATIONAL_PICONE_COEFFICIENT_VERIFIED','polynomial_constant_first':P,'positive_quadratic_minimum_r_ge_1':str(qmin),'positive_quadratic_minimum_r_le_1':str(bmin),'H1_over_ell_squared_coefficient':'49/10','proved_T_over_p_squared_coefficient':'39/49','qc_damping_coefficient':(q*c*39/49).str(70),'warning':'Auxiliary damping inequality only, not complete IPM coercivity or existence.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
