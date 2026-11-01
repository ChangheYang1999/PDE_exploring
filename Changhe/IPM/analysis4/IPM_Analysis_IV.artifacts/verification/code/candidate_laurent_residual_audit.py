"""Direct Laurent-polynomial stationary checks, independent of split sine convolutions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,arb_poly,fmpq,ctx
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('checkpoint');ap.add_argument('--orders',default='2,3,6,10,20,40,80,160,233,300,390');ap.add_argument('--seconds',type=float,default=510);a=ap.parse_args()
start=time.monotonic();now=datetime.now(timezone.utc);ctx.prec=2304
root=Path('research/91_candidate_checkpoint_audit/verification')/('nonlinear_'+now.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
path=Path(a.checkpoint);raw=path.read_bytes()
if path.suffix=='.gz':raw=gzip.decompress(raw)
digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
assert state['prec']==2048 and state['ring']=='arb'
orders=list(map(int,a.orders.split(',')));N=max(orders);assert max(state['f'])>=N
delta=arb(fmpq(state['delta_exact']));c=1/(1-delta);B=20
polys={};derivs={}
for field in ['f','g']:
 polys[field]={};derivs[field]={}
 for n,row in sorted(state[field].items()):
  if n>N:continue
  off=B*n;v=[arb(0)]*(2*off+1);ev=[arb(0)]*(2*off+1)
  for j,packed in enumerate(row):
   m=2*j+(field=='f');z=arb(*unpack(packed))
   if m==0:assert z.is_zero();continue
   assert m<=off
   h=z/2;v[off+m]=h;v[off-m]=-h;ev[off+m]=m*h;ev[off-m]=m*h
  polys[field][n]=arb_poly(v);derivs[field][n]=arb_poly(ev)
  if n%100==0:print(json.dumps(dict(stage='pack',field=field,n=n,elapsed_s=time.monotonic()-start)),flush=True)
del state
text=lambda x:x.str(40,radius=True)
result=dict(checked_at_utc=now.isoformat(timespec='seconds'),checkpoint_path=str(path),checkpoint_sha256=digest,precision_bits=2304,angular_offset_per_order=B,orders=[],source_sha256={})
for name in ['candidate_laurent_residual_audit.py','stream_precision_audit.py']:
 content=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(content);result['source_sha256'][name]=sha256(content).hexdigest()
for n in orders:
 if time.monotonic()-start>a.seconds:break
 at=time.monotonic();total=arb_poly()
 for i in range(1,n):
  j=n-i
  total+=(polys['g'][i]*derivs['f'][j])*(2-i*delta)-(derivs['g'][i]*polys['f'][j])*(1-j*delta)
 expected=polys['f'][n]*((n-1)*(c-1));residual=total-expected
 vals=residual.coeffs();bad=[k for k,v in enumerate(vals) if not v.contains(0)]
 norm=sum(map(abs,expected.coeffs()),arb(0));err=sum(map(abs,vals),arb(0))
 row=dict(n=n,pairs=n-1,checked_coefficients=len(vals),failure_count=len(bad),failed_coefficients=bad[:20],all_residuals_contain_zero=not bad,
          forcing_norm=text(norm),residual_norm=text(err),relative_residual=text(err/norm),actual_elapsed_s=time.monotonic()-at)
 result['orders'].append(row);result['actual_elapsed_s']=time.monotonic()-start
 (root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(row),flush=True)
 assert not bad
result['complete_requested_orders']=len(result['orders'])==len(orders);result['actual_elapsed_s']=time.monotonic()-start
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(output_directory=str(root),complete=result['complete_requested_orders'],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
