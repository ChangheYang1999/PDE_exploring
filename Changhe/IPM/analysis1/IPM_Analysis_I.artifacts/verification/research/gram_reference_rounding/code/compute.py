from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from types import SimpleNamespace
import ast,hashlib,json,math
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_rounding'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
def load(p):return json.loads(p.read_text())
pins={}
for n in ['research/gram_internal_jumps/evidence/verdict.json','research/gram_conformity/evidence/verdict.json']:
 v=load(B/n);pins[n]=sha(B/n)
 for p,h in v['files'].items():check(sha(B/p)==h,'prior pin');pins[p]=h
s=load(D/'sources/scalars.json');src=D/'sources/c2_gram2.py';check(sha(src)==s['source_sha256'],'source');tree=ast.parse(src.read_text());fn=next(q for q in tree.body if isinstance(q,ast.FunctionDef) and q.name=='step_pieces');cc=next(q for q in tree.body if isinstance(q,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='STEP_COEF' for t in q.targets));coef=ast.literal_eval(cc.value)
expected=ast.parse("""def step_pieces(ta,tb):
 w=float(tb-ta)
 return [(-np.inf,float(ta),0.0,[1.0]),(float(ta),float(tb),0.0,[c/w**j for j,c in enumerate(STEP_COEF)])]
""").body[0]
check(ast.dump(fn.args)==ast.dump(expected.args) and [ast.dump(x) for x in fn.body[1:]]==[ast.dump(x) for x in expected.body] and not fn.decorator_list and fn.returns is None,'complete step body')
refs=[q for q in ast.walk(tree) if isinstance(q,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='REFS' for t in q.targets)];check(len(refs)==1 and ast.dump(refs[0].value)==ast.dump(ast.parse("[('ref_J',t00-1.0,t00),('ref_Jin',tmin-1.0,tmin),('ref_wide',tmin,t00)]",mode='eval').body),'complete REFS')
env={'np':SimpleNamespace(inf=math.inf),'STEP_COEF':coef};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(src),'exec'),env)
vals={}
for r in s['scalars']:
 check(sha(B/r['copy'])==r['sha256']==pins[r['copy']],'scalar pin');vals[r['member']]=float.fromhex(r['hex']);check(F(vals[r['member']])==F(r['exact_value']),'scalar exact')
tmin,t0=vals['tmin.npy'],vals['t0.npy'];rows=[]
def horner(c,x):
 z=F(0)
 for a in reversed(c):z=z*x+a
 return z
for name,a,b in [('ref_J',t0-1.0,t0),('ref_Jin',tmin-1.0,tmin),('ref_wide',tmin,t0)]:
 pieces=env['step_pieces'](a,b);aa,bb,alpha,c=pieces[1];check(alpha==0.0 and len(c)==10,'returned polynomial');q=[F(v) for v in c];l=[];r=[]
 for j in range(5):
  l.append(str(horner(q,F(0))-(1 if j==0 else 0)));r.append(str(horner(q,F(bb)-F(aa))));q=[(i+1)*q[i+1] for i in range(len(q)-1)]
 rows.append({'name':name,'a_hex':aa.hex(),'b_hex':bb.hex(),'w_hex':float(bb-aa).hex(),'coefficients_hex':[v.hex() for v in c],'lower_jump_derivatives_exact':l,'upper_trace_derivatives_exact':r,'value_continuous':F(l[0])==F(r[0])==0,'C4':all(F(v)==0 for v in l+r),'upper_value_float_orientation':float(F(r[0]))})
q=list(map(F,coef));ideal=[]
for j in range(5):ideal.append([str(horner(q,F(0))-(1 if j==0 else 0)),str(horner(q,F(1)))]);q=[(i+1)*q[i+1] for i in range(len(q)-1)]
check(all(F(x)==0 for row in ideal for x in row),'ideal C4')
for p in [D/'PROOF.md',D/'evidence/proof_first.json',src,D/'sources/scalars.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FROZEN_STEP_REPRODUCTION_AND_EXACT_ENDPOINT_AUDIT','records':rows,'ideal_C4_residuals':ideal,'files':pins,'scope':'Current isolated source reproduction for pinned M24 scalars; no future or historical matrix output authenticated.'}
with (D/'evidence/compute.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'records':[{k:r[k] for k in ['name','value_continuous','C4','upper_value_float_orientation']} for r in rows]}))
