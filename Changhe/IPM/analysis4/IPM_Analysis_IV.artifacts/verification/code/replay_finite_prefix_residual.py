"""Independent direct-pair evaluation of retained residual bounds."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
ROOT=Path('research/188_finite_prefix_stationary_residual')
start=time.monotonic();summary=json.loads((ROOT/'verification/summary.json').read_text())
packed=(ROOT/'verification/checks.json.gz').read_bytes();raw=gzip.decompress(packed)
assert sha256(packed).hexdigest()==summary['archive_sha256'] and sha256(raw).hexdigest()==summary['raw_sha256']
data=json.loads(raw);pairs=values=0
for profile in data['rows']:
    path=Path(profile['path']);assert sha256(path.read_bytes()).hexdigest()==profile['sha256']
    J,B=profile['J'],profile['B'];delta,z=F(profile['delta']),F(profile['z'])
    alpha={int(k):F(v) for k,v in profile['alpha'].items()};beta={int(k):F(v) for k,v in profile['beta'].items()}
    C={int(k):F(v) for k,v in profile['C'].items()};out={n:F(0) for n in range(J+1,2*J+1)}
    contributions=[]
    for i in range(1,J+1):
        for j in range(1,J+1):
            if i+j<=J: continue
            first=abs(2-i*delta)*beta[i]*(B*j*alpha[j])
            second=abs(1-j*delta)*(B*i*beta[i])*alpha[j]
            out[i+j]+=first+second;contributions.append((i+j,first+second));pairs+=1
    assert C==out
    for row in profile['rows']:
        a,b=row['a'],row['b'];value=sum((v*z**(n-1)*abs(1-n*delta)**a*(B*n)**b for n,v in contributions),F(0))
        assert value==F(row['upper_bound']);e=row['strict_dyadic_exponent'];assert F(2)**(e-1)<=value<F(2)**e;values+=1
# Exact one-mode residual obtained directly by differentiating trigonometric fields.
import sympy as s
th,gamma=s.symbols('theta gamma',real=True)
f=s.sin(th);g=-s.sin(2*th)/(2*(gamma+3))
raw_bracket=(gamma+1)*g*s.diff(f,th)-gamma*s.diff(g,th)*f
expected=-((1+3*gamma)*s.sin(th)+(1-gamma)*s.sin(3*th))/(4*(gamma+3))
assert s.trigsimp(s.expand_trig(raw_bracket-expected))==0
assert s.simplify(expected.subs(gamma,s.Rational(1,3))+s.Rational(3,20)*s.sin(th)+s.Rational(1,20)*s.sin(3*th))==0
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,profiles=len(data['rows']),ordered_pairs=pairs,derivative_values=values,independent_symbolic_single_mode_identity=True,source_raw_sha256=sha256(raw).hexdigest(),actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/replay.json').write_text(json.dumps(result,indent=2)+'\n');(ROOT/'sources/replay_finite_prefix_residual.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(result))
