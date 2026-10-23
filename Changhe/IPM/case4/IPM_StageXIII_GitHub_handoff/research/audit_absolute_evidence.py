"""Standard-library-only read-only integrity audit of absolute-loss evidence.

No numerical package or research engine is imported. Missing/in-progress final
outputs are PENDING unless --require-complete is requested. Archived assessment
v1 source is accepted only by exact SHA-256 match to the recorded snapshot.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'base'
HEX=set('0123456789abcdef')
CORE={'absolute_fields.py','highprecision_origin.py','absolute_common.py'}
ROLE_SOURCES={
 'field_tests.json':CORE|{'field_tests.py'},
 'manufactured_tests.json':{'manufactured_tests.py','manufactured_reference.py'},
 'integration_driver_tests.json':{'integration_driver_tests.py','manufactured_reference.py','log_integral.py'},
 'tail_envelope_tests.json':{'tail_envelope_tests.py','outer_envelopes.py','tail_envelope.py','absolute_fields.py'},
 'candidate_semantics.json':{'candidate_semantics.py','absolute_chart.py','absolute_fields.py','highprecision_origin.py'},
 'far_asymptotic_checks.json':CORE|{'far_asymptotic.py'},
 'arithmetic_comparison.json':CORE|{'arithmetic_comparison.py'},
 'exact_dilation_checks.json':{'exact_dilation_checks.py','absolute_fields.py','highprecision_origin.py'},
 'global_chart_v2.json':{'absolute_chart_v2.py','chart_diagnostics_v2.py','absolute_chart.py','absolute_fields.py','highprecision_origin.py'},
}


def read(path):return json.loads(Path(path).read_text())


def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()


def sha(value):return isinstance(value,str) and len(value)==64 and set(value)<=HEX


def relative(path):
 try:return str(Path(path).relative_to(ROOT))
 except ValueError:return str(path)


def expected_records():
 rows=[('results/'+name,'acceptance' if name not in ('candidate_semantics.json','far_asymptotic_checks.json') else 'diagnostic') for name in ROLE_SOURCES if name!='global_chart_v2.json']
 for case in ('stage11','combined','local','global'):
  rows += [('results/integrals/'+case+'.json','integral'),('results/assessments/'+case+'.json','assessment'),
           ('results/derivatives/'+case+'/checks.json','preserved_failure' if case=='global' else 'acceptance'),('results/whole_axis_preparation/'+case+'/preparation.json','acceptance')]
 for factor in (2,16,256,1024):
  label='stage11_lambda_'+str(factor)
  rows += [('results/integrals/'+label+'.json','integral'),('results/assessments/'+label+'.json','assessment')]
 rows += [('results/chart_diagnostics_v2/global_chart_v2.json','acceptance'),('results/derivatives/global_recovery/checks.json','acceptance')]
 return rows


def source_map(record):
 out={}
 for key in ('source_identity','sources'):
  item=record.get(key,{})
  if isinstance(item,dict):
   if isinstance(item.get('new_sources'),dict):out.update(item['new_sources'])
   else:out.update({k:v for k,v in item.items() if k.endswith('.py') and sha(v)})
 if isinstance(record.get('source_sha256'),dict):out.update(record['source_sha256'])
 return out


def used_sources(path):
 if '/integrals/' in str(path):return CORE|{'integrate_candidate.py','log_integral.py','outer_envelopes.py','tail_envelope.py'}
 if '/assessments/' in str(path):return CORE|{'assess_candidates.py'}
 if '/derivatives/global_recovery/' in str(path):return {'absolute_common.py','absolute_fields.py','highprecision_origin.py','absolute_model.py','absolute_chart.py','absolute_chart_v2.py','absolute_derivative_checks.py','absolute_derivative_checks_v2.py','chart_diagnostics_v2.py'}
 if '/derivatives/' in str(path):return {'absolute_fields.py','highprecision_origin.py','absolute_model.py','absolute_chart.py','absolute_derivative_checks.py'}
 if '/whole_axis_preparation/' in str(path):return {'absolute_fields.py','highprecision_origin.py','absolute_model.py','whole_axis_mesh.py','prepare_whole_axis.py'}
 return ROLE_SOURCES.get(path.name,set())


def walk(value,trail=()):
 if isinstance(value,dict):
  yield trail,value
  for k,v in value.items():yield from walk(v,trail+(str(k),))
 elif isinstance(value,list):
  for i,v in enumerate(value):yield from walk(v,trail+(str(i),))


def run(args):
 errors=[];warnings=[];pending=[];observations=[];checks=[];hash_cache={};record_rows=[];accepted_runs=set();preserved_runs=set();referenced_artifacts={};loaded_records={}
 def hashed(path):
  path=Path(path)
  if path not in hash_cache:hash_cache[path]=digest(path)
  return hash_cache[path]
 def check_file(path,want,context,required=True):
  path=Path(path)
  if not path.is_file():
   (errors if required else pending).append({'context':context,'problem':'missing file','path':str(path)});return False
  got=hashed(path)
  if got!=want:errors.append({'context':context,'problem':'SHA-256 mismatch','path':str(path),'expected':want,'actual':got});return False
  checks.append({'context':context,'path':relative(path),'sha256':got});return True
 manifest=read(ROOT/'provenance/base_manifest.json')
 for name,want in manifest.items():check_file(BASE/name,want,'immutable base')
 actual_base={str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file()}
 extra=sorted(actual_base-set(manifest))
 if extra:errors.append({'context':'immutable base','problem':'unmanifested files','paths':extra})
 index=read(ROOT/'inputs/candidates.json')
 if not isinstance(index.get('a_ref'),(int,float)) or not index['a_ref']>0:errors.append({'context':'fixed reference','problem':'a_ref is not positive'})
 for label,item in index['candidates'].items():
  check_file(ROOT/'inputs'/(label+'.json'),item['source_sha256'],'candidate input '+label)
  check_file(item['original_path'],item['source_sha256'],'original candidate '+label)
 if index['a_ref']!=read(ROOT/'inputs/stage11.json')['a0']:errors.append({'context':'fixed reference','problem':'a_ref differs from saved Stage XI a0'})
 design_path=ROOT/'inputs/absolute_assessment_design.json'
 if design_path.exists():
  design=read(design_path)
  check_file(design['original_30_regions'],design['original_30_regions_sha256'],'frozen original independent grids')
  check_file(ROOT/'inputs/absolute_assessment_coordinates.npz',design['new_coordinate_file_sha256'],'frozen added assessment coordinates')
 else:pending.append({'context':'assessment design','problem':'not yet present'})
 archive_path=ROOT/'provenance/source_versions/assessment_versions.json'
 archives={}
 if archive_path.exists():
  versions=read(archive_path)
  for ver in ('v1','v2'):
   p=ROOT/'provenance/source_versions'/('assess_candidates_'+ver+'.py');want=versions[ver+'_sha256']
   if check_file(p,want,'archived assessment '+ver):archives[want]=p
 # Every reference is hashed; processing excludes partial and superseded failed
 # serialization artifacts, which remain preserved and listed below.
 rows=expected_records()
 preservation=read(ROOT/'provenance/global_derivative_v1_failure.json')
 check_file(preservation['record_path'],preservation['record_sha256'],'preserved original global derivative failure')
 check_file(preservation['arrays_path'],preservation['arrays_sha256'],'preserved original global derivative failure arrays')
 known={p for p,_ in rows}
 for p in sorted((ROOT/'results/integrals').glob('*.json')):
  if relative(p) not in known:rows.append((relative(p),'integral'))
 for p in sorted((ROOT/'results/assessments').glob('*.json')):
  if relative(p) not in known:rows.append((relative(p),'assessment'))
 ledger_path=ROOT/'resource_session/session_ledger.jsonl';ledger=[json.loads(v) for v in ledger_path.read_text().splitlines() if v.strip()]
 ledger_map={r['run_id']:r for r in ledger}
 resource_runs={p.name:p for p in (ROOT/'resource_session/runs').iterdir() if p.is_dir()}
 command_records=[json.loads(v) for v in (ROOT/'provenance/commands.jsonl').read_text().splitlines() if v.strip()]
 for name,role in rows:
  path=ROOT/name
  if not path.exists():pending.append({'context':name,'problem':'expected final output not yet present'});continue
  try:r=read(path)
  except (ValueError,OSError) as exc:errors.append({'context':name,'problem':'unreadable JSON','detail':str(exc)});continue
  complete=r.get('completed',r.get('complete',True))
  if complete is False:
   pending.append({'context':name,'problem':'output is still in progress'});continue
  status={'path':name,'sha256':hashed(path),'role':role,'complete':True,'passed':r.get('passed',r.get('numerical_error_checks_passed'))}
  record_rows.append(status);loaded_records[name]=r
  if role=='preserved_failure':
   if r.get('passed') is not False or len(r.get('raw_checks',[]))!=31 or not all(v.get('passed') for v in r.get('raw_checks',[])) or r.get('feasible_chart_failure')!='Analytic-center C5 normal system is unresolved':
    errors.append({'context':name,'problem':'preserved global v1 failure no longer matches recorded completed raw-PASS/chart-FAIL evidence'})
  if role=='acceptance' and r.get('passed') is not True:errors.append({'context':name,'problem':'completed acceptance record did not pass'})
  if role=='integral':
   if not r.get('numerical_error_checks_passed') or not r.get('finite_whole_axis'):errors.append({'context':name,'problem':'whole-radius numerical checks did not pass'})
   if r.get('center_convention')!='center_chart':errors.append({'context':name,'problem':'unexpected center interpretation'})
   value=r.get('J_abs_estimate');err=r.get('total_error_diagnostic')
   if not all(isinstance(x,(int,float)) and math.isfinite(x) and x>=0 for x in (value,err)):errors.append({'context':name,'problem':'nonfinite/negative integral or diagnostic'})
  if role=='assessment' and len(r.get('regions',{}))!=32:errors.append({'context':name,'problem':'not all 32 frozen regions are present'})
  if path.name=='candidate_semantics.json':
   for label,case_record in r.get('candidates',{}).items():
    hp=case_record.get('center_chart_independent_C5_report',{})
    if not case_record.get('all_saved_core_free_and_extra_coefficients_preserved') or case_record.get('candidate_repaired_refitted_or_overwritten') is not False:
     errors.append({'context':name+':'+label,'problem':'saved independent coefficients not preserved'})
    if not case_record.get('original_physical_parameter_bounds_pass') or not case_record.get('center_chart_C5_passes_historical_1e_minus10_tolerance') or not case_record.get('center_chart_all_C5_physical_residual_coefficients_pass_1e_minus10') or hp.get('max_abs',math.inf)>1e-10:
     errors.append({'context':name+':'+label,'problem':'analytic-center interpretation violates original bounds or C5 tolerance'})
  if 'a_ref' in r and r['a_ref']!=index['a_ref']:errors.append({'context':name,'problem':'reference amplitude changed'})
  for flag in ('optimization_performed','candidate_modified','saved_candidates_modified','candidate_exported','old_basis_refit_performed'):
   if r.get(flag) is True:errors.append({'context':name,'problem':'forbidden mutation/optimization flag '+flag})
  sources=source_map(r);needed=used_sources(path)
  for source in needed:
   want=sources.get(source)
   if not sha(want):errors.append({'context':name,'problem':'missing critical numerical source binding','source':source});continue
   current=ROOT/source
   if current.is_file() and hashed(current)==want:checks.append({'context':name+' critical source','path':source,'sha256':want})
   elif source=='assess_candidates.py' and want in archives:observations.append({'context':name,'archived_source_accepted':relative(archives[want]),'sha256':want})
   else:errors.append({'context':name,'problem':'critical numerical source hash mismatch','source':source,'expected':want,'actual':hashed(current) if current.is_file() else None})
  # Global source snapshots include files never imported by this worker.
  # Their evolution is informational rather than falsely invalidating evidence.
  for source,want in sources.items():
   if source not in needed and sha(want) and (ROOT/source).is_file() and hashed(ROOT/source)!=want:
    observations.append({'context':name,'unrelated_snapshot_source_changed':source,'recorded_sha256':want,'current_sha256':hashed(ROOT/source)})
  for trail,obj in walk(r):
   for key,want in obj.items():
    if not sha(want):continue
    context=name+':'+'.'.join(trail+(key,));target=None
    if key=='base_manifest_sha256':target=ROOT/'provenance/base_manifest.json'
    elif key=='candidate_index_sha256':target=ROOT/'inputs/candidates.json'
    elif key=='candidate_sha256':
     target=Path(obj['candidate_path']) if obj.get('candidate_path') else (ROOT/'inputs'/(str(obj.get('case',r.get('case')))+'.json') if obj.get('case',r.get('case')) else None)
    elif key=='design_sha256':target=design_path
    elif key=='arrays_sha256':target=obj.get('arrays_path',obj.get('array_path'))
    elif key=='artifact_sha256':target=obj.get('artifact',obj.get('artifact_path'))
    elif key.endswith('_file_sha256'):target=obj.get(key[:-12]+'_path')
    elif key.endswith('_sha256'):
     stem=key[:-7];target=obj.get(stem+'_path')
    if target:
     target=Path(target);target=target if target.is_absolute() else ROOT/target
     check_file(target,want,context)
     if target.suffix=='.npz':referenced_artifacts[str(target)]=want
  env=next((r[k] for k in ('native_environment','provenance','environment') if isinstance(r.get(k),dict) and r[k].get('resource_run')),None)
  if env is None and r.get('resource_run'):env=r
  if env is not None:
   runpath=Path(env['resource_run']);runid=runpath.name
  else:
   # Manufactured analytic reference has no embedded process provenance; bind
   # its accepted supervisor execution by exact worker script and command log.
   worker=next((s for s in needed if s==path.stem+'.py'),None)
   matches=[]
   if worker:
    for runid0,p0 in resource_runs.items():
     rp=p0/'result.json'
     if rp.exists():
      rr=read(rp)
      if rr.get('success') and any(Path(v).name==worker for v in rr.get('command',[])):matches.append(p0)
   if len(matches)==1:runpath=matches[0];runid=runpath.name;observations.append({'context':name,'resource_binding':'unique successful exact worker command (record has no embedded provenance)'})
   else:errors.append({'context':name,'problem':'no unambiguous supervisor provenance'});continue
  if runpath.parent!=ROOT/'resource_session/runs':errors.append({'context':name,'problem':'resource run outside fresh session','path':str(runpath)});continue
  rp=runpath/'result.json'
  if not rp.exists():pending.append({'context':name,'problem':'supervisor result still pending'});continue
  rr=read(rp)
  if role=='preserved_failure':preserved_runs.add(runid)
  else:accepted_runs.add(runid)
  expected_returncode=2 if role=='preserved_failure' else 0
  expected_success=role!='preserved_failure'
  if rr.get('success') is not expected_success or rr.get('returncode')!=expected_returncode or rr.get('stop_reasons'):errors.append({'context':name,'problem':'supervisor outcome does not match acceptance/preserved-failure role','run':runid,'expected_returncode':expected_returncode})
  if runid not in ledger_map or ledger_map[runid].get('returncode')!=expected_returncode:errors.append({'context':name,'problem':'matching run outcome missing from fresh ledger','run':runid})
  controlled=rr.get('controlled_environment',{})
  for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
   if controlled.get(key)!='1':errors.append({'context':name,'problem':'thread policy mismatch','variable':key})
  if env and env is not r:
   if env.get('resource_session')!=str(ROOT/'resource_session'):errors.append({'context':name,'problem':'embedded session mismatch'})
   if env.get('nice')!=15:errors.append({'context':name,'problem':'unexpected niceness'})
   for pool in env.get('threadpools',[]):
    if pool.get('num_threads')!=1:errors.append({'context':name,'problem':'loaded BLAS thread count is not 1'})
  worker=Path(rr['command'][-1]).name
  # Arguments may follow worker, so select the Python source argument itself.
  workerpaths=[Path(v) for v in rr.get('command',[]) if isinstance(v,str) and v.endswith('.py')]
  if workerpaths:
   worker=workerpaths[-1].name;want=sources.get(worker)
   runtime_command=rr.get('command',[])
   matching_commands=[c for c in command_records if len(c.get('command',[]))>=len(runtime_command) and c['command'][-len(runtime_command):]==runtime_command and (want is None or c.get('worker_sha256')==want) and 0<=rr.get('started_time',0)-c.get('epoch',0)<=300]
   if not matching_commands:errors.append({'context':name,'problem':'no matching launch command/source hash','worker':worker})
 # NPZ paths must always have a sibling digest. Catch a new result field that
 # would otherwise silently escape the recognized artifact conventions.
 for row in record_rows:
  record=read(ROOT/row['path'])
  for trail,obj in walk(record):
   for key,value in obj.items():
    if isinstance(value,str) and value.endswith('.npz') and (key.endswith('_path') or key in ('artifact','array_path')):
     p=Path(value);p=p if p.is_absolute() else ROOT/p
     if str(p) not in referenced_artifacts:errors.append({'context':row['path']+':'+'.'.join(trail+(key,)),'problem':'NPZ reference lacks verified SHA-256','path':str(p)})
 # A new coordinate chart cannot erase the original failed preparation.
 # Acceptance requires separately completed full derivative and geometry tests.
 recovery_name='results/derivatives/global_recovery/checks.json'
 geometry_name='results/chart_diagnostics_v2/global_chart_v2.json'
 recovery=loaded_records.get(recovery_name);geometry=loaded_records.get(geometry_name)
 recovery_ok=False;geometry_ok=False
 if geometry is not None:
  ng=geometry.get('new_geometry',{})
  geometry_ok=bool(geometry.get('passed') is True and geometry.get('original_to_new_coordinate_rank')==19 and geometry.get('all_19_original_feasible_directions_represented') is True and geometry.get('normal_cl_row_is_exact_zero') is True and geometry.get('all_5_physical_constraints_unchanged') is True and geometry.get('HP_tolerance_unchanged_1e_minus10') is True and geometry.get('numerical_singular_pairs_removed') is False and geometry.get('base_candidate_corrected') is False and ng.get('all_five_singular_pairs_retained') is True and ng.get('tangent_rank')==19 and ng.get('complete_24_rank')==24 and ng.get('raw_G_normal_condition',math.inf)<=1e10 and ng.get('base_HP',{}).get('max_abs',math.inf)<1e-10)
  if not geometry_ok:errors.append({'context':geometry_name,'problem':'required v2 full-family geometry qualification failed'})
 if recovery is not None:
  bindings=recovery.get('recovery_bindings',{})
  required_bindings={'geometry_diagnostic_path':str(ROOT/geometry_name),
   'geometry_diagnostic_sha256':hashed(ROOT/geometry_name) if (ROOT/geometry_name).exists() else None,
   'geometry_diagnostic_arrays_path':geometry.get('arrays_path') if geometry else None,
   'geometry_diagnostic_arrays_sha256':geometry.get('arrays_sha256') if geometry else None,
   'preserved_v1_failed_checks_path':preservation['record_path'],
   'preserved_v1_failed_checks_sha256':preservation['record_sha256'],
   'preserved_v1_failed_arrays_path':preservation['arrays_path'],
   'preserved_v1_failed_arrays_sha256':preservation['arrays_sha256'],
   'candidate_sha256':index['candidates']['global']['source_sha256'],
   'new_chart_source_sha256':hashed(ROOT/'absolute_chart_v2.py'),
   'geometry_is_coordinate_change_not_new_function_space':True,
   'all_five_constraints_and_all_nineteen_core_directions_retained':True,
   'normal_corrections_leave_cl_fixed':True}
  bindings_ok=recovery.get('recovery_bindings_unchanged') is True and all(bindings.get(k)==v for k,v in required_bindings.items())
  if not bindings_ok:errors.append({'context':recovery_name,'problem':'recovery is not bound to exact preserved failure, v2 geometry and current chart source'})
  raw=recovery.get('raw_checks',[]);feasible=recovery.get('feasible_checks',[]);operators=recovery.get('operator_checks',[])
  thresholds={'raw_two_step_relative':3e-5,'feasible_two_step_relative':1e-3,'operator_relative':1e-10,'adjoint_scaled':1e-12,'C5_absolute':1e-10}
  recovery_ok=bool(bindings_ok and recovery.get('passed') is True and recovery.get('thresholds')==thresholds and len(raw)==31 and len(feasible)==23 and len(operators)==3 and all(v.get('passed') and len(v.get('steps',[]))==2 and all(t.get('relative_error',math.inf)<3e-5 for t in v['steps']) for v in raw) and all(v.get('passed') and len(v.get('steps',[]))==2 and all(t.get('completed') and t.get('relative_error',math.inf)<1e-3 and t.get('maximum_HP_defect',math.inf)<1e-10 for t in v['steps']) for v in feasible) and all(v.get('passed') and max(v.get('Jv_relative',math.inf),v.get('JT_relative',math.inf))<1e-10 and v.get('adjoint_scaled',math.inf)<1e-12 for v in operators))
  if not recovery_ok:errors.append({'context':recovery_name,'problem':'required full global recovery derivative checks did not pass unchanged thresholds/counts'})
 if not (recovery_ok and geometry_ok):errors.append({'context':'global derivative acceptance','problem':'original v1 chart failure remains unresolved until separate geometry and full derivative recovery both pass'})
 failure_resolution={'original_failure_preserved':True,'original_record_sha256':preservation['record_sha256'],'geometry_passed':geometry_ok,'separate_full_derivative_recovery_passed':recovery_ok,'resolved':recovery_ok and geometry_ok}
 # Invariance comparisons use the independently expanded/refined integral
 # records, rather than treating a translated finite window as invariant.
 dilation_comparisons=[]
 baseline_path=ROOT/'results/integrals/stage11.json'
 if baseline_path.exists():
  baseline=read(baseline_path)
  for factor in (2,16,256,1024):
   dilation_path=ROOT/'results/integrals'/('stage11_lambda_'+str(factor)+'.json')
   if not dilation_path.exists():continue
   other=read(dilation_path)
   difference=abs(other['J_abs_estimate']-baseline['J_abs_estimate'])
   limit=other['total_error_diagnostic']+baseline['total_error_diagnostic']+128*2.220446049250313e-16*max(abs(other['J_abs_estimate']),abs(baseline['J_abs_estimate']))
   ok=other.get('dilation')==factor and difference<=limit
   dilation_comparisons.append({'factor':factor,'difference':difference,'combined_numerical_diagnostic':limit,'passed':ok})
   if not ok:errors.append({'context':relative(dilation_path),'problem':'scale-invariance comparison outside combined recorded numerical diagnostics'})
 incomplete_runs=[p.name for p in resource_runs.values() if not (p/'result.json').exists()]
 if incomplete_runs:pending.append({'context':'fresh resource session','problem':'running supervisor results','runs':incomplete_runs})
 failed_runs=[{'run_id':r['run_id'],'returncode':r.get('returncode'),'stop_reasons':r.get('stop_reasons',[])} for r in ledger if r.get('returncode')!=0]
 preserved_partials=[relative(p) for p in sorted((ROOT/'results').glob('*.serialization_failed*.partial'))]
 if failed_runs:observations.append({'preserved_nonacceptance_failed_runs':failed_runs,'not_counted_as_passes':True})
 if preserved_partials:observations.append({'preserved_serialization_partials':preserved_partials})
 if args.require_complete and pending:errors.append({'context':'completion gate','problem':'required evidence or supervisor work remains pending','pending_count':len(pending)})
 result={'schema':'absolute_evidence_readonly_audit_v1','epoch':time.time(),'require_complete':args.require_complete,
  'passed':not errors,'complete':not pending,'errors':errors,'pending':pending,'warnings':warnings,'observations':observations,
  'base_manifest_files_verified':len(manifest),'candidate_inputs_verified':len(index['candidates']),
  'completed_records':record_rows,'verified_reference_count':len(checks),'verified_npz_artifacts':referenced_artifacts,
  'global_derivative_failure_resolution':failure_resolution,'preserved_failure_supervisor_runs':sorted(preserved_runs),'scale_invariance_integral_comparisons':dilation_comparisons,'accepted_supervisor_runs':sorted(accepted_runs),'resource_ledger_runs':len(ledger),'preserved_failed_run_count':len(failed_runs),
  'audit_source_sha256':digest(Path(__file__)),'numerical_execution_performed':False,
  'scope':'hashes, completion flags, recorded numerical PASS states and fresh-session provenance; no independent re-execution or continuous-error certificate'}
 if args.output:
  p=Path(args.output);p=p if p.is_absolute() else ROOT/p
  if ROOT not in p.parents:raise ValueError('Audit output must remain in the new workspace')
  p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.partial');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(p)
 print(json.dumps({'passed':result['passed'],'complete':result['complete'],'errors':len(errors),'pending':len(pending),'records':len(record_rows),'NPZ':len(referenced_artifacts),'output':str(args.output) if args.output else None}))
 if errors:
  for e in errors:print(json.dumps(e))
 return 0 if not errors else 2

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--require-complete',action='store_true');p.add_argument('--output',type=Path);raise SystemExit(run(p.parse_args()))
