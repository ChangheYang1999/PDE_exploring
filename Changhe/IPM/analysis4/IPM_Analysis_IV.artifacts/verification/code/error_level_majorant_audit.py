"""Independently enclose the error-level tree constant and finite scalar tests."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from flint import arb, fmpq, ctx
import json, math, time, sys
sys.dont_write_bytecode = True
from brjuno_constants_verify import convergents, continued_fraction

ctx.prec = 1024
started = time.monotonic()
root = Path('research/76_error_level_majorant')
source = Path('research/02_candidate007/data/leading_exact.json')
raw = source.read_bytes()
profile = json.loads(raw)
F = sum((abs(Fraction(v)) for v in profile['density'].values()), Fraction())
ball = lambda x: arb(fmpq(Fraction(x).numerator, Fraction(x).denominator))
text = lambda x: x.str(45, radius=True)
sqrt5 = arb(5).sqrt()
ref_cf = continued_fraction(Fraction(profile['delta'])/2)
ref_cv = convergents(ref_cf)
p, q = ref_cv[-1]
pp, qp = ref_cv[-2]
phi = (1+sqrt5)/2
near = (p*phi+pp)/(q*phi+qp)
families = [
    ('sqrt5', 1/(2*sqrt5), [0,4]+[2,8]*55, 80, 8),
    ('sqrt2', arb(2).sqrt()-1, [0]+[2]*112, 80, 2),
    ('sqrt5_other', (sqrt5-1)/4, [0,3]+[4]*110, 80, 4),
    ('near_reference', near, ref_cf+[1]*120, 100, 1),
]
for N in [4,8,16,32,64]:
    large_c = 2*N+sqrt5
    families.append((f'large_c_N{N}', (1-1/large_c)/2, [0,2,N]+[1]*120, 100, 1))
assert 2**8*5**33 < 6**33
assert Fraction(8*97*33**2*6,32**3*5) < 32
assert 96**33 < 128**32
records = []
constant_rows = []
separation_tests = tree_tests = scalar_tests = 0
for name, alpha, aa, terms, tail_max in families:
    cv = convergents(aa)
    es = [abs(qj*alpha-pj) for pj,qj in cv]
    assert all(e>0 for e in es)
    for k in range(1,terms):
        assert es[k-1] > es[k]
        assert (es[k-1]-aa[k+1]*es[k]-es[k+1]).contains(0)
        assert es[k-1]/es[k] > aa[k+1]
        assert es[k-1]/es[k] < aa[k+1]+1
    Epartial = sum(((es[k-1]/es[k]).log()/cv[k][1] for k in range(1,terms)),arb(0))
    tail = 4*arb(tail_max+1).log()/cv[terms][1]
    Eupper = Epartial+tail
    delta = 2*alpha
    c = 1/(1-delta)
    lam = ball(Fraction(3,2))+delta/2+1/delta
    for tag, norm, L in [('sin1',Fraction(1),1),('candidate007_raw',F,19)]:
        K = 2*lam*(L+2)/(c-1)
        A_lower = 4*K*ball(norm)*(2*Epartial).exp()/(alpha*delta)
        A_upper = 4*K*ball(norm)*(2*Eupper).exp()/(alpha*delta)
        log2R_lower = A_lower.log()/(delta*arb(2).log())
        log2R_upper = A_upper.log()/(delta*arb(2).log())
        power = math.ceil(float(log2R_upper.mid()))
        assert log2R_upper < power
        assert A_upper < (delta*power*arb(2).log()).exp()
        constant_rows.append(dict(parameter=name,profile=tag,leading_norm_exact=str(norm),L=L,
            K=text(K),A_lower_ball=text(A_lower),A_upper_ball=text(A_upper),
            log2_R_lower_ball=text(log2R_lower),log2_R_upper_ball=text(log2R_upper),
            certified_exterior_radius_power_of_two=power,
            certified_exterior_radius_integer=str(2**power)))
    distances = {}
    for m in range(1,2001):
        nearest = int(round(float((m*alpha).mid())))
        v = abs(m*alpha-nearest)
        assert v<ball(Fraction(1,2))
        distances[m] = v
    max_marked = []
    for k in range(1,16):
        qk = cv[k][1]
        marked = []
        threshold = es[k-1]/2
        for m,v in distances.items():
            assert v<threshold or v>threshold
            if v<threshold: marked.append(m)
        if marked:
            assert min(marked)>=qk
            assert all(b-a>=qk for a,b in zip(marked,marked[1:]))
        separation_tests += len(distances)
        if qk>512: continue
        members=set(marked)
        maxima=[0]*513
        for n in range(2,513):
            maxima[n]=(n in members)+max(maxima[i]+maxima[n-i] for i in range(1,n//2+1))
            assert qk*maxima[n]<=2*n
            tree_tests += 1
        max_marked.append(dict(k=k,q=qk,maximum_count_at_512=maxima[512]))
    # Equality scalar majorant at K=Y1=1, independent of the nonlinear IPM code.
    A_scalar=4*(2*Eupper).exp()/alpha
    values=[arb(0),arb(1)]
    largest_log_slack=arb(0)
    roots=[]
    for n in range(2,513):
        full=sum((values[i]*values[n-i] for i in range(1,n)),arb(0))/(2*distances[n])
        values.append(full)
        upper=alpha*A_scalar**n/4
        assert full<upper
        scalar_tests+=1
        if n in [64,128,256,512]:roots.append(dict(n=n,scalar_root=text(full.root(n)),bound_root=text(A_scalar)))
    records.append(dict(name=name,alpha=text(alpha),delta=text(delta),c=text(c),terms=terms,
        E_partial_ball=text(Epartial),E_upper_ball=text(Eupper),tail_bound=text(tail),
        continued_fraction_prefix=aa[:min(20,len(aa))],first_denominators=[x[1] for x in cv[:8]],
        maximum_marked_tree_counts=max_marked,scalar_roots=roots))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
    arithmetic='1024-bit Arb, exact continued-fraction recurrences, integer tree dynamic programming',
    input_profile_path=str(source),input_profile_sha256=sha256(raw).hexdigest(),
    code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),parameters=records,constant_table=constant_rows,
    finite_separation_tests=separation_tests,all_tree_bound_comparisons=tree_tests,
    scalar_equality_majorant_comparisons=scalar_tests,all_checks_passed=True,
    actual_elapsed_s=time.monotonic()-started)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['error_level_majorant_audit.py','brjuno_constants_verify.py']:
    (root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['parameters','constant_table']},indent=2))
for row in records:print(row['name'],'E=',row['E_upper_ball'])
for row in constant_rows:print(row['parameter'],row['profile'],'A=',row['A_upper_ball'],'R=2^'+str(row['certified_exterior_radius_power_of_two']))
