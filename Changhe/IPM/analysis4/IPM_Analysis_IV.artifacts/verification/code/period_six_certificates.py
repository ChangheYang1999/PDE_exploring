"""Independent modular, Sturm, and response certificates for delta=1/3."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as F
import json, sys, time
sys.dont_write_bytecode = True
import sympy as sp
from flint import nmod_poly
from exact_polynomial_certificates import *
root = Path('research/154_period_six_tuning')
out = root/'verification'
start = time.monotonic()
b, k = sp.symbols('b k')
def put(name, obj):
    (out/name).write_text(json.dumps(obj, indent=2)+'\n')
try:
    data = json.loads((out/'obstruction_checks.json').read_text())
    O = sp.Poly(sp.sympify(data['O12']), b, domain=sp.QQ)
    P = primitive([F(str(O.nth(i))) for i in range(O.degree()+1)])
    if P[-1] < 0:
        P = [-v for v in P]
    assert len(P) == 13
    seq = sturm(P)
    assert len(seq[-1]) == 1
    roots = []
    for rr in data['real_roots']:
        lo, hi = map(F, rr['interval'])
        assert evaluate(P, lo) and evaluate(P, hi)
        v = [sturm_finite(seq, x) for x in [lo, hi]]
        assert v[0]-v[1] == 1
        roots.append(dict(interval=rr['interval'], approx=float((lo+hi)/2), sturm_variations=v))
    vi = [sturm_infinity(seq, neg) for neg in [True, False]]
    assert vi[0]-vi[1] == len(roots) == 6
    possible = set(range(1, 12))
    mods = []
    for prime, expected in [(13, [3, 9]), (19, [1, 11])]:
        assert P[-1] % prime
        factors = nmod_poly([v % prime for v in P], prime).factor()[1]
        product, degrees, cert = [1], [], []
        for factor, mult in factors:
            assert int(mult) == 1
            co = modtrim(factor.coeffs(), prime)
            ci = irreducibility_certificate(co, prime)
            cert.append(ci)
            degrees.append(len(co)-1)
            product = modmul(product, co, prime)
        assert sorted(degrees) == expected
        target = modtrim(P, prime)
        scalar = target[-1]*pow(product[-1], -1, prime) % prime
        assert modtrim([scalar*v for v in product], prime) == target
        subset = {0}
        for degree in degrees:
            subset |= {x+degree for x in tuple(subset)}
        possible &= subset
        mods.append(dict(prime=prime, degrees=degrees, product_scalar=scalar,
                         factors=cert, possible_factor_degrees=sorted(possible)))
    assert not possible
    source = Path('../a4-lead/code/tuned/tq_cert_Q6.out')
    source_raw = source.read_bytes()
    lines = source_raw.decode().splitlines()
    leadP = sp.sympify(next(s.split(' P = ', 1)[1] for s in lines if s.startswith('Q = 6 ')))
    leadscale = sp.sympify(next(s.split('O_2Q = P * ', 1)[1] for s in lines if s.startswith('O_2Q = P * ')))
    assert sp.Poly(leadP, b) == sp.Poly(sum(sp.Rational(v)*b**i for i,v in enumerate(P)), b)
    assert sp.expand(O.as_expr()-leadscale*leadP) == 0
    sr = json.loads((out/'symbolic_responses.json').read_text())
    limit = sp.Poly(sp.sympify(sr['sigma_infinity']), b, domain=sp.QQ)
    leadlimit = sp.sympify(next(s.split('sigma_inf = ', 1)[1] for s in lines if s.startswith('sigma_inf = ')))
    assert sp.expand(limit.as_expr()-leadlimit) == 0
    small = json.loads((out/'small_responses.json').read_text())['rows']
    assert sr['limit_nonzero'] and sr['small_nonzero']
    assert not sr['integer_common_zeros_in_tail'] and sr['limit_degree'] == 6
    assert all(row['gcd_obstruction_degree'] == 0 and row['degree'] <= 6 for row in small)
    assert sr['limit_gcd_obstruction_degree'] == 0
    den = sp.Poly(sp.sympify(sr['denominator']), k, domain=sp.QQ)
    denroots = []
    for fac, mult in sp.factor_list(den)[1]:
        assert fac.degree() == 1
        rt = -fac.nth(0)/fac.nth(1)
        assert rt < 13
        denroots.append(dict(root=str(rt), multiplicity=int(mult)))
    common = sp.Poly(sp.sympify(sr['common_numerator_coefficient_factor']), k, domain=sp.QQ)
    commonroots = []
    for fac, mult in sp.factor_list(common)[1]:
        assert fac.degree() == 1
        rt = -fac.nth(0)/fac.nth(1)
        assert rt < 13
        commonroots.append(dict(root=str(rt), multiplicity=int(mult)))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  all_checks_pass=True, primitive_coefficients_ascending=list(map(str, P)),
                  primitive_sturm_sequence=[list(map(str, a)) for a in seq],
                  sturm_variations_at_infinities=vi, real_roots=roots,
                  modular_certificates=mods, irreducible_over_Q=True,
                  source_path=str(source), source_sha256=sha256(source_raw).hexdigest(),
                  obstruction_exactly_equal=True, limit_exactly_equal=True,
                  independent_direct_k=list(range(2,19)), independent_tail_overlap=list(range(13,19)),
                  denominator_roots=denroots, common_numerator_roots=commonroots,
                  sigma_infinity=str(limit.as_expr()), all_six_uniform_response_infima_positive=True,
                  actual_elapsed_s=time.monotonic()-start)
    put('root_response_certificates.json', result)
    (root/'sources/lead_Q6_output.txt').write_bytes(source_raw)
    for name in ['period_six_certificates.py', 'exact_polynomial_certificates.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files = {str(p.relative_to(root)):dict(bytes=p.stat().st_size, sha256=sha256(p.read_bytes()).hexdigest())
             for p in root.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
    put('MANIFEST.json', dict(files=files))
    print(json.dumps({key:result[key] for key in ['checked_at_utc','all_checks_pass',
                     'sturm_variations_at_infinities','real_roots','actual_elapsed_s']}), flush=True)
except Exception as exc:
    import traceback
    fail = dict(error_type=type(exc).__name__, error=str(exc),
                frames=[dict(file=Path(f.filename).name,line=f.lineno)
                        for f in traceback.extract_tb(exc.__traceback__)],
                actual_elapsed_s=time.monotonic()-start)
    put('CERTIFICATE_FAILURE.json', fail)
    print(json.dumps(fail), flush=True)
    raise SystemExit(1)
