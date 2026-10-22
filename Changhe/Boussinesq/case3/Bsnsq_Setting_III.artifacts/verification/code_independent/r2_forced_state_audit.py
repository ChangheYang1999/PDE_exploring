"""Independent Cartesian/axis audit of archived epsilon0 r2 spline states.
Uses an analytic external whole-plane inverse, finite differences, no num code.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from r2_state_values import R2State
from gaussian_characteristics import GaussianFlow
from finite_difference import derivative,safe_ratio

start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Unconverged epsilon0 forced states, not B2 candidates. External inverse used exactly; self-consistent full inverse is not claimed.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'zero_rule':'N=R=0 ->0; N=0,R!=0 ->infinity. No floor. No nonzero sampled term was below normal floating-point range.','axis_note':'Original undivided odd derivatives at exact x=0 have floating-point cancellation terms. Ratios there are retained but not used as a physical defect. Divided equations supply the axis check.','states':[]}
for filename in ('fb30_eps0.npz','fb25_eps0.npz'):
 state=R2State(Path('candidate_snapshots/num_homotopy_20261020T1507')/filename)
 flow=GaussianFlow(c=1+state.beta/2)
 row={'filename':filename,'sha256':state.sha256,'center':state.center(),'runs':[]}
 for radial in (.001,.01,.1,1.,3.,10.,100.,10000.):
  ph=np.array([0.,.07,.43,.86,np.pi/2,2.21,np.pi-.09,np.pi])
  points=radial*np.column_stack((np.sin(ph),-np.cos(ph)));points[[0,-1],0]=0
  Ffun=lambda x,y:state.divided(x,y,'F');Gfun=lambda x,y:state.divided(x,y,'G')
  F=Ffun(*points.T);G=Gfun(*points.T);th=state.theta(*points.T);om=state.omega(*points.T)
  data=[flow.field(p) for p in points];W=np.array([a[1] for a in data]);axis=points[:,0]==0
  A=np.empty(len(points));A[~axis]=W[~axis,0]/points[~axis,0];A[axis]=np.array([a[3][0,0] for a in data])[axis]
  for eps in (1e-3,5e-4,2.5e-4):
   step=eps*max(.01,radial)
   Fx=derivative(Ffun,points,0,step);Fy=derivative(Ffun,points,1,step)
   Gx=derivative(Gfun,points,0,step);Gy=derivative(Gfun,points,1,step)
   tx=derivative(state.theta,points,0,step);ty=derivative(state.theta,points,1,step)
   ox=derivative(state.omega,points,0,step);oy=derivative(state.omega,points,1,step)
   tf=np.column_stack((A*(2*F+points[:,0]*Fx),W[:,1]*Fy,-(state.beta-2)*F))
   tg=np.column_stack((A*(G+points[:,0]*Gx),W[:,1]*Gy,G,-(2*F+points[:,0]*Fx)))
   tt=np.column_stack((W[:,0]*tx,W[:,1]*ty,-(state.beta-2)*th))
   to=np.column_stack((W[:,0]*ox,W[:,1]*oy,om,-tx))
   terms={'F':tf,'G':tg,'Theta':tt,'Omega':to}
   record={'radius':radial,'relative_step':eps,'step':step,'points':points.tolist()}
   for kind,ts in terms.items():
    R=ts.sum(1);N=np.abs(ts).sum(1);nr=safe_ratio(R,N)
    record[kind]={'R':R.tolist(),'N':N.tolist(),'normalized':nr.tolist(),'max_absolute':float(np.max(abs(R))),'max_normalized':float(np.max(nr)),'zero_N_count':int(np.count_nonzero(N==0)),'max_normalized_off_axis':float(np.max(nr[~axis])),'subnormal_nonzero_term_count':int(np.count_nonzero((np.abs(ts)>0)&(np.abs(ts)<np.finfo(float).tiny)))}
   row['runs'].append(record)
  r=row['runs'][-1];print(filename,radial,{k:(r[k]['max_absolute'],r[k]['max_normalized']) for k in ('F','G','Theta','Omega')},flush=True)
 out['states'].append(row)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
Path('verification/r2_forced_state_audit.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'])
