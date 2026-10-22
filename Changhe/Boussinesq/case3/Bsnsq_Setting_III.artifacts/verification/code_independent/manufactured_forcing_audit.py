"""Independent differential residuals of the nonlinear manufactured problem.

Only serialized values are read. No numerics-lane code is imported or run.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,os,hashlib
import numpy as np
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative,safe_ratio
root=Path('verification/manufactured_20261020T1915')
start=time.monotonic()
s0=R2State(root/'snapshots/fb30g_eps0.npz')
p=np.array([[0.,0.],[.00013,.00027],[.031,.023],[.13,.27],[.63,-.42],[1.13,.73],[0.,.81],[0.,-.81],[-.63,-.42],[.47,0.],[2.03,-1.17],[4.7,8.2]])
axis=p[:,0]==0
def Fv(x,y):
 return np.asarray(x)*s0.divided(x,y,'external')-s0.omega(x,y)
def inverse(fun,core,order):
 return CartesianInverse(fun,InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/s0.bb))
def diagnose(s,V,A,h):
 W=s.beta*p+V;x=p[:,0]
 F=lambda x,y:s.divided(x,y,'F')
 G=lambda x,y:s.divided(x,y,'G')
 fv,gv=F(*p.T),G(*p.T)
 fx,fy=derivative(F,p,0,h),derivative(F,p,1,h)
 gx,gy=derivative(G,p,0,h),derivative(G,p,1,h)
 tx,ty=derivative(s.theta,p,0,h),derivative(s.theta,p,1,h)
 ox,oy=derivative(s.omega,p,0,h),derivative(s.omega,p,1,h)
 terms={'F':np.column_stack((A*(2*fv+x*fx),W[:,1]*fy,-(s.beta-2)*fv)),
        'G':np.column_stack((A*(gv+x*gx),W[:,1]*gy,gv,-(2*fv+x*fx))),
        'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(s.beta-2)*s.theta(*p.T))),
        'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,s.omega(*p.T),-tx))}
 result={'h':h,'W':W.tolist(),'A':A.tolist()}
 for name,t in terms.items():
  r=t.sum(1);n=abs(t).sum(1);rat=safe_ratio(r,n);take=np.ones(len(p),bool) if name in ('F','G') else ~axis
  ai=int(np.argmax(abs(r)));ri=int(np.flatnonzero(take)[np.argmax(rat[take])])
  result[name]={'R':r.tolist(),'N':n.tolist(),'ratio':rat.tolist(),'max_abs':float(abs(r[ai])),'max_abs_point':p[ai].tolist(),'max_ratio':float(rat[ri]),'max_ratio_point':p[ri].tolist(),'zeros_N':int((n==0).sum()),'subnormal_terms':int(((abs(t)>0)&(abs(t)<np.finfo(float).tiny)).sum())}
 return result
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','pid':os.getpid(),'points':p.tolist(),'states':[],
 'code_sha256':{n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['manufactured_forcing_audit.py','r2_state_values.py','cartesian_inverse.py','finite_difference.py']},
 'forced_definition':'Omega_velocity = Omega_state + Omega_external_from_S0 - Omega_S0; transported Omega = Omega_state',
 'normalizers':'Grouped absolute transport terms; no floor. Cartesian on-axis ratios excluded from maxima; divided axis limits retained.'}
def save():
 out['elapsed_seconds']=time.monotonic()-start
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for file in ['fb30g_eps0.npz','man_pic1.npz']:
 s=R2State(root/'snapshots'/file)
 row={'file':file,'sha256':s.sha256,'meta':s.meta,'center':s.center(),'runs':[]};out['states'].append(row)
 def force(x,y):return s.omega(x,y)+Fv(x,y)
 for core in [12.,24.,48.]:
  for order in [32,64]:
   for label,fun in [('forced',force),('self',s.omega)]:
    vi=inverse(fun,core,order);V=vi.relative(p)
    A=np.empty(len(p));A[~axis]=s.beta+V[~axis,0]/p[~axis,0]
    ad=[]
    for h in [4e-5,2e-5]:
     pp=p[axis].copy();dx=np.array([[-2*h,0],[-h,0],[h,0],[2*h,0]])
     vp=vi.relative((pp[:,None,:]+dx[None,:,:]).reshape(-1,2)).reshape(len(pp),4,2)
     ax=s.beta+(vp[:,0,0]-8*vp[:,1,0]+8*vp[:,2,0]-vp[:,3,0])/(12*h)
     A[axis]=ax
     d=diagnose(s,V,A,h);d.update(kind=label,core=core,order=order)
     row['runs'].append(d);ad.append(ax.tolist())
    save();print(file,label,core,order,'seconds',time.monotonic()-start,flush=True)
 row['status']='COMPLETE';save()
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
