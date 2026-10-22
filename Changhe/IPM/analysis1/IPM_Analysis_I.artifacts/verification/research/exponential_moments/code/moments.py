"""Outward Arb exponential-polynomial moments using scaled series and explicit tails."""
import math
from fractions import Fraction as F
from flint import arb,ctx

def aa(x):
 if isinstance(x,F):return arb(x.numerator)/x.denominator
 return x if isinstance(x,arb) else arb(x)
def phi(j,z,N=None):
 z=aa(z);az=abs(z)
 if N is None:N=max(32,ctx.prec//3)
 assert az<N+1
 term=arb(1);out=arb(0)
 for n in range(N):out+=term/(j+n+1);term=term*z/(n+1)
 tail=az**N/(arb(math.factorial(N))*(j+N+1)*(1-az/(N+1)))
 return out+arb(0,tail.upper())
def cell(lam,coeffs,a,b,N=None):
 lam=aa(lam);a=aa(a);b=aa(b);h=b-a;assert h>0
 scaled=[]
 for j in range(len(coeffs)):
  scaled.append(h**j*sum((math.comb(l,j)*aa(coeffs[l])*a**(l-j) for l in range(j,len(coeffs))),arb(0)))
 return h*(lam*a).exp()*sum((c*phi(j,lam*h,N) for j,c in enumerate(scaled)),arb(0))
def integral(lam,coeffs,a,b,N=None):
 # Endpoints must be exact rational numbers to form a provable covering partition.
 a,b=F(a),F(b);assert a<b
 az=abs(aa(lam)*aa(b-a)).upper()
 parts=max(1,int(float(az))+1)
 while not az<parts:parts+=1
 return sum((cell(lam,coeffs,a+(b-a)*F(i,parts),a+(b-a)*F(i+1,parts),N) for i in range(parts)),arb(0))
