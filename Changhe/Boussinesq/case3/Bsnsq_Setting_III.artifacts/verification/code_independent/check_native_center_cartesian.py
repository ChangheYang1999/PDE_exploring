"""Physical-square full-plane center-strain audit, independent of modal inversion."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib
import numpy as np
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path(sys.argv[1]);start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'method':'Cartesian Duffy triangles in square plus entire compactified square exterior; centered velocity differences','states':[]}
for item in json.loads((root/'manifest.json').read_text())['states']:
 s=R2State(root/item['snapshot']);lam=float(s.meta['lam']);target=1+s.beta/2
 def mixed(x,y):return s.omega(x,y)+lam*x*s.divided(x,y,'native_seed')
 row={'label':item['label'],'archive_sha256':s.sha256,'target':target,'moment_comparison':s.center(),'tests':[]}
 for R,n,na,ne in [(6.,12,48,64),(12.,16,72,96),(18.,20,96,128)]:
  cfg=InverseSettings(radius=R,core_radial_order=n,core_angular_order=na,exterior_radial_order=ne,exterior_angular_order=na,decay_power=min(1/s.beta,1/float(s.meta['beta_seed'])))
  inv=CartesianInverse(mixed,cfg);hs=[.02,.01,.005];pts=np.array([[0,sign*h] for h in hs for sign in [1.,-1.]])
  v=inv.relative(pts);cs=[float((v[2*i,1]-v[2*i+1,1])/(2*h)) for i,h in enumerate(hs)]
  row['tests'].append({'settings':vars(cfg),'steps':hs,'c_from_velocity':cs,'mismatch':[c-target for c in cs],'velocity':v.tolist(),'richardson_last':(4*cs[-1]-cs[-2])/3,'scope':'floating-point quadrature/refinement, not interval certification'})
  print(item['label'],R,cs,[c-target for c in cs],flush=True)
 out['states'].append(row)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(root/'cartesian_center_strain.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
