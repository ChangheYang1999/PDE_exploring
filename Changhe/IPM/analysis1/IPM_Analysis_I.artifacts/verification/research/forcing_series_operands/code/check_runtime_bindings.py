"""Discharge the final explicitly requested AST/runtime binding obligations."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys,inspect,marshal
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S))
import midrad,cert_forcing,cert_forcing2
assert midrad.np is np and cert_forcing2.BiTM is cert_forcing.BiTM
sources={k:(S/k).read_text() for k in ['midrad.py','cert_forcing.py','cert_forcing2.py']};trees={k:ast.parse(v) for k,v in sources.items()}
items=[('midrad.py',None,'succ',midrad.succ),('cert_forcing.py','BiTM','__init__',cert_forcing.BiTM.__init__),('cert_forcing2.py','Recentre','__init__',cert_forcing2.Recentre.__init__),('cert_forcing2.py','Recentre','many',cert_forcing2.Recentre.many)]
items += [('midrad.py','MR',name,getattr(midrad.MR,name)) for name in ['__init__','exact','__getitem__','__add__','__mul__']]
records=[]
for file,cls,name,fun in items:
 body=trees[file].body
 if cls:
  nodes=[n for n in body if isinstance(n,ast.ClassDef) and n.name==cls];assert len(nodes)==1;body=nodes[0].body
 nodes=[n for n in body if isinstance(n,ast.FunctionDef) and n.name==name];assert len(nodes)==1,(file,cls,name)
 node=nodes[0];line=min([node.lineno]+[n.lineno for n in node.decorator_list]);assert fun.__code__.co_firstlineno==line and Path(fun.__code__.co_filename).resolve()==(S/file).resolve()
 # A simple rebinding in the same lexical scope is also rejected.
 for n in body:
  if isinstance(n,(ast.Assign,ast.AnnAssign,ast.AugAssign)):
   targets=n.targets if isinstance(n,ast.Assign) else [n.target]
   assert not any(isinstance(t,ast.Name) and t.id==name for target in targets for t in ast.walk(target))
  if isinstance(n,(ast.Import,ast.ImportFrom)):assert not any((a.asname or a.name.split('.')[0])==name for a in n.names)
 assert inspect.getmodule(fun).__file__==str(S/file)
 records.append({'module':file,'class':cls,'name':name,'ast_definition_line':node.lineno,'runtime_first_line':line,'runtime_code_sha256':hashlib.sha256(marshal.dumps(fun.__code__)).hexdigest()})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINAL_RUNTIME_SOURCE_BINDINGS','functions':records,'midrad_np_is_numpy':True,'forcing2_BiTM_is_forcing_BiTM':True,'source_sha256':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in sources.items()},'scope':'The exact missing binding checks requested in the third actual Opus review. No full software-stack or historical execution certification.'}
(D/'evidence/runtime_bindings.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(records))
