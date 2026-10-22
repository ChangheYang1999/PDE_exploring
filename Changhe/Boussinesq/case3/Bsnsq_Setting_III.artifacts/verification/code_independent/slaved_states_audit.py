"""Independent whole-plane audit; no fitting-lane imports or execution."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,json,hashlib
import numpy as np
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative,safe_ratio
root=Path('verification/slaved_states_20261020T1900')
t0=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','pid':os.getpid(),'states':[],
     'code_sha256':{n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['slaved_states_audit.py','r2_state_values.py','cartesian_inverse.py','finite_difference.py']},
     'scope':'Intermediate homotopy states. True B2 residual uses self inverse. Forced residual uses mixed inverse. Actual represented a0 retained.'}
def save():
 out['elapsed_seconds']=time.monotonic()-t0
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
def inv(state,kind,core,order):
 source=state.omega if kind=='self' else state.mixed_omega
 return CartesianInverse(source,InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/state.bb))
def residual(state,p,V,A,h):
 x=p[:,0];W=state.beta*p+V;off=x!=0
 f=lambda x,y:state.divided(x,y,'F');g=lambda x,y:state.divided(x,y,'G')
 F=f(*p.T);G=g(*p.T);fx=derivative(f,p,0,h);fy=derivative(f,p,1,h);gx=derivative(g,p,0,h);gy=derivative(g,p,1,h)
 tx=derivative(state.theta,p,0,h);ty=derivative(state.theta,p,1,h);ox=derivative(state.omega,p,0,h);oy=derivative(state.omega,p,1,h)
 terms={'F':np.column_stack((A*(2*F+x*fx),W[:,1]*fy,-(state.beta-2)*F)),
        'G':np.column_stack((A*(G+x*gx),W[:,1]*gy,G,-(2*F+x*fx))),
        'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(state.beta-2)*state.theta(*p.T))),
        'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,state.omega(*p.T),-tx))}
 ans={'h':h,'points':p.tolist(),'W':W.tolist(),'A':A.tolist()}
 for key,t in terms.items():
  r=t.sum(1);n=abs(t).sum(1);q=safe_ratio(r,n);take=np.ones(len(p),dtype=bool) if key in ('F','G') else off
  im=np.flatnonzero(take)[np.argmax(q[take])]
  ans[key]={'R':r.tolist(),'N':n.tolist(),'ratio':q.tolist(),'max_abs':float(abs(r).max()),'max_ratio':float(q[take].max()),'max_ratio_point':p[im].tolist(),'zero_N':int((n==0).sum()),'subnormal_terms':int(((abs(t)>0)&(abs(t)<np.finfo(float).tiny)).sum())}
 return ans
p=np.array([[.00013,.00027],[.031,.023],[.13,.27],[.63,-.42],[1.13,.73],[0.,.81],[0.,-.81],[-.63,-.42],[.47,0.],[2.03,-1.17],[4.7,8.2]])
axis=p[:,0]==0
for rec in json.loads((root/'sources.json').read_text()):
 s=R2State(rec['snapshot']);cc=s.center();a=cc['F']['value'];b=cc['G']['value'];c=cc['c_self']
 center={'a0_represented':a,'a0_metadata':s.meta.get('a0'),'a0_metadata_discrepancy':a-float(s.meta.get('a0',a)),
 'b0':b,'b0_minus_4a0_over_beta':b-4*a/s.beta,'c_self':c,'c_self_minus_required':c-1-s.beta/2,
 'R_F_self':(2*(s.beta-c)-(s.beta-2))*a,'R_G_self':(s.beta-c+1)*b-2*a,'F_y':cc['F']['dy'],'G_y':cc['G']['dy']}
 row={'file':Path(rec['snapshot']).name,'sha256':s.sha256,'meta':s.meta,'center':center,'inverse_runs':[],'residual_runs':[],'far_runs':[]};out['states'].append(row);save()
 for core in (12.,24.,48.):
  for order in (32,64):
   run={'core':core,'order':order,'points':p.tolist()}
   for kind in ('self','mixed'):
    vi=inv(s,kind,core,order);V=vi.relative(p)
    run[kind]={'V':V.tolist(),'omitted_exterior_max':float(abs(V-vi.relative(p,include_exterior=False)).max())}
    if core==24.:
     A=np.empty(len(p));A[~axis]=s.beta+V[~axis,0]/p[~axis,0]
     axis_checks=[]
     for hh in (.0005,.00025):
      for j in np.flatnonzero(axis):
       q=p[j]+np.array([[-2*hh,0],[-hh,0],[hh,0],[2*hh,0]])
       vals=vi.relative(q)[:,0];aa=s.beta+(vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*hh)
       axis_checks.append({'point':p[j].tolist(),'h':hh,'A':float(aa)})
       if hh==.00025:A[j]=aa
     for h in (.00008,.00004):
      rr=residual(s,p,V,A,h);rr.update(kind=kind,core=core,order=order,axis_checks=axis_checks);row['residual_runs'].append(rr)
   row['inverse_runs'].append(run);save();print(row['file'],core,order,'elapsed',time.monotonic()-t0,flush=True)
 angles=np.array([.273,1.137]);far=100*np.column_stack((np.cos(angles),np.sin(angles)))
 for core in (200.,400.,800.):
  for order in (32,64):
   vi=inv(s,'self',core,order);V=vi.relative(far);A=s.beta+V[:,0]/far[:,0]
   rr=residual(s,far,V,A,.001);rr.update(kind='self',core=core,order=order,a_scaled=(100**(1/s.beta)*s.omega(*far.T)).tolist(),h_scaled=(100**(-(1-2/s.beta))*s.theta(*far.T)).tolist())
   row['far_runs'].append(rr);save()
 row['parity']={'Theta_even':float(s.theta(.739,-.381)-s.theta(-.739,-.381)),'Omega_odd':float(s.omega(.739,-.381)+s.omega(-.739,-.381))}
 row['status']='COMPLETE';save();print(row['file'],'COMPLETE',time.monotonic()-t0,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
