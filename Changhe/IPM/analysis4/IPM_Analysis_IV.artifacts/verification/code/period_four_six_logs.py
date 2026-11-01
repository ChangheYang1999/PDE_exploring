"""Independent polar prefixes and Euclidean certificates for Q4--Q6 logs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import ast,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
import tuned_cartesian_exact as ce
from period_first_logs import R,b,add,polar,from_coeff,serial,csine
from exact_polynomial_certificates import primitive,remainder
ROOT=Path('research/260_period_four_six_potential_logs')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();rows=[]
 for Q,number in [(4,142),(5,130),(6,154)]:
  folder=next(Path('research').glob(str(number)+'_*'));op=folder/'verification/obstruction_checks.json';ob=op.read_bytes();obs=json.loads(ob);assert obs['all_exact_checks_pass']
  pp=folder/'verification/exact_prefix.json';pr=pp.read_bytes();exact=json.loads(pr);ff,gg,products=polar(Q);count=0
  for label,fields in [('density',ff),('stream',gg)]:
   for n,values in fields.items():
    raw=exact[label][str(n)];assert F(raw['radial_exponent'])==F(1 if label=='density' else 2)-F(2*n,Q)
    actual=ce.F(ce.K(sp.Rational(raw['radial_exponent'])),{ast.literal_eval(k):ce.R(sp.sympify(v)) for k,v in raw['signed_laurent'].items()});actual.check_sine()
    indices={abs(m) for k,m in actual.v}|set(values);assert all(k==0 for k,m in actual.v)
    for m in indices:assert actual.sine(m)==ce.R(values.get(m,R.zero).as_expr()),('prefix',Q,label,n,m)
    count+=len(indices)
  a=ff[Q].get(1,R.zero);assert a and a.degree()<=Q;P=from_coeff(obs['coefficients_ascending']);assert P.degree()==2*Q
  chain=[primitive(list(map(F,serial(P)))),primitive(list(map(F,serial(a))))]
  while len(chain[-1])>1:
   r=primitive(remainder(chain[-2],chain[-1]));assert r,('common_factor',Q);chain.append(r)
  assert len(chain[-1])==1 and abs(chain[-1][0])==1
  assert sp.gcd(sp.Poly(P.as_expr(),sp.Symbol('b')),sp.Poly(a.as_expr(),sp.Symbol('b'))).degree()==0
  residual=dict(ff[Q]);pure=ce.F(ce.K(2),{});columns={}
  for m in range((max(residual)-1)//2,1,-1):
   top=residual.get(2*m+1,R.zero);coef=top/(4*m*(1-m*m));columns[2*m]=serial(coef)
   add(residual,2*m+1,-top);add(residual,2*m-1,-top)
   if coef:
    cc=ce.R(coef.as_expr())/2;pure=pure+ce.F(ce.K(2),{(0,2*m):cc,(0,-2*m):cc})
  assert set(residual)<={1,3};d=residual.get(3,R.zero);alpha=(d-a)/4;beta=d/4;assert beta-alpha==a/4
  df=(pure.X().X()-pure.Y().Y()).Y()+csine(-1,1,-4*alpha+4*beta)+csine(-1,3,4*beta)
  dg=pure.X().Y().scale(-1)+csine(0,2,alpha)+csine(0,4,-beta/2)
  for actual,expected in [(df,ff[Q]),(dg,gg[Q])]:
   actual.check_sine()
   for m in {abs(m) for k,m in actual.v}|set(expected):assert actual.sine(m)==ce.R(expected.get(m,R.zero).as_expr()),('potential',Q,m)
  rows.append(dict(Q=Q,delta=str(F(2,Q)),polar_cartesian_coefficients=count,ordered_products=products,a_Q=serial(a),alpha_Q=serial(alpha),beta_Q=serial(beta),pure_cosine_columns=columns,euclidean_remainders=chain,compatibility_degree=P.degree(),a_Q_degree=a.degree(),real_root_count=len(obs['real_roots']),coprime=True,exact_density_and_stream_reconstruction=True,sources=[dict(path=str(p),sha256=sha256(raw).hexdigest()) for p,raw in [(op,ob),(pp,pr)]]))
  print(json.dumps(dict(at=stamp(),Q=Q,coefficients=count,a_Q_degree=a.degree(),remainder_degrees=[len(v)-1 for v in chain],all_checks_pass=True,actual_elapsed_s=time.monotonic()-start)),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['period_four_six_logs.py','period_first_logs.py','exact_polynomial_certificates.py','tuned_cartesian_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(dict(at=stamp(),all_checks_pass=True,actual_elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
