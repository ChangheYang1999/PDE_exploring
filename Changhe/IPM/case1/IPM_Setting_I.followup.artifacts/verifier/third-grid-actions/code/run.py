from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import ceil,sqrt
import os,sys,json,hashlib,time
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
sys.path.insert(0,str(ROOT.parent/'ritz-resolution/code'))
sys.path.insert(0,str(ROOT.parent/'sampled-physical-actions/code'))
sys.path.insert(0,str(ROOT.parent/'scale-actions/code'))
from collocation import NodalDensity
from density import gradient_fd
from gpu import GPUField
from split_kernel import SplitKernel
from linearized import direction_coefficients,LinearDensity,MultiLinearGPU
from tails import tail_constants
from blocked_kernel import BlockedMultiSplit as MultiSplit

torch.set_num_threads(1)
VROOT=ROOT/'verification';DATA=ROOT/'data';source=DATA
config={'nang':4096,'order':32,'panel':.075,'rmax':'1e30','relative_steps':[.00003125,.0000625]}
pts=[]
for r in [.2,1.,3.,8.,8.6,10.,30.,100.]:
 for t in [.002,.03,.2,.7,1.2,1.55]:pts.append([float(r*np.cos(t)),float(r*np.sin(t))])
for x in [8.59,8.61]:
 for y in [.01,.1]:pts.append([x,y])
for r in [1e3,1e4]:
 for t in [.01,.3,1.5]:pts.append([float(r*np.cos(t)),float(r*np.sin(t))])
pointpath=VROOT/'points.json';pointbytes=(json.dumps({'points':pts,'selection':'Prescribed before physical evaluation;58points'},indent=2)+'\n').encode()
if pointpath.exists():assert pointpath.read_bytes()==pointbytes
else:pointpath.write_bytes(pointbytes)
path=VROOT/'actions.json'
if path.exists():
 out=json.loads(path.read_text());assert out['config']==config and out['points']==pts
else:out={'date_start':datetime.now(timezone.utc).isoformat(),'config':config,'points':pts,'point_sha256':hashlib.sha256(pointbytes).hexdigest(),'states':[],'scope':'Sampled physical numerator derivatives, no continuum spectrum or endpoint'}

def save():
 temporary=path.with_name(path.name+'.temporary')
 temporary.write_text(json.dumps(out,indent=2)+'\n')
 temporary.replace(path)
for tag,name in [('n72m30S','dnB_n72m30S.npz')]:
 raw=(source/name).read_bytes();target=DATA/name
 if target.exists():assert target.read_bytes()==raw
 else:target.write_bytes(raw)
 d=NodalDensity(target)
 z={k:v.numpy() if hasattr(v,'numpy') else v for k,v in torch.load(source/('ritz_'+tag+'.pt'),map_location='cpu',weights_only=True).items()}
 uu,ss,vh=np.linalg.svd(z['D'],full_matrices=False);V=(z['Q']@vh.T)[:,::-1][:,:10]
 stored=z['Wv'][:,::-1][:,:10];V*=np.sign(np.sum(V*stored,axis=0))
 assert np.max(abs(V-stored))<2e-10
 qq,tt=np.meshgrid(d.qnodes[1:],d.thetanodes,indexing='ij')
 labels=[f'ritz{j}' for j in range(10)]
 for a,b,m in [(2,1,2),(1,2,1),(3,1,3),(1,1,0)]:
  cal=np.r_[(qq**a*(1-qq)**b*np.cos(2*m*tt)).ravel(),0.,0.]
  # Orthogonalize twice in the specified node metric.
  for _ in range(2):cal-=V@(V.T@cal)
  assert np.linalg.norm(cal)>1e-8
  cal/=np.linalg.norm(cal);V=np.column_stack([V,cal]);labels.append(f'own_cal_q{a}_1q{b}_cos{2*m}_orthogonalized')
 assert np.linalg.norm(V.T@V-np.eye(V.shape[1]))<1e-12
 dirpath=DATA/('directions_'+tag+'.npz')
 if dirpath.exists():assert np.array_equal(np.load(dirpath)['V'],V)
 else:np.savez_compressed(dirpath,V=V,labels=np.array(labels))
 co=direction_coefficients(d,V);cpu=[LinearDensity(d,co[:,:,j],V[-2,j]) for j in range(V.shape[1])]
 baseC,deltaC=tail_constants(d,V)
 existing=[r for r in out['states'] if r['tag']==tag]
 if existing:
  row=existing[0];assert row['state_md5']==d.md5 and row['direction_sha256']==hashlib.sha256(dirpath.read_bytes()).hexdigest()
 else:
  row={'tag':tag,'state_md5':d.md5,'N':d.N,'M':d.M,'cl':d.cl,'direction_sha256':hashlib.sha256(dirpath.read_bytes()).hexdigest(),'labels':labels,'dcl':V[-2].tolist(),'dC':V[-1].tolist(),'node_orthogonality_error':float(np.linalg.norm(V.T@V-np.eye(V.shape[1]))),'tail_base_C':str(baseC),'tail_delta_C':[str(c) for c in deltaC],'rows':[]};out['states'].append(row);save()
 if len(row['rows'])==len(pts):continue
 gpu=MultiLinearGPU(d,co,V[-2]);row['cpu_gpu_density_max_error']=max(float(abs(gpu(*pt).cpu().numpy()-np.array([f(*pt) for f in cpu])).max()) for pt in pts[::7]);save()
 begin=time.monotonic();print('BUILD',tag,datetime.now(timezone.utc).isoformat(),flush=True)
 ker=MultiSplit(gpu,4096,32,.075,rmax=1e30);bk=SplitKernel(GPUField(d),4096,32,.075,rmax=1e30)
 print('READY',tag,'buildseconds',time.monotonic()-begin,flush=True)
 for i,pt in enumerate(pts):
  if i<len(row['rows']):assert row['rows'][i]['point']==pt;continue
  u=bk.velocity(pt);du=ker.velocity(pt);rho=float(d(*pt));g=gradient_fd(d,*pt,relative_step=.00003125);g2=gradient_fd(d,*pt,relative_step=.0000625)
  dr=np.array([float(f(*pt)) for f in cpu]);dg=np.array([gradient_fd(f,*pt,relative_step=.00003125) for f in cpu]);dg2=np.array([gradient_fd(f,*pt,relative_step=.0000625) for f in cpu]);W=d.cl*np.array(pt)+u;N=abs(rho)+sum(abs(W*g));assert N>0
  act=V[-2]*(np.array(pt)@g)+dg@W+du@g-dr;act2=V[-2]*(np.array(pt)@g2)+dg2@W+du@g2-dr
  obs=max(1,ceil(sqrt(sum(t*t for t in pt))))
  while sum(F(t)**2 for t in pt)>obs**2:obs+=1
  tail=lambda C:C*F(5,2)*obs/F(10**24)/(1-F(obs,10**30)**2)**2
  tailB=tail(baseC);tailD=[tail(c) for c in deltaC]
  err=np.array([float(t)*sum(abs(g)) for t in tailD])+float(tailB)*np.sum(abs(dg),axis=1)
  result={'index':i,'point':pt,'rho':rho,'gradient':g.tolist(),'base_U':u.tolist(),'base_R':float(W@g-rho),'N_report_f':float(N),'delta_rho':dr.tolist(),'delta_gradient':dg.tolist(),'delta_U':du.tolist(),'delta_R':act.tolist(),'action_over_fixed_Nf':(act/N).tolist(),'spatial_step_change_fixed_units':(abs(act-act2)/N).tolist(),'exact_tail_observer':obs,'base_U_tail_bound_exact':str(tailB),'delta_U_tail_bounds_exact':[str(t) for t in tailD],'tail_action_bound_using_numerical_gradients':(err/N).tolist(),'cumulative_seconds':time.monotonic()-begin,'date':datetime.now(timezone.utc).isoformat()}
  row['rows'].append(result);save();print('POINT',tag,i+1,'/',len(pts),'radius',round(np.linalg.norm(pt),4),'maxritz',float(max(abs(act[:10]/N))),'base',float(abs(W@g-rho)/N),'seconds',round(time.monotonic()-begin,2),flush=True)
 del ker,bk,gpu;torch.cuda.empty_cache();row['date_end']=datetime.now(timezone.utc).isoformat();save()
out['date_end']=datetime.now(timezone.utc).isoformat();out['complete']=True;save();print('COMPLETE',out['date_end'],flush=True)
