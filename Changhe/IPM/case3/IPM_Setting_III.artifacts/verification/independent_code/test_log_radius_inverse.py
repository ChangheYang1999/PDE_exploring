"""Manufactured and overlap checks of the exact log-radius exterior formula."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from direct_inverse import DirectInverse,Quadrature,kernel_difference_scaled
from log_radius_inverse import LogTailInverse,LogRadiusQCheckpoint,factored_kernel

out=Path('research/log_radius_inverse/verification');out.mkdir(exist_ok=True)
rows=[];overlap=[];kernel_rows=[]
mp.mp.dps=250
for tau in ['0.001','0.000000000001','1e-100','1e-200']:
    z=mp.mpf(tau);nx=mp.mpf(3)/5;ny=mp.mpf(4)/5;ex=mp.mpf(5)/13;ey=mp.mpf(12)/13
    def kernel(x,y):
        den=(x*x+y*y)**2
        return (-x*y/(mp.pi*den),(x*x-y*y)/(2*mp.pi*den))
    a=kernel(z*nx-ex,z*ny-ey);b=kernel(-ex,-ey)
    exact=np.array([float((a[i]-b[i])/z) for i in range(2)])
    own=factored_kernel(float(z),.6,.8,5/13,12/13)
    err=float(np.max(abs(own-exact)));assert err<3e-16
    kernel_rows.append({'tau':tau,'error':err,'factored':own.tolist()})
assert np.isfinite(factored_kernel(0.,.6,.8,5/13,12/13)).all()

class RadialTest:
    def __init__(self,kappa):self.eta=1/kappa;self.p=1-self.eta
    def rho(self,x,y):
        return np.asarray(y)*np.exp(-self.eta*np.log(np.hypot(1.,np.hypot(x,y))))
    def log_scaled_polar_density(self,s,theta):
        return np.exp(-self.eta/2*np.logaddexp(0.,-2*np.asarray(s)))[:,None]*np.sin(theta)[None,:]
    def exact(self,x,y):
        r=np.hypot(x,y);f=np.exp(-self.eta*np.log(np.hypot(1.,r)))
        H=f*quad(lambda t:t**3*np.exp(-self.eta*(np.log(np.hypot(1.,r*t))-np.log(np.hypot(1.,r)))),0,1,epsabs=2e-13,epsrel=2e-13,limit=150)[0]
        J=f-4*H;ss=(y/r)**2 if r else 0.;cc=(x/r)**2 if r else 0.
        return np.array([x*(H+ss*J),-y*(H+cc*J)])

for kap in [51.,201.]:
    c=RadialTest(kap)
    for level,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
        inv=LogTailInverse(c.rho,Quadrature(nr,nt,ne,of,1.,c.p,16.,kap));errors=[]
        for x,y in [(0.,.003),(.7,.4),(3.1,.039),(0.,1e4),(0.,1e80),(0.,1e250)]:
            exact=c.exact(x,y)
            with np.errstate(over='raise',invalid='raise',divide='raise'):
                u,parts=inv.velocity(x,y,parts=True)
            scale=max(1.,float(np.max(abs(exact))));err=float(np.max(abs(u-exact))/scale);errors.append(err)
            rows.append({'kappa':kap,'level':level,'x':x,'y':y,'velocity_scaled_error':err,'U':u.tolist(),'exact_U':exact.tolist(),'largest_log_radius':parts['largest_quadrature_log_radius'],'ordinary_radius_overflow':bool(parts['largest_quadrature_log_radius']>np.log(np.finfo(float).max))})
        print(json.dumps({'kappa':kap,'level':level,'max_scaled_error':max(errors)}),flush=True)
        if level==2:assert max(errors)<3e-9

state=Path('evidence/q_evaluations/qfree_N64_first/snapshot.npz')
c=LogRadiusQCheckpoint(state)
for r in [1e-8,.003,.7,1e4,1e22,1e80]:
    angles=np.array([.0037,.231,np.pi/2])
    old=c.polar_density(np.array([r]),angles)/r**c.p
    new=c.log_scaled_polar_density(np.array([np.log(r)]),angles)
    err=float(np.max(abs(new-old))/max(1.,np.max(abs(old))))
    assert err<2e-8
    overlap.append({'check':'Q scaled density','r':r,'relative_scale_error':err})
q=Quadrature(40,256,144,4.,c.L*2**(-c.kappa),c.p,16*c.L,c.kappa)
a=DirectInverse(c.rho,q);b=LogTailInverse(c.rho,q)
for x,y in [(0.,.003),(.7,.4),(0.,1e22),(0.,1e80)]:
    u=a.velocity(x,y);v=b.velocity(x,y);err=float(np.max(abs(u-v))/max(1.,np.max(abs(u))))
    overlap.append({'check':'Q full velocity old-new','x':x,'y':y,'scaled_error':err});assert err<3e-10
# A large log radius is supplied directly, without constructing exp(log_r).
far=c.log_scaled_polar_density(np.array([1e4,1e5]),np.array([.231,np.pi/2]))
endpoint=np.array([sum(v) for v in c.coeff]);theta=np.array([.231,np.pi/2])
limit=c.L**c.eta/2*np.sin(theta)*(endpoint@np.cos(2*np.arange(c.M)[:,None]*theta[None,:]))
assert np.max(abs(far-limit))<3e-10
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','kernel_checks':kernel_rows,'manufactured_velocity_rows':rows,'overlap_checks':overlap,'far_scaled_limit':far.tolist(),'scope':'Exact exterior rewrite checked at three quadrature levels against analytic radial-integral velocities, including kappa51 and201 with ordinary radius overflow. Not an interval certificate; finite query coordinates and densities must still be representable; algebraically scaled geometry is tested through radius1e250.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'utc':result['utc'],'status':'PASS','manufactured_rows':len(rows),'overlap_rows':len(overlap)}),flush=True)
