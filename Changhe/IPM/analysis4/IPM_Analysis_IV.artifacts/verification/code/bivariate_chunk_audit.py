"""Bounded chunks of the independent high-order Laurent convolution audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,pickle,sys,time
from flint import arb,arb_poly,ctx
from stream_precision_audit import unpack
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=290);ap.add_argument('--checkpoint',default='research/82_weighted_loss_criterion/update_N290_20261031T0624Z/verification/input_checkpoint.pkl.gz');ap.add_argument('--first',type=int);ap.add_argument('--last',type=int);ap.add_argument('--merge',nargs='*');a=ap.parse_args()
ctx.prec=640;start=time.monotonic();now=datetime.now(timezone.utc);n=a.n;stride=4*n+1
base=Path('research/84_bivariate_residual_audit/verification')
label='merge' if a.merge else f'pairs{a.first}_{a.last}'
root=base/f'n{n}_{label}_{now.strftime("%Y%m%dT%H%M%SZ")}';root.mkdir();(root/'sources').mkdir()
path=Path(a.checkpoint)
raw=gzip.decompress(path.read_bytes());digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
assert (state['A'],state['B'])==('2','3')
values={f:{i:[[arb(*unpack(v)) for v in row] for row in cols] for i,cols in state[f].items() if (i==n if a.merge else i<=n)} for f in ['f','g']};del state
text=lambda x:x.str(32,radius=True)
def pack(field,i,op,radial=arb(0),derivative=arb(0)):
 cols=values[field][i];shift=2*i;out=[arb(0) for _ in range(stride*(len(cols)-1)+4*i+1)]
 for q,row in enumerate(cols):
  for j,v in enumerate(row):
   m=2*j+(field=='f')
   if not m:assert v==0;continue
   assert m<=shift
   plus,minus=stride*q+shift+m,stride*q+shift-m;v=v/2
   if op=='E':out[plus]+=m*v;out[minus]+=m*v
   else:
    out[plus]+=radial*v;out[minus]-=radial*v
    if q and derivative!=0:out[plus-stride]+=derivative*q*v;out[minus-stride]-=derivative*q*v
 return arb_poly(out)
def encode(v):
 m,e=v.mid().man_exp();r,re=v.rad().man_exp()
 return str(m),int(e),str(r),int(re)
def decode(v):
 m,e,r,re=v
 return arb(*unpack((m,e,'0' if r=='0' else f'{r}*2^{re}')))
res=dict(checked_at_utc=now.isoformat(timespec='seconds'),checkpoint_path=str(path),checkpoint_sha256=digest,n=n,stride=stride,precision_bits=640,source_sha256={})
for name in ['bivariate_chunk_audit.py','stream_precision_audit.py']:
 raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw);res['source_sha256'][name]=sha256(raw).hexdigest()
total=arb_poly()
if a.merge:
 intervals=[];inputs=[]
 for name in a.merge:
  p=Path(name);raw=p.read_bytes();v=pickle.loads(gzip.decompress(raw))
  assert v['checkpoint_sha256']==digest and v['n']==n and v['precision_bits']==640
  intervals.append((v['first'],v['last']));inputs.append(dict(path=str(p),sha256=sha256(raw).hexdigest()))
  total+=arb_poly([decode(z) for z in v['coefficients']])
 covered=[i for first,last in sorted(intervals) for i in range(first,last+1)];assert covered==list(range(1,n))
 expected=pack('f',n,'R',arb(2*(n-1)),arb(-3));residual=total-expected
 failed=[i for i,x in enumerate(residual.coeffs()) if not x.contains(0)]
 forcing=sum(map(abs,expected.coeffs()),arb(0));error=sum(map(abs,residual.coeffs()),arb(0))
 res.update(inputs=inputs,intervals=intervals,checked_coefficients=len(residual),failure_count=len(failed),failed_coefficients=failed[:20],forcing_norm=text(forcing),residual_norm=text(error),relative_residual=text(error/forcing),all_residual_coefficients_contain_zero=not failed)
 assert not failed
else:
 assert 1<=a.first<=a.last<n
 for i in range(a.first,a.last+1):
  j=n-i
  total+=pack('g',i,'R',arb(2)-arb(2*i)/3,arb(1))*pack('f',j,'E')-pack('g',i,'E')*pack('f',j,'R',arb(1)-arb(2*j)/3,arb(1))
  if (i-a.first+1)%12==0:print(json.dumps(dict(n=n,through_pair=i,actual_elapsed_s=time.monotonic()-start)),flush=True)
 payload=dict(n=n,first=a.first,last=a.last,precision_bits=640,checkpoint_sha256=digest,coefficients=[encode(v) for v in total.coeffs()])
 data=gzip.compress(pickle.dumps(payload,protocol=5),compresslevel=1);(root/'partial.pkl.gz').write_bytes(data)
 res.update(first=a.first,last=a.last,pairs=a.last-a.first+1,partial_path=str(root/'partial.pkl.gz'),partial_sha256=sha256(data).hexdigest(),partial_bytes=len(data),output_length=len(total))
res['actual_elapsed_s']=time.monotonic()-start;res['complete']=True
(root/'checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),**res)),flush=True)
