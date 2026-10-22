from pathlib import Path
from datetime import datetime,timezone
import time,json
import numpy as np
from duffy_inverse import DuffyQuadrature,velocity_duffy
from manufactured import PolynomialRadialStream
start=time.monotonic()
points=np.array([[0,0],[.01,0],[0,.03],[.3,.7],[-.3,.7],[1,1],[3,.1],[10,0],[20,17],[100,0],[100,30]])
rows=[]
for name,a,k,gamma in [('gaussian',None,1,1),('slow',1/6,1,1/3),('anisotropic',1/4,2.5,.5)]:
 model=PolynomialRadialStream(a,k)
 for order in [32,64,128]:
  for scale in [.5,1,3]:
   got=velocity_duffy(model.omega,points,DuffyQuadrature(order,gamma,scale))
   exact=model.velocity(points)
   row=dict(name=name,order=order,scale=scale,
            max_abs_error=float(np.max(np.abs(got-exact))),
            errors_by_target=np.max(np.abs(got-exact),axis=1).tolist())
   rows.append(row);print(json.dumps(row),flush=True)
Path('runs/duffy_inverse_tests.json').write_text(json.dumps(dict(
 timestamp=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
 points=points.tolist(),rows=rows),indent=2)+'\n')
