"""Bind original-coordinate saved-vector source path by AST, without executing it."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
def dump(x):return ast.dump(x,include_attributes=False)
def expr(s):return ast.parse(s,mode='eval').body
m=json.loads((D/'data_exact/manifest.json').read_text());pins=dict(m['files'])
for n,h in pins.items():need(sha(B/n)==h,'inherited source digest')
p=B/'notes/constraint_rank_watch/c2_gram2.py';s=p.read_text();need(sha(p)=='958a27152449e90e2fd1723bf90a7e479181d913d6edccb7ad3cc48146e7d085','frozen source anchor');tree=ast.parse(s);nodes=list(ast.walk(tree));records=[]
loops=[n for n in nodes if isinstance(n,ast.For) and dump(n.target)==dump(ast.parse('name,sel',mode='eval').body).replace('Load()','Store()') and dump(n.iter)==dump(expr('section_list'))];need(len(loops)==1,'unique saved section loop');loop=loops[0];inside=list(ast.walk(loop))
expected={'Ds':'Ds=D[sel]','Q':'Q=(N @ QN)*Ds[:,None]','small':'small=np.arange(len(S_)-min(5,len(S_)),len(S_))','H':'H=np.column_stack([extend(Vt[i]) for i in small])'}
for name,text in expected.items():
 hits=[n for n in nodes if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)];need(len(hits)==1 and dump(hits[0])==dump(ast.parse(text).body[0]) and hits[0] in inside,'unique loop assignment '+name);records.append((name,hits[0]))
exp='''def extend(v):
 h=np.zeros(next_)
 h[sel]=Q @ v
 return h'''
hits=[n for n in nodes if isinstance(n,ast.FunctionDef) and n.name=='extend'];need(len(hits)==1 and hits[0] in inside and dump(hits[0])==dump(ast.parse(exp).body[0]),'complete coordinate extension');records.append(('extend',hits[0]))
exp=ast.parse('vec_out[name+"_h"]=H[:,::-1].copy()').body[0];hits=[n for n in nodes if isinstance(n,ast.Assign) and dump(n)==dump(exp)];need(len(hits)==1 and hits[0] in inside,'saved coefficients order');records.append(('saved_h',hits[0]))
sel=[n for n in nodes if isinstance(n,ast.Tuple) and len(n.elts)==2 and isinstance(n.elts[0],ast.Constant) and n.elts[0].value=='Fminus'];need(len(sel)==1 and dump(sel[0])==dump(expr('("Fminus",list(range(nF+2)))')),'Fminus original-coordinate selection');records.append(('Fminus',sel[0]))
saves=[n for n in nodes if isinstance(n,ast.Call) and dump(n.func)==dump(expr('np.savez_compressed'))];need(len(saves)==1,'one vector export');save=saves[0];kw={n.arg:n.value for n in save.keywords};need(len(kw)==len(save.keywords),'unique keyword keys')
for key,text in [('col_m','col_m'),('col_label','col_label'),('nF','nF'),('Mh','Mh'),('NJ','NJ'),('ROWS','ROWS'),('ntot','ntot'),('next','next_'),('tmin','tmin'),('t0','t00'),(None,'vec_out')]:need(key in kw and dump(kw[key])==dump(expr(text)),'vector export field '+str(key))
need(dump(kw['script_sha256'])==dump(expr('__import__("hashlib").sha256(open(os.path.abspath(__file__),"rb").read()).hexdigest()')),'metadata source hash expression');records.append(('savez',save))
need(sel[0].lineno<loop.lineno<save.lineno,'coordinate selection, loop and export order')
spans=[]
for name,n in records:
 p=D/'sources'/('vector_'+name+'.txt')
 with p.open('x') as f:f.write(ast.get_source_segment(s,n)+'\n')
 pins[str(p.relative_to(B))]=sha(p);spans.append({'name':name,'line':n.lineno,'end_line':n.end_lineno,'path':str(p.relative_to(B)),'sha256':sha(p)})
for p in [D/'data_exact/manifest.json',D/'ADDENDUM.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final source pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STATIC_ORIGINAL_COORDINATE_VECTOR_SOURCE_PATH','records':spans,'assignments':4,'complete_extend_functions':1,'export_fields':12,'files':dict(sorted(pins.items())),'scope':'The inspected source constructs original-coordinate h via Q=(N@QN)*Ds and extends into the saved full coordinate order. Static binding and metadata agree; no external execution attestation, SVD accuracy or physical-component trace assertion.'}
with (D/'evidence/source_binding.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','assignments','complete_extend_functions','export_fields']}))
