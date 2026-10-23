"""Exact finite-field arithmetic, explicit Bezout witness, and rational gcd certificate."""
from math import isqrt
from exact_degree21 import prim,divexact,univ

def trim(a):
 while a and a[-1]==0:a.pop()
 return a

def add(a,b,p,sgn=1):
 r=[0]*max(len(a),len(b))
 for i in range(len(r)):r[i]=((a[i]if i<len(a)else 0)+sgn*(b[i]if i<len(b)else 0))%p
 return trim(r)

def mul(a,b,p):
 r=[0]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%p
 return trim(r)

def divide(a,b,p):
 assert b
 r=trim([v%p for v in a]);q=[0]*max(0,len(r)-len(b)+1);inv=pow(b[-1],-1,p)
 while len(r)>=len(b):
  j=len(r)-len(b);c=r[-1]*inv%p;q[j]=c
  for i,v in enumerate(b):r[j+i]=(r[j+i]-c*v)%p
  trim(r)
 return trim(q),r

def certify(F,G,D):
 D=prim(D);A=prim(divexact(F,D));B=prim(divexact(G,D));aa,bb=univ(A),univ(B)
 for p in [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211]:
  assert p>1 and all(p%d for d in range(2,isqrt(p)+1))
  if aa[-1]%p==0 or bb[-1]%p==0:continue
  a,b=[v%p for v in aa],[v%p for v in bb];r0,r1=a[:],b[:];s0,s1=[1],[];t0,t1=[],[1];steps=0
  while r1:
   q,r=divide(r0,r1,p);assert add(mul(q,r1,p),r,p)==r0
   r0,r1=r1,r;s0,s1=s1,add(s0,mul(q,s1,p),p,-1);t0,t1=t1,add(t0,mul(q,t1,p),p,-1);steps+=1
  if len(r0)!=1:continue
  inv=pow(r0[0],-1,p);s=[v*inv%p for v in s0];t=[v*inv%p for v in t0]
  assert add(mul(s,a,p),mul(t,b,p),p)==[1]
  return dict(prime=p,cofactor_degrees=[len(a)-1,len(b)-1],s=s,t=t,steps=steps,identity_verified=True,leading_degrees_preserved=True,exact_divisions_verified=True)
 raise ArithmeticError('No coprime degree-preserving prime found; rational gcd unconfirmed')
