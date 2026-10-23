"""Check basis assembly against two independently derived exact Poisson pairs."""
import json,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial import chebyshev as C
from smooth_basis import SmoothBasis
from kernel_basis import KernelBasis
from direct_inverse import Quadrature,cartesian_gradient
from manufactured_high_modes import HighMode
p=1/3;a=(1-p)/2
b=SmoothBasis(8,4,p,1.)
t=np.cos(np.pi*(np.arange(40)+.5)/40);u=(1-t)/2;sigma=1-u**3
coeff0=np.zeros((b.M,b.N+1));coeff0[0]=C.chebfit(t,-(p+3)-(1-p)*u**3,b.N)
# G=Im(z^3)*w/9, rho=Delta G, psi=-G_x.
coeff1=np.zeros_like(coeff0)
coeff1[0]=C.chebfit(t,(-16*a*sigma+4*a*(a+1)*sigma*sigma)/9,b.N)
coeff1[1]=C.chebfit(t,(-32*a+8*a*(a+1)*sigma)/9,b.N)
points=np.array([[.03,.07],[.3,.7],[3.,-2.],[100.,40.],[5.,.003]])
x,y=points.T;s=x*x+y*y;w=(1+s)**(-a)
exact0=np.column_stack([-x*w+2*a*x*y*y*w/(1+s),y*w-2*a*x*x*y*w/(1+s)])
exact1=HighMode(3,p).components(x,y)[1]
checks=[]
for n,nt,ne in [(20,64,64),(32,128,96),(48,256,144)]:
 q=Quadrature(n,nt,ne,4.,1.,p,16.,1/(1-p));k=KernelBasis(b,q)
 mats=np.array([k.velocity_matrix(*point) for point in points])
 for name,coeff,exact in [('radial',coeff0,exact0),('third_mode',coeff1,exact1)]:
  calc=mats@coeff.reshape(-1)
  checks.append({'case':name,'quadrature':q.__dict__,'max_error':float(np.max(abs(calc-exact))),'errors':(calc-exact).tolist()})
# Direct Taylor check of the coefficient rows by density values, no modal inverse.
rows=b.cubic_density_rows();H=b.quartic_stream_difference()
assert abs(b.center_strain()@coeff0.reshape(-1)-1)<1e-12
assert abs(H@coeff0.reshape(-1))<1e-12
# psi=-G_x=-2xy w*(3-a(3x*x-y*y)/(1+s))/9.
# q1=(6a+6a)/9=4a/3, q2=(6a-2a)/9=4a/9, H=8a/9.
assert abs(H@coeff1.reshape(-1)-8*a/9)<1e-12
out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'third_mode_H':float(H@coeff1.reshape(-1)),'third_mode_exact_H':8*a/9}
Path('research/smooth_representation/verification/manufactured_basis.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
assert max(v['max_error'] for v in checks[-2:])<1e-8
