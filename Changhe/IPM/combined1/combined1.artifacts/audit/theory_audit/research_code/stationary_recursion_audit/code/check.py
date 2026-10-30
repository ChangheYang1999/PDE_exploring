from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import json,time,math
from flint import fmpq as Q,arb,ctx
start=time.monotonic();ctx.prec=512
base=Path(__file__).resolve().parents[1]
def digest(p):return sha256((base/p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
p,q=4076476460239181,2251799813685248;c=Q(p,q);d=p-q;delta=1-1/c
assert d%2==1 and math.gcd(d,p)==1
summary=json.loads((base/'source/N4_summary.json').read_text())
assert summary['coefficient_equalities']==3060 and len(summary['norm_checks'])==13
assert all(r['exponent'] and r['potential'] and r['density'] for r in summary['checks'])
assert all(r['exact_energy_match'] and r['exponent_match'] for r in summary['norm_checks'])
count=0;rows=[]
for j in range(17):
 s=4-(j+1)*delta;assert s.denominator!=1
 pivots=[]
 for n in range(0,20*(j+1),2):
  pivot=-s*s*(s-2) if n==0 else -(s*s-n*n)*(s-2-n)/2
  assert pivot!=0;pivots.append(abs(pivot));count+=1
 rows.append({'order':j,'s':str(s),'dimension':len(pivots),'smallest_pivot':ar(min(pivots)).str(70)})
assert count==1530
s=4-9*delta;amplification=(1+ar((s-2)**2)/4).sqrt()/abs(ar(s))
selected=json.loads((base/'data/order8_selected.json').read_text());assert Q(selected['cl'])==c
C={int(n):Q(v) for n,v in selected['potential_cos'].items()}
a=-s*s*(s-2)*C[0];b=s*(s*s-4)*C[2]/2
assert a+b==Q(selected['density_sin1'])
x=s*(s-2)*C[0]/2;y=-(s+4)*(s+2)*C[4]/4
out={'utc':datetime.now(timezone.utc).isoformat(),'all_1530_pivots_nonzero':True,'pivots':rows,'order8':{'s':str(s),'pure_mode_velocity_amplification':amplification.str(90),'density_C0_contribution':ar(a).str(90),'density_C2_contribution':ar(b).str(90),'density_sum_matches_exactly':True,'stream_C0_contribution':ar(x).str(90),'stream_C4_contribution':ar(y).str(90),'stream_mode2_sum':ar(x+y).str(90)},'hashes':{v:digest(v) for v in ['PROOF.md','code/check.py','source/N4_summary.json','data/order8_selected.json']},'elapsed_seconds':time.monotonic()-start}
target=base/'verification/results.json';assert not target.exists();target.write_text(json.dumps(out,indent=2)+'\n')
print('all1530 pivots nonzero; s8',ar(s).str(30),'amplification',amplification.str(30));print('order8 stream terms',ar(x).str(25),ar(y).str(25));print('seconds',out['elapsed_seconds'])
