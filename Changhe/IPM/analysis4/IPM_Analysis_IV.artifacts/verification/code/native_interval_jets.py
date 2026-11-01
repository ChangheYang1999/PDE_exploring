"""Native Arb series implementing the interval jets of the reviewed theorem234."""
from fractions import Fraction as F
from flint import arb,arb_series,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball

class NativeJet:
 def __init__(self,coefficients,degree):
  assert degree>=0 and ctx.cap>=degree+1,'insufficient native series cap'
  self.degree=degree;self.p=arb_series(list(coefficients)[:degree+1],prec=degree+1)
  assert self.p.prec>=degree+1
 @property
 def c(self):return [self.p[i] for i in range(self.degree+1)]
 def new(self,p):
  assert p.prec>=self.degree+1,'native operation lost required coefficients'
  v=object.__new__(NativeJet);v.degree=self.degree;v.p=p;return v
 def coerce(self,other):
  if isinstance(other,NativeJet):assert other.degree==self.degree;return other
  return NativeJet([other if isinstance(other,arb) else arb(other)],self.degree)
 def __add__(self,other):return self.new(self.p+self.coerce(other).p)
 __radd__=__add__
 def __neg__(self):return self.new(-self.p)
 def __sub__(self,other):return self.new(self.p-self.coerce(other).p)
 def __rsub__(self,other):return self.coerce(other)-self
 def __mul__(self,other):return self.new(self.p*self.coerce(other).p)
 __rmul__=__mul__
 def __truediv__(self,other):
  other=self.coerce(other);assert not other.p[0].contains(0),'jet denominator contains zero'
  return self.new(self.p/other.p)
 def __rtruediv__(self,other):return self.coerce(other)/self
 def contains(self,value):return self.p[0].contains(value)

def enclose_native(response,a,b,degree=5):
 a,b=F(a),F(b);assert a<=b and degree>=1
 middle=(a+b)/2;radius=(b-a)/2
 interval=ball(mpq(str(a))).union(ball(mpq(str(b))));point=ball(mpq(str(middle)))
 whole=response.compact(NativeJet([interval,arb(1)],degree))
 if whole is None:return None
 center=response.compact(NativeJet([point,arb(1)],degree))
 if center is None:return None
 if not isinstance(whole,NativeJet):whole=NativeJet([whole],degree)
 if not isinstance(center,NativeJet):center=NativeJet([center],degree)
 x=ball(mpq(str(-radius))).union(ball(mpq(str(radius))));value=whole.p[degree]
 for j in range(degree-1,-1,-1):value=value*x+center.p[j]
 return value
