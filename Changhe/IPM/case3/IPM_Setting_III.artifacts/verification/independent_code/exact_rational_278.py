"""Our rational polynomial arithmetic from result275; no producer code."""
from exact_polynomial_275 import P,F
def divpoly(a,b):
 """Single-divisor leading-term division; a zero remainder proves exact divisibility."""
 if not b.a:raise ZeroDivisionError
 q=P(dim=a.d);r=P(a.a,a.d);kb=max(b.a);vb=b.a[kb]
 while r.a:
  kr=max(r.a)
  if not all(i>=j for i,j in zip(kr,kb)):return q,r
  term=P({tuple(i-j for i,j in zip(kr,kb)):r.a[kr]/vb},a.d);q=q+term;r=r-term*b
 return q,r
factors=[];cancellations=[]
class Rat:
 def __init__(self,num=0,den=None):
  self.num=num if isinstance(num,P)else P({(0,0):F(num)});self.den={k:v for k,v in (den or {}).items()if v}
  for k in sorted(self.den):
   while self.den[k]>0:
    q,r=divpoly(self.num,factors[k])
    if r.a:break
    self.num=q;self.den[k]-=1;cancellations.append(k)
  self.den={k:v for k,v in self.den.items()if v}
 def cast(self,b):return b if isinstance(b,Rat)else Rat(b)
 def __add__(self,b):
  b=self.cast(b);den={k:max(self.den.get(k,0),b.den.get(k,0))for k in set(self.den)|set(b.den)};a1=self.num;b1=b.num
  for k,v in den.items():a1=a1*factors[k]**(v-self.den.get(k,0));b1=b1*factors[k]**(v-b.den.get(k,0))
  return Rat(a1+b1,den)
 __radd__=__add__
 def __neg__(self):return Rat(-self.num,self.den)
 def __sub__(self,b):return self+-self.cast(b)
 def __rsub__(self,b):return self.cast(b)+-self
 def __mul__(self,b):
  b=self.cast(b);return Rat(self.num*b.num,{k:self.den.get(k,0)+b.den.get(k,0)for k in set(self.den)|set(b.den)})
 __rmul__=__mul__
 def __pow__(self,k):
  assert isinstance(k,int)and k>=0
  return Rat(self.num**k,{j:v*k for j,v in self.den.items()})
 def denominator(self):
  d=P({(0,0):1})
  for k,v in self.den.items():d=d*factors[k]**v
  return d
 def evaluate(self,v):return self.num.evaluate(v)/self.denominator().evaluate(v)
def ps(co,K):
 L=len(co)-1;out=[L]
 for k in range(1,K+1):
  if k<=L:out.append(-sum(co[j]*out[k-j]for j in range(1,k))-k*co[k])
  else:out.append(-sum(co[j]*out[k-j]for j in range(1,L+1)))
 return out
