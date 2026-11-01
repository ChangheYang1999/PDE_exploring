"""Independent Cartesian obstruction, Sturm and modular checks at delta1/4."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
from flint import nmod_poly
import tuned_cartesian_exact as ce
from exact_polynomial_certificates import primitive,sturm,sturm_finite,sturm_infinity,evaluate,modtrim,modmul,irreducibility_certificate,isprime
ROOT=Path('research/256_period_eight_tuning')
ce.p=lambda n:1-ce.K(1)*n/4
b=sp.Symbol('b')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b)};gg={1:ce.poisson(ff[1])}
 for n in range(2,17):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i])
  ff[n]=acc.scale(ce.K(3)/(n-1));ff[n].check_sine();assert all(a==0 and m%2 and abs(m)<=4*n-1 for a,m in ff[n].v)
  if n<16:gg[n]=ce.poisson(ff[n])
  print(json.dumps(dict(at=stamp(),stage='exact_order',n=n,actual_elapsed_s=time.monotonic()-start)),flush=True)
 O=sp.Poly(ff[16].sine(1).as_expr(),b,domain=sp.QQ);assert O.degree()==16
 P=primitive([F(str(O.nth(i))) for i in range(17)])
 if P[-1]<0:P=[-x for x in P]
 source=Path('../a4-lead/code/tuned/tq_cert_Q8.log');raw=source.read_bytes();lines=raw.decode().splitlines()
 lead=sp.Poly(sp.sympify(next(s.split(' P = ',1)[1] for s in lines if s.startswith('Q = 8 '))),b,domain=sp.QQ)
 scale=sp.sympify(next(s.split('O_2Q = P * ',1)[1] for s in lines if s.startswith('O_2Q = P * ')))
 assert lead==sp.Poly(sum(sp.Integer(v)*b**i for i,v in enumerate(P)),b,domain=sp.QQ) and sp.expand(O.as_expr()-lead.as_expr()*scale)==0
 seq=sturm(P);infinity=[sturm_infinity(seq,neg) for neg in [True,False]];roots=[]
 for interval,multiplicity in sp.polys.polytools.intervals(lead,eps=sp.Rational(1,10**60)):
  lo,hi=map(lambda x:F(str(x)),interval);v=[sturm_finite(seq,x) for x in [lo,hi]];assert multiplicity==1 and v[0]-v[1]==1 and evaluate(P,lo) and evaluate(P,hi)
  roots.append(dict(interval=list(map(str,[lo,hi])),sturm_variations=v,approximate=float((lo+hi)/2)))
 assert infinity[0]-infinity[1]==len(roots)==10
 possible=set(range(1,16));modular=[]
 for prime in range(2,200):
  if not isprime(prime) or not P[-1]%prime:continue
  factors=nmod_poly([v%prime for v in P],prime).factor()[1]
  if any(int(m)!=1 for _,m in factors):continue
  product=[1];degrees=[];certificates=[]
  for factor,multiplicity in factors:
   co=modtrim(factor.coeffs(),prime);certificates.append(irreducibility_certificate(co,prime));degrees.append(len(co)-1);product=modmul(product,co,prime)
  target=modtrim(P,prime);scalar=target[-1]*pow(product[-1],-1,prime)%prime
  assert modtrim([scalar*v for v in product],prime)==target
  subset={0}
  for degree in degrees:subset|={v+degree for v in tuple(subset)}
  possible&=subset
  modular.append(dict(prime=prime,factor_degrees=sorted(degrees),product_scalar=scalar,factors=certificates,possible_proper_factor_degrees=sorted(possible)))
  if not possible:break
 assert not possible
 fields={}
 for label,data in [('f',ff),('g',gg)]:
  fields[label]={}
  for n,value in data.items():
   polys={}
   for m in range(1,4*n+1):
    coefficient=sp.Poly(value.sine(m).as_expr(),b,domain=sp.QQ)
    if not coefficient.is_zero:polys[str(m)]=[str(coefficient.nth(i)) for i in range(coefficient.degree()+1)]
   fields[label][str(n)]=dict(radial_exponent=str(value.q),sine_polynomials=polys)
 polynomial_data=dict(exact=True,delta='1/4',fields=fields)
 pp=ROOT/'verification/prefix_polynomials.json.gz';decoded=json.dumps(polynomial_data,separators=(',',':')).encode();pp.write_bytes(gzip.compress(decoded,mtime=0))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,O16=str(O.as_expr()),primitive_coefficients=list(map(str,P)),sturm_sequence=[list(map(str,row)) for row in seq],infinity_variations=infinity,real_roots=roots,modular_irreducibility=modular,source_path=str(source),source_sha256=sha256(raw).hexdigest(),obstruction_exactly_matches=True,ordered_low_products=120,poisson_identity_orders=list(range(1,16)),prefix_polynomials=dict(path=str(pp),sha256=sha256(pp.read_bytes()).hexdigest(),raw_sha256=sha256(decoded).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/obstruction_checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/lead_initial_output.txt').write_bytes(raw)
 for name in ['period_eight_obstruction.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['sturm_sequence','modular_irreducibility','O14','primitive_coefficients']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/obstruction_FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
