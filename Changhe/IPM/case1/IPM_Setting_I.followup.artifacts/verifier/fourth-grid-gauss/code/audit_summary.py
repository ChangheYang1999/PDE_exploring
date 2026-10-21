"""Reconstruct every finite action by scalar loops and use SVD metric coordinates."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
import numpy as np
R=Path(__file__).resolve().parents[1];V=R/'verification'
p=argparse.ArgumentParser();p.add_argument('case',choices=['84']);a=p.parse_args();tag={'84':'n84m35S'}[a.case]
ap=V/(tag+'_actions.json');sp=V/(tag+'_summary.json');mp=V/(tag+'_matrices.npz');raw=json.loads(ap.read_text());s=json.loads(sp.read_text());z=np.load(mp);assert raw['complete'] and s['complete'];assert hashlib.sha256(ap.read_bytes()).hexdigest()==s['actions_sha256'];assert raw['cpu_gpu_density_checked_points']==64 and raw['cpu_gpu_density_max_scaled_error']<1e-10
for rel,h in raw['pins'].items():assert hashlib.sha256((R.parent.parent/rel).read_bytes()).hexdigest()==h
weights=np.sqrt(raw['weights']);points=np.array(raw['points']);assert np.all(weights>0) and abs(sum(weights**2)-1)<1e-14;d=np.array(raw['dcl']);cl=raw['c_l'];field=raw['field_rows'];assert len(field)==64;nf=z['Nf'];M=z['M'];assert np.array_equal(M[-1],d)
vel={str(x['config']['nang']):x['rows'] for x in raw['passes']};assert set(vel)=={'2048','4096'}
for rows in vel.values():assert len(rows)==64 and [r['point'] for r in rows]==raw['points']
for i,row in enumerate(field):
 for j in range(14):assert abs(M[i,j]-weights[i]*row['delta_rho'][j]/(1+abs(row['rho'])))<1e-14
 W=cl*points[i]+np.array(vel['4096'][i]['base_U']);den=abs(row['rho'])+sum(abs(W[l]*row['gradient'][l]) for l in range(2));assert abs(den-nf[i])<1e-9*(1+den)
checks=[]
for rule in ['2048','4096','FD','FD2']:
 velocity=vel[rule if rule in vel else '4096'];grad='gradient' if rule in vel else rule+'_gradient';dg='delta_gradient' if rule in vel else rule+'_delta_gradient';A=np.empty((64,14))
 for i,row in enumerate(field):
  x=points[i];u=velocity[i]['base_U'];bg=row[grad]
  for j in range(14):A[i,j]=weights[i]*(sum((cl*x[l]+u[l])*row[dg][j][l]+(d[j]*x[l]+velocity[i]['delta_U'][j][l])*bg[l] for l in range(2))-row['delta_rho'][j])/nf[i]
 assert np.max(abs(A-z[rule]))<1e-11
 for k in [4,10,14]:
  _,ms,mv=np.linalg.svd(M[:,:k],full_matrices=False);C=mv.T/ms;assert np.linalg.norm((M[:,:k]@C).T@(M[:,:k]@C)-np.eye(k))<1e-10
  sigma=np.linalg.svd(A[:,:k]@C,compute_uv=False)[::-1];target=s['spaces'][str(k)]['rules'][rule];assert np.allclose(sigma,target['physical_singular_values_ascending'],rtol=1e-8,atol=1e-11)
  _,sa,va=np.linalg.svd(A[:,:k],full_matrices=False);dual=(va@d[:k])/sa;cost=1/np.linalg.norm(dual);coeff=va.T@(dual/sa)*cost**2;assert abs(d[:k]@coeff-1)<1e-9;assert abs(np.linalg.norm(A[:,:k]@coeff)/cost-1)<1e-9;assert abs(cost/target['unit_cl_cost']-1)<1e-8
  checks.append({'rule':rule,'dimension':k,'SVD_sigma_min':float(sigma[0]),'SVD_cost':float(cost),'max_scalar_action_difference':float(np.max(abs(A-z[rule])))})
 for small,large in [(4,10),(10,14)]:
  x=s['spaces'][str(small)]['rules'][rule];y=s['spaces'][str(large)]['rules'][rule];assert y['physical_singular_values_ascending'][0]<=x['physical_singular_values_ascending'][0]*(1+1e-9);assert y['unit_cl_cost']<=x['unit_cl_cost']*(1+1e-9)
o={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'verdict':'PASS','checks':checks,'pins':{str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [ap,sp,mp,Path(__file__)]},'scope':'Scalar action reconstruction and independent finite-matrix coordinates/cost calculation. No additional inverse evaluation or interval certification.'};(V/(tag+'_audit.json')).write_text(json.dumps(o,indent=2)+'\n');print('PASS',tag,len(checks))
