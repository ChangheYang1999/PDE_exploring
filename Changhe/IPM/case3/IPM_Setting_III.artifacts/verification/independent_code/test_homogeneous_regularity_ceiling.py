"""Independent frozen-equation algebra and exceptional-family diagnostics.

No producer code is imported. The analytic distribution and Holder arguments
are in the standalone proof, not certified by these tests.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_hermite,gamma
A,a,d=s.symbols('A a d',positive=True);B=A-1
kx=(A*d-1)/B;py=(a-d+1)/B;u=(d-A)/B;v=(a+2-A*(d+1))/B
checks=[]
for name,expr in [('degree',u+v-a/B+d+2),('vertical exponent',py-d-v-1),('horizontal frequency',u-a/B+1+py),('horizontal exceeds radial',kx-d-(d-1)/B)]:
 assert s.factor(expr)==0;checks.append(name)
xi,eta=s.symbols('xi eta',positive=True)
# Compute the quadrant equation through independent logarithmic derivatives.
logx=u/xi-a*xi/(B*(xi*xi+eta*eta))
logy=v/eta-a*eta/(B*(xi*xi+eta*eta))
assert s.factor(A*xi*logx+eta*logy+A+2+a*xi*xi/(xi*xi+eta*eta))==0
checks.append('quadrant Fourier transport')
n=s.symbols('n',integer=True,nonnegative=True)
assert s.expand(-A*(n+1)+(n-d-1)+(A+2)-(1-d-B*n))==0
checks.append('frequency line highest transverse coefficient')
t=s.symbols('t',positive=True)
ct=s.cos(t);st=s.sin(t);q=A*ct**2+st**2
row=s.Matrix([[(d*q-1)/(B*st*ct),a*(d+1)/(B*st),-a/(B*ct)]])
M=row.col_join(s.Matrix([[0,0,1]])).col_join(st*row+s.Matrix([[-d*ct,-(d+1)**2,0]]))
Rx=s.Matrix([[s.limit(t*M[i,j],t,0,dir='+') for j in range(3)] for i in range(3)])
expectedx=s.Matrix([[kx,a*(d+1)/B,0],[0,0,0],[0,0,0]])
assert all(s.factor(z)==0 for z in Rx-expectedx);checks.append('horizontal residue from coupled angular system')
S=s.diag(1,1,-1);My=-S*M.subs(t,s.pi/2-t)*S
Ry=s.Matrix([[s.limit(t*My[i,j],t,0,dir='+') for j in range(3)] for i in range(3)])
expectedy=s.Matrix([[-(d-1)/B,0,-a/B],[0,0,0],[(d-1)/B,0,a/B]])
assert all(s.factor(z)==0 for z in Ry-expectedy);checks.append('vertical residue from coupled angular system')
z=s.symbols('z')
for name,R,k in [('x',Rx,kx),('y',Ry,py)]:
 assert s.factor((z*s.eye(3)-R).det()-z*z*(z-k))==0
 checks.append(name+' residue spectrum')
assert all(s.factor(z)==0 for z in Ry*s.Matrix([1,0,-1])-py*s.Matrix([1,0,-1]));checks.append('vertical fractional eigenvector')
x,y=s.symbols('x y',positive=True)
for aa,p in [(s.Rational(3,2),s.Rational(1,3)),(2,s.Rational(3,2)),(3,s.Rational(5,2)),(5,s.Rational(9,2))]:
 h=y*x**p;psi=-y*x**(p+1)/(p+1);av=aa*p;dv=p+1
 assert s.simplify(aa*x*s.diff(h,x)+y*s.diff(h,y)-h+av*s.diff(psi,x))==0
 assert s.simplify(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(h,x))==0
 assert s.factor(v.subs({A:aa,a:av,d:dv})+2)==0
 assert s.factor(py.subs({A:aa,a:av,d:dv})-p)==0
 checks.append('physical delta-prime frequency family '+str((aa,p)))
# The positive odd v cancellation example is checked in a complex variable.
z=s.symbols('z',nonzero=True);tt=(z-1)/s.I
f=2*z**s.Rational(3,2)-3*z**s.Rational(1,2)
J=s.I*(2*z**s.Rational(3,2)-s.Rational(4,5)*z**s.Rational(5,2))
g=-(J/2+tt*f)/6
Dt=lambda f:s.I*s.diff(f,z)
assert s.simplify(Dt(J)-f)==0
assert s.simplify(s.Rational(3,2)*f+tt*Dt(f)+6*Dt(g))==0
assert s.simplify((1+tt*tt)*Dt(Dt(g))-5*tt*Dt(g)+s.Rational(35,4)*g+Dt(f))==0
checks.append('positive odd v cancellation physical example')
rows=[]
# Gaussian derivatives have a finite number of vanishing moments; explicit
# cusp tests check the scaling obstruction independently of Fourier inversion.
for p,m in [(.5,2),(1.5,2),(2.5,3),(4.5,4)]:
 exact=2.**m*gamma((p+1)/2)*np.prod([p-2*j for j in range(m)])
 value,error=quad(lambda x:2*x**p*eval_hermite(2*m,x)*np.exp(-x*x),0,12,epsabs=1e-10,epsrel=1e-11,limit=200)
 rel=abs(value-exact)/max(1.,abs(exact));assert rel<2e-10,(p,m,rel)
 assert abs(exact)>1e-4
 rows.append({'p':p,'gaussian_derivative_order':2*m,'pairing_exact':float(exact),'pairing_quad':value,'estimated_error':error,'relative_error':rel})
checks.append('noninteger cusp vanishing-moment pairings')
# The normalized G_v inverse constant at every first four negative-even poles.
for n0 in range(4):
 vv=-2*n0-2
 physical=s.I*2**s.Integer(vv)/(s.sqrt(s.pi)*s.gamma(s.Rational(1-vv,2)))
 delta=s.Rational((-1)**(n0+1)*s.factorial(n0),s.factorial(2*n0+1))*(-s.I)**(2*n0+1)/(2*s.pi)
 assert abs(complex(s.N(physical-delta,30)))<1e-25
 checks.append('exceptional Fourier constant '+str(vv))
root=Path('research/homogeneous_regularity_ceiling/verification');root.mkdir(parents=True,exist_ok=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','count':len(checks),'checks':checks,'cusp_pairings':rows,'scope':'Exact local equations, endpoint residues, exceptional Fourier constants and manufactured cusp testing. Distributional classification, convergent endpoint construction and Holder necessity are proved separately.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
