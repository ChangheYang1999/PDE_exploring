"""Re-run only the geometry, comparing2-vs17 batches on all actual operands."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,sys,time,hashlib,struct
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S));tic=time.monotonic()
from midrad import MR
from cert_forcing import BiTM
from cert_forcing2 import Recentre
original=Recentre.many;counts={'batches':0,'retained_arrays_compared':0,'retained_array_entries_compared':0,'scalar_remainders_compared':0}
def bits_equal(a,b):return a.shape==b.shape and np.array_equal(a.view(np.uint64),b.view(np.uint64))
def wrapped(self,fs,a_s,a_p,newcell):
 assert len(fs)==2;shape=fs[0].c.m.shape;assert shape==fs[1].c.m.shape==(13,9)
 two=original(self,fs,a_s,a_p,newcell);dummy=[]
 for k in range(15):
  mm=np.fromfunction(lambda i,j:((-1.0)**(i+j+k))*(1+i+2*j+k)*2.0**(-20-k),shape);rr=np.full(shape,2.0**(-50-k));dummy.append(BiTM(MR(mm,rr),2.0**(-80-k),fs[0].cell))
 many=original(self,dummy+fs,a_s,a_p,newcell)[-2:]
 for a,b in zip(two,many):
  for x,y in [(a.c.m,b.c.m),(a.c.r,b.c.r)]:assert bits_equal(x,y);counts['retained_arrays_compared']+=1;counts['retained_array_entries_compared']+=x.size
  assert struct.pack('d',a.r)==struct.pack('d',b.r);counts['scalar_remainders_compared']+=1
 counts['batches']+=1
 return two
# Execute the unchanged frozen replay algorithm with only its three output paths
# redirected, leaving every already-pinned evidence file intact.
p=D/'code/regenerate.py';text=p.read_text();tree=ast.parse(text);mapping={f'evidence/{s}':f'evidence/batch_replay/{s}' for s in ['operands.npz','blocks.json','regeneration.json']}
class Outputs(ast.NodeTransformer):
 def visit_Constant(self,node):
  if isinstance(node.value,str) and node.value in mapping:return ast.copy_location(ast.Constant(mapping[node.value]),node)
  return node
tree=Outputs().visit(tree);ast.fix_missing_locations(tree);(D/'evidence/batch_replay').mkdir(exist_ok=True);Recentre.many=wrapped
try:exec(compile(tree,str(p),'exec'),{'__file__':str(p),'__name__':'geometry_batch_audit'})
finally:Recentre.many=original
fresh=D/'evidence/batch_replay';assert json.loads((fresh/'blocks.json').read_text())==json.loads((D/'evidence/blocks.json').read_text())
with np.load(fresh/'operands.npz',allow_pickle=False) as x,np.load(D/'evidence/operands.npz',allow_pickle=False) as y:
 assert x.files==y.files
 for k in x.files:assert bits_equal(x[k],y[k]),k
assert counts=={'batches':832,'retained_arrays_compared':3328,'retained_array_entries_compared':389376,'scalar_remainders_compared':1664}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_FULL_GEOMETRIC_BATCH_AND_OPERAND_BIT_REPLAY','counts':counts,'replay_source_sha256':sha(p),'redirected_outputs':mapping,'fresh_regeneration_sha256':sha(fresh/'regeneration.json'),'original_operands_sha256':sha(D/'evidence/operands.npz'),'fresh_operands_sha256':sha(fresh/'operands.npz'),'scope':'All actual two-entry geometry batches compared with15arbitrary finite dummy entries prepended. Structural per-entry argument is separate; no actual17entry residual array or historical run is authenticated.'}
(D/'evidence/batch.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],counts,flush=True)
