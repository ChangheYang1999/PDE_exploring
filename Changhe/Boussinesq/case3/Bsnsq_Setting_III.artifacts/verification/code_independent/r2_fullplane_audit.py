"""Independent Cartesian full-plane audit of two fixed-beta initial states.

SciPy spline values, seven-point Cartesian derivatives, Duffy singular quadrature
and four-side infinite exterior quadrature. No numerics-lane source imports.
Both the represented forcing and the represented transported vorticity are
inverted; epsilon0 is explicitly a forced problem, not a profile candidate.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, time
import numpy as np
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse, InverseSettings
from finite_difference import derivative, safe_ratio
from gaussian_characteristics import GaussianFlow

root=Path('verification/r2_projected_fullplane');root.mkdir(exist_ok=True)
start=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','pid':os.getpid(),
     'scope':'Unconverged projected epsilon0 states. Whole-plane inversion of the actual spline continuations, not their fitting-lane velocity interpolants. No B2 candidate.',
     'zero_rule':'N=R=0 gives0; N=0 and R!=0 gives infinity; no floor. Exact-axis original ratios are not used in maxima because roundoff cancellation can dominate. Axis equations use divided limits.',
     'source_hashes':{name:hashlib.sha256(Path('code_independent',name).read_bytes()).hexdigest() for name in ('r2_fullplane_audit.py','r2_state_values.py','cartesian_inverse.py','finite_difference.py')},'states':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start
 (root/'status.json').write_text(json.dumps(out,indent=2)+'\n')
save()
points=np.array([[.13,.27],[.63,-.42],[1.13,.73],[0.,.81],[-.63,-.42],[.47,0.],[2.03,-1.17]])
for filename in ('fb30b_eps0.npz','fb25b_eps0.npz'):
 state=R2State(Path('candidate_snapshots/num_homotopy_20261020T1539')/filename)
 row={'file':str(state.path),'sha256':state.sha256,'meta':state.meta,'center':state.center(),'inverse_runs':[],'fd_runs':[],'elliptic_checks':[],'truncated_center':[]}
 out['states'].append(row);save()
 f=lambda x,y:state.divided(x,y,'F');g=lambda x,y:state.divided(x,y,'G')
 ext=lambda x,y:np.asarray(x)*state.divided(x,y,'external')
 beta=state.beta;axis=points[:,0]==0;F=f(*points.T);G=g(*points.T);Theta=state.theta(*points.T);Omega=state.omega(*points.T)
 gflow=GaussianFlow(c=1+beta/2)
 exact_ext_velocity=np.array([gflow.field(p)[0] for p in points])-np.array([0.,gflow.u0])
 final_ext=None
 for core in (6.,12.,24.):
  for order in (16,32,48):
   settings=InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/state.bb)
   vals={}
   for kind,omega in [('external',ext),('self',state.omega)]:
    inv=CartesianInverse(omega,settings);v=inv.relative(points);trunc=inv.relative(points,include_exterior=False)
    vals[kind]={'velocity':v.tolist(),'without_exterior':trunc.tolist(),'omitted_exterior_max':float(np.max(np.abs(v-trunc)))}
    if kind=='external':
     vals[kind]['difference_from_exact_gaussian_max']=float(np.max(np.abs(v-exact_ext_velocity)))
     if core==12. and order==48:final_ext=v
   row['inverse_runs'].append({'core':core,'order':order,'points':points.tolist(),**vals});save()
   print(filename,'inverse',core,order,'elapsed',time.monotonic()-start,flush=True)
 W=beta*points+final_ext;A=np.empty(len(points));A[~axis]=W[~axis,0]/points[~axis,0]
 # On x=0, use an independent inverse difference for d_x V1, not a fitted jet.
 inv=CartesianInverse(ext,InverseSettings(radius=12.,core_radial_order=48,core_angular_order=48,exterior_radial_order=48,exterior_angular_order=48,decay_power=1/state.bb))
 axis_values=[]
 for h in (.004,.002):
  p=points[axis][0];nodes=np.array([p+np.array([j*h,0]) for j in (-2,-1,1,2)])
  vx=inv.relative(nodes)[:,0];ax=(vx[0]-8*vx[1]+8*vx[2]-vx[3])/(12*h)
  axis_values.append({'h':h,'A':float(beta+ax)})
 A[axis]=axis_values[-1]['A'];row['axis_inverse_difference']=axis_values
 for h in (.001,.0005,.00025):
  Fx=derivative(f,points,0,h);Fy=derivative(f,points,1,h);Gx=derivative(g,points,0,h);Gy=derivative(g,points,1,h)
  tx=derivative(state.theta,points,0,h);ty=derivative(state.theta,points,1,h);ox=derivative(state.omega,points,0,h);oy=derivative(state.omega,points,1,h)
  terms={'F':np.column_stack((A*(2*F+points[:,0]*Fx),W[:,1]*Fy,-(beta-2)*F)),
         'G':np.column_stack((A*(G+points[:,0]*Gx),W[:,1]*Gy,G,-2*F-points[:,0]*Fx)),
         'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(beta-2)*Theta)),
         'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,Omega,-tx))}
  result={'h':h,'points':points.tolist(),'W':W.tolist()}
  for kind,ts in terms.items():
   R=ts.sum(1);N=np.abs(ts).sum(1);norm=safe_ratio(R,N)
   result[kind]={'R':R.tolist(),'N':N.tolist(),'normalized':norm.tolist(),'max_absolute':float(np.max(abs(R))),
                 'max_normalized_off_axis':float(np.max(norm[~axis])),
                 'max_normalized_including_axis':float(np.max(norm)) if kind in ('F','G') else None,
                 'zero_N_count':int(np.count_nonzero(N==0)),
                 'subnormal_nonzero_terms':int(np.count_nonzero((abs(ts)>0)&(abs(ts)<np.finfo(float).tiny)))}
  row['fd_runs'].append(result);save()
 # Independent div-curl check is a numerical elliptic diagnostic, not a proof.
 p=np.array([.73,-.39]);om=float(ext(*p))
 for order in (24,48,72):
  check=CartesianInverse(ext,InverseSettings(radius=12.,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/state.bb))
  for h in (.004,.002):
   grad=[]
   for dim in (0,1):
    e=np.zeros(2);e[dim]=h;values=check.relative(np.array([p+j*e for j in (-2,-1,1,2)]))
    grad.append((values[0]-8*values[1]+8*values[2]-values[3])/(12*h))
   J=np.array(grad).T
   row['elliptic_checks'].append({'point':p.tolist(),'order':order,'h':h,'gradient':J.tolist(),'divergence':float(np.trace(J)),'minus_curl_minus_Omega':float(-J[1,0]+J[0,1]-om),'Omega_source':om})
   save()
 invself=CartesianInverse(state.omega)
 for R in (1.,10.,100.,1000.,10000.):
  row['truncated_center'].append(invself.circular_center_moments(R,order=32,panels=32));save()
 print(filename,'COMPLETE',time.monotonic()-start,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save()
print('COMPLETE',out['elapsed_seconds'],flush=True)
