"""Extract the actual source parameter, branch, imports, and reviewed bodies."""
from pathlib import Path
from datetime import datetime,timezone
import ast,copy,json,hashlib,sys,importlib
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S));src=(S/'cert_forcing2.py').read_text();tree=ast.parse(src);main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');mod=importlib.import_module('cert_forcing2');assert Path(mod.__file__).resolve()==(S/'cert_forcing2.py').resolve()
args=[a.arg for a in main.args.args];defaults=dict(zip(args[-len(main.args.defaults):],main.args.defaults));K=ast.literal_eval(defaults['Kser']);assert K==16
branches=[n.test for n in ast.walk(main) if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and ast.unparse(n.test.left)=='xr'];assert len(branches)==1
branch=branches[0];assert isinstance(branch.ops[0],ast.Lt) and len(branch.comparators)==1 and ast.literal_eval(branch.comparators[0])==0.6
compiled=compile(ast.Expression(body=copy.deepcopy(branch)),'source_active_comparison','eval');rows=json.loads((D/'evidence/blocks.json').read_text())
for r in rows:assert bool(eval(compiled,dict(vars(mod),xr=r['xr'])))==r['active']
raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());assert raw['Kser']==K and raw['Qs']==12 and raw['Qp']==8 and raw['ntheta']==16 and raw['nbs']==raw['nbp']==2
bindings={}
for name,module in [('comb','math'),('arb','flint'),('MR','midrad'),('succ','midrad'),('U','midrad')]:
 found=[n for n in tree.body if isinstance(n,ast.ImportFrom) and n.module==module and any(a.name==name and a.asname in [None,name] for a in n.names)];assert len(found)==1,(name,module)
 actual=getattr(mod,name);expected=getattr(importlib.import_module(module),name);assert actual is expected or (name=='U' and actual==expected)
 bindings[name]={'import':ast.unparse(found[0]),'resolved_module':module,'identity_checked':True}
rec=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='Recentre');many=next(n for n in rec.body if isinstance(n,ast.FunctionDef) and n.name=='many');mr=(S/'midrad.py').read_text();mt=ast.parse(mr);mc=next(n for n in mt.body if isinstance(n,ast.ClassDef) and n.name=='MR');needed=['__init__','exact','__getitem__','__add__','__mul__'];bodies={n.name:ast.unparse(n) for n in mc.body if isinstance(n,ast.FunctionDef) and n.name in needed};assert len(bodies)==5
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SOURCE_PARAMETERS_BRANCH_IMPORTS_AND_BODY_EXTRACTION','Kser_default':K,'active_condition':ast.unparse(branch),'active_comparisons':len(rows),'import_bindings':bindings,'Recentre_many_body':ast.unparse(many),'MR_bodies':bodies,'source_sha256':hashlib.sha256(src.encode()).hexdigest(),'midrad_sha256':hashlib.sha256(mr.encode()).hexdigest(),'scope':'Exact source objects and extracted bodies for the explicit per-entry argument in SOURCE_ADDENDUM; no generic mathematical proof inferred from a whitelist.'}
(D/'evidence/parameters.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(rows),K)
