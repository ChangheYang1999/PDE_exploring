"""Independent exact and direct-kernel tests of SGN2 ingredients.
No producer modules or copied verification code. One sequential CPU worker.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import sympy as S
import numpy as np
from direct_inverse import DirectInverse,Quadrature
x,y,r,t,s,p,a,D,eps=S.symbols('x y r t s p a D eps', real=True)
checks={}
def exact(name,expr):
    value=S.simplify(S.trigsimp(S.expand_trig(expr)))
    assert value==0,(name,value)
    checks[name]='exact zero'
k=S.sin(t)**2*(4*S.sin(t)**2-3)
exact('angular integration by parts',k+S.diff(S.cos(t)*S.sin(t)**3,t))
exact('zero angular mean',S.integrate(S.expand_trig(k),(t,0,S.pi/2)))
exact('positive kernel mass',S.integrate(S.expand_trig(k),(t,S.pi/3,S.pi/2))-3*S.sqrt(3)/16)
exact('cos2 contrast coefficient',S.integrate(S.expand_trig(k*S.cos(2*t)),(t,0,S.pi/2))+S.pi/8)
phi=(3*x*x*y-y**3)/(x*x+y*y)**3
exact('cubic harmonic',S.diff(phi,x,2)+S.diff(phi,y,2))
exact('cubic y derivative',S.diff(phi,y)-3*(x**4-6*x*x*y*y+y**4)/(x*x+y*y)**4)
xx=r*S.cos(t);yy=r*S.sin(t)
expr=(y*(x*S.diff(phi,x)-y*S.diff(phi,y))).subs({x:xx,y:yy},simultaneous=True)
exact('circular singular cancellation',expr+3/r**2*S.sin(t)*S.sin(5*t))
exact('zero circular angular mean',S.integrate(S.sin(t)*S.sin(5*t),(t,0,2*S.pi)))
# The B constraint follows from the actual weighted identity, not an assigned sign.
B=S.symbols('B')
weighted=-D*S.pi*a*(S.Rational(1,4)-s)+a*a*B+S.pi*a*D/2
exact('normalized cubic target',weighted.subs({D:a*s,B:-S.pi*s*(s+S.Rational(1,4))},simultaneous=True))
# General radial stream contraction: angular integration leaves the claimed h' term.
h,hp,F=S.symbols('h hp F',real=True)
U1=x*h+x*y*y*hp/r;U2=-y*h-x*x*y*hp/r
integrand=(y*F*(U1*S.diff(phi,x)+U2*S.diff(phi,y))).subs({x:xx,y:yy},simultaneous=True)*r
angular=S.integrate(S.expand_trig(S.cancel(S.trigsimp(integrand))),(t,0,2*S.pi))
exact('radial B formula',angular-3*S.pi*F*hp/4)
angles=[]
for th,phi_sign,dy_sign in [(S.pi/12,1,1),(S.pi/4,1,-1),(5*S.pi/12,-1,1),(17*S.pi/48,-1,-1)]:
    ph=S.sin(3*th);dy=3*S.cos(4*th)
    assert float(ph)*phi_sign>0 and float(dy)*dy_sign>0
    angles.append({'angle_over_pi':str(th/S.pi),'phi':str(S.simplify(ph)),'phi_y':str(S.simplify(dy))})
# Canonical Gaussian stream, with derivative signs checked directly.
rr=x*x+y*y;H=(1-(1+rr)*S.exp(-rr))/(2*rr**2);psi=-x*y*H;g=y*S.exp(-rr)
exact('Gaussian elliptic equation',-S.diff(psi,x,2)-S.diff(psi,y,2)-S.diff(g,x))
Tg=-S.diff(psi,x);value=S.simplify(Tg.subs({x:2,y:1}))
exact('Gaussian point value',value-(-S.Rational(11,250)+S.Rational(133,125)*S.exp(-5)))
assert float(value)<0
# General compact-potential identities and a trigonometric interior patch.
f=S.Function('f')(x,y);dn=-S.diff(f,x,2)-S.diff(f,y,2);zx=-S.diff(f,x,y);zy=S.diff(f,x,2)
exact('compact potential divergence',S.diff(zx,x)+S.diff(zy,y))
exact('compact potential curl',S.diff(zy,x)-S.diff(zx,y)+S.diff(dn,x))
Th0=a*S.sin(t);ur=a*S.cos(2*t)/(p+3);ut=-a*(p+1)*S.sin(t)*S.cos(t)/(p+3)
exact('required second tail coefficient',(p*ur*Th0+ut*S.diff(Th0,t))/D+a*a/(D*(p+3))*S.sin(t)*(S.cos(t)**2+p*S.sin(t)**2))
# Full-plane cancellation quadrature independently checks the Gaussian velocity.
rows=[]
def gaussian(xx,yy):return np.asarray(yy)*np.exp(-np.asarray(xx)**2-np.asarray(yy)**2)
uxf=S.lambdify((x,y),-S.diff(psi,y),'numpy');uyf=S.lambdify((x,y),S.diff(psi,x),'numpy')
for lev,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
    inv=DirectInverse(gaussian,Quadrature(nr,nt,ne,of,1.,.5,0.,2.));errs=[]
    for xx0,yy0 in [(2.,1.),(-2.,1.),(2.,-1.),(.31,.73),(4.2,.09),(0.,2.3)]:
        u=inv.velocity(xx0,yy0);expected=np.array([uxf(xx0,yy0),uyf(xx0,yy0)],float)
        err=float(np.linalg.norm(u-expected));errs.append(err)
        rows.append({'level':lev,'x':xx0,'y':yy0,'U':u.tolist(),'expected':expected.tolist(),'absolute_error':err})
    assert max(errs)<1e-7,(lev,errs)
    print(json.dumps({'level':lev,'max_absolute_error':max(errs)}),flush=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'angles':angles,'Gaussian_Tg_2_1':str(value),'canonical_quadrature':rows,'scope':'Independent symbolic ingredient checks and real-space full-plane Gaussian tests. The bump IVT construction is justified by the standalone analytic proof; no computed root or exact transport solution is asserted.'}
for name in ['angular_contrast','scalar_constraints_nonprofiles']:
    Path('research',name,'verification','independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'quadrature_rows':len(rows),'utc':result['utc']}),flush=True)
