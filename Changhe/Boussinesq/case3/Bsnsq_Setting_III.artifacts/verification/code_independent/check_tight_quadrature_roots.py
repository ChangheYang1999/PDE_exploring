"""Separate exact witness consumer and two tighter secant-stage comparisons for P294."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
R=Path('research/294_tight_quadrature_roots/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
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
check('grid_complete',results['status']=='COMPLETE' and len(results['states'])==2)
check('exact_center_consumer_passed',center['all_passed'] and len(center['checks'])==2)
records=[]
geometry=['beta','beta_basis','beta_seed','beta_fixed','K','Nt','Nphi','deg','grade','L','mreg','ngc','rmap','a0','eps']
for index,src in enumerate(manifest['states']):
 name=src['snapshot'];label=src['label'];tag=name.split('_beta')[0];order=[12,48][index];log=(R/(tag+'.out')).read_text();header=ast.literal_eval(log.splitlines()[0].split(' ',4)[-1]) if False else ast.literal_eval(log.splitlines()[0][log.splitlines()[0].index('{'):])
 check('nominal_quadrature_order',header['ng_quad']==order and f'ng_quad={order};' in log,label)
 check('same_nominal_tighter_tolerances',header['tol_m']==1e-7 and header['tol_f']==3e-6 and header['iters']==60,label)
 check('finite_objective_acceptance',header['accept_factor']==1e9,label)
 check('same_initial_lambda_and_increment',header['lam0']==.93171 and header['dlam']==.0001,label)
 stage=[l for l in log.splitlines()if l.startswith('  secant ')];check('four_logged_secants',len(stage)==4,label)
 ss=[]
 for i in range(4):
  with np.load(R/f'{tag}_beta3.062_sec{i}.npz',allow_pickle=False)as sec:
   sm={k:sec[k].item()for k in sec.files if sec[k].shape==()};ss.append(sm)
   check('secant_inner_converged',sm['inner_converged']==1 and sm['inner_f']<3e-6,[label,i])
   with np.load(R/src['comparison'],allow_pickle=False)as oldsource:
    check('secant_source_block_unchanged',np.array_equal(sec['cG_f'],oldsource['cG_f']) and all(np.array_equal(sec[k],oldsource[k]) for k in sec.files if k.startswith('seed_')),[label,i])
   match=re.search(r'secant (\d+): beta=([\d.]+) lambda=([\d.]+) m=([+\-\de.]+).*iters=(\d+)',stage[i]);check('secant_log_match',match is not None and int(match[1])==i and float(match[2])==sm['beta'] and abs(float(match[3])-sm['lam'])<=5e-7 and abs(float(match[4])-sm['strain_mismatch'])<=5.1e-11,[label,i])
   if match:sm['logged_iterations']=int(match[5]);check('iteration_count',int(match[5])==[[11,13,13,7],[12,13,13,7]][index][i],[label,i])
 check('bracketing_sample_mismatches',ss[0]['strain_mismatch']>0 and ss[1]['strain_mismatch']<0,label)
 check('outer_threshold_first_met_at3',all(abs(x['strain_mismatch'])>1e-7 for x in ss[:3])and abs(ss[3]['strain_mismatch'])<1e-7,label)
 for i in [2,3]:
  a,b=ss[i-2],ss[i-1];la,lb=Q(a['lam']),Q(b['lam']);ma,mb=Q(a['strain_mismatch']),Q(b['strain_mismatch']);formula=lb-mb*(lb-la)/(mb-ma)
  check('saved_secant_formula_rounding',abs(formula-Q(ss[i]['lam']))<Q(1,10**14),[label,i,float(formula-Q(ss[i]['lam']))])
 with np.load(R/name,allow_pickle=False)as new,np.load(R/src['comparison'],allow_pickle=False)as old,np.load(R/f'{tag}_beta3.062_sec3.npz',allow_pickle=False)as last:
  meta={k:new[k].item()for k in new.files if new[k].shape==()}
  changes={k:dict(max_absolute=float(np.max(abs(new[k]-old[k]))),relative_l2=float(np.linalg.norm(new[k]-old[k])/np.linalg.norm(old[k])),bitwise_equal=bool(np.array_equal(new[k],old[k])))for k in ['cF','cG','cG_f']}
  check('quadrature_not_stored','ng_quad'not in new.files,label)
  check('same_field_geometry',all(np.array_equal(new[k],old[k])for k in geometry),label)
  check('same_native_source_geometry',all(np.array_equal(new[k],old[k])for k in new.files if k.startswith('seed_')),label)
  check('source_unchanged',changes['cG_f']['bitwise_equal'],label)
  check('both_unknown_fields_updated',changes['cF']['max_absolute']>0 and changes['cG']['max_absolute']>0,label)
  check('lambda_not_inherited',new['lam'].item()!=old['lam'].item(),label)
  check('final_fields_match_secant3',all(np.array_equal(new[k],last[k])for k in ['lam','beta','cF','cG','cG_f','obj','strain_mismatch']),label)
  check('final_acceptance_flags',all(meta[k]==1 for k in ['converged','inner_converged','continuation_accepted'])and meta['unfinished_selected']==0,label)
  check('source_restart_hash',meta['start_sha256']==h(R/src['comparison'])and Path(meta['start_path']).name==src['comparison'],label)
  check('previous_objective',meta['prev_stage_obj']==old['obj'].item(),label)
  check('final_fixedpoint_stop',meta['inner_crit']=='fixed_point'and meta['inner_f']<3e-6,label)
  c=center_by_hash[src['sha256']];c2=c2_by_hash[src['sha256']]
  check('exact_self_center_nonzero',c['self']['ratioF']>0 and c['self']['RF']!=0,label)
  check('saved_self_strain_metadata',abs(c['self']['c']-meta['c_self_saved'])<1e-13,label)
  check('weighted_source_metadata',abs(c['forced']['c']-c['self']['c']-meta['src_strain'])<1e-13,label)
  check('exact_saved_forced_m_below_tolerance',0<abs(c['forced']['m'])<1e-7,label)
  check('C2_strict_negative',Q(c2['C2_enclosure'][0])<Q(c2['C2_enclosure'][1])<0,label)
  cert=json.loads((R/'inverse_constant_certificates'/f'{label}_certificate.check.json').read_text());check('C2_independent_consumer',cert['verdict']=='CONFIRMED_NEGATIVE',label)
  slope=(Q(ss[0]['strain_mismatch'])-Q(ss[1]['strain_mismatch']))/(Q(ss[0]['lam'])-Q(ss[1]['lam']))
  records.append(dict(label=label,sha256=src['sha256'],metadata=meta,order=order,secants=ss,sample_slope_exact=str(slope),sample_slope=float(slope),changes=changes,old_lambda=old['lam'].item(),old_objective=old['obj'].item(),new_objective=meta['obj'],objective_increase_percent=100*(meta['obj']/old['obj'].item()-1),lambda_shift_exact=str(Q(meta['lam'])-Q(old['lam'].item())),new_logged_m=meta['strain_mismatch'],saved_forced_m=c['forced']['m'],saved_minus_logged_m=c['forced']['m']-meta['strain_mismatch'],center=c,C2=c2))
check('both_absolute_thermal_residuals_infinite',all(s['self_verdict']==s['forced_verdict']=='INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL'for s in tail['states']))
delta=Q(records[1]['metadata']['lam'])-Q(records[0]['metadata']['lam']);check('positive_finite_order_comparison',Q('1.75e-8')<delta<Q('1.77e-8'),str(delta))
with np.load(R/manifest['states'][0]['snapshot'],allow_pickle=False)as a,np.load(R/manifest['states'][1]['snapshot'],allow_pickle=False)as b:
 between={k:dict(max_absolute=float(np.max(abs(b[k]-a[k]))),relative_l2=float(np.linalg.norm(b[k]-a[k])/np.linalg.norm(a[k])))for k in ['cF','cG']};check('same_exact_source_across_orders',np.array_equal(a['cG_f'],b['cG_f']))
out=dict(started_utc=started,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,records=records,lambda_difference_exact=str(delta),lambda_difference_float=float(delta),between_orders=between,script_sha256=h(__file__),scope='Two finite forced secant re-solves; exact literal-field center and tail obstruction; no continuum root enclosure, convergence theorem or B2 endpoint.')
(R/'tail_stage_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print('FAILED',[x for x in checks if not x['passed']]);print('lambda48-lambda12',float(delta))
for row in records:print(row['label'],row['saved_forced_m'],row['sample_slope'],row['C2']['C2_enclosure_float'])
