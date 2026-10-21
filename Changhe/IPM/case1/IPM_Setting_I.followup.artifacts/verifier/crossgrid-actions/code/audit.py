from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,sys
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebvander
import torch
torch.set_num_threads(1)
root=Path(__file__).resolve().parents[1];num=root.parent.parent/'numerics/runs'
# Explicit sibling source path; this program writes only under root.
num=Path('numerics/runs').resolve()
meta=[]
def snapshot(name):
 p=num/name;dest=root/'data'/name;b=p.read_bytes();dest.write_bytes(b)
 meta.append({'source':str(p),'copy':str(dest),'sha256':hashlib.sha256(b).hexdigest()})
 return dest
def tensors(path):
 z=torch.load(path,map_location='cpu',weights_only=True)
 return {k:v.numpy() if hasattr(v,'numpy') else v for k,v in z.items()}
def coeff(nodes):
 out=dct(nodes[::-1],type=1,axis=0)/(nodes.shape[0]-1);out[[0,-1]]*=.5
 out=dct(out,type=2,axis=1)/nodes.shape[1];out[:,0]*=.5
 return out
def interp(V,N0,M0,N1,M1):
 a=np.zeros((N0+1,M0,V.shape[1]));a[1:]=V[:-2].reshape(N0,M0,-1)
 co=coeff(a);q=(1-np.cos(np.pi*np.arange(N1+1)/N1))/2
 rad=chebvander(2*q-1,N0);ang=np.cos(np.pi*(np.arange(M1)+.5)[:,None]*np.arange(M0)[None,:]/M1)
 ans=np.einsum('an,nmk,bm->abk',rad,co,ang,optimize=True)
 return np.vstack([ans[1:].reshape(N1*M1,-1),V[-2:]])
rows=[]
for tag in ['n120m48_from_n96S','n96m40_from_n120S']:
 name='crossgrid_'+tag;m=json.loads(snapshot(name+'.json').read_text());z=tensors(snapshot(name+'.pt'))
 a=np.load(snapshot(Path(m['state']).name));b=np.load(snapshot(Path(m['target_state']).name));s=tensors(snapshot(Path(m['softvecs']).name));V=s['Vsoft_unscaled'][:,:m['k']]
 N0,M0,N1,M1=map(int,[a['N'],a['M'],b['N'],b['M']]);assert float(a['L'])==float(b['L'])==8 and float(a['beta'])==float(b['beta'])
 Vi=interp(V,N0,M0,N1,M1);Q,D,V1,z1=(z[k] for k in ['Q1','D1','V1','z1']);T=Q.T@V1;vn=np.linalg.norm(V1,axis=0)
 acts=np.linalg.norm(D@T/vn,axis=0);sv=np.linalg.svd(D,compute_uv=False)[::-1]
 target=np.r_[b['b'][1:].ravel(),float(b['c_l']),float(b['C'])]
 gram=(V1/vn).T@(V1/vn);np.fill_diagonal(gram,0)
 row={'tag':tag,'N_source':N0,'M_source':M0,'N_target':N1,'M_target':M1,'independent_interpolation_max_error':float(abs(Vi-V1).max()),'target_state_max_error':float(abs(z1-target).max()),'Q_orthogonality_error':float(np.linalg.norm(Q.T@Q-np.eye(m['k']))),'V_span_reconstruction_error':float(np.linalg.norm(Q@T-V1)),'ritz_target':sv.tolist(),'ritz_json_error':float(abs(sv-m['target']['ritz']).max()),'Q_actions':np.linalg.norm(D,axis=0).tolist(),'Q_action_json_error':float(abs(np.linalg.norm(D,axis=0)-[x['action'] for x in m['target']['rows']]).max()),'V_unit_actions':acts.tolist(),'V_unit_action_json_error':float(abs(acts-m['target']['actions_along_interpolated_unit_vectors']).max()),'max_offdiag_cos':float(abs(gram).max()),'source_ritz_only_metadata':m['source']['ritz'],'source_D0_stored':False,'target_source_ritz_ratio_using_metadata':(sv/np.array(m['source']['ritz'])).tolist(),'source_q0_step_difference_metadata':m['source']['q0_diff_s_10s'],'target_q0_step_difference_metadata':m['target']['q0_diff_s_10s'],'finite_difference_step':m['s']}
 assert row['independent_interpolation_max_error']<1e-8 and row['target_state_max_error']==0 and row['ritz_json_error']<1e-12 and row['V_unit_action_json_error']<1e-12
 rows.append(row);print(json.dumps(row),flush=True)
examples=[]
for n in [10,100,1000,10000]:
 A=np.array([[1.,float(n)],[0.,1.]]);v=np.array([1.,-1/n]);v/=np.linalg.norm(v)
 U,s,Vh=np.linalg.svd(A);u=Vh[-1];u*=np.sign(u[0]);sv=2/(np.sqrt(n*n+4)+n)
 assert abs(s[-1]-sv)<1e-13
 examples.append({'n':n,'sigma_min':float(s[-1]),'explicit_v_action':float(np.linalg.norm(A@v)),'right_min_direction_distance_to_e1':float(np.linalg.norm(u-[1,0]))})
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Own interpolation and algebra; supplied target FD columns; source D0 not stored','inputs':meta,'rows':rows,'exact_counterexample_samples':examples}
(root/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n')
