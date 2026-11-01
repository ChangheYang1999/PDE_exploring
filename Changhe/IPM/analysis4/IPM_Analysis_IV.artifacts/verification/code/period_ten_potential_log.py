"""Independent polar check of the first required potential logarithm at Q10."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import sympy as sp
import tuned_cartesian_exact as ce
from period_first_logs import R,b,add,polar,from_coeff,serial,csine
from exact_polynomial_certificates import primitive,remainder
ROOT=Path('research/283_period_ten_potential_log')
start=time.monotonic();Q=10
src=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json')
raw=src.read_bytes();obs=json.loads(raw);assert obs['all_checks_pass'] and obs['independent_exact']
receipt=obs['prefix_polynomials'];pr=Path(receipt['path']).read_bytes();assert sha256(pr).hexdigest()==receipt['sha256']
decoded=gzip.decompress(pr);assert sha256(decoded).hexdigest()==receipt['raw_sha256'];exact=json.loads(decoded)
ff,gg,products=polar(Q);count=0
for label,fields in [('f',ff),('g',gg)]:
    for n,values in fields.items():
        expected={int(m):from_coeff(c) for m,c in exact['fields'][label][str(n)]['sine_polynomials'].items()}
        assert values==expected,('polar_cartesian',label,n);count+=len(set(values)|set(expected))
a=ff[Q].get(1,R.zero);assert a and a.degree()<=Q
P=from_coeff(obs['primitive_coefficients']);assert P.degree()==2*Q
chain=[primitive(list(map(F,serial(P)))),primitive(list(map(F,serial(a))))]
while len(chain[-1])>1:
    r=primitive(remainder(chain[-2],chain[-1]));assert r;chain.append(r)
assert len(chain[-1])==1 and abs(chain[-1][0])==1
residual=dict(ff[Q]);pure=ce.F(ce.K(2),{});columns={}
for m in range((max(residual)-1)//2,1,-1):
    top=residual.get(2*m+1,R.zero);coef=top/(4*m*(1-m*m));columns[2*m]=serial(coef)
    add(residual,2*m+1,-top);add(residual,2*m-1,-top)
    if coef:
        cc=ce.R(coef.as_expr())/2;pure=pure+ce.F(ce.K(2),{(0,2*m):cc,(0,-2*m):cc})
assert set(residual)<={1,3};d=residual.get(3,R.zero);alpha=(d-a)/4;beta=d/4;assert beta-alpha==a/4
df=(pure.X().X()-pure.Y().Y()).Y()+csine(-1,1,-4*alpha+4*beta)+csine(-1,3,4*beta)
dg=pure.X().Y().scale(-1)+csine(0,2,alpha)+csine(0,4,-beta/2)
reconstruction=0
for actual,expected in [(df,ff[Q]),(dg,gg[Q])]:
    actual.check_sine()
    for m in {abs(m) for k,m in actual.v}|set(expected):
        assert actual.sine(m)==ce.R(expected.get(m,R.zero).as_expr());reconstruction+=1
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,Q=Q,delta='1/5',polar_cartesian_coefficients=count,ordered_products=products,a_Q=serial(a),alpha_Q=serial(alpha),beta_Q=serial(beta),pure_cosine_columns=columns,euclidean_remainders=chain,compatibility_degree=P.degree(),a_Q_degree=a.degree(),real_root_count=len(obs['real_roots']),coprime=True,exact_density_and_stream_reconstruction=True,reconstruction_coefficients=reconstruction,source=dict(path=str(src),sha256=sha256(raw).hexdigest()),prefix=receipt,scope='Finite necessary potential logarithm; later convergence requires separate admission.',actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
for name in ['period_ten_potential_log.py','period_first_logs.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in out.items() if k not in ['a_Q','alpha_Q','beta_Q','pure_cosine_columns','euclidean_remainders']}))
