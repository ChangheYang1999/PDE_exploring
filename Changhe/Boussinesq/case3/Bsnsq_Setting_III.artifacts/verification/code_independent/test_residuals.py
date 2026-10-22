import json,time
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from finite_difference import cartesian_residuals,desingularized_residuals,mixed,safe_ratio
from manufactured import Gaussian


def main():
    start=time.monotonic()
    points=np.array([[0,0],[0,.3],[0,-1],[1e-7,.2],[.1,-.3],[.4,.4],[1.,.25],[-2,1]],float)
    theta=lambda x,y:x*x
    omega=lambda x,y:2*x
    psi=lambda x,y:2*x*y-x**3/3+0.7*x
    relative=lambda p:np.column_stack((-2*p[:,0],2*p[:,1]-p[:,0]**2))
    out=[]
    for h in (0.04,0.02,0.01):
        r=cartesian_residuals(theta,omega,psi,relative,points,2.,h)
        d=desingularized_residuals(theta,omega,psi,relative,points,2.,h)
        record={'step':h,'cartesian':{k:np.asarray(v).tolist() for k,v in r.items()},
                'desingularized':{k:np.asarray(v).tolist() for k,v in d.items()},
                'max_absolute':{k:float(np.max(np.abs(r[k]))) for k in ('R_Omega','R_Theta','E')},
                'divided_max_absolute':{k:float(np.max(np.abs(d[k]))) for k in ('R_F','R_G','R_H')}}
        print('polynomial',h,record['max_absolute'],record['divided_max_absolute'])
        assert max(record['max_absolute'].values())<1e-8
        assert max(record['divided_max_absolute'].values())<1e-8
        out.append(record)
    # It is essential that this zero-residual control fails the far-field test.
    tailpoints=np.array([[r,0] for r in (10.,100.,1000.)])
    growth=np.linalg.norm(relative(tailpoints),axis=1)/tailpoints[:,0]
    assert growth[-1]>900
    # Wrong center drift must produce a measurable defect in a general field.
    g=Gaussian()
    th=lambda x,y:x*x*np.exp(-(x*x+y*y))
    r1=cartesian_residuals(th,g.omega,g.psi,g.relative,points,3.,.01)
    wrong=lambda p:g.velocity(p[:,0],p[:,1])
    r2=cartesian_residuals(th,g.omega,g.psi,wrong,points,3.,.01)
    drift_impact=float(np.max(np.abs(r2['R_Omega']-r1['R_Omega'])))
    assert drift_impact>.1
    assert np.array_equal(safe_ratio(np.array([0.,1.]),np.array([0.,0.])),np.array([0.,np.inf]))
    payload={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
             'elapsed_seconds':time.monotonic()-start,'points':points.tolist(),
             'polynomial_control':out,'polynomial_growth_U_over_r':growth.tolist(),
             'wrong_drift_residual_change':drift_impact,
             'normalization_policy':'No positive floor. Exact N=R=0 gives 0; N=0 and R!=0 gives infinity. Raw normalized ratios can be order one when every term is roundoff; retain them and use absolute error and desingularized checks.'}
    Path('verification/residual_manufactured.json').write_text(json.dumps(payload,indent=2)+'\n')

if __name__=='__main__':main()
