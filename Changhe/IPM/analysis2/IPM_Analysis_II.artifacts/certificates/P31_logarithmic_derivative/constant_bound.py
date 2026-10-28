"""Gamma-product constants retaining the full cylinder derivative factor."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,fmpq as Q,ctx
sys.set_int_max_str_digits(0);ctx.prec=384
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
c=Q(4076476460239181,2251799813685248);delta=1-1/c;astar=7*delta/2-2
annp=B/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json';es={int(m):Q(v) for m,v in json.loads(annp.read_text())['leading_sine_coefficients'].items()}
auditp=B/'26_uniform_family_gap/verification/audit_algebra.json';audit=json.loads(auditp.read_text());assert audit['dependencies'][str(annp.relative_to(B))]==sha256(annp.read_bytes()).hexdigest()
rows={}
def bound(K):
 if K in rows:return rows[K][1]
 M=2*K+4;n=12*(M+1)-8;lnD=-arb(2*astar+1).log()/2
 for ell in range(1,13):
  low=max(0,int(((7-ell)*delta/2).ceil()))+int(ell==7)
  b=(ell-7)*delta/2;d=(ell+7)*delta/2-3
  lnD+=arb(M+1+b).lgamma()-arb(low+b).lgamma()+arb(low+d).lgamma()-arb(M+1+d).lgamma()
 D=lnD.exp();Qn=Q(2*n*(n*n+2)+1,3)
 HM=D*(arb.pi()/2*sum((arb(e)**2/(m*m+arb(Qn)) for m,e in es.items()),arb(0))).sqrt()
 NU=(1-arb(34)/2**18)*512*(arb(20)/21).sqrt()*HM;ratio=1572864*NU
 row={'K':K,'n':n,'degree_w':M,'D':D.str(70),'exponential_HS_squared_exact':str(Q(n*(n*n+2),6)),'cylinder_derivative_squared_exact':str(Qn),'Hminus_lower':HM.str(70),'Route_U_N_lower':NU.str(70),'ratio_to_eta':ratio.str(70),'coefficient_slots':6*(60*(K+1)-1770),'excludes_threshold':bool(ratio>1)}
 rows[K]=(row,ratio);print('K',K,'ratio',ratio.str(20),flush=True);return ratio
assert bound(75)>1
lo=75;hi=350
while bound(hi)>1:lo=hi;hi*=2
while hi-lo>1:
 mid=(lo+hi)//2
 if bound(mid)>1:lo=mid
 else:assert bound(mid)<1;hi=mid
assert hi==lo+1 and bound(lo)>1 and bound(hi)<1
for K in [59,100,200,349,350,500,750,1000]:bound(K)
files=[H.parent/'PROOF.md',annp,auditp,B/'30_radial_degree_obstruction/PROOF.md',B/'26_uniform_family_gap/PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'BALL CONSTANTS VERIFIED; independent audit pending','precision_bits':ctx.prec,'last_K_excluded_by_bound':lo,'first_K_not_decided_by_bound':hi,'rows':[rows[k][0] for k in sorted(rows)],'dependencies':{str(p.relative_to(B)):sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('constant_bound.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',lo,hi,out['seconds'])
