"""Independent exact consistency tests for the monotonicity proof.
No producer code is imported. These tests are not an existence certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
from datetime import datetime,timezone
import json, math
import sympy as s
from scipy.integrate import quad
x,y,A,a=s.symbols('x y A a',real=True)
checks=[]
for k in range(1,8):
    ts=s.symbols('t:'+str(k+1))
    Q=sum(ts[j]*x**(2*j)*y**(2*k-2*j) for j in range(k+1))
    ds=[2*j*A+2*(k-j) for j in range(k+1)]
    Psi=-sum(ds[j]*ts[j]*x**(2*j+1)*y**(2*k-2*j+1)/s.Integer(2*j+1) for j in range(k+1))
    assert s.expand(s.diff(Psi,x)+y*(A*x*s.diff(Q,x)+y*s.diff(Q,y)))==0
    P=s.Poly(s.expand(s.diff(Psi,x,2)+s.diff(Psi,y,2)+a*y*s.diff(Q,x)),x,y)
    for j in range(1,k+1):
        expected=2*j*(a-ds[j])*ts[j]-s.Rational((2*k-2*j+3)*(2*k-2*j+2),2*j-1)*ds[j-1]*ts[j-1]
        assert s.expand(P.coeff_monomial(x**(2*j-1)*y**(2*k-2*j+1))-expected)==0
    checks.append({'item':'first_monotone_jet','k':k,'exact':True})
C,S=s.symbols('C S',real=True)
def circle_int(poly):
    ans=0
    for (i,j),coeff in s.Poly(s.expand(poly),C,S).terms():
        if i%2 or j%2:continue
        u,v=i//2,j//2
        ans+=coeff*2*s.pi*s.Rational(math.factorial(2*u)*math.factorial(2*v),4**(u+v)*math.factorial(u)*math.factorial(v)*math.factorial(u+v))
    return s.simplify(ans)
gx=6*C*S-6*C*(3*C*C*S-S**3)
gy=3*(C*C-S*S)-6*S*(3*C*C*S-S**3)
assert circle_int(S*(-C*gx+S*gy))==0
assert circle_int(S*(-C*S*S*gx+C*C*S*gy))==-3*s.pi/4
assert s.rem(s.Poly(s.expand(gy-3*(C**4-6*C*C*S*S+S**4)),C),s.Poly(C*C+S*S-1,C)).as_expr()==0
checks.append({'item':'one_mode_J','fk_coefficient':'0','fkprime_coefficient':'-3*pi/4','exact':True})
# Interior stream harmonics for an ellipsoidal flat density. Im(C+iS)^(2n)
# gives sin(2n theta); every angular integral must vanish identically.
al,be=s.symbols('alpha beta',real=True)
for n in range(2,9):
    sinmode=s.expand(sum(s.binomial(2*n,j)*C**(2*n-j)*S**j*(-1)**((j-1)//2) for j in range(1,2*n+1,2)))
    value=circle_int(sinmode*C*S*(al*C*C+be*S*S)**(n-2))
    assert value==0
    checks.append({'item':'flat_ellipsoidal_harmonic','mode':2*n,'exact':True})
# Independent angular quadrature and its closed strain coefficient.
for av,bv in [(1.,1.),(4.,1.),(.04,3.),(7.,.3)]:
    integ,err=quad(lambda th:math.cos(th)**2*math.sin(th)**2/(av*math.cos(th)**2+bv*math.sin(th)**2),0,2*math.pi,epsabs=2e-13,epsrel=2e-13,limit=100)
    exact=math.pi/(math.sqrt(av)+math.sqrt(bv))**2
    assert abs(integ-exact)<3e-12
    checks.append({'item':'ellipsoidal_strain','alpha':av,'beta':bv,'angular_error':abs(integ-exact),'quad_error_estimate':err})
# Sign locations in the bump construction; no claim of numerical realization.
for theta,sgn in [(s.pi/4,-1),(s.pi/12,1)]:
    assert s.sin(3*theta)>0
    assert s.sign(s.cos(4*theta))==sgn
assert s.sin(3*5*s.pi/12)<0
checks.append({'item':'bump_strain_and_J_signs','exact':True})
# Radial Fourier majorant for the no-extra-equilibrium nonprofile.
u=s.symbols('u',positive=True)
radial=s.integrate(u**3*(3+u*u)*s.exp(-u*u/4),(u,0,s.oo))/4
assert radial==22
checks.append({'item':'Gaussian_velocity_gradient_majorant','value':str(radial),'exact':True})
result={'updated_utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','scope':'Consistency tests of identities and countertest constants; proof and hypotheses remain essential.','checks':checks}
out=Path('research/monotonicity_and_sign/verification');out.mkdir(parents=True,exist_ok=True)
(out/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
