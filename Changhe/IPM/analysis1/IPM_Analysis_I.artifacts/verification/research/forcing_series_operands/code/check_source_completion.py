"""Complete the transitive elementwise-body extraction requested by Opus."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,json,hashlib,sys,math
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S))
import midrad
from cert_forcing2 import Recentre
sources={k:(S/k).read_text() for k in ['midrad.py','cert_forcing.py','cert_forcing2.py']};trees={k:ast.parse(v) for k,v in sources.items()}
mt=trees['midrad.py'];succ=next(n for n in mt.body if isinstance(n,ast.FunctionDef) and n.name=='succ');assert ast.unparse(succ)=='def succ(x):\n    return np.nextafter(x, INF)'
constants={}
for name in ['U','ETA','BETA','INF']:
 n=next(n for n in mt.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets));v=getattr(midrad,name);assert np.isscalar(v)
 constants[name]={'expression':ast.unparse(n.value),'type':type(v).__name__,'exact':str(Q.from_float(float(v))) if math.isfinite(v) else 'positive infinity'}
assert midrad.U==2.0**-53 and midrad.ETA==2.0**-1074 and np.isposinf(midrad.INF)
assert Q.from_float(float(midrad.BETA))>=Q(1,2**53-1)
ft=trees['cert_forcing.py'];bitm=next(n for n in ft.body if isinstance(n,ast.ClassDef) and n.name=='BiTM');bi=next(n for n in bitm.body if isinstance(n,ast.FunctionDef) and n.name=='__init__');assert ast.unparse(bi)=='def __init__(self, c, r, cell):\n    self.c = c\n    self.r = float(r)\n    self.cell = cell'
ct=trees['cert_forcing2.py'];rec=next(n for n in ct.body if isinstance(n,ast.ClassDef) and n.name=='Recentre');ri=next(n for n in rec.body if isinstance(n,ast.FunctionDef) and n.name=='__init__');r=Recentre(12,8);checks=0
for a,n in [(r.cs,13),(r.cp,9)]:
 assert a.shape==(n,n)
 for i in range(n):
  for j in range(n):assert Q.from_float(float(a[i,j]))==(math.comb(i,j) if i>=j else 0);checks+=1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_ELEMENTWISE_PATH_EXTRACTION','succ_body':ast.unparse(succ),'constants':constants,'BiTM_init_body':ast.unparse(bi),'Recentre_init_body':ast.unparse(ri),'binomial_entries_exact':checks,'source_sha256':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in sources.items()},'scope':'Discharges the specific missing-body and scalar-constant obligations in the second Opus review. Full source-path and historical execution still excluded.'}
(D/'evidence/source_completion.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks)
