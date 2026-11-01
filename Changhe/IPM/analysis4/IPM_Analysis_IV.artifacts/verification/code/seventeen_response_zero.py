"""Taylor certificate for the sin17 response crossing between indices2379 and2380."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from extremal_single_probe import ExtremalResponse
from pure_cartesian_ball import ball
from taylor_response_enclosure import Jet
from certified_initial_majorants import pack
from unpack_dyadic4 import unpack
ROOT=Path('research/252_seventeen_response_zero')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ar(q):return ball(mpq(str(q)))
def bound(response,a,b):
 m=(a+b)/2;r=(b-a)/2
 center=response.compact(Jet([ar(m),arb(1)],3))
 whole=response.compact(Jet([ar(a).union(ar(b)),arb(1)],3))
 assert isinstance(center,Jet) and isinstance(whole,Jet)
 value=center.c[1]+2*center.c[2]*ar(-r).union(ar(r))+3*whole.c[3]*arb(0).union(ar(r*r))
 return value

def main():
 started=time.monotonic();replay='--replay' in sys.argv;ctx.prec=1536 if replay else 1024
 ball.cache_clear();response=ExtremalResponse(3,13);a=F(1,14278);b=F(1,14272)
 left=response.compact(ar(a));right=response.compact(ar(b));assert left>0 and right<0
 path=ROOT/'verification/uniqueness_checks.json'
 if replay:
  raw=path.read_bytes();src=json.loads(raw);assert src['all_checks_pass']
  rows=src['leaves'];last=a
  for row in rows:
   x,y=F(row['a']),F(row['b']);assert x==last and x<y
   value=bound(response,x,y);assert value<0 and value.overlaps(arb(*unpack(row['derivative'])))
   last=y
  assert last==b
  out=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=1536,leaves_replayed=len(rows),unique_zero=True,receipt=dict(path=str(path),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-started)
  path=ROOT/'verification/uniqueness_replay.json'
 else:
  stack=[(a,b,0)];rows=[]
  while stack:
   x,y,depth=stack.pop();value=bound(response,x,y)
   if value<0:rows.append(dict(a=str(x),b=str(y),depth=depth,derivative=pack(value),display=value.str(35,radius=True)))
   else:
    assert depth<16,('maximum_depth',str(x),str(y),str(value));m=(x+y)/2
    stack.extend([(m,y,depth+1),(x,m,depth+1)])
   print(json.dumps(dict(at=stamp(),accepted=len(rows),pending=len(stack),depth=depth)),flush=True)
  out=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=1024,a=str(a),b=str(b),left=pack(left),right=pack(right),leaves=rows,unique_zero=True,real_index_interval=[2379,2380],left_display=left.str(50,radius=True),right_display=right.str(50,radius=True),all_denominators_separated=True,actual_elapsed_s=time.monotonic()-started)
 path.write_text(json.dumps(out,indent=2)+'\n')
 for name in ['seventeen_response_zero.py','taylor_response_enclosure.py','extremal_single_probe.py','compact_response_bounds.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['leaves','left','right']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/uniqueness_FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
