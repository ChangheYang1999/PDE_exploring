"""Finite rational positivity certificate for the exact all-k response minimum."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
sys.dont_write_bytecode=True
import sympy as sp
from flint import arb,fmpq,ctx
ctx.prec=512
b,k,t=sp.symbols('b k t');R=sp.Rational
root=Path('research/123_tuned_response_minimum');src=Path('research/119_tuned_rational_series/verification')
start=time.monotonic()
def bounds(e,lo,hi):
 p=sp.Poly(e,b,domain=sp.QQ);a=z=R(0)
 for (n,),v in p.terms():
  a+=v*(lo**n if v>=0 else hi**n);z+=v*(hi**n if v>=0 else lo**n)
 return a,z
def interval_entry(e,lo,hi):
 a,z=bounds(e,lo,hi)
 return dict(polynomial=str(e),lower=str(a),upper=str(z)),a,z
try:
 generic=sp.sympify(json.loads((src/'sigma_symbolic_exact.json').read_text())['sigma']);num,den=map(sp.expand,sp.fraction(generic))
 small={r['k']:sp.sympify(r['sigma']) for r in json.loads((src/'sigma_integer_exact.json').read_text())['rows']}
 sig4=small[4]
 denpoly=sp.Poly(den.subs(k,t+7),t);assert all(c>0 for c in denpoly.all_coeffs())
 target=sp.Poly(sp.expand((sig4*den-num).subs(k,t+7)),t)
 roots=json.loads(Path('research/120_tuned_explicit_radius/verification/response_bound.json').read_text())['rows']
 rows=[]
 for rootrow in roots:
  lo,hi=map(R,rootrow['interval']);s4,l4,u4=interval_entry(sig4,lo,hi);assert u4<0
  sr=[]
  for j in [2,3,5,6]:
   s,l,u=interval_entry(small[j],lo,hi)
   assert l>0 or u<0
   cmp=(small[j] if l>0 else -small[j])+sig4
   c,lc,uc=interval_entry(cmp,lo,hi);assert lc>0,(rootrow['root_index'],j,lc)
   sr.append(dict(k=j,response=s,modulus_gap=c))
  terms=[]
  for (power,),e in target.terms():
   c,l,u=interval_entry(e,lo,hi);assert l>0,(rootrow['root_index'],power,l)
   terms.append(dict(t_degree=power,**c))
  exactrows=json.loads((src/'algebraic_numeric_values.json').read_text())['rows'];wide=exactrows[rootrow['root_index']-1]['root_interval']
  x=arb(fmpq(wide[0])).union(arb(fmpq(wide[1])));v=arb(0)
  for c in sp.Poly(-sig4,b).all_coeffs():v=v*x+arb(fmpq(str(c)))
  rows.append(dict(root_index=rootrow['root_index'],root_interval=rootrow['interval'],sigma4=s4,small_comparisons=sr,tail_positive_coefficients=terms,exact_minimum_polynomial=str(-sig4),minimum_enclosure=v.str(65,radius=True)))
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,minimum_attained_only_at_k=4,denominator_positive_coefficients=[str(x) for x in denpoly.all_coeffs()],rows=rows,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for p in [Path(__file__),src/'sigma_symbolic_exact.json',src/'sigma_integer_exact.json',src/'algebraic_numeric_values.json',Path('research/120_tuned_explicit_radius/verification/response_bound.json')]:
  (root/'sources'/p.name).write_bytes(p.read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,minima=[r['minimum_enclosure'] for r in rows],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno,code=f.line) for f in traceback.extract_tb(exc.__traceback__)])),flush=True)
 raise SystemExit(1)
