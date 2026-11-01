"""Small rational Sturm and finite-field certificate helpers with no import-time work."""
from fractions import Fraction as F
from math import gcd,lcm,isqrt

def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a

def evaluate(a,x):
 v=0
 for c in reversed(a):v=v*x+c
 return v

def primitive(a):
 a=trim(a)
 if not a:return []
 den=lcm(*(v.denominator for v in a));b=[int(v*den) for v in a];content=gcd(*b)
 return [v//abs(content) for v in b]

def remainder(a,b):
 a=[F(v) for v in a];b=[F(v) for v in b]
 while len(a)>=len(b):
  q=a[-1]/b[-1];s=len(a)-len(b)
  for j,c in enumerate(b):a[s+j]-=q*c
  a=trim(a)
 return a

def sturm(a):
 a=primitive(list(map(F,a)));seq=[a,primitive([F(j*a[j]) for j in range(1,len(a))])]
 while seq[-1]:
  r=primitive([-v for v in remainder(seq[-2],seq[-1])])
  if not r:break
  seq.append(r)
 return seq

def sign(v):return (v>0)-(v<0)
def variations(signs):
 a=[s for s in signs if s];return sum(x!=y for x,y in zip(a,a[1:]))
def sturm_finite(seq,x):return variations([sign(evaluate(a,x)) for a in seq])
def sturm_infinity(seq,negative):return variations([sign(a[-1])*(-1 if negative and (len(a)-1)%2 else 1) for a in seq])

def modtrim(a,p):return trim([int(v)%p for v in a])
def modrem(a,b,p):
 a=modtrim(a,p);b=modtrim(b,p);inv=pow(b[-1],-1,p)
 while len(a)>=len(b):
  q=a[-1]*inv%p;s=len(a)-len(b)
  for j,c in enumerate(b):a[s+j]=(a[s+j]-q*c)%p
  a=trim(a)
 return a

def modmul(a,b,p):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c)
def modpow(a,n,f,p):
 out=[1]
 while n:
  if n%2:out=modrem(modmul(out,a,p),f,p)
  a=modrem(modmul(a,a,p),f,p);n//=2
 return out

def modsub(a,b,p):return modtrim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)
def modgcd(a,b,p):
 while b:a,b=b,modrem(a,b,p)
 return modtrim([v*pow(a[-1],-1,p) for v in a],p)
def isprime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def irreducibility_certificate(a,p):
 assert isprime(p);a=modtrim(a,p);a=modtrim([v*pow(a[-1],-1,p) for v in a],p);degree=len(a)-1;assert degree>=1
 tests={degree//q for q in range(2,degree+1) if degree%q==0 and isprime(q)};h=[0,1];rows=[]
 for j in range(1,degree+1):
  h=modpow(h,p,a,p)
  if j in tests:
   g=modgcd(a,modsub(h,[0,1],p),p);assert g==[1];rows.append(dict(frobenius_order=j,gcd=g))
 final=modrem(modsub(h,[0,1],p),a,p);assert not final
 return dict(prime=p,degree=degree,monic_coefficients_ascending=a,gcd_checks=rows,final_frobenius_remainder=final)
