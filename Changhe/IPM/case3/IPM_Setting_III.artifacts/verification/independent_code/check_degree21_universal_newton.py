from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import fmpz_mpoly_ctx
import exact_degree21 as q
from exact_polynomial_275 import P,F
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];cert=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError(n)
q.C=fmpz_mpoly_ctx.get(tuple('c'+str(i)for i in range(1,9)),ordering='lex');var=q.C.gens();pv=[P.var(i,8)for i in range(8)];zero=P(dim=8);one=zero+1;K=9
for L in range(1,9):
 co=[q.Q(1)]+[q.Q(v)for v in var[:L]];native=q.ps(co,K);other=q.logps(co,K);C=[one]+pv[:L];sp=[zero+L]
 for k in range(1,K+1):
  z=-sum((C[j]*sp[k-j]for j in range(1,min(k,L+1))),zero)
  if k<=L:z-=k*C[k]
  sp.append(z)
 aa=[zero]+pv[:L];power=[one];logs=[zero for _ in range(K+1)]
 for ell in range(1,K+1):
  out=[zero for _ in range(K+1)]
  for i,a in enumerate(power):
   for j,b in enumerate(aa):
    if i+j<=K:out[i+j]+=a*b
  power=out
  for k in range(1,K+1):logs[k]+=power[k]*F((-1)**(ell+1),ell)
 for k in range(K+1):
  ck('native universal Lk'+str((L,k)),native[k]==other[k]);ck('purePython universal Lk'+str((L,k)),sp[k]==(zero+L if k==0 else -k*logs[k]))
  ck('native denominator constant Lk'+str((L,k)),native[k].d.total_degree()==0)
  den=int(native[k].d.leading_coefficient());terms={tuple(map(int,p)):F(int(v),den)for p,v in native[k].n.terms()};ck('cross-library all coefficients Lk'+str((L,k)),terms==sp[k].a)
  cert.append(dict(L=L,k=k,terms=[[list(p),str(v)]for p,v in sorted(terms.items())]))
out=dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,certificates=cert,library_sha256=sha('independent_code/exact_degree21.py'),other_library_sha256=sha('independent_code/exact_polynomial_275.py'),driver_sha256=sha(__file__),proof_sha256=sha(R/'NEWTON_UNIVERSAL_PROOF.md'));(V/'UNIVERSAL_NEWTON.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks))
