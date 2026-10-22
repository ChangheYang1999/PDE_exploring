"""Exact Bernstein operations for far-polynomial certificates, integer split path."""
from flint import fmpq, fmpq_poly as Poly, fmpz_poly as ZPoly
from fractions import Fraction as F
from math import factorial,gcd,comb
from functools import lru_cache
Q=lambda v:fmpq(str(v))
@lru_cache(None)
def facs(n):return [factorial(k) for k in range(n+1)]
def pack(p,n=None):
 p=Poly(p);d=int(p.denom());nn=p.numer();n=max(0,p.degree()) if n is None else n
 return [int(nn[k]) for k in range(n+1)],d
def reduce(b,d):
 g=d
 for z in b:g=gcd(g,z)
 return ([v//g for v in b],d//g)
def root(p):
 p=Poly(p);n=max(0,p.degree());fs=facs(n)
 q=Poly([p[k]*fs[n-k] for k in range(n+1)])*Poly([fmpq(1,fs[k]) for k in range(n+1)])
 return pack(Poly([q[k]*fmpq(fs[k],fs[n]) for k in range(n+1)]),n)
def split(b,d):
 n=len(b)-1;fs=facs(n);fac=fs[n];divisor=fac*fac
 coeff=[fac//fs[k] for k in range(n+1)];v=ZPoly(coeff)
 def trans(bb):
  cc=ZPoly([bb[k]*coeff[k] for k in range(n+1)])*v;out=[]
  for k in range(n+1):
   num=int(cc[k])*fs[k];q,r=divmod(num,divisor)
   if r:raise ArithmeticError('noninteger binomial transform')
   out.append(q)
  return out
 t,tr=trans(b),trans(list(reversed(b)))
 return reduce([t[k]<<(n-k) for k in range(n+1)],d<<n),reduce([tr[n-k]<<k for k in range(n+1)],d<<n)
def bounds(b,d):return F(min(b),d),F(max(b),d)
def c12_interval(alpha,bits=256):
 alpha=F(alpha);n=max(100,int(alpha)+2);lo=sum((alpha**k/factorial(k) for k in range(n+1)),F(0));hi=lo+alpha**(n+1)/factorial(n+1)/(1-alpha/F(n+2))
 l=((1-1/lo)/alpha)**2;u=((1-1/hi)/alpha)**2;D=2**bits
 return (F((l.numerator*D)//l.denominator,D),F(-((-u.numerator*D)//u.denominator),D)),{'terms_through':n,'exp_lo':str(lo),'exp_hi':str(hi),'dyadic_bits':bits}
def absolute(iv):
 l,h=iv;return (F(0) if l<=0<=h else min(abs(l),abs(h)),max(abs(l),abs(h)))
def leaf(state,ci,a):
 bb={k:bounds(*v) for k,v in state.items()};al=bb['A'][0]
 eps=(ci[1]-ci[0])/2;err=eps*absolute(bb['N123'])[1];c=(bb['Cmid'][0]-err,bb['Cmid'][1]+err)
 den=ci[0]*sum((absolute(bb[f'N{j}'])[0] for j in range(1,4)),F(0))+abs(a)*absolute(bb['N4'])[0]
 ub=None if den<=0 else min(F(1),absolute(c)[1]/den)
 return {'A_lower':al,'denominator_lower':den,'ratio_upper':ub}
