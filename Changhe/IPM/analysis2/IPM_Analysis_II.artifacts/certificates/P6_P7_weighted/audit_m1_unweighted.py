from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
import high_symbol_certificate as hc
ctx.prec=384;HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'state131_high_symbol_polynomials.json').read_text());s=json.loads((hc.BASE/'source_audit/state131_exact.json').read_text())
dfile=HERE/'state131_high_symbol_k1_adaptive_unweighted09.json';d=json.loads(dfile.read_text())
assert d['status']=='COMPLETE' and not d['pending'] and not d['failed']
assert d['input_sha256']==raw['input_sha256']==s['canonical_serialization_sha256']
assert Q(d['sigma'])==0 and Q(d['k'])==1 and Q(d['target'])==Q(9,10)
P={(k.rsplit('_',1)[0],int(k.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for k,vals in raw['polynomials'].items()}
B=hc.load(P,Q(s['exact_parameters']['cl']),Q(1),Q(1),Q(0),Q(9,10));Lt,Rt=hc.cc.split_matrices(hc.cc.NT);Lz,Rz=hc.cc.split_matrices(hc.cc.NZ)
paths={v['path']:v for v in d['accepted']};assert len(paths)==len(d['accepted']);lows=[]
def visit(path,b,tl,th,zl,zh):
 if path in paths:
  row=paths[path];assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
  assert not any(p!=path and p.startswith(path) for p in paths)
  lo=hc.bound(b,tl,th,zl,zh,Q(raw['delta']));assert lo.is_finite() and lo>=0;lows.append(lo);return 1
 kids={p[len(path)] for p in paths if p.startswith(path)};assert kids in ({'t','T'},{'z','Z'})
 ax='t' if kids=={'t','T'} else 'z';left,right=hc.cc.split(b,ax,Lt if ax=='t' else Lz,Rt if ax=='t' else Rz)
 if ax=='t':
  m=(tl+th)/2;return visit(path+'t',left,tl,m,zl,zh)+visit(path+'T',right,m,th,zl,zh)
 m=(zl+zh)/2;return visit(path+'z',left,tl,th,zl,m)+visit(path+'Z',right,tl,th,m,zh)
n=visit('',B,Q(0),Q(1),Q(-1),Q(1));assert n==len(paths)
worst=lows[0]
for v in lows:worst=worst.min(v)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','target':'9/10','precision_bits':ctx.prec,'leaves':n,'minimum_numerator_after_target':worst.str(55),'certificate_sha256':hashlib.sha256(dfile.read_bytes()).hexdigest(),'source_sha256':s['canonical_serialization_sha256']}
(HERE/'unweighted_M1_09_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
