"""Independent Q4 root, irreducibility, response, and lead-formula comparison certificates."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import json,re,sys,time
sys.dont_write_bytecode=True
import sympy as sp
from flint import nmod_poly
from exact_polynomial_certificates import *
root=Path('research/142_period_four_tuning');out=root/'verification';start=time.monotonic();b,k=sp.symbols('b k')
def put(name,obj):(out/name).write_text(json.dumps(obj,indent=2)+'\n')
try:
 data=json.loads((out/'obstruction_checks.json').read_text());O=sp.Poly(sp.sympify(data['O8']),b,domain=sp.QQ);P=primitive([F(str(O.nth(i))) for i in range(O.degree()+1)])
 if P[-1]<0:P=[-v for v in P]
 assert len(P)==9
 seq=sturm(P);assert len(seq[-1])==1
 roots=[]
 for rr in data['real_roots']:
  lo,hi=map(F,rr['interval']);assert evaluate(P,lo) and evaluate(P,hi);v=[sturm_finite(seq,x) for x in [lo,hi]];assert v[0]-v[1]==1
  roots.append(dict(interval=rr['interval'],approx=float((lo+hi)/2),sturm_variations=v))
 vi=[sturm_infinity(seq,neg) for neg in [True,False]];assert vi[0]-vi[1]==len(roots)==6
 possible=set(range(1,8));mods=[]
 for p,expected in [(5,[2,6]),(29,[1,7])]:
  assert P[-1]%p
  factors=nmod_poly([v%p for v in P],p).factor()[1];product=[1];degrees=[];cert=[]
  for factor,mult in factors:
   assert int(mult)==1;co=modtrim(factor.coeffs(),p);ci=irreducibility_certificate(co,p);cert.append(ci);degrees.append(len(co)-1);product=modmul(product,co,p)
  assert sorted(degrees)==expected
  target=modtrim(P,p);scalar=target[-1]*pow(product[-1],-1,p)%p;assert modtrim([scalar*v for v in product],p)==target
  subset={0}
  for degree in degrees:subset|={x+degree for x in tuple(subset)}
  possible&=subset;mods.append(dict(prime=p,degrees=degrees,product_scalar=scalar,factors=cert,possible_factor_degrees=sorted(possible)))
 assert not possible
 source=Path('../a4-lead/code/tuned/tq_Q4_M3.out');source_raw=source.read_bytes();lines=source_raw.decode().splitlines()
 leadO=sp.sympify(next(s.split(' O_8(b) = ',1)[1] for s in lines if ' O_8(b) = ' in s));assert sp.expand(O.as_expr()-leadO)==0
 sr=json.loads((out/'symbolic_responses.json').read_text());own=sp.sympify(sr['sigma']);lead=sp.sympify(next(s.split('generic sigma(k) = ',1)[1] for s in lines if s.startswith('generic sigma(k) = ')))
 assert sp.cancel(own-lead)==0
 small=json.loads((out/'small_responses.json').read_text())['rows'];small_comparisons=[]
 for row in small:
  n=row['k'];expr=sp.sympify(next(s.split(' sigma=',1)[1] for s in lines if s.startswith('k='+str(n)+' sigma=')));assert sp.cancel(expr-sp.sympify(row['sigma']))==0
  small_comparisons.append(n)
 # Check the extra direct values in the other implementation against our tail formula.
 for n in range(12,15):
  expr=sp.sympify(next(s.split(' sigma=',1)[1] for s in lines if s.startswith('k='+str(n)+' sigma=')));assert sp.cancel(own.subs(k,n)-expr)==0
 assert sr['limit_nonzero'] and sr['small_nonzero'] and not sr['integer_common_zeros_in_tail'] and sr['limit_degree']==4
 assert all(row['gcd_obstruction_degree']==0 for row in small) and sr['limit_gcd_obstruction_degree']==0
 den=sp.Poly(sp.sympify(sr['denominator']),k,domain=sp.QQ);df=sp.factor_list(den)[1];denroots=[]
 for fac,mult in df:
  assert fac.degree()==1;rt=-fac.nth(0)/fac.nth(1);assert rt<9;denroots.append(dict(root=str(rt),multiplicity=int(mult)))
 limit=sp.Poly(sp.sympify(sr['sigma_infinity']),b,domain=sp.QQ)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,primitive_coefficients_ascending=list(map(str,P)),primitive_sturm_sequence=[list(map(str,a)) for a in seq],sturm_variations_at_infinities=vi,real_roots=roots,modular_certificates=mods,irreducible_over_Q=True,source_path=str(source),source_sha256=sha256(source_raw).hexdigest(),obstruction_exactly_equal=True,generic_response_exactly_equal=True,small_responses_exactly_equal=small_comparisons,extra_tail_direct_comparisons=[12,13,14],denominator_roots=denroots,sigma_infinity=str(limit.as_expr()),all_six_uniform_response_infima_positive=True,actual_elapsed_s=time.monotonic()-start)
 put('root_response_certificates.json',result);(root/'sources/lead_Q4_output.txt').write_bytes(source_raw)
 for name in ['period_four_certificates.py','exact_polynomial_certificates.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files))
 print(json.dumps({k:v for k,v in result.items() if k not in ['primitive_sturm_sequence','modular_certificates']}),flush=True)
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('CERTIFICATE_FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
