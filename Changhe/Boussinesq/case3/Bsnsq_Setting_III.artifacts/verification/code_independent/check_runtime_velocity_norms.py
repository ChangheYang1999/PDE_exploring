"""Independent full-plane norms and finite arithmetic audit, no NUM imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
R=Path('research/291_runtime_velocity_norms/verification');t0=time.monotonic();utc=lambda:datetime.now(timezone.utc).isoformat()
m=json.loads((R/'manifest.json').read_text());checks=[]
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(n,v,d=None):checks.append({'name':n,'passed':bool(v),'detail':d})
check('proof_hash',h(R.parent/'PROOF.md')==m['proof_sha256'])
for p in m['supporting_inputs']:check('support_hash',h(R/p['snapshot'])==p['sha256'],p['snapshot'])
phi=np.arange(1,182)*np.pi/182;sn=np.sin(phi);cs=np.cos(phi)
out={'started_utc':utc(),'status':'RUNNING','states':[],'method':'Own full-plane physical-radius adaptive inverse, 181 interior half-circle angles, component maximum norm. No NUM code imported or executed.','limitations':'Runtime maxima treated as reported; runtime component arrays unavailable. Ordinary quadrature estimates and tolerance sensitivity are not rigorous bounds.'}
def save():
 out.update(checks=checks,passed=sum(c['passed']for c in checks),total=len(checks),elapsed_seconds=time.monotonic()-t0)
 (R/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
for src in m['states']:
 check('archive_hash',h(R/src['snapshot'])==src['sha256'],src['label']);check('runtime_table_hash',h(R/src['runtime_table'])==src['runtime_table_sha256'],src['label'])
 table=json.loads((R/src['runtime_table']).read_text());s=R2State(R/src['snapshot'])
 check('table_metadata',table['beta']==s.beta and table['lam']==s.meta['lam'] and table['K']==s.K,src['label'])
 check('quadrature_labels',table['ng_ref']==12 and table['ng']==48,src['label'])
 check('forced_native_source',s.native_source and s.meta['eps']==1 and s.meta['beta_seed']==3,src['label'])
 unknown=R2ModeSource(s);seed=R2ModeSource(s,kind='native_seed');count=max(unknown.count,seed.count);lam=s.meta['lam']
 def source(r):
  a=unknown(r);b=seed(r);v=np.zeros(count);v[:len(a)]+=a;v[:len(b)]+=lam*b;return v
 row={'label':src['label'],'archive_sha256':src['sha256'],'table_sha256':src['runtime_table_sha256'],'rows':[]};out['states'].append(row)
 invs=[AdaptiveModalInverse(source,count,ModalSettings(min(1/s.bb,1/s.meta['beta_seed']),tol,tol)) for tol in [1e-10,3e-12]]
 arrays={}
 for item in table['rows']:
  r=item['r'];vel=[]
  check('ratio_arithmetic_U',np.isclose(item['rel_to_maxU'],item['max_dU']/item['max_U48'],rtol=1e-14,atol=0),[src['label'],r])
  check('ratio_arithmetic_beta_r',np.isclose(item['rel_to_beta_r'],item['max_dU']/(s.beta*r),rtol=1e-14,atol=0),[src['label'],r])
  for inv in invs:
   pr,dp=inv.radial(r);n=inv.n
   ur=-(n*pr)@np.cos(n[:,None]*phi);ut=dp@np.sin(n[:,None]*phi)
   vel.append(np.column_stack((ur*sn+ut*cs,-ur*cs+ut*sn)))
  V=vel[1];M=float(np.max(abs(V)));change=float(np.max(abs(vel[0]-V)))
  normdiff=abs(item['max_U48']-M)
  rec={**item,'independent_max_V':M,'independent_max_V_over_beta_r':M/(s.beta*r),'independent_tolerance_change_max':change,'independent_relative_tolerance_change':change/M,'absolute_difference_of_norms':normdiff,'difference_of_norms_over_independent_norm':normdiff/M,'difference_of_norms_over_beta_r':normdiff/(s.beta*r),'half_runtime_D_over_beta_r':item['max_dU']/(2*s.beta*r)}
  row['rows'].append(rec);arrays[f'V_r{r:g}']=V
  print(src['label'],r,'M',M,'normdiff/own',normdiff/M,'tol',change/M,flush=True);save()
 for j,inv in enumerate(invs):
  row[f'quadrature_{j}']=inv.evidence;check('adaptive_integrals_report_success',all(v['inner_success'] and v['outer_success'] for v in inv.evidence),[src['label'],j])
 arrays['phi']=phi;np.savez_compressed(R/(src['label']+'_independent.npz'),**arrays)
 row['status']='COMPLETE';save()
out.update(status='COMPLETE',ended_utc=utc(),script_sha256=h(__file__),dependency_hashes={n:h(Path('code_independent')/n)for n in ['r2_state_values.py','adaptive_modal_inverse.py']});save();print('COMPLETE',out['passed'],out['total'],out['elapsed_seconds'],flush=True)
