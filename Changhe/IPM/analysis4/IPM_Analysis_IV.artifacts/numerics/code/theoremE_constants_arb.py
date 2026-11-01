"""Arb outward (upper-bound) certificate of the lead's Theorem E constants (code/rational_finite_order.py of the lead):
delta/2 = p/q in lowest terms, convergent denominators q_0 = 1, q_1, ..., q_K = q of the continued fraction of p/q,
B_rat = sum_{k=0}^{K-1} log(q_{k+1})/q_k,  lambda = 3/2 + delta/2 + 1/delta,  K_c = 2 lambda (L+2)/(c-1),
A = 8 K_c exp(2 B_rat) alpha_1 / delta,  with L the top frequency index... (lead: L+2 = B+1 where B = top frequency + 1).
All quantities are computed in 256-bit ball arithmetic and reported as rigorous upper bounds (arb.upper()).
usage: theoremE_constants_arb.py"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import fmpq, arb, ctx, fmpz
from fractions import Fraction
import math
ctx.prec = 256
def _frac(x):
    """exact rational value of an exact (zero-radius) arb"""
    m, e = x.man_exp(); m = int(m); e = int(e)
    return Fraction(m) * (Fraction(2) ** e)
def dec_upper(x, digits=20):
    """decimal string >= x.upper() (explicit outward rounding)"""
    f = _frac(x.upper()); q = Fraction(10) ** digits
    n = math.ceil(f * q); return f'{n // q.numerator}.{str(n % q.numerator).zfill(digits)}' if digits > 0 else str(n)
def dec_lower(x, digits=20):
    f = _frac(x.lower()); q = Fraction(10) ** digits
    n = math.floor(f * q); return f'{n // q.numerator}.{str(n % q.numerator).zfill(digits)}' if digits > 0 else str(n)
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def cf(p, q):
    a = []
    while q: a.append(p // q); p, q = q, p - (p // q) * q
    return a
def dens(a):
    q = [1, a[1]]
    for k in range(2, len(a)): q.append(a[k] * q[-1] + q[-2])
    return q
def constants(delta, alpha1, Ltop):
    """delta fmpq; alpha1 fmpq (exact l1 norm of f_1); Ltop = top frequency of f_1 (odd integer)"""
    half = delta / 2; p, q = int(half.p), int(half.q)
    a = cf(p, q); qs = dens(a)
    Brat = arb(0)
    for k in range(len(qs) - 1): Brat += arb(qs[k + 1]).log() / arb(qs[k])
    d = arb(delta); c = 1 / (1 - d)
    lam = arb(3) / 2 + d / 2 + 1 / d
    B = Ltop + 1                              # lead: B = top frequency + 1 ; factor (B+1) = L + 2 in the lead's code with L = top frequency
    Kc = 2 * lam * (B + 1) / (c - 1)
    A = 8 * Kc * (2 * Brat).exp() * arb(alpha1) / d
    R0 = (A.log() / d).exp()
    out = {'delta': str(delta), 'q_last': qs[-1], 'n_cf_terms': len(a), 'B_rat_upper': dec_upper(Brat, 20), 'B_rat_lower': dec_lower(Brat, 20),
           'lambda_ball': lam.str(20), 'K_c_upper': dec_upper(Kc, 20), 'A_upper': dec_upper(A, 12), 'A_lower': dec_lower(A, 12),
           'A_upper_integer': dec_upper(A, 0), 'log10_A_upper': dec_upper(A.log() / arb(10).log(), 12), 'R0_upper = A^(1/delta)': dec_upper(R0, 3), 'R0_lower': dec_lower(R0, 3),
           'A_ball': A.str(30), 'R0_ball': R0.str(30)}
    return out
d007 = fmpq(1824676646553933, 4076476460239181)
f1 = json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))['f1_sine_coefficients_exact']
alpha007 = sum(abs(fmpq(int(x.split('/')[0]), int(x.split('/')[1]))) for x in f1)
res = {'sin_theta_at_007_delta': constants(d007, fmpq(1), 1), 'cand007_profile_at_007_delta': constants(d007, alpha007, 19)}
for dl in (fmpq(4, 9), fmpq(1, 2), fmpq(2, 5), fmpq(9, 20), fmpq(2, 3)):
    res[f'sin_theta_at_delta_{dl.p}_{dl.q}'] = constants(dl, fmpq(1), 1)
res['alpha1_cand007_exact'] = str(alpha007); res['alpha1_cand007_float'] = float(alpha007)
res['note'] = 'rigorous bounds from 256-bit ball arithmetic with EXPLICIT OUTWARD decimal rounding (dec_upper = ceiling of the exact dyadic upper endpoint, dec_lower = floor of the lower endpoint); _ball fields are arb strings; formulas as in the lead code rational_finite_order.py (constants()); convention B = top frequency + 1 (factor B + 1 = L + 2)'
json.dump(res, open(os.path.join(LANE, 'notes', 'theoremE_constants_arb.json'), 'w'), indent=1)
for k, v in res.items():
    if isinstance(v, dict): print(k, {kk: vv for kk, vv in v.items() if kk in ('q_last', 'B_rat_upper', 'A_upper', 'A_lower', 'A_upper_integer', 'R0_upper = A^(1/delta)', 'A_ball')})
