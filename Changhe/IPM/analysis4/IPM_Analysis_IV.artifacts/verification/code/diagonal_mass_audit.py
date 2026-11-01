"""Exact-distance partitions with independent Arb mass enclosures."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import gzip,json,time,sys,argparse
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--orders',default='240,250,260');a=ap.parse_args()
start=time.monotonic();ctx.prec=640
src=Path(a.snapshot)/'selected_packed_coefficients.json'
if src.exists():raw=src.read_bytes()
else:
 src=src.with_suffix('.json.gz');raw=gzip.decompress(src.read_bytes())
data=json.loads(raw);assert data['delta']=='2/3'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root=Path('research/75_diagonal_mass/verification')/stamp;root.mkdir();(root/'sources').mkdir()
orders=[int(n) for n in a.orders.split(',')];results=[];count=0
text=lambda x:x.str(28,radius=True)
for f in ['f','g']:
 for n in orders:
  cols=data[f][str(n)];rows=[];weighted=[]
  for q,col in enumerate(cols):
   bands=[arb(0) for _ in range(3 if q else 2)];total=arb(0);active=[0]*len(bands);far_signed=[arb(0),arb(0)];peak=arb(0);peak_frequency=None
   for j,p in enumerate(col):
    v=abs(arb(*unpack(p)));total+=v;count+=1
    m=2*j+(1 if f=='f' else 0);signedS=3*(m+(3 if f=='f' else 2))-2*n;S=abs(signedS)
    if v>0 and (peak==0 or v>peak):peak,peak_frequency=v,m
    threshold=3*q if q else 6
    if signedS < -threshold:far_signed[0]+=v
    if signedS > threshold:far_signed[1]+=v
    b=(0 if S<=6 else 1) if not q else (0 if 4*S<=3*q else 1 if S<=3*q else 2)
    bands[b]+=v
    if v>0:active[b]+=1
   assert (sum(bands,arb(0))-total).contains(0)
   assert total>0,(f,n,q)
   frac=[v/total for v in bands];assert sum(frac,arb(0)).contains(1)
   rows.append(dict(q=q,column_norm=text(total),band_norms=[text(v) for v in bands],fractions=[text(v) for v in frac],active_modes=active,far_below_fraction=text(far_signed[0]/total),far_above_fraction=text(far_signed[1]/total),largest_mode_frequency=peak_frequency))
   if q:weighted.append((factorial(q)*total,q))
  winner,q=max(weighted,key=lambda x:float(x[0].log().mid()));cert=all(winner>x for x,j in weighted if j!=q);assert cert
  results.append(dict(field=f,n=n,winner=q,winner_certified=cert,winner_bands=rows[q],columns=rows))
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),source_path=str(src),source_sha256=sha256(raw).hexdigest(),checkpoint_sha256=data['checkpoint_sha256'],precision_bits=640,coefficient_count=count,results=results,actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['diagonal_mass_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps(dict(output_directory=str(root),coefficient_count=count,actual_elapsed_s=record['actual_elapsed_s'],winners=[{k:v for k,v in r.items() if k!='columns'} for r in results]),indent=2))
