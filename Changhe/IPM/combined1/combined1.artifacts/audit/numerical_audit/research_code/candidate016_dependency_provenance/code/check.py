"""Static provenance check. Do not import or run the inspected modules."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import ast, json, time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_dependency_provenance'
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);raw=p.read_bytes();s=sha256(raw).hexdigest();assert h is None or h==s,(p,h,s);inputs[str(p.relative_to(R))]=s;return raw
 prep=json.loads(bind(B/'verification/PREPARE.json'));bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 prior=json.loads(bind(R/'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json',prep['own_checkpoint_sha256']))
 for p,h in prior['inputs'].items():bind(R/p,h)
 paths={
  'production':'research/scaled_product_norms/code/production.py',
  'packed':'research/scaled_product_norms/code/packed.py',
  'helper':'research/n3_synthetic_field_audit/code/check.py',
  'fields':'research/joint_scaled_factored_weak/code/fields_joint.py',
  'moments':'research/rational_pole_moments/code/moments.py',
  'cartesian':'research/multiscale_generators/code/cartesian.py',
 }
 for name in ['legqs_norms','legqs_e2norms','e2norms','legqs_integrals']:paths[name]=f'research/n3_scaled_norm_audit/source/{name}.py'
 trees={k:ast.parse(bind(R/p).decode()) for k,p in paths.items()};prod=trees['production'];helper=trees['helper']
 accesses=sorted({n.attr for n in ast.walk(prod) if isinstance(n,ast.Attribute) and isinstance(n.value,ast.Name) and n.value.id=='H'})
 checks['only_two_own_helper_attributes']=accesses==['direct_derivative','evaluate']
 selected={n.name:n for n in helper.body if isinstance(n,ast.FunctionDef) and n.name in accesses}
 assert len(selected)==2
 selected_records={}
 for name,node in selected.items():
  names=sorted({n.id for n in ast.walk(node) if isinstance(n,ast.Name)})
  assert not set(names)&{'N','LS','E','eval','exec','getattr','__import__','load','importlib','sys'}
  assert not any(isinstance(n,(ast.Import,ast.ImportFrom)) for n in ast.walk(node))
  selected_records[name]={'source':ast.get_source_segment((R/paths['helper']).read_text(),node),'names':names,'AST_sha256':sha256(ast.dump(node,include_attributes=False).encode()).hexdigest()}
 checks['selected_helper_functions_no_peer_or_dynamic_access']=True
 def loads(tree):
  return [[ast.literal_eval(a) for a in n.args] for n in tree.body if isinstance(n,ast.Assign) for n in [n.value] if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='load']
 ploads=loads(prod);hloads=loads(helper)
 checks['production_explicit_own_paths']=sorted(p for name,p in ploads)==sorted([paths['moments'],paths['helper'],paths['cartesian']]) and all(name!='__main__' for name,p in ploads)
 checks['helper_explicit_own_paths']=sorted(p for name,p in hloads)==sorted([paths['fields'],paths['cartesian'],paths['moments']]) and all(name!='__main__' for name,p in hloads)
 def imports(tree):
  rows=[]
  for n in tree.body:
   if isinstance(n,ast.Import):rows.extend({'module':a.name,'alias':a.asname} for a in n.names)
   elif isinstance(n,ast.ImportFrom):rows.append({'module':n.module,'names':[a.name for a in n.names]})
  return rows
 imports_by_file={k:imports(t) for k,t in trees.items()}
 assert {'module':'legqs_norms','alias':'N'} in imports_by_file['helper']
 assert {'module':'legqs_e2norms','alias':'LS'} in imports_by_file['helper']
 checks['frozen_peer_initialization_is_present']=True
 module_guards={}
 for name in ['helper','legqs_norms','legqs_e2norms','e2norms','legqs_integrals']:
  guards=[ast.unparse(n.test) for n in trees[name].body if isinstance(n,ast.If)]
  assert guards==["__name__ == '__main__'"],(name,guards)
  module_guards[name]=guards
 checks['peer_and_helper_main_blocks_guarded']=True
 precision={}
 for name,tree in trees.items():
  precision[name]=[{'line':n.lineno,'value':ast.unparse(n.value)} for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) and isinstance(t.value,ast.Name) and t.value.id=='ctx' and t.attr=='prec' for t in n.targets)]
 assert precision['production']==[{'line':81,'value':'args.bits'}]
 assert precision['helper'][0]['value']=='1536'
 assert precision['legqs_integrals'][0]['value']=='512'
 assert all(not precision[k] for k in ['packed','fields','moments','cartesian'])
 checks['production_resets_precision_after_imports']=prior['precision_bits']==2048 and prior['point_checks']['minimum_accuracy_bits']>=1931
 pmain=next(n for n in prod.body if isinstance(n,ast.FunctionDef) and n.name=='main')
 calls=[ast.unparse(n.func) for n in ast.walk(pmain) if isinstance(n,ast.Call)]
 assert 'P.J.ScaledRadial' in calls and 'P.residual' in calls and 'P.all_derivatives' in calls
 norm=next(n for n in prod.body if isinstance(n,ast.FunctionDef) and n.name=='integrate_norm')
 assert sum(isinstance(n,ast.Call) and ast.unparse(n.func)=='M.integral' for n in ast.walk(norm))==2
 checks['candidate_assembly_and_integrals_own_modules']=True
 flags={k:prior[k] for k in ['foreign_code_executed','source_copy_only','frozen_peer_modules_imported_for_own_fixture_helpers','peer_field_or_norm_routines_called']}
 assert flags=={'foreign_code_executed':False,'source_copy_only':True,'frozen_peer_modules_imported_for_own_fixture_helpers':True,'peer_field_or_norm_routines_called':False}
 checks['actual_output_flags_bound']=True
 assert all(checks.values()),checks
 for p,h in inputs.items():assert sha256((R/p).read_bytes()).hexdigest()==h,p
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'inputs':inputs,'production_helper_attributes':accesses,'selected_helper_functions':selected_records,'production_explicit_loads':ploads,'helper_explicit_loads':hloads,'module_imports':imports_by_file,'main_guards':module_guards,'precision_assignments':precision,'completed_checkpoint_flags':flags,'verdicts':{'no_peer_initialization':'REFUTED literal reading','no_peer_candidate_field_or_norm_routines':'CONFIRMED by bound explicit source inspection, not runtime instrumentation','executed_original_peer_lane':'No; local frozen source paths only'},'mathematical_status_unchanged':True,'inspected_source_executed_by_this_checker':False}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({'utc':out['utc'],'elapsed_seconds':out['elapsed_seconds'],'checks':len(checks),'bindings':len(inputs),'result_sha256':sha256(p.read_bytes()).hexdigest()}),flush=True)
if __name__=='__main__':main()
