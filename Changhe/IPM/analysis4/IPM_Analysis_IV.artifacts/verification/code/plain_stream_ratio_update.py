"""Append-only plain stream/density ratios, preserving uncertain decisions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import argparse,json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=640
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('weighted');a=ap.parse_args()
start=time.monotonic();now=datetime.now(timezone.utc)
snapshot=Path(a.snapshot)/'checks.json';weighted=Path(a.weighted)/'verification/checks.json'
raw=snapshot.read_bytes();data=json.loads(raw);raw2=weighted.read_bytes();other=json.loads(raw2)
assert data['checkpoint_sha256']==other['checkpoint_sha256']
N=data['maximum_order'];assert N==other['maximum_order']
root=Path('research/88_plain_stream_criterion/verification')/('update_N'+str(N)+'_'+now.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
text=lambda x:x.str(35,radius=True)
L10=arb(10).log();quarter=arb(1)/4
fields={f:{r['n']:arb(r['log10_plain_norm']) for r in data['fields'][f]['all_order_factorial_comparisons']} for f in ['f','g']}
for block in other['weights']:
 if block['s']!=1:continue
 for r in block['rows']:
  if r['n']<=6:
   # Canonical delta2/3 coefficients have degree zero through order6.
   fields['f'][r['n']]=arb(r['density_log10']);fields['g'][r['n']]=arb(r['stream_log10'])
ratios={};rows=[];prefix=0;first_above=None;first_uncertain=None
for n in range(1,N+1):
 lg=fields['g'][n]-fields['f'][n];ratio=(lg*L10).exp();ratios[n]=ratio
 below=bool(ratio<=quarter);above=bool(ratio>quarter)
 if below and prefix==n-1:prefix=n
 if above and first_above is None:first_above=n
 if not below and not above and first_uncertain is None:first_uncertain=n
 rows.append(dict(n=n,ratio=text(ratio),log10_ratio=text(lg),certified_at_most_quarter=below,certified_above_quarter=above,
                  density_log10=text(fields['f'][n]),stream_log10=text(fields['g'][n])))
winner=max(ratios,key=lambda n:float(ratios[n].mid()))
strict=all(bool(ratios[winner]>v) for n,v in ratios.items() if n!=winner)
lfact={n:arb(factorial(n)).log()/L10 for n in range(N+1)};indicators=[]
for f in ['f','g']:
 for n in range(100,N+1):
  for h in [9,18,30]:
   val=(fields[f][n]-2*fields[f][n-h]+fields[f][n-2*h])/(lfact[n]-2*lfact[n-h]+lfact[n-2*h])
   indicators.append(dict(field=f,n=n,h=h,finite_sigma=text(val)))
res=dict(checked_at_utc=now.isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,checkpoint_sha256=data['checkpoint_sha256'],maximum_order=N,
 last_both_field_resolved_prefix=data.get('last_both_field_resolved_prefix'),last_both_field_1e_minus_6_prefix=data.get('last_both_field_1e_minus_6_prefix'),
 last_quarter_bound_prefix=prefix,first_certified_above_quarter=first_above,first_uncertain_quarter_comparison=first_uncertain,
 maximum_candidate_n=winner,maximum_candidate_ratio=text(ratios[winner]),maximum_is_strictly_certified=strict,
 inputs=[dict(path=str(snapshot),sha256=sha256(raw).hexdigest()),dict(path=str(weighted),sha256=sha256(raw2).hexdigest())],
 ratios=rows,plain_curvature_indicators=indicators,
 scope='Finite plain-norm ratios. The all-order hypothesis and extrapolations are not certified.')
(root/'checks.json').write_text(json.dumps(res,indent=2)+'\n');(root/'sources/plain_stream_ratio_update.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(output_directory=str(root),**{k:v for k,v in res.items() if k not in ['ratios','plain_curvature_indicators','inputs']})),flush=True)
for row in rows:
 if row['n']>=291:print(json.dumps(row),flush=True)
for row in indicators:
 if row['n']==N and row['h']==30:print(json.dumps(row),flush=True)
