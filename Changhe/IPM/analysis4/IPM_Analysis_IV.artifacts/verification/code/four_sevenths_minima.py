"""Fixed-threshold certificates of the three delta4/7 response minima."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,gzip,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball,refine_root
from compact_response_bounds import Response
from taylor_response_enclosure import enclose
from certified_initial_majorants import pack,endpoints
from unpack_dyadic4 import unpack
ROOT=Path('research/247_four_sevenths_exact_minima')
SOURCE=Path('research/239_four_sevenths_two_mode/verification/obstruction_checks.json')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ar(q):return ball(mpq(str(q)))
def ceil(q):return -(-q.numerator//q.denominator)
def range_of(a,b,K):return max(K,ceil((1/b+2)/4)),None if not a else ((1/a+2)/4).__floor__()
def save(path,out):
 raw=json.dumps(out,separators=(',',':')).encode();path.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
def fixed_cover(response,K,U):
 edge=F(1,4*K-2);stack=[(F(0),edge,'')];rows=[];last=time.monotonic()
 while stack:
  a,b,address=stack.pop();lo,hi=range_of(a,b,K);row=dict(a=str(a),b=str(b),address=address,lower=lo,upper=hi)
  if hi is not None and hi<lo:row['status']='empty';rows.append(row);continue
  if hi==lo:
   value=response.compact(ar(F(1,4*lo-2)));assert abs(value)>ar(U),('singleton_not_above_target',lo,str(value),str(U))
   row.update(status='singleton',k=lo,enclosure=pack(value));rows.append(row);continue
  value=enclose(response,a,b,degree=3)
  if value is not None and abs(value)>ar(U):row.update(status='interval',degree=3,enclosure=pack(value));rows.append(row)
  else:
   assert len(address)<80 and len(rows)<10000;mid=(a+b)/2
   stack.extend([(mid,b,address+'1'),(a,mid,address+'0')])
  if time.monotonic()-last>40:
   print(json.dumps(dict(at=stamp(),stage='cover',leaves=len(rows),pending=len(stack))),flush=True);last=time.monotonic()
 return rows

def main():
 start=time.monotonic();replay='--replay' in sys.argv;ctx.prec=1536 if replay else 1024;ball.cache_clear()
 raw=SOURCE.read_bytes();src=json.loads(raw);assert src['all_checks_pass'];pol=list(map(int,src['primitive_coefficients']));results=[]
 for i,(m,K) in enumerate([(4,16),(8,24),(6,16)],1):
  begin=time.monotonic();b,I=refine_root(pol,src['real_roots'][i-1]['interval'],ctx.prec+64);response=Response(2,7,b)
  target=abs(response.full(m));U=endpoints(target)[1];assert U>0
  path=ROOT/f'verification/root{i}.json.gz'
  if replay:
   frozen=path.read_bytes();data=json.loads(gzip.decompress(frozen));assert data['all_checks_pass'];U=F(data['target_upper']);assert target<=ar(U)
   rows=data['leaves'];oldfinite={x['k']:x for x in data['finite']}
  else:rows=None;oldfinite=None
  finite=[]
  for k in range(1,K):
   value=response.full(k)
   if k!=m:assert abs(value)>ar(U),('finite_not_above_target',i,k)
   if oldfinite:assert value.overlaps(arb(*unpack(oldfinite[k]['enclosure'])))
   finite.append(dict(k=k,enclosure=pack(value)))
  if not replay:rows=fixed_cover(response,K,U)
  else:
   edge=F(1,4*K-2);ordered=[]
   for row in rows:
    address=row['address'];den=2**len(address);num=int(address,2) if address else 0;a=edge*num/den;c=edge*(num+1)/den
    assert (str(a),str(c))==(row['a'],row['b']);assert range_of(a,c,K)==(row['lower'],row['upper'])
    lo,hi=row['lower'],row['upper'];status=row['status']
    if status=='empty':assert hi is not None and hi<lo
    else:
     if status=='singleton':assert hi==lo==row['k'];value=response.compact(ar(F(1,4*lo-2)))
     else:assert status=='interval' and row['degree']==3;value=enclose(response,a,c,degree=3)
     assert abs(value)>ar(U) and value.overlaps(arb(*unpack(row['enclosure'])))
    ordered.append((a,c))
   ordered.sort();assert ordered[0][0]==0 and ordered[-1][1]==edge and all(x[1]==y[0] for x,y in zip(ordered,ordered[1:]))
  counts={s:sum(x['status']==s for x in rows) for s in ['empty','singleton','interval']}
  result=dict(checked_at_utc=stamp(),all_checks_pass=True,root=i,minimizing_index=m,K=K,bits=ctx.prec,target=pack(target),target_display=target.str(45,radius=True),target_upper=str(U),root_interval=I,finite=finite,leaves=rows,leaf_counts=counts,actual_elapsed_s=time.monotonic()-begin)
  if replay:result['construction_sha256']=sha256(frozen).hexdigest();path=ROOT/f'verification/root{i}_replay.json.gz'
  save(path,result);results.append({k:v for k,v in result.items() if k not in ['target','target_upper','root_interval','finite','leaves']});print(json.dumps(results[-1]),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,replay=replay,roots=results,source=dict(path=str(SOURCE),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 save(ROOT/('verification/review.json' if replay else 'verification/checks.json'),out)
 for name in ['four_sevenths_minima.py','taylor_response_enclosure.py','compact_response_bounds.py','pure_cartesian_ball.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(out),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  save(ROOT/'verification/FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
