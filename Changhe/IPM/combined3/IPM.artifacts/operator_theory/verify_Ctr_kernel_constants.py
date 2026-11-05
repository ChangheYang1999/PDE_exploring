#!/usr/bin/env python3
"""Rigorous scalar constants for the preconditioned transport kernel.

This certifies universal kernel factors, not profile-dependent Fourier norms.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
from flint import arb,arb_series,ctx

ctx.prec=256
qf=F(21,10);q=arb(21)/10
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def choose(x,n):
    ans=F(1)
    for j in range(n):ans*=F(x-j,j+1)
    return ans
def falling(j,k):return math.factorial(j)//math.factorial(j-k)
a3=choose(qf,3)-choose(-qf,3)-qf
a4=choose(qf,4)-choose(-qf,4)+qf
assert a3==F(2387,1000)
limits=[F(3),F(9),F(18)]
near=[];h=F(1,100)
for k in range(3):
    s=abs(a3)*falling(3,k)+abs(a4)*falling(4,k)*h
    s+=sum((2*j*j*falling(j,k)*h**(j-3) for j in range(5,101)),F(0))
    s+=2*101**2*falling(101,k)*h**98/(1-2*h)
    s*=F(101,100)  # tau^(3-q)<=tau<=1.01.
    assert s<limits[k];near.append(str(s))
# Far tau>=4: exact analytic bounds stated in the companion proof.
assert 3*F(3,4)**3>1
assert qf/F(3,4)**2<9
assert (qf*(qf-1)+qf*(qf+1)/4**4+2*qf/4**3)/F(3,4)<18
# Entire compact range, using actual Taylor coefficients + Cauchy tails.
lo=F(1,100);checks=0;maxrat=[arb(0),arb(0),arb(0)]
ctx.cap=13
while lo<3:
    hi=min(F(3),lo*F(101,100));center=1+(lo+hi)/2;half=(hi-lo)/2
    c=aa(center);hh=aa(half);rr=arb_series([c,1],prec=13)
    H=rr**q-rr**(-q)-q*(rr-1/rr)
    R=c/4;small=R/2;theta=hh/small
    assert theta<1
    M=(c+R)**q+(c-R)**(-q)+q*((c+R)+1/(c-R))
    dH=H;tball=arb(0,hh.abs_upper());tau=c+tball;delta=tau-1
    for k in range(3):
        val=arb(0)
        for cc in reversed(dH.coeffs()[:13-k]):val=val*tball+cc
        tail=math.factorial(k)*M/small**k*theta**(13-k)/(1-theta)
        ratio=(val+arb(0,tail.abs_upper())).abs_upper()*tau**(3-q)/delta**(3-k)
        assert ratio<aa(limits[k]),(lo,hi,k,str(ratio))
        maxrat[k]=max(maxrat[k],ratio.abs_upper());dH=dH.derivative()
    checks+=1;lo=hi
assert F(27,25)**10>2
assert F(3,2)*F(27,25)<2
assert F(15)*F(27,25)<20
assert F(111,2)*F(27,25)<60
out={'status':'CTR_UNIVERSAL_KERNEL_CONSTANTS_PASS','q':'21/10','precision_bits':ctx.prec,
     'scalar_limits_H_Hprime_Hsecond':['3','9','18'],
     'compact_tau_interval':['101/100','4'],'compact_interval_count':checks,
     'compact_ratio_max_arb':[str(x) for x in maxrat],
     'near_tau_rational_uppers':near,
     'kernel_F_factor':'2','kernel_first_derivative_factor':'20','kernel_mixed_derivative_factor':'60',
     'profile_Fourier_moments':'NOT evaluated by this certificate',
     'Ctr_operator_norm':'NOT certified by this calculation',
     'stationary_existence':'NOT CLAIMED'}
dest=Path(__file__).resolve().parent/'Ctr_kernel_constants_result.json';dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='near_tau_rational_uppers'},indent=2))
