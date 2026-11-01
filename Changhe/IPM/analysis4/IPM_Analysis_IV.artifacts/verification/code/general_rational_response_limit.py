"""Direct carrier-limit recurrence and first obstruction for delta=2h/Q."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import tuned_cartesian_exact as ce
root=Path('research/144_general_rational_response_limit');start=time.monotonic();R,b=ring('b',QQ);bs=sp.Symbol('b')
def add(*args):
 out={}
 for a in args:
  for m,v in a.items():out[m]=out.get(m,R.zero)+v
 return {m:v for m,v in out.items() if v}
def scale(a,v):return {m:c*v for m,c in a.items() if c*v}
def mul(a,b):
 out={}
 for m,v in a.items():
  for n,w in b.items():out[m+n]=out.get(m+n,R.zero)+v*w
 return {m:v for m,v in out.items() if v}
def convert(f):
 assert all(a==0 for a,m in f.v)
 return {m:R.from_expr(v.as_expr()) for (a,m),v in f.v.items()}
def serial(a):return {str(m):str(v.as_expr()) for m,v in sorted(a.items())}
def put(name,data):(root/'verification'/name).write_text(json.dumps(data,indent=2)+'\n')
def run(h,Q):
 tick=time.monotonic();delta=QQ(2*h,Q);ce.p=lambda n:1-ce.K(2*h)*n/Q
 ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b)};gg={1:ce.poisson(ff[1])};pairs=0
 for n in range(2,Q+1):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i]);pairs+=1
  ff[n]=acc.scale(ce.K(Q-2*h)/(2*h*(n-1)));ff[n].check_sine()
  if n<Q:gg[n]=ce.poisson(ff[n])
  print(json.dumps(dict(h=h,Q=Q,low_order=n,elapsed_s=time.monotonic()-tick)),flush=True)
 A={j:{m:(QQ(1)-j*delta+m)*v for m,v in convert(ff[j]).items()} for j in ff}
 B={j:{m:(QQ(2)-j*delta+m)*v for m,v in convert(gg[j]).items()} for j in gg}
 U={};V={}
 for r in range(1,Q+1):
  terms=[scale(A[r],QQ(-1,2))]
  for s in range(1,r):terms.extend([mul(U[s],B[r-s]),scale(mul(V[s],A[r-s]),-1)])
  U[r]=scale(add(*terms),1-delta)
  if r<Q:
   assert all(m%2 and m+1-delta*r for m in U[r]);V[r]={m+1:-v/(2*(m+1-delta*r)) for m,v in U[r].items()}
  print(json.dumps(dict(h=h,Q=Q,limit_step=r,offsets=len(U[r]),elapsed_s=time.monotonic()-tick)),flush=True)
 sigma=2*U[Q].get(2*h-1,R.zero);expr=sp.factor(sigma.as_expr());row=dict(h=h,Q=Q,delta=str(delta),c=str(1/(1-delta)),sigma_infinity=str(expr),degree=sigma.degree(),positive_carrier={str(r):serial(u) for r,u in U.items()},low_density={str(n):ce.serial(f) for n,f in ff.items()},low_stream={str(n):ce.serial(g) for n,g in gg.items()},ordered_pairs=pairs,poisson_orders=Q-1)
 if h==1:
  path={3:'research/119_tuned_rational_series/verification/sigma_symbolic_exact.json',4:'research/142_period_four_tuning/verification/symbolic_responses.json',5:'research/130_period_five_tuning/verification/symbolic_responses.json'}[Q];expected=sp.sympify(json.loads(Path(path).read_text())['sigma_infinity']);assert sp.expand(expr-expected)==0;row.update(previous_limit_exactly_equal=True,previous_source=path,previous_source_sha256=sha256(Path(path).read_bytes()).hexdigest())
 else:
  O=sp.Poly(ff[Q].sine(2*h-3).as_expr(),bs,domain=sp.QQ);S=sp.Poly(expr,bs,domain=sp.QQ);gcd=sp.gcd(O,S);fac=sp.factor_list(O)
  row.update(first_obstruction=str(O.as_expr()),obstruction_degree=O.degree(),obstruction_factorization=dict(constant=str(fac[0]),factors=[dict(polynomial=str(v.as_expr()),multiplicity=m) for v,m in fac[1]]),gcd_with_limiting_response=str(gcd.as_expr()),gcd_degree=gcd.degree(),limiting_response_proportional_to_obstruction=sp.rem(S,O).is_zero,real_obstruction_roots=[dict(interval=list(map(str,I)),multiplicity=m) for I,m in sp.polys.polytools.intervals(O,eps=sp.Rational(1,10**30))])
 row['actual_elapsed_s']=time.monotonic()-tick;put('h'+str(h)+'_Q'+str(Q)+'.json',row);return row
try:
 rows=[]
 for h,Q in [(1,3),(1,4),(1,5),(2,9)]:
  row=run(h,Q);rows.append({k:v for k,v in row.items() if k not in ['positive_carrier','low_density','low_stream']});print(json.dumps(rows[-1]),flush=True)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start);put('checks.json',result)
 for name in ['general_rational_response_limit.py','tuned_cartesian_exact.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files))
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
