"""Independent vector-adjoint and finite-integral controls for packet140.
No teammate code or model-produced code is imported. All computation is local.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,sys
import sympy as s
import numpy as np
start=time.monotonic();root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
x,y,b,a=s.symbols('x y beta a0',real=True);lam=(b-2)/2;mu=1+3*b/2;q=4*a/b
W=s.Matrix([lam*x,mu*y-q*x*x/2]);om=q*x;theta=a*x*x
xy=(x,y)
def grad(f):return s.Matrix([s.diff(f,z) for z in xy])
def perp(f):return s.Matrix([-s.diff(f,y),s.diff(f,x)])
def curl(v):return s.diff(v[1],x)-s.diff(v[0],y)
def adv(f):return W.dot(grad(f))
def lap(f):return s.diff(f,x,2)+s.diff(f,y,2)
def formal(p):
 f=-adv(p)+(1-2*b)*p
 B=p*grad(om)+perp(f)
 D=s.Matrix([adv(v) for v in B])+2*b*B+W.jacobian(xy).T*B+s.diff(p,x)*grad(theta)
 return s.cancel(curl(D))
tests=[]
def check(name,expr):
 e=s.cancel(expr);assert e==0,(name,e);tests.append({'name':name,'passed':True})
eta=s.Function('eta')(x,y);h=perp(eta)
dW=h.jacobian(xy)*W-W.jacobian(xy)*h
dOm=-curl(dW);dTheta=-h.dot(grad(theta))
dR=s.expand(dW.dot(grad(om))+adv(dOm)+dOm-s.diff(dTheta,x))
check('divergence-preserving infinitesimal field',s.diff(dW[0],x)+s.diff(dW[1],y))
check('linearized thermal equation',dW.dot(grad(theta))+adv(dTheta)-(b-2)*dTheta)
check('polynomial patch thermal',adv(theta)-(b-2)*theta)
check('polynomial patch vorticity',adv(om)+om-s.diff(theta,x))
p=x*y/(x*x+y*y)**2
check('weight harmonic away from0',lap(p))
Ap=formal(p)
H=2*(lam-mu)*s.diff(p,x,2)-2*q*x*s.diff(p,x,y)
check('scalar form derived from vector adjoint',Ap+adv(H)+4*b*H+2*a*x*s.diff(p,x,y))
check('axis coefficient',Ap.subs(y,0)+3*q*(17*b+28)/(2*x**3))
check('adjoint parity',Ap.subs(x,-x)+Ap)
# A separate direct integration check substitutes an explicit compact C^7 bump.
# Its zero extension has enough regularity for all displayed integration by parts.
# The theorem uses a C-infinity bump, whose existence does not need quadrature.
v=(1-((x-1)/s.Rational(1,6))**2)**8*(1-(y/s.Rational(1,7))**2)**8
rows=[]
for bb in [s.Rational(9,4),s.Rational(3),s.Rational(7,2)]:
 pars={b:bb,a:s.Rational(1)}
 dd=dR.subs(eta,v).doit().subs(pars)
 u,z=s.symbols('u z')
 local={x:1+u/6,y:z/7}
 dd=dd.subs(local)
 # Use generated Python/Numpy arithmetic only, with no numerical inverse or fit code.
 left=s.lambdify((u,z),p.subs(local)*dd,'numpy',cse=True)
 right=s.lambdify((x,y),v*Ap.subs(pars),'numpy',cse=True)
 vals=[]
 for n in [24,40,64]:
  z,w=np.polynomial.legendre.leggauss(n)
  X=1+z[:,None]/6;Y=z[None,:]/7;weight=w[:,None]*w[None,:]/42
  # The reflected bump contributes the same integral by parity.
  L=2*float(np.sum(weight*left(z[:,None],z[None,:])));R=2*float(np.sum(weight*right(X,Y)))
  err=abs(L-R);rel=err/max(abs(R),1e-30)
  vals.append({'order':n,'integral_p_deltaR':L,'integral_eta_Ap':R,'absolute_error':err,'relative_error':rel})
 assert vals[-1]['integral_eta_Ap']<0
 # The earlier monomial expansion failed from catastrophic cancellation.
 # This evaluation retains the bump factors in their native local coordinates.
 assert vals[-1]['relative_error']<2e-7,vals
 rows.append({'beta':str(bb),'quadrature':vals})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_count':len(tests),'exact_tests':tests,'finite_integral_controls':rows,'scope':'Exact vector/product-rule identities and numerical compact C7 controls. The smooth deformation theorem is established by the standalone proof, not numerical sampling.'}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_count':len(tests),'seconds':out['elapsed_seconds'],'quad_max_relative':max(v['relative_error'] for r in rows for v in r['quadrature'])}),flush=True)
