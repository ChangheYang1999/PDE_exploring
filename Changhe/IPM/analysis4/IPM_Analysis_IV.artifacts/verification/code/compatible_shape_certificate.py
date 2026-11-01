"""Exact Cartesian obstruction polynomial and explicit analytic shape disk."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,time,json
sys.dont_write_bytecode=True
import sympy as sp
from sympy.polys.rings import ring
from flint import arb,fmpq,ctx
import tuned_cartesian_exact as ce
ctx.prec=768
R,b,tau=ring('b,tau',ce.K.to_domain());ce.R=R;ce.b=b;ce.MOD=None
root=Path('research/125_explicit_compatible_shape');start=time.monotonic()
bs,ts,x=sp.symbols('b tau x')

def bs_eval(expr,ball):
 out=arb(0)
 for c in sp.Poly(expr,bs).all_coeffs():out=out*ball+arb(fmpq(str(c)))
 return out
try:
 ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,b)+ce.sine(ce.p(1),5,tau)};gg={1:ce.poisson(ff[1])}
 for n in range(2,7):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i])
  ff[n]=acc.scale(ce.K(1)/(2*(n-1)));ff[n].check_sine()
  assert all(a==0 and abs(m)<=6*n-1 for a,m in ff[n].v)
  if n<6:gg[n]=ce.poisson(ff[n])
  print(json.dumps(dict(stage='Cartesian_order',n=n,elapsed_s=time.monotonic()-start)),flush=True)
 O=sp.Poly(ff[6].sine(1).as_expr(),bs,ts,domain=sp.QQ)
 old=sp.sympify(json.loads(Path('research/119_tuned_rational_series/verification/o6_exact.json').read_text())['O6'])
 assert sp.cancel(O.as_expr().subs(ts,0)-old)==0
 assert O.total_degree()<=6
 (root/'verification/obstruction_polynomial.json').write_text(json.dumps(dict(total_degree=O.total_degree(),terms=[dict(b_degree=i,tau_degree=j,coefficient=str(c)) for (i,j),c in O.terms()],expression=str(O.as_expr()),restriction_tau_zero_matches=True),indent=2)+'\n')
 raw=json.loads(Path('research/120_tuned_explicit_radius/verification/response_bound.json').read_text())['rows']
 exact=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json').read_text())['rows']
 rows=[];h=sp.Rational(1,10**13);profile_radius=sp.Rational(1,790272000000)
 for index,r in enumerate(raw):
  lo,hi=map(sp.Rational,r['interval']);mid=(lo+hi)/2;width=(hi-lo)/2
  shift=sp.Poly(O.as_expr().subs(bs,mid+x),x,ts,domain=sp.QQ);A=shift.coeff_monomial(x);assert A!=0 and width<h
  trials=[]
  for exponent in range(1,31):
   t0=sp.Rational(1,10**exponent)
   bound=sum(abs(c)*h**i*t0**j for (i,j),c in shift.terms() if (i,j)!=(1,0))
   passed=bool(bound<abs(A)*h and h+width+t0<profile_radius)
   trials.append(dict(decimal_exponent=exponent,nonlinear_bound=str(bound),linear_bound=str(abs(A)*h),profile_distance_bound=str(h+width+t0),passes=passed))
   if passed:break
  assert passed
  interval=exact[index]['root_interval'];ball=arb(fmpq(interval[0])).union(arb(fmpq(interval[1])))
  O_b=sp.diff(O.as_expr(),bs).subs(ts,0);O_t=sp.diff(O.as_expr(),ts).subs(ts,0)
  deriv=-bs_eval(O_t,ball)/bs_eval(O_b,ball)
  rows.append(dict(root_index=index+1,root_interval=r['interval'],center=str(mid),h=str(h),t0=str(t0),linear_coefficient=str(A),circle_ratio=str(sp.cancel(bound/(abs(A)*h))),profile_distance_bound=str(h+width+t0),profile_radius=str(profile_radius),tangent_enclosure=deriv.str(65,radius=True),shifted_coefficients=[dict(x_degree=i,tau_degree=j,coefficient=str(c)) for (i,j),c in shift.terms()],trials=trials))
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for src in [Path(__file__),Path('code/tuned_cartesian_exact.py'),Path('research/120_tuned_explicit_radius/verification/response_bound.json')]:
  (root/'sources'/src.name).write_bytes(src.read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_exact_checks_pass=True,rows=[{k:r[k] for k in ['root_index','t0','tangent_enclosure']} for r in rows],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno,code=f.line) for f in traceback.extract_tb(exc.__traceback__)])),flush=True)
 raise SystemExit(1)
