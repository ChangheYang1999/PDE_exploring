"""Independent polar prefix and necessary potential logs for periods seven/eight."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import tuned_cartesian_exact as ce
ROOT=Path('research/258_period_seven_eight_potential_logs')
R,b=ring('b',QQ)
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def add(d,m,a):
 if not m or not a:return
 if m<0:m,a=-m,-a
 d[m]=d.get(m,R.zero)+a
 if not d[m]:del d[m]
def poisson(f,n,Q):
 p=QQ(1)-QQ(2*n,Q);P=p+1;rhs={};g={}
 for l,a in f.items():
  add(rhs,l+1,a*(p-l)/2);add(rhs,l-1,a*(p+l)/2)
 for m,a in rhs.items():
  den=m*m-P*P;assert den;g[m]=a/den
 return g
def polar(Q):
 ff={1:{1:R.one,3:b}};gg={1:poisson(ff[1],1,Q)};products=0
 for n in range(2,Q+1):
  f={}
  for i in range(1,n):
   j=n-i;Pi=QQ(2)-QQ(2*i,Q);pj=QQ(1)-QQ(2*j,Q)
   for q,v in gg[i].items():
    for l,a in ff[j].items():
     add(f,q+l,a*v*(Pi*l-pj*q)/2);add(f,q-l,a*v*(Pi*l+pj*q)/2)
   products+=1
  factor=QQ(Q-2,2*(n-1));ff[n]={m:v*factor for m,v in f.items()};gg[n]=poisson(ff[n],n,Q)
 return ff,gg,products
def from_coeff(c):
 result=R.zero
 for a in reversed(c):result=result*b+QQ(a)
 return result
def serial(p):
 return [str(p.get((i,),QQ.zero)) for i in range(p.degree()+1)] if p else ['0']
def csine(p,m,a):return ce.sine(ce.K(p),m,ce.R(a.as_expr()))
def main():
 start=time.monotonic();rows=[]
 for Q,number in [(7,253),(8,256)]:
  folder=next(Path('research').glob(str(number)+'_*'));src=folder/'verification/obstruction_checks.json';raw=src.read_bytes();obs=json.loads(raw);assert obs['all_checks_pass']
  receipt=obs['prefix_polynomials'];pr=Path(receipt['path']).read_bytes();assert sha256(pr).hexdigest()==receipt['sha256'];decoded=gzip.decompress(pr);assert sha256(decoded).hexdigest()==receipt['raw_sha256'];exact=json.loads(decoded)
  ff,gg,products=polar(Q);count=0
  for label,fields in [('f',ff),('g',gg)]:
   for n,values in fields.items():
    expected={int(m):from_coeff(c) for m,c in exact['fields'][label][str(n)]['sine_polynomials'].items()}
    assert values==expected,('polar_cartesian',Q,label,n);count+=len(set(values)|set(expected))
  a1=ff[Q].get(1,R.zero);assert a1 and a1.degree()<=Q
  P=from_coeff(obs['primitive_coefficients']);assert P.degree()==2*Q
  bs=sp.Symbol('b');assert sp.gcd(sp.Poly(P.as_expr(),bs),sp.Poly(a1.as_expr(),bs)).degree()==0
  residual=dict(ff[Q]);pure=ce.F(ce.K(2),{});pure_coeff={}
  for m in range((max(residual)-1)//2,1,-1):
   top=residual.get(2*m+1,R.zero);coef=top/QQ(4*m*(1-m*m));pure_coeff[2*m]=coef
   add(residual,2*m+1,-top);add(residual,2*m-1,-top)
   if coef:
    cc=ce.R(coef.as_expr())/2;pure=pure+ce.F(ce.K(2),{(0,2*m):cc,(0,-2*m):cc})
  assert set(residual)<={1,3};d=residual.get(3,R.zero);alpha=(d-a1)/4;beta=d/4;assert beta-alpha==a1/4
  df=(pure.X().X()-pure.Y().Y()).Y()+csine(-1,1,-4*alpha+4*beta)+csine(-1,3,4*beta)
  dg=pure.X().Y().scale(-1)+csine(0,2,alpha)+csine(0,4,-beta/2)
  for actual,expected in [(df,ff[Q]),(dg,gg[Q])]:
   indices={abs(m) for k,m in actual.v}|set(expected)
   for m in indices:assert actual.sine(m)==ce.R(expected.get(m,R.zero).as_expr()),('potential',Q,m)
  rows.append(dict(Q=Q,delta=str(F(2,Q)),polar_cartesian_coefficients=count,ordered_products=products,a_Q=serial(a1),alpha_Q=serial(alpha),beta_Q=serial(beta),a_Q_degree=a1.degree(),compatibility_degree=P.degree(),coprime=True,exact_density_and_stream_reconstruction=True,source=dict(path=str(src),sha256=sha256(raw).hexdigest()),prefix=receipt))
  print(json.dumps(dict(at=stamp(),Q=Q,all_checks_pass=True,a_Q_degree=a1.degree(),coefficients=count,actual_elapsed_s=time.monotonic()-start)),flush=True)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['period_first_logs.py','tuned_cartesian_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(dict(checked_at_utc=stamp(),all_checks_pass=True,actual_elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)
