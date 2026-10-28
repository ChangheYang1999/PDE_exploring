"""Exact finite exponents and ball arithmetic for the radial-degree obstruction."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,ctx,fmpq
sys.set_int_max_str_digits(0);ctx.prec=384
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
c=Q(4076476460239181,2251799813685248);delta=1-1/c;astar=7*delta/2-2
aq=lambda x:arb(fmpq(str(x)))
auditp=B/'26_uniform_family_gap/verification/audit_algebra.json';audit=json.loads(auditp.read_text())
annp=B/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json'
assert audit['dependencies'][str(annp.relative_to(B))]==sha256(annp.read_bytes()).hexdigest()
es={int(m):Q(v) for m,v in json.loads(annp.read_text())['leading_sine_coefficients'].items()}
rows={}
def bound(K):
 if K in rows:return rows[K][1]
 exps=sorted({ell*delta/2+k-2 for ell in range(1,13) for k in range(2*K+5) if ell*delta/2+k-2>=astar})
 assert exps[0]==astar and len(exps)==12*(2*K+5)-8
 S=sum((2*x+1 for x in exps),Q(0));D=1/aq(2*astar+1).sqrt()
 for x in exps[1:]:D*=aq(x-astar)/aq(x+astar+1)
 C=(4*aq(S)**2/arb.pi()**2+arb(1)/4).sqrt()
 Cf=(sum((aq(x*x) for x in exps),arb(0))+(aq(S)**2-sum((aq((2*x+1)**2) for x in exps),arb(0)))/2).sqrt()
 Hminus=D*(arb.pi()/2*sum((aq(e*e)/(m*m+(1+2*C)**2) for m,e in es.items()),arb(0))).sqrt()
 N=(1-arb(34)/2**18)*512*(arb(20)/21).sqrt()*Hminus;ratio=N*1572864
 assert C<Cf
 row={'K':K,'relaxed_residual_degree':2*K+4,'exponent_count':len(exps),'S_exact':str(S),'D':D.str(70),'C_Volterra':C.str(70),'C_Frobenius':Cf.str(70),'Hminus_lower':Hminus.str(70),'Route_U_N_lower':N.str(70),'ratio_to_eta':ratio.str(70),'coefficient_slots':6*(60*(K+1)-1770),'excludes_current_threshold':bool(ratio>1)}
 rows[K]=(row,ratio)
 print('K',K,'ratio',ratio.str(18),flush=True)
 return ratio
assert bound(59)>1
lo=59;hi=75
while bound(hi)>1:lo=hi;hi*=2
assert bound(hi)<1
while hi-lo>1:
 mid=(lo+hi)//2
 if bound(mid)>1:lo=mid
 else:assert bound(mid)<1;hi=mid
assert bound(lo)>1 and bound(hi)<1 and hi==lo+1
for K in [75,100,150,200,250,300,400]:bound(K)
files=[H.parent/'PROOF.md',auditp,annp,B/'26_uniform_family_gap/PROOF.md',B/'11_residual_norms/PROOF.md',B/'09_quasilinear/PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED constants with independent gamma-ratio audit','precision_bits':ctx.prec,'last_K_excluded_by_bound':lo,'next_K_not_decided_by_bound':hi,'all_rows':[rows[k][0] for k in sorted(rows)],'dependencies':{str(p.relative_to(B)):sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('degree_bound.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',lo,hi,out['seconds'],flush=True)
