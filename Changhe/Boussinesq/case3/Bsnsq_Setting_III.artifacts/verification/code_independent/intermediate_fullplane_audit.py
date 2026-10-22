"""Independent Cartesian audit of saved, forced epsilon0.34 intermediate states.
SciPy value reader, seven-point Cartesian differences, own Duffy/infinite
exterior inverse. No fitting-lane code is imported or executed.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,time,json,hashlib
import numpy as np
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative,safe_ratio

snapshot=Path(Path('verification/latest_intermediate_snapshot.txt').read_text().strip())
root=Path('verification/intermediate_fullplane_20261020T1640');root.mkdir(exist_ok=True)
started=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','pid':os.getpid(),'snapshot':str(snapshot),'scope':'Intermediate forced epsilon0.34 states, not published B2 candidates. Actual B2 residual uses self-source inverse. Forced homotopy residual also recorded separately.','normalization':'Cartesian N as prompt. Divided F denominator is sum abs of 2AF, AxFx, BFy, -(beta-2)F; G sum abs of AG, AxGx, BGy, G, -2F, -xFx. No floor;0/0=0, nonzero/0=infinity. Original Cartesian axis ratios are vacuous and excluded from maxima; divided axis values reported.','sources':{},'states':[]}
for name in ('intermediate_fullplane_audit.py','r2_state_values.py','cartesian_inverse.py','finite_difference.py'):
 out['sources'][name]=hashlib.sha256(Path('code_independent',name).read_bytes()).hexdigest()
def save():
 out['elapsed_seconds']=time.monotonic()-started
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
save()
points=np.array([[.00013,.00027],[.031,.023],[.13,.27],[.63,-.42],[1.13,.73],[0.,.81],[0.,-.81],[-.63,-.42],[.47,0.],[2.03,-1.17],[4.7,8.2]])
axis=points[:,0]==0

def inverse(state,kind,core,order):
 fun=state.omega if kind=='self' else state.mixed_omega
 return CartesianInverse(fun,InverseSettings(radius=core,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/state.bb))

def residuals(state,p,V,A,h):
 beta=state.beta;x=p[:,0];W=beta*p+V;axes=x==0
 f=lambda x,y:state.divided(x,y,'F');g=lambda x,y:state.divided(x,y,'G')
 F=f(*p.T);G=g(*p.T);T=state.theta(*p.T);O=state.omega(*p.T)
 Fx=derivative(f,p,0,h);Fy=derivative(f,p,1,h);Gx=derivative(g,p,0,h);Gy=derivative(g,p,1,h)
 tx=derivative(state.theta,p,0,h);ty=derivative(state.theta,p,1,h);ox=derivative(state.omega,p,0,h);oy=derivative(state.omega,p,1,h)
 terms={'F':np.column_stack((2*A*F,A*x*Fx,W[:,1]*Fy,-(beta-2)*F)),
        'G':np.column_stack((A*G,A*x*Gx,W[:,1]*Gy,G,-2*F,-x*Fx)),
        'Theta':np.column_stack((W[:,0]*tx,W[:,1]*ty,-(beta-2)*T)),
        'Omega':np.column_stack((W[:,0]*ox,W[:,1]*oy,O,-tx))}
 result={'h':h,'points':p.tolist(),'W':W.tolist(),'A':A.tolist()}
 for key,ts in terms.items():
  R=ts.sum(axis=1);N=abs(ts).sum(axis=1);ratio=safe_ratio(R,N)
  result[key]={'R':R.tolist(),'N':N.tolist(),'ratio':ratio.tolist(),'max_absolute':float(abs(R).max()),'max_normalized_off_axis':float(ratio[~axes].max()),'max_normalized_including_axis':float(ratio.max()) if key in ('F','G') else None,'zero_N':int((N==0).sum()),'subnormal_terms':int(((abs(ts)>0)&(abs(ts)<np.finfo(float).tiny)).sum())}
 return result

for filename in ('fb30d_eps0.34.npz','fb25d_eps0.34.npz','fb30e_eps0.34.npz'):
 state=R2State(snapshot/filename)
 row={'file':filename,'sha256':state.sha256,'meta':state.meta,'center':state.center(),'inverse_runs':[],'residual_runs':[],'far_runs':[],'parity':{},'divcurl':[]}
 out['states'].append(row);save()
 for core in (12.,24.,48.):
  for order in (24,48,72):
   rr={'core':core,'order':order,'points':points.tolist()}
   for kind in ('self','mixed'):
    inv=inverse(state,kind,core,order);V=inv.relative(points);cut=inv.relative(points,include_exterior=False)
    A=np.empty(len(points));A[~axis]=state.beta+V[~axis,0]/points[~axis,0]
    if core==24. and order in (48,72):
     axisdata=[]
     for h in (.0005,.00025):
      for i,p in enumerate(points):
       if not axis[i]:continue
       stencil=np.array([p+np.array([j*h,0.]) for j in (-2,-1,1,2)])
       vx=inv.relative(stencil)[:,0];ax=(vx[0]-8*vx[1]+8*vx[2]-vx[3])/(12*h)
       axisdata.append({'point':p.tolist(),'h':h,'A':float(state.beta+ax)})
       if h==.00025:A[i]=state.beta+ax
     for h in (.00008,.00004,.00002):
      record=residuals(state,points,V,A,h);record.update(kind=kind,core=core,order=order,axis_inverse_differences=axisdata)
      row['residual_runs'].append(record)
    rr[kind]={'V':V.tolist(),'without_exterior':cut.tolist(),'omitted_exterior_max':float(abs(V-cut).max())}
   row['inverse_runs'].append(rr);save()
   print(filename,'inverse',core,order,'elapsed',time.monotonic()-started,flush=True)
 # Far-region residual and leading-tail samples. These are finite samples, not a uniform tail certification.
 for radius in (10.,100.,1000.):
  angles=np.array([.273,1.137,2.419]);p=radius*np.column_stack((np.cos(angles),np.sin(angles)))
  for factor in (2.,4.,8.):
   for order in (24,48,72):
    rr={'radius':radius,'core_factor':factor,'order':order,'points':p.tolist(),'a_scaled':(radius**(1/state.beta)*state.omega(*p.T)).tolist(),'h_scaled':(radius**(-(1-2/state.beta))*state.theta(*p.T)).tolist()}
    for kind in ('self','mixed'):
     inv=inverse(state,kind,factor*radius,order);V=inv.relative(p);AA=state.beta+V[:,0]/p[:,0]
     rr[kind]={'V':V.tolist()}
     if factor==4 and order in (48,72):rr[kind]['residual']=residuals(state,p,V,AA,radius*1e-5)
    row['far_runs'].append(rr);save()
  print(filename,'far',radius,'elapsed',time.monotonic()-started,flush=True)
 # Explicit parity in field values and independent inverse at one non-axis reflection pair.
 pair=np.array([[.739,-.381],[-.739,-.381]])
 vals=inverse(state,'self',24.,72).relative(pair)
 row['parity']={'points':pair.tolist(),'Theta_even_defect':float(state.theta(*pair[0])-state.theta(*pair[1])),'Omega_odd_defect':float(state.omega(*pair[0])+state.omega(*pair[1])),'V1_odd_defect':float(vals[0,0]+vals[1,0]),'V2_even_defect':float(vals[0,1]-vals[1,1])}
 # Physical-space div-curl diagnostic at a point off the spline knots.
 p=np.array([.739,-.381])
 for order in (48,72):
  for h in (.004,.002):
   for kind in ('self','mixed'):
    inv=inverse(state,kind,24.,order);grad=[]
    for dim in (0,1):
     ee=np.zeros(2);ee[dim]=h
     vals=inv.relative(np.array([p+j*ee for j in (-2,-1,1,2)]))
     grad.append((vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*h))
    J=np.array(grad).T;source=state.omega(*p) if kind=='self' else state.mixed_omega(*p)
    row['divcurl'].append({'kind':kind,'order':order,'h':h,'point':p.tolist(),'J':J.tolist(),'div':float(np.trace(J)),'minus_curl_minus_source':float(-J[1,0]+J[0,1]-source),'source':float(source),'source_minus_profile_Omega':float(source-state.omega(*p))})
 print(filename,'COMPLETE',time.monotonic()-started,flush=True);save()
out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save()
print('COMPLETE',out['elapsed_seconds'],flush=True)
