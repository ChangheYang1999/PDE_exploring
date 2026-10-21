from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
import numpy as np
D=Path(__file__).resolve().parents[1]/'verification'
r=json.loads((D/'actions.json').read_text());s=json.loads((D/'summary.json').read_text());z=np.load(D/'summary_matrices.npz');checks=[];scalar_checks=[]
assert r['complete'] and s['complete'] and len(r['points'])==58
assert hashlib.sha256((D/'actions.json').read_bytes()).hexdigest()==s['new_actions_sha256']
for st,sm in zip(r['states'],s['states']):
 tag=st['tag'];assert tag==sm['tag'];assert len(st['rows'])==58
 assert [x['point'] for x in st['rows']]==r['points']
 A=z[tag+'_A'];M=z[tag+'_M'];assert A.shape==(58,14) and M.shape==(59,14)
 # Rebuild every matrix entry with scalar arithmetic directly from saved raw fields.
 rebuilt_A=np.empty_like(A);rebuilt_M=np.empty_like(M);base_residual=[]
 for i,rr in enumerate(st['rows']):
  point=rr['point'];rho=float(rr['rho']);grad=rr['gradient']
  W=[st['cl']*point[t]+rr['base_U'][t] for t in range(2)]
  normal=abs(rho)+sum(abs(W[t]*grad[t]) for t in range(2))
  assert normal>0 and abs(normal/rr['N_report_f']-1)<1e-13
  base_residual.append((sum(W[t]*grad[t] for t in range(2))-rho)/normal)
  for j in range(14):
   value=st['dcl'][j]*sum(point[t]*grad[t] for t in range(2))
   value+=sum(W[t]*rr['delta_gradient'][j][t] for t in range(2))
   value+=sum(rr['delta_U'][j][t]*grad[t] for t in range(2))
   value-=rr['delta_rho'][j]
   rebuilt_A[i,j]=value/normal/np.sqrt(58)
   rebuilt_M[i,j]=rr['delta_rho'][j]/(1+abs(rho))/np.sqrt(58)
 rebuilt_M[-1]=st['dcl']
 assert np.allclose(rebuilt_A,A,rtol=2e-10,atol=5e-13)
 assert np.allclose(rebuilt_M,M,rtol=2e-13,atol=5e-14)
 assert abs(max(abs(v) for v in base_residual)-sm['base_max_R_Nf'])<1e-13
 assert int(np.argmax(abs(np.array(base_residual))))==sm['base_max_index']
 scalar_checks.append({'state':tag,'entries':58*14,'max_action_difference':float(np.max(abs(rebuilt_A-A))),'max_metric_difference':float(np.max(abs(rebuilt_M-M))),'base_maximum':max(abs(v) for v in base_residual)})
 for k in (4,10,14):
  B=z[f'{tag}_{k}_B'];_,metric_s,metric_vh=np.linalg.svd(M[:,:k],full_matrices=False);coords=metric_vh.T/metric_s
  assert np.linalg.norm((M[:,:k]@coords).T@(M[:,:k]@coords)-np.eye(k))<1e-10
  sv=np.linalg.svd(A[:,:k]@coords,compute_uv=False)[::-1]
  assert np.allclose(sv,sm['spaces'][str(k)]['physical_singular_values_ascending'],rtol=2e-12,atol=1e-14)
  # A separate SVD least-squares calculation checks the QR cost and its minimizer.
  u,vh_s,vh=np.linalg.svd(A[:,:k],full_matrices=False);d=M[-1,:k]
  dual=(vh@d)/vh_s;cost=1/np.linalg.norm(dual)
  c=vh.T@(dual/vh_s)*cost**2
  assert abs(d@c-1)<2e-11
  assert abs(np.linalg.norm(A[:,:k]@c)/cost-1)<1e-10
  assert abs(cost/sm['spaces'][str(k)]['unit_cl_cost']-1)<1e-10
  Q,T=np.linalg.qr(M[:,:k],mode='reduced');assert np.linalg.norm(B@T-A[:,:k])<1e-10
  checks.append({'state':tag,'dimension':k,'svd_cost':float(cost),'QR_cost':sm['spaces'][str(k)]['unit_cl_cost'],'metric_reconstruction_error':float(np.linalg.norm(B@T-A[:,:k]))})
obj={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'raw_scalar_checks':scalar_checks,'verdict':'PASS','scope':'Finite saved matrices and summary arithmetic only; no independent second inverse implementation is asserted by this audit.','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [D/'actions.json',D/'summary.json',D/'summary_matrices.npz',Path(__file__)]}}
(D/'summary_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(checks),'finite span arithmetic checks')
