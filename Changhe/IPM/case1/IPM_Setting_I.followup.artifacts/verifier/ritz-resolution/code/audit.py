from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
import numpy as np
import torch
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebvander

torch.set_num_threads(1)
root=Path(__file__).resolve().parents[1];num=root.parent.parent/'numerics/runs'
sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity

inputs=[]
def copy(name):
 p=num/name;b=p.read_bytes();q=root/'data'/name;q.write_bytes(b)
 inputs.append({'source':str(p),'copy':str(q),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()});return q
def load(p):
 return {k:v.numpy() if hasattr(v,'numpy') else v for k,v in torch.load(p,map_location='cpu',weights_only=True).items()}
rows=[]
for tag,state,soft,cross in [('n96m40S','dnB_n96m40S.npz','n96m40S_final_softvecs_node_cl400.pt','crossgrid_n120m48_from_n96S.json'),('n120m48_S','dnSB_n120m48.npz','n120m48_S_softvecs_node_cl400.pt','crossgrid_n96m40_from_n120S.json')]:
 m=json.loads(copy('ritz_'+tag+'.json').read_text());z=load(copy('ritz_'+tag+'.pt'));d=NodalDensity(copy(state));ss=load(copy(soft));cm=json.loads(copy(cross).read_text())
 Q,D,W=z['Q'],z['D'],z['Wv'];U,s,Vh=np.linalg.svd(D,full_matrices=False);VV=(Q@Vh.T)[:,::-1];stored=W[:,::-1]
 signs=np.sign(np.sum(VV*stored,axis=0));VV*=signs
 sv=s[::-1];nodeq=d.qnodes[1:];r=np.full(d.N,np.inf);r[:-1]=d.L*np.sqrt(np.expm1(-2*np.log1p(-nodeq[:-1])/(1-d.k)));rr=np.repeat(r,d.M)
 structure=[]
 for j in range(10):
  v=VV[:,j];e=v[:-2]**2;tot=v@v
  row={'index':j,'ritz':float(sv[j]),'dcl':float(v[-2]),'dC':float(v[-1]),'far':float(e[rr>100].sum()/tot),'near':float(e[rr<1].sum()/tot),'mid':float(e[(rr>=1)&(rr<=100)].sum()/tot)}
  row['metadata_max_error']=max(abs(row[k]-m['ritz_vectors'][j][k]) for k in ['ritz','dcl','dC','far','near','mid']);structure.append(row)
 V0=ss['Vsoft_unscaled'][:,:10];Q0=np.linalg.qr(V0,mode='reduced')[0];T=Q.T@Q0;projerr=np.linalg.norm(Q@T-Q0);sv10=np.linalg.svd(D@T,compute_uv=False)[::-1]
 qq,tt=np.meshgrid(d.qnodes[1:],d.thetanodes,indexing='ij');cal=np.r_[(qq*qq*(1-qq)*np.cos(4*tt)).ravel(),0.,0.];cal/=np.linalg.norm(cal)
 dirs=np.column_stack([VV[:,:4],cal]);labels=np.array([f'ritz{i}' for i in range(4)]+['own_smooth_calibration']);np.savez_compressed(root/'data'/('directions_'+tag+'.npz'),V=dirs,labels=labels)
 item={'tag':tag,'source_state_in_pt':z['state'],'field_file':state,'shape_Q':list(Q.shape),'shape_D':list(D.shape),'orthogonality_error':float(np.linalg.norm(Q.T@Q-np.eye(Q.shape[1]))),'ritz':sv.tolist(),'ritz_metadata_error':float(abs(sv-m['ritz']).max()),'Q_actions':np.linalg.norm(D,axis=0).tolist(),'action_metadata_error':float(abs(np.linalg.norm(D,axis=0)-m['actions']).max()),'stored_ritz_vector_max_error_after_sign':float(abs(VV-stored).max()),'structure':structure,'ten_source_span_projection_error':float(projerr),'ten_source_restricted_measured_ritz':sv10.tolist(),'separate_ten_source_metadata':cm['source']['ritz'],'ten_value_absolute_differences':abs(sv10-cm['source']['ritz']).tolist(),'F_metadata_only':m['F'],'F_projection_metadata_only':m['F_in_spanD'],'F_array_stored':False,'finite_difference_step_metadata':m['s']}
 assert item['ritz_metadata_error']<1e-11 and item['action_metadata_error']<1e-10 and item['orthogonality_error']<1e-12
 rows.append(item);print(json.dumps(item),flush=True)
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Own algebra on supplied finite-difference matrices; no exact-Jacobian certificate and no independently recomputed orbit residual','inputs':inputs,'rows':rows,'ritz_ratios_96_over_120':(np.array(rows[0]['ritz'])/rows[1]['ritz']).tolist()}
(root/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n')
