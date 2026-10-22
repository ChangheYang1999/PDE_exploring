"""Adversarial exact PDE state which must fail global admissibility."""
from datetime import datetime,timezone
from pathlib import Path
import json
import numpy as np
from residuals import cartesian,divided,summary

def state(beta):
    k=beta+2;m=2*beta+1
    def theta(p):
        x,y=np.asarray(p).T
        return 2*k*m*np.sin(x)**2*y
    def omega(p):
        x,y=np.asarray(p).T
        return 4*k*np.sin(x)*np.cos(x)*y
    def psi(p):
        x,y=np.asarray(p).T
        return (beta*x+k*np.sin(x)*np.cos(x))*y
    def u(p):
        x,y=np.asarray(p).T
        return np.stack([-beta*x-k*np.sin(x)*np.cos(x),
                          (beta+k*np.cos(2*x))*y],axis=-1)
    return theta,omega,psi,u

p=np.array([[0,0],[.01,0],[0,.3],[.2,.4],[.7,.5],[1.1,.03],
            [np.pi/2,0],[np.pi/2,.4],[np.pi,.2]])
rows=[]
for beta in [1.5,2,3,6]:
    theta,omega,psi,u=state(beta)
    for step in [.004,.002,.001]:
        c=cartesian(theta,omega,beta,p,u=u,psi=psi,step=step)
        d=divided(theta,omega,beta,p,u=u,step=step,axis_step=step)
        row=dict(beta=beta,step=step,cartesian=summary(c),divided=summary(d),
                 fields={k:np.asarray(v).tolist() for k,v in c.items()},
                 divided_fields={k:np.asarray(v).tolist() for k,v in d.items()})
        rows.append(row)
        print(json.dumps(dict(beta=beta,step=step,
            abs_ro=float(np.max(np.abs(c['R_omega']))),abs_rt=float(np.max(np.abs(c['R_theta']))),
            abs_do=float(np.max(np.abs(d['R_omega_div']))),abs_dt=float(np.max(np.abs(d['R_theta_div']))),
            ratio_ro=float(np.max(c['ratio_omega'])),ratio_rt=float(np.max(c['ratio_theta'])))),flush=True)
Path('runs/exact_inadmissible_tests.json').write_text(json.dumps(dict(
 timestamp=datetime.now(timezone.utc).isoformat(),points=p.tolist(),rows=rows,
 admissible=False,verdict='REFUTED as a target candidate: U has linear growth',
 limitation='Pointwise ratios at analytically zero denominators or floating representations of exact stagnation points can be one despite tiny absolute roundoff. All values are retained without a positive floor.'),indent=2)+'\n')
