"""Extract and bind the frozen coordinate and array-index conventions."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,sys,importlib
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records={};spec={'cert_forcing.py':{'BiTM':['__init__','from_sigma','from_phi','sup_crude']},'cert_forcing2.py':{'Recentre':['__init__','__call__','many']},'midrad.py':{'MR':['__init__','__getitem__']},'cert_resid.py':{None:['tm_exp']}}
for file,classes in spec.items():
 p=S/file;t=ast.parse(p.read_text());mod=importlib.import_module(p.stem);assert Path(mod.__file__).resolve()==p.resolve()
 for cls,names in classes.items():
  parent=next(n for n in t.body if isinstance(n,ast.ClassDef) and n.name==cls) if cls else t
  for name in names:
   found=[n for n in parent.body if isinstance(n,ast.FunctionDef) and n.name==name];assert len(found)==1;node=found[0];runtime=getattr(getattr(mod,cls),name) if cls else getattr(mod,name)
   assert Path(runtime.__code__.co_filename).resolve()==p.resolve() and runtime.__code__.co_firstlineno in [node.lineno,*[n.lineno for n in node.decorator_list]]
   records[f'{p.stem}.{cls+"." if cls else ""}{name}']={'source':str(p.relative_to(B)),'sha256':sha(p),'lineno':node.lineno,'end_lineno':node.end_lineno,'body':ast.unparse(node),'runtime_binding_checked':True}
gen=B/'research/forcing_series_operands/code/regenerate.py';tree=ast.parse(gen.read_text());assign={};wanted=['theta_c','cc','ss','ta','E1','a_s','a_p','ub','qb','Ucell','Vcell','H','hb','wb','w_up','Qs','Qp']
for node in ast.walk(tree):
 if isinstance(node,ast.Assign):
  ids={n.id for target in node.targets for n in ast.walk(target) if isinstance(n,ast.Name)}
  if ids&set(wanted):assign[f'{node.lineno}:{node.col_offset}']={'lineno':node.lineno,'column':node.col_offset,'body':ast.unparse(node)}
assert any('MR.exact(bs * hb)' in z['body'] for z in assign.values()) and any('REC.many' in z['body'] for z in assign.values()) and any('theta_c' in z['body'] and 'dth' in z['body'] for z in assign.values())
external=Path('numerics/data/cert_green.npz');expected='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1';assert sha(external)==expected
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COORDINATE_CONVENTION_SOURCE_BINDING','functions':records,'generator':{'path':str(gen.relative_to(B)),'sha256':sha(gen),'assignments':assign},'external_dependency':{'path':str(external),'sha256':expected,'bytes':external.stat().st_size,'read_only_not_copied':True},'scope':'Actual unnormalized coordinate conventions and index order; mathematical interpretation explained in BINDING_ADDENDUM. No new proof of generic MR arithmetic.'}
(D/'evidence/conventions.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(records),len(assign))
