"""Independent exact Cartesian first compatibility at delta4/7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
import tuned_cartesian_exact as ce
from exact_polynomial_certificates import primitive,sturm,sturm_finite,sturm_infinity,evaluate,modtrim,irreducibility_certificate
ROOT=Path('research/239_four_sevenths_two_mode')
ce.p=lambda n:1-ce.K(4)*n/7
b=sp.Symbol('b')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();ff={1:ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b)};gg={1:ce.poisson(ff[1])}
 for n in range(2,8):
  acc=ce.F(ce.p(n),{})
  for i in range(1,n):acc=acc+ce.adv(gg[i],ff[n-i])
  ff[n]=acc.scale(ce.K(3)/(4*(n-1)));ff[n].check_sine();assert all(a==0 and m%2 and abs(m)<=4*n-1 for a,m in ff[n].v)
  if n<7:gg[n]=ce.poisson(ff[n])
 O=sp.Poly(ff[7].sine(1).as_expr(),b,domain=sp.QQ);assert O.degree()==7
 P=primitive([F(str(O.nth(i))) for i in range(8)])
 if P[-1]<0:P=[-x for x in P]
 source=Path('../a4-lead/code/tuned/tq_certh_Q7h2.log');raw=source.read_bytes();lines=raw.decode().splitlines()
 lead=sp.Poly(sp.sympify(next(s[4:] for s in lines if s.startswith('P = '))),b,domain=sp.QQ)
 scale=sp.sympify(next(s.split('O = P * ',1)[1] for s in lines if s.startswith('O = P * ')))
 assert lead==sp.Poly(sum(sp.Integer(v)*b**i for i,v in enumerate(P)),b,domain=sp.QQ) and sp.expand(O.as_expr()-lead.as_expr()*scale)==0
 seq=sturm(P);infinity=[sturm_infinity(seq,neg) for neg in [True,False]];roots=[]
 for interval,multiplicity in sp.polys.polytools.intervals(lead,eps=sp.Rational(1,10**60)):
  lo,hi=map(lambda x:F(str(x)),interval);v=[sturm_finite(seq,x) for x in [lo,hi]];assert multiplicity==1 and v[0]-v[1]==1 and evaluate(P,lo) and evaluate(P,hi)
  roots.append(dict(interval=list(map(str,[lo,hi])),sturm_variations=v,approximate=float((lo+hi)/2)))
 assert infinity[0]-infinity[1]==len(roots)==3 and P[-1]%23
 irreducibility=irreducibility_certificate(modtrim(P,23),23)
 fields={}
 for label,data in [('f',ff),('g',gg)]:
  fields[label]={}
  for n,value in data.items():
   polys={}
   for m in range(1,4*n+1):
    coefficient=sp.Poly(value.sine(m).as_expr(),b,domain=sp.QQ)
    if not coefficient.is_zero:polys[str(m)]=[str(coefficient.nth(i)) for i in range(coefficient.degree()+1)]
   fields[label][str(n)]=dict(radial_exponent=str(value.q),sine_polynomials=polys)
 polynomial_data=dict(exact=True,delta='4/7',fields=fields)
 pp=ROOT/'verification/prefix_polynomials.json';pp.write_text(json.dumps(polynomial_data,indent=2)+'\n')
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,O7=str(O.as_expr()),primitive_coefficients=list(map(str,P)),sturm_sequence=[list(map(str,row)) for row in seq],infinity_variations=infinity,real_roots=roots,modular_irreducibility=irreducibility,source_path=str(source),source_sha256=sha256(raw).hexdigest(),obstruction_exactly_matches=True,ordered_low_products=21,poisson_identity_orders=list(range(1,7)),prefix_polynomials=dict(path=str(pp),sha256=sha256(pp.read_bytes()).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/obstruction_checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/lead_initial_output.txt').write_bytes(raw)
 for name in ['four_sevenths_obstruction.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['sturm_sequence','modular_irreducibility','O7']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/obstruction_FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
