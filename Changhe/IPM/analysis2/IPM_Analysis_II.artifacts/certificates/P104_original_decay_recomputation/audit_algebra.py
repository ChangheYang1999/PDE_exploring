"""Independent original third-derivative reconstruction and source bindings."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import json,sys,time
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(root/'research/02_energy/verification'))
from compact_matrix import derivative,add
@lru_cache(None)
def angular(n,typ):
 P={}
 for b in range(0 if typ=='c' else 1,n+1,2):
  j=b//2;h=(n-b-1)//2 if typ=='c' else (n-b)//2;v=F((-1)**j*comb(n,b),2**(h+j))
  for x in range(h+1):
   for y in range(j+1):P[x+y]=P.get(x+y,F(0))+v*comb(h,x)*comb(j,y)*(-1)**y
 return {k:v for k,v in P.items() if v}
start=time.monotonic();src=root/'research/source_audit/state131_exact.json';s=json.loads(src.read_text());p=here/'polynomials.json';d=json.loads(p.read_text());oldpath=root/'research/96_original_auxiliary_recomputation/verification/polynomials.json';old=json.loads(oldpath.read_text());assert d['source_sha256']==old['source_sha256']==sha256(src.read_bytes()).hexdigest();assert d['fourth_polynomials_sha256']==sha256(oldpath.read_bytes()).hexdigest();assert d['canonical_sha256']==s['canonical_serialization_sha256'];assert all(d['polynomials'][k]==v for k,v in old['polynomials'].items());c=F(s['exact_parameters']['cl']);delta=1-1/c;checks=0
for label,axes,sign,typ in [('u1','xyy',-1,'c'),('u2','xxy',1,'s')]:
 for j in range(4):
  trig={};exponent=(3+1/c-j*delta)/2
  for (jj,m,k),a in zip(s['canonical_order'],s['canonical_coefficients']):
   if jj!=j:continue
   D={('c',2*m,0):F(a)}
   for order,axis in enumerate(axes):D=derivative(D,exponent,k,order,axis)
   for (kind,n,l),v in D.items():add(trig,kind,n,k-2+l,sign*v)
  P={}
  for (kind,n,i),v in trig.items():
   assert kind==typ and n%2 and i>=0;checks+=1
   for k,a in angular(n,kind).items():P[i,k]=P.get((i,k),F(0))+v*a
  P={k:v for k,v in P.items() if v};assert P=={(i,k):F(v) for i,k,v in d['polynomials'][f'{label}_{j}']};checks+=len(P)+1
assert F(2,5)<delta<1;record={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'checks':checks,'polynomials_sha256':sha256(p.read_bytes()).hexdigest(),'source_sha256':sha256(src.read_bytes()).hexdigest(),'fourth_polynomials_sha256':sha256(oldpath.read_bytes()).hexdigest(),'seconds':time.monotonic()-start};(here/'algebra.json').write_text(json.dumps(record,indent=2)+'\n');print(record['utc'],checks,'PASS',record['seconds'],flush=True)
