"""Independent exact coefficient and Cartesian inverse checks for result35."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import numpy as np
from direct_inverse import DirectInverse,Quadrature
z=s.symbols('z',nonzero=True);I=s.I
cos=(z+1/z)/2;sin=(z-1/z)/(2*I)
dt=lambda f:s.expand(I*z*s.diff(f,z))
sn=lambda n:(z**n-z**(-n))/(2*I)
def zero(f):return s.expand(f)==0
def stream(a,theta):
    rhs=s.expand(a*cos*theta-sin*dt(theta));phi=0
    for term in s.Add.make_args(rhs):
        n=int(term.as_powers_dict().get(z,0));coef=term/z**n
        assert n!=0 and n%2==0
        phi+=coef*z**n/(n*n-(a+1)**2)
    phi=s.expand(phi)
    assert zero(-dt(dt(phi))-(a+1)**2*phi-rhs)
    return phi
checks=[]
for p in [s.Rational(1,4),s.Rational(1,2),s.Rational(2,3),s.Rational(3,4)]:
    ell=1/p;D=ell-1;q=2*p-1;t=3*p-2
    theta=sn(1)+sn(3)/5-sn(5)/10
    phi=stream(p,theta);ur=-dt(phi);ut=(p+1)*phi
    force=s.expand(p*ur*theta+ut*dt(theta));theta1=s.expand(force/D)
    phi1=stream(q,theta1)
    assert zero((ell*q-1)*theta1+force)
    assert zero(theta1.subs(z,1/z)+theta1)
    assert zero(theta1.subs(z,-1/z)-theta1)
    assert s.simplify(1-q-2*(1-p))==0
    assert s.simplify(1/D-ell/D*q-1)==0
    assert s.simplify(1/D-ell/D*t-2)==0
    checks.append({'p':str(p),'q':str(q),'two_poisson_relations':True,'second_transport_coefficient':True,'parities':True,'scale_and_time_exponents':True})
class SmoothOneMode:
    def __init__(self,q):self.q=q
    def rho(self,x,y):return np.asarray(y)*(1+np.asarray(x)**2+np.asarray(y)**2)**((self.q-1)/2)
    def exact(self,x,y):
        r=np.hypot(x,y);a=(self.q-1)/2;log=np.log1p(r*r)
        integral=.5*(np.expm1((a+2)*log)/(a+2)-np.expm1((a+1)*log)/(a+1))
        g=-integral/(2*r*r);gp=integral/r**3-r*(1+r*r)**a/2
        c=x/r;ss=y/r;ur=-2*g/r*(c*c-ss*ss);ut=gp*2*c*ss
        return np.array([ur*c-ut*ss,ur*ss+ut*c])
    def homogeneous(self,x,y):
        r=np.hypot(x,y);c=x/r;ss=y/r;q=self.q
        g=-r**(q+1)/(2*(q+3));gp=-(q+1)*r**q/(2*(q+3))
        ur=-2*g/r*(c*c-ss*ss);ut=gp*2*c*ss
        return np.array([ur*c-ut*ss,ur*ss+ut*c])
numeric=[]
points=[(.7,.3),(1.8,.4),(12.,3.),(0.,100.)]
for q in [-.5,0.,.5]:
    field=SmoothOneMode(q);levels=[]
    for nr,nt,ne in [(24,128,96),(40,256,144),(64,512,224)]:
        # A positive exterior bound is valid also for these decaying inputs.
        inv=DirectInverse(field.rho,Quadrature(nr,nt,ne,4.,1.,.5,16.,2.))
        errors=[float(np.max(abs(inv.velocity(x,y)-field.exact(x,y)))) for x,y in points]
        levels.append({'radial':nr,'angular':nt,'exterior':ne,'point_errors':errors,'max_error':max(errors)})
    assert levels[-1]['max_error']<3e-8,levels
    ratios=[]
    for r in [10.,100.,1000.,10000.]:
        x,y=.8*r,.6*r
        ratios.append({'radius':r,'scaled_velocity_remainder':float(np.max(abs(field.exact(x,y)-field.homogeneous(x,y)))/r**(q-2))})
    numeric.append({'density_exponent':q,'velocity_remainder_exponent':q-2,'quadrature':levels,'asymptotic_ratio':ratios})
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_checks':checks,'manufactured_inverse_checks':numeric,'scope':'Algebra and sampled canonical-inverse calibration, not a continuum proof or an actual nonlinear profile.'}
Path('research/far_field_second_term/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
