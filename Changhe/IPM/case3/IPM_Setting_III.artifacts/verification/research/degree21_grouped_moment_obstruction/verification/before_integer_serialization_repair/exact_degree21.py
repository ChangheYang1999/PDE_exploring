"""Our independent degree21 arithmetic. No external checker is imported.

Rational expressions use integer multivariate arithmetic. Determinants and
pseudo-division are implemented here explicitly; no FLINT resultant is used.
"""
from flint import fmpz_mpoly_ctx, fmpz, fmpq_poly
from math import gcd,comb
C=fmpz_mpoly_ctx.get(('x','y','eta'),ordering='lex');x,y,h=C.gens()
def poly(a):return a if hasattr(a,'terms')else C.constant(a)
def prim(a):
 a=poly(a)
 if not a:return a
 c=a.content();return a//(c if a.leading_coefficient()>0 else -c)
def degree(a,i):return int(a.degrees()[i]) if a else -1
def coef(a,i,k):
 d={}
 for ex,v in a.terms():
  if ex[i]==k:
   new=list(ex);new[i]=0;d[tuple(new)]=v
 return C.from_dict(d)
def decode(d):return C.from_dict({tuple(k):int(v)for k,v in d['terms']})
def encode(a):return dict(terms=[[list(k),str(v)]for k,v in a.terms()],degrees=list(a.degrees()),total_degree=int(a.total_degree()))
class Q:
 def __init__(self,n=0,d=1):
  if isinstance(n,Q):self.n,self.d=n.n,n.d;return
  n=poly(n);d=poly(d)
  if not d:raise ZeroDivisionError
  if not n:self.n,self.d=C.constant(0),C.constant(1);return
  g=n.gcd(d);n=n//g;d=d//g
  if d.leading_coefficient()<0:n=-n;d=-d
  self.n,self.d=n,d
 def cast(self,b):return b if isinstance(b,Q)else Q(b)
 def __add__(self,b):b=self.cast(b);return Q(self.n*b.d+b.n*self.d,self.d*b.d)
 __radd__=__add__
 def __neg__(self):return Q(-self.n,self.d)
 def __sub__(self,b):return self+-self.cast(b)
 def __rsub__(self,b):return self.cast(b)+-self
 def __mul__(self,b):b=self.cast(b);return Q(self.n*b.n,self.d*b.d)
 __rmul__=__mul__
 def __truediv__(self,b):b=self.cast(b);return Q(self.n*b.d,self.d*b.n)
 def __rtruediv__(self,b):return self.cast(b)/self
 def __pow__(self,k):
  assert isinstance(k,int)
  return Q(self.n**k,self.d**k) if k>=0 else Q(self.d**(-k),self.n**(-k))
 def __eq__(self,b):b=self.cast(b);return self.n*b.d==b.n*self.d
 def at(self,values):return self.n(*values)/self.d(*values)
 def saved(self):return dict(numerator=encode(self.n),denominator=encode(self.d))
 def compose(self,values):return Q(self.n.compose(*values),self.d.compose(*values))
def qdecode(d):return Q(decode(d['numerator']),decode(d['denominator']))
def ps(co,K):
 co=list(map(Q,co));L=len(co)-1;s=[Q(L)]
 for k in range(1,K+1):
  v=-sum((co[j]*s[k-j]for j in range(1,min(k,L+1))),Q(0))
  if k<=L:v-=k*co[k]
  s.append(v)
 return s
def conv(a,b,K):
 out=[Q(0)for _ in range(K+1)]
 for i,u in enumerate(a):
  for j,v in enumerate(b):
   if i+j<=K:out[i+j]+=u*v
 return out
def logps(co,K):
 aa=[Q(0)]+[Q(c)for c in co[1:]];power=[Q(1)];out=[Q(0)for _ in range(K+1)]
 for ell in range(1,K+1):
  power=conv(power,aa,K)
  for k in range(1,K+1):out[k]+=power[k]*((-1)**(ell+1))/ell
 return [Q(len(co)-1)]+[-k*out[k]for k in range(1,K+1)]
def val(co,z):
 v=Q(0)
 for c in co:v=v*z+c
 return v
def der(co,z):return val([(len(co)-1-i)*Q(c)for i,c in enumerate(co[:-1])],z)
def sylv(f,g,i):
 m,n=degree(f,i),degree(g,i);assert m>0 and n>0
 aa=[coef(f,i,k)for k in range(m,-1,-1)];bb=[coef(g,i,k)for k in range(n,-1,-1)];z=C.constant(0)
 return [[z]*k+aa+[z]*(n-1-k)for k in range(n)]+[[z]*k+bb+[z]*(m-1-k)for k in range(m)]
def bareiss(a):
 a=[list(r)for r in a];one=C.constant(1);old=one;sign=1;divs=0;swaps=0
 for k in range(len(a)-1):
  piv=next((i for i in range(k,len(a))if a[i][k]),None)
  if piv is None:return C.constant(0),divs,swaps
  if piv!=k:a[k],a[piv]=a[piv],a[k];sign=-sign;swaps+=1
  d=a[k][k]
  for i in range(k+1,len(a)):
   for j in range(k+1,len(a)):
    numerator=a[i][j]*d-a[i][k]*a[k][j];q,r=divmod(numerator,old)
    if r:raise ArithmeticError('Nonexact multivariate Bareiss division')
    a[i][j]=q;divs+=1
   a[i][k]=C.constant(0)
  old=d
 return sign*a[-1][-1],divs,swaps
def resultant(f,g,i):return bareiss(sylv(f,g,i))[0]
def prem(f,g,i):
 dg=degree(g,i);assert dg>=0 and g
 r=f;q=C.constant(0);lc=coef(g,i,dg);power=0;target=max(0,degree(f,i)-dg+1);var=C.gens()[i]
 while r and degree(r,i)>=dg:
  d=degree(r,i)-dg;c=coef(r,i,degree(r,i));q=lc*q+c*var**d;r=lc*r-c*var**d*g;power+=1
 q*=lc**(target-power);r*=lc**(target-power)
 assert lc**target*f==q*g+r
 return r,q,target
def univ(a):
 assert all(k[0]==k[1]==0 for k,v in a.terms())
 d=max(0,degree(a,2));co=[0]*(d+1)
 for k,v in a.terms():co[k[2]]=int(v)
 return co
def shifted(co,z):return [sum(int(co[j])*comb(j,k)*z**(j-k)for j in range(k,len(co)))for k in range(len(co))]
def divexact(f,g):
 q,r=divmod(f,g)
 if r:raise ArithmeticError('Nonexact stated polynomial division')
 return q
