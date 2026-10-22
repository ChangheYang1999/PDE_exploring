"""Independent FD and Cartesian inverse audit of saved global-stream fits."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,os,hashlib
import numpy as np
from global_stream_basis import GlobalBasis,GlobalField,Resolution,stream_term,temperature_term
from finite_difference import derivative
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path('verification/global_stream_saved_audit');root.mkdir(exist_ok=True)
start=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'scope':'Saved failed fits only; numerical conditioning/inverse check, no candidate','cases':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
p=np.array([[0.,0.],[0.,.371],[0.,-.619],[.00013,.00027],[.137,.271],[.791,-.383],[1.137,.739],[3.173,-2.371]])
for tag in ['medium/b2.5_s0','high/b2.5_s0','high/b2.9_s0']:
 path=Path('verification/global_stream_search')/(tag+'_final.npz');z=np.load(path,allow_pickle=False);beta=float(z['beta']);co=z['coefficients'];res=Resolution(*map(int,z['resolution']));field=GlobalField(beta,co,res);basis=GlobalBasis(p,beta,res);a=basis.fields(co)
 row={'file':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':beta,'resolution':res.__dict__,'coefficient_max':float(abs(co).max()),'derivatives':[],'inverse':[]};out['cases'].append(row);save()
 # Recompute each term using extended-precision arithmetic and summation.
 lp=p.astype(np.longdouble);lb=np.longdouble(beta);lc=co.astype(np.longdouble)
 ref=stream_term(lp,lb,(1,1,0));sr=stream_term(lp,lb,(2,1,0));tf=temperature_term(lp,lb,(0,0,0))
 terms={k:[-ref[k]/(2*lb)+(1+lb/2)*sr[k]/2] for k in ref}
 for label,v in zip(basis.stream_labels,lc[:basis.nv]):
  k,n,j=label;s=stream_term(lp,lb,label)
  for key in s:terms[key].append(v*(s[key]-int(k==1 and j<=1)*ref[key]-int(k==2 and j==0)*sr[key]))
 for key in tf:terms[key]=[tf[key]]
 for label,v in zip(basis.temperature_labels,lc[basis.nv:]):
  l,h,j=label;s=temperature_term(lp,lb,label)
  for key in s:terms[key].append(v*(s[key]-int(l==0 and j==0)*tf[key]))
 aa={k:np.sum(np.stack(ts),axis=0,dtype=np.longdouble) for k,ts in terms.items()};aa['A']+=lb;aa['B']+=lb*lp[:,1]
 row['longdouble_difference']={k:float(abs(aa[k]-a[k]).max()) for k in aa}
 row['absolute_sum_of_terms_max']={k:float(np.sum(abs(np.stack(ts)),axis=0).max()) for k,ts in terms.items()}
 row['longdouble_bits']=int(np.finfo(np.longdouble).nmant)
 for h in (.004,.002,.001):
  vel=np.column_stack((-derivative(field.psi,p,1,h),derivative(field.psi,p,0,h)))
  ell=-derivative(field.psi,p,0,h,order=2)-derivative(field.psi,p,1,h,order=2)-field.omega(*p.T)
  fx=derivative(lambda x,y:field.fields(x,y)['F'],p,0,h);fy=derivative(lambda x,y:field.fields(x,y)['F'],p,1,h)
  gx=derivative(lambda x,y:field.fields(x,y)['G'],p,0,h);gy=derivative(lambda x,y:field.fields(x,y)['G'],p,1,h)
  A=a['A'];B=a['B'];x=p[:,0];F=a['F'];G=a['G'];rf=A*(2*F+x*fx)+B*fy-(beta-2)*F;rg=A*(G+x*gx)+B*gy+G-2*F-x*fx
  rr=basis.residual(co);row['derivatives'].append({'h':h,'velocity_max_error':float(abs(vel-field.velocity(p)).max()),'elliptic_max_error':float(abs(ell).max()),'F_gradient_max_error':float(max(abs(fx-a['Fx']).max(),abs(fy-a['Fy']).max())),'G_gradient_max_error':float(max(abs(gx-a['Gx']).max(),abs(gy-a['Gy']).max())),'divided_residual_max_difference':float(abs(np.r_[rf,rg]-rr).max()),'RF_max':float(abs(rf).max()),'RG_max':float(abs(rg).max())});save()
 probes=p[[4,5,6]]
 for core in (4.,8.,16.):
  for order in (16,32,48):
   inv=CartesianInverse(field.omega,InverseSettings(core,order,order,order,order,1/beta));v=inv.relative(probes);expected=field.velocity(probes)
   row['inverse'].append({'core':core,'order':order,'points':probes.tolist(),'value':v.tolist(),'expected':expected.tolist(),'max_absolute_error':float(abs(v-expected).max())});save()
   print(tag,'core',core,'order',order,'error',row['inverse'][-1]['max_absolute_error'],'elapsed',time.monotonic()-start,flush=True)
 row['status']='COMPLETE';save()
out['status']='COMPLETE';out['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['elapsed_seconds'],flush=True)
