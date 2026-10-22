"""Independent P244 array computations; no NUM code execution or map claims."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
R=Path('research/244_j2_revision_and_schur/verification');P=Path('research/234_lineage1_jacobian/verification')
now=lambda:datetime.now(timezone.utc).isoformat();start=time.monotonic();o={'started_utc':now(),'checks':[]}
def ck(n,b,**data):o['checks'].append({'name':n,'pass':bool(b),**data})
def near(n,a,b,atol=1e-10,rtol=1e-9):ck(n,abs(a-b)<=atol+rtol*abs(b),actual=float(a),comparison=float(b))
f=np.load(P/'frozen_sources/jacobian.npz',allow_pickle=False);prior=np.load(P/'recomputed_matrix_arrays.npz',allow_pickle=False)
m=json.loads((R/'own_P234.json').read_text())['values'];d=json.loads((R/'jac_summary.json').read_text());post=json.loads((R/'jac_post.json').read_text());aug=json.loads((R/'jac_aug.json').read_text())
text=(R/'NUM_REPORT.md').read_text();sec=text.split('(g) J2:')[1].split('(iii) Equal-budget')[0]
for n,s in [('matrix_cause','does not establish that causal explanation'),('coefficient_scope','this is not a localization statement in physical radius'),('vertex_scope','two states do not establish that the near-null direction is'),('root_scope','Neither state is an exact root'),('forced_scope','nothing here concerns the unforced problem'),('source_scope','comparison does not isolate the effect of vertex proximity')]:ck('scope repair '+n,s in sec)
ck('no blanket existence assertion in header','no candidate exists' not in text.split('## 5b.')[1].split('\n')[0])
# Supplied singular vectors are verified against the supplied J, with their own sign convention.
J=f['JT'];V=f['Vweak'];U=f['Uweak'];sig=f['S'][-8:]
ck('singular-vector archive dimensions',V.shape==(8,1332)and U.shape==(1332,8))
ck('right singular vectors orthonormal',np.linalg.norm(V@V.T-np.eye(8),ord=np.inf)<1e-10)
ck('left singular vectors orthonormal',np.linalg.norm(U.T@U-np.eye(8),ord=np.inf)<1e-10)
for i in range(8):ck('independent singular equation '+str(i),np.linalg.norm(J@V[i]-V[i]-sig[i]*U[:,i])<1e-9,residual=float(np.linalg.norm(J@V[i]-V[i]-sig[i]*U[:,i])))
act=f['act_idx'].astype(int);nb=d['Nt']+5;full=np.zeros(d['K']*nb);full[act]=V[-1];full=full.reshape(d['K'],nb)
radial=(full*full).sum(axis=0);angular=(full*full).sum(axis=1);energy=float(radial[-3:].sum())
near('weak vector normalized energy',radial.sum(),1)
near('last three coefficient squared norm rounded',energy,.436,atol=.0005,rtol=0)
ck('largest radial contributions actually last three',set(np.argsort(radial)[-3:])==set(range(nb-3,nb)))
for k,p in [(2,.20),(1,.20),(3,.16),(4,.12)]:near('mode coefficient energy rounded '+str(k),angular[k],p,atol=.005,rtol=0)
vl=prior['v_lambda'];vb=prior['v_beta'];ml=m['linearized']['m_lambda'];mb=m['linearized']['m_beta']
bound=abs(ml)/np.sqrt(1+vl@vl);correction=-(m['outer_defect']+m['linearized']['Newton_strain'])/mb
near('Schur upper bound versus NUM',bound,aug['schur']['bound_sigma_min_B_lambda'])
ck('Schur bound above actual array minimum',bound>=m['augmented']['B_lambda']['sigma_min_positive_raw'])
near('corrected linearized beta displacement rounded',correction,-1.746e-5,atol=5e-9,rtol=0)
near('lambda state response norm rounded',np.linalg.norm(vl),1045,atol=.5,rtol=0)
near('beta state response norm rounded',np.linalg.norm(vb),311,atol=.5,rtol=0)
near('projection ratio independently verified in P234',m['coefficient_metric']['projection_Jq_ratio'],3.9e-6,atol=.05e-6,rtol=0)
for key in ['dT_dlam','dT_dbeta']:
 c=np.abs(U.T@f[key])/np.linalg.norm(f[key]);near(key+' weak-left cosines',np.max(c),max(d['cos_dTdlam_weakU'if key=='dT_dlam'else'cos_dTdbeta_weakU']))
 ck(key+' reported cosine upper bound',np.max(c)<=.082)
rawcond=m['augmented']['B_lambda']['sigma_max_raw']/m['augmented']['B_lambda']['sigma_min_positive_raw']
scaledcond=aug['B_lambda']['sv_largest_scaled']/m['augmented']['B_lambda']['sigma_min_positive_scaled']
near('raw augmented condition rounding',rawcond,4.2e5,atol=.05e5,rtol=0)
near('scaled augmented condition rounding',scaledcond,5.7e4,atol=.05e4,rtol=0)
# This aggregates logs. Raw finite-difference columns are absent and are not reconstructed.
steps=np.array([x['reldiff']for x in d['step_study']]);ck('twelve logged step columns',steps.shape==(12,2))
for i,wantlo,wanthi,tollo,tolhi in [(0,8.3e-5,3.5e-3,.05e-5,.05e-3),(1,1.1e-5,3.6e-4,.05e-5,.05e-4)]:
 near('logged minimum round '+str(i),steps[:,i].min(),wantlo,atol=tollo,rtol=0);near('logged maximum round '+str(i),steps[:,i].max(),wanthi,atol=tolhi,rtol=0)
for name,vals in [('raw and scaled reported field metric',post['field_metric'])]:ck(name,vals['cond']>0)
o.update(values={'last_three_coefficient_fraction':energy,'radial_coefficient_energies':radial.tolist(),'mode_coefficient_energies':angular.tolist(),'Schur_bound_B_lambda':float(bound),'linearized_beta_correction':float(correction),'raw_Blambda_condition':float(rawcond),'scaled_Blambda_condition_NUMmaximum_and_ownminimum':float(scaledcond),'logged_step_ranges':[[float(steps[:,i].min()),float(steps[:,i].max())]for i in range(2)]},ended_utc=now(),elapsed_seconds=time.monotonic()-start,passed=sum(c['pass']for c in o['checks']),total=len(o['checks']),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),limitations=['FD step columns not supplied; only logged range aggregation','NUM sampled-field maximum singular value not independently recomputed','no exact nonlinear derivative/root/branch'])
(R/'checks.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items()if k not in ['checks','values']},indent=2));print('FAILURES',[c for c in o['checks']if not c['pass']]);print('VALUES',json.dumps({k:v for k,v in o['values'].items()if'energies'not in k}))
