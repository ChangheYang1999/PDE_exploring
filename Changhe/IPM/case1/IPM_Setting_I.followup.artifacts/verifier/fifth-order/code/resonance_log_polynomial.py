"""Exact resonant coefficient on all R12 radii at A=2.
Independent Laurent-polynomial arithmetic in S=L^2.
"""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
class P:
 def __init__(self,x=0):self.c={0:F(x)} if x else {}
 @classmethod
 def monomial(cls,k,v=1):p=cls();p.c={k:F(v)};return p
 def __add__(x,y):
  y=cp(y);z=P();z.c=x.c.copy()
  for k,v in y.c.items():z.c[k]=z.c.get(k,F(0))+v
  z.c={k:v for k,v in z.c.items() if v};return z
 __radd__=__add__
 def __neg__(x):z=P();z.c={k:-v for k,v in x.c.items()};return z
 def __sub__(x,y):return x+-cp(y)
 def __mul__(x,y):
  y=cp(y);z=P()
  for k,v in x.c.items():
   for j,w in y.c.items():z.c[k+j]=z.c.get(k+j,F(0))+v*w
  z.c={k:v for k,v in z.c.items() if v};return z
 __rmul__=__mul__
 def __truediv__(x,y):return x*F(1,y)
def cp(x):return x if isinstance(x,P) else P(x)
N=16
zero=lambda:[P() for _ in range(N+1)]
def add(*xs):return [sum((x[i] for x in xs),P()) for i in range(N+1)]
def mul(x,y):return [sum((x[j]*y[i-j] for j in range(i+1)),P()) for i in range(N+1)]
def scale(x,s):return [v*s for v in x]
def deriv(x,n=1):
 for _ in range(n):x=[(j+1)*x[j+1] for j in range(N)]+[P()]
 return x
w=zero();g=zero();w[1]=P(-2)
for m in range(1,8):w[2*m+1]=P.monomial(-m,4*(-1)**(m+1))
for m in range(1,9):g[2*m]=P.monomial(1-m,(-1)**(m-1))
h=scale(deriv(w),-1);h[0]+=3
ap=scale(add(deriv(g),scale(deriv(w,2),-1)),F(1,2));bp=scale(deriv(ap),-F(1,3))
f3=scale(add(mul(ap,deriv(g)),mul(bp,g)),-1);k3=scale(h,3);k3[0]-=1
G3=zero()
for m in range(7):
 n=2*m;lower=add(mul(w,deriv(G3)),mul(k3,G3))[n];G3[n]=(f3[n]-lower)/(14-2*n)
a4=scale(add(deriv(G3),deriv(bp)),F(1,4));b5=scale(deriv(a4),-F(1,5))
f5=scale(add(mul(ap,deriv(G3)),scale(mul(bp,G3),3),mul(a4,deriv(g)),mul(b5,g)),-1)
from math import comb
plus=zero();minus=zero()
for m in range(7):plus[2*m]=P.monomial(-m,comb(6,m))
minus[0]=P(1);minus[2]=P.monomial(-1,-1)
E=scale(mul(mul(f5,plus),minus),F(1,2))[12]
import sympy as s
S=s.symbols('S');expr=sum(s.Rational(v.numerator,v.denominator)*S**k for k,v in E.c.items());fac=s.factor(expr)
out={'E12_minus_F_over_wH':str(fac),'positive_roots':[str(r) for r in s.solve(expr,S) if r.is_positive]}
print(out);Path('verifier/fifth-order/verification/resonance_log_polynomial.json').write_text(json.dumps(out,indent=2)+'\n')
