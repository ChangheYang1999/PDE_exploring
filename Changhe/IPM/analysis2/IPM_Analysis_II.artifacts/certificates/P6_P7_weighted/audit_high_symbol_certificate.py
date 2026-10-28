"""Reconstruct the entire interval proof tree at greater precision."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
import high_symbol_certificate as hc
HERE=Path(__file__).resolve().parent
ctx.prec=384
raw=json.loads((HERE/'state131_high_symbol_polynomials.json').read_text())
s=json.loads((hc.BASE/'source_audit'/'state131_exact.json').read_text())
P={(key.rsplit('_',1)[0],int(key.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for key,vals in raw['polynomials'].items()}
assert raw['input_sha256']==s['canonical_serialization_sha256']
results=[]
for k in (1,2,3):
 file=HERE/(f'state131_high_symbol_k{k}_adaptive'+('_auxiliary' if k==3 else '')+'.json')
 d=json.loads(file.read_text())
 assert d['status']=='COMPLETE' and d['pending']==0 and not d['failed']
 assert d['input_sha256']==raw['input_sha256'] and Q(d['target'])==(Q(-5,4) if k==3 else Q(1,2))
 paths={x['path']:x for x in d['accepted']};assert len(paths)==len(d['accepted'])
 B=hc.load(P,Q(s['exact_parameters']['cl']),Q(d['k']),Q(d['radius']),Q(d['sigma']),Q(d['target']))
 Lt,Rt=hc.cc.split_matrices(hc.cc.NT);Lz,Rz=hc.cc.split_matrices(hc.cc.NZ)
 lows=[]
 def visit(path,b,tl,th,zl,zh):
  if path in paths:
   row=paths[path]
   assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
   assert not any(p!=path and p.startswith(path) for p in paths)
   low=hc.bound(b,tl,th,zl,zh,Q(raw['delta']))
   assert low>=0 and arb(row['lower_numerator_after_target'])>=0
   lows.append(low)
   return 1
  children={p[len(path)] for p in paths if p.startswith(path)}
  assert children in ({'t','T'},{'z','Z'}),(path,children)
  axis='t' if children=={'t','T'} else 'z'
  left,right=hc.cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
  if axis=='t':
   mid=(tl+th)/2
   return visit(path+'t',left,tl,mid,zl,zh)+visit(path+'T',right,mid,th,zl,zh)
  mid=(zl+zh)/2
  return visit(path+'z',left,tl,th,zl,mid)+visit(path+'Z',right,tl,th,mid,zh)
 n=visit('',B,Q(0),Q(1),Q(-1),Q(1));assert n==len(paths)
 worst=lows[0]
 for low in lows:worst=worst.min(low)
 results.append({'k':k,'radius':d['radius'],'sigma':d['sigma'],'target':d['target'],'leaves':n,'minimum_recomputed_numerator':worst.str(50),'certificate_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'coverage':'complete binary partition; every leaf recomputed at384 bits'})
 print(k,n,worst.str(30),flush=True)
(HERE/'high_symbol_certificate_audit.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','source_sha256':s['canonical_serialization_sha256'],'results':results},indent=2)+'\n')
