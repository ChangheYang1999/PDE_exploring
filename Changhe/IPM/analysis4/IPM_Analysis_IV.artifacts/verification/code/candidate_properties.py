"""Exact sign and monotonicity certificates for the extracted leading profile."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from math import comb
from pathlib import Path

from flint import arb, fmpq, ctx
from gmpy2 import mpq
import sympy as sp

src = Path('research/02_candidate007/data/leading_exact.json')
data = json.loads(src.read_text())
a = {int(k): sp.Rational(v) for k, v in data['density'].items()}
t = sp.Symbol('t')
P = sp.Poly(0, t)
for m, value in a.items():
    basis = sum((-1)**j*comb(m, 2*j+1)*(1-t)**((m-1)//2-j)*t**j
                for j in range((m+1)//2))
    P += sp.Poly(value*basis, t)
Q = P+2*sp.Poly(t,t)*P.diff()
sturm = Q.sturm()


def signs_at(x):
    return [int(sp.sign(poly.eval(x))) for poly in sturm]


def variations(signs):
    signs = [v for v in signs if v]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def frac(x):
    return f'{sp.numer(x)}/{sp.denom(x)}'


s0, s1 = signs_at(0), signs_at(1)
root_count = variations(s0)-variations(s1)
assert root_count == 1
assert Q.eval(0) > 0 > Q.eval(1)
left, right = sp.Rational(0), sp.Rational(1)
for _ in range(60):
    mid = (left+right)/2
    if Q.eval(mid) > 0:
        left = mid
    else:
        right = mid
assert Q.eval(left) > 0 > Q.eval(right)
margin = a[1]-sum(m*abs(value) for m, value in a.items() if m != 1)
assert margin > sp.Rational('6.75')
curvature = -Q.eval(1)
assert sp.Rational('4.4495') < curvature < sp.Rational('4.4496')
ctx.prec = 256
norm_sq_pi = sum(value*value for value in a.values())/4
norm = (arb.pi()*arb(fmpq(int(sp.numer(norm_sq_pi)),
                         int(sp.denom(norm_sq_pi))))).sqrt()
lo, hi = '16.5710002630288', '16.5710002630289'
assert arb(lo) < norm < arb(hi)
result = {
    'date_utc': datetime.now(timezone.utc).isoformat(),
    'input': src.as_posix(), 'input_sha256': sha256(src.read_bytes()).hexdigest(),
    'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'P_coefficients_ascending': [frac(P.nth(i)) for i in range(P.degree()+1)],
    'Q_coefficients_ascending': [frac(Q.nth(i)) for i in range(Q.degree()+1)],
    'sturm_signs_0': s0, 'sturm_signs_1': s1,
    'sturm_variations_0': variations(s0), 'sturm_variations_1': variations(s1),
    'sturm_roots_in_0_1': root_count,
    'maximum_sin_squared_bracket': [frac(left), frac(right)],
    'strict_positivity_margin_exact': frac(margin),
    'strict_positivity_margin_lower': '27/4',
    'second_derivative_pi_over_2_exact': frac(curvature),
    'quarter_norm_squared_over_pi': frac(norm_sq_pi),
    'quarter_norm_bracket': [lo, hi], 'arb_precision_bits': 256,
    'quarter_norm_arb_display': str(norm),
    'maximum_sin_squared_approx': float((left+right)/2),
}
out = Path('research/02_candidate007/verification/properties.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({key: result[key] for key in (
    'sturm_variations_0', 'sturm_variations_1', 'sturm_roots_in_0_1',
    'maximum_sin_squared_approx', 'quarter_norm_bracket')}, indent=2))
