import json
from dataclasses import asdict
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from manufactured import make_pair

points=np.array([[0,0],[0.001,0.002],[0.3,0.7],[1.,0],[0,1.],[3.,-2.],[-5.,1.7],[8.,8.],[100.,40.]])
records=[]
for anisotropic in [False,True]:
    f,center=make_pair(anisotropic=anisotropic)
    truth=np.column_stack([f['u1'](*points.T),f['u2'](*points.T)])
    for nr,nt,nex in [(24,64,32),(40,128,64),(64,256,96)]:
        for radius in [2.,4.,8.]:
            cfg=Quadrature(nr,nt,nex,radius,1.,0.5)
            solver=DirectInverse(f['rho'],cfg)
            actual=solver.velocities(points)
            err=np.abs(actual-truth)
            row={'anisotropic':anisotropic,'config':asdict(cfg),'center':center,'max_U_absolute_error':float(err.max()),'max_U_scaled_error':float(np.max(err/(1+np.abs(truth)))),'points':points.tolist(),'errors':err.tolist()}
            records.append(row)
            print(json.dumps({k:v for k,v in row.items() if k not in ['points','errors']}),flush=True)
    for step in [0.003,0.001,0.0003]:
        gx,gy=cartesian_gradient(f['rho'],*points.T,relative_step=step)
        err=max(np.max(np.abs(gx-f['gx'](*points.T))),np.max(np.abs(gy-f['gy'](*points.T))))
        print('gradient',anisotropic,step,float(err),flush=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'method':'direct kernel quadrature + infinite exterior Jacobi map, Cartesian order-8 differences','records':records}
Path('research/inverse/verification/manufactured_direct.json').write_text(json.dumps(result,indent=2)+'\n')
