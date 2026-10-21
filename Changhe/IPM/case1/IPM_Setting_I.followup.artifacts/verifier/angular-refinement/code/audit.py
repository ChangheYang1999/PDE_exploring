"""Independently inspect saved action arrays. No residual/solver code imported.
DCT reconstruction and NumPy linear algebra are ours; D entries remain supplied data.
"""
from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
import numpy as np
from scipy.fft import dct
import torch
torch.set_num_threads(1)
root=Path(__file__).resolve().parents[1]
num=Path('numerics/runs')
def load(name):
 p=num/name;d=torch.load(p,map_location='cpu',weights_only=True)
 return {k:v.numpy() if hasattr(v,'numpy') else v for k,v in d.items()}
def md5(name):return hashlib.md5((num/name).read_bytes()).hexdigest()
soft=load('n120m48_S_softvecs_node_cl400.pt')['Vsoft_unscaled']
base=load('ritz_n120m48_S.pt');Q,D=base['Q'],base['D']
V=soft/np.linalg.norm(soft,axis=0)
Q0,T0=np.linalg.qr(V,mode='reduced');co=Q.T@Q0;D0=D@co
coarse_sv=np.linalg.svd(D0,compute_uv=False)[::-1]
source=np.load(num/'dnSB_n120m48.npz')
z=np.r_[source['b'][1:].ravel(),float(source['c_l']),float(source['C'])]
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'algebra and interpolation checked independently; supplied finite-difference action entries not certified as exact derivatives',
 'source_hashes':{s:md5(s) for s in ['n120m48_S_softvecs_node_cl400.pt','ritz_n120m48_S.pt','dnSB_n120m48.npz']},
 'coarse':{'raw_direction_norms':np.linalg.norm(soft,axis=0).tolist(),'subspace_reconstruction_error':float(np.linalg.norm(Q@co-Q0)),
  'orthogonality_error':float(np.linalg.norm(Q0.T@Q0-np.eye(10))), 'ritz_on_same_10dimensional_subspace':coarse_sv.tolist(),
  'actions_along_original_unit_vectors':np.linalg.norm(D@(Q.T@V),axis=0).tolist(),
  'ritz_24_subspace':np.linalg.svd(D,compute_uv=False)[::-1][:10].tolist()},'targets':[]}
def interp(vec,Mtarget,is_state=False):
 arr=vec[:-2].reshape(120,48,-1)
 cs=dct(arr,type=2,axis=1)/48;cs[:,0,:]*=.5
 st=(np.arange(Mtarget)+.5)*np.pi/Mtarget
 ev=np.cos(st[:,None]*np.arange(48)[None,:])
 vals=np.einsum('tm,nmk->ntk',ev,cs).reshape(120*Mtarget,-1)
 return np.vstack((vals,vec[-2:].reshape(2,-1)))
for M in [64,96]:
 tag=f'crossgrid_n120m{M}_from_dnSB';f=load(tag+'.pt');meta=json.loads((num/(tag+'.json')).read_text())
 Qt,Dt,Vt,zt=(f[k] for k in ['Q1','D1','V1','z1'])
 Vi=interp(V,M);zi=interp(z[:,None],M)[:,0]
 # QR may choose signs; compare the supplied V1, and Q1 spans, not QR signs.
 vn=np.linalg.norm(Vt,axis=0);Vunit=Vt/vn;rt=Qt.T@Vunit
 actions=np.linalg.norm(Dt@rt,axis=0)
 sig=np.linalg.svd(Dt,compute_uv=False)[::-1]
 row={'M':M,'hashes':{tag+s:md5(tag+s) for s in ['.pt','.json']},
 'Q_orthogonality_error':float(np.linalg.norm(Qt.T@Qt-np.eye(10))),
 'V_span_reconstruction_error':float(np.linalg.norm(Qt@rt-Vunit)),
 'V_interpolation_max_error':float(np.max(np.abs(Vi-Vt))),
 'state_interpolation_max_error':float(np.max(np.abs(zi-zt))),
 'state_parameters':zt[-2:].tolist(),'ritz':sig.tolist(),
 'ritz_json_max_error':float(np.max(np.abs(sig-np.array(meta['target']['ritz'])))),
 'action_on_Q_columns':np.linalg.norm(Dt,axis=0).tolist(),
 'action_Q_json_max_error':float(np.max(np.abs(np.linalg.norm(Dt,axis=0)-[r['action'] for r in meta['target']['rows']]))),
 'actions_on_V_unit':actions.tolist(),
 'action_V_json_max_error':float(np.max(np.abs(actions-meta['target']['actions_along_interpolated_unit_vectors']))),
 'ratios_to_coarse_same_10dimensional_subspace':(sig/coarse_sv).tolist(),
 'ratio_to_reported_24dimensional_coarse_ritz':(sig/np.array(out['coarse']['ritz_24_subspace'])).tolist(),
 'metadata_F_norm':meta['target']['F'],'metadata_fd_step':meta['s'],'metadata_inverse_Npsi':meta['Npsi']}
 out['targets'].append(row)
out['M96_to_M64_ritz_ratios']=(np.array(out['targets'][1]['ritz'])/np.array(out['targets'][0]['ritz'])).tolist()
(root/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
