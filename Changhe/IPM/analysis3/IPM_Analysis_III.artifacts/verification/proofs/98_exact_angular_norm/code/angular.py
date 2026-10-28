"""Exact strong-target angular norm. Importing this module performs no IO."""
from fractions import Fraction as F
from flint import arb,arb_poly

def aa(x):
 if isinstance(x,F):return arb(x.numerator)/x.denominator
 return arb(x)

def moments(n):
 if n<0:return []
 out=[F(1)]
 if n==0:return out
 out.append(F(-5,7))
 for k in range(1,n):out.append((-10*out[k]+(4*k-7)*out[k-1])/(4*k+7))
 return out

def quotient(coeff):
 """Return q with sum q cos(2j theta)=(B-B(axis))/cos(theta)^2."""
 n=len(coeff)-1
 if n<=0:return [coeff[0]*0 if coeff else 0]
 out=[coeff[0]*0 for _ in range(n)]
 tail=coeff[0]*0;weighted=coeff[0]*0
 for j in range(n-1,-1,-1):
  tail=coeff[j+1]-tail
  weighted=tail-weighted
  out[j]=(2 if j==0 else 4)*weighted
 return out

def axis(coeff):return sum((b if j%2==0 else -b for j,b in enumerate(coeff)),0)

def normalized_square(q,mm=None):
 q=list(map(aa,q));n=len(q)-1
 if n<0:return arb(0)
 if mm is None:mm=moments(2*n)
 assert len(mm)>2*n
 co=[arb(0) for _ in range(2*n+1)]
 co[n]=q[0]
 for j in range(1,n+1):co[n+j]=co[n-j]=q[j]/2
 square=arb_poly(co)**2
 return square[2*n]+sum((2*square[2*n+j]*aa(mm[j]) for j in range(1,2*n+1)),arb(0))

def beta_mass():
 return 2*(arb(1)/4).gamma()*(arb(3)/2).gamma()/(arb(7)/4).gamma()

def target_integrand(coeff,mm=None):
 b=list(map(aa,coeff));g=axis(b);q=quotient(b)
 return g*g+beta_mass()*normalized_square(q,mm)
