"""Check actual dependency-return keys and prepare's AST path lists before freeze.
Does not execute prepare or claim primary completion. Reads only local inputs.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import ast,json,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
import check_cells,cell_iv,audit_full
assert not sys.flags.optimize
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_second/evidence';PE=BASE/'research/middle_residual/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
 driver=BASE/'research/middle_second/code/run_full.py';tree=ast.parse(driver.read_text());prepare=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='prepare')
 tag='full_q16';k,L,knots,pub,kp=check_cells.inputs();samples,audits,pointpins=check_cells.point_dependencies()
 env={'BASE':BASE,'E':E,'PE':PE,'Path':Path,'__file__':str(driver),'cell_iv':cell_iv,'check_cells':check_cells,'kp':kp,'pa':PE/(tag+'_output_audit.json'),'pp':PE/(tag+'_cells.jsonl'),'ps':PE/(tag+'_summary.json'),'ka':PE/'knot_audit.json','manifest':PE/'knot_manifest.json','partition':PE/'partition_exact.json'}
 actual={}
 for name in ['sourcepaths','evidence']:
  node=next(n for n in prepare.body if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id==name)
  actual[name]=eval(compile(ast.Expression(node.value),str(driver),'eval'),{'__builtins__':{}},env)
 names={str(p.relative_to(BASE)) for p in actual['sourcepaths']+actual['evidence']}|set(pointpins)
 # These additions match the two explicit loops in the reviewed source. Their
 # literal paths and evidence.extend statement are checked in the AST itself.
 additions=next(n for n in prepare.body if isinstance(n,ast.For) and ast.unparse(n.target)=='(key, path)')
 for key,path in ast.literal_eval(additions.iter):names.add(path)
 regionloop=next(n for n in prepare.body if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple) and len(n.target.elts)==4)
 assert any(isinstance(n,ast.Expr) and ast.unparse(n.value)=='evidence.extend([vp, mp, cp])' for n in regionloop.body)
 for region in ['inner','outer']:
  names.update(['research/'+region+'_cells/evidence/verdict.json','research/'+region+'_cells/evidence/full_q16_manifest.json','research/'+region+'_majorant/evidence/exact_'+region+'_coefficients.json'])
 required=audit_full.required_pins(tag);assert required<=names
 assert sorted(samples)==[0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808]
 files=[Path(__file__),driver,Path(cell_iv.__file__),Path(check_cells.__file__),Path(audit_full.__file__)]
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PREFREEZE_DEPENDENCY_KEY_CHECK','method':'Evaluated actual prepare AST sourcepaths/evidence lists, actual inputs and point_dependencies, and literal primary source loop. Region additions are separately checked against their reviewed AST statement. No fake primary output or completion is supplied.','required':sorted(required),'provided':sorted(names),'missing':sorted(required-names),'point_dependency_keys':sorted(pointpins),'canonical_archive_key':str(kp.relative_to(BASE)),'pins':{str(p.relative_to(BASE)):sha(p) for p in files},'scope':'Cheap pre-freeze key check only. prepare execution still requires actual completed primary output and audit.'}
 tmp=E/'prefreeze_keys.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'prefreeze_keys.json');print(json.dumps({k:v for k,v in result.items() if k not in ['required','provided']}))
if __name__=='__main__':main()
