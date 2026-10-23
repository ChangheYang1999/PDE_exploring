"""Independent weighted-affine energy and Mellin multiplier checks."""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import numpy as np
import sympy as s
import mpmath as mp
m,n,z,ell=s.symbols('m n z ell',positive=True);checks=[]
def zero(name,value):
    assert s.simplify(value)==0,(name,s.simplify(value));checks.append(name)
den=(z+(n-m)**2)*(z+(n+m)**2)
zero('resolvent factorization',den-((m*m-n*n-z)**2+4*m*m*z))
zero('multiplier monotonic form',(z+m*m+n*n)**2/den-1-4*m*m*n*n/den)
zero('multiplier derivative',s.diff((z+m*m+n*n)**2/den,z)+8*m*m*n*n*(z+m*m+n*n)/den**2)
zero('balanced weight',((m*m+4)/(m*m-4)-(m*m+16)/(16-m*m)).subs(m,s.sqrt(8)))
Nm=lambda mm:max((mm*mm+4)/(mm*mm-4),(mm*mm+16)/(16-mm*mm))
assert abs(Nm(3)-25/7)<1e-15
bound=((m-1)*ell-1)*(16-m*m)/(m*m+16)
zero('optimized derivative',s.diff(bound,m)-(ell*(256-m**4)-64*ell*m*m+64*(ell+1)*m)/(m*m+16)**2)
# Direct singular-value checks with complex row/column operators, including high angular modes.
svrows=[]
for mm in [2.1,2.5,math.sqrt(8),3.,3.5,3.9]:
    maximum=0.
    for nn in range(0,202,2):
        for xi in [0.,.01,.31,1.,4.,100.]:
            vec=np.array([mm+1j*xi,1j*nn]);mat=np.outer(vec,vec)/(nn*nn-(mm+1j*xi)**2)
            norm=float(np.linalg.svd(mat,compute_uv=False)[0]);maximum=max(maximum,norm)
            expected=(xi*xi+mm*mm+nn*nn)/math.sqrt((xi*xi+(nn-mm)**2)*(xi*xi+(nn+mm)**2))
            assert abs(norm-expected)<3e-13*max(1.,expected)
            assert norm<=Nm(mm)*(1+2e-14)
    svrows.append({'m':mm,'maximum':maximum,'N_m':Nm(mm)})
# Gaussian manufactured field, center exact with a=4D, ell=1+D.
# Angular polynomial integration is symbolic; remaining radial quadrature is 55-digit.
mp.mp.dps=55
rr,th,aa,DD,hh,jj,ff=s.symbols('r th a D H J f',real=True)
xx=rr*s.cos(th);yy=rr*s.sin(th);rh=aa*yy*ff;ht=aa*yy*(ff-1)
ux=aa*xx*(hh+s.sin(th)**2*jj);uy=-aa*yy*(hh+s.cos(th)**2*jj)
vx=ux-aa*xx/4;vy=uy+aa*yy/4
gx=-2*xx*rh;gy=aa*ff*(1-2*yy*yy)
R=((1+DD)*xx+ux)*gx+((1+DD)*yy+uy)*gy-rh
quantities={'h2':ht*ht,'v2':vx*vx+vy*vy,'F2':R*R,'v2h':vy*ht,'Fh':R*ht,'XUh2':(xx*ux+yy*uy)/rr**2*ht*ht}
angular={}
for name,value in quantities.items():
    av=s.integrate(s.expand_trig(s.expand(value)),(th,0,2*s.pi))
    angular[name]=s.lambdify((rr,aa,DD,hh,jj,ff),av,'mpmath')
def radial_values(r):
    ss=r*r;f=mp.exp(-ss)
    if ss<mp.mpf('.05'):
        # The integral H=int_0^1 t^3 exp(-s t²) dt, evaluated by its entire series.
        H=mp.fsum((-ss)**k/(mp.factorial(k)*(4+2*k)) for k in range(45))
    else:H=(1-(1+ss)*f)/(2*ss*ss)
    return H,f-4*H,f
records=[]
for mm in [mp.mpf('2.5'),mp.sqrt(8),mp.mpf(3),mp.mpf('3.5')]:
    for d in [mp.mpf('.03'),mp.mpf('.25')]:
        a=4*d
        vals={}
        for name,func in angular.items():
            def integrand(r):
                if r==0:return mp.mpf(0)
                H,J,f=radial_values(r)
                return func(r,a,d,H,J,f)*r**(1-2*mm)
            # Tiny endpoints are handled by asymptotically negligible cutoffs, no cancellation at r~1e-60.
            vals[name]=mp.quad(integrand,[mp.mpf('1e-8'),mp.mpf('.03'),mp.mpf('.3'),1,3,10,mp.inf])
        E=((mm-1)*(1+d)-1)*vals['h2']+mm*vals['XUh2']+a*vals['v2h']-vals['Fh']
        rel=abs(E)/max(vals['h2'],vals['F2'])
        assert rel<mp.mpf('2e-7'),(mm,d,rel)
        ratio=mp.sqrt(vals['v2']/vals['h2']);assert ratio<=Nm(mm)
        records.append({'m':str(mm),'D':str(d),'energy_relative_defect':str(rel),'velocity_to_density_weighted_norm':str(ratio),'N_m':str(Nm(mm)),'residual_to_density_weighted_norm':str(mp.sqrt(vals['F2']/vals['h2']))})
        print(json.dumps(records[-1]),flush=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'singular_value_checks':svrows,'manufactured_energy':records,'scope':'Independent exact Mellin algebra, complex matrix singular values, and direct 55-digit Gaussian radial integration after exact angular integration. No exact profile or sharpness of the enlarged-input elliptic bound is asserted.'}
Path('research/weighted_affine_defect/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','utc':result['utc']}),flush=True)
