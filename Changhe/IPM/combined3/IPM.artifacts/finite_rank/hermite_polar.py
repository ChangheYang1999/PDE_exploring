#!/usr/bin/env python3
"""Exact polar harmonic formulas for Hermite phi,R1phi,R2phi,U1phi,U2phi.

Coefficients are exact Gaussian rationals. Arb evaluates radial Kummer functions.
Uses unitary Fourier transform in dimension two, hence inverse angular factor i^|l|.
"""
from fractions import Fraction as Q
from functools import lru_cache
import math
from flint import arb,ctx
try:from .hermite_gram import hermite,mul,arbq
except ImportError:from hermite_gram import hermite,mul,arbq


def zadd(a,b):return a[0]+b[0],a[1]+b[1]
def zmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def zscale(a,c):return a[0]*c,a[1]*c
def ipow(n):return [(Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1))][n%4]


def angular_poly(i,j):
    out={}
    phase=ipow(-j)
    for s in range(i+1):
        for t in range(j+1):
            l=i+j-2*(s+t)
            c=zscale(phase,Q(math.comb(i,s)*math.comb(j,t)*(-1)**t,2**(i+j)))
            out[l]=zadd(out.get(l,(Q(0),Q(0))),c)
    return {l:c for l,c in out.items() if c!=(0,0)}


MULT={
 'phi':{0:(Q(1),Q(0))},
 'r1':{1:(Q(0),Q(1,2)),-1:(Q(0),Q(1,2))},
 'r2':{1:(Q(1,2),Q(0)),-1:(Q(-1,2),Q(0))},
 'u1':{2:(Q(0),Q(-1,4)),-2:(Q(0),Q(1,4))},
 'u2':{0:(Q(-1,2),Q(0)),2:(Q(-1,4),Q(0)),-2:(Q(-1,4),Q(0))},
}


class HermitePolar:
 def __init__(self,m,n,alpha=Q(1)):
    self.m,self.n,self.alpha=m,n,Q(alpha)
    self.norm=1/(arbq(self.alpha)*arb.pi().sqrt()*arb(2**(m+n)*math.factorial(m)*math.factorial(n)).sqrt())
    pp=mul(hermite(m,0,self.alpha),hermite(n,1,self.alpha))
    self.terms={}
    for op,mm in MULT.items():
        out={}
        for (i,j),v in pp.items():
            p=i+j
            for l,c in angular_poly(i,j).items():
                for shift,d in mm.items():
                    ll=l+shift
                    cc=zscale(zmul(zmul(c,d),ipow(-(m+n)+abs(ll))),v)
                    out[p,ll]=zadd(out.get((p,ll),(Q(0),Q(0))),cc)
        self.terms[op]={key:c for key,c in out.items() if c!=(0,0)}
 def modes(self,r,ops=None):
    r=arb(r);beta=1/(2*arbq(self.alpha)**2);x=-r*r/(4*beta)
    @lru_cache(None)
    def radial(p,l):
        A=(arb(p+l)+2)/2
        return r**l*A.gamma()/(2**(l+1)*beta**A*arb(l+1).gamma())*x.hypgeom_1f1(A,l+1)
    ans={}
    for op,terms in self.terms.items():
      if ops is not None and op not in ops:continue
      out={}
      for (p,l),cc in terms.items():
        old=out.get(l,(arb(0),arb(0)));v=self.norm*radial(p,abs(l))
        out[l]=(old[0]+arbq(cc[0])*v,old[1]+arbq(cc[1])*v)
      trig={}
      if 0 in out:
        assert out[0][1].contains(0)
        trig['c',0]=out[0][0]
      for l,c in out.items():
        if l>0:
          neg=out.get(-l,(arb(0),arb(0)))
          assert (neg[0]-c[0]).contains(0) and (neg[1]+c[1]).contains(0)
          if not c[0].is_zero():trig['c',l]=2*c[0]
          if not c[1].is_zero():trig['s',l]=-2*c[1]
      ans[op]=trig
    return ans


if __name__=='__main__':
 ctx.prec=256
 for mn in [(0,1),(2,1),(0,3)]:
  h=HermitePolar(*mn)
  for r in ['0','0.1','1','5','20']:
   ans=h.modes(r)
   print(mn,r,{op:{str(k):v.str(12) for k,v in vv.items()} for op,vv in ans.items()})
