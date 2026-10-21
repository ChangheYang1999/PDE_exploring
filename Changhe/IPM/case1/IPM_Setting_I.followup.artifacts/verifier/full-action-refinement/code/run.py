from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time,sys
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1]
for name in ('inverse','ritz-resolution','sampled-physical-actions'):
 sys.path.insert(0,str(ROOT.parent/name/'code'))
from collocation import NodalDensity
from gpu import GPUField
from split_kernel import SplitKernel
from linearized import direction_coefficients,MultiLinearGPU
from blocked_kernel import BlockedMultiSplit
p=argparse.ArgumentParser();p.add_argument('case',choices=['72','L16']);a=p.parse_args()
cases={'72':('third-grid-actions','n72m30S'),'L16':('scale-actions','n96m40SL16')}
folder,tag=cases[a.case];origin=ROOT.parent/folder
files={'source':origin/'data'/('dnB_'+tag+'.npz'),'directions':origin/'data'/('directions_'+tag+'.npz'),'points':origin/'verification/points.json','proof':ROOT/'PROOF.md','run':Path(__file__)}
pins={k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in files.items()}
d=NodalDensity(files['source']);V=np.load(files['directions'])['V'];assert V.shape==(d.N*d.M+2,14) and np.linalg.norm(V.T@V-np.eye(14))<1e-12
pts=json.loads(files['points'].read_text())['points'];assert len(pts)==58
configs=[{'nang':2048,'order':24,'panel':.1},{'nang':4096,'order':24,'panel':.1}]
path=ROOT/'verification'/(tag+'_actions.json')
if path.exists():
 out=json.loads(path.read_text());assert out['pins']==pins and out['configs']==configs and out['points']==pts and out['source_md5']==d.md5
else:out={'date_start':datetime.now(timezone.utc).isoformat(),'tag':tag,'source_md5':d.md5,'pins':pins,'files':{k:str(v.relative_to(ROOT.parent.parent)) for k,v in files.items()},'points':pts,'configs':configs,'rmax':'1e30','passes':[],'scope':'Full58row inverse sensitivity at fixed gradients and normalizers; no certified canonical quadrature error or continuum inference.'}
def save():
 q=path.with_suffix('.temporary');q.write_text(json.dumps(out,indent=2)+'\n');q.replace(path)
if out.get('complete'):print('ALREADY_COMPLETE',tag,flush=True);sys.exit(0)
torch.set_num_threads(1);co=direction_coefficients(d,V);save()
for cfg in configs:
 old=[x for x in out['passes'] if x['config']==cfg]
 if old:st=old[0]
 else:st={'config':cfg,'rows':[]};out['passes'].append(st);save()
 if len(st['rows'])==58:continue
 gpu=MultiLinearGPU(d,co,V[-2]);start=time.monotonic();print('BUILD',tag,cfg,datetime.now(timezone.utc).isoformat(),flush=True)
 ker=BlockedMultiSplit(gpu,cfg['nang'],cfg['order'],cfg['panel'],rmax=1e30);base=SplitKernel(GPUField(d),cfg['nang'],cfg['order'],cfg['panel'],rmax=1e30)
 for i,pt in enumerate(pts):
  if i<len(st['rows']):assert st['rows'][i]['point']==pt and st['rows'][i]['index']==i;continue
  u=base.velocity(pt);du=ker.velocity(pt);assert u.shape==(2,) and du.shape==(14,2)
  st['rows'].append({'index':i,'point':pt,'base_U':u.tolist(),'delta_U':du.tolist(),'date':datetime.now(timezone.utc).isoformat()});save();print('POINT',tag,cfg['nang'],i+1,'/58','seconds',round(time.monotonic()-start,2),flush=True)
 st['date_end']=datetime.now(timezone.utc).isoformat();save();del ker,base,gpu;torch.cuda.empty_cache()
out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',tag,out['date_end'],flush=True)
