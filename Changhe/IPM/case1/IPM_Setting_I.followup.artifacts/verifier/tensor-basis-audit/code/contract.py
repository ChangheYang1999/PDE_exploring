from pathlib import Path
from datetime import datetime,timezone
import numpy as np,math,json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
files=['grid-states/data/dnB_n96m40S.npz','ritz-resolution/data/dnSB_n120m48.npz','domain-states/data/dnB_n96m40SL4.npz','domain-states/data/dnB_n96m40SL16.npz','third-grid-actions/data/dnB_n72m30S.npz','refreshed-third-grid/data/dnC_n72m30S.npz','fixed-cl-correction/data/n96m40S_radius0.05.npz','fixed-cl-correction/data/n120m48_S_radius0.05.npz']
rows=[]
for rel in files:
 p=ROOT.parent/rel
 with np.load(p) as z:
  N=int(z['N']);M=int(z['M']);assert N>0 and M>0
  d={k:str(z[k].dtype) for k in ('b','L','c_l','beta')};assert all(x=='float64' for x in d.values());assert z['b'].shape==(N+1,M);assert z['q'].shape==(N+1,) and z['theta'].shape==(M,)
  q=np.array([(1-math.cos(math.pi*j/N))/2 for j in range(N+1)]);s=np.array([math.pi*(2*j+1)/(4*M) for j in range(M)]);theta=s+float(z['beta'])*np.sin(2*s)/2
  e1=float(np.max(abs(z['q']-q)));e2=float(np.max(abs(z['theta']-theta)));assert e1<4e-16 and e2<2e-15
  assert np.all(np.diff(z['q'])>0) and np.all(np.diff(z['theta'])>0) and z['q'][0]==0 and z['q'][-1]==1 and np.all(z['b'][0]==1)
  rows.append({'file':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'N':N,'M':M,'shape':list(z['b'].shape),'dtypes':d,'q_ascending':True,'s_ascending':True,'row0_is_one':True,'q_double_formula_maxdifference':e1,'theta_double_formula_maxdifference':e2})
checks=[];metapins={}
for tag in ['center_code_low','hessian_code_low']:
 mp=ROOT.parent/'model-review/verification'/f'{tag}_metadata.json';metapins[tag]=hashlib.sha256(mp.read_bytes()).hexdigest();m=json.loads(mp.read_text());assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn'
 for file,digest in m['files'].items():
  actual=hashlib.sha256((ROOT.parent.parent/file).read_bytes()).hexdigest();assert actual==digest
  checks.append({'review':tag,'file':file,'review_sha256':digest,'current_sha256':actual,'equal':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'data':rows,'review_metadata_sha256':metapins,'primary_review_input_identity':checks,'scope':'Data-specific dtype, shape and ascending-node convention audit. q/theta equality is a floating diagnostic, not a change to the exact ideal-node interpolant definition. No shared certificate code was modified during running jobs.'}
(OUT/'contract_reproduced.json').write_text(json.dumps(out,indent=2)+'\n');print('CONTRACT_PASS',len(rows),'files;',len(checks),'review input hashes')
