import json
import time
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from inverse import Quadrature, velocity, center_strain
from manufactured import PolynomialRadialStream

np.seterr(over='raise',invalid='raise')
start=time.monotonic()
rng=np.random.default_rng(882717)
points=np.vstack([[0,0],[0.01,0],[0,0.03],[0.4,0.6],[1,1],[3,0.1],
                  rng.uniform(-2,2,(12,2))])
tests=[('gaussian',None,1,1),('algebraic_a1',1,1,1),
       ('slow_a1over6',1/6,1,1/3),('anisotropic_a1over4',1/4,2.5,1/2)]
rows=[]
for name,a,k,gamma in tests:
    model=PolynomialRadialStream(a,k)
    exact=model.velocity(points)
    for nr,na in [(64,96),(128,192),(256,384)]:
        q=Quadrature(nr,na,gamma)
        num=velocity(model.omega,points,q)
        c=center_strain(model.omega,q)
        row=dict(name=name,nr=nr,na=na,tail_power=gamma,
                 max_abs_velocity=float(np.max(np.abs(num-exact))),
                 max_relative_velocity=float(np.max(np.abs(num-exact)/(1+np.abs(exact)))),
                 center_strain=float(c),center_error=float(abs(c-1)))
        rows.append(row)
        print(json.dumps(row),flush=True)
report=dict(timestamp=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
            method='independent target-centered physical-space polar quadrature',
            candidate_test=False,rows=rows,points=points.tolist())
Path('runs/independent_inverse_tests.json').write_text(json.dumps(report,indent=2)+'\n')
