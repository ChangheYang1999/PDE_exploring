"""Outward-rounded realized forcing losses in weighted factorial norms."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import argparse,gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack

ap=argparse.ArgumentParser()
ap.add_argument('--weights',default='1,12')
ap.add_argument('--checkpoint',default='research/78_factorial_product_losses/verification/input_checkpoint.pkl.gz')
ap.add_argument('--output',default='research/82_weighted_loss_criterion')
ap.add_argument('--freeze-input',action='store_true')
a=ap.parse_args()
ctx.prec=640
root=Path(a.output)
for name in ['sources','verification']:(root/name).mkdir(parents=True,exist_ok=True)
start=time.monotonic()
path=Path(a.checkpoint)
from read_checkpoint_archive import read_bytes
raw=read_bytes(path)
digest=sha256(raw).hexdigest()
state=pickle.loads(raw)
if a.freeze_input:
 frozen=root/'verification/input_checkpoint.pkl.gz'
 with gzip.open(frozen,'wb',compresslevel=1) as f:f.write(raw)
 path=frozen
del raw
assert (state['A'],state['B'],state['prec'])==('2','3',512)
N=max(state['f'])
cols={};forcing={}
for field in ['f','g']:
 cols[field]={}
 for n,packed in sorted(state[field].items()):
  values=[[arb(*unpack(z)) for z in row] for row in packed]
  cols[field][n]=[sum(map(abs,row),arb(0)) for row in values]
  if field=='f' and n>=2:
   forcing[n]=[]
   for q,row in enumerate(values):
    nxt=values[q+1] if q+1<len(values) else []
    forcing[n].append(sum((abs(2*(n-1)*(row[j] if j<len(row) else arb(0))-3*(q+1)*(nxt[j] if j<len(nxt) else arb(0))) for j in range(max(len(row),len(nxt)))),arb(0)))
del state
text=lambda x:x.str(35,radius=True)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),input_path=str(path),
 checkpoint_sha256=digest,maximum_order=N,precision_bits=640,source_sha256={},weights=[])
for name in ['weighted_loss_audit.py','stream_precision_audit.py','read_checkpoint_archive.py']:
 source=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(source);result['source_sha256'][name]=sha256(source).hexdigest()
ref=json.loads(Path('research/78_factorial_product_losses/verification/checks.json').read_text())
ref_ratios={r['n']:arb(r['rho']) for r in ref['full_ratios']}
for s in map(int,a.weights.split(',')):
 factor=[arb(factorial(q)*s**q) for q in range(N+1)]
 weight=lambda row:sum((factor[q]*v for q,v in enumerate(row)),arb(0))
 norms={field:{n:weight(row) for n,row in byn.items()} for field,byn in cols.items()}
 rows=[]
 for n in range(1,N+1):
  f,g=norms['f'][n],norms['g'][n]
  row=dict(n=n,density=text(f),stream=text(g),stream_over_density=text(g/f),
    density_log10=text(f.log()/arb(10).log()),stream_log10=text(g.log()/arb(10).log()),
    density_root=text((f.log()/n).exp()),stream_root=text((g.log()/n).exp()))
  if n>=2:
   den=arb(0)
   for i in range(1,n):
    j=n-i;w=2*j*(abs(arb(2)-arb(2*i)/3)+1)+2*i*(abs(arb(1)-arb(2*j)/3)+1)
    den+=w*norms['g'][i]*norms['f'][j]
   S=weight(forcing[n]);rho=S/den
   row.update(forcing_norm=text(S),baseline=text(den),rho=text(rho))
   if s==1 and n in ref_ratios:
    assert rho.overlaps(ref_ratios[n]),n
    row['overlaps_previous_unweighted']=True
  rows.append(row)
 result['weights'].append(dict(s=s,rows=rows))
 result['actual_elapsed_s']=time.monotonic()-start
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(weight=s,maximum_order=N,last=rows[-1],elapsed_s=result['actual_elapsed_s'])),flush=True)
result['complete']=True;result['actual_elapsed_s']=time.monotonic()-start
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(complete=True,elapsed_s=result['actual_elapsed_s'])),flush=True)
