"""Compare printed floating Q7/Q8 data with directed prefixes; exact decimal fits."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,gzip,re,sys,time,math
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball
from period_polar_prefix_replay import unpack
from certified_initial_majorants import pack
ROOT=Path('research/263_floating_period_growth_audit')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def ab(x):return ball(mpq(str(x)))
def disp(x):return x.str(32,radius=True)
def fit(rows,Q):
 blocks=[]
 for j in range(max(rows)//Q):
  ns=list(range(j*Q+1,(j+1)*Q+1))
  if all(n in rows for n in ns):blocks.append((F((j+1)*Q),max(rows[n][0] for n in ns),max(rows[n][1] for n in ns)))
 out=[]
 for lo in (100,150,200):
  subset=[x for x in blocks if x[0]>=lo]
  if len(subset)<2:continue
  m=len(subset);sx=sum(x[0] for x in subset);sxx=sum(x[0]**2 for x in subset);dd=m*sxx-sx*sx
  channels=[]
  for col in (1,2):
   sy=sum(x[col] for x in subset);sxy=sum(x[0]*x[col] for x in subset);a=(m*sxy-sx*sy)/dd;b=(sy-a*sx)/m;sq=sum((a*x[0]+b-x[col])**2 for x in subset)/m
   A=(ab(a)*arb(10).log()).exp();R=(ab(a*Q/2)*arb(10).log()).exp();rms=ab(sq).sqrt()
   channels.append(dict(channel='density' if col==1 else 'stream',slope=str(a),intercept=str(b),A=disp(A),apparent_radius=disp(R),rms=disp(rms)))
  out.append(dict(window_lower=lo,block_count=m,last_block_end=int(subset[-1][0]),channels=channels))
 return out
start=time.monotonic();ctx.prec=256;results=[]
for Q in (7,8):
 for index in range(1,11):
  src=Path('../a4-lead/code/tuned')/f'hhf_Q{Q}h1_root{index}_N{301 if Q==7 else 304}_f64.out'
  assert src.is_file(),(Q,index,str(src));dst=ROOT/'sources'/src.name;dst.write_bytes(src.read_bytes());text=dst.read_text();hdr=text.splitlines()[0];assert f'Q={Q} h=1' in hdr
  prefix=Path(f'research/261_period_seven_eight_prefixes/verification/Q{Q}_root{index}_checks.json.gz');polar=prefix.with_name(f'Q{Q}_root{index}_polar_replay.json.gz')
  longer=Path(f'research/262_tail_response_prefix/verification/Q{Q}_root3_checks.json.gz');longerpolar=longer.with_name(f'Q{Q}_root3_polar_replay.json.gz')
  if index==3 and longer.exists() and longerpolar.exists():prefix,polar=longer,longerpolar
  d=read(prefix);pd=read(polar);assert d['all_checks_pass'] and pd['all_checks_pass'] and pd['source']==ref(prefix)
  rows={};tuning={}
  for line in text.splitlines():
   if line.startswith('n '):
    _,n,f,g=line.split();
    if all(math.isfinite(float(x)) for x in (f,g)):rows[int(n)]=(F(f),F(g))
   elif line.startswith('k '):
    t=line.split();k=int(t[1]);tuning[k]=dict(Rsign=int(t[3]),Rlog=F(t[4]),sigma=F(t[6]),Hsign=int(t[8]),Hlog=F(t[9]))
  logrows=[];harmrows=[]
  for row in d['norms']:
   n=row['n']
   if n not in rows:continue
   for c,col in [('F',0),('G',1)]:
    v=unpack(row[c]).log()/arb(10).log();error=abs(ab(rows[n][col])-v)
    logrows.append(dict(n=n,channel=c,printed=str(rows[n][col]),directed_log=disp(v),absolute_log_discrepancy=disp(error),midpoint_error=float(error.mid())))
  for row in d['harmonics']:
   n=row['n'];k=n//Q
   if k not in tuning:continue
   t=tuning[k];v=unpack(row['sigma']);H=unpack(row['H']);err=abs((ab(t['sigma'])-v)/v);he=abs(ab(t['Hlog'])-abs(H).log()/arb(10).log());sign=1 if H>0 else -1 if H<0 else 0
   harmrows.append(dict(k=k,n=n,relative_sigma_discrepancy=disp(err),sigma_midpoint_error=float(err.mid()),absolute_H_log_discrepancy=disp(he),H_midpoint_error=float(he.mid()),H_sign_agrees=sign==t['Hsign']))
  assert logrows and harmrows
  results.append(dict(Q=Q,root_index=index,source=ref(dst),prefix=ref(prefix),polar=ref(polar),maximum_prefix_order=d['maximum_order'],last_printed_order=max(rows),producer_completed='# done,' in text,log_comparisons=len(logrows),tuning_comparisons=len(harmrows),max_log_discrepancy=max(x['midpoint_error'] for x in logrows),max_relative_sigma_discrepancy=max(x['sigma_midpoint_error'] for x in harmrows),max_H_log_discrepancy=max(x['H_midpoint_error'] for x in harmrows),all_H_signs_agree=all(x['H_sign_agrees'] for x in harmrows),log_rows=logrows,tuning_rows=harmrows,fits=fit(rows,Q)))
  print(json.dumps({k:v for k,v in results[-1].items() if k not in ['log_rows','tuning_rows','fits','source','prefix','polar']}),flush=True)
out=dict(checked_at_utc=now(),metadata_checks_pass=True,scope='Finite floating discrepancies and exact fits of printed decimal data only.',rows=results,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/checks.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0));(ROOT/'sources/floating_period_audit.py').write_bytes(Path(__file__).read_bytes())
for name in ['hh_float.py','fit_hhf.py']:(ROOT/'sources'/name).write_bytes(Path('../a4-lead/code/tuned',name).read_bytes())
print(json.dumps(dict(checked_at_utc=now(),completed_roots=len(results),actual_elapsed_s=out['actual_elapsed_s'])),flush=True)
