"""Complete the self-B2 check of epsilon-zero states with cached own inverses."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,os
import numpy as np
from r2_state_values import R2State
from finite_difference import derivative,safe_ratio
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path('verification/r2_projected_fullplane');old=json.loads((root/'status.json').read_text());start=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','pid':os.getpid(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256((root/'status.json').read_bytes()).hexdigest(),'scope':'True self-induced B2 residuals of epsilon0 projected states; old fd_runs use external velocity instead. Cached velocity is from the original independently written whole-plane evaluator.','states':[]}
for row in old['states']:
 state=R2State(row['file']);invrow=next(z for z in row['inverse_runs'] if z['core']==12 and z['order']==48)
 pts=np.array(invrow['points']);axis=pts[:,0]==0;W=state.beta*pts+np.array(invrow['self']['velocity']);F=state.divided(*pts.T,'F');G=state.divided(*pts.T,'G');T=state.theta(*pts.T);O=state.omega(*pts.T)
 A=np.zeros(len(pts));A[~axis]=W[~axis,0]/pts[~axis,0];inv=CartesianInverse(state.omega,InverseSettings(radius=12.,core_radial_order=48,core_angular_order=48,exterior_radial_order=48,exterior_angular_order=48,decay_power=1/state.bb));axis_checks=[]
 for h in (.004,.002):
  p=pts[axis][0];values=inv.relative(np.array([p+np.array([j*h,0]) for j in (-2,-1,1,2)]))[:,0];aa=state.beta+(values[0]-8*values[1]+8*values[2]-values[3])/(12*h);axis_checks.append({'h':h,'A':float(aa)})
 A[axis]=axis_checks[-1]['A'];r={'file':row['file'],'sha256':state.sha256,'beta':state.beta,'points':pts.tolist(),'axis_checks':axis_checks,'runs':[],'center':state.center()};out['states'].append(r)
 r['center']['b0_minus_4a0_over_beta']=r['center']['G']['value']-4*r['center']['F']['value']/state.beta
 for h in (.001,.0005,.00025):
  f=lambda x,y:state.divided(x,y,'F');g=lambda x,y:state.divided(x,y,'G')
  fx=derivative(f,pts,0,h);fy=derivative(f,pts,1,h);gx=derivative(g,pts,0,h);gy=derivative(g,pts,1,h);tx=derivative(state.theta,pts,0,h);ty=derivative(state.theta,pts,1,h);ox=derivative(state.omega,pts,0,h);oy=derivative(state.omega,pts,1,h)
  terms={'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(state.beta-2)*T)),'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,O,-tx)),'F':np.column_stack((A*(2*F+pts[:,0]*fx),W[:,1]*fy,-(state.beta-2)*F)),'G':np.column_stack((A*(G+pts[:,0]*gx),W[:,1]*gy,G,-2*F-pts[:,0]*fx))}
  run={'h':h}
  for kind,ts in terms.items():
   R=ts.sum(1);N=abs(ts).sum(1);ratio=safe_ratio(R,N)
   run[kind]={'R':R.tolist(),'N':N.tolist(),'ratio':ratio.tolist(),'max_absolute':float(abs(R).max()),'max_normalized_off_axis':float(ratio[~axis].max()),'max_normalized_including_axis':float(ratio.max()) if kind in ('F','G') else None}
  r['runs'].append(run)
 print(state.path.name,{k:(v['max_absolute'],v['max_normalized_off_axis']) for k,v in r['runs'][-1].items() if k!='h'},flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'self_velocity_residuals.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
