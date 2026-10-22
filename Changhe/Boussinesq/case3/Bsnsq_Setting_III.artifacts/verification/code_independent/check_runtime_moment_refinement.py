"""Exact-moment and breakpoint sensitivity supplement for P291."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,ModalSettings
from moment_modal_inverse import exact_moment2,MomentModalInverse
R=Path('research/291_runtime_velocity_norms/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();m=json.loads((R/'manifest.json').read_text());checks=[];rows=[]
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(n,ok,d=None):checks.append({'name':n,'passed':bool(ok),'detail':d})
check('original_proof_preserved',h(R/'PROOF_initial.md')==m['original_proof_sha256'])
check('corrected_proof_registered',h(R.parent/'PROOF.md')==m['proof_sha256'])
initial=json.loads((R/'checks.json').read_text());check('initial_142_completed',initial['status']=='COMPLETE' and initial['passed']==initial['total']==142)
for src in m['states']:
 s=R2State(R/src['snapshot']);u=R2ModeSource(s);f=R2ModeSource(s,kind='native_seed');count=max(u.count,f.count);lam=s.meta['lam']
 def source(r):
  a=u(r);b=f(r);z=np.zeros(count);z[:len(a)]+=a;z[:len(b)]+=lam*b;return z
 moment=exact_moment2(s)+Q(lam)*exact_moment2(s,True)
 bp=[]
 for field in [s,s.seed_field]:
  t=field.edges[1:-1];bp.extend(field.L*np.sqrt(np.expm1(-2*field.bb*np.log1p(-t))))
 inv=MomentModalInverse(source,count,ModalSettings(min(1/s.bb,1/s.meta['beta_seed']),3e-12,3e-12),moment,bp)
 with np.load(R/(src['label']+'_independent.npz'),allow_pickle=False) as z:
  phi=z['phi'];sn=np.sin(phi);cs=np.cos(phi)
  for r in [1e8,1e9]:
   pr,dp=inv.radial(r);n=inv.n;ur=-(n*pr)@np.cos(n[:,None]*phi);ut=dp@np.sin(n[:,None]*phi)
   V=np.column_stack((ur*sn+ut*cs,-ur*cs+ut*sn));old=z[f'V_r{r:g}'];diff=float(np.max(abs(V-old)));M=float(np.max(abs(old)))
   check('moment_partition_relative_agreement_below_1e7',diff/M<1e-7,[src['label'],r,diff/M])
   check('moment_quadrature_success',inv.evidence[-1]['inner_success'] and inv.evidence[-1]['outer_success'],[src['label'],r])
   rows.append({'label':src['label'],'radius':r,'moment2_exact':str(moment),'max_component_difference':diff,'relative_difference':diff/M,'refined_max_component':float(np.max(abs(V))),'evidence':inv.evidence[-1]});print(src['label'],r,diff/M,flush=True)
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'rows':rows,'script_sha256':h(__file__),'supplement_proof_sha256':h(R.parent/'SUPPLEMENT_PROOF.md'),'scope':'Numerical consistency with exact global second moment and knot-partitioned quadrature, not a rigorous error bound.'}
(R/'moment_refinement.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['passed'],out['total'],out['elapsed_seconds'],flush=True)
