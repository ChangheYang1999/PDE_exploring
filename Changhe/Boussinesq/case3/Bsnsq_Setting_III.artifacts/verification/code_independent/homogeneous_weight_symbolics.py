"""Own exact algebra for the informal homogeneous-weight audit."""
import sympy as s
import json,datetime
from pathlib import Path
x,y,a,b,G,q,nu,beta,k=s.symbols('x y a b G q nu beta k',real=True,nonzero=True)
r2=x*x+y*y
f=x*y/r2**2; g=s.diff(f,x)
checks={}
def check(name,lhs,rhs):
 z=s.simplify(s.factor(s.together(lhs-rhs)));assert z==0,(name,z);checks[name]=str(z)
check('gx',g,y*(y*y-3*x*x)/r2**3)
check('fy',s.diff(f,y),x*(x*x-3*y*y)/r2**3)
check('degree_f',x*s.diff(f,x)+y*s.diff(f,y),-2*f)
check('degree_g',x*s.diff(g,x)+y*s.diff(g,y),-3*g)
va=G/(4*s.pi*a)-G*a/(s.pi*(a*a+b*b))
npair=2*G*va*s.diff(f,y).subs({x:a,y:b})
target=G**2*(b*b-3*a*a)*(a*a-3*b*b)/(2*s.pi*(a*a+b*b)**4)
check('centered_blob',npair,target)
c=2*G*a*b/(s.pi*(a*a+b*b)**2)
check('diagonal_blob',npair.subs(b,a),s.pi*c.subs(b,a)**2/2)
unc=2*G*(G/(4*s.pi*a))*s.diff(f,y).subs({x:a,y:b})
check('uncentered_sign',unc.subs(b,a),-npair.subs(b,a))
psi=-x*(1+r2)**q
omega=-s.diff(psi,x,2)-s.diff(psi,y,2)
check('tail_source',omega,4*q*x*(1+r2)**(q-2)*(2+(q+1)*r2))
check('tail_center_jet',s.diff(omega,x).subs({x:0,y:0}),8*q)
ux=-s.diff(psi,y);uy=s.diff(psi,x)
check('velocity_divergence',s.diff(ux,x)+s.diff(uy,y),0)
check('velocity_curl',-s.diff(uy,x)+s.diff(ux,y),omega)
check('axis_mixed_sign',(-x*s.diff(g,x)+y*s.diff(g,y)).subs(x,0),-3/y**3)
check('mellin_vorticity_coefficient',1-(2-k)*beta,beta*(k-(2-1/beta)))
check('mellin_temperature_coefficient',(2-k)*beta-2,-beta*(k-(2-2/beta)))
th=s.symbols('th',real=True)
check('center_angular_constant',4*s.integrate(s.cos(th)**2*s.sin(th),(th,0,s.pi/2)),s.Rational(4,3))
root=Path('verification/homogeneous_weights_20261020T2045')
(root/'symbolic_results.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'count':len(checks),'scope':'Exact algebra checks only. Absolute convergence, blob limits, Mellin uniqueness and scope are proved in PROOF.md.'},indent=2)+'\n')
print('PASS',len(checks),'independent exact symbolic checks')
