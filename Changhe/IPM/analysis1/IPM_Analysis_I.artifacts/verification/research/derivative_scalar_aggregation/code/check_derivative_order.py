from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,ast,collections,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_scalar_aggregation'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
base=json.loads((D/'evidence/coverage.json').read_text());pins=dict(base['files'])
for n,h in pins.items():assert sha(B/n)==h
source=(D/'sources/src__cert_resid.py').read_text();tree=ast.parse(source);fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_cell_core_deriv')
loops=[x for x in fn.body if isinstance(x,ast.For) and ast.unparse(x.target)=='i' and ast.unparse(x.iter)=='range(nder + 1)']
outer=next(x for x in loops if any(isinstance(z,ast.For) and ast.unparse(z.target)=='j' for z in x.body))
inner=next(x for x in outer.body if isinstance(x,ast.For) and ast.unparse(x.target)=='j')
assert ast.unparse(inner.iter)=='range(nder + 1 - i)'
assign=inner.body[0];assert isinstance(assign,ast.Assign)
assert ast.unparse(assign.targets[0])=="out['W_%d_%d' % (i, j)]"
assert isinstance(assign.value,ast.IfExp) and ast.unparse(assign.value.test)=='j <= 2' and ast.unparse(assign.value.body)=='float(Wb[j])'
assert ast.unparse(outer.body[0])=='tot = eps[i]'
assert ast.unparse(outer.body[1])=='supN, Wb0, Wb1, Wb2 = self.bernstein_sup_sub(tot, hpow, h_up, K=4)'
assert ast.unparse(outer.body[3])=='Wb = [Wb0, Wb1, Wb2]'
regions={};fields=0
expected={'middle':{2:7432,5:377},'inner':{2:2632},'outer':{2:8948}}
for region,name in [('middle','runs__cert_deriv_middle.json'),('inner','runs__cert_deriv_regions_inner.json'),('outer','runs__cert_deriv_regions_outer.json')]:
 rows=json.loads((D/'sources'/name).read_text())['rows'];counts=collections.Counter(r['nder'] for r in rows);assert dict(counts)==expected[region]
 for r in rows:
  pairs={(i,j) for i in range(r['nder']+1) for j in range(r['nder']+1-i)}
  assert {(2,0),(1,1),(0,2)}<=pairs
  for i,j in pairs:
   key='W_%d_%d'%(i,j);assert key in r and F.from_float(r[key])>=0;fields+=1
  assert all(F.from_float(r[k])>0 for k in ['W_2_0','W_1_1','W_0_2'])
 regions[region]={'rows':len(rows),'nder_counts':dict(counts),'positive_second_order_fields':3*len(rows)}
for p in [D/'REVIEW_RESOLUTIONS.md',D/'evidence/coverage.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ORDER_LABELS_AND_ALL_SAVED_DERIVATIVE_FIELDS_PHYSICAL_OPEN','regions':regions,'all_order_indexed_fields':fields,'source_loop_ast_sha256':hashlib.sha256(ast.dump(outer,include_attributes=False).encode()).hexdigest(),'files':dict(sorted(pins.items())),'scope':'Source field creation and finite saved-field presence and positivity only; physical derivative majorants remain open.'}
with (D/'evidence/derivative_order.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','regions','all_order_indexed_fields']}))
