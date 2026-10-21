from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import ceil, sqrt
import sys,json,hashlib,time,argparse
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification';DATA=ROOT/'data'
for rel in ['inverse/code','ritz-resolution/code','sampled-physical-actions/code','scale-actions/code']:
 sys.path.insert(0,str(ROOT.parent/rel))
from collocation import NodalDensity
from density import gradient_fd
from gpu import GPUField
from split_kernel import SplitKernel
from linearized import direction_coefficients,LinearDensity,MultiLinearGPU
from tails import tail_constants
from blocked_kernel import BlockedMultiSplit
from analytic_gradients import gradients
p=argparse.ArgumentParser();p.add_argument('case',choices=['72','96','120']);a=p.parse_args()
tag,name,folder={'72':('n72m30S','dnB_n72m30S.npz','third-grid-actions'),'96':('n96m40S','dnB_n96m40S.npz','sampled-physical-actions'),'120':('n120m48_S','dnSB_n120m48.npz','sampled-physical-actions')}[a.case]
utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
torch.set_num_threads(1)
pointpath=OUT/'points.json';ps=json.loads(pointpath.read_text());pts=np.array(ps['points']);weights=np.array(ps['weights']);assert len(pts)==64 and np.all(weights>0) and abs(sum(weights)-1)<1e-14
for n in [name,'directions_'+tag+'.npz']:
 origin=ROOT.parent/folder/'data'/n;target=DATA/n
 if target.exists():assert target.read_bytes()==origin.read_bytes()
 else:target.write_bytes(origin.read_bytes())
d=NodalDensity(DATA/name);V=np.load(DATA/('directions_'+tag+'.npz'))['V'];assert V.shape==(d.N*d.M+2,14) and np.linalg.norm(V.T@V-np.eye(14))<1e-12
pins={str(x.relative_to(ROOT.parent.parent)):sha(x) for x in [ROOT/'PROOF.md',Path(__file__),pointpath,DATA/name,DATA/('directions_'+tag+'.npz')]}
# Keep all implementation dependencies visible and frozen at startup.
for rel in ['inverse/code/collocation.py','inverse/code/density.py','inverse/code/gpu.py','inverse/code/split_kernel.py','inverse/code/linearized.py','scale-actions/code/tails.py','sampled-physical-actions/code/blocked_kernel.py','scale-actions/code/analytic_gradients.py']:
 x=ROOT.parent/rel;pins[str(x.relative_to(ROOT.parent.parent))]=sha(x)
path=OUT/(tag+'_actions.json')
if path.exists():
 out=json.loads(path.read_text());assert out['pins']==pins and out['points']==ps['points'] and out['weights']==ps['weights']
else:out={'date_start':utc(),'tag':tag,'state_md5':d.md5,'pins':pins,'points':ps['points'],'weights':ps['weights'],'c_l':d.cl,'dcl':V[-2].tolist(),'passes':[],'complete':False,'scope':'Two finite inverse rules on64weighted physical points. No quadrature error certificate or continuum spectrum.'}
def save():
 tmp=path.with_suffix('.temporary');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(path)
co=direction_coefficients(d,V);cpu=[LinearDensity(d,co[:,:,j],V[-2,j]) for j in range(14)];baseC,deltaC=tail_constants(d,V)
if 'field_rows' not in out:
 ga,dga=gradients(d,V,pts);rows=[]
 for i,pt in enumerate(pts):
  rho=float(d(*pt));dr=np.array([float(f(*pt)) for f in cpu]);g1=gradient_fd(d,*pt,relative_step=.00003125);g2=gradient_fd(d,*pt,relative_step=.0000625)
  dg1=np.array([gradient_fd(f,*pt,relative_step=.00003125) for f in cpu]);dg2=np.array([gradient_fd(f,*pt,relative_step=.0000625) for f in cpu])
  obs=max(1,ceil(sqrt(sum(t*t for t in pt))))
  while sum(F(float(t))**2 for t in pt)>obs**2:obs+=1
  tail=lambda C:C*F(5,2)*obs/F(10**24)/(1-F(obs,10**30)**2)**2
  rows.append({'index':i,'point':pt.tolist(),'rho':rho,'delta_rho':dr.tolist(),'gradient':ga[i].tolist(),'delta_gradient':dga[i].tolist(),'FD_gradient':g1.tolist(),'FD_delta_gradient':dg1.tolist(),'FD2_gradient':g2.tolist(),'FD2_delta_gradient':dg2.tolist(),'exact_tail_observer':obs,'base_U_tail_bound_exact':str(tail(baseC)),'delta_U_tail_bounds_exact':[str(tail(c)) for c in deltaC]})
 out['field_rows']=rows;save()
assert len(out['field_rows'])==64
gpu=MultiLinearGPU(d,co,V[-2]);errors=[];relative_errors=[]
for pt in pts:
 ref=np.array([f(*pt) for f in cpu]);err=abs(gpu(*pt).cpu().numpy()-ref)
 errors.append(float(err.max()));relative_errors.append(float((err/(1+abs(ref))).max()))
out['cpu_gpu_density_max_error']=max(errors);out['cpu_gpu_density_max_scaled_error']=max(relative_errors);out['cpu_gpu_density_checked_points']=len(pts)
assert out['cpu_gpu_density_max_scaled_error']<1e-10
save()
for nang in [2048,4096]:
 cfg={'nang':nang,'order':24,'panel':.1,'rmax':'1e30'};existing=[r for r in out['passes'] if r['config']==cfg]
 if existing:row=existing[0]
 else:row={'config':cfg,'date_start':utc(),'rows':[]};out['passes'].append(row);save()
 if len(row['rows'])==64:continue
 start=time.monotonic();print('BUILD',tag,nang,utc(),flush=True)
 ker=BlockedMultiSplit(gpu,nang,24,.1,rmax=1e30);bk=SplitKernel(GPUField(d),nang,24,.1,rmax=1e30)
 print('READY',tag,nang,round(time.monotonic()-start,2),flush=True)
 for i,pt in enumerate(pts):
  if i<len(row['rows']):assert row['rows'][i]['point']==pt.tolist();continue
  u=bk.velocity(pt);du=ker.velocity(pt);assert np.isfinite(u).all() and np.isfinite(du).all()
  row['rows'].append({'index':i,'point':pt.tolist(),'base_U':u.tolist(),'delta_U':du.tolist(),'utc':utc()});save()
  print('POINT',tag,nang,i+1,'/64',round(time.monotonic()-start,2),flush=True)
 del ker,bk;torch.cuda.empty_cache();row['date_end']=utc();save()
for rel,digest in pins.items():assert sha(ROOT.parent.parent/rel)==digest
out['complete']=True;out['date_end']=utc();save();print('COMPLETE',tag,out['date_end'],flush=True)
