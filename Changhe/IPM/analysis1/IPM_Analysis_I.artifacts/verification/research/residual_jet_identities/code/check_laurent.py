"""Every mode pair, exact integer Laurent products versus current AST indices."""
from pathlib import Path
from datetime import datetime,timezone
from types import SimpleNamespace
import ast,hashlib,json,sys,time
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1]
S=B/'research/forcing_v22/source/src/cert_resid.py'
expected='1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(S)==expected
t0=time.monotonic();tree=ast.parse(S.read_text());cls=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name=='Certifier');fn=next(x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name=='__init__')
need=['self.n','nn','jj','self.N1','self.N2','self.S2','self.Nmax'];chosen=[];bindings=[]
for node in fn.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and ast.unparse(node.targets[0]) in need:
  chosen.append(node);bindings.append({'line':node.lineno,'column':node.col_offset,'target':ast.unparse(node.targets[0]),'expression':ast.unparse(node.value)})
assert [b['target'] for b in bindings]==need
obj=SimpleNamespace(M=260,Nf=261)
exec(compile(ast.fix_missing_locations(ast.Module(body=chosen,type_ignores=[])),str(S),'exec'),{'__builtins__':{},'np':np,'self':obj})
assert obj.n.tolist()==list(range(1,262)) and obj.Nmax==522
assert obj.N1.shape==obj.N2.shape==obj.S2.shape==(261,261)
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,0)+v
 return clean(d)
def mul(p,q):
 d={}
 for k,v in p.items():
  for l,w in q.items():d[k+l]=d.get(k+l,0)+v*w
 return clean(d)
def scale(p,v):return clean({k:w*v for k,w in p.items()})
def sn(k):return {} if k==0 else {k:1,-k:-1}
def cs(k):return {0:2} if k==0 else {k:1,-k:1}
# sn(k)=2i*sin(k theta), cs(k)=2*cos(k theta).
# cs(a)*sn(b) corresponds to 2cos(a)sin(b), with common2i removed.
count=0;radchecks=tangchecks=0;maxfreq=0;maxdiff=0;digest=hashlib.sha256();branch={'n_le_j':0,'n_gt_j':0};counts=[0]*523
for ni,n in enumerate(range(1,262)):
 for j in range(261):
  a,b=2*n,2*j+1;N1=int(obj.N1[ni,j]);N2=int(obj.N2[ni,j]);s=int(obj.S2[ni,j]);assert float(obj.S2[ni,j])==s and s in [-1,1]
  p1,p2=2*N1+1,2*N2+1
  radial=mul(cs(a),sn(b));tangent=mul(sn(a),cs(b))
  assert radial==add(sn(p1),scale(sn(p2),s)),(n,j,'radial')
  assert tangent==add(sn(p1),scale(sn(p2),-s)),(n,j,'tangent')
  assert min(N1,N2)>=0 and max(N1,N2)<=521 and p1%2 and p2%2
  assert 0 not in radial and 0 not in tangent
  assert N1==n+j and p2==abs(b-a) and s==(1 if b-a>0 else -1)
  counts[N1]+=1;counts[N2]+=1;count+=1;radchecks+=1;tangchecks+=1;maxfreq=max(maxfreq,p1,p2);maxdiff=max(maxdiff,N2);branch['n_le_j' if n<=j else 'n_gt_j']+=1
  digest.update(f'{n},{j},{N1},{N2},{s};'.encode())
assert count==68121 and maxfreq==1043 and maxdiff==260 and counts[522]==0
# A constant angular mode is impossible in odd/even product parity, not discarded numerically.
# Check every linear-drift placement against the actual source slice endpoints.
core=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_cell_core_deriv')
corebindings=[]
for node in ast.walk(core):
 if isinstance(node,ast.Assign):
  for target in node.targets:
   if ast.unparse(target) in ['em[:self.M + 1]','er[:self.M + 1]','erem[:self.M + 1]']:
    corebindings.append({'line':node.lineno,'target':ast.unparse(target),'expression':ast.unparse(node.value)})
assert {x['target']:x['expression'] for x in corebindings}=={'em[:self.M + 1]':'lin.c.m','er[:self.M + 1]':'lin.c.r','erem[:self.M + 1]':'lin.r'}
assert sha(S)==expected
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_EXACT_LAURENT_ALL_CURRENT_FREQUENCY_PAIRS',M=260,Nf=261,pairs=count,radial_checks=radchecks,tangential_checks=tangchecks,branch_counts=branch,maximum_physical_sine_frequency=maxfreq,maximum_difference_index=maxdiff,allocated_last_index=522,allocated_last_index_count=counts[522],scatter_counts=counts,index_digest=digest.hexdigest(),source_bindings=bindings,linear_placement_bindings=corebindings,source_sha256=expected,code_sha256=sha(Path(__file__)),seconds=time.monotonic()-t0,scope='All exact integer Laurent identities and selected AST index expressions; no floating product/scatter enclosure or physical jet assertion.')
(D/'evidence/laurent.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],count,out['seconds'])
