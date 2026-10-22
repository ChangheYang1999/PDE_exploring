from pathlib import Path
from datetime import datetime,timezone
import json,time
import numpy as np
from inverse import PanelQuadrature,velocity_panels
from manufactured import PolynomialRadialStream
start=time.monotonic()
points=np.array([[0,0],[.3,.7],[3,.1],[10,0],[0,10],[20,17],[100,0],[100,30]])
rows=[]
for name,a,k,gamma in [('gaussian',None,1,1),('slow',1/6,1,1/3),('anisotropic',1/4,2.5,.5)]:
 model=PolynomialRadialStream(a,k)
 for order in [8,12,18]:
  for scale in [.5,1,3]:
   cfg=PanelQuadrature(order,gamma,scale,1)
   result=velocity_panels(model.omega,points,cfg)
   exact=model.velocity(points)
   row=dict(name=name,order=order,radial_scale=scale,
            abs_error=float(np.max(np.abs(result-exact))),
            relative_error=float(np.max(np.abs(result-exact)/(1+np.abs(exact)))),
            errors_by_target=np.max(np.abs(result-exact),axis=1).tolist())
   rows.append(row);print(json.dumps(row),flush=True)
Path('runs/independent_far_inverse_tests.json').write_text(json.dumps(dict(
 timestamp=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
 points=points.tolist(),candidate_test=False,rows=rows),indent=2)+'\n')
