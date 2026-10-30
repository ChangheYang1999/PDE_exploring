from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,time
from flint import arb,ctx
ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def A(x):
    x=Q(x);return arb(x.numerator)/x.denominator
start=time.monotonic();source=ROOT/'verification/tail_results.json';tail=json.loads(source.read_text())
J=13;test=next(r for r in tail['tail_tests'] if r['J']==J);assert test['below_half'];assert arb(test['relative_remainder_upper'])<arb(1)/2
c=Q(tail['c']);delta=Q(tail['delta']);b=Q(tail['b']);E=Q(tail['angular_squared_norms_over_pi']['0']);K=(1-arb(2)**A(2*b-2))/A(2-2*b)
N=256;rows=[];ratios=[];margins=[]
for j in range(N):
    lo=Q(j,N);hi=Q(j+1,N)
    left=A(E/4)*K*A(1+2/c+delta*lo)**2
    right=8*A((c-1)**4*(1-lo)**4)*(1-arb(2)**A(-2*delta*hi))*arb(2)**A(2*J*delta*hi)
    gap=left-right;assert gap>0,(j,gap)
    ratio=left/right;assert ratio>1
    rows.append({'left':str(lo),'right':str(hi),'LHS_lower_ball':left.str(70),'RHS_upper_ball':right.str(70),'positive_gap_ball':gap.str(70),'squared_ratio_lower_ball':ratio.str(70)})
    margins.append(gap.lower());ratios.append(ratio.lower())
result={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(source),'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(__file__),'precision_bits':ctx.prec,'J':J,'epsilon':'1/2','cover_cells':N,'x_interval':['0','1'],'a_interval':[str(2/c),str(1+1/c)],'minimum_gap_lower_bound':min(margins).str(80),'minimum_squared_ratio_lower_bound':min(ratios).str(80),'cells':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/cover_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('certified_cells',N,'min_positive_gap',result['minimum_gap_lower_bound'],'min_squared_ratio',result['minimum_squared_ratio_lower_bound'],'elapsed',result['elapsed_seconds'])
