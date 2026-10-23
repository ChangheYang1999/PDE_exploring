"""Independent canonical inverse and jet checks for the vanishing family."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
import sympy as s
from scipy.integrate import quad
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
out=Path('research/vanishing_approximate_family/verification');out.mkdir(exist_ok=True)
D=s.symbols('D',positive=True);eta=D/(1+D);a=4*D;A=1+2*D;b=-a*eta/2
assert s.simplify((a-2*A)*b-6*b-16*D**2/(1+D))==0
assert s.simplify((a-4*A)*b-8*D**2)==0
q,tau,J,z=s.symbols('q tau J z',real=True)
# z=cos(theta)^2; J=1-4tau. Check the U.grad rho contraction.
contraction=(tau+(1-z)*J)*z*(-eta*q)-(tau+z*J)*(1-eta*q*(1-z))
assert s.expand(contraction+tau+z*J+eta*q*tau*(2*z-1))==0
rows=[];limits=[]
for dd in [1/4,1/8,1/16]:
    ee=dd/(1+dd);aa=4*dd;kap=1/ee;pp=1-ee;ell=1+dd
    def rho(x,y):return aa*np.asarray(y)*np.exp(-ee*np.log(np.hypot(1.,np.hypot(x,y))))
    def analytic(x,y):
        rr=np.hypot(x,y);ff=np.exp(-ee*np.log(np.hypot(1.,rr)))
        hh=quad(lambda t:t**3*np.exp(-ee*np.log(np.hypot(1.,rr*t))),0,1,epsabs=2e-13,epsrel=2e-13)[0]
        jj=ff-4*hh;zz=(x/rr)**2 if rr else 0.;ss=(y/rr)**2 if rr else 0.
        vel=np.array([aa*x*(hh+ss*jj),-aa*y*(hh+zz*jj)])
        den=np.hypot(1.,rr);grad=aa*ff*np.array([-ee*(x/den)*(y/den),1-ee*(y/den)**2])
        return vel,grad,hh,ff
    levels=[]
    for level,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
        inv=DirectInverse(rho,Quadrature(nr,nt,ne,of,1.,pp,16.,kap));errors=[]
        for x,y in [(0.,.003),(.013,.007),(.7,.4),(0.,2.),(3.1,.039),(0.,1e4)]:
            exact,g,hh,ff=analytic(x,y);u=inv.velocity(x,y);fd=np.array(cartesian_gradient(rho,x,y,.0015,0.));rv=float(rho(x,y))
            tx=(ell*x+u[0])*fd[0];ty=(ell*y+u[1])*fd[1];R=tx+ty-rv
            nf=abs(tx)+abs(ty)+abs(rv);nv=abs(rv)+abs(x*fd[0]+y*fd[1])+abs(np.dot(u,fd))
            raw=(ell*np.array([x,y])+exact)@g-rv
            nrx=abs(u-exact).max()/max(1.,abs(exact).max());dg=abs(fd-g).max()/max(1.,abs(g).max())
            row={'D':dd,'level':level,'x':x,'y':y,'velocity_error_scaled':float(nrx),'gradient_error_scaled':float(dg),'R':float(R),'R_analytic':float(raw),'R_Nf':float(abs(R)/nf),'R_Nv':float(abs(R)/nv),'uniform_bound':4*dd,'tau':hh/ff}
            errors.append(nrx);rows.append(row)
            assert abs(R)/nf <4*dd+1e-8 and abs(R)/nv<4*dd+1e-8
            assert .25-1e-12<=hh/ff<=1/(4-ee)+1e-12
        levels.append(max(errors));print(json.dumps({'D':dd,'level':level,'max_velocity_error_scaled':levels[-1]}),flush=True)
    assert levels[-1]<3e-9
    for yy in [1e2,1e4,1e6]:
        exact,g,_,_=analytic(0.,yy);R=(ell*np.array([0.,yy])+exact)@g-float(rho(0.,yy))
        predicted=-aa*aa*pp/(4-ee);measured=R/yy**(1-2*ee)
        limits.append({'D':dd,'y':yy,'scaled_R':float(measured),'far_coefficient':predicted,'relative_error':float(abs(measured/predicted-1))})
    assert limits[-1]['relative_error']<1e-7
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_symbolic_checks':['T1','T2','U dot gradient quotient'],'inverse_rows':rows,'far_axis_limits':limits,'scope':'Separate direct full-plane inverse and Cartesian FD8 checked against the explicit radial-integral solution. Analytic global residual, compact convergence and gradient bounds are proved in PROOF.md, not certified by this finite sample.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','utc':result['utc'],'rows':len(rows)}),flush=True)
