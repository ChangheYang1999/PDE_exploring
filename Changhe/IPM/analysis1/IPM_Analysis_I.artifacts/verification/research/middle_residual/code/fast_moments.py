"""Exact exponential-moment recurrence evaluated with outward Arb arithmetic."""
from fractions import Fraction as F
from math import comb
from flint import arb

def aa(x):x=F(x);return arb(x.numerator)/x.denominator

def phi_values(z_exact,degree=7):
 z_exact=F(z_exact)
 if z_exact==0:return [aa(F(1,j+1)) for j in range(degree+1)]
 z=aa(z_exact);assert not z.contains(0);ez=z.exp();v=[z.expm1()/z]
 for j in range(1,degree+1):v.append((ez-j*v[-1])/z)
 assert all(q>0 and q.rel_accuracy_bits()>120 for q in v),(str(z_exact),min(q.rel_accuracy_bits() for q in v))
 return v

def shift_poly(p,delta):
 d=aa(delta);degree=len(p)-1
 return [sum((p[l]*comb(l,j)*d**(l-j) for l in range(j,degree+1)),arb(0)) for j in range(degree+1)]

def integral(p,offset,h,rate,reverse=False,cache=None):
 """Integral_0^h exp(rate*v) p(offset +/- v) dv; p about original span midpoint."""
 h,offset,rate=F(h),F(offset),F(rate);assert h>=0
 if h==0:return arb(0)
 key=(rate*h,len(p)-1)
 if cache is not None and key in cache:ph=cache[key]
 else:
  ph=phi_values(rate*h,len(p)-1)
  if cache is not None:cache[key]=ph
 # Translate and scale before summing the exact moment identity.
 shifted=shift_poly(p,offset);hb=aa(h)
 return hb*sum((v*hb**j*(-1 if reverse and j%2 else 1)*ph[j] for j,v in enumerate(shifted)),arb(0))
