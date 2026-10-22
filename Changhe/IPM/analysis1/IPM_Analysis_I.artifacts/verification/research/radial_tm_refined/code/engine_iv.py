"""Method B: factorial ODE recurrence, endpoint propagation, rational exp bound."""
from functools import lru_cache
from fractions import Fraction
from math import factorial
from mpmath import iv
from common import iv_endpoints
PRECISION=180;ORDER=20;SCALE=1<<1074
FACT=[factorial(j) for j in range(23)]

def setup():iv.dps=PRECISION
def exact_rational(value):
 value=Fraction(value)
 return iv.mpf(value.numerator)/value.denominator
def endpoint_interval(low,high):
 assert low<=high
 # mpmath's interval conversion supplies directed endpoint rounding.
 return iv.mpf([low,high])/SCALE

def exponential_nonnegative(value):
 """Rational Taylor bracket, no transcendental call in this engine."""
 value=Fraction(value);assert 0<=value<1
 x=exact_rational(value);term=iv.mpf(1);total=iv.mpf(1)
 for j in range(1,65):term=term*x/j;total+=term
 omitted=term*x/65;upper=total+omitted/(1-x/66)
 return iv.mpf([total.a,upper.b])

def exponential_rational(value):
 value=Fraction(value);negative=value<0;reduced=abs(value);doublings=0
 while reduced>=1:reduced/=2;doublings+=1
 result=exponential_nonnegative(reduced)
 for _ in range(doublings):result=result*result
 return 1/result if negative else result

@lru_cache(maxsize=261)
def weights(n):
 assert 1<=n<=261
 lp,lm=2*n-2,-2*n-2
 a=[0,1]+[0]*8;b=[1,0]+[0]*8;result=[]
 for j in range(ORDER+1):
  result.append((tuple(x+y for x,y in zip(a,b)),tuple(x-y for x,y in zip(a,b))))
  if j<ORDER:
   a=[lp*x for x in a];b=[lm*x for x in b]
   for k in range(min(j,7)+1):
    forcing=FACT[j]*(1<<(j-k))//FACT[j-k]
    a[2+k]-=forcing;b[2+k]+=forcing
 return tuple(result)

def sign_hull(weights,lower,upper):
 left=0;right=0
 for w,lo,hi in zip(weights,lower,upper):
  assert lo<=hi
  if w>=0:left+=w*lo;right+=w*hi
  else:left+=w*hi;right+=w*lo
 return endpoint_interval(left,right)

def coefficients(n,em,er,am,ar,bm,br,fm,fr):
 setup();E=endpoint_interval(em-er,em+er);Z=E*E
 low=[am-ar,bm-br]+[m-r for m,r in zip(fm,fr)];high=[am+ar,bm+br]+[m+r for m,r in zip(fm,fr)]
 out=[[],[]]
 for j,pair in enumerate(weights(n)):
  for family,w in enumerate(pair):
   homogeneous=sign_hull(w[:2],low[:2],high[:2]);forcing=sign_hull(w[2:],low[2:],high[2:])
   out[family].append((homogeneous/Z+Z*forcing)/(2*FACT[j]))
 return out

@lru_cache(maxsize=12)
def derivative_weights(width):
 setup();h=exact_rational(width);powers=tuple(h**j for j in range(22));cols=[]
 for k in range(8):
  # Different construction from the first method's binomial formula.
  poly=[int(j==k) for j in range(8)];col=[]
  for d in range(21):
   value=iv.mpf(0)
   for coefficient in reversed(poly):value=value*h+coefficient
   col.append(value)
   poly=[2*v+(j+1)*poly[j+1] if j<7 else 2*v for j,v in enumerate(poly)]
  cols.append(col)
 return tuple(tuple(cols[k][d] for k in range(8)) for d in range(21)),powers

@lru_cache(maxsize=4000)
def remainder_weights(width,n):
 setup();rows,powers=derivative_weights(width);h=exact_rational(width);lp,lm=2*n-2,2*n+2
 ep=exponential_nonnegative(lp*width);e2=exponential_nonnegative(2*width);c=powers[21]/(2*FACT[21])
 aa=c*lm**21;bb=c*lp**21*ep;ff=[]
 for k in range(8):
  sumderivatives=iv.mpf(0)
  for d in range(21):sumderivatives+=(lp**(20-d)+lm**(20-d))*rows[d][k]
  ff.append(c*e2*((lp**21*ep+lm**21)*powers[k+1]+sumderivatives))
 return aa,bb,tuple(ff),powers

def absolute_upper(x):
 a,b=x._mpi_;assert a[3]>=0 and b[3]>=0
 return abs(x).b

def remainder(n,width,em,er,am,ar,bm,br,fm,fr,coefficients_pair):
 setup();a,b,forcing,powers=remainder_weights(width,n)
 lower=endpoint_interval(em-er,em-er);upper=endpoint_interval(em+er,em+er)
 amag=endpoint_interval(abs(am)+ar,abs(am)+ar);bmag=endpoint_interval(abs(bm)+br,abs(bm)+br)
 tail=(a*amag+b*bmag)/(lower*lower)
 total=iv.mpf(0)
 for w,m,r in zip(forcing,fm,fr):total+=w*endpoint_interval(abs(m)+r,abs(m)+r)
 tail+=upper*upper*total
 result=[]
 for coefs in coefficients_pair:
  value=tail
  for j in range(13,21):value+=absolute_upper(coefs[j])*powers[j]
  iv_endpoints(value);result.append(value)
 return result
