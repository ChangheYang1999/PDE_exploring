"""Fresh Arb1536 audit: finite particular solution, not either primary formula."""
from functools import lru_cache
from fractions import Fraction as Q
from math import factorial,comb
from flint import arb,ctx,fmpq
PRECISION=1536;ORDER=22

def setup():ctx.prec=PRECISION;ctx.threads=1
def to_arb(q):
 q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def box(m,r):
 m,r=Q(float(m)),Q(float(r));assert r>=0
 return to_arb(m-r).union(to_arb(m+r))

def monomial_particular(k,lam,sign):
 assert lam!=2
 poly=[Q(0)]*8
 for j in range(7,-1,-1):poly[j]=(Q(sign if j==k else 0)-(j+1)*poly[j+1] if j<7 else Q(sign if j==k else 0))/(2-lam)
 # Coefficient-by-coefficient substitution of Q'+(2-lambda)Q=sign*u^k.
 for j in range(8):assert (2-lam)*poly[j]+((j+1)*poly[j+1] if j<7 else 0)==(sign if j==k else 0)
 return poly

@lru_cache(maxsize=261)
def weights(n):
 result=[];lp,lm=2*n-2,-2*n-2
 branches=[]
 for lam,sign in ((lp,-1),(lm,1)):
  table=[]
  for k in range(8):
   poly=monomial_particular(k,lam,sign) if lam!=2 else None;row=[]
   for j in range(23):
    if lam==2:value=Q(sign*2**(j-k-1),(k+1)*factorial(j-k-1)) if j>=k+1 else Q(0)
    else:value=sum((poly[v]*Q(2**(j-v),factorial(j-v)) for v in range(min(j,7)+1)),Q(0))-poly[0]*Q(lam**j,factorial(j))
    row.append(value)
   assert row[0]==0;table.append(row)
  branches.append(table)
 for j in range(23):
  plus,minus=branches
  result.append((tuple((plus[k][j]+minus[k][j])/2 for k in range(8)),tuple((plus[k][j]-minus[k][j])/2 for k in range(8))))
 return tuple(result)

def derivative_poly(poly,N,h):
 out=arb(0)
 for k,p in enumerate(poly):
  scalar=sum((Q(comb(N,v)*2**(N-v)*factorial(k),factorial(k-v))*h**(k-v) for v in range(min(N,k)+1)),Q(0))
  out+=p.abs_upper()*to_arb(scalar)
 return out

def derivative(q0,Z,F,lam,sign,N,h):
 if lam==2:
  polynomial=[q0]+[sign*Z*x/(k+1) for k,x in enumerate(F)]
  return (2*to_arb(h)).exp()*derivative_poly(polynomial,N,h)
 polynomial=[arb(0)]*8
 for k in range(7,-1,-1):polynomial[k]=(sign*F[k]-((k+1)*polynomial[k+1] if k<7 else 0))/(2-lam)
 constant=q0-Z*polynomial[0]
 return abs(lam)**N*to_arb(max(lam,0)*h).exp()*constant.abs_upper()+Z.abs_upper()*(2*to_arb(h)).exp()*derivative_poly(polynomial,N,h)

def compute(arrays,n):
 setup();h=Q(float(arrays['scalar'][0]));m=n-1
 E=box(arrays['scalar'][1],arrays['scalar'][2]);Z=E**2
 A=box(arrays['A_mid'][m],arrays['A_rad'][m]);B=box(arrays['B_mid'][m],arrays['B_rad'][m]);F=[box(x,r) for x,r in zip(arrays['F_mid'][m],arrays['F_rad'][m])]
 lp,lm=2*n-2,-2*n-2;P=[];R=[]
 for j,(wp,wm) in enumerate(weights(n)):
  a=A*to_arb(Q(lm**j,2*factorial(j)));b=B*to_arb(Q(lp**j,2*factorial(j)))
  P.append((a+b)/Z+Z*sum((x*to_arb(w) for x,w in zip(F,wp)),arb(0)))
  R.append((b-a)/Z+Z*sum((x*to_arb(w) for x,w in zip(F,wm)),arb(0)))
 dp=derivative(B/Z,Z,F,lp,-1,23,h);dm=derivative(A/Z,Z,F,lm,1,23,h)
 tail=(dp+dm)*to_arb(h**23/Q(2*factorial(23)));remainders=[]
 for seq in (P,R):remainders.append(tail+sum((seq[j].abs_upper()*to_arb(h**j) for j in range(13,23)),arb(0)))
 return (P,R),remainders


def endpoint_refinement(arrays,n,j,family):
 """Independent fmpq corner calculation with finite-particular weights."""
 setup();assert 1<=n<=261 and 0<=j<=12 and family in ('P','R');idx=n-1
 def rat(x):
  a,b=float(x).as_integer_ratio();return fmpq(a,b)
 def end(m,r):
  mm,rr=rat(m),rat(r);assert rr>=0;return mm-rr,mm+rr
 def hull(weights,boxes):
  lower=upper=fmpq(0)
  for w,(lo,hi) in zip(weights,boxes):
   w=fmpq(w.numerator,w.denominator) if isinstance(w,Q) else fmpq(w)
   lower+=min(w*lo,w*hi);upper+=max(w*lo,w*hi)
  return lower,upper
 e0,e1=end(arrays['scalar'][1],arrays['scalar'][2]);assert e0>0;zz=(e0*e0,e1*e1)
 aa=end(arrays['A_mid'][idx],arrays['A_rad'][idx]);bb=end(arrays['B_mid'][idx],arrays['B_rad'][idx])
 ff=[end(m,r) for m,r in zip(arrays['F_mid'][idx],arrays['F_rad'][idx])]
 lm,lp=-2*n-2,2*n-2
 wa=Q(lm**j,2*factorial(j))*(1 if family=='P' else -1);wb=Q(lp**j,2*factorial(j))
 uu=hull([wa,wb],[aa,bb]);vv=hull(weights(n)[j][0 if family=='P' else 1],ff)
 quot=[u/z for u in uu for z in zz];prod=[v*z for v in vv for z in zz]
 lo,hi=min(quot)+min(prod),max(quot)+max(prod);assert lo<=hi
 a,b=arb(lo),arb(hi);assert a.is_finite() and b.is_finite()
 return tuple((int(m),int(e)) for m,e in (a.lower().man_exp(),b.upper().man_exp()))
