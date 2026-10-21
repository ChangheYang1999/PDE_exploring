from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
p=argparse.ArgumentParser();p.add_argument('case',choices=['84']);a=p.parse_args();tag={'84':'n84m35S'}[a.case]
path=OUT/(tag+'_actions.json');raw=path.read_bytes();o=json.loads(raw);assert o['complete'];n=64;pts=np.array(o['points']);w=np.sqrt(o['weights']);fr=o['field_rows'];assert len(fr)==n
for rel,digest in o['pins'].items():assert hashlib.sha256((ROOT.parent.parent/rel).read_bytes()).hexdigest()==digest,rel
ps=json.loads((OUT/'points.json').read_text());assert ps['points']==o['points'] and ps['weights']==o['weights']
assert o['cpu_gpu_density_checked_points']==64 and o['cpu_gpu_density_max_scaled_error']<1e-10
assert [r['point'] for r in fr]==o['points'];rho=np.array([r['rho'] for r in fr]);dr=np.array([r['delta_rho'] for r in fr]);g=np.array([r['gradient'] for r in fr]);dg=np.array([r['delta_gradient'] for r in fr]);d=np.array(o['dcl']);cl=o['c_l']
velocity={}
for pa in o['passes']:
 cfg=pa['config'];assert cfg['order']==24 and cfg['panel']==.1 and cfg['rmax']=='1e30';rr=pa['rows'];assert len(rr)==n and [r['point'] for r in rr]==o['points']
 velocity[str(cfg['nang'])]=(np.array([r['base_U'] for r in rr]),np.array([r['delta_U'] for r in rr]))
assert set(velocity)=={'2048','4096'};W=cl*pts+velocity['4096'][0];nf=abs(rho)+np.sum(abs(W*g),axis=1);assert np.all(nf>0)
M=np.vstack([w[:,None]*dr/(1+abs(rho[:,None])),d]);arrays={'M':M,'points':pts,'weights':w*w,'Nf':nf};sv=lambda x:np.linalg.svd(x,compute_uv=False)
def action(rule,bg,ddg):
 U,V=velocity[rule];WW=cl*pts+U
 return w[:,None]*(d[None,:]*np.sum(pts*bg,axis=1)[:,None]+np.einsum('ijk,ik->ij',ddg,WW)+np.einsum('ijk,ik->ij',V,bg)-dr)/nf[:,None]
A={key:action(key,g,dg) for key in velocity}
A['FD']=action('4096',np.array([r['FD_gradient'] for r in fr]),np.array([r['FD_delta_gradient'] for r in fr]))
A['FD2']=action('4096',np.array([r['FD2_gradient'] for r in fr]),np.array([r['FD2_delta_gradient'] for r in fr]))
arrays.update(A)
u0,v0=velocity['2048'];u1,v1=velocity['4096'];direct=w[:,None]*(np.einsum('ijk,ik->ij',dg,u1-u0)+np.einsum('ijk,ik->ij',v1-v0,g))/nf[:,None]
assert np.max(abs(direct-(A['4096']-A['2048'])))<5e-12
bt=np.array([float(Fraction(r['base_U_tail_bound_exact'])) for r in fr]);dt=np.array([[float(Fraction(t)) for t in r['delta_U_tail_bounds_exact']] for r in fr]);tail=w[:,None]*(bt[:,None]*np.sum(abs(dg),axis=2)+dt*np.sum(abs(g),axis=1)[:,None])/nf[:,None]
res=(np.sum(W*g,axis=1)-rho)/nf;imax=int(np.argmax(abs(res)))
out={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'state_md5':o['state_md5'],'actions_sha256':hashlib.sha256(raw).hexdigest(),'summary_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'point_sha256':hashlib.sha256((OUT/'points.json').read_bytes()).hexdigest(),'complete':True,'sample_count':n,'base_max_R_Nf':float(max(abs(res))),'base_max_point':pts[imax].tolist(),'base_weighted_R_Nf':float(np.linalg.norm(w*res)),'cpu_gpu_density_max_error':o['cpu_gpu_density_max_error'],'spaces':{},'scope':'Numerical finite-matrix results with positive64point weights. No continuum spectrum, quadrature-error certificate or endpoint. Tail propagated through computed gradients.'}
for k in [4,10,14]:
 assert np.linalg.norm(d[:k])>0, "Unit-c constraint requires a nonzero parameter row"
 Q,T=np.linalg.qr(M[:,:k],mode='reduced');s=sv(T);assert s[-1]>1e-10*s[0];entry={'metric_condition':float(s[0]/s[-1]),'rules':{},'comparisons':{}};arrays[str(k)+'_Q']=Q
 for rule,C in A.items():
  B=np.linalg.solve(T.T,C[:,:k].T).T;arrays[f'{k}_{rule}_B']=B
  QA,RA=np.linalg.qr(C[:,:k],mode='reduced');sa=sv(RA);assert sa[-1]>1e-12*sa[0]
  z=np.linalg.solve(RA.T,d[:k]);cost=1/np.linalg.norm(z);coeff=np.linalg.solve(RA,z)*cost**2
  assert abs(d[:k]@coeff-1)<1e-9 and abs(np.linalg.norm(C[:,:k]@coeff)/cost-1)<1e-9
  entry['rules'][rule]={'physical_singular_values_ascending':sv(B)[::-1].tolist(),'unit_cl_cost':float(cost),'cl_minimizer':coeff.tolist()}
 for label,delta in [('angular',direct),('analytic_vs_FD',A['4096']-A['FD']),('FD_step',A['FD']-A['FD2'])]:
  E=np.linalg.solve(T.T,delta[:,:k].T).T;entry['comparisons'][label]={'Frobenius':float(np.linalg.norm(E)),'spectral':float(np.linalg.norm(E,2))}
 entry['tail_Frobenius_bound_using_computed_gradients']=float(np.linalg.norm(tail[:,:k]@abs(np.linalg.solve(T,np.eye(k)))))
 out['spaces'][str(k)]=entry
(OUT/(tag+'_summary.json')).write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(OUT/(tag+'_matrices.npz'),**arrays)
print('COMPLETE',tag,out['utc'],'Rmax',out['base_max_R_Nf'])
for k,e in out['spaces'].items():print(k,e['rules']['4096']['physical_singular_values_ascending'][0],e['rules']['4096']['unit_cl_cost'],e['comparisons'])
