"""Own interval parity/Taylor evaluator on F=1. No fitter imports.

Exact gmpy2 rational endpoints; directed dyadic compression bounds bit growth.
"""
from math import comb,factorial
from fractions import Fraction
from functools import lru_cache
import gmpy2 as g
Q=g.mpq
BITS=176
DEN=g.mpz(1)<<BITS

def q(v):
 if isinstance(v,Fraction):return Q(v.numerator,v.denominator)
 return Q(v)
class I:
 __slots__=('lo','hi')
 def __init__(self,a=0,b=None):
  if isinstance(a,I):self.lo,self.hi=a.lo,a.hi;return
  self.lo,self.hi=q(a),q(a if b is None else b)
  if self.lo>self.hi:raise ValueError('reversed interval')
 @classmethod
 def rounded(cls,l,h):
  l,h=l*DEN,h*DEN
  return cls(Q(l.numerator//l.denominator,DEN),Q(-((-h.numerator)//h.denominator),DEN))
 def __add__(self,b):
  b=I(b);return I.rounded(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,b):return self+-I(b)
 def __rsub__(self,b):return I(b)+-self
 def __mul__(self,b):
  b=I(b);p=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi);return I.rounded(min(p),max(p))
 __rmul__=__mul__
 def reciprocal(self):
  if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
  return I.rounded(1/self.hi,1/self.lo)
 def __truediv__(self,b):return self*I(b).reciprocal()
 def __rtruediv__(self,b):return I(b)*self.reciprocal()
 def __abs__(self):return I(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),max(abs(self.lo),abs(self.hi)))
 def __bool__(self):return self.lo!=0 or self.hi!=0
 def __repr__(self):return f'I({float(self.lo):.8g},{float(self.hi):.8g})'
 def serial(self):return {'lo':str(self.lo),'hi':str(self.hi)}

@lru_cache(None)
def indices(n):return tuple((i,j) for i in range(n+1) for j in range(n+1-i))
class Jet:
 def __init__(self,n,c=None):
  if n<0:raise ValueError('insufficient jet order')
  self.n=n;self.c={ij:I((c or {}).get(ij,0)) for ij in indices(n)}
 @property
 def v(self):return self.c[0,0]
 def trunc(self,n):return Jet(n,self.c)
 def __add__(self,b):
  if not isinstance(b,Jet):b=Jet(self.n,{(0,0):b})
  n=min(self.n,b.n);return Jet(n,{ij:self.c[ij]+b.c[ij] for ij in indices(n)})
 __radd__=__add__
 def __neg__(self):return Jet(self.n,{ij:-v for ij,v in self.c.items()})
 def __sub__(self,b):return self+-b
 def __rsub__(self,b):return -self+b
 def __mul__(self,b):
  if not isinstance(b,Jet):return Jet(self.n,{ij:v*b for ij,v in self.c.items()})
  n=min(self.n,b.n);out={ij:I(0) for ij in indices(n)}
  for (i,j),v in self.c.items():
   if i+j>n or not v:continue
   for (k,l),w in b.c.items():
    if i+j+k+l<=n and w:out[i+k,j+l]=out[i+k,j+l]+v*w
  return Jet(n,out)
 __rmul__=__mul__
 def dzero(self):
  c=dict(self.c);c[0,0]=I(0);return Jet(self.n,c)
 def reciprocal(self):
  rec=self.v.reciprocal();z=self.dzero()*(-rec);t=Jet(self.n,{(0,0):1});out=t
  for k in range(1,self.n+1):t=t*z;out=out+t
  return out*rec
 def __truediv__(self,b):return self*(b.reciprocal() if isinstance(b,Jet) else I(b).reciprocal())
 def derivative(self,k):
  n=self.n-1
  if n<0:raise ValueError('insufficient derivative order')
  return Jet(n,{(i,j):self.c[i+(k==0),j+(k==1)]*(i+1 if k==0 else j+1) for i,j in indices(n)})
 def integer_power(self,n):
  t=Jet(self.n,{(0,0):1})
  for _ in range(n):t=t*self
  return t
 def unit_power(self,r):
  if self.v.lo!=1 or self.v.hi!=1:raise ValueError('unit constant required')
  z=self.dzero();t=Jet(self.n,{(0,0):1});out=t;b=Q(1);r=q(r)
  for k in range(1,self.n+1):t=t*z;b*= (r-k+1)/k;out=out+t*b
  return out

class Parity:
 def __init__(self,eps,delta,v,X,H):self.eps,self.delta,self.v,self.X,self.H=eps,delta,v,X,H
 def __add__(self,b):
  if self.eps!=b.eps or self.delta!=b.delta:raise ValueError('parity addition mismatch')
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
  return self*(I(b).reciprocal())
 def dx(self):
  d=self.v.derivative(0)
  v=self.v+2*self.X*d if self.eps else 2*d
  return Parity(1-self.eps,self.delta,v,self.X,self.H)
 def de(self):
  d=self.v.derivative(1)
  v=self.v+2*self.H*d if self.delta else 2*d
  return Parity(self.eps,1-self.delta,v,self.X,self.H)

# Exact power coefficients of shifted Chebyshev polynomials, own recurrence.
def padd(a,b):
 out=[Q(0)]*max(len(a),len(b))
 for i,v in enumerate(a):out[i]+=v
 for i,v in enumerate(b):out[i]+=v
 return out
@lru_cache(None)
def cheb_power(n):
 if n==0:return (Q(1),)
 if n==1:return (Q(-1),Q(2))
 p=list(cheb_power(n-1));out=padd([-2*v for v in p],[Q(0)]+[4*v for v in p]);return tuple(padd(out,[-v for v in cheb_power(n-2)]))
def to_bernstein(co):
 n=len(co)-1;power=[Q(0)]*(n+1)
 for i,c in enumerate(co):
  for j,v in enumerate(cheb_power(i)):power[j]+=c*v
 return [sum((power[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),Q(0)) for k in range(n+1)]
def split(b):
 lev=list(b);left=[];right=[]
 while lev:
  left.append(lev[0]);right.append(lev[-1]);lev=[(lev[i]+lev[i+1])/2 for i in range(len(lev)-1)]
 return left,right[::-1]
def bern_derivative(b,width,k):
 for _ in range(k):
  n=len(b)-1
  if n==0:return I(0)
  b=[n*(b[i+1]-b[i])/width for i in range(n)]
 return I(min(b),max(b))

def endpoint_rows(data):
 co=[[q(v) for v in row] for row in data['outer']];J=len(co)-1;K=len(co[0])-1
 rows=[]
 for d in range(3):
  weights=[(Q((-1)**n),Q(-2*(-1)**n*n*n),Q(4*(-1)**n*n*n*(n*n-1),3))[d] for n in range(J+1)]
  rows.append([sum((co[n][k]*weights[n] for n in range(J+1)),Q(0)) for k in range(K+1)])
 return rows

def exp_bound(alpha,N=100):
 alpha=q(alpha)
 if not 0<alpha<N+2:raise ValueError('alpha range')
 lo=sum((alpha**k/factorial(k) for k in range(N+1)),Q(0));hi=lo+alpha**(N+1)/factorial(N+1)/(1-alpha/(N+2));return I(lo,hi)

def evaluate(lo,hi,bs,s,alpha,a):
 lo,hi,s,alpha,a=map(q,(lo,hi,s,alpha,a));width=hi-lo
 if width<=0:raise ValueError('positive leaf width required')
 n=5;X=Jet(n,{(0,0):I(1-hi**3,1-lo**3),(1,0):1});H=Jet(n,{(0,0):I(s*s*lo,s*s*hi),(0,1):1})
 FF=X+H.integer_power(3)/(s**6);FF.c[0,0]=I(1)
 W=H*FF.unit_power(Q(-1,3))/(s*s);W.c[0,0]=I(lo,hi);J=W.dzero()
 powers=[Jet(n,{(0,0):1})]
 for _ in range(n):powers.append(powers[-1]*J)
 ps=[]
 for b in bs:
  v=Jet(n)
  for k in range(n+1):v=v+powers[k]*(bern_derivative(b,width,k)/factorial(k))
  ps.append(v)
 g0=Parity(1,1,(FF.unit_power(Q(1,3))*ps[0]).trunc(5),X,H)
 g1=Parity(1,1,(FF.unit_power(Q(1,6))*ps[1]).trunc(4),X,H)
 g2=Parity(1,1,((ps[1]*alpha+ps[2])/2).trunc(3),X,H)
 A=g0.dx().de()
 if A.v.v.lo<=0:raise ArithmeticError(('A not enclosed positive',A.v.v))
 b=g0.dx().dx()/A
 Dx=lambda f:f.dx()-b*f.de()
 Dy=lambda f:f.de()/A
 s0=-g1;s1=-2*g2+g1.dx()*g1.de()/A
 v1=-Dy(s0);v2=Dx(s0)
 lap=lambda f:Dx(Dx(f))+Dy(Dy(f))
 o0=-lap(s0);o1=-lap(s1)
 terms=[-o1,v1*Dx(o0),v2*Dy(o0),b*a]
 c1=(I(1)-I(1)/exp_bound(alpha))/alpha;c12=c1*c1
 for i in range(3):terms[i]=terms[i]*c12
 if any((f.eps,f.delta)!=(1,1) for f in terms):raise AssertionError('final parity')
 vals=[f.v.v for f in terms];C=sum(vals,I(0));N=sum(map(abs,vals),I(0))
 if N.lo<=0:raise ArithmeticError(('denominator not enclosed positive',N))
 ratio=abs(C)/N;ratio=I(max(Q(0),ratio.lo),min(Q(1),ratio.hi))
 # First section derivative is available without radical variables.
 derivatives=[-3*I(lo*lo,hi*hi)*f.v.c[1,0]+s*s*f.v.c[0,1] for f in terms]
 return {'A':A.v.v,'terms':vals,'C':C,'N':N,'ratio':ratio,'derivative_terms':derivatives}
