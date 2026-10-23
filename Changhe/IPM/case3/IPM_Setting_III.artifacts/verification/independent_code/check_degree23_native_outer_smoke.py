"""Run actual native closure record/index code against an actual smoke job."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import ast,json,gzip,hashlib
from flint import fmpq
from exact_degree21 import decode,degree

def main():
 R=Path('research/degree23_grouped_moment_obstruction');V=R/'verification';p=Path('independent_code/check_degree23_closure_native.py');s=p.read_text();checks=[];bound={};stats=Counter();outer_rows=[]
 sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 env={**globals(),**locals()}
 for node in ast.parse(s).body:
  if isinstance(node,ast.FunctionDef)and node.name in ['ck','bind']:exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),env)
 def block(begin,end,indent):
  a=s.index(begin);b=s.index(end,a);return '\n'.join(z[indent:]for z in s[a:b].splitlines())
 init=block(" native_m=bind(V/'native/MANUFACTURES.json')"," index=bind(V/'RECONSTRUCTION_INDEX.json')",1)
 exec(compile(init,str(p)+':native_common','exec'),env)
 cid='1_7_2_1_1';cf=V/'cases'/(cid+'.json.gz');case=json.loads(gzip.decompress(cf.read_bytes()));assert len(case['jobs'])==1
 env.update(cid=cid,cf=cf,case=case)
 records=block("  for j,job in enumerate(case['jobs']):","  records={z['name']",2)
 exec(compile(records,str(p)+':outer_records','exec'),env)
 index=block(" oi=bind(V/'OUTER_NATIVE_INDEX.json')"," ck('reconstruction count index'",1)
 assert index.count("V/'OUTER_NATIVE_INDEX.json'")==1 and index.count("'COMPLETE_REQUIRES_FINAL_COVERAGE_GATE'")==1
 index=index.replace("V/'OUTER_NATIVE_INDEX.json'","V/'OUTER_NATIVE_SMOKE_INDEX.json'").replace("'COMPLETE_REQUIRES_FINAL_COVERAGE_GATE'","'SMOKE_ONLY'")
 exec(compile(index,str(p)+':smoke_index','exec'),env)
 env['ck']('smoke exactly1outer',len(outer_rows)==1 and outer_rows[0]['name']==case['jobs'][0]['name'])
 oi=env['oi'];env['ck']('smoke exact totals',oi['count']==stats['outer_assertions']and oi['samples']==stats['exact_samples'])
 bound[str(p)]=sha(p);bound['independent_code/check_degree23_outer_native.py']=sha('independent_code/check_degree23_outer_native.py');bound[str(R/'NATIVE_PATH_SMOKE_PROOF.md')]=sha(R/'NATIVE_PATH_SMOKE_PROOF.md')
 for path,digest in bound.items():env['ck']('unchanged smoke '+path,sha(path)==digest)
 obj=dict(status='PASS_ACTUAL_NATIVE_RECORD_AND_SMOKE_INDEX',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bound,driver_sha256=sha(__file__),actual_record_block=records,smoke_index_block=index,scope='One actual identity only. Complete82identitygate, all gcd and positivity gates, and final review still pending. No degree23 theorem or primary PDE endpoint.')
 (V/'native/OUTER_SMOKE_CLOSURE.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status'],obj['count'])
if __name__=='__main__':main()
