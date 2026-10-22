"""Complete branch/function AST specification, no execution of teammate code."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/fd_repair_scope'
def check(v,t):
 if not v:raise ValueError(t)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p):return ast.dump(p,include_attributes=False)
spec='''def weighted_rows(Xu):
    quad = ROWS.endswith("q")
    if quad:
        om = np.zeros(Ne); dtv = np.diff(t_eval); om[:-1] += 0.5 * dtv; om[1:] += 0.5 * dtv
        sq_om = np.sqrt(om); sq_dt = np.sqrt(dtv)
    else: sq_om = np.ones(Ne); sq_dt = np.ones(Ne - 1)
    if ROWS in ("L2", "L2q"): return Xu * (roww * np.repeat(sq_om, Mout))[:, None]
    X3 = Xu.reshape(Ne, Mout, -1); nc = X3.shape[2]
    ang = np.sqrt(1.0 + (2 * np.arange(Mout) + 1.0) ** 2)
    val = (X3 * ((w_i * sq_om)[:, None, None] * ang[None, :, None])).reshape(Ne * Mout, nc)
    dt = np.diff(t_eval); wm = 0.5 * (w_i[1:] + w_i[:-1])
    der = ((X3[1:] - X3[:-1]) * (wm * sq_dt / dt)[:, None, None]).reshape((Ne - 1) * Mout, nc)
    return np.vstack([val, der])
'''
p=D/'evidence/c2_gram2_source.py.txt';tree=ast.parse(p.read_text());main=next(a for a in tree.body if isinstance(a,ast.FunctionDef) and a.name=='main');wr=next(a for a in main.body if isinstance(a,ast.FunctionDef) and a.name=='weighted_rows');check(isinstance(wr.body[0],ast.Expr) and isinstance(wr.body[0].value,ast.Constant) and isinstance(wr.body[0].value.value,str),'single leading docstring');wr.body=wr.body[1:];ref=ast.parse(spec).body[0];check(dump(wr)==dump(ref),'complete weighted_rows AST')
expect={'uu':'np.exp(t_eval)/L','mr':'uu**3*(1+uu**2)**((k-3)/2)','w_i':'(1+uu)**0.5/mr','roww':'np.repeat((1+uu)**0.5/mr,Mout)','t_eval':'d["t_eval"]','Mout':'int(d["Mout"])','Ne':'int(d["Ne"])','Aw_all':'weighted_rows(np.column_stack([Mat,KP,TAU,tails]))'}
for name,expression in expect.items():
 assignments=[node for node in main.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in node.targets)]
 check(len(assignments)==1 and dump(assignments[0].value)==dump(ast.parse(expression,mode='eval').body),'unique direct binding '+name)
 if name!='Aw_all':check(main.body.index(assignments[0])<main.body.index(wr),'binding before weighted_rows '+name)
# Only explicitly listed ROWS inputs are assigned the meanings in this theorem.
check('ROWS = \'H1\'' in ast.get_docstring(next(a for a in ast.walk(ast.parse(p.read_text())) if isinstance(a,ast.FunctionDef) and a.name=='weighted_rows')),'source declared image interpretation')
prior=json.loads((D/'evidence/independent.json').read_text());pins={}
for n,h in prior['files'].items():check(sha(B/n)==h,'prior pin');pins[n]=h
for path in [D/'evidence/independent.json',D/'ADDENDUM.md',Path(__file__)]:pins[str(path.relative_to(B))]=sha(path)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_ROW_FUNCTION_AST_AND_EIGHT_DIRECT_BINDINGS','complete_function_ast_sha256':hashlib.sha256(dump(ref).encode()).hexdigest(),'specification':spec,'direct_bindings':expect,'files':pins,'scope':'Current frozen source as an array transformation only. Physical contents of raw arrays and historical job execution OPEN.'}
op=D/'evidence/source_binding.json';check(not op.exists(),'immutable');op.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','complete_function_ast_sha256']}))
