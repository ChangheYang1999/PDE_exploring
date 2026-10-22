"""Method A: beta-integral integer weights, midpoint-radius hulls, Arb512."""
from functools import lru_cache
from fractions import Fraction
from math import factorial,comb
from flint import arb,ctx
from common import rational_arb
PRECISION=512;ORDER=20
FACT=[factorial(j) for j in range(23)]

def setup():ctx.prec=PRECISION;ctx.threads=1
def box(mid,rad):
 assert rad>=0
 return arb((int(mid),-1074),(int(rad),-1074))
def integer_hull(weights,mids,radii):
 mid=sum(w*m for w,m in zip(weights,mids));rad=sum(abs(w)*r for w,r in zip(weights,radii))
 return box(mid,rad)

def integral_integer(j,k,lam):
 if j<=k:return 0
 result=0
 for v in range(j-k):result+=(FACT[k+v]//FACT[v])*pow(lam,j-k-1-v)*(1<<v)
 if lam==0:assert result==FACT[j-1]*(1<<(j-k-1))//FACT[j-k-1]
 return result

@lru_cache(maxsize=261)
def weights(n):
 assert 1<=n<=261
 plus,minus=2*n-2,-2*n-2;result=[]
 for j in range(ORDER+1):
  wp=[integral_integer(j,k,plus) for k in range(8)];wm=[integral_integer(j,k,minus) for k in range(8)]
  result.append(((pow(minus,j),pow(plus,j),*[a-b for a,b in zip(wm,wp)]),(-pow(minus,j),pow(plus,j),*[-a-b for a,b in zip(wm,wp)])))
 return tuple(result)

def coefficients(n,em,er,am,ar,bm,br,fm,fr):
 setup();Z=box(em,er)**2
 assert Z.lower()>0
 mids=[am,bm,*fm];rads=[ar,br,*fr];out=[[],[]]
 for j,pair in enumerate(weights(n)):
  for family,w in enumerate(pair):
   U=integer_hull(w[:2],mids[:2],rads[:2]);V=integer_hull(w[2:],mids[2:],rads[2:])
   out[family].append((U/Z+Z*V)/(2*FACT[j]))
 return out

@lru_cache(maxsize=12)
def derivative_weights(width):
 setup();h=rational_arb(width);hp=[h**j for j in range(22)];rows=[]
 for d in range(ORDER+1):
  rows.append(tuple(sum((comb(d,v)*(1<<(d-v))*(FACT[k]//FACT[k-v])*hp[k-v] for v in range(min(d,k)+1)),arb(0)) for k in range(8)))
 return tuple(rows),tuple(hp)

@lru_cache(maxsize=4000)
def remainder_weights(width,n):
 setup();rows,hp=derivative_weights(width);h=hp[1];plus=2*n-2;minus=2*n+2
 ep=(plus*h).exp();e2=(2*h).exp();c=hp[21]/(2*FACT[21])
 a=c*minus**21;b=c*plus**21*ep
 forcing=[]
 for k in range(8):
  value=(plus**21*ep+minus**21)*hp[k+1]
  value+=sum(((plus**(20-d)+minus**(20-d))*rows[d][k] for d in range(21)),arb(0))
  forcing.append(c*e2*value)
 return a,b,tuple(forcing),tuple(hp)

def remainder(n,width,em,er,am,ar,bm,br,fm,fr,coefficients_pair):
 setup();a,b,ff,hp=remainder_weights(width,n)
 lo=arb((em-er,-1074));hi=arb((em+er,-1074));assert lo.lower()>0
 aa=arb((abs(am)+ar,-1074));bb=arb((abs(bm)+br,-1074))
 tail=(a*aa+b*bb)/lo**2+hi**2*sum((w*arb((abs(m)+r,-1074)) for w,m,r in zip(ff,fm,fr)),arb(0))
 assert tail.lower()>=0
 results=[]
 for coefs in coefficients_pair:
  result=tail+sum((coefs[j].abs_upper()*hp[j] for j in range(13,21)),arb(0))
  assert result.is_finite() and result.lower()>=0
  results.append(result)
 return results
