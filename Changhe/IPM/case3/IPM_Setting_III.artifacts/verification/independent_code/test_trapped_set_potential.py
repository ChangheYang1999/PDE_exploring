"""Independent exact algebra for the potential/axis mechanisms in result38.

These finite tests do not replace the compact-set or invariant-manifold proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,ell,m=s.symbols('x y ell m',real=True)
r2=x*x+y*y
phi=s.Rational(1,2)*y*s.exp(-r2)*(1+10*x**4)
psi=s.diff(phi,x);rho=-s.diff(phi,x,2)-s.diff(phi,y,2)
W=s.Matrix([ell*x-s.diff(psi,y),ell*y+s.diff(psi,x)])
P=ell*r2/2-s.diff(phi,y)+s.Rational(1,2)
checks=[]
assert s.simplify(s.diff(P,x)-W[0])==0
assert s.simplify(s.diff(P,y)-W[1]-rho)==0
checks.append('explicit canonical potential gradient for independent rapidly decaying stream manufacture')
assert s.simplify(s.diff(W[0],x)+s.diff(W[1],y)-2*ell)==0
assert s.simplify(s.diff(W[1],x)-s.diff(W[0],y)+s.diff(rho,x))==0
assert s.simplify((s.diff(P,x)*W[0]+s.diff(P,y)*W[1])-W.dot(W)-rho*W[1])==0
checks.append('divergence, curl and potential transport derivative identities')
origin={x:0,y:0,ell:2}
assert s.diff(rho,y).subs(origin)==4
assert s.diff(psi,x,y).subs(origin)==-1
assert W.jacobian([x,y]).subs(origin)==s.diag(3,1)
assert s.hessian(P,[x,y]).subs(origin)==s.diag(3,5)
checks.append('origin slope4, strain-1, source(3,1), potential Hessian(3,5)')
w=W[0].subs({y:0,ell:2});g=s.diff(rho,y).subs(y,0)
axisfailure=s.simplify((w*s.diff(g,x)-(s.diff(w,x)-3)*g).subs(x,1))
assert s.simplify(axisfailure-(346*s.exp(-1)-1746*s.exp(-2)))==0
assert axisfailure!=0
checks.append('manufactured field is explicitly not a transport profile; no false counterexample')
A=2*ell-1;lam=-A/(m-1);beta=2*ell-lam
assert s.simplify(m*lam+beta-1)==0
assert s.simplify(beta-(2*ell+A/(m-1)))==0
checks.append('first-axis saddle resonance and fast vertical eigenvalue algebra')
# A trace-positive symmetric critical linearization has at least one eigenvalue >1,
# while the axis maximum argument distinguishes the positive horizontal curvature.
bx=s.symbols('bx',real=True)
assert s.diff(bx*x*x/2+(2*ell-bx)*y*y/2,x,2)==bx
assert s.diff(bx*x*x/2+(2*ell-bx)*y*y/2,y,2)==2*ell-bx
checks.append('axis potential Hessian entries used in the maximum contradiction')
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':checks,
 'scope':'Exact algebra only. The compact connected trapped-set maximum argument and fast unstable manifold proof are analytic and must be independently reviewed.'}
Path('research/trapped_set_potential/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
