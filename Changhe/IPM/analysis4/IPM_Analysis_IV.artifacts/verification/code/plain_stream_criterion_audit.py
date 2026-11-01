"""Floor-bound corners and the finite prefix in the plain-stream criterion."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=640;start=time.monotonic();root=Path('research/88_plain_stream_criterion')
count=0;params=0
for b in range(2,81):
 for a in range(1,b):
  if gcd(a,b)!=1:continue
  params+=1;g=gcd(a,2);q=2*b//g;h=a//g;eps=int(h==1)
  for n in range(2,601):
   d=max(0,(n-1)//q-eps)
   assert 2*b*d<=a*(n-2),(a,b,n,d)
   count+=1
snapshot=Path('research/64_log_precision_updates/verification/log_sin1_c3_p512_N290_20261031T061856Z/checks.json')
weighted=Path('research/82_weighted_loss_criterion/update_N290_20261031T0624Z/verification/checks.json')
raw=snapshot.read_bytes();data=json.loads(raw);raw2=weighted.read_bytes();old=json.loads(raw2)
assert data['checkpoint_sha256']==old['checkpoint_sha256']
early={r['n']:r for w in old['weights'] if w['s']==1 for r in w['rows'] if r['n']<=6}
fields={f:{r['n']:arb(r['log10_plain_norm']) for r in data['fields'][f]['all_order_factorial_comparisons']} for f in ['f','g']}
for n,r in early.items():
 fields['f'][n]=arb(r['density_log10']);fields['g'][n]=arb(r['stream_log10'])
L10=arb(10).log();rows=[];ratios={}
for n in range(1,291):
 ratio=((fields['g'][n]-fields['f'][n])*L10).exp();ratios[n]=ratio
 assert ratio<arb(1)/4,(n,str(ratio))
 rows.append(dict(n=n,ratio=ratio.str(32,radius=True),below_quarter=True))
winner=max(ratios,key=lambda n:float(ratios[n].mid()));assert all(ratios[winner]>v for n,v in ratios.items() if n!=winner)
radius=arb(6)*(arb(64)**(-arb(2)/3))*(arb(64).log()**(arb(2)/3));assert radius<1
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,parameter_count=params,exact_floor_checks=count,finite_prefix_maximum_order=290,strict_maximum_n=winner,maximum_plain_stream_over_density=ratios[winner].str(35,radius=True),conditional_A='6',conditional_R='64',radial_ratio_at_64=radius.str(35,radius=True),scope='All-order ratio hypothesis is not established; these are finite checks.',inputs=[dict(path=str(snapshot),sha256=sha256(raw).hexdigest()),dict(path=str(weighted),sha256=sha256(raw2).hexdigest())],ratios=rows)
(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(root/'sources/plain_stream_criterion_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in out.items() if k not in ['ratios','inputs']}))
