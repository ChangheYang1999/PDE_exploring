from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast,hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_c2_repair';OLD=B/'research/gram_conforming_repair'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def shape(s):return ast.dump(ast.parse(s,mode='eval').body,include_attributes=False)
pins={};binding=json.loads((D/'evidence/binding.json').read_text())
for n,h in binding['files'].items():check(sha(B/n)==h,'pin '+n);pins[n]=h
primary=json.loads((OLD/'evidence/compute.json').read_text());independent=json.loads((OLD/'evidence/independent.json').read_text());c2=json.loads((D/'evidence/compute.json').read_text());rows=[];checks=0
for a,b,c in zip(primary['records'],independent['records'],c2['records'],strict=True):
 delta=F(a['public']['uniform_single_column_relative_broken_energy_upper']);check(delta==F(b['public']['uniform_single_column_relative_broken_energy_upper']),'both old ceilings identical');check(delta>0,'positive norm ceiling');margins=[]
 for u,v in zip(a['columns'],b['columns'],strict=True):
  check(u['column_index']==v['column_index'],'column agreement')
  for record,method in ((u,'arb512'),(v,'iv120')):
   U=list(map(F,record['U_'+method]));V=list(map(F,record['V_'+method]));check(0<=U[0]<=U[1] and 0<V[0]<=V[1],'positive interval data');gap=delta*delta*V[0]-U[1];check(gap>0,'delta is strictly a norm bound, without taking a numerical square root');margins.append(gap);checks+=1
 delta2=F(c['public']['single_column_relative_broken_norm_error_upper']);xd=F(c['public']['single_column_relative_X_distance_from_C0_upper']);check(xd*(1-delta)>delta+delta2,'norm-level triangle ratio');rows.append({'M':a['M'],'N':a['N'],'old_delta_norm_exact':str(delta),'norm_ratio_inequalities_checked':2*len(a['columns']),'minimum_positive_rational_gap_exact':str(min(margins)),'new_delta_norm_exact':str(delta2),'X_distance_ceiling_exact':str(xd)})
source=OLD/'code/compute.py';tree=ast.parse(source.read_text());assigns={}
for node in ast.walk(tree):
 if isinstance(node,ast.Assign):
  for target in node.targets:
   if isinstance(target,ast.Name):assigns.setdefault(target.id,[]).append(ast.dump(node.value,include_attributes=False))
check(shape('(U/V).sqrt()') in assigns['rat'],'old rat computes norm square root');check(shape('box(rat)') in assigns['rb'],'old rb encloses norm ratio');check(shape('rb[1]') in assigns['maxratio'],'old maximum uses upper norm endpoint')
publics=[node for node in ast.walk(tree) if isinstance(node,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='uniform_single_column_relative_broken_energy_upper' for k in node.keys)];check(len(publics)==1,'unique public field');p=publics[0]
for key,value in zip(p.keys,p.values):
 if isinstance(key,ast.Constant) and key.value=='uniform_single_column_relative_broken_energy_upper':check(ast.dump(value,include_attributes=False)==shape('enc(floorceil(maxratio))'),'field stores strict norm ceiling')
for p in (D/'evidence/binding.json',D/'evidence/compute.json',OLD/'evidence/compute.json',OLD/'evidence/independent.json',OLD/'PROOF.md',OLD/'REVIEW_RESOLUTIONS.md',OLD/'FINAL_ADJUDICATION.md',source,Path(__file__)):pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_C0_FIELD_IS_NORM_RATIO_BY_EXACT_SQUARED_INEQUALITIES_AND_SOURCE_AST','exact_rational_norm_comparisons':checks,'source_AST_bindings':4,'records':rows,'files':dict(sorted(pins.items())),'scope':'Resolves the historical energy field name: the field is a strict square-root norm ratio in every column and both interval methods. No estimate changes.'};p=D/'evidence/norm_semantics.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'checks':checks,'records':[{k:r[k] for k in ('M','N','old_delta_norm_exact','new_delta_norm_exact','X_distance_ceiling_exact')} for r in rows]}))
