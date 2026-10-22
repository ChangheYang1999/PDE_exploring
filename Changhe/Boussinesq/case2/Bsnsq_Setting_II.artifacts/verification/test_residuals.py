from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from residuals import cartesian,divided,normalized,summary
from manufactured import PolynomialRadialStream
from inverse import Quadrature

beta=3.0
stream=PolynomialRadialStream()
omega=lambda p:8*stream.omega(p)
u=lambda p:8*stream.velocity(p)
psi=lambda p:8*stream.psi(p)
def theta(p):
    x,y=np.asarray(p).T
    return 336*x*x*y*np.exp(-x*x-y*y)

def exact_divided(p):
    x,y=np.asarray(p).T;q=x*x+y*y;h=np.exp(-q)
    a=336*h;g=8*(12-4*q)*h
    ax=-2*x*a;ay=-2*y*a
    gx=16*x*(4*q-16)*h;gy=16*y*(4*q-16)*h
    A=beta-8*(1-2*y*y)*h;B=beta+8*(1-2*x*x)*h
    rt=A*(2*a+x*ax)+B*(a+y*ay)-(beta-2)*a
    ro=A*(g+x*gx)+B*(g+y*gy)+g-(2*a+x*ax)
    return ro,rt

p=np.array([[0,0],[0,0.03],[0.01,0],[0.5,0],[0,0.7],
            [1e-7,0.2],[0.2,1e-7],[0.2,0.4],[0.9,0.7],[2,1]])
exact_o,exact_t=exact_divided(p)
rows=[]
for step in [0.004,0.002,0.001]:
    d=divided(theta,omega,beta,p,u=u,step=step,axis_step=step)
    c=cartesian(theta,omega,beta,p,u=u,psi=psi,step=step)
    rows.append(dict(step=step,
        divided_omega_error=float(np.max(np.abs(d['R_omega_div']-exact_o))),
        divided_theta_error=float(np.max(np.abs(d['R_theta_div']-exact_t))),
        cartesian_omega_error=float(np.max(np.abs(c['R_omega']-p[:,0]*p[:,1]*exact_o))),
        cartesian_theta_error=float(np.max(np.abs(c['R_theta']-p[:,0]**2*p[:,1]*exact_t))),
        poisson_error=float(np.max(np.abs(c['E_stream']))),
        curl_error=float(np.max(np.abs(c['E_curl']))),
        residuals=summary(d)))
    print(json.dumps({k:v for k,v in rows[-1].items() if k!='residuals'}),flush=True)
# Run an independent inverse, not the exact analytic velocity, on axis points.
q=Quadrature(192,256,1)
p2=p[:5]
d2=divided(theta,omega,beta,p2,config=q)
e2o,e2t=exact_divided(p2)
inv=dict(max_divided_omega_error=float(np.max(np.abs(d2['R_omega_div']-e2o))),
         max_divided_theta_error=float(np.max(np.abs(d2['R_theta_div']-e2t))))
print('Independent-inverse axis check:',json.dumps(inv),flush=True)
zero=normalized(np.array([0.,1.,1e-300]),np.array([0.,0.,1e-300]))
assert zero[0]==0 and np.isinf(zero[1]) and zero[2]==1
result=dict(timestamp=datetime.now(timezone.utc).isoformat(),beta=beta,
            candidate_test=False,manufactured_state='Gaussian fields with matched A2 center jet but nonzero PDE residual',
            points=p.tolist(),finite_difference_tests=rows,independent_inverse_axis=inv,
            denominator_rule='No positive floor. Exact 0/0 -> 0; nonzero/0 -> infinity. Subnormal denominators reported.')
Path('runs/independent_residual_tests.json').write_text(json.dumps(result,indent=2)+'\n')
