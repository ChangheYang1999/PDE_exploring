"""Independent exact first compatibility obstruction at delta=2/5."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
import tuned_cartesian_exact as ce
root=Path('research/130_period_five_tuning');start=time.monotonic()
ce.p=lambda n:1-ce.K(2)*n/5
bs=sp.Symbol('b')
try:
 ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b)};gg={1:ce.poisson(ff[1])}
 counts=dict(poisson_orders=1,ordered_pairs=0,symmetry_orders=1)
 for n in range(2,11):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i]);counts['ordered_pairs']+=1
  ff[n]=acc.scale(ce.K(3)/(2*(n-1)));ff[n].check_sine();counts['symmetry_orders']+=1
  assert all(a==0 and abs(m)<=4*n-1 and m%2 for a,m in ff[n].v)
  if n<10:gg[n]=ce.poisson(ff[n]);counts['poisson_orders']+=1
  print(json.dumps(dict(n=n,elapsed_s=time.monotonic()-start)),flush=True)
 O=sp.Poly(ff[10].sine(1).as_expr(),bs,domain=sp.QQ)
 assert O.degree()<=10
 factor=sp.factor_list(O);ints=sp.polys.polytools.intervals(O,eps=sp.Rational(1,10**30))
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,delta='2/5',c='5/3',O10=str(O.as_expr()),degree=O.degree(),coefficients_ascending=[str(O.nth(i)) for i in range(O.degree()+1)],factorization=dict(constant=str(factor[0]),factors=[dict(polynomial=str(v.as_expr()),multiplicity=m) for v,m in factor[1]]),real_roots=[dict(interval=[str(a),str(b)],multiplicity=m) for (a,b),m in ints],counts=counts,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/obstruction_checks.json').write_text(json.dumps(result,indent=2)+'\n')
 (root/'verification/exact_prefix.json').write_text(json.dumps(dict(density={str(n):ce.serial(v) for n,v in ff.items()},stream={str(n):ce.serial(v) for n,v in gg.items()}),indent=2)+'\n')
 for name in ['period_five_exact.py','tuned_cartesian_exact.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(result),flush=True)
except Exception as e:
 import traceback
 result=dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)],actual_elapsed_s=time.monotonic()-start)
 (root/'verification/FAILURE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);raise SystemExit(1)
