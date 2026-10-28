"""Third computation for verification topics 75 and 77 (conditional logarithmic linear inverse at beta = 1, and at
every logarithmic power 0 < beta <= 1).

Written from the statements of topics 75 and 77 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): even spatial moments of the integer powers P^n of P = (I + tau K)^-1, from the gamma
   mixture (outer shape n, Bessel shape a = tau U, heat time of shape a, 2D heat moments 2^j Gamma(1 + j/2) T^(j/2)):
   M2 = 4v, M4 = 32[v^2 + (tau + 1)v], v = n tau; the odd-moment bounds through Gamma(a + 1/2)/Gamma(a) <= sqrt(pi) a,
   expanded exactly as polynomials in v; their rational majorants with pi < 22/7 < 10/3; the low-kernel coefficients
   l1, l2, l3 of (9) from the topic 71 formula with sigma = 11/5; l1 < 8, l2 < 1, l3 < 1 at R = 2^31; the topic 75
   n = 1 coefficients 82/5, 34, 109, 2541/10, 352 and the bound 1 + 8 tau; the Frullani form of
   ((1 + tau z)/(1 + z))^beta with mass beta log(1/tau); the identity (1 + z)/(1 + tau z) = tau^-1 (1 - q/(1 + tau z));
   the generating-function sums S0 to S3 and their bounds; 1 + pi < 29/7; the rate, commutator and conversion
   inequalities 2^14, 1/29, 2^28 and (841/7)(2 + 16/1024) < 256.
2. FLOAT (mpmath): odd moments M1, M3, M5 of P^n by one-dimensional gamma quadrature against their bounds (several n,
   tau); M1 of B_(1,1) below pi/2; the scalar Laplace formula (6), the resolvent integral and the fractional-power
   integral of (16), (17); partial sums of the binomial series against S0 to S3 and the bound (14) on a grid of
   (beta, tau).

Usage: python3 check_p75_p77.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
chk, out = {}, {}
n, tau, v, a, z, q, bt, ta = sp.symbols('n tau v a z q beta tau_', positive=True)


def rising(xx, k):
    return sp.prod([xx + i for i in range(k)])


# 1. exact even moments: E|Z|^(2m) = 4^m m! E[T^m], E[T^m | a] = a^(m), E[(tau U)^k] = tau^k n^(k) (rising)
def even_moment(m):
    poly = sp.expand(rising(a, m))
    ea = sum(poly.coeff(a, k) * tau ** k * rising(n, k) for k in range(0, m + 1))
    return sp.expand(4 ** m * sp.factorial(m) * ea)


M2 = even_moment(1); M4 = even_moment(2)
chk['M2(P^n) = 4 v exactly'] = sp.expand(M2.subs(n, v / tau) - 4 * v) == 0
chk['M4(P^n) = 32[v^2 + (tau + 1) v] exactly'] = sp.expand(M4.subs(n, v / tau) - 32 * (v ** 2 + (tau + 1) * v)) == 0
# odd moments: 2^j Gamma(1 + j/2) E[Gamma(a + j/2)/Gamma(a)], Gamma(a + j/2)/Gamma(a) = (a + 1/2)...(a + j/2 - 1) G(a),
# G(a) = Gamma(a + 1/2)/Gamma(a) <= sqrt(pi) a; so M_j <= 2^j Gamma(1 + j/2) sqrt(pi) E[a (a + 1/2) ... ]
def odd_bound(j):
    pref = 2 ** j * sp.gamma(1 + sp.Rational(j, 2)) * sp.sqrt(sp.pi)
    poly = sp.expand(a * sp.prod([a + sp.Rational(1, 2) + i for i in range((j - 1) // 2)]))
    ea = sum(poly.coeff(a, k) * tau ** k * rising(n, k) for k in range(0, j + 1))
    return sp.expand(sp.simplify(pref * ea).subs(n, v / tau))


B1, B3, B5 = odd_bound(1), odd_bound(3), odd_bound(5)
chk['M1 bound = pi v'] = sp.simplify(B1 - sp.pi * v) == 0
chk['M3 bound = 6 pi [v^2 + (tau + 1/2) v]'] = sp.simplify(B3 - 6 * sp.pi * (v ** 2 + (tau + sp.Rational(1, 2)) * v)) == 0
chk['M5 bound = 60 pi [v^3 + (3 tau + 2) v^2 + (2 tau^2 + 2 tau + 3/4) v]'] = \
    sp.simplify(B5 - 60 * sp.pi * (v ** 3 + (3 * tau + 2) * v ** 2 + (2 * tau ** 2 + 2 * tau + sp.Rational(3, 4)) * v)) == 0
P_UP = F(10, 3)
chk['pi < 22/7 < 10/3'] = sp.pi < sp.Rational(22, 7) and F(22, 7) < P_UP
# majorants with tau <= 1
chk['6 pi <= 20 and 6 pi (tau + 1/2) <= 30 for tau <= 1'] = 6 * P_UP <= 20 and 6 * P_UP * F(3, 2) <= 30
chk['60 pi <= 200, 60 pi (3 tau + 2) <= 1000, 60 pi (2 tau^2 + 2 tau + 3/4) <= 1000 for tau <= 1'] = \
    60 * P_UP <= 200 and 60 * P_UP * 5 <= 1000 and 60 * P_UP * F(19, 4) <= 1000
chk['pi <= 4 and 4 = M2 coefficient; 32 (tau + 1) <= 64'] = P_UP <= 4 and 32 * 2 <= 64
# low-kernel formula of topic 71 with sigma = 11/5
sig = F(11, 5)
cf = [3 + sig / 2, 3 + 5 * sig / 2, 1 + 9 * sig / 2, 7 * sig / 2, sig]
chk['topic 71 coefficients 41/10, 17/2, 109/10, 77/10, 11/5'] = cf == [F(41, 10), F(17, 2), F(109, 10), F(77, 10), F(11, 5)]
R = F(2) ** 31
# moment majorants as (coef of v, v^2, v^3)
mom = [(4, 0, 0), (4, 0, 0), (30, 20, 0), (64, 32, 0), (1000, 1000, 200)]
l = [sum(cf[k] * mom[k][p] / R ** (k + 1) for k in range(5)) for p in range(3)]
l1x = F(82, 5) / R + 34 / R ** 2 + 327 / R ** 3 + F(2464, 5) / R ** 4 + 2200 / R ** 5
l2x = 218 / R ** 3 + F(1232, 5) / R ** 4 + 2200 / R ** 5
l3x = 440 / R ** 5
chk['l1, l2, l3 of topic 77 exactly'] = l == [l1x, l2x, l3x]
chk['l1 < 8, l2 < 1, l3 < 1 at R = 2^31 (so (9) dominates both component factors 1 + 8v and the low factor)'] = \
    l1x < 8 and l2x < 1 and l3x < 1 and 2 * 4 <= 8
# topic 75 n = 1 coefficients: M1 <= 4 tau, M2 = 4 tau, M3 <= 10 tau, M4 <= 33 tau, M5 <= 160 tau for tau <= 2^-12
T12 = F(1, 2 ** 12)
chk['topic 75 moment majorants (4, 4, 10, 33, 160) tau at tau <= 2^-12'] = \
    P_UP <= 4 and 6 * F(22, 7) * (2 * T12 + F(1, 2)) <= 10 and 32 * (2 * T12 + 1) <= 33 and \
    60 * F(22, 7) * (6 * T12 ** 2 + 4 * T12 + F(3, 4)) <= 160
c75 = [cf[k] * [4, 4, 10, 33, 160][k] for k in range(5)]
chk['topic 75 low coefficients 82/5, 34, 109, 2541/10, 352'] = c75 == [F(82, 5), 34, 109, F(2541, 10), 352]
chk['topic 75 ||B_tau|| <= 1 + 8 tau: 2 pi < 8 and the low excess below 8 tau'] = \
    2 * F(22, 7) < 8 and sum(c75[k] / R ** (k + 1) for k in range(5)) < 8
# Frullani form (11): d/dz of the exponent and its value at z = 0
tt = sp.symbols('t', positive=True)
expo = -sp.integrate((1 - sp.exp(-tt * z)) * (sp.exp(-tt) - sp.exp(-tt / tau)) / tt, (tt, 0, sp.oo), conds='none')
chk['(11): log((1 + tau z)/(1 + z)) = -int (1 - e^-tz)(e^-t - e^(-t/tau))/t dt (z-derivative)'] = \
    sp.simplify(sp.diff(sp.log(1 + tau * z) - sp.log(1 + z), z)
                + sp.integrate(sp.exp(-tt * z) * (sp.exp(-tt) - sp.exp(-tt / tau)), (tt, 0, sp.oo), conds='none')) == 0
mass = sp.integrate((sp.exp(-tt) - sp.exp(-tt / tau)) / tt, (tt, 0, sp.oo), conds='none')
chk['(11): mass of nu equals beta log(1/tau)'] = sp.simplify(mass - sp.log(1 / tau)) == 0
chk['(13): (1 + z)/(1 + tau z) = tau^-1 (1 - (1 - tau)/(1 + tau z))'] = \
    sp.simplify((1 + z) / (1 + tau * z) - (1 - (1 - tau) / (1 + tau * z)) / tau) == 0
# S_k = (q d/dq)^k [1 - (1 - q)^beta], tau = 1 - q
# write q = 1 - ta with ta > 0, so q d/dq = -(1 - ta) d/dta
gq = 1 - ta ** bt
Sk = [gq]
for k in range(3):
    Sk.append(sp.simplify(-(1 - ta) * sp.diff(Sk[-1], ta)))
q = 1 - ta
Sx = [1 - ta ** bt, bt * q * ta ** (bt - 1), bt * q * ta ** (bt - 1) + bt * (1 - bt) * q ** 2 * ta ** (bt - 2),
      bt * q * ta ** (bt - 1) + 3 * bt * (1 - bt) * q ** 2 * ta ** (bt - 2) + bt * (1 - bt) * (2 - bt) * q ** 3 * ta ** (bt - 3)]
chk['S0 to S3 by differentiating 1 - (1 - q)^beta'] = all(sp.simplify(Sk[k] - Sx[k]) == 0 for k in range(4))
chk['a_n = (-1)^(n+1) binom(beta, n) >= 0 for 0 < beta < 1 (n <= 40, beta = 1/3, 1/2, 9/10)'] = \
    all((-1) ** (m + 1) * sp.binomial(sp.Rational(p, 30), m) >= 0 for p in (10, 15, 27) for m in range(1, 41))
# bounds tau S1 <= beta tau^beta, tau^2 S2 <= 2 beta tau^beta, tau^3 S3 <= 6 beta tau^beta: termwise with q <= 1, tau <= 1
chk['termwise: tau S1 = beta q tau^beta; tau^2 S2 = beta q tau^(beta+1) + beta(1-beta) q^2 tau^beta; tau^3 S3 similar'] = \
    sp.simplify(ta * Sx[1] - bt * q * ta ** bt) == 0 and \
    sp.simplify(ta ** 2 * Sx[2] - (bt * q * ta ** (bt + 1) + bt * (1 - bt) * q ** 2 * ta ** bt)) == 0 and \
    sp.simplify(ta ** 3 * Sx[3] - (bt * q * ta ** (bt + 2) + 3 * bt * (1 - bt) * q ** 2 * ta ** (bt + 1)
                                   + bt * (1 - bt) * (2 - bt) * q ** 3 * ta ** bt)) == 0
chk['coefficient sums 1 + (1 + 1) + (1 + 3 + 2) = 1, 2, 6 and 8 + 2 + 6 = 16'] = 1 + 1 == 2 and 1 + 3 + 2 == 6 and 8 + 2 + 6 == 16
chk['(12): 1 + pi < 29/7'] = 1 + F(22, 7) == F(29, 7) and sp.pi < sp.Rational(22, 7)
C0 = F(9325421, 600)
chk['(17): C0 (1 + 8 tau)^3 < 2^14 for tau <= 2^-12'] = C0 * (1 + 8 * T12) ** 3 < 2 ** 14
T20 = F(1, 2 ** 20)
chk['(18): 1/20 - C0 tau (1 + 8 tau)^3 > 1/29 at tau = 2^-20'] = F(1, 20) - C0 * T20 * (1 + 8 * T20) ** 3 > F(1, 29)
chk['topic 75: 29 (29/7)(2/tau + 7) < 2^28 at tau = 2^-20'] = 29 * F(29, 7) * (2 * 2 ** 20 + 7) < 2 ** 28
chk['(5): (841/7)(2 + 16/1024) < 256'] = F(841, 7) * (2 + F(16, 1024)) < 256
out['exact'] = {'l1': str(l1x), 'l2': str(l2x), 'l3': str(l3x), 'C0': str(C0),
                'rate_margin_tau_2^-20': str(F(1, 20) - C0 * T20 * (1 + 8 * T20) ** 3 - F(1, 29)),
                'conversion_beta1': str(29 * F(29, 7) * (2 * 2 ** 20 + 7)), 'conversion_factor_beta_ge_half': str(F(841, 7) * (2 + F(16, 1024)))}

# 2. FLOAT
mpmath.mp.dps = 30
def odd_moment(j, nn, tt_):
    pref = 2 ** j * mpmath.gamma(1 + mpmath.mpf(j) / 2)
    f = lambda U: U ** (nn - 1) * mpmath.exp(-U) / mpmath.gamma(nn) * \
        mpmath.exp(mpmath.loggamma(tt_ * U + mpmath.mpf(j) / 2) - mpmath.loggamma(tt_ * U))
    return pref * mpmath.quad(f, [0, 1, nn, 4 * nn + 40, mpmath.inf])
fl = {}; okm = True
for nn in (1, 3, 20):
    for tt_ in (mpmath.mpf(2) ** -12, mpmath.mpf(1) / 7, mpmath.mpf(1)):
        vv = nn * tt_
        m1, m3, m5 = odd_moment(1, nn, tt_), odd_moment(3, nn, tt_), odd_moment(5, nn, tt_)
        b1 = mpmath.pi * vv; b3 = 6 * mpmath.pi * (vv ** 2 + (tt_ + 0.5) * vv)
        b5 = 60 * mpmath.pi * (vv ** 3 + (3 * tt_ + 2) * vv ** 2 + (2 * tt_ ** 2 + 2 * tt_ + 0.75) * vv)
        okm = okm and m1 <= b1 and m3 <= b3 and m5 <= b5
        fl[f'n={nn},tau={float(tt_):.6g}'] = [float(m1 / b1), float(m3 / b3), float(m5 / b5)]
chk['odd moments M1, M3, M5 of P^n below their bounds (FLOAT quadrature)'] = okm
m1B = odd_moment(1, 1, mpmath.mpf(1))
chk['M1(B_(1,1)) <= pi/2 (FLOAT)'] = m1B <= mpmath.pi / 2
okl = True
def halfline(f, wmax=400):
    # int_0^oo f(s) ds through s = exp(w), which turns the power-law ends into exponential ones; the integrands below
    # are O(exp(-|w|/4)) at both ends, so the cut at |w| = 400 changes them by less than 1e-40
    return mpmath.quad(lambda w: f(mpmath.exp(w)) * mpmath.exp(w), [-400, -40, -10, 0, 10, 40, wmax])
for be in (mpmath.mpf('0.3'), mpmath.mpf('0.75')):
    for k in (mpmath.mpf('0.5'), mpmath.mpf(7)):
        # k plays the role of |xi|^2; K has symbol log(1 + k) and J^(-2a) has symbol (1 + k)^-a
        lhs = (1 + mpmath.mpf(2) ** -12 * mpmath.log(1 + k)) ** -be
        rhs = halfline(lambda u: mpmath.exp(-u) * u ** (be - 1) * (1 + k) ** (-mpmath.mpf(2) ** -12 * u), wmax=7) / mpmath.gamma(be)
        okl = okl and abs(lhs - rhs) < 1e-15
        # fractional power integral and resolvent identity of (16) with scalar Q = 1 + tau k
        Qs = 1 + mpmath.mpf(2) ** -12 * k
        pw = mpmath.sin(mpmath.pi * be) / mpmath.pi * halfline(lambda s: s ** (be - 1) * Qs / (s + Qs))
        okl = okl and abs(pw - Qs ** be) < 1e-15
    ri = halfline(lambda s: s ** be / (1 + s) ** 2)
    okl = okl and abs(ri - be * mpmath.pi / mpmath.sin(mpmath.pi * be)) < 1e-15
chk['(6), the power integral of (16) and the resolvent integral of (17) (FLOAT)'] = okl
okb = True; worst = 0.0
for be in (0.1, 0.3, 0.5, 0.75, 0.95):
    for tt_ in (2.0 ** -20, 2.0 ** -12, 0.01, 0.3):
        qq = 1 - tt_
        an = 1.0; s0 = s1 = s2 = s3 = 0.0
        for m in range(1, 200000 if tt_ >= 0.01 else 2):
            an *= (m - 1 - be) / m if m > 1 else be
            term = an * qq ** m
            s0 += term; s1 += term * m; s2 += term * m * m; s3 += term * m ** 3
            if term * m ** 3 < 1e-18 * max(s3, 1) and m > 50:
                break
        e0 = 1 - tt_ ** be; e1 = be * qq * tt_ ** (be - 1)
        e2 = be * qq * tt_ ** (be - 1) + be * (1 - be) * qq ** 2 * tt_ ** (be - 2)
        e3 = be * qq * tt_ ** (be - 1) + 3 * be * (1 - be) * qq ** 2 * tt_ ** (be - 2) + be * (1 - be) * (2 - be) * qq ** 3 * tt_ ** (be - 3)
        if tt_ >= 0.01:
            okb = okb and all(abs(u_ - w_) < 1e-9 * max(1, w_) for u_, w_ in ((s0, e0), (s1, e1), (s2, e2), (s3, e3)))
        lhs = tt_ ** -be * (1 + e0 + 8 * tt_ * e1 + tt_ ** 2 * e2 + tt_ ** 3 * e3)
        okb = okb and lhs < 2 * tt_ ** -be + 16
        worst = max(worst, lhs / (2 * tt_ ** -be + 16))
chk['binomial partial sums equal S0 to S3 (tau >= 0.01) and the closed forms satisfy (14) on a grid of (beta, tau) (FLOAT)'] = okb
out['FLOAT'] = {'odd_moment_ratios': fl, 'M1_B11': float(m1B), 'worst_ratio_14': worst}
out['checks'] = {k: bool(v) for k, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k for k, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
