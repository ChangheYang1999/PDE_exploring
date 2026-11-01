"""Certify P9 roots and compute a two-coefficient all-k response criterion."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Fr
import json,sys,time
sys.dont_write_bytecode=True
import sympy as sp
from flint import nmod_poly
import tuned_cartesian_exact as ce
from exact_polynomial_certificates import *
root=Path('research/146_four_ninths_profiles');start=time.monotonic();bs,ks=sp.symbols('b k');ce.p=lambda n:1-ce.K(4)*n/9
src=Path('research/144_general_rational_response_limit/verification/h2_Q9.json');source=json.loads(src.read_text());O=sp.Poly(sp.sympify(source['first_obstruction']),bs,domain=sp.QQ);O0=ce.K(int(O.nth(0).p))/int(O.nth(0).q);O9=ce.K(int(O.nth(9).p))/int(O.nth(9).q)
def put(name,data):
 (root/'verification'/name).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(dict(stage=name,elapsed_s=time.monotonic()-start)),flush=True)
def algebraic():
 P=primitive([Fr(str(O.nth(i))) for i in range(10)])
 if P[-1]<0:P=[-x for x in P]
 seq=sturm(P);assert len(seq[-1])==1;vi=[sturm_infinity(seq,n) for n in [True,False]];rows=[]
 for rr in source['real_obstruction_roots']:
  lo,hi=map(Fr,rr['interval']);v=[sturm_finite(seq,x) for x in [lo,hi]];assert v[0]-v[1]==1;rows.append(dict(interval=rr['interval'],approx=float((lo+hi)/2),variations=v))
 assert vi[0]-vi[1]==len(rows)==5
 possible=set(range(1,9));mods=[]
 for p in range(2,200):
  if not isprime(p) or P[-1]%p==0:continue
  facs=nmod_poly([c%p for c in P],p).factor()[1]
  if any(int(m)!=1 for f,m in facs):continue
  prod=[1];degs=[];fproof=[]
  for f,m in facs:
   a=modtrim(f.coeffs(),p);fproof.append(irreducibility_certificate(a,p));degs.append(len(a)-1);prod=modmul(prod,a,p)
  target=modtrim(P,p);scalar=target[-1]*pow(prod[-1],-1,p)%p;assert modtrim([scalar*x for x in prod],p)==target
  subsets={0}
  for d in degs:subsets|={x+d for x in tuple(subsets)}
  narrowed=possible&subsets
  if narrowed!=possible:mods.append(dict(prime=p,factor_degrees=degs,scalar=scalar,factors=fproof,remaining_proper_degrees=sorted(narrowed)))
  possible=narrowed
  if not possible:break
 assert not possible
 S=sp.Poly(sp.sympify(source['sigma_infinity']),bs,domain=sp.QQ);chain=[list(map(Fr,P)),[Fr(str(S.nth(i))) for i in range(S.degree()+1)]]
 while chain[-1]:
  rem=remainder(chain[-2],chain[-1])
  if not rem:break
  chain.append(list(map(Fr,primitive(rem))))
 assert len(chain[-1])==1
 put('algebraic_certificates.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source_sha256=sha256(src.read_bytes()).hexdigest(),primitive_coefficients=list(map(str,P)),sturm_sequence=[list(map(str,a)) for a in seq],infinity_variations=vi,real_roots=rows,modular_irreducibility=mods,limit_coprime_remainder_chain=[list(map(str,a)) for a in chain],actual_elapsed_s=time.monotonic()-start))
def low(mode):
 ff={1:ce.sine(ce.p(1),mode)};gg={1:ce.poisson(ff[1])}
 for n in range(2,10):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i])
  ff[n]=acc.scale(ce.K(5)/(4*(n-1)));ff[n].check_sine()
  if n<9:gg[n]=ce.poisson(ff[n])
 assert ff[9].sine(1)==ce.R(O0 if mode==1 else O9)
 return ff,gg
def response(t,ff,gg,mode):
 n=9*t;symbolic=t==ce.k;e=ce.sine(ce.p(n)+1,(4,-2) if symbolic else 4*int(t)-2);ph={};ps={}
 for r in range(1,10):
  acc=ce.adv(e,ff[r])
  for s in range(1,r):acc=acc+ce.adv(gg[r-s],ph[s])+ce.adv(ps[s],ff[r-s])
  ph[r]=acc.scale(ce.K(5)/(4*(n+r-1)));ph[r].check_sine()
  if r<9:ps[r]=ce.poisson(ph[r])
  if symbolic:put('mode'+str(mode)+'_symbolic_step'+str(r)+'.json',dict(step=r,density=ce.serial(ph[r]),stream=ce.serial(ps[r]) if r<9 else None))
 return 2*ph[9].v.get((4,1) if symbolic else (0,4*int(t)+1),ce.R.zero)
try:
 algebraic();mode_results={};generic={};small={}
 for mode in [1,3]:
  ff,gg=low(mode);rows=[]
  for t in range(1,12):
   sig=response(t,ff,gg,mode);rows.append(dict(k=t,sigma=str(sig.as_expr())));print(json.dumps(dict(mode=mode,k=t,elapsed_s=time.monotonic()-start)),flush=True)
  small[mode]=rows;put('mode'+str(mode)+'_small.json',dict(rows=rows))
  sig=response(ce.k,ff,gg,mode);expr=sp.factor(sig.as_expr())
  for t in [10,11]:assert sp.cancel(expr.subs(ks,t)-sp.sympify(rows[t-1]['sigma']))==0
  lim=sp.factor(sp.limit(expr,ks,sp.oo));full_limit=sp.Poly(sp.sympify(source['sigma_infinity']),bs,domain=sp.QQ);expected=full_limit.nth(0 if mode==1 else 9);assert lim==expected
  generic[mode]=sig;put('mode'+str(mode)+'_generic.json',dict(sigma=str(expr),limit=str(lim),limit_matches_direct_carrier=True,tail_starts_at=10,direct_comparisons=[10,11],actual_elapsed_s=time.monotonic()-start))
 crit=sp.factor((generic[1]*O9-generic[3]*O0).as_expr());num,den=sp.fraction(crit);N=sp.Poly(num,ks,domain=sp.QQ);D=sp.Poly(den,ks,domain=sp.QQ)
 if D.LC()<0:N=-N;D=-D
 finite=[]
 for t in range(1,10):
  val=sp.cancel(O.nth(9)*sp.sympify(small[1][t-1]['sigma'])-O.nth(0)*sp.sympify(small[3][t-1]['sigma']));assert val!=0;finite.append(dict(k=t,D=str(val)))
 roots=sp.polys.polytools.ground_roots(N);integer_roots=[int(r) for r in roots if r.q==1 and r>=10];assert not integer_roots
 droots=sp.polys.polytools.ground_roots(D);assert not [r for r in droots if r.q==1 and r>=10]
 trials=[];success=None
 for K in [10,16,24,32,48,64,96,128,256,512,1024]:
  ncoeff=N.shift(K).all_coeffs();dcoeff=D.shift(K).all_coeffs();sn=1 if ncoeff[0]>0 else -1;sd=1 if dcoeff[0]>0 else -1
  ok=all(sn*x>=0 for x in ncoeff) and sn*ncoeff[-1]>0 and all(sd*x>=0 for x in dcoeff) and sd*dcoeff[-1]>0;trials.append(dict(K=K,passes=ok))
  if ok:success=dict(K=K,numerator_sign=sn,denominator_sign=sd,numerator_coefficients=list(map(str,ncoeff)),denominator_coefficients=list(map(str,dcoeff)));break
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),criterion=str(crit),numerator_degree=N.degree(),denominator_degree=D.degree(),finite_checks=finite,numerator_rational_roots={str(k):int(v) for k,v in roots.items()},denominator_rational_roots={str(k):int(v) for k,v in droots.items()},no_integer_zeros_or_poles_from_10=True,tail_positive_certificate=success,tail_trials=trials,actual_elapsed_s=time.monotonic()-start);put('criterion_checks.json',result)
 for name in ['four_ninths_responses.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files))
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
