"""Read numerical matrices as data; independently check norms and singular values.
Imports no code from the numerical lane. CPU single-threaded, assigned CUDA only.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from numpy.polynomial.chebyshev import chebvander,chebder,chebval
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse'/'code'))
from collocation import NodalDensity

torch.set_num_threads(1)
root=Path(sys.argv[1]);outpath=Path(sys.argv[2])
Jpath=root/'J_n120m48_S_refreshed.pt'
target=json.loads((root/'svd_n120m48_S.json').read_text())
data=torch.load(Jpath,map_location='cpu',weights_only=True)
rdata=torch.load(root/'ritz_n120m48_S.pt',map_location='cpu',weights_only=True)
field=NodalDensity(root/'dnSB_n120m48.npz')
z=data['z0'].numpy();J=data['J'];n=J.shape[1];N,M=field.N,field.M
q=field.qnodes;th=field.thetanodes
# Integrate the cardinal polynomials from their exact Chebyshev moments.
V=chebvander(2*q-1,N).T
mom=np.array([1/(1-j*j) if j%2==0 else 0. for j in range(N+1)])
wq=np.linalg.solve(V,mom)
s=field.map_inverse(th);wa=np.pi/(2*M)*(1+field.beta*np.cos(2*s))
weight=np.sqrt(wq[1:,None]*wa[None,:])
cq=2*chebder(field.co,axis=0)
bq=chebval(2*q-1,cq).T@np.cos(2*np.arange(M)[:,None]*s[None,:])
rfrac=1-(1-q)**(2/(1-field.k))
S=(1-field.k)*(1-q)*rfrac
Xg=3+(field.k-3)*rfrac[1:,None]+S[1:,None]*bq[1:]/field.b[1:]
ccl=float(np.linalg.norm(weight*Xg))
Dcol=np.r_[(field.b[1:]/weight).ravel(),1/ccl,field.C]
Dr=weight/field.b[1:];Dr[:3]*=(1-q[1:4,None])/.02
Drow=np.r_[Dr.ravel(),1.,1.]
scale=np.ones(n);scale[-2]=1/400
Q=rdata['Q'].numpy();D=rdata['D'].numpy();Wv=rdata['Wv'].numpy()
u,sv,vh=np.linalg.svd(D,full_matrices=False)
F0=data['F0'].numpy()
out={'jpath':str(Jpath.resolve()),'md5':hashlib.md5(Jpath.read_bytes()).hexdigest(),
     'matrix_shape':list(J.shape),'state_md5':field.md5,'quadrature_min_weight':float(wq.min()),'quadrature_sum':float(wq.sum()),
     'state_vs_z0_max':float(np.max(np.abs(z-np.r_[field.b[1:].ravel(),field.cl,field.C]))),
     'metadata_C':float(data['C']),'state_C':field.C,'z0_C':float(z[-1]),'stored_F0_norm':float(np.linalg.norm(F0)),
     'reported_F_norm':target['F2'],'Q_orthogonality_operator_error':float(np.linalg.norm(Q.T@Q-np.eye(Q.shape[1]),2)),
     'ritz_measured_singular_values_ascending':sv[::-1].tolist(),
     'Wv_orthogonality_error':float(np.linalg.norm(Wv.T@Wv-np.eye(Wv.shape[1]),2)),
     'stored_F0_projection_norm':float(np.linalg.norm(u.T@F0)),
     'ccl':ccl,'norms':{}}
for name,cols,rows in [('node_cl400',scale,np.ones(n)),('S3norm',Dcol,Drow)]:
 vd=torch.load(root/f'n120m48_S_softvecs_{name}.pt',map_location='cpu',weights_only=True)
 vv=vd['Vsoft_unscaled'].double();jv=(J@vv).numpy();v=vv.numpy();rep=[]
 for i in range(v.shape[1]):
  domain=float(np.linalg.norm(v[:,i]/cols));physical=float(np.linalg.norm(v[:,i]));action=float(np.linalg.norm(jv[:,i]))
  image=float(np.linalg.norm(rows*jv[:,i]));ratio=image/domain
  record=target['svd'][name]['soft'][i]
  rep.append({'i':i,'physical_vector_norm':physical,'specified_domain_norm':domain,'physical_Jv':action,
    'specified_image_norm':image,'consistent_matrix_action_ratio':ratio,'reported_matrix_sigma':record['sigma'],
    'reported_physical_FD_actions':[record['dF_ds_0.0001'],record['dF_ds_0.001']],
    'reported_difference_to_Jv':[record['dF_minus_Jv_0.0001'],record['dF_minus_Jv_0.001']],
    'same_direction_scaled_FD_ratio_if_no_row_scaling':[record['dF_ds_0.0001']/domain,record['dF_ds_0.001']/domain] if name=='node_cl400' else None})
 out['norms'][name]={'vectors':rep}
 outpath.write_text(json.dumps(out,indent=2)+'\n')
 start=time.monotonic();jg=J.to('cuda:0')
 vals=torch.linalg.svdvals(torch.as_tensor(rows,device='cuda:0')[:,None]*jg*torch.as_tensor(cols,device='cuda:0')[None,:]).cpu().numpy()
 out['norms'][name].update(svd_seconds=time.monotonic()-start,smax=float(vals[0]),smallest20=vals[-20:][::-1].tolist(),
   max_relative_difference_to_report_first20=float(np.max(np.abs(vals[-20:][::-1]/target['svd'][name]['smallest20']-1))))
 outpath.write_text(json.dumps(out,indent=2)+'\n')
 print(name,json.dumps(out['norms'][name]),flush=True)
