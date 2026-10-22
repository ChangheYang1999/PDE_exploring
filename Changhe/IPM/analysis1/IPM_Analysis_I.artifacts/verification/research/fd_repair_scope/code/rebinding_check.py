"""Supplementary exhaustive Store/Del check for the frozen row inputs."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/fd_repair_scope'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
p=D/'evidence/c2_gram2_source.py.txt';tree=ast.parse(p.read_text());main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');wr=next(n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=='weighted_rows');rows={}
for name in ['uu','mr','w_i','roww','t_eval','Mout','Ne','Aw_all']:
 stores=[n for n in ast.walk(main) if isinstance(n,ast.Name) and n.id==name and isinstance(n.ctx,(ast.Store,ast.Del))];check(len(stores)==1 and isinstance(stores[0].ctx,ast.Store),'all recursive stores '+name);rows[name]=stores[0].lineno
check(all(rows[n]<wr.lineno<rows['Aw_all'] for n in rows if n!='Aw_all'),'source initialization and use order')
check(not any(isinstance(n,(ast.Global,ast.Nonlocal)) for n in ast.walk(main)),'no dynamic scope rebinding declaration')
check(not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in {'exec','eval'} for n in ast.walk(main)),'no dynamic execution in source main')
prior=json.loads((D/'evidence/source_binding.json').read_text());pins={}
for n,h in prior['files'].items():check(sha(B/n)==h,'prior pin');pins[n]=h
for path in [D/'evidence/source_binding.json',Path(__file__)]:pins[str(path.relative_to(B))]=sha(path)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_RECURSIVE_ROW_INPUT_STORES_AND_EXECUTION_ORDER','source_store_line_numbers':rows,'weighted_rows_definition_line':wr.lineno,'files':pins,'scope':'Frozen source variable binding, not a job execution or physical row certificate.'}
p=D/'evidence/rebinding_check.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','source_store_line_numbers']}))
