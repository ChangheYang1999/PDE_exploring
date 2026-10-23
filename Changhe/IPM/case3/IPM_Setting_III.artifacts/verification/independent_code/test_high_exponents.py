from pathlib import Path
from datetime import datetime,timezone
from dataclasses import asdict
import json
import numpy as np
import sympy as sp
from manufactured import make_pair
from direct_inverse import DirectInverse,Quadrature
out=[]
points=np.array([[.001,.002],[.3,.7],[3.,-2.],[100.,40.]])
for p in [sp.Rational(1,5),sp.Rational(4,5),sp.Rational(24,25)]:
 f,center=make_pair(p=p)
 truth=np.column_stack([f['u1'](*points.T),f['u2'](*points.T)])
 for n,nt,ne in [(24,128,48),(40,256,96),(64,512,144)]:
  cfg=Quadrature(n,nt,ne,4.,1.,float(p),16.)
  inv=DirectInverse(f['rho'],cfg)
  err=np.abs(inv.velocities(points)-truth)
  row={'exponent':str(p),'config':asdict(cfg),'max_absolute_error':float(err.max()),'errors':err.tolist()}
  out.append(row); print(json.dumps(row),flush=True)
Path('research/inverse/verification/manufactured_high_exponents.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'records':out},indent=2)+'\n')
