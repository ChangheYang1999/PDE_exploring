"""Exact endpoint comparison of the frozen family; no quadrature."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import comb
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
sys.set_int_max_str_digits(0)
b=Path(__file__).resolve().parents[1];s=b/'source';start=time.monotonic()
hashof=lambda p:sha256(p.read_bytes()).hexdigest()
manifest=json.loads((s/'MANIFEST.json').read_text())
for name,rec in manifest.items():assert hashof(s/name)==rec['sha256']
c=Q(4076476460239181,2251799813685248);d=3+1/c
records=[];reference=None
for name,rec in manifest.items():
 if rec['kind']=='manifest':continue
 raw=json.loads((s/name).read_text());assert Q(raw.get('cl',raw.get('cl_exact')))==c
 amp=defaultdict(Q);counts=defaultdict(int)
 if rec['kind']=='canonical':
  for (j,m,k),cf in zip(raw['order'],raw['coefficients']):
   if int(j)==0:amp[int(m)]+=Q(cf)
  counts['canonical_terms']=len(raw['coefficients'])
 else:
  ss=json.loads((s/(rec['snapshot']+'_MANIFEST.json')).read_text())
  matches=[x for x in ss['coefficient_files'] if x['name']==Path(rec['path']).name]
  assert len(matches)==1 and matches[0]['sha256']==rec['sha256']
  for g in raw['generators']:
   j=int(g['j']);m=int(g['m']);spec=g['spec'];typ=spec[0];counts[typ]+=1
   assert j>=0 and m>=0
   if typ=='mono':
    assert int(spec[1])>=0;endpoint=Q(1)
   elif typ=='leg':
    w,n=map(int,spec[1:]);assert w>=0 and n>=0
    endpoint=Q(sum((-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)));assert endpoint==1
   elif typ=='legqs':
    w,n,q=map(int,spec[1:4]);R=Q(spec[4]);assert w>=0 and n>=0 and q==4 and R>0
    endpoint=Q(0)
   else:raise AssertionError(typ)
   if j==0:amp[m]+=Q(g['coef'])*endpoint
 amp={m:v for m,v in sorted(amp.items()) if v}
 if reference is None:reference=amp
 b1=-amp.get(0,Q(0))*d*d*(d-2)+amp.get(1,Q(0))*(d*d-4)*d/2
 assert amp==reference and 18<b1<19
 records.append({'candidate':name.removesuffix('.json'),'source_sha256':rec['sha256'],'format':rec['kind'],'counts':dict(counts),'leading_potential_amplitudes':{str(m):str(v) for m,v in amp.items()},'identical_to_state131':True,'first_density_harmonic':str(b1),'strict_lower':'18','strict_upper':'19','float_diagnostic':float(b1)})
assert len(records)==10
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'c':str(c),'gamma':str(1/c),'records':records,'proof_sha256':hashof(b/'PROOF.md'),'code_sha256':hashof(Path(__file__)),'manifest_sha256':hashof(s/'MANIFEST.json'),'status':'All exact leading profiles agree; OPEN numerical-lane independent reproduction of this family table.'}
with (b/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
for rec in records:print(rec['candidate'],rec['identical_to_state131'],rec['float_diagnostic'],rec['counts'])
