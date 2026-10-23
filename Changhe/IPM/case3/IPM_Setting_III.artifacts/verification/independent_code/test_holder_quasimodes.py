"""Independent exact formula checks and sampled convolution consistency."""
import json,math
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

x,y=s.symbols('x y',real=True);r=s.sqrt(x*x+y*y)
checks=[]
for d in [s.Rational(5,4),s.Rational(3,2),s.Rational(7,4)]:
    A=d;a=(d-1)*(d+3)
    h=y*r**(d-1);psi=-x*y*r**(d-1)/(d+3)
    poisson=s.simplify(-s.diff(psi,x,2)-s.diff(psi,y,2)-s.diff(h,x))
    transport=s.simplify(A*x*s.diff(h,x)+y*s.diff(h,y)-h+a*s.diff(psi,x))
    assert poisson==0 and transport==0
    checks.append({'test':'homogeneous_pair','d':str(d),'poisson':str(poisson),'transport':str(transport)})
# General radial Q with DQ=a_T-(d+3)Q. A logarithmic polynomial Q
# makes the canonical relation exact locally and checks all cutoff terms.
for d in [s.Rational(5,4),s.Rational(3,2)]:
    z=s.symbols('z',positive=True);Q=1+2*s.log(z)+3*s.log(z)**2
    aa=s.simplify(z*s.diff(Q,z)+(d+3)*Q)
    hh=y*r**(d-1)*aa.subs(z,r);pp=-x*y*r**(d-1)*Q.subs(z,r)
    a=(d-1)*(d+3)
    actual=s.simplify(d*x*s.diff(hh,x)+y*s.diff(hh,y)-hh+a*s.diff(pp,x))
    Daa=(z*s.diff(aa,z)).subs(z,r)
    one=(d+3)*Daa/4;three=(d-1)*(Daa/4+(d+3)*(Q.subs(z,r)-aa.subs(z,r)/(d+3)))
    expected=r**d*(one*y/r+three*(3*x*x*y-y**3)/r**3)
    assert s.simplify(actual-expected)==0
    assert s.simplify(-s.diff(pp,x,2)-s.diff(pp,y,2)-s.diff(hh,x))==0
    checks.append({'test':'nonlocal_cutoff_residual','d':str(d),'exact':True})
# A smooth eta with eta(0)=1, eta'(0)=0. A plateau is not needed for
# the sampled checks; the proof can choose a plateau cutoff instead.
def eta(t):
    if abs(t)>=1:return 0.
    return math.exp(-t*t/(1-t*t))
def deta(t):
    if abs(t)>=1:return 0.
    return -2*t*eta(t)/(1-t*t)**2
samples=[]
for d in (1.25,1.5,1.75):
    for T in (1.,2.,4.,8.,16.):
        maximum=0.;max_identity=0.
        for log_r in np.linspace(-3*T-.3,-T+.3,91):
            lo=max(0.,log_r+T);hi=max(0.,log_r+3*T)
            def integral(offset):
                l=max(0.,log_r+offset+T);h=max(0.,log_r+offset+3*T)
                return quad(lambda v:math.exp(-(d+3)*v)*eta((log_r+offset-v+2*T)/T),l,h,epsabs=2e-13,epsrel=2e-13,limit=100)[0] if h>l else 0.
            q=integral(0.);a=eta((log_r+2*T)/T)
            maximum=max(maximum,abs(q-a/(d+3)))
            h=1e-4
            fd=(-integral(2*h)+8*integral(h)-8*integral(-h)+integral(-2*h))/(12*h)
            max_identity=max(max_identity,abs(fd-(a-(d+3)*q)))
        assert max_identity<2e-8
        samples.append({'d':d,'T':T,'T_times_max_Q_defect':T*maximum,'max_convolution_ODE_FD_error':max_identity})
# Independent angular quadrature verifies the exact Chebyshev normalization.
coeffchecks=[]
for delta in (.3,.7,1.4,2.3):
    for n in (1,2,3,7,13):
        integral=2/math.pi*quad(lambda t:((1+math.cos(t))/2)**delta*math.cos(n*t),0,math.pi,epsabs=3e-13,epsrel=3e-13,limit=200)[0]
        exact=2**(1-2*delta)*gamma(2*delta+1)/(gamma(delta+n+1)*gamma(delta-n+1))
        err=abs(integral-exact);assert err<2e-11
        coeffchecks.append({'delta':delta,'n':n,'absolute_error':err})
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_checks':checks,'sampled_convolution_checks':samples,'chebyshev_coefficients':coeffchecks,'scope':'Formula and sampled convolution checks; the standalone proof gives continuum Holder estimates. No nonlinear profile or discrete singular-value theorem.'}
p=Path('research/holder_quasimodes/verification/checks.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
