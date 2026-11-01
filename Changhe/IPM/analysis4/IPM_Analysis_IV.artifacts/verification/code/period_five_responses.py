"""Exact Q=5 resonant responses, independent Cartesian implementation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import ast,json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
import tuned_cartesian_exact as ce
ce.p=lambda n:1-ce.K(2)*n/5
root=Path('research/130_period_five_tuning');start=time.monotonic();bs,ks=sp.symbols('b k')
def save(name,data):
 (root/'verification'/name).write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(dict(stage=name,elapsed_s=time.monotonic()-start)),flush=True)
def loadfield(data):return ce.F(ce.K.from_expr(sp.sympify(data['radial_exponent'])),{ast.literal_eval(m):ce.R.from_expr(sp.sympify(v)) for m,v in data['signed_laurent'].items()})
def response(t,F,G):
 n=5*t;freq=(2,-2) if t==ce.k else 2*int(t)-2;e=ce.sine(ce.p(n)+1,freq);phi={};gp={}
 for r in range(1,6):
  acc=ce.adv(e,F[r])
  for s in range(1,r):acc=acc+ce.adv(G[r-s],phi[s])+ce.adv(gp[s],F[r-s])
  phi[r]=acc.scale(ce.K(3)/(2*(n+r-1)));phi[r].check_sine()
  if r<5:gp[r]=ce.poisson(phi[r])
  if t==ce.k:save('symbolic_response_step'+str(r)+'.json',dict(step=r,field=ce.serial(phi[r]),stream=ce.serial(gp[r]) if r<5 else None))
 key=(2,-1) if t==ce.k else (0,2*int(t)-1)
 return 2*phi[5].v.get(key,ce.R.zero),phi
try:
 raw=json.loads((root/'verification/exact_prefix.json').read_text());F={n:loadfield(raw['density'][str(n)]) for n in range(1,6)};G={n:loadfield(raw['stream'][str(n)]) for n in range(1,5)}
 small=[]
 for k0 in range(2,13):
  sig,phi=response(k0,F,G);expr=sp.factor(sig.as_expr());poly=sp.Poly(expr,bs,domain=sp.QQ)
  small.append(dict(k=k0,sigma=str(expr),degree=poly.degree(),nonzero=not poly.is_zero))
  save('small_responses.json',dict(rows=small))
 sig,phi=response(ce.k,F,G);expr=sp.factor(sig.as_expr());num,den=sp.fraction(expr)
 for k0 in range(11,13):assert sp.cancel(expr.subs(ks,k0)-sp.sympify(small[k0-2]['sigma']))==0
 for ph in phi.values():
  for slope,offset in ph.v:
   assert abs(slope)==2 and abs(offset+2 if slope==2 else -offset+2)<=19
 np=sp.Poly(num,bs);common=sp.gcd_list(np.all_coeffs());ground=sp.polys.polytools.ground_roots(sp.Poly(common,ks,domain=sp.QQ));integerzeros=[int(r) for r in ground if r.q==1 and r>=11]
 limit=sp.factor(sp.limit(expr,ks,sp.oo));assert not limit.has(sp.oo,-sp.oo,sp.zoo);lp=sp.Poly(limit,bs,domain=sp.QQ)
 O=sp.Poly(sp.sympify(json.loads((root/'verification/obstruction_checks.json').read_text())['O10']),bs,domain=sp.QQ)
 checks=[dict(k=r['k'],gcd_degree=sp.gcd(O,sp.Poly(sp.sympify(r['sigma']),bs)).degree()) for r in small]
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),sigma=str(expr),numerator=str(num),denominator=str(den),numerator_degree_b=np.degree(),common_numerator_coefficient_factor=str(sp.factor(common)),rational_zeros_of_common_factor={str(r):int(m) for r,m in ground.items()},integer_common_zeros_at_or_above11=integerzeros,sigma_infinity=str(limit),limit_degree=lp.degree(),limit_gcd_obstruction_degree=sp.gcd(O,lp).degree(),small_gcd_checks=checks,small_nonzero=all(r['nonzero'] for r in small),limit_nonzero=not lp.is_zero,tail_comparisons_at_11_12_pass=True,actual_elapsed_s=time.monotonic()-start)
 save('symbolic_responses.json',result)
 for name in ['period_five_responses.py','tuned_cartesian_exact.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['sigma','numerator','denominator']}),flush=True)
except Exception as e:
 import traceback
 result=dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)],actual_elapsed_s=time.monotonic()-start)
 save('RESPONSE_FAILURE.json',result);raise SystemExit(1)
