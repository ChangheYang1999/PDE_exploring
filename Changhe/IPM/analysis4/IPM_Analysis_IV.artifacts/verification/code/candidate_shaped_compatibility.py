"""Exact first obstruction with Candidate 007's higher modes fixed."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, sys, time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import fmpq as Q, fmpq_poly as Poly
import sympy as sp
from polynomial_prime_audit import Field
from exact_polynomial_certificates import primitive, sturm, sturm_finite, sturm_infinity, evaluate
from fractions import Fraction
root = Path('research/156_candidate_shaped_compatibility')
start = time.monotonic()
def save(name, data):
    (root/'verification'/name).write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(dict(stage=name, elapsed_s=time.monotonic()-start)), flush=True)
try:
    source = Path('research/02_candidate007/data/leading_exact.json')
    inp = json.loads(source.read_text())
    aa = {int(j):Q(v) for j,v in inp['density'].items()}
    amp = aa[1]
    assert amp > 0
    b0 = aa[3]/amp
    initial = {j:Poly([v/amp]) for j,v in aa.items()}
    initial[3] = Poly([0,1])
    signed = {}
    for j,v in initial.items():
        signed[j],signed[-j] = v/2,-v/2
    delta = Q(4,9)
    F = {1:Field(1-delta,signed)}
    G = {}; XF = {}; YF = {}; XG = {}; YG = {}
    rows=[]; counts=dict(ordered_products=0,poisson_orders=0,symmetry_coefficients=0,support_coefficients=0)
    for n in range(1,10):
        p = 1-n*delta
        if n > 1:
            total = Field(p,{})
            for i in range(1,n):
                total = total+XG[i]*YF[n-i]-YG[i]*XF[n-i]
                counts['ordered_products'] += 1
            F[n] = total.scale(Q(5,4*(n-1)))
        assert all(m%2 and abs(m)<=20*n-1 and a.degree()<=n for m,a in F[n].a.items())
        for m,a in F[n].a.items():
            assert F[n].a.get(-m,Poly([])) == -a
        counts['symmetry_coefficients'] += len(F[n].a)
        counts['support_coefficients'] += len(F[n].a)
        if n < 9:
            XF[n],YF[n] = F[n].X(),F[n].Y()
            P = p+1
            dd = {}
            for m,a in XF[n].a.items():
                den = m*m-P*P
                assert den
                dd[m] = a/den
            G[n] = Field(P,dd)
            XG[n],YG[n] = G[n].X(),G[n].Y()
            assert not (XG[n].X().scale(-1)+YG[n].Y()-XF[n]).a
            counts['poisson_orders'] += 1
        rows.append(dict(n=n,density_signed_modes=len(F[n].a),maximum_mode=max(map(abs,F[n].a)),maximum_polynomial_degree=max(a.degree() for a in F[n].a.values())))
        save('progress.json',dict(rows=rows,counts=counts))
    O = 2*F[9].a.get(1,Poly([]))
    assert O.degree() == 9
    ref = json.loads(Path('research/144_general_rational_response_limit/verification/h2_Q9.json').read_text())
    # Locate the exact two-mode obstruction without importing another recurrence.
    obskeys = [key for key in ref if 'obstruction' in key.lower()]
    if 'first_obstruction' in ref:
        expr = ref['first_obstruction']
    elif 'obstruction' in ref:
        expr = ref['obstruction']
    else:
        raise KeyError(('obstruction keys',obskeys))
    if isinstance(expr,dict):
        expr = expr['polynomial']
    b = sp.Symbol('b')
    reference = sp.Poly(sp.sympify(expr),b,domain=sp.QQ)
    assert O[9] == Q(str(reference.nth(9)))
    older_path = Path('research/03_resonances/verification/independent_first_resonances/candidate_9_5.json')
    older = json.loads(older_path.read_text())
    at_original = O(b0)*amp**9
    assert at_original == Q(older['kappa'])
    primitive_coeffs = primitive([Fraction(str(v)) for v in O.coeffs()])
    if primitive_coeffs[-1] < 0:
        primitive_coeffs = [-v for v in primitive_coeffs]
    save('polynomial.json',dict(delta='4/9',c='9/5',coefficients_ascending=list(map(str,O.coeffs())),primitive_coefficients_ascending=list(map(str,primitive_coeffs)),fixed_normalized_coefficients={str(j):str(v/amp) for j,v in aa.items() if j!=3},original_normalized_b=str(b0),original_amplitude=str(amp),original_obstruction_matches=True,leading_coefficient_matches_two_mode=True,counts=counts))
    poly = sp.Poly.from_list(list(reversed(primitive_coeffs)),b,domain=sp.ZZ)
    intervals = sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**24))
    seq = sturm(primitive_coeffs)
    assert len(seq[-1]) == 1
    vi = [sturm_infinity(seq,negative) for negative in [True,False]]
    assert vi[0]-vi[1] == len(intervals)
    rr = []
    for index,((lo,hi),mult) in enumerate(intervals,1):
        assert mult == 1
        denominator = 1 << 90
        left = Fraction(int(sp.floor(lo*denominator)),denominator)
        right = Fraction(int(sp.ceiling(hi*denominator)),denominator)
        assert left < right and sp.Rational(left.numerator,left.denominator) <= lo
        assert sp.Rational(right.numerator,right.denominator) >= hi
        assert evaluate(primitive_coeffs,left) and evaluate(primitive_coeffs,right)
        variations = [sturm_finite(seq,x) for x in [left,right]]
        assert variations[0]-variations[1] == 1
        change = [Fraction(str(amp))*x-Fraction(str(aa[3])) for x in [left,right]]
        distance = [Fraction(0),max(map(abs,change))] if change[0]<=0<=change[1] else sorted(map(abs,change))
        rr.append(dict(root_index=index,interval=[str(left),str(right)],approx=float((left+right)/2),sturm_variations=variations,sin3_coefficient_change_interval=list(map(str,change)),leading_l1_change_interval=list(map(str,distance)),leading_l1_change_approx=float(sum(distance)/2)))
    nearest = min(rr,key=lambda row:Fraction(row['leading_l1_change_interval'][1]))
    assert all(Fraction(nearest['leading_l1_change_interval'][1]) < Fraction(row['leading_l1_change_interval'][0]) for row in rr if row is not nearest)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source_sha256=sha256(source.read_bytes()).hexdigest(),older_obstruction_sha256=sha256(older_path.read_bytes()).hexdigest(),real_root_count=len(rr),sturm_variations_at_infinities=vi,primitive_sturm_sequence=[list(map(str,v)) for v in seq],roots=rr,nearest_root_index=nearest['root_index'],counts=counts,actual_elapsed_s=time.monotonic()-start,scope='Only first compatibility; infinite response infimum not checked.')
    save('checks.json',result)
    for name in ['candidate_shaped_compatibility.py','polynomial_prime_audit.py','exact_polynomial_certificates.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    save('MANIFEST.json',dict(files=files))
    print(json.dumps(dict(all_checks_pass=True,roots=rr,actual_elapsed_s=time.monotonic()-start)),flush=True)
except Exception as exc:
    import traceback
    fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start)
    save('FAILURE.json',fail)
    print(json.dumps(fail),flush=True)
    raise SystemExit(1)
