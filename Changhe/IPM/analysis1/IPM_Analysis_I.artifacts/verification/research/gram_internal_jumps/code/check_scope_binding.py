from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_internal_jumps';p=D/'sources/src__c2_gram.py';tree=ast.parse(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main'];check(len(main)==1,'top-level main');main=main[0]
cons=[n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=='constraints'];check(len(cons)==1,'directly nested constraints')
check(not any(isinstance(n,(ast.Global,ast.Nonlocal)) for n in ast.walk(main)),'no alternate lexical binding')
ds=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='d' for t in n.targets)];check(len(ds)==1 and ast.dump(ds[0].value)==ast.dump(ast.parse('np.load(raw)',mode='eval').body),'d=np.load(raw)')
locals_cons={n.id for n in ast.walk(cons[0]) if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Store)};check('tmin' not in locals_cons and 't00' not in locals_cons,'closure joins not locally shadowed')
av=[n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=='avec'];check(len(av)==1,'angular helper');expect=ast.parse('''def avec(pairs):
    a = np.zeros(Mang)
    for m, c in pairs: a[m] += c
    return a
''').body[0];check(ast.dump(av[0])==ast.dump(expect),'whole angular helper')
pins={str(x.relative_to(B)):sha(x) for x in [p,Path(__file__),D/'evidence/source_check.json']};out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_LEXICAL_RAW_BINDING_AND_ANGULAR_HELPER','checks':['d=np.load(raw) unique','constraints directly nested in main','no global/nonlocal declarations','join names not local stores in constraints','whole avec AST matches nonzero single-mode construction'],'files':pins};q=D/'evidence/scope_binding.json';check(not q.exists(),'immutable');q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
