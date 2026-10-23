"""Independent direct-kernel calibration at the largest currently saved harmonic."""
from pathlib import Path
from datetime import datetime,timezone
from dataclasses import asdict
import json,time
import numpy as np
from direct_inverse import DirectInverse,Quadrature
from manufactured_high_modes import HighMode
points=np.array([[.3,.7],[3.,-2.],[100.,40.],[5.,.003]])
rows=[]
for exponent in (1/3,2/3,.96):
 obj=HighMode(95,exponent);exact=obj.components(*points.T)[1]
 for nr,nt,ne in ((40,256,144),(64,512,224),(80,1024,288)):
  q=Quadrature(nr,nt,ne,4.,1.,exponent,16.)
  start=time.time();got=DirectInverse(obj.rho,q).velocities(points)
  row={'utc':datetime.now(timezone.utc).isoformat(),'mode':95,'exponent':exponent,'config':asdict(q),'points':points.tolist(),'exact':exact.tolist(),'computed':got.tolist(),'max_absolute_error':float(np.max(abs(got-exact))),'seconds':time.time()-start}
  rows.append(row);print(json.dumps(row),flush=True)
  Path('research/inverse/verification/manufactured_mode95.json').write_text(json.dumps(rows,indent=2)+'\n')
 assert rows[-1]['max_absolute_error']<1e-9
