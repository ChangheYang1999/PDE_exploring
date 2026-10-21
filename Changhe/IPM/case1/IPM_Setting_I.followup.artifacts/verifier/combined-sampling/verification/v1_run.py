from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification';B=ROOT.parent
p=argparse.ArgumentParser();p.add_argument('case',choices=['72','96','120']);a=p.parse_args();tag={'72':'n72m30S','96':'n96m40S','120':'n120m48_S'}[a.case];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
gpath=B/'gauss-sampled-actions/verification'/(tag+'_summary.json');g=json.loads(gpath.read_text());assert g['complete'];gp=gpath.with_name(tag+'_matrices.npz');gz=np.load(gp);gar=gpath.with_name(tag+'_actions.json');ga=json.loads(gar.read_text());assert ga['complete'] and sha(gar)==g['actions_sha256']
for rel,digest in ga['pins'].items():assert sha(B.parent/rel)==digest
if a.case=='72':
 sp=B/'third-grid-actions/verification/summary.json';s=json.loads(sp.read_text());assert s['complete'];sm=sp.with_name('summary_matrices.npz');sz=np.load(sm);old=next(x for x in s['states'] if x['tag']==tag);oldtag='source_md5';fdir=B/'third-grid-actions/data'/('directions_'+tag+'.npz');M1=sz[tag+'_M'];A1=sz[tag+'_A'];rawpath=sp.with_name('actions.json');raw=json.loads(rawpath.read_text());assert raw['complete'] and sha(rawpath)==s['new_actions_sha256'];oldstate=next(x for x in raw['states'] if x['tag']==tag);assert sha(fdir)==oldstate['direction_sha256']
else:
 sp=B/'sampled-physical-actions/verification/summary_all_radial.json';s=json.loads(sp.read_text());assert s['complete'];sm=sp.with_name('summary_all_radial_matrices.npz');sz=np.load(sm);old=next(x for x in s['states'] if x['tag']==tag);oldtag='state_md5';fdir=B/'sampled-physical-actions/data'/('directions_'+tag+'.npz');M1=sz[tag+'_M'];A1=sz[tag+'_a4096_r32_A'];assert sha(fdir)==old['direction_sha256']
gdir=B/'gauss-sampled-actions/data'/('directions_'+tag+'.npz');assert fdir.read_bytes()==gdir.read_bytes();assert old[oldtag]==g['state_md5']==ga['state_md5']
M2=gz['M'];A2=gz['FD'];assert M1.shape==(59,14) and M2.shape==(65,14) and A1.shape==(58,14) and A2.shape==(64,14);assert np.array_equal(M1[-1],M2[-1]);assert np.array_equal(M2[-1],np.array(ga['dcl']));d=M1[-1];sv=lambda x:np.linalg.svd(x,compute_uv=False)
plan=OUT/'plan.json';ps=json.loads(plan.read_text());assert ps['alphas']==[0,.25,.5,.75,1] and ps['dimensions']==[4,10,14]
files=[Path(__file__),ROOT/'PROOF.md',plan,sp,sm,gpath,gp,gar,fdir,gdir];out={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'state_md5':g['state_md5'],'direction_sha256':sha(fdir),'pins':{str(f):sha(f) for f in files},'rows':[],'scope':'Mixed finite sampling norms with fixed computed denominators and previously measured velocity approximations. No continuum error bound, kernel count, family or endpoint.'};arrays={'M1':M1,'M2':M2,'A1':A1,'A2':A2}
for k in ps['dimensions']:
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
out['complete']=True;out['verdict']='PASS';(OUT/(tag+'_summary.json')).write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(OUT/(tag+'_matrices.npz'),**arrays)
for row in out['rows']:print(tag,row['dimension'],row['alpha_first_sample'],row['physical_singular_values_ascending'][0],row['unit_cl_cost'])
print('COMPLETE',out['utc'])
