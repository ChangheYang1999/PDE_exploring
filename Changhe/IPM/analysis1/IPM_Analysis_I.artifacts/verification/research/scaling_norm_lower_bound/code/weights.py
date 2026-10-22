"""Directed scalar weights: Arb direct powers and iv logarithmic expression."""
from fractions import Fraction as F
from flint import arb, fmpq, ctx
from mpmath import iv
ctx.prec=512;iv.dps=220

def aq(s):
    q=F(s);return arb(fmpq(q.numerator,q.denominator))

def iq(s):
    q=F(s);return iv.mpf(q.numerator)/iv.mpf(q.denominator)

def apair(z):
    assert z.is_finite()
    def f(x):
        m,e=x.man_exp();return F(int(m))*F(2)**int(e)
    return {'lower_exact':str(f(z.lower())),'upper_exact':str(f(z.upper()))}

def ipair(z):
    def f(v):
        s,m,e,bc=v;assert bc>=0
        return F((-1 if s else 1)*m)*F(2)**e
    return {'lower_exact':str(f(z._mpi_[0])),'upper_exact':str(f(z._mpi_[1]))}

def valid(p):
    lo,hi=F(p['lower_exact']),F(p['upper_exact']);assert 0<=lo<=hi;return lo,hi

def cell_arb(row,k,L):
    k=aq(k);L=aq(L);Q=aq(row['Q']);assert F(row['Q'])>=0
    def v(t):
        x=(2*aq(t)).exp();return arb.pi()*L**6*x*(1+x/L**2)**(aq('3/2')-k)*Q
    return {'left':apair(v(row['a'])),'right':apair(v(row['b']))}

def cell_iv(row,k,L):
    k=iq(k);L=iq(L);Q=iq(row['Q']);assert F(row['Q'])>=0
    def v(t):
        t=iq(t);logv=6*iv.ln(L)+2*t+(iq('3/2')-k)*iv.ln(1+iv.exp(2*t)/L**2)
        return iv.pi*iv.exp(logv)*Q
    return {'left':ipair(v(row['a'])),'right':ipair(v(row['b']))}

def enclose_a(p):
    lo,hi=valid(p);return arb(fmpq((lo+hi).numerator,(lo+hi).denominator)/2, fmpq((hi-lo).numerator,(hi-lo).denominator)/2)

def enclose_i(p):
    lo,hi=valid(p);return iv.mpf([iq(str(lo)).a,iq(str(hi)).b])

def root_arb(p):return apair(enclose_a(p).sqrt())
def root_iv(p):
    lo,hi=valid(p)
    if hi==0:return {'lower_exact':'0','upper_exact':'0'}
    assert lo>0
    return ipair(iv.exp(iv.ln(enclose_i(p))/2))

def downward(q,digits=24):
    q=F(q);assert q>0 and type(digits) is int and digits>=2
    exp=len(str(abs(q.numerator)))-len(str(q.denominator))
    while q<F(10)**exp:exp-=1
    while q>=F(10)**(exp+1):exp+=1
    unit=F(10)**(exp-digits+1);n=(q/unit).numerator//(q/unit).denominator
    if n*unit==q:n-=1
    x=n*unit;assert 0<x<q
    power=max(0,-(exp-digits+1));scaled=x*10**power;assert scaled.denominator==1
    text=str(scaled.numerator).rjust(power+1,'0')
    return text if power==0 else text[:-power]+'.'+text[-power:]
