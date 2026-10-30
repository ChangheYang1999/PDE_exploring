from fractions import Fraction as Q
from collections import defaultdict
from math import comb
c=Q(4076476460239181,2251799813685248)
delta=1-1/c
p0=(3+1/c)/2
def add(*ps):
 out=defaultdict(Q)
 for p in ps:
  for k,v in p.items():out[k]+=v
 return {k:v for k,v in out.items() if v}
def scale(p,v):return {k:x*v for k,x in p.items() if x*v}
def mul(p,q,degree=4):
 out=defaultdict(Q)
 for (a,b),v in p.items():
  for (d,e),w in q.items():
   if a+b+d+e<=degree:out[a+d,b+e]+=v*w
 return {k:v for k,v in out.items() if v}
def diff(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   j=list(k);j[axis]-=1;out[tuple(j)]=v*k[axis]
 return out
def dx(p):return diff(p,0)
def dy(p):return diff(p,1)
X={(1,0):Q(1)};Y={(0,1):Q(1)}
def binomial(x,n):
 out=Q(1)
 for j in range(n):out*= (x-j)/(j+1)
 return out
def radial(n):return {(i,n-i):Q(comb(n,i)) for i in range(n+1)}
def harmonic(m):return {(m-j,j):Q((-1)**j*comb(2*m,2*j)) for j in range(m+1)}
def canonical_jet(j,m,k):
 if k>4:return {}
 assert k>=m>=0
 p=p0-j*delta/2
 return add(*(scale(mul(harmonic(m),radial(k-m+l)),binomial(p-k,l)) for l in range(5-k)))
def fields(phi):
 xy=dx(dy(phi));xxy=dx(xy);xyy=dy(xy);yyy=dy(dy(dy(phi)))
 R=add(scale(xy,-4),scale(dy(dy(phi)),-12),scale(mul(X,xxy),-8),scale(mul(Y,yyy),-8))
 U=add(scale(xy,-4),scale(mul(Y,xyy),-8));W=add(scale(xy,4),scale(mul(X,xxy),8))
 return R,U,W
def residual(phi):
 R,U,W=fields(phi)
 return add(scale(mul(X,mul(add({(0,0):c},U),dx(R)),2),2),scale(mul(Y,mul(add({(0,0):c},W),dy(R)),2),2),mul(add({(0,0):c-1},W),R,2))
def linear(phi,eta):
 R,U,W=fields(phi);h,u,w=fields(eta)
 return add(scale(mul(X,add(mul(u,dx(R)),mul(add({(0,0):c},U),dx(h))),2),2),scale(mul(Y,add(mul(w,dy(R)),mul(add({(0,0):c},W),dy(h))),2),2),mul(w,R,2),mul(add({(0,0):c-1},W),h,2))
