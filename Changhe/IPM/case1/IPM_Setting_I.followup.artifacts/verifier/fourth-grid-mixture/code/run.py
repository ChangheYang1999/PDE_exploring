from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
p=argparse.ArgumentParser();p.add_argument('case',choices=['84']);a=p.parse_args();tag={'84':'n84m35S'}[a.case];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if not __debug__:raise RuntimeError('This verifier refuses optimized Python; checks must remain enabled')
from contracts import all_arrays,authenticate,need
plan=OUT/'plan.json';registration=OUT/'registration.json';registered=json.loads(registration.read_text());need(sha(plan)==registered['plan_sha256'],'plan registration mismatch');ps=json.loads(plan.read_text());authenticate(ps)
need(ps['alphas']==[0,.25,.5,.75,1] and ps['dimensions']==[4,10,14], 'changed design')
M1,A1,M2,A2,gauss_actions,gauss_summary,sourcefiles,reconstruction=all_arrays(tag,ps)
need(M1.shape==(59,14) and M2.shape==(65,14) and A1.shape==(58,14) and A2.shape==(64,14), 'array shapes')
need(np.array_equal(M1[-1],M2[-1]), 'parameter row mismatch');d=M1[-1];sv=lambda x:np.linalg.svd(x,compute_uv=False)
files=[Path(__file__),ROOT/'PROOF.md',plan,registration,*sourcefiles];out={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'state_md5':gauss_summary['state_md5'],'pins':{str(f):sha(f) for f in files},'source_reconstruction':reconstruction,'rows':[],'scope':'Mixed finite sampling norms with fixed computed denominators and previously measured velocity approximations. No continuum error bound, kernel count, family or endpoint.'};arrays={'M1':M1,'M2':M2,'A1':A1,'A2':A2}
for k in ps['dimensions']:
 need(np.linalg.norm(d[:k])>0,'zero truncated parameter row')
 records=[]
 for alpha in ps['alphas']:
  M=np.vstack([np.sqrt(alpha)*M1[:-1,:k],np.sqrt(1-alpha)*M2[:-1,:k],d[:k]]);A=np.vstack([np.sqrt(alpha)*A1[:,:k],np.sqrt(1-alpha)*A2[:,:k]])
  assert np.allclose(M.T@M,alpha*(M1[:,:k].T@M1[:,:k])+(1-alpha)*(M2[:,:k].T@M2[:,:k]),rtol=2e-12,atol=1e-14)
  assert np.allclose(A.T@A,alpha*(A1[:,:k].T@A1[:,:k])+(1-alpha)*(A2[:,:k].T@A2[:,:k]),rtol=2e-12,atol=1e-14)
  Q,T=np.linalg.qr(M,mode='reduced');sM=sv(T);assert sM[-1]>1e-10*sM[0];Bmat=np.linalg.solve(T.T,A.T).T;values=sv(Bmat)[::-1]
  _,sm0,vhm=np.linalg.svd(M,full_matrices=False);coords=vhm.T/sm0;checkvals=sv(A@coords)[::-1];assert np.allclose(values,checkvals,rtol=2e-9,atol=1e-12)
  _,sa,vha=np.linalg.svd(A,full_matrices=False);assert sa[-1]>1e-12*sa[0];dual=(vha@d[:k])/sa;cost=1/np.linalg.norm(dual);coeff=vha.T@(dual/sa)*cost**2;assert abs(d[:k]@coeff-1)<1e-9;assert abs(np.linalg.norm(A@coeff)/cost-1)<1e-9
  rec={'dimension':k,'alpha_first_sample':alpha,'physical_singular_values_ascending':values.tolist(),'unit_cl_cost':float(cost),'unit_cl_minimizer':coeff.tolist(),'metric_condition':float(sM[0]/sM[-1]),'two_factorizations_max_difference':float(max(abs(values-checkvals)))};records.append(rec);arrays[f'k{k}_alpha{alpha}_B']=Bmat
 left,right=records[0],records[-1]
 for rec in records:
  alpha=rec['alpha_first_sample'];minimum=min(left['physical_singular_values_ascending'][0],right['physical_singular_values_ascending'][0]);costlower=np.sqrt(alpha*right['unit_cl_cost']**2+(1-alpha)*left['unit_cl_cost']**2);assert rec['physical_singular_values_ascending'][0]>=minimum*(1-1e-9);assert rec['unit_cl_cost']>=costlower*(1-1e-9);rec['proved_finite_cost_lower_bound']=float(costlower)
 out['rows']+=records
authenticate(ps)
for rel,h in out['pins'].items():need(sha(Path(rel))==h,'changed final input '+rel)
out['complete']=True;out['verdict']='PASS';(OUT/(tag+'_summary.json')).write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(OUT/(tag+'_matrices.npz'),**arrays)
for row in out['rows']:print(tag,row['dimension'],row['alpha_first_sample'],row['physical_singular_values_ascending'][0],row['unit_cl_cost'])
print('COMPLETE',out['utc'])
