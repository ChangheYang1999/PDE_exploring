"""Directed Taylor-Bernstein products on a radial cell; no acceptance policy."""
from fractions import Fraction as F
from math import comb,factorial
from flint import arb,arb_mat
from matrix import aa

def magnitude(entries):
 value=arb(0)
 for v in entries:value=value.max(abs(v))
 return value.upper()

def ranges(B,labels,branches,delta,tl,th,power_offset=0,N=4):
 if th==1:return None
 n=next(iter(B.values())).nrows()-1;nz=next(iter(B.values())).ncols()-1
 width=aa(th-tl);left=1-aa(tl);right=1-aa(th);multipliers={};errors={}
 for j in branches:
  q=(j+power_offset)*delta/2;fall=F(1);power=[]
  for l in range(N+1):
   if l:fall*=q-(l-1)
   power.append(aa((-1)**l*fall/F(factorial(l)))*width**l*left**aa(q-l))
  bern=[sum((aa(F(comb(i,l),comb(N,l)))*power[l] for l in range(i+1)),arb(0)) for i in range(N+1)]
  fall*=q-N
  errors[j]=aa(abs(fall)/factorial(N+1))*width**(N+1)*right**aa(q-N-1)
  M=arb_mat(n+N+1,n+1)
  for i in range(n+1):
   for l in range(N+1):M[i+l,i]=aa(F(comb(n,i)*comb(N,l),comb(n+N,i+l)))*bern[l]
  multipliers[j]=M
 out={}
 for label in labels:
  total=arb_mat(n+N+1,nz+1);error=arb(0)
  for j in branches:
   total+=multipliers[j]*B[label,j]
   error+=errors[j]*magnitude(B[label,j].entries())
  vals=total.entries();low=vals[0];high=vals[0]
  for v in vals[1:]:low=low.min(v);high=high.max(v)
  out[label]=((low-error).lower(),(high+error).upper())
 return out
