"""Independent absolute residual samples on explicit axis strips and core discs.

Uses the verifier's already manufactured-tested complementary Green inverse.
No producer evaluation code. No positive floor for either denominator.
"""
import argparse,hashlib,json,math
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from complementary_inverse_charts import ComplementaryQ,FullChart
from angular_log_inverse import AngularLogInverse
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);args=ap.parse_args()
model=ComplementaryQ(args.snapshot);dest=Path('evidence/q_small_neighborhoods')/args.tag;dest.mkdir(parents=True,exist_ok=True)
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.snapshot,source_sha256=hashlib.sha256(Path(args.snapshot).read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),metadata=model.meta,rows=[],origin=dict(x=0,y=0,R=0,Nf=0,Nv=0,R_Nf=None,R_Nv=None),axis_identity='At y=0, symmetry forces rho=rho_x=U2=0, hence R=Nf=Nv=0 exactly. Ratios there and at the origin are undefined. The y-axis is evaluated normally.',scope='Finite independent samples on physical axis strips and center discs; maxima are sampled, not uniform bounds. Canonical inverse includes the infinite exterior. No nearby-profile claim.')
peaks=set()
def save():
 record['updated_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(record,indent=2)+'\n')
for density,order in [(1,128),(2,256)]:
 logr=np.unique(np.concatenate([np.linspace(-12.031,2,320*density+1),np.log10([1e-4,1e-3,1e-2,100.])]))*math.log(10)
 theta=np.unique(np.concatenate([[0.,math.pi/2],(np.arange(240*density)+.3819660112501051)/(240*density)*(math.pi/2),np.geomspace(1e-14,.03,36*density),math.pi/2-np.geomspace(1e-14,.03,36*density)]))
 r=np.exp(logr)[:,None];sn=np.sin(theta)[None,:];cs=np.cos(theta)[None,:]
 xx=r*cs;yy=r*sn;xx[:,theta==math.pi/2]=0;yy[:,theta==0]=0
 z={key:np.zeros((len(logr),len(theta)))for key in ['R','Nf','Nv','R_Nf','R_Nv']}
 for defect in [True,False]:
  ids=np.flatnonzero((logr<=model.log_core)==defect)
  if not len(ids):continue
  owner=model if defect else FullChart(model);f=AngularLogInverse(owner,order).fields(logr[ids],theta)
  rho=f['H']+owner.a*sn;res=f['Fr']+owner.a*(owner.cl+owner.c-1)*sn
  gx=f['grad_radial']*cs-f['grad_angular']*sn;gy=f['grad_radial']*sn+f['grad_angular']*cs
  ux=f['ur']*cs-f['ut']*sn;uy=f['ur']*sn+f['ut']*cs
  nf=np.abs((model.cl*cs+ux)*gx)+np.abs((model.cl*sn+uy)*gy)+np.abs(rho)
  nv=np.abs(rho)+np.abs(cs*gx+sn*gy)+np.abs(ux*gx+uy*gy)
  z['R'][ids]=res*r[ids];z['Nf'][ids]=nf*r[ids];z['Nv'][ids]=nv*r[ids]
  with np.errstate(divide='ignore',invalid='ignore'):
   z['R_Nf'][ids]=np.where(nf>0,np.abs(res)/nf,np.nan);z['R_Nv'][ids]=np.where(nv>0,np.abs(res)/nv,np.nan)
 assert np.all(z['R'][:,theta==0]==0)
 assert np.all(z['Nf'][:,theta==0]==0)and np.all(z['Nv'][:,theta==0]==0)
 result=dict(radial_nodes=len(logr),angular_nodes=len(theta),inverse_order=order,physical_radius_range=[float(r.min()),float(r.max())],regions=[])
 outer=np.broadcast_to(r<=100*(1+8*np.finfo(float).eps),xx.shape)
 for eps in [1e-4,1e-3,1e-2]:
  for label,mask in [('x_axis_strip',outer&(yy<=eps)),('y_axis_strip',outer&(xx<=eps)),('center_disc',np.broadcast_to(r<=eps*(1+8*np.finfo(float).eps),xx.shape))]:
   name=label+'_'+str(eps);row=dict(name=name,epsilon=eps,geometry=('r<=100 and |y|<=epsilon'if label=='x_axis_strip'else'r<=100 and |x|<=epsilon'if label=='y_axis_strip'else'r<=epsilon'),sample_count=int(mask.sum()),zero_Nf_samples=int(np.count_nonzero(mask&(z['Nf']==0))),zero_Nv_samples=int(np.count_nonzero(mask&(z['Nv']==0))),min_positive_Nf=float(np.min(z['Nf'][mask&(z['Nf']>0)])),min_positive_Nv=float(np.min(z['Nv'][mask&(z['Nv']>0)])),maxima={})
   for field in ['abs_R','R_Nf','R_Nv']:
    vv=np.abs(z['R'])if field=='abs_R'else z[field];vv=np.where(mask,vv,np.nan)
    if not np.any(np.isfinite(vv)):continue
    i,j=np.unravel_index(np.nanargmax(vv),vv.shape)
    row['maxima'][field]=dict(value=float(vv[i,j]),x=float(xx[i,j]),y=float(yy[i,j]),r=float(r[i,0]),theta=float(theta[j]),R=float(z['R'][i,j]),Nf=float(z['Nf'][i,j]),Nv=float(z['Nv'][i,j]),R_Nf=float(z['R_Nf'][i,j]),R_Nv=float(z['R_Nv'][i,j]))
    if density==2:peaks.add((float(xx[i,j]),float(yy[i,j])))
   result['regions'].append(row)
 record['rows'].append(result);save();print(json.dumps({'utc':record['updated_utc'],'tag':args.tag,'order':order,'points':len(logr)*len(theta),'absolute_maxima':{v['name']:v['maxima']['abs_R']for v in result['regions']}}),flush=True)
pts=sorted(peaks,key=lambda p:(math.hypot(*p),math.atan2(p[1],p[0])));pts.extend([(0.,0.),(1.,0.)])
(dest/'mp_points.json').write_text(json.dumps(pts,indent=2)+'\n')
record['status']='COMPUTED';record['mp_followup_points']=len(pts);save()
lines=[f'# Absolute residual neighborhoods: {args.tag}','',record['updated_utc'],'',record['scope'],'',record['axis_identity'],'','| region | sampled max absolute R | x | y | Nf at that point | Nv at that point |','|---|---:|---:|---:|---:|---:|']
for row in record['rows'][-1]['regions']:
 p=row['maxima']['abs_R'];lines.append('| '+row['name']+' | '+' | '.join(f'{p[k]:.13g}'for k in ['value','x','y','Nf','Nv'])+' |')
lines+=['','The full JSON retains both sampling resolutions, normalization maxima and locations, sample counts, zero denominators and the smallest sampled positive denominators. Selected maxima are queued for independent multiprecision full-plane evaluation.']
(dest/'TABLE.md').write_text('\n'.join(lines)+'\n')
