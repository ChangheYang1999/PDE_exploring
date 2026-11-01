"""Global two-sided norm bounds from positive coefficients and independent point evaluations."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,pickle,time,sys
sys.dont_write_bytecode=True
from flint import arb,arb_poly,ctx
from stream_precision_audit import unpack
ctx.prec=640;start=time.monotonic();now=datetime.now(timezone.utc)
root=Path('research/90_real_line_norm_enclosure');out=root/'verification'/now.strftime('%Y%m%dT%H%M%SZ');out.mkdir();(out/'sources').mkdir()
checkpoint=Path('research/82_weighted_loss_criterion/update_N290_20261031T0624Z/verification/input_checkpoint.pkl.gz')
raw=gzip.decompress(checkpoint.read_bytes());digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
leadpath=Path('../a4-lead/logs/exptype_c3.json');raw=leadpath.read_bytes();lead=json.loads(raw)
(out/'sources/lead_grid.json').write_bytes(raw)
eta=arb(1)/3;h=arb(1)/4;L10=arb(10).log();text=lambda x:x.str(34,radius=True)
rows=[]
for n in [150,180,200,210,240,260,270,290]:
 if str(n) not in lead['orders']:continue
 for field in ['f','g']:
  cols=[[arb(*unpack(v)) for v in col] for col in state[field][n]];K=len(cols)-1;M=max(map(len,cols))
  U=arb_poly([sum(map(abs,col),arb(0)) for col in cols])
  step=lead['grid_step'];T=lead['tmax'];values=lead['orders'][str(n)][field]['log10V']
  samples=[]
  for side in [-1,1]:
   choices=[]
   for i,value in enumerate(values):
    t=-T+i*step
    if value is not None and side*t>=0:choices.append((value-abs(t)/(3*float(L10.mid())),t))
   _,t=max(choices);ta=arb(t);v=[arb(0)]*M
   for col in reversed(cols):v=[x*ta+(col[j] if j<len(col) else arb(0)) for j,x in enumerate(v)]
   norm=sum(map(abs,v),arb(0));weight=(-eta*abs(ta)).exp();w=norm*weight
   samples.append(dict(t=t,weighted_norm=text(w),log10_weighted_norm=text(w.log()/L10) if w>0 else None,relative_radius=text(w.rad()/abs(w.mid())) if w.mid()!=0 else None,resolved_positive=bool(w>0),side=side))
  lower=max([arb(0)]+[arb(arb(s['weighted_norm']).lower()) for s in samples]);assert lower>0
  upper=arb(0);max_cell=None
  # K/eta=3K and h=1/4, so the endpoint is exactly represented.
  for j in range(1,12*K+1):
   a=arb(j-1)/4;b=arb(j)/4;bound=(-eta*a).exp()*U(b);u=arb(bound.upper())
   if u>upper:upper,max_cell=u,[str(a),str(b)]
  assert lower<=upper
  rows.append(dict(n=n,field=field,degree=K,eta='1/3',partition_step='1/4',partition_endpoint=str(3*K),cell_count=12*K,samples=samples,
      global_lower=text(lower),global_upper=text(upper),log10_global_lower=text(lower.log()/L10),log10_global_upper=text(upper.log()/L10),
      log10_enclosure_width=text((upper/lower).log()/L10),maximal_upper_cell=max_cell))
  print(json.dumps({k:v for k,v in rows[-1].items() if k not in ['samples','global_lower','global_upper']}),flush=True)
res=dict(checked_at_utc=now.isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,checkpoint_path=str(checkpoint),checkpoint_sha256=digest,lead_grid_path=str(leadpath),lead_grid_sha256=sha256(raw).hexdigest(),precision_bits=640,rows=rows,scope='Certified global norm enclosure, not a certified maximizing location or asymptotic statement.')
for name in ['real_line_norm_enclosure.py','stream_precision_audit.py']:(out/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
(out/'checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(out),actual_elapsed_s=res['actual_elapsed_s'],rows=len(rows))))
