"""Read-only source binding and AST comparison for actual N3 norm production."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import ast,json,difflib,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_scaled_norm_peer';C=R/'research/n3_scaled_norm_audit/source'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ast_parts(path):
 t=ast.parse(path.read_text());out={}
 for node in t.body:
  if isinstance(node,(ast.FunctionDef,ast.ClassDef)):
   out[node.name]=node
   if isinstance(node,ast.ClassDef):
    for f in node.body:
     if isinstance(f,ast.FunctionDef):out[node.name+'.'+f.name]=f
 return out
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,actual,h);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 manifest=read(B/'source/MANIFEST_v01.json')
 for name,v in manifest['files'].items():bind(B/'source'/name,v['sha256'])
 peer=read(B/'source/N3_norms_partial_v01.json')
 for name,h in peer['code_sha256'].items():bind(B/'source'/name,h)
 checks['four_actual_production_hashes']=len(peer['code_sha256'])==4
 for name in ['legqs_e2norms.py','legqs_integrals.py','e2norms.py']:
  bind(C/name);checks['identical_'+name]=sha(C/name)==sha(B/'source'/name)
 old=bind(B/'source/legqs_norms.py');new=bind(C/'legqs_norms.py');op=ast_parts(old);np=ast_parts(new)
 unchanged=['fq2arb','add_t','plus_t','to_tuple','from_plain','to_plain','merge_scales','canon_t','equal_t','diff_t','fields_t','residual_t','ScaleTables.__init__','ScaleTables.entry','ScaleTables.pack','ScaleTables.beta_column','ScaleTables.pf','_lcm','Accumulator.__init__','Accumulator.add','Accumulator.is_rational','save_F','load_F','run']
 for name in unchanged:checks['unchanged_'+name]=ast.dump(op[name],include_attributes=False)==ast.dump(np[name],include_attributes=False)
 changed=['ScaleTables.I0','Accumulator.value','normsq_t','norm_t','pair_t']
 for name in changed:checks['changed_'+name]=ast.dump(op[name],include_attributes=False)!=ast.dump(np[name],include_attributes=False)
 got=''.join(difflib.unified_diff(new.read_text().splitlines(True),old.read_text().splitlines(True),fromfile=str(new.relative_to(R)),tofile=str(old.relative_to(R))))
 stored=bind(B/'verification/legqs_norms.py.calibration_to_production.diff');checks['complete_diff_bound']=stored.read_text()==got
 assert "key = (Q(a), Q(b0))" in ast.get_source_segment(old.read_text(),op['ScaleTables.I0'])
 assert "assert b > -1" in ast.get_source_segment(old.read_text(),op['Accumulator.add'])
 checks['admissible_exponent_guard_already_present']=True
 checks['fixed1024_record']=peer['precision_bits']==1024 and all(row['precision_bits']==1024 for row in peer['norms'].values())
 checks['raw_identity']=peer['source_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 checks['actual_first_three_norms_complete']=set(peer['norms'])=={'G0','rF','G1'} and all(row['status']=='FINITE' for row in peer['norms'].values())
 checks['P2_absent']=peer['status']=='RUNNING' and 'P2' not in peer['norms']
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 bind(B/'PROOF.md');bind(Path(__file__))
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'unchanged_AST_functions':unchanged,'changed_AST_functions':changed,'calibration_repairs_used':'Production already guards b>-1 and uses no quadrature. N4-302 replaces inadmissible calibration inputs; N4-305 and308 validate independent exact fields. No repaired quadrature is used in production.','old_accumulator_scope':'Every R1 conversion and class addition is outward, although not every cross-class cancellation is exact.','old_cache_scope':'Key omits precision, but the recorded run uses1024 throughout its shared cache.','elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED actual production source identity and limited changes; actual norm numbers remain OPEN until independent production comparison'}
 dest=B/'verification/source_audit.json'
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',len(checks),'checks',len(inputs),'bindings',sha(dest),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
