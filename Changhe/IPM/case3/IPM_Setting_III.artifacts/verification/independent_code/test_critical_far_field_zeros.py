"""Exact checks of the formulas in result 42, independent of teammate code."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,ell,kap=s.symbols('x y ell kap',real=True,positive=True)
A=2*ell-1
psi=(ell*x-A*s.sin(kap*x)/kap)*y
rho=A*(1+s.cos(kap*x))*y
U=s.Matrix([-s.diff(psi,y),s.diff(psi,x)])
W=ell*s.Matrix([x,y])+U
checks=[]
def check(name,expr):
    out=s.trigsimp(s.simplify(expr))
    assert out==0,(name,out)
    checks.append(name)
check('model divergence',s.diff(W[0],x)+s.diff(W[1],y)-2*ell)
check('model curl',s.diff(W[1],x)-s.diff(W[0],y)+s.diff(rho,x))
check('model Poisson',-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(rho,x))
check('model transport',W.dot(s.Matrix([s.diff(rho,x),s.diff(rho,y)]))-rho)
check('model origin strain',s.diff(psi,x,y).subs({x:0,y:0})-(1-ell))
check('model origin slope',s.diff(rho,y).subs({x:0,y:0})-2*A)
check('model saddle wprime',s.diff(W[0],x).subs(x,s.pi/kap)+A)
check('model saddle second g coefficient',s.diff(rho,x,2,y).subs(x,s.pi/kap)/2-A*kap**2/2)
check('axis ODE in model',W[0]*s.diff(rho,x,y)-(s.diff(W[0],x)-A)*s.diff(rho,y))
for k in range(2,9):
    for j in range(1,k):
        mu=(2*k*ell-1)/(k-j);lam=(1-2*j*ell)/(k-j)
        check(f'resonance trace {k},{j}',mu+lam-2*ell)
        check(f'resonance equation {k},{j}',j*mu+k*lam-1)
        check(f'transverse exponent {k},{j}',(1-k*lam)/mu-j)
for m in range(2,10):
    lam=-A/(m-1);mu=2*ell-lam
    check(f'axis m exponent {m}',(1-m*lam)/mu-1)
    for i in range(1,m):
        # Strict upper bound follows because mu-(1-i lambda)=(m-i)(-lambda)>0.
        check(f'axis lower order gap {m},{i}',mu-(1-i*lam)-(m-i)*(-lam))
b11,b12,b21,th=s.symbols('b11 b12 b21 th',real=True)
B=s.Matrix([[b11,b12],[b21,2*ell-b11]])
T=s.Matrix([s.cos(th),s.sin(th)]);N=s.Matrix([-s.sin(th),s.cos(th)])
check('nodal normal exponent',1-(N.T*B*N)[0]-(T.T*B*T)[0]+A)
root=Path('research/critical_far_field_zeros/verification');root.mkdir(parents=True,exist_ok=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_check_count':len(checks),'checks':checks,'scope':'Exact algebra supports, but does not replace, the separate full analytic proof. Periodic example deliberately violates sublinear growth and canonical sublinear gauge.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
