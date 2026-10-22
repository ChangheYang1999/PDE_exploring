"""Exact Q[w,A(w)^(-1)] parity jets for the beta3 far residual.

No fitting code imports. Scalar exp(alpha) is factored out of the algebra.
"""
from flint import fmpq, fmpq_poly as Poly
from functools import lru_cache
from math import factorial
from fractions import Fraction

Q=lambda x:fmpq(str(x))
@lru_cache(None)
def ids(n):return tuple((i,j) for i in range(n+1) for j in range(n+1-i))
BASE=Poly([1]);POWERS=[BASE**0]
def set_base(p):
 global BASE,POWERS
 BASE=Poly(p);POWERS=[Poly([1])]
def basepow(k):
 while len(POWERS)<=k:POWERS.append(POWERS[-1]*BASE)
 return POWERS[k]
class RF:
 __slots__=('p','k')
 def __init__(self,p=0,k=0):
  if isinstance(p,RF):self.p,self.k=p.p,p.k;return
  self.p=p if isinstance(p,Poly) else Poly([Q(p)])
  self.k=k if self.p else 0
 def __bool__(self):return bool(self.p)
 def __add__(self,b):
  b=RF(b);k=max(self.k,b.k)
  return RF(self.p*basepow(k-self.k)+b.p*basepow(k-b.k),k)
 __radd__=__add__
 def __neg__(self):return RF(-self.p,self.k)
 def __sub__(self,b):return self+-RF(b)
 def __rsub__(self,b):return RF(b)+-self
 def __mul__(self,b):
  b=RF(b);return RF(self.p*b.p,self.k+b.k)
 __rmul__=__mul__
 def reciprocal(self):
  if not self.p:raise ZeroDivisionError('zero rational function')
  if self.p.degree()==0:return RF(basepow(self.k)/self.p[0])
  if self.p==BASE:
   return RF(basepow(self.k-1)) if self.k else RF(1,1)
  raise ValueError('reciprocal outside the certified ring construction')
 def __truediv__(self,b):return self*RF(b).reciprocal()
 def at(self,w):return self.p(Q(w))/(BASE(Q(w))**self.k)
 def serial(self):return {'coefficients':[str(v) for v in self.p.coeffs()],'denominator_power':self.k}

class Jet:
 def __init__(self,n,c=None):
  if n<0:raise ValueError('insufficient jet order')
  self.n=n;self.c={ij:RF((c or {}).get(ij,0)) for ij in ids(n)}
 @property
 def v(self):return self.c[0,0]
 def trunc(self,n):
  if n>self.n:raise ValueError('cannot increase jet order')
  return Jet(n,self.c)
 def __add__(self,b):
  if not isinstance(b,Jet):b=Jet(self.n,{(0,0):b})
  n=min(self.n,b.n);return Jet(n,{ij:self.c[ij]+b.c[ij] for ij in ids(n)})
 __radd__=__add__
 def __neg__(self):return Jet(self.n,{ij:-v for ij,v in self.c.items()})
 def __sub__(self,b):return self+-b
 def __rsub__(self,b):return -self+b
 def __mul__(self,b):
  if not isinstance(b,Jet):return Jet(self.n,{ij:v*b for ij,v in self.c.items()})
  n=min(self.n,b.n);out={ij:RF(0) for ij in ids(n)}
  for (i,j),v in self.c.items():
   if i+j>n or not v:continue
   for (k,l),t in b.c.items():
    if i+j+k+l<=n and t:out[i+k,j+l]=out[i+k,j+l]+v*t
  return Jet(n,out)
 __rmul__=__mul__
 def dzero(self):
  c=dict(self.c);c[0,0]=RF(0);return Jet(self.n,c)
 def reciprocal(self):
  rec=self.v.reciprocal();z=self.dzero()*(-rec);t=Jet(self.n,{(0,0):1});out=t
  for k in range(1,self.n+1):t=t*z;out=out+t
  return out*rec
 def __truediv__(self,b):return self*(b.reciprocal() if isinstance(b,Jet) else RF(b).reciprocal())
 def derivative(self,k):
  n=self.n-1
  if n<0:raise ValueError('insufficient derivative order')
  return Jet(n,{(i,j):self.c[i+(k==0),j+(k==1)]*(i+1 if k==0 else j+1) for i,j in ids(n)})
 def ipow(self,n):
  t=Jet(self.n,{(0,0):1})
  for _ in range(n):t=t*self
  return t
 def unit_power(self,r):
  if self.v.k or self.v.p!=Poly([1]):raise ValueError('exact unit constant required')
  z=self.dzero();t=Jet(self.n,{(0,0):1});out=t;b=fmpq(1);r=Q(r)
  for k in range(1,self.n+1):t=t*z;b*= (r-k+1)/k;out=out+t*b
  return out
class Parity:
 def __init__(self,eps,delta,v,X,H):self.eps,self.delta,self.v,self.X,self.H=eps,delta,v,X,H
 def __add__(self,b):
  if (self.eps,self.delta)!=(b.eps,b.delta):raise ValueError('parity mismatch')
  return Parity(self.eps,self.delta,self.v+b.v,self.X,self.H)
 def __neg__(self):return Parity(self.eps,self.delta,-self.v,self.X,self.H)
 def __sub__(self,b):return self+-b
 def __mul__(self,b):
  if not isinstance(b,Parity):return Parity(self.eps,self.delta,self.v*b,self.X,self.H)
  v=self.v*b.v
  if self.eps and b.eps:v=v*self.X
  if self.delta and b.delta:v=v*self.H
  return Parity(self.eps^b.eps,self.delta^b.delta,v,self.X,self.H)
 __rmul__=__mul__
 def __truediv__(self,b):
  if isinstance(b,Parity):
   if b.eps or b.delta:raise ValueError('odd reciprocal forbidden')
   return Parity(self.eps,self.delta,self.v/b.v,self.X,self.H)
  return self*(RF(b).reciprocal())
 def dx(self):
  d=self.v.derivative(0);v=self.v+2*self.X*d if self.eps else 2*d
  return Parity(1-self.eps,self.delta,v,self.X,self.H)
 def de(self):
  d=self.v.derivative(1);v=self.v+2*self.H*d if self.delta else 2*d
  return Parity(self.eps,1-self.delta,v,self.X,self.H)

def construct(polynomials,s,alpha,order=4):
 set_base(Poly([1]));s,alpha=Q(s),Q(alpha);n=order
 X=Jet(n,{(0,0):Poly([1,0,0,-1]),(1,0):1});H=Jet(n,{(0,0):Poly([0,s*s]),(0,1):1})
 F=X+H.ipow(3)/(s**6)
 assert F.v.p==Poly([1]) and F.v.k==0
 W=H*F.unit_power('-1/3')/(s*s);assert W.v.p==Poly([0,1]) and W.v.k==0
 J=W.dzero();powers=[Jet(n,{(0,0):1})]
 for k in range(n):powers.append(powers[-1]*J)
 ps=[]
 for p in polynomials:
  v=Jet(n);dp=Poly(p)
  for k in range(n+1):v=v+powers[k]*(dp/factorial(k));dp=dp.derivative()
  ps.append(v)
 g0=Parity(1,1,(F.unit_power('1/3')*ps[0]).trunc(n),X,H)
 g1=Parity(1,1,(F.unit_power('1/6')*ps[1]).trunc(n-1),X,H)
 g2=Parity(1,1,((ps[1]*alpha+ps[2])/2).trunc(n-2),X,H)
 A=g0.dx().de();assert not A.v.v.k
 set_base(A.v.v.p)
 b=g0.dx().dx()/A;Dx=lambda f:f.dx()-b*f.de();Dy=lambda f:f.de()/A
 s0=-g1;s1=-2*g2+g1.dx()*g1.de()/A;v1=-Dy(s0);v2=Dx(s0)
 lap=lambda f:Dx(Dx(f))+Dy(Dy(f))
 o0=-lap(s0);o1=-lap(s1)
 terms=[-o1,v1*Dx(o0),v2*Dy(o0),b]
 assert all((f.eps,f.delta)==(1,1) for f in terms)
 vals=[f.v.v for f in terms];K=max(v.k for v in vals);nums=[v.p*basepow(K-v.k) for v in vals]
 return {'A':BASE,'terms':vals,'K':K,'numerators':nums,'final_orders':[f.v.n for f in terms]}

def endpoint_polynomials(data):
 co=[[Q(v) for v in row] for row in data['outer']];J=len(co)-1;K=len(co[0])-1
 W=Poly([-1,2]);T=[Poly([1])]
 if K:T.append(W)
 for k in range(2,K+1):T.append(2*W*T[-1]-T[-2])
 out=[]
 for d in range(3):
  weights=[(fmpq((-1)**n),fmpq(-2*(-1)**n*n*n),fmpq(4*(-1)**n*n*n*(n*n-1),3))[d] for n in range(J+1)]
  out.append(sum((T[k]*sum((co[n][k]*weights[n] for n in range(J+1)),fmpq(0)) for k in range(K+1)),Poly([])))
 return out
