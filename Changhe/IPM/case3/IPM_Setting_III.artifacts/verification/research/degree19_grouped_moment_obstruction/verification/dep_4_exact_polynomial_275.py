"""Result275 library, copied from our independently written Result267 verifier.
Pure Python exact sparse polynomial and integer determinant arithmetic.
No symbolic algebra system or producer routine is imported.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import gcd,lcm,comb
import json,hashlib
R=Path('research/degree17_grouped_moment_obstruction');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
class P:
 def __init__(self,terms=None,dim=2):
  self.d=dim;self.a={tuple(k):F(v)for k,v in (terms or {}).items()if v}
 @classmethod
 def var(cls,index,dim=2):
  k=[0]*dim;k[index]=1;return cls({tuple(k):1},dim)
 def cast(self,x):
  if isinstance(x,P):assert x.d==self.d;return x
  return P({(0,)*self.d:x},self.d)
 def __add__(self,other):
  other=self.cast(other);a=self.a.copy()
  for k,v in other.a.items():a[k]=a.get(k,F(0))+v
  return P(a,self.d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.a.items()},self.d)
 def __sub__(self,other):return self+-self.cast(other)
 def __rsub__(self,other):return self.cast(other)+-self
 def __mul__(self,other):
  other=self.cast(other);a={}
  for x,u in self.a.items():
   for y,v in other.a.items():
    k=tuple(i+j for i,j in zip(x,y));a[k]=a.get(k,F(0))+u*v
  return P(a,self.d)
 __rmul__=__mul__
 def __pow__(self,k):
  assert isinstance(k,int)and k>=0
  out=self.cast(1);b=self
  while k:
   if k%2:out=out*b
   b=b*b;k//=2
  return out
 def __eq__(self,other):return self.a==self.cast(other).a
 def degree(self,i):return max((k[i]for k in self.a),default=-1)
 def evaluate(self,values):
  out=F(0)
  for k,c in self.a.items():
   a=c
   for n,v in zip(k,values):a*=F(v)**n
   out+=a
  return out
 def primitive(self):
  den=1
  for v in self.a.values():den=lcm(den,v.denominator)
  a={k:int(v*den)for k,v in self.a.items()};content=0
  for v in a.values():content=gcd(content,v)
  sign=1 if a[max(a)]>0 else -1
  return P({k:v//content*sign for k,v in a.items()},self.d),F(content*sign,den)
 def specialize(self,value,degree):
  a=[F(0)]*(degree+1)
  for (i,j),c in self.a.items():a[degree-i]+=c*F(value)**j
  return [v.numerator if v.denominator==1 else v for v in a]
def stored(rows):return P({tuple(t['powers']):int(t['coefficient'])for t in rows})
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def peval(a,x):
 y=0
 for v in reversed(a):y=y*x+v
 return y
def sylvester(a,b):
 da,db=len(a)-1,len(b)-1;out=[]
 for i in range(db):out.append([0]*i+a+[0]*(db-1-i))
 for i in range(da):out.append([0]*i+b+[0]*(da-1-i))
 assert all(len(row)==da+db for row in out)
 return out
def bareiss(matrix):
 a=[row[:]for row in matrix];old=1;sign=1;divisions=0;swaps=0
 for k in range(len(a)-1):
  pivot=next((i for i in range(k,len(a))if a[i][k]),None)
  if pivot is None:return 0,divisions,swaps
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign;swaps+=1
  d=a[k][k]
  for i in range(k+1,len(a)):
   for j in range(k+1,len(a)):
    v,r=divmod(a[i][j]*d-a[i][k]*a[k][j],old)
    if r:raise ArithmeticError('Nonexact Bareiss division')
    a[i][j]=v;divisions+=1
   a[i][k]=0
  old=d
 return sign*a[-1][-1],divisions,swaps
def gaussian(matrix):
 a=[[F(x)for x in row]for row in matrix];det=F(1)
 for k in range(len(a)):
  row=next((i for i in range(k,len(a))if a[i][k]),None)
  if row is None:return F(0)
  if row!=k:a[row],a[k]=a[k],a[row];det=-det
  pivot=a[k][k];det*=pivot
  for j in range(k,len(a)):a[k][j]/=pivot
  for i in range(k+1,len(a)):
   c=a[i][k]
   for j in range(k,len(a)):a[i][j]-=c*a[k][j]
 return det
