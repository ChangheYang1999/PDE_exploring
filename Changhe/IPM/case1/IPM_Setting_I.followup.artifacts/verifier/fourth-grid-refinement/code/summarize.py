from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('case',choices=['84']);a=p.parse_args()
folder,tag={'84':('fourth-grid-actions','n84m35S')}[a.case]
origin=ROOT.parent/folder;mainpath=origin/'verification/actions.json';refpath=ROOT/'verification'/(tag+'_actions.json')
main=json.loads(mainpath.read_text());ref=json.loads(refpath.read_text());assert main.get('complete') and ref.get('complete')
assert main['points']==ref['points'] and len(ref['points'])==58
st=next(s for s in main['states'] if s['tag']==tag);assert st['state_md5']==ref['source_md5'];rows=st['rows'];assert len(rows)==58
V=np.load(origin/'data'/('directions_'+tag+'.npz'))['V'];assert hashlib.sha256((origin/'data'/('directions_'+tag+'.npz')).read_bytes()).hexdigest()==st['direction_sha256']==ref['pins']['directions']
pts=np.array(main['points']);g=np.array([r['gradient'] for r in rows]);dg=np.array([r['delta_gradient'] for r in rows]);nf=np.array([r['N_report_f'] for r in rows]);rho=np.array([r['rho'] for r in rows]);dr=np.array([r['delta_rho'] for r in rows]);dc=V[-2]
M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(58),dc]);A=np.array([r['delta_R'] for r in rows])/nf[:,None]/np.sqrt(58)
vel={'main':(np.array([r['base_U'] for r in rows]),np.array([r['delta_U'] for r in rows]))}
for ps in ref['passes']:
 assert len(ps['rows'])==58 and [r['point'] for r in ps['rows']]==main['points'] and [r['index'] for r in ps['rows']]==list(range(58))
 cfg=ps['config'];assert cfg['order']==24 and cfg['panel']==.1
 vel[str(cfg['nang'])]=(np.array([r['base_U'] for r in ps['rows']]),np.array([r['delta_U'] for r in ps['rows']]))
assert set(vel)=={'main','2048','4096'}
def diff(a,b):
 u,du=vel[b];v,dv=vel[a]
 return (np.einsum('ijk,ik->ij',dg,u-v)+np.einsum('ijk,ik->ij',du-dv,g))/nf[:,None]/np.sqrt(58)
Ds={'angular':diff('2048','4096'),'radial':diff('4096','main')}
As={'main':A,'4096':A-Ds['radial'],'2048':A-Ds['radial']-Ds['angular']}
out={'date':datetime.now(timezone.utc).isoformat(),'tag':tag,'source_md5':st['state_md5'],'main_sha256':hashlib.sha256(mainpath.read_bytes()).hexdigest(),'refinement_sha256':hashlib.sha256(refpath.read_bytes()).hexdigest(),'summary_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':58,'spaces':{},'scope':'Differences between full58row finite rules. Gradients/normalizers/domain metric fixed. All spectral and cost values numerical; no certified quadrature error and no continuum inference.'};arrays={'M':M,**As,**Ds}
sv=lambda x:np.linalg.svd(x,compute_uv=False)
for k in(4,10,14):
 Q,T=np.linalg.qr(M[:,:k],mode='reduced');assert sv(T)[-1]>1e-10*sv(T)[0];entry={'inverse_differences':{},'rules':{}}
 for label,E in Ds.items():
  B=np.linalg.solve(T.T,E[:,:k].T).T;entry['inverse_differences'][label]={'Frobenius':float(np.linalg.norm(B)),'spectral':float(np.linalg.norm(B,2)),'max_entry':float(np.max(abs(B)))};arrays[f'{k}_{label}_B']=B
 for label,C in As.items():
  B=np.linalg.solve(T.T,C[:,:k].T).T;QA,RA=np.linalg.qr(C[:,:k],mode='reduced');assert sv(RA)[-1]>1e-12*sv(RA)[0];z=np.linalg.solve(RA.T,dc[:k]);cost=1/np.linalg.norm(z)
  entry['rules'][label]={'singular_values_ascending':sv(B)[::-1].tolist(),'unit_cl_cost':float(cost)};arrays[f'{k}_{label}_B']=B
 out['spaces'][str(k)]=entry
path=ROOT/'verification'/(tag+'_summary.json');path.write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(path.with_suffix('.npz'),**arrays)
print(json.dumps({'tag':tag,'rows':58,'spaces':out['spaces']},indent=2));print('COMPLETE',tag,out['date'])
