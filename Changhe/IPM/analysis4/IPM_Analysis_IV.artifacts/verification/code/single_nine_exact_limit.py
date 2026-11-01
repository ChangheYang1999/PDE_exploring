"""Exact t=0 limiting response, independent rational polynomial recurrence."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq as Q,arb,ctx
from gmpy2 import mpq
from extremal_single_exact import ExactSingle
from extremal_single_probe import ExtremalResponse
from pure_cartesian_ball import ball
from certified_initial_majorants import pack
from unpack_dyadic4 import unpack
ROOT=Path('research/265_single_nine_exact_limit')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def terms(p):
 assert len(p.a)<=1
 return {j-p.M:v for j,v in enumerate(p.a[0].coeffs()) if v} if p.a else {}
def plus(*ps):
 out={}
 for p in ps:
  for m,v in p.items():out[m]=out.get(m,Q(0))+v
 return {m:v for m,v in out.items() if v}
def scale(p,a):return {m:v*a for m,v in p.items() if v*a}
products=0
def times(p,q):
 global products
 out={}
 for m,v in p.items():
  for n,w in q.items():out[m+n]=out.get(m+n,Q(0))+v*w;products+=1
 return {m:v for m,v in out.items() if v}
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def main():
 started=time.monotonic();ctx.prec=1536
 exact=ExactSingle(2,7);exact.initialize();delta=Q(4,7)
 A={r:terms(exact.FX[r]+exact.FY[r]) for r in range(1,8)}
 C={r:terms(exact.GX[r]+exact.GY[r]) for r in range(1,7)}
 U={};V={}
 for r in range(1,8):
  total=scale(A[r],Q(-1,2))
  for s in range(1,r):total=plus(total,scale(times(V[s],A[r-s]),-1),times(U[s],C[r-s]))
  U[r]={m+1:(1-delta)*v for m,v in total.items()}
  if r<7:
   V[r]={}
   for m,v in U[r].items():
    den=2*(m+1-delta*r);assert den;V[r][m+1]=-v/den
 value=2*U[7].get(3,Q(0));fresh=ExtremalResponse(2,7);count=0
 for n in range(1,8):
  for m,v in terms(exact.F[n]).items():assert fresh.f[n].coefficient(m).contains(ball(mpq(str(v))));count+=1
  if n<7:
   for m,v in terms(exact.G[n]).items():assert fresh.g[n].coefficient(m).contains(ball(mpq(str(v))));count+=1
 limit=fresh.compact(arb(0));value_ball=ball(mpq(str(value)));assert limit.overlaps(value_ball)
 p=Path('research/231_extremal_single_harmonics/verification/h2_Q7_probe.json');old=json.loads(p.read_text());oldlim=arb(*unpack(old['limit']));assert oldlim.contains(value_ball)
 proposed=(F(5,10**9),F(9,10**8));v=F(str(value));outside=not(proposed[0]<=v<=proposed[1]);assert outside and v>proposed[1]
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,h=2,Q=7,mode=9,exact_limit=str(value),display=value_ball.str(80,radius=True),fresh_limit=pack(limit),old_limit=old['limit'],old_contains_exact=True,fresh_overlaps_exact=True,independent_prefix_coefficients=count,rational_scalar_products=products,proposed_fit_range=list(map(str,proposed)),exact_limit_above_fit_range=True,ratio_to_fit_upper=str(v/proposed[1]),arithmetic_bits=1536,source=ref(p),actual_elapsed_s=time.monotonic()-started)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['single_nine_exact_limit.py','extremal_single_exact.py','laurent_log_audit.py','extremal_single_probe.py','compact_response_bounds.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['exact_limit','fresh_limit','old_limit','ratio_to_fit_upper']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
