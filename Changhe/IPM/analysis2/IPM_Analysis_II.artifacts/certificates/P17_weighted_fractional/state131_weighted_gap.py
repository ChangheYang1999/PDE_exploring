"""Independent point certificate and rigorous lower bound in weighted N_s^w."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,hashlib,time
from flint import arb,ctx
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'source_audit'))
sys.path.insert(0,str(root/'11_residual_norms/verification'))
from field_eval import State
import audit_norms as an
import compact_norms as cn
start=time.monotonic();ctx.prec=768
p=root/'11_residual_norms/verification/state131_polynomials.json'
raw=json.loads(p.read_text());c,A,sha,recordsha=cn.source('state131')
assert sha==raw['canonical_sha256'] and recordsha==raw['source_record_sha256']
D={tuple(map(int,k.split(','))):cn.dec(v) for k,v in raw['polynomials'].items()}
delta=Q(raw['delta']);assert delta==1-1/c
fpolar=an.polar_eval(D,delta,Q(0),Q(1000))[0,0]
state=State(131,768)
for jm,terms in state.groups.items():
 assert [l for l,v in terms]==list(range(len(terms)))
fcart=state.evaluate('0','1000')['residual']
fcart7=an.direct_F(A,c,arb(0),arb(1000))[0,0]
assert all(f.is_finite() and f>arb(1)/8 for f in [fpolar,fcart,fcart7])
assert fpolar.overlaps(fcart) and fpolar.overlaps(fcart7)
assert 1000<4**5
# V077 growth gives |F(0,1000)| < 2^13*4*N(F).
low=Q(1,2**18);s=Q(1,2**104);eta=Q(1,24*2**78)
assert 2**13*4*low==Q(1,8)
ratio=low/eta;assert ratio==24*2**60
q=2/c-1;assert 0<q<Q(1,5)
paths=[p,root/'source_audit/state131_exact.json',root/'source_audit/field_eval.py',
 root/'11_residual_norms/verification/audit_norms.py',root/'11_residual_norms/verification/compact_norms.py',
 root/'02_energy/verification/compact_matrix.py',root/'16_weighted_fractional/PROOF.md']
result={'verdict':'CONFIRMED','utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,
 'point':['0','1000'],'cartesian_order4':fcart.str(100),'cartesian_order7':fcart7.str(100),
 'polar':fpolar.str(100),'canonical_sha256':sha,'source_record_sha256':recordsha,
 'residual_degree':str(q),'s':str(s),'strict_N_lower_bound':str(low),'conditional_eta':str(eta),
 'strict_gap_ratio_lower_bound':str(ratio),'all_inequalities':'strict',
 'scope':'Point and V077 norm lower bound are certified. Eta is the proposed weighted closure threshold; its theorem has a separate audit.',
 'dependencies':{str(x.relative_to(root)):hashlib.sha256(x.read_bytes()).hexdigest() for x in paths},
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
out=root/'16_weighted_fractional/verification/state131_weighted_gap.json'
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
