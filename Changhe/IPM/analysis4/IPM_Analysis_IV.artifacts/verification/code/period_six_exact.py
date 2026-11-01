"""Independent Cartesian obstruction and symbolic resonant response for Q=6."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
import tuned_cartesian_exact as ce
Q=6;K0=13;ce.p=lambda n:1-ce.K(2)*n/Q
root=Path('research/154_period_six_tuning');start=time.monotonic();bs,ks=sp.symbols('b k')
def save(name,data):
 (root/'verification'/name).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(dict(stage=name,elapsed_s=time.monotonic()-start)),flush=True)
def response(t,F,G):
 n=Q*t;freq=(2,-2) if t==ce.k else 2*int(t)-2;e=ce.sine(ce.p(n)+1,freq);phi={};gp={}
 for r in range(1,Q+1):
  acc=ce.adv(e,F[r])
  for s in range(1,r):acc=acc+ce.adv(G[r-s],phi[s])+ce.adv(gp[s],F[r-s])
  phi[r]=acc.scale(ce.K(Q-2)/(2*(n+r-1)));phi[r].check_sine()
  if r<Q:gp[r]=ce.poisson(phi[r])
  if t==ce.k:save('symbolic_response_step'+str(r)+'.json',dict(step=r,field=ce.serial(phi[r]),stream=ce.serial(gp[r]) if r<Q else None))
 key=(2,-1) if t==ce.k else (0,2*int(t)-1)
 return 2*phi[Q].v.get(key,ce.R.zero),phi
try:
 ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b)};gg={1:ce.poisson(ff[1])};counts=dict(poisson_orders=1,ordered_pairs=0,symmetry_orders=1)
 for n in range(2,2*Q+1):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i]);counts['ordered_pairs']+=1
  ff[n]=acc.scale(ce.K(Q-2)/(2*(n-1)));ff[n].check_sine();counts['symmetry_orders']+=1
  assert all(a==0 and abs(m)<=4*n-1 and m%2 for a,m in ff[n].v)
  if n<2*Q:gg[n]=ce.poisson(ff[n]);counts['poisson_orders']+=1
 O=sp.Poly(ff[2*Q].sine(1).as_expr(),bs,domain=sp.QQ);factor=sp.factor_list(O);ints=sp.polys.polytools.intervals(O,eps=sp.Rational(1,10**30))
 save('obstruction_checks.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,delta='1/3',c='3/2',O12=str(O.as_expr()),degree=O.degree(),coefficients_ascending=[str(O.nth(i)) for i in range(O.degree()+1)],factorization=dict(constant=str(factor[0]),factors=[dict(polynomial=str(v.as_expr()),multiplicity=m) for v,m in factor[1]]),real_roots=[dict(interval=[str(a),str(b)],multiplicity=m) for (a,b),m in ints],counts=counts,actual_elapsed_s=time.monotonic()-start))
 save('exact_prefix.json',dict(density={str(n):ce.serial(v) for n,v in ff.items()},stream={str(n):ce.serial(v) for n,v in gg.items()}))
 small=[]
 for k0 in range(2,K0+6):
  sig,phi=response(k0,ff,gg);expr=sp.factor(sig.as_expr());poly=sp.Poly(expr,bs,domain=sp.QQ)
  small.append(dict(k=k0,sigma=str(expr),degree=poly.degree() if not poly.is_zero else None,nonzero=not poly.is_zero,gcd_obstruction_degree=sp.gcd(O,poly).degree()))
  save('small_responses.json',dict(rows=small))
 sig,phi=response(ce.k,ff,gg);expr=sp.factor(sig.as_expr());num,den=sp.fraction(expr)
 for k0 in range(K0,K0+6):assert sp.cancel(expr.subs(ks,k0)-sp.sympify(small[k0-2]['sigma']))==0
 for ph in phi.values():
  for slope,offset in ph.v:assert abs(slope)==2 and abs(offset+2 if slope==2 else -offset+2)<=4*Q-1
 np=sp.Poly(num,bs);common=sp.gcd_list(np.all_coeffs());ground=sp.polys.polytools.ground_roots(sp.Poly(common,ks,domain=sp.QQ));integerzeros=[int(r) for r in ground if r.q==1 and r>=K0]
 limit=sp.factor(sp.limit(expr,ks,sp.oo));assert not limit.has(sp.oo,-sp.oo,sp.zoo);lp=sp.Poly(limit,bs,domain=sp.QQ)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),sigma=str(expr),numerator=str(num),denominator=str(den),numerator_degree_b=np.degree(),common_numerator_coefficient_factor=str(sp.factor(common)),rational_zeros_of_common_factor={str(r):int(m) for r,m in ground.items()},integer_common_zeros_in_tail=integerzeros,sigma_infinity=str(limit),limit_degree=lp.degree() if not lp.is_zero else None,limit_gcd_obstruction_degree=sp.gcd(O,lp).degree(),small_nonzero=all(r['nonzero'] for r in small),limit_nonzero=not lp.is_zero,tail_comparisons_pass=True,tail_starts_at=K0,actual_elapsed_s=time.monotonic()-start)
 save('symbolic_responses.json',result)
 for name in ['period_six_exact.py','tuned_cartesian_exact.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};save('MANIFEST.json',dict(files=files))
 print(json.dumps({k:v for k,v in result.items() if k not in ['sigma','numerator','denominator']}),flush=True)
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);save('FAILURE.json',fail);raise SystemExit(1)
