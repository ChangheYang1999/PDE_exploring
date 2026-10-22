"""Separate exact witness consumer and six quadrature-stage comparisons for P287."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
R=Path('research/287_quadrature_resolved_fields/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prod(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def power(z,n):
 if n<0:
  d=z[0]**2+z[1]**2;z=(z[0]/d,-z[1]/d);n=-n
 out=(Q(1),Q(0))
 while n:
  if n&1:out=prod(out,z)
  z=prod(z,z);n//=2
 return out
def evaluate(poly,x,y,derivative=False):
 out=(Q(0),Q(0))
 for n,c in poly.items():
  n=int(n);v=tuple(map(Q,c))
  if derivative:v=(-n*v[1],n*v[0])
  v=prod(v,power((x,y),n));out=(out[0]+v[0],out[1]+v[1])
 return out
manifest=json.loads((R/'manifest.json').read_text());known={s['sha256']:s for s in manifest['states']}
tail=json.loads((R/'exact_native_tail.json').read_text())
for s in tail['states']:
 src=known[s['archive_sha256']];check('archive',h(R/src['snapshot'])==s['archive_sha256'],src['label'])
 beta=Q(s['beta_exact']);check('positive_nonzero_lambda',Q(s['lambda_exact'])>0,src['label']);check('positive_native_scales',Q(s['L_exact'])>0 and Q(s['seed_L_exact'])>0,src['label']);check('seed_basis_three',s['seed_basis']==3,src['label']);check('exponent_order',1-3/beta>Q(2,3)-2/beta>0>1-4/beta,str(beta))
 for key,w in s['exact_witnesses'].items():
  x,y=Q(w['cos_theta']),Q(w['sin_theta']);check('unit_witness',x*x+y*y==1,[src['label'],key]);val=evaluate(s['coefficients'][key],x,y)
  check('exact_nonzero_witness',val[1]==0 and val[0]==Q(w['exact_value']) and val[0]!=0,[src['label'],key,float(val[0])])
 for axis in s['source_axes']:
  y=Q(axis['sin_theta']);v=evaluate(s['coefficients']['PS0'],Q(0),y);dv=evaluate(s['coefficients']['PS0'],Q(0),y,True)
  check('source_simple_axis_zero',v==(0,0) and dv[1]==0 and dv[0]==Q(axis['PS_derivative']) and dv[0]!=0,[src['label'],str(y),float(dv[0])])


for src in manifest['supporting_inputs']:
 check('supporting_input_hash',h(R/src['snapshot'])==src['sha256'],src['snapshot'])

import ast,csv
results=json.loads((R/'results.json').read_text())
center=json.loads((R/'center_certificates/checks.json').read_text())
center_by_hash={c['sha256']:c['inverse'] for c in center['checks']}
c2rows=json.loads((R/'inverse_constant_certificates/summary.json').read_text())['rows']
c2_by_hash={c['archive_sha256']:c for c in c2rows}
check('proof_unchanged',h(R.parent/'PROOF.md')==manifest['proof_sha256'])
check('pipeline_complete','ALL_COMPLETE' in (R/'timeline.log').read_text())
check('grid_complete',results['status']=='COMPLETE' and len(results['states'])==6)
check('exact_center_consumer_passed',center['all_passed'] and len(center['checks'])==6)
records=[]
expected_iterations=[8,8,9,4,8,1]
geometry=['beta','beta_basis','beta_seed','beta_fixed','K','Nt','Nphi','deg','grade','L','mreg','ngc','rmap','a0','eps']
for index,src in enumerate(manifest['states']):
 name=src['snapshot'];label=src['label'];logname=name.split('_beta')[0]+'.out'
 log=(R/logname).read_text()
 first=log.splitlines()[0];header=ast.literal_eval(first[first.index('{'):])
 check('quadrature48_log_header',header['ng_quad']==48 and 'ng_quad=48;' in log,label)
 check('permissive_finite_objective_test',header['accept_factor']==1e9,label)
 check('inner_and_outer_tolerances',header['tol_m']==1e-5 and header['tol_f']==3e-5,label)
 stage=[line for line in log.splitlines() if line.startswith('  secant ')]
 check('only_secant_zero',len(stage)==1 and 'secant 0:' in stage[0],label)
 iterations=int(re.search(r'iters=(\d+)',stage[0])[1]);check('logged_inner_count',iterations==expected_iterations[index],[label,iterations])
 check('completed_accepted_log','ok=True' in log and '# picard_lam done ' in log,label)
 with np.load(R/name,allow_pickle=False) as new,np.load(R/src['comparison'],allow_pickle=False) as old,np.load(R/name.replace('.npz','_sec0.npz'),allow_pickle=False) as sec:
  meta={k:new[k].item() for k in new.files if new[k].shape==()}
  changes={k:{'max_absolute':float(np.max(abs(new[k]-old[k]))),'relative_l2':float(np.linalg.norm(new[k]-old[k])/np.linalg.norm(old[k])),'bitwise_equal':bool(np.array_equal(new[k],old[k]))} for k in ['cF','cG','cG_f']}
  check('archive_quadrature_not_recorded','ng_quad' not in new.files,label)
  check('same_geometry',all(np.array_equal(new[k],old[k]) for k in geometry),label)
  check('same_source_geometry',all(np.array_equal(new[k],old[k]) for k in new.files if k.startswith('seed_')),label)
  check('source_unchanged',changes['cG_f']['bitwise_equal'],label)
  check('temperature_updated',changes['cF']['max_absolute']>0,label)
  check('vorticity_update_or_inheritance',changes['cG']['max_absolute']>0 if index<5 else changes['cG']['bitwise_equal'],label)
  check('inherited_lambda',new['lam'].item()==old['lam'].item(),label)
  check('accepted_state_matches_secant0',all(np.array_equal(new[k],sec[k]) for k in ['cF','cG','cG_f','beta','lam']),label)
  check('accepted_flags',all(meta[k]==1 for k in ['converged','inner_converged','continuation_accepted']) and meta['unfinished_selected']==0,label)
  check('source_restart_hash',meta['start_sha256']==h(R/src['comparison']) and Path(meta['start_path']).name==src['comparison'],label)
  check('previous_objective_metadata',meta['prev_stage_obj']==old['obj'].item(),label)
  check('logged_m_below_1p5e6',abs(meta['strain_mismatch'])<1.5e-6,label)
  check('inner_fixedpoint_stopping',meta['inner_crit']=='fixed_point' and meta['inner_f']<3e-5,label)
  check('a0_normalization_label',meta['a0']==(1 if index==5 else 1.011258),label)
  c=center_by_hash[src['sha256']];c2=c2_by_hash[src['sha256']]
  check('self_center_ratio_strictly_positive',c['self']['ratioF']>0 and c['self']['RF']!=0,label)
  check('saved_self_strain_agrees',abs(c['self']['c']-meta['c_self_saved'])<1e-13,label)
  check('weighted_source_strain_metadata',abs(c['forced']['c']-c['self']['c']-meta['src_strain'])<1e-13,label)
  check('C2_strictly_negative',Q(c2['C2_enclosure'][0])<Q(c2['C2_enclosure'][1])<0,[label,c2['C2_enclosure_float']])
  cc=json.loads((R/'inverse_constant_certificates'/f'{label}_certificate.check.json').read_text())
  check('C2_separate_consumer',cc['verdict']=='CONFIRMED_NEGATIVE',label)
  records.append({'label':label,'sha256':src['sha256'],'metadata':meta,'iterations':iterations,'changes':changes,'old_objective':old['obj'].item(),'new_objective':meta['obj'],'objective_increase_percent':100*(meta['obj']/old['obj'].item()-1),'old_logged_m':old['strain_mismatch'].item(),'new_logged_m':meta['strain_mismatch'],'saved_forced_m':c['forced']['m'],'saved_minus_logged_m':c['forced']['m']-meta['strain_mismatch'],'center':c,'C2':c2})
check('all_objectives_increased',all(r['objective_increase_percent']>0 for r in records))
check('lineage1_objective_range',all(.474<r['objective_increase_percent']<3.501 for r in records[:5]))
check('lineage2_objective_increase_below_point03',0<records[5]['objective_increase_percent']<.03)
check('positive_temperature_power_all',all(s['self_verdict']==s['forced_verdict']=='INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL' for s in tail['states']))
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks,'records':records,'script_sha256':h(__file__),'scope':'Six frozen 48-point-quadrature forced states, exact center and tail witness consumers, finite saved-stage comparison. Not a runtime interpolation audit, root shift, convergence theorem or B2 endpoint.'}
(R/'tail_stage_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['passed'],out['total'],out['elapsed_seconds']);print([a for a in checks if not a['passed']])
for r in records:print(r['label'],r['objective_increase_percent'],r['saved_forced_m'],r['saved_minus_logged_m'])
