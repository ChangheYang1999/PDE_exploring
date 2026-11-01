"""Certified finite growth diagnostics from independently enclosed column norms."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
from math import factorial
import json,sys,time
ctx.prec=640;start=time.monotonic();src=Path(sys.argv[1]);raw=src.read_bytes();data=json.loads(raw);root=src.parent
text=lambda x:x.str(25,radius=True)
rows={f:{r['n']:r for r in data['fields'][f]['all_order_factorial_comparisons']} for f in ['f','g']}
plain={};reconstruction=0
for f,rs in rows.items():
 plain[f]={}
 for n,r in rs.items():
  val=arb(r['log10_plain_norm']);recon=sum((arb(10)**arb(v) for v in r['column_log10_norms'] if v is not None),arb(0)).log()/arb(10).log()
  assert val.overlaps(recon)
  plain[f][n]=val;reconstruction+=1
increments=[]
for n in range(180,data['maximum_order']+1):
 rec={'n':n}
 for f in ['f','g']:
  L=plain[f]
  if n-11 not in L:continue
  same=(L[n]-L[n-9])/9
  one={m:L[m]-L[m-1] for m in range(n-8,n+1)}
  groups=[sum((v for m,v in one.items() if m%3==r),arb(0))/3 for r in range(3)]
  assert same.overlaps(sum(groups,arb(0))/3)
  rec[f]=dict(log10_plain_norm=text(L[n]),same_residue_nine_order_increment=text(same),one_step_group_means_by_endpoint_residue=[text(v) for v in groups])
 increments.append(rec)
deficits=[]
for r in [1,2,3]:
 for k in range(70,(data['maximum_order']-r)//3+1):
  n=3*k+r
  if n not in rows['f'] or n-15 not in rows['f']:continue
  for d in range(0,min(60,k-6)+1):
   q=k-1-d;q0=q-5
   if q0<0:continue
   a=rows['f'][n]['column_log10_norms'];b=rows['f'][n-15]['column_log10_norms']
   if q>=len(a) or q0>=len(b) or a[q] is None or b[q0] is None:continue
   val=arb(a[q])+arb(factorial(q)).log()/arb(10).log();old=arb(b[q0])+arb(factorial(q0)).log()/arb(10).log()
   deficits.append(dict(k=k,r=r,n=n,d=d,q=q,log10_factorial_column=text(val),five_block_mean_increment=text((val-old)/5)))
peer=Path('../a4-num/logs/log_sin1_c3_p512.jsonl');peerraw=peer.read_bytes();peerrows={r['n']:r for r in map(json.loads,peerraw.splitlines()) if 'n' in r and 'log10_sum_cols' in r}
errors=[]
for n,L in plain['f'].items():
 if n in peerrows:errors.append(abs(float(L.mid())-peerrows[n]['log10_sum_cols']))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),source_path=str(src),source_sha256=sha256(raw).hexdigest(),peer_log_path=str(peer),peer_log_sha256=sha256(peerraw).hexdigest(),precision_bits=640,all_plain_reconstructions_overlap=True,reconstruction_count=reconstruction,maximum_density_log10_difference_from_peer_float=max(errors),definitions={'same_residue':'(L(n)-L(n-9))/9','one_step_groups':'mean of L(m)-L(m-1) for m in [n-8,n], grouped by m mod3','deficit_increment':'[log10(q! c(n,q))-log10((q-5)! c(n-15,q-5))]/5'},increments=increments,fixed_deficit_diagnostics=deficits,actual_elapsed_s=time.monotonic()-start)
(root/'growth_diagnostics.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/column_growth_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['increments','fixed_deficit_diagnostics']}))
