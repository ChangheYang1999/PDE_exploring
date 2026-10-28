"""Third computation for verification topic 60 (seven-branch weighted floor): the exact exponent comparisons, the
moments of b_0 = (t - 1)^2 (2 - t)^2, the symmetrized determinant, an interval enclosure of
J_* = I(p + 1) [M(q + 1) - M(p + 1)] with M(z) = I(z + 1)/I(z), the rational bound J_* > 1/67200 and the integrals (11).
Written from the statement of topic 60 only. Usage: python3 check_p60.py [OUTPUT_JSON]"""
import json, sys, hashlib
from fractions import Fraction as Q
from pathlib import Path
from mpmath import iv
iv.prec = 300
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
I_ = lambda q: iv.mpf(Q(q).numerator) / Q(q).denominator
lo = lambda x: Q(x.a.man) * Q(2) ** x.a.exp if x.a.man else Q(0)
c = Q(4076476460239181, 2251799813685248); g = 1 / c; d = 1 - g
q = g - 2 * d - 2; p = g - 7 * d; beta = 2 - 4 * d
out = {'q': float(q), 'p': float(p), 'beta': float(beta)}
ex = {'q=-1-3delta': q == -1 - 3 * d, 'p=1-8delta': p == 1 - 8 * d, 'q>p': q > p, 'q<-2': q < -2, 'p<-2': p < -2,
      '0<beta<delta': 0 < beta < d, 'p-beta=gamma-3delta-2': p - beta == g - 3 * d - 2, 'gamma-4<p-beta': g - 4 < p - beta,
      'p-delta<p-beta': p - d < p - beta, 'p-beta+1<0': p - beta + 1 < 0, 'q+1<0': q + 1 < 0,
      '0<d<1': 0 < q - p < 1, 'd>1/5': q - p > Q(1, 5), 'p+q+1>-4': p + q + 1 > -4,
      'delta_denominator': (d.denominator, d.denominator > 13)}
# nonresonance: (h' - h) delta = 2 (n - n') has no solution with 0 < |h - h'| <= 13
ex['nonresonant'] = all((k * d).denominator != 1 for k in range(1, 14))
out['exponents'] = {k: (v if isinstance(v, bool) else str(v)) for k, v in ex.items()}
assert all(v for k, v in ex.items() if isinstance(v, bool))
# b_0 polynomial in t
b0 = [Q(4), Q(-12), Q(13), Q(-6), Q(1)]                         # (t-1)^2 (2-t)^2 = t^4 - 6t^3 + 13t^2 - 12t + 4
def I_exact(k):                                                  # integer moment
    return sum((cf * (Q(2) ** (k + j + 1) - 1) / (k + j + 1) for j, cf in enumerate(b0)), Q(0))
def I_iv(z):
    z = I_(z)
    return sum((I_(cf) * (iv.mpf(2) ** (z + j + 1) - 1) / (z + j + 1) for j, cf in enumerate(b0)), iv.mpf(0))
mom = {'I0': I_exact(0), 'I1': I_exact(1), 'I2': I_exact(2)}
out['moments'] = {k: str(v) for k, v in mom.items()}
assert mom == {'I0': Q(1, 30), 'I1': Q(1, 20), 'I2': Q(8, 105)}
out['determinant_1/25200'] = mom['I0'] * mom['I2'] - mom['I1'] ** 2 == Q(1, 25200)
# J_* by interval arithmetic
cstar = I_iv(q + 2) / I_iv(q + 1)
J = cstar * I_iv(p + 1) - I_iv(p + 2)
annih = cstar * I_iv(q + 1) - I_iv(q + 2)
out['c_star'] = [float(cstar.a), float(cstar.b)]; out['J_star'] = [float(J.a), float(J.b)]
out['annihilation_width'] = float(abs(annih).b)
out['1<c_star<2'] = bool(cstar.a > 1 and cstar.b < 2)
out['J_star>1/67200'] = bool(J.a > I_(Q(1, 67200)).b)
out['J_star/(1/67200)'] = float(J.a * 67200)
# rational chain: d 2^(p+q+1)/840 > 1/67200 using d > 1/5 and p+q+1 > -4
out['chain_(1/5)2^-4/840=1/67200'] = Q(1, 5) * Q(1, 16) / 840 == Q(1, 67200)
# integrals (11): int b0 = 1/30, int t b0'^2 = 1/35, int b0^2 = 1/630, int t b0^2 = 1/420
def pmul(a, b):
    r = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
pint = lambda P: sum((cf * (Q(2) ** (k + 1) - 1) / (k + 1) for k, cf in enumerate(P)), Q(0))
db0 = [k * b0[k] for k in range(1, 5)]
ints = {'int_b0': pint(b0), 'int_t_b0p^2': pint(pmul([Q(0), Q(1)], pmul(db0, db0))), 'int_b0^2': pint(pmul(b0, b0)),
        'int_t_b0^2': pint(pmul([Q(0), Q(1)], pmul(b0, b0)))}
out['integrals'] = {k: str(v) for k, v in ints.items()}
assert ints == {'int_b0': Q(1, 30), 'int_t_b0p^2': Q(1, 35), 'int_b0^2': Q(1, 630), 'int_t_b0^2': Q(1, 420)}
# 15 J_* E_0 > E_0/4480 and P_T > T^(p+2) E_0^2/134400 follow from J_* > 1/67200
out['15/67200=1/4480'] = Q(15, 67200) == Q(1, 4480); out['2*67200=134400'] = 2 * 67200 == 134400
# mu_70 = sin^2(pi/282) > 1/8100
mu70 = iv.sin(iv.pi / 282) ** 2
out['mu_70'] = float(mu70.a); out['mu_70>1/8100'] = bool(mu70.a > I_(Q(1, 8100)).b)
out['nu_formula_consistent_with_N60'] = Q(7000, 33 * 12000) == Q(7, 396)
assert out['determinant_1/25200'] and out['1<c_star<2'] and out['J_star>1/67200'] and out['mu_70>1/8100']
assert out['chain_(1/5)2^-4/840=1/67200'] and out['15/67200=1/4480'] and out['nu_formula_consistent_with_N60']
out['all_pass'] = True
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print(json.dumps(out, indent=1)); print('DONE')
