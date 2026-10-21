"""Exact first parameter jets of the resonant x^12 forcing coefficient.
Fraction arithmetic and power-series recursion, independent of lead code.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
class D:
 def __init__(self,v=0,a=0,b=0):self.v,self.a,self.b=map(Q,(v,a,b))
 def __add__(x,y):
  y=cv(y);return D(x.v+y.v,x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return D(-x.v,-x.a,-x.b)
 def __sub__(x,y):return x+-cv(y)
 def __rsub__(x,y):return cv(y)+-x
 def __mul__(x,y):
  y=cv(y);return D(x.v*y.v,x.a*y.v+x.v*y.a,x.b*y.v+x.v*y.b)
 __rmul__=__mul__
 def inv(x):return D(1/x.v,-x.a/x.v**2,-x.b/x.v**2)
 def __truediv__(x,y):return x*cv(y).inv()
 def __rtruediv__(x,y):return cv(y)*x.inv()
 def __pow__(x,n):
  if n<0:return x.inv()**(-n)
  out=D(1)
  for _ in range(n):out=out*x
  return out
 def result(x):return {'value':str(x.v),'dA':str(x.a),'dS':str(x.b)}
def cv(x):return x if isinstance(x,D) else D(x)
N=16
zero=lambda:[D() for _ in range(N+1)]
def add(*xs):return [sum((x[i] for x in xs),D()) for i in range(N+1)]
def mul(x,y):return [sum((x[j]*y[i-j] for j in range(i+1)),D()) for i in range(N+1)]
def scale(x,s):return [v*s for v in x]
def deriv(x,n=1):
 for _ in range(n):x=[(j+1)*x[j+1] for j in range(N)]+[D()]
 return x
A=D(2,1,0);S=D(4,0,1);w=zero();g=zero()
w[1]=-A
for m in range(1,8):w[2*m+1]=2*A*(-1)**(m+1)/S**m
for m in range(1,9):g[2*m]=(-1)**(m-1)/S**(m-1)
h=scale(deriv(w),-1);h[0]+=A+1
ap=scale(add(deriv(g),scale(deriv(w,2),-1)),Q(1,2))
bp=scale(deriv(ap),-Q(1,3))
f3=scale(add(mul(ap,deriv(g)),mul(bp,g)),-1)
k3=scale(h,3);k3[0]-=1
G3=zero()
for m in range(0,7):
 n=2*m
 lower=add(mul(w,deriv(G3)),mul(k3,G3))[n]
 G3[n]=(f3[n]-lower)/(k3[0]+w[1]*n)
a4=scale(add(deriv(G3),deriv(bp)),Q(1,4));b5=scale(deriv(a4),-Q(1,5))
f5=scale(add(mul(ap,deriv(G3)),scale(mul(bp,G3),3),mul(a4,deriv(g)),mul(b5,g)),-1)
q=4/A
plus=zero();minus=zero();choose=D(1)
from math import comb
for m in range(7):plus[2*m]=comb(6,m)/S**m
for m in range(9):
 if m:choose=choose*(q-m)/m
 minus[2*m]=choose*(-1)**m/S**m
E=scale(mul(mul(f5,plus),minus),1/A)[12]
assert E.v==0
sprime=Q(46,15);bres=Q(11,1474560)
curve_jump=E.a+sprime*E.b
assert curve_jump==-2*bres,(curve_jump,bres)
out={'E12':E.result(),'Sprime':str(sprime),'resonant_B5':str(bres),
 'curve_jump':str(curve_jump),'curve_limit':str(bres+curve_jump),
 'fixed_S_jump':str(E.a),'fixed_S_limit':str(bres+E.a),
 'limit_formula':'B5_res + dA_E12 + lambda*dS_E12 for S=4+lambda*(A-2)+o(A-2)',
 'G3_even_coefficients_through12':[c.result() for c in G3[::2][:7]]}
Path('verifier/fifth-order/verification/resonance_path.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
