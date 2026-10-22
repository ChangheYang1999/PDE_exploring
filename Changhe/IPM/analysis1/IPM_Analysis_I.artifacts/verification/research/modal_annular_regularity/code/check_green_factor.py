"""Independent Poisson coefficient identity after detecting a draft prefactor error."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
from flint import fmpq as Q,ctx
assert not sys.flags.optimize
ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/modal_annular_regularity';E=D/'evidence'
now=lambda:datetime.now(timezone.utc).isoformat()
start=now();count=0;dig=hashlib.sha256()
for n in range(1,262):
 m=2*n
 # State coordinates: I,J,A,B,A',B'. Derivative of a linear state form.
 def deriv(v):return [-(m+4)*v[0],(m-4)*v[1],v[0],-v[1],v[2],v[3]]
 y=[-F(1,2),F(1,2),F(0),F(0),F(0),F(0)];d=deriv(y);dd=deriv(d)
 lhs=[-(dd[j]+8*d[j]+(16-m*m)*y[j]) for j in range(6)]
 # Angular differentiation, computed independently from l=m-1 and l=m+1.
 lower=m-1;higher=m+1
 rhs=[Q(0),Q(0),Q(3-lower,2),Q(3+higher,2),Q(1,2),Q(1,2)]
 # Factored (D+4+m)(D+4-m), after using both first-order ODEs.
 factor=[Q(0),Q(0),Q(4-m,2),Q(4+m,2),Q(1,2),Q(1,2)]
 for j,(a,b,c) in enumerate(zip(lhs,rhs,factor)):
  assert Q(a.numerator,a.denominator)==b==c,(n,j)
  dig.update(f'{n}:{j}:{a}\n'.encode());count+=1
 if n in [2,135]:assert any(Q((z/F(n)).numerator,(z/F(n)).denominator)!=q for z,q in zip(lhs,rhs))
files={}
for p in [D/'PROOF.md',D/'GREEN_FACTOR_CORRECTION.md',Path(__file__),B/'research/full_green_linkage/PROOF.md']:
 files[str(p.relative_to(B))]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'start_utc':start,'utc':now(),'status':'PASS_CORRECTED_CANONICAL_GREEN_PREFACTOR','modes':261,'coefficient_comparisons':count,'wrong_prefactor_rejected_at_n':[2,135],'comparison_stream_sha256':dig.hexdigest(),'scope':'Exact Poisson algebra only; regularity proof must use corrected r^4/2 prefactor. No numerical moment membership.','files':files}
with (E/'green_factor_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='files'}))
