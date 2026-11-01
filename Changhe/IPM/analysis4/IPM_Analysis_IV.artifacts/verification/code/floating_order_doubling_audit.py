"""Freeze completed extended outputs and exactly fit their printed block maxima."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,gzip,re,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=768
ROOT=Path('research/290_floating_order_doubling')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def reference(p):
 r=p.read_bytes();return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def ab(q):return arb(q.numerator)/q.denominator
def disp(q):return q.str(38,radius=True)
def parse(p,Q):
 text=p.read_text();lines=text.splitlines();h=lines[0]
 assert f'Q={Q} h=1' in h and '# done,' in text
 rows={};tuning={}
 for line in lines:
  if line.startswith('n '):
   _,n,f,g=line.split();assert f.lower() not in ('inf','nan','-inf') and g.lower() not in ('inf','nan','-inf')
   rows[int(n)]=(F(f),F(g))
  elif line.startswith('k '):
   t=line.split();tuning[int(t[1])]=(int(t[3]),F(t[4]),F(t[6]),int(t[8]),F(t[9]))
 assert sorted(rows)==list(range(1,max(rows)+1))
 normalized=re.sub(r' eps=[^ ]+','',re.sub(r' N=\d+','',h))
 epsilon=F(re.search(r' eps=([^ ]+)',h).group(1));assert epsilon>0
 assert epsilon.numerator&(epsilon.numerator-1)==0 and epsilon.denominator&(epsilon.denominator-1)==0
 return dict(header=h,normalized=normalized,epsilon=str(epsilon),rows=rows,tuning=tuning,announced_order=int(re.search(r'# done, last density order (\d+)',text).group(1)))
def fits(rows,Q):
 blocks=[]
 for j in range(max(rows)//Q):
  ns=list(range(j*Q+1,(j+1)*Q+1));assert all(n in rows for n in ns)
  blocks.append((F((j+1)*Q),max(rows[n][0] for n in ns),max(rows[n][1] for n in ns)))
 result=[]
 for lo in [100,150,200,300,400,500]:
  ss=[v for v in blocks if v[0]>=lo]
  if len(ss)<4:continue
  count=len(ss);sx=sum(v[0] for v in ss);sxx=sum(v[0]**2 for v in ss);den=count*sxx-sx*sx;assert den>0
  for channel,j in [('density',1),('stream',2)]:
   sy=sum(v[j] for v in ss);sxy=sum(v[0]*v[j] for v in ss);a=(count*sxy-sx*sy)/den;b=(sy-a*sx)/count
   sq=sum((a*v[0]+b-v[j])**2 for v in ss)/count
   result.append(dict(window_lower=lo,first_block_end=int(ss[0][0]),last_block_end=int(ss[-1][0]),blocks=count,channel=channel,slope=str(a),intercept=str(b),squared_rms=str(sq),A=disp((ab(a)*arb(10).log()).exp()),apparent_radius=disp((ab(a*F(Q,2))*arb(10).log()).exp()),rms=disp(ab(sq).sqrt())))
 return result

def main():
 start=time.monotonic();done=[];pending=[]
 for Q in [7,8]:
  N=602 if Q==7 else 600
  for index in range(1,11):
   name=f'hhf_Q{Q}h1_root{index}_N{N}_f64.out';src=Path('../a4-lead/code/tuned')/name
   if not src.exists() or '# done,' not in src.read_text():pending.append(dict(Q=Q,root=index));continue
   out=ROOT/'verification'/f'Q{Q}_root{index}.json'
   if out.exists():done.append(json.loads(out.read_text()));continue
   if index==1:base=Path('research/264_floating_response_accuracy/sources')/f'hhf_Q{Q}h1_root1_N{301 if Q==7 else 304}_f64e16.out'
   else:base=Path('research/263_floating_period_growth_audit/sources')/f'hhf_Q{Q}h1_root{index}_N{301 if Q==7 else 304}_f64.out'
   dst=ROOT/'sources'/name;dst.write_bytes(src.read_bytes());a=parse(base,Q);b=parse(dst,Q)
   assert a['normalized']==b['normalized'],(a['normalized'],b['normalized'])
   common=set(a['rows'])&set(b['rows']);assert common==set(a['rows'])
   errors=[abs(a['rows'][n][j]-b['rows'][n][j]) for n in sorted(common) for j in [0,1]]
   assert max(errors)<F(1,10**7),(Q,index,max(errors))
   tuning_common=set(a['tuning'])&set(b['tuning']);assert tuning_common==set(a['tuning'])
   tuning_errors=[]
   for k in sorted(tuning_common):
    aa=a['tuning'][k];bb=b['tuning'][k];assert aa[0]==bb[0] and aa[3]==bb[3]
    tuning_errors.append(dict(k=k,R_log_difference=str(abs(aa[1]-bb[1])),sigma_relative_difference=str(abs((aa[2]-bb[2])/aa[2])),H_log_difference=str(abs(aa[4]-bb[4]))))
   fa=fits(a['rows'],Q);fb=fits(b['rows'],Q);old={(r['channel'],r['window_lower']):r for r in fa};changes=[]
   for r in fb:
    key=(r['channel'],r['window_lower'])
    if key in old:
     da=F(r['slope'])-F(old[key]['slope']);ratio=(ab(da)*arb(10).log()).exp()
     changes.append(dict(channel=key[0],window_lower=key[1],relative_A_change=disp(ratio-1),absolute_relative_A_change=disp(abs(ratio-1))))
   previous=[arb(r['A']) for r in fa if r['channel']=='density' and r['window_lower'] in [100,150,200]]
   low=min(previous,key=lambda x:float(x.mid()));high=max(previous,key=lambda x:float(x.mid()));outside=[]
   for r in fb:
    if r['channel']!='density' or r['window_lower'] not in [100,200,300,400]:continue
    v=arb(r['A']);dist=low/v-1 if v<low else v/high-1 if v>high else arb(0)
    outside.append(dict(window_lower=r['window_lower'],relative_distance_outside_old_A_range=disp(dist),within_one_percent=dist<arb('0.01')))
   record=dict(at=stamp(),all_checks_pass=True,Q=Q,root_index=index,source=reference(dst),baseline=reference(base),header=b['header'],announced_order=b['announced_order'],last_printed_order=max(b['rows']),last_complete_block=Q*(max(b['rows'])//Q),printed_norm_overlap_count=len(errors),exact_printed_norm_overlaps=sum(v==0 for v in errors),maximum_printed_log_difference=str(max(errors)),printed_tuning_row_overlaps=len(tuning_common),tuning_overlap_discrepancies=tuning_errors,baseline_epsilon=a['epsilon'],extended_epsilon=b['epsilon'],baseline_fits=fa,extended_fits=fb,same_window_changes=changes,outside_old_range=outside,scope='Exact finite statistics of rounded printed floating data; no high-order enclosure or infinite-tail estimate.')
   out.write_text(json.dumps(record,indent=2)+'\n');done.append(record);print(json.dumps({k:v for k,v in record.items() if k in ['Q','root_index','last_printed_order','last_complete_block','exact_printed_norm_overlaps','exact_printed_tuning_row_overlaps','outside_old_range']}),flush=True)
 result=dict(at=stamp(),all_completed_checks_pass=True,completed=len(done),pending=pending,checked_sources=[r['source'] for r in done],actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/latest.json').write_text(json.dumps(result,indent=2)+'\n');(ROOT/'sources/floating_order_doubling_audit.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(result),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  failure=dict(at=stamp(),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(e.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
