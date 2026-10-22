"""Independent exact and Cartesian full-plane pressure controls for packet157.

No fitting-lane imports. The physical-space pressure inverse uses the
verifier-owned Cartesian Duffy implementation, followed by centered differences.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time, hashlib
import numpy as np
import sympy as sp
from cartesian_inverse import CartesianInverse, InverseSettings

root=Path(sys.argv[1]); inputs=json.loads((root/'inputs.json').read_text())
start=time.monotonic()
report={'started_utc':datetime.now(timezone.utc).isoformat(),'exact_checks':[], 'inverse_cases':[],
        'scope':'Analytic Gaussian data only. Cartesian whole-plane pressure inverse and finite differences are independent controls, not interval certificates or B2 profile checks.'}

def exact(name, expr):
    v=sp.simplify(expr)
    report['exact_checks'].append({'name':name,'difference':str(v),'pass':v==0})
    if v!=0:
        report['status']='FAIL_EXACT'; save(); raise AssertionError((name,v))

def save():
    report['ended_utc']=datetime.now(timezone.utc).isoformat()
    report['elapsed_seconds']=time.monotonic()-start
    report['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['inputs_sha256']=hashlib.sha256((root/'inputs.json').read_bytes()).hexdigest()
    report['proof_sha256']=hashlib.sha256(Path(inputs['proof']).read_bytes()).hexdigest()
    (root/'results.json').write_text(json.dumps(report,indent=2)+'\n')

x,z=sp.symbols('x z',real=True)
a,b,alpha,gamma,mu,lam=sp.symbols('a b alpha gamma mu lam',positive=True)
S=x*z*sp.exp(-a*x*x-b*z*z)
H=sp.hessian(S,(x,z)); determinant=sp.expand(H.det()*sp.exp(2*a*x*x+2*b*z*z))
poly=-1+4*a*x*x+4*b*z*z-4*a*a*x**4-4*b*b*z**4+20*a*b*x*x*z*z-8*a*a*b*x**4*z*z-8*a*b*b*x*x*z**4
exact('Gaussian Hessian determinant',determinant-poly)
U=sp.Matrix([-sp.diff(S,z),sp.diff(S,x)])
DU=U.jacobian([x,z])
exact('Euler pressure source',sp.trace(DU*DU)+2*H.det())
exact('determinant divergence',sp.diff(sp.diff(S,x)*sp.diff(S,z,2),x)-sp.diff(sp.diff(S,x)*sp.diff(S,x,z),z)-H.det())
exact('center v',sp.diff(S,z,x).subs({x:0,z:0})-1)
exact('center g',sp.diff(S,x,z).subs({x:0,z:0})-1)
# Gaussian product integrals prove zero mass without differentiating numerically.
def gaussian_integral_1d(k,coef):
    if k%2: return sp.Integer(0)
    n=k//2
    return sp.gamma(sp.Rational(2*n+1,2))/coef**sp.Rational(2*n+1,2)
mass=0
for (i,j),coef in sp.Poly(poly,x,z).terms():
    mass+=coef*gaussian_integral_1d(i,2*a)*gaussian_integral_1d(j,2*b)
exact('pressure source integral zero',mass)
# The singular constant was subtracted before radial integration.
c,d,A=sp.symbols('c d A',real=True)
quartic=-4*a*a*c**4-4*b*b*d**4+20*a*b*c*c*d*d
sixth=-8*a*b*c*c*d*d*(a*c*c+b*d*d)
exact('quartic radial factor',quartic-(-4*(a*c*c+b*d*d)**2+28*a*b*c*c*d*d))
exact('radial polynomial sum',(4*A)/(4*A)+(-4*A*A+28*a*b*c*c*d*d)/(8*A*A)+(-8*a*b*c*c*d*d*A)/(8*A**3)-(sp.Rational(1,2)+sp.Rational(5,2)*a*b*c*c*d*d/(A*A)))
q=sp.symbols('q',real=True)
pa=a/(a-b)**2; pb=-1/(a-b); pc=-a*b/(a-b)**2
exact('angular partial fraction',q*q/((1+q*q)**2*(a+b*q*q))-(pa/(1+q*q)+pb/(1+q*q)**2+pc/(a+b*q*q)))
partial=4*(pa*sp.pi/2+pb*sp.pi/4+pc*sp.pi/(2*sp.sqrt(a*b)))
exact('angular I formula',partial.subs({a:alpha**2,b:gamma**2})-sp.pi/(alpha+gamma)**2)
I=sp.pi/(sp.sqrt(a)+sp.sqrt(b))**2
J=-sp.diff(I,a)+sp.diff(I,b)
J_formula=sp.pi*(gamma-alpha)/(alpha*gamma*(alpha+gamma)**3)
exact('angular differentiated formula',J.subs({a:alpha**2,b:gamma**2})-J_formula)
t=(alpha-gamma)/(alpha+gamma)
Q=t*(2-5*alpha*gamma/(alpha+gamma)**2)
exact('Q final expression',2*t+5*alpha**2*gamma**2/sp.pi*J_formula-Q)
exact('Q a4 b1',Q.subs({alpha:2,gamma:1})-sp.Rational(8,27))
exact('Q isotropic',Q.subs(gamma,alpha))
exact('Q width reversal',Q+Q.xreplace({alpha:gamma,gamma:alpha}))
y=sp.symbols('y',real=True)
Psi=sp.sqrt(mu)*S.subs(z,y/sp.sqrt(mu))
exact('anisotropic Hessian determinant',sp.det(sp.hessian(Psi,(x,y)))-H.det().subs(z,y/sp.sqrt(mu)))
pi_xx=-1-Q/2;pi_yy=(-1+Q/2)/mu
exact('anisotropic pressure trace',pi_xx+mu*pi_yy+2)
exact('apex v derivative',1+pi_xx+Q/2)
exact('apex g derivative',-1-mu*pi_yy+Q/2)
exact('correct full apex equation',(mu+1)*(-Q/2)-((mu-1)-mu*(pi_yy-pi_xx)))
exact('specified pressure anisotropy',(pi_yy-pi_xx).subs({alpha:2,gamma:1,mu:3})-sp.Rational(70,81))
exact('specified actual derivative',(-Q/(2*lam)).subs({alpha:2,gamma:1,lam:2})+sp.Rational(2,27))
exact('specified claimed derivative',((mu-1)/((mu+1)*lam)).subs({mu:3,lam:2})-sp.Rational(1,4))
for aval,bval in inputs['widths']:
    aa,bb=float(aval),float(bval)
    al,ga=np.sqrt(aa),np.sqrt(bb)
    expected=((al-ga)/(al+ga))*(2-5*al*ga/(al+ga)**2)
    target=np.array([-1-expected/2,-1+expected/2,expected])
    def omega(xx,zz):
        ex=np.exp(-2*aa*xx*xx-2*bb*zz*zz)
        # This source is the negative of Delta pressure, obtained by a
        # direct determinant of the independently differentiated Hessian.
        sxx=2*aa*xx*zz*(2*aa*xx*xx-3)
        szz=2*bb*xx*zz*(2*bb*zz*zz-3)
        sxz=(1-2*aa*xx*xx)*(1-2*bb*zz*zz)
        return -2*ex*(sxx*szz-sxz*sxz)
    for rad in inputs['square_radii']:
        for order in inputs['quadrature_orders']:
            inv=CartesianInverse(omega,InverseSettings(radius=float(rad),core_radial_order=int(order),core_angular_order=int(order)*2,exterior_radial_order=int(order)*2,exterior_angular_order=int(order)*2,decay_power=1.0))
            rows=[]
            for h in inputs['difference_steps']:
                h=float(h)
                vv=inv.relative([[h,0],[-h,0],[0,h],[0,-h]])
                pxx=(vv[0,1]-vv[1,1])/(2*h)
                pzz=-(vv[2,0]-vv[3,0])/(2*h)
                vals=np.array([pxx,pzz,pzz-pxx])
                rows.append({'h':h,'pxx':pxx,'pzz':pzz,'Q':pzz-pxx,'max_error':float(np.max(np.abs(vals-target)))})
            v1=np.array([rows[-2][k] for k in ('pxx','pzz','Q')]);v2=np.array([rows[-1][k] for k in ('pxx','pzz','Q')])
            rich=(4*v2-v1)/3
            err=float(np.max(np.abs(rich-target)))
            passed=err<float(inputs['tolerance'])
            case={'a':aa,'b':bb,'radius':rad,'order':order,'exact_pxx_pzz_Q':target.tolist(),'differences':rows,'richardson_pxx_pzz_Q':rich.tolist(),'richardson_max_error':err,'pass':passed}
            report['inverse_cases'].append(case)
            print(json.dumps({'a':aa,'b':bb,'radius':rad,'order':order,'richardson_max_error':err,'pass':passed}),flush=True)
            save()
report['status']='PASS' if all(x['pass'] for x in report['inverse_cases']) else 'FAIL_NUMERICAL'
save()
print(json.dumps({k:v for k,v in report.items() if k not in ('inverse_cases','exact_checks')},indent=2),flush=True)
if report['status']!='PASS':sys.exit(1)
