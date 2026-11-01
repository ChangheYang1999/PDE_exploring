"""Exact QQ(k)[b,tau] Cartesian response calculation, c=3."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
import sys
sys.dont_write_bytecode = True
import sympy as sp
from sympy.polys.rings import ring
import tuned_cartesian_exact as ce

BASE = Path('research/136_three_mode_responses')
START = time.monotonic()
ce.R, ce.b, tau = ring('b,tau', ce.K.to_domain())
bs, ts, ks = sp.symbols('b tau k')


def save(name, data):
    (BASE/'verification'/name).write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({'stage': name, 'actual_elapsed_s': time.monotonic()-START}), flush=True)


def main():
    ff = {1: ce.sine(ce.p(1), 1) + ce.sine(ce.p(1), 3, ce.b) + ce.sine(ce.p(1), 5, tau)}
    gg = {1: ce.poisson(ff[1])}
    for n in (2, 3):
        acc = ce.F(ce.p(n), {})
        for i in range(1, n):
            acc = acc + ce.adv(gg[i], ff[n-i])
        ff[n] = acc.scale(ce.K(1)/(2*(n-1)))
        ff[n].check_sine()
        if n == 2:
            gg[n] = ce.poisson(ff[n])
    save('low_prefix.json', {'density': {str(n): ce.serial(v) for n, v in ff.items()},
                             'stream': {str(n): ce.serial(v) for n, v in gg.items()}})
    rows = []
    small = {}
    for k0 in range(2, 15):
        sig, response = ce.response(k0, ff, gg)
        small[k0] = sig
        expr = sp.factor(sig.as_expr())
        assert sp.Poly(expr, bs, ts).total_degree() <= 3
        rows.append({'k': k0, 'sigma': str(expr), 'response_support_sizes': [len(f.v) for f in response]})
        save('small_responses.json', {'rows': rows})
    sig, response = ce.response(ce.k, ff, gg)
    for f, window in zip(response, (5, 11, 17)):
        for slope, offset in f.v:
            assert abs(slope) == 2
            assert abs(offset+2 if slope == 2 else -offset+2) <= window
    expr = sp.factor(sig.as_expr())
    for k0 in range(10, 15):
        assert sp.cancel(expr.subs(ks, k0)-small[k0].as_expr()) == 0
    limit = sp.factor(sp.limit(expr, ks, sp.oo))
    assert sp.Poly(limit, bs, ts).total_degree() <= 3
    old = json.loads(Path('research/119_tuned_rational_series/verification/sigma_symbolic_exact.json').read_text())
    assert sp.cancel(expr.subs(ts, 0)-sp.sympify(old['sigma'])) == 0
    assert sp.cancel(limit.subs(ts, 0)-sp.sympify(old['sigma_infinity'])) == 0
    num, den = sp.fraction(expr)
    save('symbolic_response.json', {'sigma': str(expr), 'numerator': str(num), 'denominator': str(den),
                                    'sigma_infinity': str(limit), 'valid_from_k': 10,
                                    'direct_comparisons_at_10_through14': True,
                                    'two_mode_specializations_match': True,
                                    'response_fields': [ce.serial(f) for f in response]})
    source = json.loads(Path('research/125_explicit_compatible_shape/verification/obstruction_polynomial.json').read_text())
    obstruction = sp.sympify(source['expression'])
    p = sp.Poly(obstruction, bs, ts, domain=sp.QQ)
    assert p.total_degree() == 6
    assert p.coeff_monomial(bs**6) == sp.Rational(336578601, 68225597440)
    result = sp.factor(sp.resultant(obstruction, limit, bs))
    assert result != 0
    rp = sp.Poly(sp.fraction(result)[0], ts, domain=sp.QQ)
    roots = sp.polys.polytools.intervals(rp, eps=sp.Rational(1, 10**24))
    save('limiting_resultant.json', {'resultant': str(result), 'degree': rp.degree(),
                                    'coefficients_ascending': [str(v) for v in reversed(rp.all_coeffs())],
                                    'real_root_intervals': [{'interval': [str(a), str(b)], 'multiplicity': multiplicity}
                                                            for ((a,b),multiplicity) in roots],
                                    'interpretation': 'Projected candidate tau values; no real branch assignment is inferred.'})
    for name in ('three_mode_responses.py', 'tuned_cartesian_exact.py'):
        (BASE/'sources'/name).write_bytes(Path('code', name).read_bytes())
    save('checks.json', {'checked_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                         'all_checks_pass': True, 'actual_elapsed_s': time.monotonic()-START})
    manifest = {}
    for f in BASE.rglob('*'):
        if f.is_file() and f.name != 'MANIFEST.json':
            b = f.read_bytes()
            manifest[str(f.relative_to(BASE))] = {'bytes': len(b), 'sha256': sha256(b).hexdigest()}
    (BASE/'verification/MANIFEST.json').write_text(json.dumps({'files': manifest}, indent=2)+'\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        import traceback
        save('FAILURE.json', {'error_type': type(exc).__name__, 'error': str(exc),
                              'frames': [{'file': Path(f.filename).name, 'line': f.lineno}
                                         for f in traceback.extract_tb(exc.__traceback__)]})
        raise SystemExit(1)
