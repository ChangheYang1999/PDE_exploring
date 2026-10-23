"""Dense independent tensor grids, local residual refinement, and peak records.

Applied to the verifier SmoothBasis formula. The density/Green inverse is the verifier's complementary-chart implementation.
Saved point lists permit separate high-precision and Cartesian-FD verification.
No optimizer or producer evaluation code is imported.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math,hashlib
import numpy as np
from complementary_inverse_charts import SmoothAngular,FullChart,point_fields
from angular_log_inverse import AngularLogInverse

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);args=ap.parse_args()
model=SmoothAngular(args.snapshot);dest=Path('evidence/smooth_residual_grid')/args.tag;dest.mkdir(parents=True,exist_ok=True)
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.snapshot,sha256=hashlib.sha256(Path(args.snapshot).read_bytes()).hexdigest(),metadata=dict(radial=model.N,angular=model.M,length=model.L,alpha=model.alpha),a=model.a,c=model.c,ell=model.cl,delta=model.cl+model.c-1,rows=[])
points=set()

def stamp():
 result['updated_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')

def evaluate(logr,theta,order,label):
 logr=np.asarray(logr);theta=np.asarray(theta);nr,nt=len(logr),len(theta)
 z={k:np.empty((nr,nt))for k in ['abs_R','R_Nf','R_Nv','Nf','Nv']}
 sn=np.sin(theta)[None,:];cs=np.cos(theta)[None,:]
 for defect in [True,False]:
  ids=np.flatnonzero((logr<=model.log_core)==defect)
  if not len(ids):continue
  owner=model if defect else FullChart(model)
  f=AngularLogInverse(owner,order).fields(logr[ids],theta)
  rho=f['H']+owner.a*sn;rr=f['Fr']+owner.a*(owner.cl+owner.c-1)*sn
  gx=f['grad_radial']*cs-f['grad_angular']*sn;gy=f['grad_radial']*sn+f['grad_angular']*cs
  ux=f['ur']*cs-f['ut']*sn;uy=f['ur']*sn+f['ut']*cs
  nf=np.abs((model.cl*cs+ux)*gx)+np.abs((model.cl*sn+uy)*gy)+np.abs(rho)
  nv=np.abs(rho)+np.abs(cs*gx+sn*gy)+np.abs(ux*gx+uy*gy)
  radii=np.exp(logr[ids])[:,None]
  z['abs_R'][ids]=np.abs(rr)*radii;z['Nf'][ids]=nf*radii;z['Nv'][ids]=nv*radii
  with np.errstate(divide='ignore',invalid='ignore'):
   z['R_Nf'][ids]=np.where(nf>0,np.abs(rr)/nf,np.nan);z['R_Nv'][ids]=np.where(nv>0,np.abs(rr)/nv,np.nan)
 z['R_Nf'][:,theta==0]=np.nan;z['R_Nv'][:,theta==0]=np.nan
 summary={}
 regions=[('all',-float('inf'),float('inf')),('origin',-float('inf'),math.log(.01)),('core',math.log(.01),0.),('middle',0.,math.log(100.)),('far',math.log(100.),float('inf'))]
 regions += [('extent_'+str(p),-float('inf'),(p+1e-12)*math.log(10))for p in [2,4,8,12,50,250]]
 for name,lo,hi in regions:
  mask=(logr>=lo)&(logr<hi)
  if not np.any(mask):continue
  row={};idx=np.flatnonzero(mask)
  for key in ['abs_R','R_Nf','R_Nv']:
   vals=z[key][mask]
   if not np.any(np.isfinite(vals)):continue
   i,j=np.unravel_index(np.nanargmax(vals),vals.shape);i=idx[i];r=math.exp(float(logr[i]));th=float(theta[j]);x=r*math.cos(th);y=r*math.sin(th)
   if th==math.pi/2:x=0.
   row[key]=dict(maximum=float(z[key][i,j]),log10_radius=float(logr[i]/math.log(10)),theta=th,x=x,y=y,Nf=float(z['Nf'][i,j]),Nv=float(z['Nv'][i,j]))
   points.add((x,y))
  summary[name]=row
 row=dict(grid=label,inverse_order=order,radii=nr,angles=nt,log10_radius=[float(logr[0]/math.log(10)),float(logr[-1]/math.log(10))],theta=[float(theta[0]),float(theta[-1])],summary=summary)
 result['rows'].append(row);stamp();print(json.dumps(dict(utc=result['updated_utc'],grid=label,order=order,points=nr*nt,summary=summary['all'])),flush=True)
 return row

lg=np.unique(np.concatenate((np.linspace(-12.017,12.033,641),np.array([-160.,-100.,-50.,-30.,-20.,20.,30.,50.,100.,160.,250.]))))*math.log(10)
theta=np.unique(np.concatenate(([0.,math.pi/2],(np.arange(321)+.3819660112501051)/321*(math.pi/2),np.geomspace(1e-10,.01,25),math.pi/2-np.geomspace(1e-10,.01,25))))
(dest/'base_grid.json').write_text(json.dumps({'log_radius':lg.tolist(),'theta':theta.tolist(),'description':'Common physical grid, independent offsets, exact axes plus near-axis geometric samples.'},indent=2)+'\n')
base=evaluate(lg,theta,128,'wide')
evaluate(lg,theta,256,'wide')
centers=[]
for quantity in ['R_Nf','R_Nv']:
 ctr=base['summary']['all'][quantity];pair=(ctr['log10_radius'],ctr['theta'])
 if pair in centers:continue
 centers.append(pair);l,t=pair
 lr=np.linspace(l-.075,l+.075,129)*math.log(10);tt=np.linspace(max(0,t-.02),min(math.pi/2,t+.02),161)
 for order in [128,192,256]:evaluate(lr,tt,order,'local_'+quantity)

pts=sorted(points,key=lambda p:(math.hypot(*p),math.atan2(p[1],p[0])))
(dest/'peaks.json').write_text(json.dumps(pts,indent=2)+'\n')
fd=[list(p)for p in pts if 1e-14<=math.hypot(*p)<=1e10]
fd.extend([[0.,0.],[.1,0.],[0.,.1],[1.,0.],[0.,1.]])
(dest/'fd_points.json').write_text(json.dumps(fd,indent=2)+'\n')
peakdest=Path('evidence/complementary_charts')/(args.tag+'_dense_peaks');peakdest.mkdir(parents=True,exist_ok=True)
logs=np.array([math.log(math.hypot(*p))for p in pts]);angles=np.array([math.atan2(p[1],p[0])for p in pts])
peak=dict(source=args.snapshot,sha256=result['sha256'],a=model.a,c=model.c,ell=model.cl,delta=result['delta'],rows=[])
for order in [128,192,256]:
 pp=point_fields(model,logs,angles,order)
 for row,(x,y) in zip(pp,pts):row['x']=x;row['y']=y
 peak['rows'].append(dict(order=order,points=pp))
peak['scope']='Selected dense/local grid maxima evaluated independently as point lists; for high-precision density follow-up. Finite samples, no uniform certificate.'
(peakdest/'diagnostic.json').write_text(json.dumps(peak,indent=2)+'\n')
result['status']='COMPUTED';result['finished_utc']=datetime.now(timezone.utc).isoformat();result['peak_points']=len(pts);result['fd_points']=len(fd)
result['scope']='Finite independent grids and local refinements, canonical whole-plane inverse. Exact x-axis ratios omitted; positive denominators evaluated without a floor. Absolute far residuals in double precision need MP interpretation. No uniform maximum, minimization guarantee, or nearby-solution theorem.'
stamp()
