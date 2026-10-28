"""Independent exact coverage and 90-decimal endpoint audit for D_.3."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import mpmath as mp
from finite_projection_extended_diagnostic import evaluate
ctx.prec=256;mp.mp.dps=90
ROOT=Path(__file__).resolve().parents[1]
name='data/finite_D_lower_a30_geometric_fine.json';final=json.loads((ROOT/name).read_text())
for p,h in final['input_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
parts=[(p,json.loads((ROOT/p).read_text())) for p in final['input_hashes'] if p.startswith('data/finite_geometric_chunks/')]
parts.sort(key=lambda item:item[1]['row_start'])
def ep(text,upper):
    b=arb(text);q=(b.upper() if upper else b.lower()).fmpq()
    return mp.mpf(str(q.numerator))/mp.mpf(str(q.denominator))
a=mp.mpf(3)/10;delta=mp.mpf(3)/56;L=mp.mpf(8191)/2
A=mp.gamma((a+2)/2)/(2*mp.sqrt(mp.pi)*mp.gamma((a+3)/2))
terms=dict(local_leading=2*A*delta**a/a,local_loss=2*a*delta/(mp.pi*(1-2*delta))+2*(1+delta)*delta**(a+3)/((1-delta)**4*(a+3)),tail_error=2**a*L**(a-1)/((1-a)*(1-1/(4*L*L))**2))
regular_lo=mp.mpf(0);regular_hi=mp.mpf(0);at=0
for p,raw in parts:
    assert raw['row_start']==at;at=raw['row_stop']
    for source,h in raw['source_hashes'].items():assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==h
    for key,v in terms.items():assert ep(raw[key],False)<v<ep(raw[key],True)
    regular_lo+=ep(raw['regular_interval'],False);regular_hi+=ep(raw['regular_interval'],True)
assert at==6144
value=(regular_lo+terms['local_leading']-terms['local_loss']-terms['tail_error']+mp.mpf('.5'))/mp.mpf('1.007')
assert mp.mpf(final['safe_D_lower'])<=value
regular=evaluate(.3,1.5,nr=480,nt=600)['regular'];assert float(regular_lo)<regular<float(regular_hi)
cname='data/local_circle_composite_a30.json';upper=json.loads((ROOT/cname).read_text())['rows'][0]['safe_upper_C']
gap=mp.mpf(final['safe_D_lower'])-mp.mpf(upper);assert gap>0
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),independent_lower_endpoint=mp.nstr(value,80),regular_lower=mp.nstr(regular_lo,80),regular_upper=mp.nstr(regular_hi,80),regular_gauss=regular,D_lower=final['safe_D_lower'],C_upper=upper,certified_gap=mp.nstr(gap,60),input_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [name,cname,'code/check_finite_D_geometric.py']},status='Exact coverage, source hashes, independent analytic endpoint recomputation and quadrature consistency passed')
(ROOT/'data/finite_D_geometric_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
