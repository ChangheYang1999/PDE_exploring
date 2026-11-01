"""All-order independent sine-product forcing check for K1/K3 edge checkpoints."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
from stream_precision_audit import unpack
import argparse,gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('snapshot');a=ap.parse_args();start=time.monotonic();ctx.prec=1152
source=Path(a.snapshot);old=json.loads((source/'checks.json').read_text());K=old['K'];N=old['maximum_order'];assert K in [1,3]
path=source/'input_checkpoint.pkl.gz';raw=gzip.decompress(path.read_bytes());digest=sha256(raw).hexdigest();assert digest==old['source_sha256'];state=pickle.loads(raw);del raw
root=Path('research/102_edge_recurrence_reference/verification')/('nonlinear_edge'+str(K)+'_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
zero=arb(0);cache={};text=lambda v:v.str(35,radius=True)
def load(field,n):
 key=(field,n)
 if key not in cache:cache[key]=[[arb(*unpack(v)) for v in row] for row in state[field][n]]
 return cache[key]
def get(cols,q,j):return cols[q][j] if q<len(cols) and j<len(cols[q]) else zero
for i in range(1,K+1):
 for field in ['f','g']:
  low=load(field,i)
  assert all(v==0 for row in low[1:] for v in row),'This audit requires log-independent low factors.'
rows=[];pair_count=checks=0;maxrel=zero
for n in range(2,N+1):
 F=load('f',n);deg=max(len(F),max(len(state[field][i]) for field in ['f','g'] for i in range(max(1,n-K),n)))
 out=[[arb(0) for _ in range(n)] for _ in range(deg)]
 def add(q,m,value):
  if not m:
   assert value==0;return
  if m<0:m=-m;value=-value
  assert m%2==1 and m<=2*n-1
  out[q][m//2]+=value
 for i in range(1,n):
  j=n-i
  if min(i,j)>K:continue
  pair_count+=1;G=load('g',i);H=load('f',j);Pi=arb(2)-arb(2*i)/3;pj=arb(1)-arb(2*j)/3
  if i<=K:
   for hindex,b in enumerate(G[0]):
    if b==0:continue
    h=2*hindex
    for q,col in enumerate(H):
     for mindex,v in enumerate(col):
      dv=(q+1)*get(H,q+1,mindex)
      if v==0 and dv==0:continue
      m=2*mindex+1
      av=Pi*b*m*v;bv=h*b*(pj*v+dv)
      add(q,h+m,(av-bv)/2);add(q,h-m,(av+bv)/2)
  else:
   assert j<=K
   for mindex,b in enumerate(H[0]):
    if b==0:continue
    m=2*mindex+1
    for q,col in enumerate(G):
     for hindex,v in enumerate(col):
      dv=(q+1)*get(G,q+1,hindex)
      if v==0 and dv==0:continue
      h=2*hindex;assert h>0
      av=m*b*(Pi*v+dv);bv=h*pj*b*v
      add(q,h+m,(av-bv)/2);add(q,h-m,(av+bv)/2)
 error=norm=zero;fail=[]
 for q,col in enumerate(out):
  for mindex,actual in enumerate(col):
   expected=2*(n-1)*get(F,q,mindex)-3*(q+1)*get(F,q+1,mindex)
   residue=actual-expected;checks+=1;error+=abs(residue);norm+=abs(expected)
   if not residue.contains(0):fail.append([q,2*mindex+1,text(residue)])
 assert not fail,(n,fail[:5])
 relative=error/norm if norm>0 else zero
 if relative.upper()>maxrel:maxrel=relative.upper()
 rows.append(dict(n=n,coefficients=sum(map(len,out)),relative_residual=text(relative),all_residuals_contain_zero=True))
 for key in list(cache):
  if K<key[1]<n-K:del cache[key]
 if n%30==0 or n==N:print(json.dumps(dict(K=K,n=n,ordered_pairs=pair_count,checked_coefficients=checks,elapsed_s=time.monotonic()-start)),flush=True)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),K=K,maximum_order=N,input_path=str(path),input_sha256=digest,precision_bits=1152,ordered_pairs=pair_count,checked_coefficients=checks,maximum_relative_residual=text(maxrel),rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Every retained ordered nonlinear product at every order2..N, with an independent sine-product implementation; finite interval verification only.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['edge_nonlinear_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps(dict(output_directory=str(root),**{k:v for k,v in result.items() if k!='rows'})),flush=True)
