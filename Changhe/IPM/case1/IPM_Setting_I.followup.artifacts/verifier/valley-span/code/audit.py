"""Independent algebra on frozen scalar observations, no source evaluator imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
NUM=ROOT.parents[1]/'numerics'
out={'date':datetime.now(timezone.utc).isoformat(),'source':{},'difference_arithmetic':[],'combinations':[],'scope':'Conditional arithmetic and sign-span audit of supplied scalar measurements; their physical observables not independently evaluated here.'}
obs={}
for tag in ['n120m48_S','n96m40S']:
 name='valley_s4e_'+tag+'.json';raw=(NUM/'runs'/name).read_bytes();(ROOT/'data'/name).write_bytes(raw);o=json.loads(raw);obs[tag]=o;out['source'][tag]=hashlib.sha256(raw).hexdigest()
 for m in o['modes']:
  s=o['s'];der={k:(m['plus'][k]-m['minus'][k])/(2*s) for k in m['deriv']};second={k:(m['plus'][k]-2*o['base'][k]+m['minus'][k])/s**2 for k in m['second']}
  err=max(abs(der[k]-m['deriv'][k]) for k in der);err2=max(abs(second[k]-m['second'][k]) for k in second);assert err<1e-8 and err2<1e-8
  out['difference_arithmetic'].append({'tag':tag,'mode':m['i'],'max_derivative_difference':err,'max_second_difference':err2,'sampled_dc':s*m['dcl'],'sampled_C_range':[m['minus']['C'],m['plus']['C']],'sampled_residual_relative_increases':[m[sgn]['F_psi_2']/o['base']['F_psi_2']-1 for sgn in ['minus','plus']],'dx_dc':der['xstar']/der['c_l'],'d3_dc':der['d3']/der['c_l'],'d5_dc':der['d5']/der['c_l'],'d3_linear_change_at_dc_0p001':.001*der['d3']/der['c_l']})
fine=obs['n120m48_S'];coarse=obs['n96m40S'];keys=['c_l','xstar','C','gP','d3','d5','d7','wpp_at_xstar'];target={k:coarse['base'][k]-fine['base'][k] for k in keys};out['coarse_minus_fine_observables']=target
for tag,ks,idx in [('n120m48_S',['c_l','xstar'],[0,1]),('n120m48_S',['c_l','xstar','C'],[0,1,2]),('n96m40S',['c_l','xstar'],[0,1])]:
 o=obs[tag];M=np.array([[o['modes'][i]['deriv'][k] for i in idx] for k in ks]);z=np.linalg.solve(M,[target[k] for k in ks]);actions={k:sum(z[j]*o['modes'][i]['deriv'][k] for j,i in enumerate(idx)) for k in keys};err=max(abs(actions[k]-target[k]) for k in ks);assert err<1e-14
 out['combinations'].append({'tag':tag,'matched_observables':ks,'modes':idx,'matrix':M.tolist(),'coefficients':z.tolist(),'matrix_condition':float(np.linalg.cond(M)),'sample_step':o['s'],'max_coefficient_over_step':float(max(abs(z))/o['s']),'matched_error':err,'predicted_change':actions,'mismatch':{k:actions[k]-target[k] for k in keys}})
assert np.array_equal(np.array([[1,1],[1,2]])@np.array([3,-2]),[1,-1])
(ROOT/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
print('ALL_ARITHMETIC_CHECKS_PASS')
