"""Finite interval regression and ratio/root scope audit, with centered replay."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from flint import arb,fmpz,ctx
ROOT=Path('research/300_half_ratio_diagnostics')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def txt(v):return v.str(35,radius=True)
def unpack(v):
 m,e,r,re=v
 return arb(arb(fmpz(m))*arb(2)**e,arb(fmpz(r))*arb(2)**re)
def fit(points):
 N=arb(len(points));xb=sum((x for x,y in points),arb(0))/N;yb=sum((y for x,y in points),arb(0))/N
 den=sum(((x-xb)**2 for x,y in points),arb(0));assert den>0
 B=sum(((x-xb)*(y-yb) for x,y in points),arb(0))/den;L=yb-B*xb;assert L>0
 rms=(sum(((y-L-B*x)**2 for x,y in points),arb(0))/N).sqrt()
 return dict(L=L,B=B,a=-B/L,rms=rms)
def calculate(c,bits):
 ctx.prec=bits;ns={r['n']:unpack(r['fields']['f']['norm']) for r in c['rows']};ln10=arb(10).log()
 ratios={n:ns[n]/ns[n-1] for n in range(2,301)}
 f=fit([(arb(1)/n,ratios[n]) for n in range(200,301)])
 steps=[(ratios[n].log()/ln10) for n in range(271,301)]
 avg=sum(steps,arb(0))/30;mini=min(steps,key=lambda v:float(v.mid()));maxi=max(steps,key=lambda v:float(v.mid()))
 assert all(mini<v for v in steps if v is not mini)
 assert all(maxi>v for v in steps if v is not maxi)
 # Exact product identity, evaluated with dependency overestimation.
 residual=(ns[300].log()-ns[1].log()-sum((v.log() for v in ratios.values()),arb(0)))/300
 assert residual.contains(0)
 root=ns[300].root(300);prediction=f['L']*(1-f['a']/300)
 assert prediction>root
 return f,dict(mean_step=avg,minimum_step=mini,maximum_step=maxi,root300=root,ratio300=ratios[300],fitted_ratio300=prediction,root_minus_fitted_ratio=root-prediction,product_log_residual=residual)
start=time.monotonic();source=Path('research/291_canonical_half_finite/verification/checks.json');c=json.loads(source.read_bytes());assert c['all_checks_pass'] and c['maximum_order']==300
f,a=calculate(c,768);fr,ar=calculate(c,1536)
assert all(f[k].overlaps(fr[k]) for k in f)
assert all(a[k].overlaps(ar[k]) for k in a)
printed=[('L','0.38386','0.00001'),('a','1.84','0.01'),('rms','0.0007','0.0001')]
rounding=[]
for key,value,unit in printed:
 v=arb(value);h=arb(unit)/2;ok=bool(fr[key]>v-h and fr[key]<v+h)
 rounding.append(dict(statistic=key,printed=value,rounding_unit=unit,enclosed=txt(fr[key]),within_rounding_bin=ok))
maxima=[]
for field in ('f','g'):
 rows=[r for r in c['rows'] if 'nonconstant_factorial_maximizer' in r['fields'][field]]
 maxima.append(dict(field=field,first_order=rows[0]['n'],last_order=rows[-1]['n'],order_count=len(rows),maximizers=sorted({r['fields'][field]['nonconstant_factorial_maximizer'] for r in rows}),all_strict=all(r['fields'][field]['maximum_strictly_certified'] for r in rows),all_below_constant=all(r['fields'][field]['nonconstant_below_constant'] for r in rows)))
source_report=ROOT/'sources/producer_experiments.md';text=source_report.read_text()
assert 'M_n^(1/n) = 0.3716 follows the smooth law L(1 - 1.84/n)' in text
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source=ref(source),source_report=ref(source_report),bits=768,replay_bits=1536,fit_window=[200,300],fit_count=101,fit={k:txt(v) for k,v in fr.items()},increment_window=[271,300],statistics={k:txt(v) for k,v in ar.items()},printed_comparisons=rounding,nonconstant_column_checks=maxima,all_replays_overlap=True,root_is_strictly_smaller_than_fitted_ratio=True,all_printed_fit_bins_pass=all(r['within_rounding_bin'] for r in rounding),scope='Finite interval diagnostics under topic291 input enclosure hypothesis. Report root-law clause has a ratio/root substitution; no infinite limit follows.',actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/half_ratio_diagnostics.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(out,indent=2))
