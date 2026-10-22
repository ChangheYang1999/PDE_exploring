"""Rational transcendental enclosures for packet187. No floating arithmetic."""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt
BITS=384
NLOG=144
NEXP=80

def down(x):
    h=1<<BITS;return Q(x.numerator*h//x.denominator,h)
def up(x):return -down(-x)
def outward(x):return down(x[0]),up(x[1])
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mulq(a,c):return (a[0]*c,a[1]*c)if c>=0 else(a[1]*c,a[0]*c)
def logs(q):
    assert 0<=q<=Q(1,3)
    q2=q*q;p=q;s=Q(0)
    for j in range(NLOG):s+=2*p/(2*j+1);p*=q2
    return outward((s,s+2*p/((2*NLOG+1)*(1-q2))))
LOG2=logs(Q(1,3))
@lru_cache(None)
def logv(v):
    assert 0<v<=1
    w=v;h=0
    while w<1:w*=2;h+=1
    return outward(sub(logs((w-1)/(w+1)),mulq(LOG2,h)))
def exppos(x):
    assert x>=0
    y=x;h=0
    while y>Q(1,2):y/=2;h+=1
    term=s=Q(1)
    for j in range(1,NEXP+1):term*=y/j;s+=term
    first=term*y/(NEXP+1);a=outward((s,s+first/(1-y/(NEXP+2))))
    for _ in range(h):a=outward((a[0]*a[0],a[1]*a[1]))
    return a
@lru_cache(None)
def power(v,alpha):
    assert 0<=v<=1 and 0<=alpha<1
    if alpha==0:return Q(1),Q(1)
    if v in (0,1):return v,v
    x=mulq(logv(v),-alpha);x=(max(Q(0),x[0]),max(Q(0),x[1]))
    aa=exppos(x[0]);bb=exppos(x[1]);return outward((1/bb[1],1/aa[0]))
def square_root(q):
    assert q>=0
    if q==0:return Q(0),Q(0)
    h=1<<120;n=isqrt(q.numerator*h*h//q.denominator);return Q(n,h),Q(n+1,h)
def serialize(a):return list(map(str,a))
