"""Small finite QR variational costs, independent of orbit-map code."""
from pathlib import Path
import json,sys
from datetime import datetime,timezone
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
label='4096' if '--refined' in sys.argv else '2048'
name='summary_gradient_refined_'+label
raw=json.loads((OUT/'actions.json').read_text());summ=json.loads((OUT/(name+'.json')).read_text())
arr=np.load(OUT/(name+'_matrices.npz'))
obj={'date':datetime.now(timezone.utc).isoformat(),'source_summary':name+'.json','states':[],
 'units':'RMS delta R/Nf per unit delta c_l, all normalizers fixed',
 'scope':'Finite-span linearized costs. Upper bounds on infima over larger spaces; no continuum lower bound, orbit-map identification, nonlinear family or endpoint.'}
for st in raw['states']:
 tag=st['tag'];A=arr[f'{tag}_{label}_A'];l=np.array(st['dcl']);row={'tag':tag,'spaces':{}}
 previous=float('inf')
 for d in (4,10,14):
  Q,R=np.linalg.qr(A[:,:d],mode='reduced');sv=np.linalg.svd(R,compute_uv=False);assert sv[-1]>1e-12*sv[0]
  b=np.linalg.solve(R.T,l[:d]);alpha=1/np.linalg.norm(b);v=np.linalg.solve(R,b)*alpha**2
  value=np.linalg.norm(A[:,:d]@v);constraint=float(l[:d]@v)
  assert abs(constraint-1)<1e-9 and abs(value/alpha-1)<1e-9 and alpha<=previous*(1+1e-9);previous=alpha
  row['spaces'][str(d)]={'alpha_cl':float(alpha),'constraint':constraint,'measured_RMS_action':float(value),
   'singular_condition_of_node_coordinate_action_matrix':float(sv[0]/sv[-1]),'minimizer_in_prescribed_direction_coordinates':v.tolist(),
   'nodal_coordinate_norm_of_minimizer':float(np.linalg.norm(v))}
 print(tag,[(d,x['alpha_cl']) for d,x in row['spaces'].items()],flush=True);obj['states'].append(row)
(OUT/('cl_cost_'+label+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
