#!/usr/bin/env python3
"""Exact rational verification of a stronger global Q dilation constant."""
from fractions import Fraction as F
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=256
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c
a=F(21,25);b=F(164,125);d=F(1431,1640);e=F(2239,2050000)
poly=add(add(mul([0,16],mul([-a,1],[-a,1])),[b*x for x in mul([-d,1],[-d,1])]),[e])
expected=[F(1),F(9),-F(3196,125),F(16)]
assert poly==expected and b>0 and e>0
coef=F(1049,1549);assert coef-F(2,3)==F(49,4647)
c=arb(4076476460239181)/2251799813685248;q=arb(21)/10
result={'status':'EXACT_RATIONAL_SOS_VERIFIED','polynomial_coefficients_constant_first':[str(x) for x in poly],'k':'1549/500','proved_T_p_squared_coefficient':str(coef),'qc_damping_coefficient':(q*c*arb(coef.numerator)/coef.denominator).str(70),'gain_over_two_thirds_qc':(q*c*arb(49)/4647).str(70)}
out=Path(__file__).resolve().with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
