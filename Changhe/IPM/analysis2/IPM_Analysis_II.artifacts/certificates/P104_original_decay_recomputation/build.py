"""Exact original third derivatives, combined with audited fourth derivatives."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(root/'research/95_refit_global_hypotheses/verification'))
from build import deriv,clean
from build_derivatives import odd_factor
start=time.monotonic();source=root/'research/source_audit/state131_exact.json';raw=json.loads(source.read_text());base=root/'research/96_original_auxiliary_recomputation/verification/polynomials.json';d=json.loads(base.read_text());assert d['source_sha256']==sha256(source.read_bytes()).hexdigest();assert d['source_canonical_sha256']==raw['canonical_serialization_sha256']
c=Q(raw['exact_parameters']['cl']);delta=1-1/c;coeff={tuple(k):Q(v) for k,v in zip(raw['canonical_order'],raw['canonical_coefficients'])};out=dict(d['polynomials'])
for label,axes,sign in [('u1','xyy',-1),('u2','xxy',1)]:
 for j in range(4):
  p=(3+1/c-j*delta)/2;D={('c',2*m,k):v for (jj,m,k),v in coeff.items() if jj==j}
  for order,axis in enumerate(axes):D=deriv(D,p,order,axis)
  P={}
  for (kind,n,k),v in D.items():
   assert n%2 and k>=2 and kind==('c' if label=='u1' else 's')
   for z,a in odd_factor(n,kind).items():P[k-2,z]=P.get((k-2,z),Q(0))+sign*v*a
  out[f'{label}_{j}']=[[i,k,str(v)] for (i,k),v in sorted(clean(P).items())]
for label in ['chi22','chi04','chi31','chi13','e','u1','u2']:
 for j in [4,5]:out[f'{label}_{j}']=[]
record={'utc':datetime.now(timezone.utc).isoformat(),'cl':str(c),'delta':str(delta),'polynomials':out,'source_sha256':sha256(source.read_bytes()).hexdigest(),'canonical_sha256':raw['canonical_serialization_sha256'],'fourth_polynomials_sha256':sha256(base.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
(here/'polynomials.json').write_text(json.dumps(record,indent=2)+'\n');print(record['utc'],'BUILT',record['seconds'],flush=True)
