from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime,timezone
from collections import Counter
import json,time
start=time.monotonic();base=Path(__file__).resolve().parents[1]
source=base/'source/candidate010.json';manifest_path=base/'source/MANIFEST.json'
d=json.loads(source.read_text());manifest=json.loads(manifest_path.read_text())
assert sha256(source.read_bytes()).hexdigest()==manifest['coefficient_files'][0]['sha256']
c=Fraction(str(d.get('cl_exact',d.get('cl'))));assert c==Fraction(manifest['c_l_exact']) and 1<c<2
kinds=Counter();multi=[]
for g in d['generators']:
 assert isinstance(g['m'],int) and g['m']>=0 and isinstance(g['j'],int) and g['j']>=0
 assert 'p' not in g
 spec=g['spec'];kind=spec[0];kinds[kind]+=1
 assert kind in ('mono','leg','legqs')
 if kind=='mono':assert isinstance(spec[1],int) and spec[1]>=0
 elif kind=='leg':assert all(isinstance(x,int) and x>=0 for x in spec[1:]) and len(spec)==3
 else:
  assert len(spec)==5
  w,n,Q,R=spec[1:];assert all(isinstance(x,int) and x>=0 for x in (w,n,Q))
  assert Q==4 and Fraction(str(R)) in (10,100)
  multi.append((g['j'],g['m'],w,n,Q,str(R)))
assert len(multi)==960 and len(d['generators'])==3942
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':manifest['id'],'all_checks_pass':True,'c':str(c),'counts':dict(kinds),'multiscale_parameters':{name:sorted(set(row[k] for row in multi)) for k,name in enumerate(('j','m','w','n','Q','R'))},'input_sha256':{str(p.relative_to(base)):sha256(p.read_bytes()).hexdigest() for p in (source,manifest_path,base/'source/ipm_exact.py',base/'PROOF.md',Path(__file__))},'elapsed_seconds':time.monotonic()-start}
target=base/'verification/metadata.json';assert not target.exists();target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'},indent=2))
