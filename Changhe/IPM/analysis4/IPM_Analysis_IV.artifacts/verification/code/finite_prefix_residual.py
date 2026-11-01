"""Rational norm-based stationary residual certificates for finite prefixes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from resonance_block_majorant import clean
from sharp_prefix_tail_bounds import dyadic_strict
ROOT=Path('research/188_finite_prefix_stationary_residual')
def upper(v):
    mid=F(v[0])*F(2)**int(v[1]);rad=F(v[2])*F(2)**int(v[3]);assert rad>=0 and mid>=0
    return mid+rad

def one(name,J,delta,B,ell,L=None):
    path=Path(name);raw=path.read_bytes();data=json.loads(raw);assert data['all_checks_pass']
    if 'independent_norms' in data:
        alpha={v['n']:upper(v['F']) for v in data['independent_norms'] if v['n']<=J}
        beta={v['n']:upper(v['G']) for v in data['independent_norms'] if v['n']<=J}
    else:
        assert J<data['N'],'Final harmonic not tuned in this prefix format'
        alpha={v['n']:F(v['bound'])/v['n'] for v in data['norms'] if v['n']<=J}
        H={v['n']:F(v['bound'])/v['n'] for v in data['harmonics']}
        beta={n:L*v+H.get(n,F(0)) for n,v in alpha.items()}
    assert set(alpha)==set(beta)==set(range(1,J+1))
    z=F(1,2**ell);coeff={n:F(0) for n in range(J+1,2*J+1)}
    for n in coeff:
        for i in range(max(1,n-J),min(J,n-1)+1):
            j=n-i
            coeff[n]+=(abs(2-i*delta)*B*j+abs(1-j*delta)*B*i)*beta[i]*alpha[j]
    rows=[]
    for d in range(4):
        for a in range(d+1):
            b=d-a
            value=sum((z**(n-1)*abs(1-n*delta)**a*(B*n)**b*c for n,c in coeff.items()),F(0))
            rows.append(dict(a=a,b=b,upper_bound=value,strict_dyadic_exponent=dyadic_strict(value)))
    return dict(path=name,sha256=sha256(raw).hexdigest(),J=J,delta=delta,B=B,z=z,R_dyadic_exponent=F(ell)/delta,alpha=alpha,beta=beta,C=coeff,rows=rows)

start=time.monotonic()
rows=[
 one('research/176_other_certified_prefixes/verification/two_mode4_checks.json',35,F(4,9),4,15,F(243,104)),
 one('research/176_other_certified_prefixes/verification/candidate1_checks.json',26,F(4,9),20,19,F(243,104)),
 one('research/180_period_five_numerical_audit/verification/root5_checks.json',50,F(2,5),4,14),
 one('research/185_period_six_numerical_audit/verification/root6_checks.json',60,F(1,3),4,15),
]
data=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,scope='Finite stationary residual upper bounds with primary weight r^(-gamma), conditional only on the separately reviewed finite recurrence coefficients and theorem188. Infinite convergence is not inferred from residual smallness.',rows=rows,actual_elapsed_s=time.monotonic()-start)
raw=(json.dumps(clean(data),indent=2)+'\n').encode();packed=gzip.compress(raw,mtime=0)
(ROOT/'verification/checks.json.gz').write_bytes(packed)
summary=dict(checked_at_utc=data['checked_at_utc'],raw_sha256=sha256(raw).hexdigest(),raw_bytes=len(raw),archive_sha256=sha256(packed).hexdigest(),archive_bytes=len(packed),profiles=len(rows),actual_elapsed_s=data['actual_elapsed_s'])
(ROOT/'verification/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'sources/finite_prefix_residual.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(summary))
for row in rows:print(row['path'],'J',row['J'],'Rexp',row['R_dyadic_exponent'],[(v['b'],v['strict_dyadic_exponent']) for v in row['rows'] if v['a']==0])
