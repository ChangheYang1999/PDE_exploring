"""Independent finite-difference check of a boundary-compatible flow solution."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from smooth_modal_flow import SmoothModalFlow,reconstruct
from r2_state_values import R2State
from finite_difference import stencil
root=Path('verification/characteristic_derivatives_20261020T2035');root.mkdir(exist_ok=True,parents=True)
base=Path('verification/characteristic_a021hr_20261020T2029');s=R2State(base/'state_snapshot.npz');a0=s.center()['F']['value']
with np.load(base/'inverse_nodes.npz',allow_pickle=False) as z:flow=SmoothModalFlow(s.beta,z['radii'],z['pr'],z['dp'],z['H'])
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','snapshot_sha256':s.sha256,'rows':[]};zz,ww=stencil(1,3)
points=[[.8318938104,2.4506801393],[-2.8780907797,.9769801726],[1.,1.]]
cache={}
def run(X):
 key=tuple(X)
 if key not in cache:
  v=reconstruct(flow,X,s.beta,a0,cutoff=.001,rtol=2e-13,atol=2e-16,compatible_seed=True)
  assert v['status']=='COMPLETE';cache[key]=v
 return cache[key]
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for X in points:
 X=np.array(X);mid=run(X);W=flow.W(X)
 for h in [2e-4,1e-4]:
  step=h*max(1,np.linalg.norm(X));dt=[];do=[]
  for axis in [0,1]:
   rr=[]
   for z in zz:
    P=X.copy();P[axis]+=step*z;rr.append(run(P))
   dt.append(np.dot(ww,[v['Theta'] for v in rr])/step);do.append(np.dot(ww,[v['Omega'] for v in rr])/step)
  dt=np.array(dt);do=np.array(do);rt=float(W@dt-(s.beta-2)*mid['Theta']);ro=float(W@do+mid['Omega']-dt[0])
  row={'point':X.tolist(),'relative_step':h,'Theta':mid['Theta'],'Omega':mid['Omega'],'gradient':mid['gradient'],'gradient_fd':dt.tolist(),'gradient_fd_max_difference':float(max(abs(dt-mid['gradient']))),'RTheta':rt,'ROmega':ro,'NTheta':float(np.sum(abs(W*dt))+abs((s.beta-2)*mid['Theta'])),'NOmega':float(np.sum(abs(W*do))+abs(mid['Omega'])+abs(dt[0])),'gradient_seed_correction':mid['gradient_seed_correction']}
  row['Theta_ratio']=abs(rt)/row['NTheta'];row['Omega_ratio']=abs(ro)/row['NOmega'];out['rows'].append(row);save();print(row,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),number_of_characteristics=len(cache),scope='Transport equations for an independently interpolated fixed forced velocity at a finite cutoff. No coupled inverse consistency or profile. Finite differences and tolerance tests are not interval certificates.')
out['code_hashes']={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['smooth_modal_flow.py','characteristic_derivative_audit.py']};save();print('COMPLETE',out['elapsed_seconds'],flush=True)
