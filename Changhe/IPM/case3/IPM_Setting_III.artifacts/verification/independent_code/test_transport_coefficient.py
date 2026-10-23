"""Exact differentiation and countertest checks for result37."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
x,y,ell,A,a=s.symbols('x y ell A a',real=True)
h=s.Function('h')(x,y);g=s.Function('g')(x,y)
w1=s.Function('w1')(x,y);w2=s.Function('w2')(x,y)
base=w1*s.diff(h,x)+w2*s.diff(h,y)-h-g
D=lambda f:w1*s.diff(f,x)+w2*s.diff(f,y)
d=1-s.diff(w1,x)+w1*s.diff(w2,x)/w2
rhs=d*s.diff(h,x)-s.diff(w2,x)/w2*h+s.diff(g,x)-s.diff(w2,x)/w2*g
check=s.expand(s.diff(base,x)-s.diff(w2,x)/w2*base-(D(s.diff(h,x))-rhs))
assert check==0
checks=['scalar elimination equals differentiated equation minus W2_x/W2 times original']
b=s.Function('b')(x,y)
assert s.simplify((s.diff(w2,x)/w2).subs(w2,y*b).doit()-s.diff(b,x)/b)==0
checks.append('smooth axis quotient identity')
psi=-ell*x*y+(x-1)**2/2
W1=ell*x-s.diff(psi,y);W2=ell*y+s.diff(psi,x)
assert W1==2*ell*x and W2==x-1
assert s.simplify(1-s.diff(W1,x)+W1*s.diff(W2,x)/W2-(1+2*ell/(x-1)))==0
assert s.diff(W1,x)+s.diff(W2,y)==2*ell
checks.append('canonical local stream countertest gives nonzero W and scalar pole')
# General parity-compatible local polynomial source jet.
c20,c02,u30,u12=s.symbols('c20 c02 u30 u12')
b0=1+c20*x*x+c02*y*y;v1=A*x+u30*x**3+u12*x*y*y
expr=1-s.diff(v1,x)+v1*s.diff(b0,x)/b0
assert s.simplify(expr.subs({x:0,y:0})-(1-A))==0
checks.append('source coefficient limit')
# Explicit smooth-angular homogeneous lattice mode used in report-wording audit.
z=s.symbols('z',nonzero=True);i=s.I
sn=lambda n:(z**n-z**(-n))/(2*i)
cs=lambda n:(z**n+z**(-n))/2
dt=lambda f:s.expand(i*z*s.diff(f,z))
deg=s.Rational(3,2);aa=s.Rational(9,4);bb=deg-1
Theta=sn(1);Phi=-sn(2)/(2*(deg+3))
poisson=-dt(dt(Phi))-(deg+1)**2*Phi-deg*cs(1)*Theta+sn(1)*dt(Theta)
transport=(deg*(deg*cs(1)**2+sn(1)**2)-1)*Theta-bb*sn(1)*cs(1)*dt(Theta)+aa*((deg+1)*cs(1)*Phi-sn(1)*dt(Phi))
assert s.expand(poisson)==0 and s.expand(transport)==0
kx=(deg*deg-1)/bb;ky=(aa-deg+1)/bb
assert kx==s.Rational(5,2) and ky==s.Rational(7,2)
checks.append('A=d=3/2,a=9/4,kappa_x=5/2,kappa_y=7/2 admits smooth angular sin(theta) mode')
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':checks,'scope':'Exact identities and a canonical local nonprofile countertest. Uniform far-axis estimates and compact-patch construction are proved in PROOF.md, not inferred from sampling.'}
Path('research/transport_coefficient/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
