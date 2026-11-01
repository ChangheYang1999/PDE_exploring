"""Certified finite stream shift shares and descriptive slope statistics."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
import argparse,gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('checkpoint');ap.add_argument('--first',type=int,default=200);ap.add_argument('--last',type=int,default=300);args=ap.parse_args()
ctx.prec=640;start=time.monotonic();stamp=datetime.now(timezone.utc)
root=Path('research/87_plain_distance_diagnostics/verification')/('stream_shifts_'+stamp.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
path=Path(args.checkpoint);raw=path.read_bytes()
if path.suffix=='.gz':raw=gzip.decompress(raw)
digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
assert (state['A'],state['B'])==('2','3')
last=min(args.last,max(state['f']));rows={};logs={'f':{},'g':{}}
text=lambda x:x.str(32,radius=True)
refpath=Path('../a4-lead/logs/stream_ratio_modes_c3.json');refraw=refpath.read_bytes();refs=json.loads(refraw)['orders'];(root/'sources/lead_stream_modes.json').write_bytes(refraw)
maxdiff=0.0;comparisons=0
for n in range(args.first,last+1):
 row={};totals={};columns={};groups={};signed={}
 for field in ['f','g']:
  cols=[];near=arb(0)
  for q,col in enumerate(state[field][n]):
   total=arb(0)
   for j,packed in enumerate(col):
    value=abs(arb(*unpack(packed)));total+=value
    if field=='g':
     if j==0:assert value.is_zero();continue
     plus=6-2*n+6*j;minus=6-2*n-6*j;s=min(abs(plus),abs(minus))
     key=str(Fraction(s,3)) if s<=12 else 'far'
     groups[key]=groups.get(key,arb(0))+value
     v=plus if abs(plus)<=abs(minus) else minus
     key2=str(Fraction(v,3)) if s<=12 else 'far'
     signed[key2]=signed.get(key2,arb(0))+value
    elif abs(abs(6-2*n)-3*(2*j+1))<=4:near+=value
   cols.append(total)
  norm=sum(cols,arb(0));assert norm>0;totals[field]=norm;columns[field]=cols;logs[field][n]=norm.log()/arb(10).log()
  maxq=max(range(len(cols)),key=lambda q:float(cols[q]));strict=all(q==maxq or cols[maxq]>cols[q] for q in range(len(cols)))
  row[field]=dict(log10_plain_norm=text(logs[field][n]),column0_share=text(cols[0]/norm),column_argmax=maxq,strict_column_argmax=strict)
  if field=='f':row[field]['density_near_share']=text(near/norm)
 row['g']['share_by_shift']={k:text(v/totals['g']) for k,v in groups.items()}
 row['g']['share_by_signed_shift']={k:text(v/totals['g']) for k,v in signed.items()}
 row['log10_stream_density_ratio']=text(logs['g'][n]-logs['f'][n]);rows[n]=row
 if str(n) in refs:
  r=refs[str(n)];pairs=[(logs['f'][n],r['log10M']),(logs['g'][n],r['log10N']),(logs['g'][n]-logs['f'][n],r['log10ratio']),(columns['g'][0]/totals['g'],r['stream_col0_share'])]
  pairs.extend((groups[k]/totals['g'],v) for k,v in r['stream_share_by_shift'].items())
  for value,reported in pairs:
   diff=abs(value-arb(reported));assert diff<arb('1e-10');maxdiff=max(maxdiff,float(diff.upper()));comparisons+=1
 if n%10==0:print(json.dumps(dict(order=n,elapsed_s=time.monotonic()-start)),flush=True)
stats=[]
for field in ['f','g']:
 for lo,hi in list(dict.fromkeys([(230,257),(263,290),(273,300),(291,300),(last-27,last),(last-9,last)])):
  ns=[n for n in range(lo,hi+1) if n in logs[field] and n-3 in logs[field]]
  if len(ns)<3:continue
  vs=[(logs[field][n]-logs[field][n-3])/3 for n in ns];num=len(ns);mean=sum(vs,arb(0))/num
  xm=arb(sum(ns))/num;sxx=sum(((arb(n)-xm)**2 for n in ns),arb(0));beta=sum(((arb(n)-xm)*(v-mean) for n,v in zip(ns,vs)),arb(0))/sxx
  sse=sum(((v-mean-beta*(arb(n)-xm))**2 for n,v in zip(ns,vs)),arb(0));se=(sse/(num-2)/sxx).sqrt();sd=(sum(((v-mean)**2 for v in vs),arb(0))/(num-1)).sqrt()
  stats.append(dict(field=field,window=[lo,hi],count=num,three_step_slope_mean=text(mean),sample_sd=text(sd),linear_trend_per_100_orders=text(100*beta),regression_standard_error_per_100_orders=text(100*se),scope='Descriptive least-squares statistics of this finite deterministic sequence; not a probabilistic confidence interval or asymptotic test.'))
for name in ['stream_shift_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
result=dict(checked_at_utc=stamp.isoformat(timespec='seconds'),checkpoint_path=str(path),checkpoint_sha256=digest,precision_bits=640,first_order=args.first,last_order=last,rows=rows,statistics=stats,lead_comparisons=comparisons,maximum_lead_float_difference=maxdiff,actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(output_directory=str(root),actual_elapsed_s=result['actual_elapsed_s'],comparisons=comparisons)),flush=True)
