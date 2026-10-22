"""FD checks of transported fields, distinct from the imposed power vorticity."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from shifted_power_flow import ShiftedPowerFlow

start=time.monotonic();f=ShiftedPowerFlow(3.);out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Forced transport checks, not self-consistent profiles','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[]}
for point in f.L*np.array([[.05,.06],[.2,-.4],[.6,.5],[1.2,2.],[.02,5.],[2.,-7.]]):
 cache={}
 def val(p):
  key=tuple(p)
  if key not in cache:cache[key]=f.evaluate(p,r_in=1e-5,rtol=3e-11)
  v=cache[key]
  if v['status'] not in ('COMPLETE','LOCAL_JET'):raise RuntimeError(v)
  return np.array([v['Theta'],v['Omega']])
 v=val(point);u,W,J,DW=f.field(point);row={'point':point.tolist(),'value':v.tolist(),'external_omega':float(f.external_omega(*point)),'differences':[]}
 for relh in (.004,.002,.001):
  h=relh*f.L;dd=[]
  for axis in (0,1):
   e=np.eye(2)[axis]*h
   dd.append((val(point-2*e)-8*val(point-e)+8*val(point+e)-val(point+2*e))/(12*h))
  dd=np.array(dd)
  RO=float(W@dd[:,1]+v[1]-dd[0,0]);RT=float(W@dd[:,0]-(f.beta-2)*v[0])
  row['differences'].append({'step':h,'R_Omega':RO,'R_Theta':RT,'gradient_error':float(max(abs(dd[:,0]-np.asarray(cache[tuple(point)]['gradient']))))})
 out['runs'].append(row);print(point,row['differences'][-1],flush=True)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
Path('verification/shifted_power_transport.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
