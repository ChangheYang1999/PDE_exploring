from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
sys.path.insert(0,str(ROOT.parent/'ritz-resolution/code'))
sys.path.insert(0,str(ROOT.parent/'sampled-physical-actions/code'))
from collocation import NodalDensity
from gpu import GPUField
from split_kernel import SplitKernel
from linearized import direction_coefficients,MultiLinearGPU
from blocked_kernel import BlockedMultiSplit

torch.set_num_threads(1)
DEST=ROOT/'refinement_selected';PATH=DEST/'actions.json';DATA=ROOT/'data'
allpts=json.loads((ROOT/'verification/points.json').read_text())['points']
indices=[0,11,16,22,28,34,35,40,46,50,54,57]
pts=[allpts[i] for i in indices]
configs=[{'nang':2048,'order':24,'panel':.1},{'nang':4096,'order':24,'panel':.1}]
if PATH.exists():
 out=json.loads(PATH.read_text());assert out['indices']==indices and out['points']==pts and out['configs']==configs
else:out={'date_start':datetime.now(timezone.utc).isoformat(),'indices':indices,'points':pts,'configs':configs,'rmax':'1e30','states':[],'scope':'selected-point numerical sensitivity, no certified error bound'}
def save():
 t=PATH.with_name(PATH.name+'.temporary');t.write_text(json.dumps(out,indent=2)+'\n');t.replace(PATH)
for tag in ['n96m40SL4','n96m40SL16']:
 d=NodalDensity(DATA/('dnB_'+tag+'.npz'))
 z={k:v.numpy() if hasattr(v,'numpy') else v for k,v in torch.load(DATA/('ritz_'+tag+'.pt'),map_location='cpu',weights_only=True).items()}
 uu,ss,vh=np.linalg.svd(z['D'],full_matrices=False);V=(z['Q']@vh.T)[:,::-1][:,:10]
 stored=z['Wv'][:,::-1][:,:10];V*=np.sign(np.sum(V*stored,axis=0));assert np.max(abs(V-stored))<2e-10
 qq,tt=np.meshgrid(d.qnodes[1:],d.thetanodes,indexing='ij')
 for a,b,m in [(2,1,2),(1,2,1),(3,1,3),(1,1,0)]:
  cal=np.r_[(qq**a*(1-qq)**b*np.cos(2*m*tt)).ravel(),0.,0.]
  for _ in range(2):cal-=V@(V.T@cal)
  cal/=np.linalg.norm(cal);V=np.column_stack([V,cal])
 assert np.linalg.norm(V.T@V-np.eye(14))<1e-12
 main=DATA/('directions_'+tag+'.npz')
 if main.exists():assert np.array_equal(np.load(main)['V'],V)
 dp=DEST/('directions_'+tag+'.npy')
 if dp.exists():assert np.array_equal(np.load(dp),V)
 else:np.save(dp,V)
 old=[s for s in out['states'] if s['tag']==tag]
 if old:st=old[0];assert st['source_md5']==d.md5
 else:st={'tag':tag,'source_md5':d.md5,'direction_sha256':hashlib.sha256(dp.read_bytes()).hexdigest(),'passes':[]};out['states'].append(st);save()
 co=direction_coefficients(d,V)
 for cfg in configs:
  old=[s for s in st['passes'] if s['config']==cfg]
  if old:entry=old[0]
  else:entry={'config':cfg,'rows':[]};st['passes'].append(entry);save()
  if len(entry['rows'])==len(pts):continue
  gpu=MultiLinearGPU(d,co,V[-2]);begin=time.monotonic();print('BUILD',tag,cfg,datetime.now(timezone.utc).isoformat(),flush=True)
  ker=BlockedMultiSplit(gpu,cfg['nang'],cfg['order'],cfg['panel'],rmax=1e30)
  bk=SplitKernel(GPUField(d),cfg['nang'],cfg['order'],cfg['panel'],rmax=1e30)
  for j,pt in enumerate(pts):
   if j<len(entry['rows']):assert entry['rows'][j]['point']==pt;continue
   u=bk.velocity(pt);du=ker.velocity(pt)
   entry['rows'].append({'index':indices[j],'point':pt,'base_U':u.tolist(),'delta_U':du.tolist(),'date':datetime.now(timezone.utc).isoformat()});save()
   print('POINT',tag,cfg['nang'],j+1,len(pts),'seconds',round(time.monotonic()-begin,2),flush=True)
  entry['date_end']=datetime.now(timezone.utc).isoformat();save();del ker,bk,gpu;torch.cuda.empty_cache()
out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['date_end'],flush=True)
