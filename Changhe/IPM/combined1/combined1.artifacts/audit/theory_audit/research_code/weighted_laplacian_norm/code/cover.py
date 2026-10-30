from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
start=time.monotonic();ctx.prec=1024
src=ROOT/'verification/d2_2048.json';d=json.loads(src.read_text());c=Q(d['c']);A=1+1/c
assert c>Q(4,3) and A<Q(7,4)
norms={Q(r['a']):arb(r['weighted_laplacian_norm']) for r in d['weights']}
rows=[]
for j in range(7):
 l,h=Q(j,4),Q(j+1,4)
 N=norms[h] if j<6 else norms[Q(3,2)]**2/norms[Q(5,4)]
 lower=arb(5)**ar((l-2)/2)*N
 upper=(8*arb.pi()).sqrt()*ar((1+c-c*l)**2/(1+l))
 gap=lower-upper;ratio=lower/upper
 assert gap>0 and ratio>1
 rows.append({'left':str(l),'right':str(h),'restricted_to_a_less_than':str(A),'norm_method':'direct right endpoint' if j<6 else 'Cauchy-Schwarz at 5/4,3/2,7/4','Y_lower_bound':lower.str(95),'ceiling_upper_bound':upper.str(95),'gap':gap.str(95),'ratio':ratio.str(95)})
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(src),'code_sha256':sha(__file__),'proof_sha256':sha(ROOT/'UNIFORM_COVER.md'),'precision_bits':ctx.prec,'candidate':'d2','all_seven_cells_pass':True,'cells':rows,'minimum_ratio_lower':min(arb(r['ratio']).lower() for r in rows).str(90),'minimum_gap_lower':min(arb(r['gap']).lower() for r in rows).str(90),'elapsed_seconds':time.monotonic()-start,'scope':'Conditional exclusion of the specified dyadic closure scheme; independent analytic and numerical review still required.'}
(ROOT/'verification/d2_cover.json').write_text(json.dumps(out,indent=2)+'\n')
print('All 7 cells pass; minimum ratio',out['minimum_ratio_lower'],'seconds',out['elapsed_seconds'],flush=True)
