from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,time,math,gzip,pickle
start=time.monotonic()
k=s.symbols('k',integer=True,positive=True);m=2*k-2;d=s.Rational(2,3)
f={};g={0:{0:s.Integer(1)}}
def add(out,j,v):out[j]=out.get(j,0)+v
for r in range(1,4):
 n=3*k+r;out={};i=r-1
 for sh,b in g[i].items():
  K=m+sh;Pi=2-d*(3*k+i);pj=1-d
  add(out,sh+1,b*(Pi-pj*K)/2);add(out,sh-1,b*(Pi+pj*K)/2)
 if r>1:
  ell=2;b=-s.Rational(3,20);Pi=s.Rational(4,3);pj=1-d*(n-1)
  for sh,a in f[r-1].items():
   K=m+sh
   add(out,sh+ell,b*a*(Pi*K-pj*ell)/2);add(out,sh-ell,b*a*(-Pi*K-pj*ell)/2)
 f[r]={j:s.factor(v/(2*(n-1))) for j,v in out.items() if s.cancel(v)!=0}
 if r<3:
  P=2-d*n;out={}
  for sh,a in f[r].items():
   add(out,sh+1,-a/(2*(m+sh+1+P)));add(out,sh-1,a/(2*(m+sh-1-P)))
  g[r]={j:s.factor(v) for j,v in out.items() if s.cancel(v)!=0}
ratio=s.factor(-f[3][1]/(2*k))
root=Path('research/103_edge_top_chain');(root/'verification').mkdir(parents=True,exist_ok=True);(root/'sources').mkdir(exist_ok=True)
ref=json.loads(Path('research/102_edge_recurrence_reference/verification/exact_reference.json').read_text())['variants']['1']['rows']
b={2:s.Rational(ref[5]['stream']['1']['2'])}
for kk in range(2,85):
 coeff=sum(v.subs(k,kk)*(1 if 2*kk-2+sh==2*kk-1 else -1 if 2*kk-2+sh==-(2*kk-1) else 0) for sh,v in f[3].items())
 b[kk+1]=s.cancel(-b[kk]*coeff/(2*kk))
assert all(v!=0 for v in b.values())
checks=0
for row in ref:
 n=row['n'];degree=row['density_log_degree']
 if n<7:continue
 kk=(n-1)//3;r=n-3*kk
 calc={}
 for sh,v in f[r].items():
  freq=2*kk-2+sh;val=s.cancel(v.subs(k,kk)*b[kk])
  if freq:add(calc,abs(freq),val*(1 if freq>0 else -1))
 calc={j:s.cancel(v) for j,v in calc.items() if v!=0}
 exact={int(j):s.Rational(v) for j,v in row['density'][str(kk-1)].items()}
 assert calc==exact,(n,calc,exact)
 checks+=len(calc)
 if n%3==0:
  assert s.Rational(row['stream'][str(n//3-1)][str(2*n//3-2)])==b[n//3]
  checks+=1
# One exact coefficient at n=250, log degree82, mode165 disproves disappearance of that column.
kk=83;v=s.cancel(b[kk]*f[1][1].subs(k,kk));assert v!=0
summary=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),definition='edge K=1, delta=2/3, f1=sin(theta), canonical resonant constants',normalized_density={str(r):{str(j):str(v) for j,v in c.items()} for r,c in f.items()},normalized_stream={str(r):{str(j):str(v) for j,v in c.items()} for r,c in g.items()},b2=str(b[2]),b3=str(b[3]),successive_ratio=str(ratio),lim_k_times_ratio=str(s.limit(k*ratio,k,s.oo)),finite_exact_coefficient_checks=checks,order250=dict(log_degree=82,frequency=165,coefficient=str(v),log10_abs=float(s.log(abs(v),10).evalf(25))),scope='Symbolic derivation and low-order exact comparison; independent proof review pending.',actual_elapsed_s=time.monotonic()-start)
x=s.symbols('x');poly=6480*k**5-3132*k**4-23454*k**3+29472*k**2-10791*k+880
summary['positive_shifted_numerator']=str(s.Poly(poly.subs(k,x+3),x).as_expr())
assert all(c>0 for c in s.Poly(poly.subs(k,x+3),x).all_coeffs())
summary['order250']['abs_lt_half_min_binary64_subnormal']=abs(int(s.numer(v)))*(1<<1075)<int(s.denom(v))
assert summary['order250']['abs_lt_half_min_binary64_subnormal']
(root/'verification/checks.json').write_text(json.dumps(summary,indent=2)+'\n')
(root/'sources/edge_top_chain.py').write_text(Path(__file__).read_text())
print(json.dumps({key:val for key,val in summary.items() if key not in ['normalized_density','normalized_stream','order250']},indent=2));print('order250log10',summary['order250']['log10_abs'])
