from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,numpy as np,torch
torch.set_num_threads(1)
root=Path(__file__).resolve().parents[1];num=Path('numerics/runs')
def load(name):
 d=torch.load(num/name,map_location='cpu',weights_only=True)
 return {k:v.numpy() if hasattr(v,'numpy') else v for k,v in d.items()}
base=load('ritz_n120m48_S.pt');alt=load('ritz_n120m48_R8.pt');out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Independent algebra on supplied finite-difference action matrices, not an independent residual differentiation.','hashes':{}}
for label,data,fn in [('base',base,'ritz_n120m48_S'),('R8',alt,'ritz_n120m48_R8')]:
 Q,D=data['Q'],data['D'];sv=np.linalg.svd(D,compute_uv=False)[::-1];m=json.loads((num/(fn+'.json')).read_text())
 out[label]={'shape_Q':list(Q.shape),'shape_D':list(D.shape),'orthogonality':float(np.linalg.norm(Q.T@Q-np.eye(24))),'ritz':sv.tolist(),'max_ritz_json_error':float(np.max(abs(sv-m['ritz']))),'Q_column_actions':np.linalg.norm(D,axis=0).tolist(),'F_metadata':m['F'],'F_in_spanD_metadata':m['F_in_spanD']}
 for ext in ['.pt','.json']:out['hashes'][fn+ext]=hashlib.md5((num/(fn+ext)).read_bytes()).hexdigest()
b=np.array(out['base']['ritz']);a=np.array(out['R8']['ritz']);out['ritz_ratios_R8_over_base']=(a/b).tolist();out['ritz_absolute_differences']=(a-b).tolist()
out['principal_cosines_24']=np.linalg.svd(base['Q'].T@alt['Q'],compute_uv=False).tolist()
# Compare right Ritz parameter directions via an independent SVD.
_,_,v0=np.linalg.svd(base['D'],full_matrices=False);_,_,v1=np.linalg.svd(alt['D'],full_matrices=False)
for n in [2,4,10]:out['principal_cosines_smallest_'+str(n)]=np.linalg.svd((base['Q']@v0[-n:].T).T@(alt['Q']@v1[-n:].T),compute_uv=False).tolist()
z=[]
for fn in ['dnSB_n120m48.npz','dnR8_n120m48.npz']:
 d=np.load(num/fn);zz=np.r_[d['b'][1:].ravel(),float(d['c_l']),float(d['C'])];z.append(zz);out['hashes'][fn]=hashlib.md5((num/fn).read_bytes()).hexdigest()
dz=z[1]-z[0];out['state_difference']={'node_cl_C_norm':float(np.linalg.norm(dz)),'shape_norm':float(np.linalg.norm(dz[:-2])),'max_nodal_shape_difference':float(np.max(abs(dz[:-2]))),'dcl':float(dz[-2]),'dC':float(dz[-1])}
(root/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
