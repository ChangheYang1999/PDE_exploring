"""Finite directed response audit of producer float64 and longdouble runs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import re,json,gzip,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball,refine_root
from compact_response_bounds import Response
from period_polar_prefix_replay import unpack
from certified_initial_majorants import pack
ROOT=Path('research/264_floating_response_accuracy')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def rat(x):return ball(mpq(str(x)))
def show(x):return x.str(30,radius=True)
start=time.monotonic();ctx.prec=768;results=[];cache={};programs={}
paths=sorted(Path('../a4-lead/code/tuned').glob('hhf_Q*h1_root*_N*.out'))
for src in paths:
 match=re.match(r'hhf_Q([78])h1_root(\d+)_',src.name)
 if not match:continue
 Q,index=map(int,match.groups());dst=ROOT/'sources'/src.name;dst.write_bytes(src.read_bytes());text=dst.read_text();lines=text.splitlines()
 if not lines:continue
 hdr=lines[0];bm=re.search(r'f_1=1:1,3:([^ ]+)',hdr)
 if not bm:continue
 bfloat=F.from_float(float(F(bm[1])));key=(Q,index,str(bfloat));rows={}
 for line in lines:
  if line.startswith('k '):
   v=line.split();rows[int(v[1])]=F(v[6])
 if not rows:continue
 if key not in programs:
  rootdir=Path('research/253_period_seven_tuning' if Q==7 else 'research/256_period_eight_tuning');obs=read(rootdir/'verification/obstruction_checks.json');b,I=refine_root(list(map(int,obs['primitive_coefficients'])),obs['real_roots'][index-1]['interval'],832)
  programs[key]=(Response(1,Q,b),Response(1,Q,rat(bfloat)),I)
 exact,binary,I=programs[key];out=[];overlaps=0;crosschecks=0
 prefix=Path(f'research/261_period_seven_eight_prefixes/verification/Q{Q}_root{index}_checks.json.gz');pd=read(prefix);archived={x['n']//Q:unpack(x['sigma']) for x in pd['harmonics']}
 tail=[k for k in rows if k>=2*Q+1];fullset={min(tail),max(tail)} if tail else set()
 for k,printed in sorted(rows.items()):
  ck=(key,k)
  if ck not in cache:
   if k>=2*Q+1:v=exact.compact(rat(F(1,2*k-2)));w=binary.compact(rat(F(1,2*k-2)))
   else:v=exact.full(k);w=binary.full(k)
   assert v is not None and w is not None and not v.contains(0) and not w.contains(0);cache[ck]=(v,w)
  v,w=cache[ck]
  if k in fullset:
   assert v.overlaps(exact.full(k)) and w.overlaps(binary.full(k));crosschecks+=2
  if k in archived:assert v.overlaps(archived[k]);overlaps+=1
  e=abs((rat(printed)-v)/v);eb=abs((rat(printed)-w)/w);er=abs((w-v)/v)
  out.append(dict(k=k,printed=str(printed),exact_response=pack(v),binary_response=pack(w),relative_exact_discrepancy=show(e),relative_binary_discrepancy=show(eb),relative_root_rounding=show(er),exact_midpoint_error=float(e.mid()),binary_midpoint_error=float(eb.mid()),root_midpoint_effect=float(er.mid())))
 result=dict(source=ref(dst),prefix=ref(prefix),Q=Q,root_index=index,header=hdr,completed='# done,' in text,first_index=min(rows),last_index=max(rows),count=len(out),exact_binary_input=str(bfloat),root_interval=[str(x) for x in I],prefix_response_overlaps=overlaps,full_compact_crosschecks=crosschecks,max_relative_exact_discrepancy=max(x['exact_midpoint_error'] for x in out),max_relative_binary_discrepancy=max(x['binary_midpoint_error'] for x in out),max_relative_root_rounding=max(x['root_midpoint_effect'] for x in out),rows=out)
 results.append(result);print(json.dumps({k:v for k,v in result.items() if k not in ['rows','root_interval','header','exact_binary_input','source','prefix']}),flush=True)
summary=dict(checked_at_utc=stamp(),all_reference_checks_pass=True,bits=768,scope='Finite accuracy of saved tuning responses only; no high-order norm or asymptotic certificate.',results=results,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/checks.json.gz').write_bytes(gzip.compress(json.dumps(summary,separators=(',',':')).encode(),mtime=0))
for name in ['floating_response_accuracy.py','compact_response_bounds.py','pure_cartesian_ball.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
print(json.dumps(dict(at=stamp(),files=len(results),actual_elapsed_s=summary['actual_elapsed_s'])),flush=True)
