from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
import numpy as np
D=Path(__file__).resolve().parents[1]/'verification'
r=json.loads((D/'actions.json').read_text());s=json.loads((D/'summary.json').read_text());z=np.load(D/'summary_matrices.npz');checks=[]
assert r['complete'] and s['complete'] and len(r['points'])==58
assert hashlib.sha256((D/'actions.json').read_bytes()).hexdigest()==s['new_actions_sha256']
for st,sm in zip(r['states'],s['states']):
 tag=st['tag'];assert tag==sm['tag'];assert len(st['rows'])==58
 assert [x['point'] for x in st['rows']]==r['points']
 A=z[tag+'_A'];M=z[tag+'_M'];assert A.shape==(58,14) and M.shape==(59,14)
 for k in (4,10,14):
  B=z[f'{tag}_{k}_B'];sv=np.linalg.svd(B,compute_uv=False)[::-1]
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
obj={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'verdict':'PASS','scope':'Finite saved matrices and summary arithmetic only; no independent second inverse implementation is asserted by this audit.','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [D/'actions.json',D/'summary.json',D/'summary_matrices.npz',Path(__file__)]}}
(D/'summary_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(checks),'finite span arithmetic checks')
