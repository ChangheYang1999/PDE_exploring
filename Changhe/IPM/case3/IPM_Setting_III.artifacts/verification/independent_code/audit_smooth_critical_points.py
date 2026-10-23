"""Finite critical-point search, independently proved in CRITICAL_POINT_PROOF.md.
Only saved coefficients are loaded. This is no completeness certificate.
"""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,math
import numpy as np
from scipy.optimize import brentq,least_squares
from complementary_inverse_charts import SmoothAngular,FullChart,point_fields
from angular_log_inverse import AngularLogInverse
from smooth_mp_primitives import SmoothMP

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
root=Path('research/smooth_N44_refinement_audit/verification/critical_points');root.mkdir(exist_ok=True)
proof=root.parent.parent/'CRITICAL_POINT_PROOF.md'
inputs=json.loads((root.parent/'THREE_RESOLUTIONS.json').read_text())['rows']
result=dict(started_utc=utc(),pid=os.getpid(),status='RUNNING',proof_sha256=sha(proof),code_sha256=sha(__file__),implementation_sha256={str(p):sha(p)for p in [Path('independent_code')/name for name in ['complementary_inverse_charts.py','angular_log_inverse.py','smooth_mp_primitives.py']]},states=[],scope='Finite nested searches in the closed first quadrant plus sampled sign-change root finding, not a proof that the critical-point list is complete. W=ell X+U equilibria and density critical points are different tests. No denominator floor.')
def save():result['updated_utc']=utc();(root/'AUDIT.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
def grids(model,lr,th,order):
 shape=(len(lr),len(th));fields={k:np.empty(shape)for k in ['wx','wy','gx','gy','rho_over_r']}
 sine=np.sin(th);cosine=np.cos(th);sine[th==0]=0.;cosine[th==np.pi/2]=0.
 for defect in [True,False]:
  ids=np.flatnonzero((lr<=model.log_core)==defect)
  if not len(ids):continue
  owner=model if defect else FullChart(model);f=AngularLogInverse(owner,order).fields(lr[ids],th)
  fields['wx'][ids]=model.cl*cosine+f['ur']*cosine-f['ut']*sine
  fields['wy'][ids]=model.cl*sine+f['ur']*sine+f['ut']*cosine
  fields['gx'][ids]=f['grad_radial']*cosine-f['grad_angular']*sine
  fields['gy'][ids]=f['grad_radial']*sine+f['grad_angular']*cosine
  fields['rho_over_r'][ids]=f['H']+owner.a*sine
 for k in ['wx','gx']:fields[k][:,th==np.pi/2]=0.
 for k in ['wy','gx']:fields[k][:,th==0]=0.
 scale=np.exp(model.alpha*np.logaddexp(0.,2*lr))[:,None]
 fields['gx_scaled']=fields['gx']*scale;fields['gy_scaled']=fields['gy']*scale
 fields['Wnorm_scaled']=np.hypot(fields['wx'],fields['wy'])
 fields['gradnorm_scaled']=np.hypot(fields['gx_scaled'],fields['gy_scaled'])
 fields['W1_over_x']=np.divide(fields['wx'],cosine,out=np.full(shape,np.nan),where=cosine!=0)
 fields['W2_over_y']=np.divide(fields['wy'],sine,out=np.full(shape,np.nan),where=sine!=0)
 return fields

def point(model,z,kind):
 f=point_fields(model,np.array([z[0]]),np.array([z[1]]),192)[0]
 if kind=='equilibrium':v=np.array([model.cl*math.cos(z[1])+f['U_over_r'][0],model.cl*math.sin(z[1])+f['U_over_r'][1]])
 else:v=np.array(f['gradient'])*math.exp(model.alpha*np.logaddexp(0.,2*z[0]))
 if z[1]==0:v[1 if kind=='equilibrium' else 0]=0.
 if z[1]==np.pi/2:v[0]=0.
 return v

def witness(values,lr,th,mask):
 allowed=np.broadcast_to(mask[:,None],values.shape)&np.isfinite(values)
 idx=np.unravel_index(np.argmin(np.where(allowed,values,np.inf)),values.shape)
 rr=float(np.exp(lr[idx[0]]));tt=float(th[idx[1]])
 return dict(value=float(values[idx]),log_radius=float(lr[idx[0]]),radius=rr,theta=tt,x=0. if tt==np.pi/2 else rr*math.cos(tt),y=0. if tt==0 else rr*math.sin(tt))

def cells_straddling(a,b):
 def bounds(v):
  corners=np.stack([v[:-1,:-1],v[1:,:-1],v[:-1,1:],v[1:,1:]])
  return corners.min(axis=0),corners.max(axis=0)
 alo,ahi=bounds(a[:,1:-1]);blo,bhi=bounds(b[:,1:-1])
 return np.argwhere((alo<=0)&(ahi>=0)&(blo<=0)&(bhi>=0))+np.array([0,1])

save()
for data in inputs:
 tag=data['tag'];source=Path(data['source']);assert sha(source)==data['sha256'];model=SmoothAngular(source)
 inputpath=Path('evidence/smooth_exact_jets')/tag/'exact_input.json';exact=json.loads(inputpath.read_text());assert exact['source_sha256']==sha(source)
 state=dict(tag=tag,source=str(source),source_sha256=sha(source),exact_input=str(inputpath),exact_input_sha256=sha(inputpath),started_utc=utc(),status='RUNNING',origin=dict(W=[0,0],gradient=[0,float(model.exact_a)],DW_diagonal=[model.cl-model.c,model.cl+model.c],equilibrium=True,density_critical=False),grids=[],axis_roots=[],interior_attempts=[],MP=[]);result['states'].append(state);save()
 previous=None;selected=[]
 thin=np.logspace(-9,-2,15)
 for level,(nr,nt,order)in enumerate([(129,65,128),(257,129,128),(513,257,128),(513,257,192)]):
  tick=time.monotonic();lr=np.linspace(-8,8,nr)*math.log(10);th=np.unique(np.r_[np.linspace(0,np.pi/2,nt),thin,np.pi/2-thin]);f=grids(model,lr,th,order)
  row=dict(level=level,radial=nr,angular=len(th),inverse_order=order,extents=[],candidate_cell_counts={})
  for extent in [10,100,1e4,1e8]:
   mask=lr<=math.log(extent)+1e-12;info=dict(extent=extent,minimum_radius=float(np.exp(lr[0])),points=int(mask.sum()*len(th)),minima={k:witness(f[k],lr,th,mask)for k in ['Wnorm_scaled','gradnorm_scaled','W1_over_x','W2_over_y','gy_scaled']})
   info['sampled_nonpositive_counts']={k:int(np.sum((f[k]<=0)&mask[:,None]))for k in ['W1_over_x','W2_over_y','gy_scaled']}
   row['extents'].append(info)
  for kind,keys in [('equilibrium',('wx','wy')),('density_critical',('gx_scaled','gy_scaled'))]:
   cells=cells_straddling(f[keys[0]],f[keys[1]]);row['candidate_cell_counts'][kind]=len(cells)
   if level==3:
    for ii,jj in cells:
     lo=np.array([lr[ii],th[jj]]);hi=np.array([lr[ii+1],th[jj+1]]);seed=(lo+hi)/2
     fit=least_squares(lambda z:point(model,z,kind),seed,bounds=(lo,hi),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=100)
     norm=float(np.linalg.norm(fit.fun));attempt=dict(kind=kind,cell=[int(ii),int(jj)],bounds=[lo.tolist(),hi.tolist()],seed=seed.tolist(),point=fit.x.tolist(),success=bool(fit.success),nfev=fit.nfev,scaled_vector=fit.fun.tolist(),scaled_norm=norm,accepted_apparent_root=norm<1e-8)
     state['interior_attempts'].append(attempt);save()
  if level==3:
   for axis,jj in [('horizontal',0),('vertical',len(th)-1)]:
    for kind,key,component in [('equilibrium','wx'if axis=='horizontal'else'wy',0 if axis=='horizontal'else 1),('density_critical','gy_scaled',1)]:
     val=f[key][:,jj];brackets=np.flatnonzero(val[:-1]*val[1:]<0)
     axisrow=dict(axis=axis,kind=kind,minimum=float(np.min(val)),maximum=float(np.max(val)),brackets=[[float(lr[i]),float(lr[i+1])]for i in brackets],roots=[],sampled_exact_zeros=[float(lr[i])for i in np.flatnonzero(val==0)])
     for ii in brackets:
      zz=brentq(lambda ll:point(model,[ll,float(th[jj])],kind)[component],lr[ii],lr[ii+1],xtol=1e-12)
      axisrow['roots'].append(dict(log_radius=zz,radius=math.exp(zz),scaled_vector=point(model,[zz,float(th[jj])],kind).tolist()))
     state['axis_roots'].append(axisrow)
   if previous:
    row['previous_inverse_order_change']={k:float(np.nanmax(np.abs(f[k]-previous[k])))for k in f}
   selected=list({(v['x'],v['y']):v for v in row['extents'][-1]['minima'].values()}.values())
  row['elapsed_seconds']=time.monotonic()-tick;state['grids'].append(row);save();print(utc(),tag,'grid',level,'seconds',row['elapsed_seconds'],'minima',[(k,v['value'])for k,v in row['extents'][-1]['minima'].items()],'cells',row['candidate_cell_counts'],flush=True)
  if level==2:previous=f
 for attempt in state['interior_attempts']:
  if attempt['accepted_apparent_root']:
   ll,tt=attempt['point'];rr=math.exp(ll);selected.append(dict(x=rr*math.cos(tt),y=rr*math.sin(tt),radius=rr,theta=tt))
 for a in state['axis_roots']:
  for rr in a['roots']:selected.append(dict(x=rr['radius']if a['axis']=='horizontal'else 0.,y=rr['radius']if a['axis']=='vertical'else 0.))
 mpmodels=[SmoothMP(exact,digits)for digits in [75,110]]
 for p in selected:
  rec=dict(selected_point=p,evaluations=[m.fields(p['x'],p['y'])for m in mpmodels]);state['MP'].append(rec);save();print(utc(),tag,'MP',p['x'],p['y'],flush=True)
 assert sha(source)==state['source_sha256'];state.update(status='DONE',finished_utc=utc());save()
result.update(status='DONE',finished_utc=utc());save();print(utc(),'DONE',flush=True)
