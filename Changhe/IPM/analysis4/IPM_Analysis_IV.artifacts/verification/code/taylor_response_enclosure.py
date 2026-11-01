"""Taylor jets over Arb; all rational divisions check their interval constant."""
from fractions import Fraction as F
from flint import arb
from gmpy2 import mpq
from pure_cartesian_ball import ball

class Jet:
    def __init__(self,coefficients,degree):
        self.degree=degree;self.c=list(coefficients[:degree+1])+[arb(0)]*max(0,degree+1-len(coefficients))
    def coerce(self,other):
        if isinstance(other,Jet):assert other.degree==self.degree;return other
        return Jet([other if isinstance(other,arb) else arb(other)],self.degree)
    def __add__(self,other):
        other=self.coerce(other);return Jet([a+b for a,b in zip(self.c,other.c)],self.degree)
    __radd__=__add__
    def __neg__(self):return Jet([-a for a in self.c],self.degree)
    def __sub__(self,other):return self+-self.coerce(other)
    def __rsub__(self,other):return self.coerce(other)+-self
    def __mul__(self,other):
        other=self.coerce(other)
        return Jet([sum((self.c[j]*other.c[n-j] for j in range(n+1)),arb(0)) for n in range(self.degree+1)],self.degree)
    __rmul__=__mul__
    def __truediv__(self,other):
        other=self.coerce(other);assert not other.c[0].contains(0),'jet denominator contains zero';out=[]
        for n in range(self.degree+1):out.append((self.c[n]-sum((other.c[j]*out[n-j] for j in range(1,n+1)),arb(0)))/other.c[0])
        return Jet(out,self.degree)
    def __rtruediv__(self,other):return self.coerce(other)/self
    def contains(self,value):return self.c[0].contains(value)

def enclose(response,a,b,degree=3):
    a,b=F(a),F(b);assert a<=b and degree>=1
    middle=(a+b)/2;radius=(b-a)/2
    interval=ball(mpq(str(a))).union(ball(mpq(str(b))));point=ball(mpq(str(middle)))
    whole=response.compact(Jet([interval,arb(1)],degree))
    if whole is None:return None
    center=response.compact(Jet([point,arb(1)],degree))
    if center is None:return None
    if not isinstance(whole,Jet):whole=Jet([whole],degree)
    if not isinstance(center,Jet):center=Jet([center],degree)
    x=ball(mpq(str(-radius))).union(ball(mpq(str(radius))));value=whole.c[degree]
    for j in range(degree-1,-1,-1):value=value*x+center.c[j]
    return value
