"""Third computation for verification topics 80 to 85 (homogeneous logarithmic low product; Lipschitz logarithmic
transport commutators; logarithmic multiplication by a profile derivative; the native low logarithmic energy;
native logarithmic products; the conditional nonlinear theorem with logarithmic surplus).

Written from the statements of topics 80 to 85 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): every rational comparison of the six proofs, the partition constant K0 = 2595/2048, the
   dyadic sum below 31/4 (closed form), the heat moments 2^m Gamma(1 + m/2) t^(m/2), the commutator constants
   C_j = 2^(j+1) Gamma((j+4)/2) Gamma(j/2), the commutator symbol [m(D), x_j d_j] = (xi_j d_j m)(D) for K (the
   sharpness symbol of topic 81 and the dilation commutator 2(I - J^-2)), the resolvent integral beta, the weighted
   kernel integral of topic 83 (9), the Young steps of the native interpolation, the binomial sums of topic 84, the
   radial Fourier integral of topic 84, the energy coefficients of topic 85 (16) to (27), the first-order identity
   (25) and the nonlinear b-identity on polynomial models, and the threshold arithmetic eta < 2^-37.
2. FLOAT: the commutator bound ||[K, W.grad]|| <= 2 ||DW||_op on the torus (same flow proof) for a trigonometric
   divergence-free W, exactly band-limited so the spectral products have no aliasing; random sampling of the
   frequency-difference bound (5) of topic 82; radial sampling of omega0^2/w <= omega1 and |D(omega0^2/w)| <= 5 omega0.

Usage: python3 check_p80_p85.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
chk, out = {}, {}
PI_LO, PI_HI = F(333, 106), F(22, 7)  # 333/106 < pi < 22/7
assert sp.Rational(333, 106) < sp.pi < sp.Rational(22, 7)
t, r, u, z, bt, a, k = sp.symbols('t r u z beta a k', positive=True)

# ---------------- topic 80 ----------------
chk['80: 507 = 3 + 54 + 450, 40 = 4 + 36, K0 = 1 + (507 + 40)/2048 = 2595/2048'] = \
    507 == 3 + 54 + 450 and 40 == 4 + 36 and 1 + F(507 + 40, 2048) == F(2595, 2048)
x = sp.Integer(2) ** sp.Rational(-4, 5)
dyad = 1 / (1 - x) + 2 * sp.log(2) * x / (1 - x) ** 2   # sum_j x^j (1 + 2 j log 2)
chk['80: sum_(j >= 0) 2^(-4j/5)(1 + 2j log 2) = 1/(1-x) + 2 log2 x/(1-x)^2 < 31/4'] = \
    bool(sp.N(dyad, 30) < sp.Rational(31, 4)) and \
    abs(sum(float(x) ** j * (1 + 2 * j * math.log(2)) for j in range(400)) - float(dyad)) < 1e-12
out['80_dyadic_sum'] = float(dyad)
chk['80: K0^2 (31/4)^2 < 64 pi (with pi > 333/106)'] = F(2595, 2048) ** 2 * F(31, 4) ** 2 < 64 * PI_LO
chk['80: (1 + 2u) e^(-8u/5) has its maximum (5/4) e^(-1/5) <= 5/4 at u = 1/8'] = \
    sp.solve(sp.diff((1 + 2 * u) * sp.exp(-8 * u / 5), u), u) == [sp.Rational(1, 8)] and \
    sp.simplify(((1 + 2 * u) * sp.exp(-8 * u / 5)).subs(u, sp.Rational(1, 8)) - sp.Rational(5, 4) * sp.exp(-sp.Rational(1, 5))) == 0
chk['80: 380 = 5 * 76 and 380^2 * 5 * (29/7)^4 < 2^28 (so 380 sqrt5 (1 + pi)^2 < 2^14)'] = \
    380 == 5 * 76 and 380 ** 2 * 5 * F(29, 7) ** 4 < 2 ** 28 and 1 + PI_HI == F(29, 7)
chk['80: (13/3)(2^14 + 4) < 2^17'] = F(13, 3) * (2 ** 14 + 4) < 2 ** 17

# ---------------- topic 81 ----------------
pt = sp.exp(-r ** 2 / (4 * t)) / (4 * sp.pi * t)
okm = all(sp.simplify(sp.integrate(r ** m * pt * 2 * sp.pi * r, (r, 0, sp.oo)) - 2 ** m * sp.gamma(1 + sp.Rational(m, 2)) * t ** sp.Rational(m, 2)) == 0
          for m in range(0, 7))
chk['81: planar heat moments int |Z|^m p_t = 2^m Gamma(1 + m/2) t^(m/2), m = 0..6'] = okm
Cj = []
for j in range(1, 5):
    inner = sp.integrate(r ** (j + 1) * (r / (2 * t)) * pt * 2 * sp.pi * r, (r, 0, sp.oo))   # int |Z|^(j+1) |Dp_t|
    cj = sp.simplify(sp.integrate(sp.exp(-t) / t * inner, (t, 0, sp.oo)))
    Cj.append(cj)
chk['81: C_j = 2^(j+1) Gamma((j+4)/2) Gamma(j/2) = 3 pi, 16, 15 pi, 192 by direct integration'] = \
    all(sp.simplify(Cj[j - 1] - 2 ** (j + 1) * sp.gamma(sp.Rational(j + 4, 2)) * sp.gamma(sp.Rational(j, 2))) == 0 for j in range(1, 5)) and \
    [sp.simplify(c) for c in Cj] == [3 * sp.pi, 16, 15 * sp.pi, 192]
chk['81: K = int e^-t (1 - e^(-t k)) dt/t has symbol log(1 + k) (k-derivative and value at 0)'] = \
    sp.simplify(sp.integrate(sp.exp(-t) * sp.exp(-t * k), (t, 0, sp.oo)) - 1 / (1 + k)) == 0
x1, x2, d = sp.symbols('xi1 xi2 d', real=True)
G = sp.Function('G')(x1, x2)
m_sym = sp.log(1 + x1 ** 2 + x2 ** 2)


def comm_xd(mm, j):
    # Fourier side of [m(D), x_j d_j] applied to G: F(x_j d_j f) = -d_(xi_j)(xi_j fhat)
    xi = (x1, x2)[j]
    return -mm * sp.diff(xi * G, xi) + sp.diff(xi * mm * G, xi)


sharp = d * (comm_xd(m_sym, 0) - comm_xd(m_sym, 1))
chk['81 (8): [K, d(x d_x - y d_y)] has symbol 2d(xi1^2 - xi2^2)/(1 + |xi|^2)'] = \
    sp.simplify(sharp - 2 * d * (x1 ** 2 - x2 ** 2) / (1 + x1 ** 2 + x2 ** 2) * G) == 0
chk['81: the multiplier 2(xi1^2 - xi2^2)/(1 + |xi|^2) has supremum 2 (limit along the xi1 axis)'] = \
    sp.limit(2 * x1 ** 2 / (1 + x1 ** 2), x1, sp.oo) == 2 and \
    sp.simplify(2 - 2 * (x1 ** 2 - x2 ** 2) / (1 + x1 ** 2 + x2 ** 2) - 2 * (1 + 2 * x2 ** 2) / (1 + x1 ** 2 + x2 ** 2)) == 0
chk['81: weight constants 2 + 2 C_1 = 2 + 6 pi < 21 and 2 + 2 C_1 + C_2 = 18 + 6 pi < 37'] = \
    2 + 6 * PI_HI < 21 and 18 + 6 * PI_HI < 37
zz = sp.symbols('zz', positive=True)
chk['81 (4): (1 + z)^3 - 1 = 3z + 3z^2 + z^3 gives 2 + 9 pi/R + 48/R^2 + 15 pi/R^3'] = \
    sp.expand((1 + zz) ** 3 - 1 - (3 * zz + 3 * zz ** 2 + zz ** 3)) == 0 and \
    sp.simplify(3 * Cj[0] - 9 * sp.pi) == 0 and 3 * Cj[1] == 48 and sp.simplify(Cj[2] - 15 * sp.pi) == 0
chk['81: omega0 and w_R moderation exponents 6/5 <= 2 and 11/5 <= 3'] = F(6, 5) <= 2 and F(11, 5) <= 3
okb = all(sp.simplify(sp.sin(sp.pi * b_) / sp.pi * sp.integrate(u ** b_ / (1 + u) ** 2, (u, 0, sp.oo)) - b_) == 0
          for b_ in (sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(3, 4)))
chk['81 (13): [sin(pi beta)/pi] int lambda^beta/(1 + lambda)^2 = beta (beta = 1/3, 1/2, 3/4)'] = okb
lam, tau = sp.symbols('lambda tau', positive=True)
chk['81 (12): (lambda + 1 + tau k)^-1 = (1 + lambda)^-1 (1 + (tau/(1 + lambda)) k)^-1'] = \
    sp.simplify(1 / (lam + 1 + tau * k) - 1 / (1 + lam) / (1 + tau / (1 + lam) * k)) == 0
Aop = sp.symbols('A', positive=True)
chk['81 (13): A (lambda + A)^-1 = I - lambda (lambda + A)^-1 (scalar form of the resolvent step)'] = \
    sp.simplify(Aop / (lam + Aop) - (1 - lam / (lam + Aop))) == 0

# ---------------- topic 82 ----------------
p, q_ = sp.symbols('p q', positive=True)   # |xi|, |eta|
chk['82: 2(1 + p^2)(1 + q^2) - (1 + (p + q)^2) = 1 + (p - q)^2 ... >= 0 (so 1 + |xi + eta|^2 <= 2(1 + |xi|^2)(1 + |eta|^2))'] = \
    sp.expand(2 * (1 + p ** 2) * (1 + q_ ** 2) - (1 + (p + q_) ** 2) - (1 + (p - q_) ** 2 + 2 * p ** 2 * q_ ** 2)) == 0
chk['82: tau log 2 < 1 for tau <= 1 and 2|z|/(1 + |z|^2) <= 1'] = \
    sp.log(2) < 1 and sp.expand((1 + z ** 2) - 2 * z - (1 - z) ** 2) == 0
chk['82: J m <= sqrt2 |xi|: 2p^2 - (1 + p^2) p^2 = p^2 (1 - p^2) (p <= 1), 2p^2 - (1 + p^2) = p^2 - 1 (p >= 1); 5 sqrt2 < 8 (50 < 64)'] = \
    sp.expand(2 * p ** 2 - (1 + p ** 2) * p ** 2 - p ** 2 * (1 - p ** 2)) == 0 and sp.expand(2 * p ** 2 - (1 + p ** 2) - (p ** 2 - 1)) == 0 and 50 < 64
okk = all(sp.simplify(b_ / sp.gamma(1 - b_) * sp.integrate(sp.exp(-u) * u ** (-1 - b_) * sp.pi * tau * u, (u, 0, sp.oo)) - sp.pi * tau * b_) == 0
          for b_ in (sp.Rational(1, 3), sp.Rational(2, 3)))
chk['82 (7): [beta/Gamma(1 - beta)] int e^-u u^(-1-beta) (pi tau u) du = pi tau beta'] = okk
v = 2 * PI_HI
chk['82: v = 2 pi tau beta <= 2 pi: 1 + 2v + 2v^2 < 100 and 8(1 + v + v^2) < 400'] = 1 + 2 * v + 2 * v ** 2 < 100 and 8 * (1 + v + v ** 2) < 400
vv = sp.symbols('v', positive=True)
Aa, Dd, ts = sp.symbols('A D s', positive=True)
coef = Aa * (1 + vv + vv ** 2) + 8 * ts * Dd * (1 + vv + vv ** 2) + vv * Aa * (1 + vv)
chk['82: combined coefficient (1 + 2v + 2v^2) A + 8 (1 + v + v^2) tau^(-1/2) D'] = \
    sp.expand(coef - ((1 + 2 * vv + 2 * vv ** 2) * Aa + 8 * (1 + vv + vv ** 2) * ts * Dd)) == 0
chk['82 (4): 100 * 4 + 400 = 800 with tau^(-1/2) <= tau^(-beta), eps <= 1'] = 100 * 4 + 400 == 800

# ---------------- topic 83 ----------------
chk['83 (6): M1 + 2 M2 <= (pi + 8) tau beta < 12 tau'] = PI_HI + 8 < 12
e_, P0, P1, L = sp.symbols('e P0 P1 L', positive=True)
y1 = sp.expand(e_ / 2 * P1 ** 2 + L ** 2 / (2 * e_) - L * P1 - (sp.sqrt(e_ / 2) * P1 - L / sp.sqrt(2 * e_)) ** 2)
y2 = sp.expand(P0 ** 2 / 2 + 25 * L ** 2 / 2 - 5 * L * P0 - (P0 / sp.sqrt(2) - 5 * L / sp.sqrt(2)) ** 2)
chk['83 (7): Young steps L P1 <= (e/2) P1^2 + L^2/(2e), 5 L P0 <= P0^2/2 + 25 L^2/2 give P0^2 <= e P1^2 + (25 + 1/e) L^2'] = \
    sp.simplify(y1) == 0 and sp.simplify(y2) == 0 and \
    sp.simplify(2 * (e_ / 2 * P1 ** 2 + L ** 2 / (2 * e_) + 25 * L ** 2 / 2) - (e_ * P1 ** 2 + (25 + 1 / e_) * L ** 2)) == 0
Rr = sp.symbols('R', positive=True)
chk['83: omega0^2/w <= omega1 since 1 + r^2/R^2 <= 1 + r^2 for R >= 1 (exponents -12/5 + 11/5 = -1/5)'] = \
    F(-12, 5) + F(11, 5) == F(-1, 5)
chk['83: 12/5 + 11/5 = 23/5 < 5 (the two terms of |D(omega0^2/w)|/omega0)'] = F(12, 5) + F(11, 5) < 5
aa_, bb_ = sp.symbols('a b', positive=True)
chk['83: (101/100) a^2 + 101 b^2 - (a + b)^2 = (a/10 - 10 b)^2'] = \
    sp.expand(F(101, 100) * aa_ ** 2 + 101 * bb_ ** 2 - (aa_ + bb_) ** 2 - (aa_ / 10 - 10 * bb_) ** 2) == 0
T20 = F(1, 2 ** 20); T24 = F(1, 2 ** 24)
cP1 = F(101, 100) * F(1, 2 ** 15) * (1 + 7 * T20) ** 2 + 101 * 144 * T20 ** 2
chk['83: (101/100) 2^-15 (1 + 7 tau)^2 + 101 * 144 tau^2 < 2^-14 at tau = 2^-20 (increasing in tau)'] = cP1 < F(1, 2 ** 14)
chk['83: (101/100)(25 + 2^15) < 2^16'] = F(101, 100) * (25 + 2 ** 15) < 2 ** 16
out['83_coef_P1'] = float(cP1)
chk['83 (4): 2^-14 P1^2 + 2^16 L^2 <= 2^-14 (P1^2 + 2^31 L^2) and E1^2 <= 2^-22 M^2 so P0 <= 2^-7 2^-11 M = 2^-18 M'] = \
    F(2 ** 16) <= F(1, 2 ** 14) * 2 ** 31 and F(2 ** 31) * 2 ** 22 == 2 ** 53
inner9 = sp.integrate((r / (2 * t)) * pt * (1 + r) ** 2 * 2 * sp.pi * r, (r, 0, sp.oo))
chk['83 (9): int |Dp_t| (1 + |Z|)^2 = sqrt(pi)/(2 sqrt t) + 4 + 3 sqrt(pi) sqrt t'] = \
    sp.simplify(inner9 - (sp.sqrt(sp.pi) / (2 * sp.sqrt(t)) + 4 + 3 * sp.sqrt(sp.pi) * sp.sqrt(t))) == 0
TT = sp.symbols('T', positive=True)
chk['83 (9): int_0^T of it = sqrt(pi) sqrt T + 4T + 2 sqrt(pi) T^(3/2)'] = \
    sp.simplify(sp.integrate(sp.sqrt(sp.pi) / (2 * sp.sqrt(t)) + 4 + 3 * sp.sqrt(sp.pi) * sp.sqrt(t), (t, 0, TT))
                - (sp.sqrt(sp.pi) * sp.sqrt(TT) + 4 * TT + 2 * sp.sqrt(sp.pi) * TT ** sp.Rational(3, 2))) == 0
ta, b2 = sp.symbols('tau_ b2', positive=True)
bound9 = sp.sqrt(sp.pi) * sp.sqrt(sp.pi) * ta * b2 + 4 * ta * b2 + 2 * sp.sqrt(sp.pi) * sp.sqrt(sp.pi) * (ta ** 2 * b2 * (b2 + 1) + ta * b2 / 2)
chk['83 (9): with E sqrt T <= sqrt(pi) tau beta, E T = tau beta, E T^(3/2) <= sqrt(pi)[tau^2 beta(beta+1) + tau beta/2]: (2 pi + 4) tau beta + 2 pi tau^2 beta(beta+1)'] = \
    sp.expand(bound9 - ((2 * sp.pi + 4) * ta * b2 + 2 * sp.pi * ta ** 2 * b2 * (b2 + 1))) == 0
chk['83 (9): (2 pi + 4) + 4 pi tau <= 6 pi + 4 < 24 (tau <= 1, beta <= 1)'] = 6 * PI_HI + 4 < 24
chk['83 (10): w/omega0 <= R^(6/5) [(1 + r^2)/(1 + r^2/R^2) <= R^2] and (16/5) 24 = 76.8 < 77'] = \
    sp.simplify(Rr ** 2 * (1 + r ** 2 / Rr ** 2) - (1 + r ** 2) - (Rr ** 2 - 1)) == 0 and F(16, 5) * 24 < 77
chk['83 (3): 2^(53/2) * 77 R^(6/5) tau * 2^-18 = 77 * 2^(17/2) R^(6/5) tau'] = F(53, 2) - 18 == F(17, 2)
chk['83 (11): sqrt2 + 1/128 < 3/2 (2 < (3/2 - 1/128)^2)'] = 2 < (F(3, 2) - F(1, 128)) ** 2
chk['83 (13): columns 525, (30464 + 2048 * 432)/2048 < 447, (371371 + 2048 (11606 + 312))/2048 < 12100 < 2^14'] = \
    F(30464 + 2048 * 432, 2048) < 447 and F(371371 + 2048 * (11606 + 312), 2048) < 12100 and 12100 < 2 ** 14 and 525 < 2 ** 14
chk['83 (13): unrounded 524.8 <= 525, 371370 + 2/3 <= 371371, 431.2 <= 432, 11605 + 1/3 <= 11606'] = \
    F(5248, 10) <= 525 and 371370 + F(2, 3) <= 371371 and F(4312, 10) <= 432 and 11605 + F(1, 3) <= 11606
# P0 line
mom1_J2 = sp.integrate(sp.exp(-TT) * sp.sqrt(sp.pi) * sp.sqrt(TT), (TT, 0, sp.oo))
chk['83: J^-2 kernel M1 = E sqrt(pi T) = pi/2, M2 = 4 E T = 4 (T ~ Exp(1)), so omega0 bound 1 + 2 M1 + M2 = 1 + pi + 4 < 9'] = \
    sp.simplify(mom1_J2 - sp.pi / 2) == 0 and 1 + PI_HI + 4 < 9
cK = sp.integrate(sp.exp(-t) / t * (sp.sqrt(sp.pi) * sp.sqrt(t) + 2 * 4 * t + 6 * sp.sqrt(sp.pi) * t ** sp.Rational(3, 2)), (t, 0, sp.oo))
chk['83: [K, m] with (1 + |Z|)^2 moderation: int e^-t/t (E|Z| + 2 E|Z|^2 + E|Z|^3) = pi + 8 + 3 pi < 21'] = \
    sp.simplify(cK - (4 * sp.pi + 8)) == 0 and 4 * PI_HI + 8 < 21
dil = comm_xd(m_sym, 0) + comm_xd(m_sym, 1)
chk['83: [K, X.D] has symbol 2|xi|^2/(1 + |xi|^2) = 2(1 - (1 + |xi|^2)^-1)'] = \
    sp.simplify(dil - 2 * (1 - 1 / (1 + x1 ** 2 + x2 ** 2)) * G) == 0
chk['83: P0 line 37 (14/5) + 21 * 3 * (8/3) + 2 (37/20)(1 + 9) <= 103.6 + 168 + 37 < 312'] = \
    37 * F(14, 5) + 21 * 3 * F(8, 3) + 2 * F(37, 20) * 10 < 312 and 37 * F(14, 5) + 168 + 40 < 312
chk['83 (14): S norm 1 + (2 pi + 4) eta < 1 + 11 eta; 2^14 (1 + 11 tau)^3 < 2^15; 2^15 (3/2) < 2^16'] = \
    2 * PI_HI + 4 < 11 and 2 ** 14 * (1 + 11 * T20) ** 3 < 2 ** 15 and 2 ** 15 * F(3, 2) < 2 ** 16
chk['83 (15): 2^12 (2^-14 P1^2 + 2^16 L^2) = P1^2/4 + 2^28 L^2 and 3/8 - 1/4 = 1/8'] = \
    2 ** 12 * F(1, 2 ** 14) == F(1, 4) and 2 ** 12 * 2 ** 16 == 2 ** 28 and F(3, 8) - F(1, 4) == F(1, 8)
chk['83 (16): 2^31/5 - 2^28 = (3/40) 2^31 and min(1/8, 3/40) >= 1/20'] = \
    F(2 ** 31, 5) - 2 ** 28 == F(3, 40) * 2 ** 31 and min(F(1, 8), F(3, 40)) >= F(1, 20)
chk['83 (17): (512/3)/128 = 4/3, 198 + 4/3 < 200, 200^2 + 352 < 41000 < 2^22 (1/20 - 1/25)'] = \
    F(512, 3) / 128 == F(4, 3) and 198 + F(4, 3) < 200 and 200 ** 2 + 352 < 41000 and 41000 < 2 ** 22 * (F(1, 20) - F(1, 25))
chk['83 (5): 1/25 - 2^16 2^-24 = 231/6400 > 1/28'] = F(1, 25) - 2 ** 16 * T24 == F(231, 6400) and F(231, 6400) > F(1, 28)

# ---------------- topic 84 ----------------
X_ = sp.symbols('X', positive=True)
an = lambda n: (-1) ** (n + 1) * sp.binomial(sp.Rational(1, 2), n)
chk['84: a_n = (-1)^(n+1) binom(1/2, n) > 0 (n <= 60) and sqrt(1 - X) = 1 - sum a_n X^n (series to order 12)'] = \
    all(an(n) > 0 for n in range(1, 61)) and \
    sp.expand(sp.series(sp.sqrt(1 - X_), X_, 0, 12).removeO() - (1 - sum(an(n) * X_ ** n for n in range(1, 12)))) == 0
chk['84: sum n a_n X^n = X d/dX (1 - sqrt(1 - X)) = X/(2 sqrt(1 - X)); at X = 1 - tau: (1 - tau)/(2 sqrt tau)'] = \
    sp.simplify(X_ * sp.diff(1 - sp.sqrt(1 - X_), X_) - X_ / (2 * sp.sqrt(1 - X_))) == 0
chk['84: (1 + z)/(1 + tau z) = tau^-1 (1 - (1 - tau)/(1 + tau z))'] = \
    sp.simplify((1 + z) / (1 + ta * z) - (1 - (1 - ta) / (1 + ta * z)) / ta) == 0
s8 = (1 + (1 - sp.sqrt(ta)) + 2 * sp.pi * ta * (1 - ta) / (2 * sp.sqrt(ta))) / sp.sqrt(ta)
chk['84 (8): tau^(-1/2)[1 + (1 - sqrt tau) + 2 pi tau (1 - tau)/(2 sqrt tau)] = 2 tau^(-1/2) - 1 + pi (1 - tau)'] = \
    sp.simplify(s8 - (2 / sp.sqrt(ta) - 1 + sp.pi * (1 - ta))) == 0
chk['84 (9): (2 * 2^10 + pi)(1 + pi 2^-20) < 3 * 2^10 and 3 tau^(-1/2) + pi (1 + 7 tau) < 4 tau^(-1/2) at tau = 2^-20'] = \
    (2 * 2 ** 10 + PI_HI) * (1 + PI_HI * T20) < 3 * 2 ** 10 and PI_HI * (1 + 7 * T20) < 2 ** 10
chk['84 (2): 1520 = 380 * 4 and 1520^2 * 5 < 2^24'] = 1520 == 380 * 4 and 1520 ** 2 * 5 < 2 ** 24
vr = sp.symbols('vr', positive=True)
integrand_r = r ** 3 / (1 + r ** 2) ** 2 * (1 + sp.log(1 + r ** 2)) ** (-2 * bt)
sub = (integrand_r.subs(r, sp.sqrt(sp.exp(vr) - 1)) * sp.diff(sp.sqrt(sp.exp(vr) - 1), vr))
chk['84: r^3/(1 + r^2)^2 (1 + log(1 + r^2))^(-2 beta) dr = (1/2)(1 - e^-v)(1 + v)^(-2 beta) dv (v = log(1 + r^2))'] = \
    sp.simplify(sub - sp.Rational(1, 2) * (1 - sp.exp(-vr)) * (1 + vr) ** (-2 * bt)) == 0
chk['84: int_0^oo (1 + v)^(-2 beta) dv = 1/(2 beta - 1) (beta = 3/4, 1) and (2 pi)^-2 (2 pi) sqrt(pi/eps) = 1/(2 sqrt(pi eps))'] = \
    sp.integrate((1 + vr) ** sp.Rational(-3, 2), (vr, 0, sp.oo)) == 2 and sp.integrate((1 + vr) ** -2, (vr, 0, sp.oo)) == 1 and \
    sp.simplify((2 * sp.pi) ** -2 * 2 * sp.pi * sp.sqrt(sp.pi / bt) - 1 / (2 * sp.sqrt(sp.pi * bt))) == 0
chk['84 (5): (13/3)(2^12 + 4) < 2^15'] = F(13, 3) * (2 ** 12 + 4) < 2 ** 15

# ---------------- topic 85 ----------------
chk['85 (13): 21 (1 + 2 pi 2^-24)^3 <= 42 and 42 * 4 = 168 (d_W <= 4 mu)'] = 21 * (1 + 2 * PI_HI * T24) ** 3 <= 42 and 42 * 4 == 168
chk['85 (16): r |D log omega2| = (16/5) r^2/(1 + 4r^2) <= 4/5 and r |D log omega1| = (1/5) r^2/(1 + r^2) <= 1/5'] = \
    sp.simplify(r * sp.diff(sp.Rational(2, 5) * sp.log(1 + 4 * r ** 2), r) - sp.Rational(16, 5) * r ** 2 / (1 + 4 * r ** 2)) == 0 and \
    sp.simplify(sp.Rational(4, 5) - sp.Rational(16, 5) * r ** 2 / (1 + 4 * r ** 2) - sp.Rational(4, 5) / (1 + 4 * r ** 2)) == 0 and \
    sp.simplify(r * sp.diff(-sp.Rational(1, 10) * sp.log(1 + r ** 2), r) + sp.Rational(1, 5) * r ** 2 / (1 + r ** 2)) == 0 and \
    sp.simplify(sp.Rational(1, 5) - sp.Rational(1, 5) * r ** 2 / (1 + r ** 2) - sp.Rational(1, 5) / (1 + r ** 2)) == 0
chk['85 (17): 800 (9/5) = 1440'] = 800 * F(9, 5) == 1440
chk['85 (18): 1600 + 168 + 16/5 < 1772, 800 + 168 + 4/5 < 970, 12 * 4 = 48 <= 1772, 1772 + 1440 < 2^12'] = \
    1600 + 168 + F(16, 5) < 1772 and 800 + 168 + F(4, 5) < 970 and 12 * 4 == 48 and 1772 + 1440 < 2 ** 12
chk['85 (23): 1/25 - 2^16 2^-24 - 2^12 2^-20 = 1/25 - 1/128 = 103/3200 > 1/32'] = \
    F(1, 25) - 2 ** 16 * T24 - 2 ** 12 * T20 == F(103, 3200) and F(103, 3200) > F(1, 32)
chk['85 (24): 1/5 - 48 * 2^-20 > 1/6'] = F(1, 5) - 48 * T20 > F(1, 6)
chk['85 (26): 6 * 2^15 * 2^-20 = 3/16; 32 eta = r0; (27) 4 * 2^-20 = 2^-18 < 1 <= a0'] = \
    6 * 2 ** 15 * T20 == F(3, 16) and 4 * T20 == F(1, 2 ** 18)
# first-order identity (25) on polynomial models with the S1 parities
xx, yy = sp.symbols('x y', real=True)
c, a0, b, ch, ck = sp.symbols('c a0 b c_h c_k', real=True)
hc = sp.symbols('h1:6', real=True); pc = sp.symbols('p1:6', real=True); vc = sp.symbols('v1:9', real=True)
hpoly = b * yy + hc[0] * xx ** 2 * yy + hc[1] * yy ** 3                        # even in x, odd in y
rho = a0 * yy + pc[0] * xx ** 2 * yy + pc[1] * yy ** 3
crho = 1 - c                                                                  # c + c[rho] = 1
V = sp.Matrix([(2 * c - 1 - ck) * xx + vc[0] * xx ** 3 + vc[1] * xx * yy ** 2,  # cX + u + U[k], DV(0) = diag(2c-1-c_k, 1+c_k)
               (1 + ck) * yy + vc[2] * xx ** 2 * yy + vc[3] * yy ** 3])
Uh = sp.Matrix([-ch * xx + vc[4] * xx ** 3 + vc[5] * xx * yy ** 2, ch * yy + vc[6] * xx ** 2 * yy + vc[7] * yy ** 3])
grad = lambda f: sp.Matrix([sp.diff(f, xx), sp.diff(f, yy)])
Akh = (V.T * grad(hpoly))[0] - hpoly + (Uh.T * grad(rho))[0]
by0 = sp.diff(Akh, yy).subs({xx: 0, yy: 0})
chk['85 (25): b[A_k h] = c[k] b[h] + a0 c[h] on S1 polynomial models with DV(0) = diag(2c - 1 - c[k], 1 + c[k])'] = \
    sp.expand(by0 - (ck * b + a0 * ch)) == 0
Bkh = Akh - ch * (xx * sp.diff(rho, xx) + yy * sp.diff(rho, yy))
chk['85: b[X.D rho] = a0, so b[B_k h] = c[k] b[h] (B_k removes the a0 c[h] term)'] = \
    sp.expand(sp.diff(Bkh, yy).subs({xx: 0, yy: 0}) - ck * b) == 0
# nonlinear identity: (cX + U[rho + h]).D(rho + h) - (rho + h) with DU[rho](0) = diag(-c[rho], c[rho]), DU[h](0) = diag(-c_h, c_h)
Urh = sp.Matrix([-(crho + ch) * xx + vc[0] * xx ** 3, (crho + ch) * yy + vc[2] * xx ** 2 * yy])
NL = ((c * sp.Matrix([xx, yy]) + Urh).T * grad(rho + hpoly))[0] - (rho + hpoly)
chk['85: b of the nonlinear equation at fixed c is (a0 + b[h]) c[h] (uniqueness in the whole ball)'] = \
    sp.expand(sp.diff(NL, yy).subs({xx: 0, yy: 0}) - (a0 + b) * ch) == 0
Fres = ((c * sp.Matrix([xx, yy]) + sp.Matrix([-crho * xx + vc[0] * xx ** 3, crho * yy + vc[2] * xx ** 2 * yy])).T * grad(rho))[0] - rho
chk['85: b[F] = a0 (c + c[rho] - 1) = 0 for the reference residual'] = sp.expand(sp.diff(Fres, yy).subs({xx: 0, yy: 0})) == 0
chk['85: gamma = 1/c in (20/37, 5/9) exceeds 1/5; 1/5 - 4/9 - gamma < 0 and 2/5 - 1 - gamma < 0'] = \
    F(20, 37) > F(1, 5) and F(1, 5) - F(4, 9) - F(20, 37) < 0 and F(2, 5) - 1 - F(20, 37) < 0
# threshold arithmetic
be_star = sp.Rational(1, 2) + 1 / (48 * sp.log(2))
eta_fun = lambda be: 2 ** -25 * mpmath.mpf(2) ** (-24 * be) * mpmath.sqrt(2 * be - 1)
etamax = eta_fun(mpmath.mpf(sp.N(be_star, 30)))
grid_max = max(eta_fun(mpmath.mpf(0.5) + mpmath.mpf(i) / 20000) for i in range(1, 10001))
chk['85: eta = 2^-25 tau^beta sqrt(2 beta - 1) <= 2^-25 tau^(1/2) = 2^-37 for every 1/2 < beta <= 1 (tau = 2^-24)'] = \
    sp.Rational(1, 2 ** 25) * sp.Rational(1, 2 ** 12) == sp.Rational(1, 2 ** 37) and etamax < mpmath.mpf(2) ** -37 and grid_max <= etamax * (1 + 1e-12)
out['85_eta'] = {'beta_star': float(sp.N(be_star)), 'eta_max': float(etamax), 'log2_eta_max': float(mpmath.log(etamax, 2))}
chk['85: certified low bounds M(F) >= 2^(53/2) L(F): 3.535e25 > 2^84 and 1.935e9 > 2^30, so gaps > 2^121 and > 2^67'] = \
    F(3535, 100) * 10 ** 24 > 2 ** 84 and F(1935, 1000) * 10 ** 9 > 2 ** 30

# ---------------- FLOAT ----------------
# (i) torus test of ||[K, W.grad] f|| <= 2 ||DW||_op ||f||
N = 256
k1 = np.fft.fftfreq(N, d=1.0 / N)
KX, KY = np.meshgrid(k1, k1, indexing='ij'); K2 = KX ** 2 + KY ** 2
gx = np.arange(N) * 2 * np.pi / N
X, Y = np.meshgrid(gx, gx, indexing='ij')
fh = np.fft.fft2; ifh = lambda f: np.fft.ifft2(f)
psi = lambda X, Y: np.sin(X) * np.sin(2 * Y) + 0.4 * np.cos(2 * X + Y) + 0.25 * np.sin(3 * Y - X)
# W = (-psi_y, psi_x); entries of DW computed analytically on a fine grid for d
def DW(X, Y):
    pxx = -np.sin(X) * np.sin(2 * Y) - 1.6 * np.cos(2 * X + Y) - 0.25 * np.sin(3 * Y - X)
    pyy = -4 * np.sin(X) * np.sin(2 * Y) - 0.4 * np.cos(2 * X + Y) - 2.25 * np.sin(3 * Y - X)
    pxy = 2 * np.cos(X) * np.cos(2 * Y) - 0.8 * np.cos(2 * X + Y) + 0.75 * np.sin(3 * Y - X)
    return -pxy, -pyy, pxx, pxy   # dW1/dx, dW1/dy, dW2/dx, dW2/dy
Nf = 2048
gf = np.arange(Nf) * 2 * np.pi / Nf
Xf, Yf = np.meshgrid(gf, gf, indexing='ij')
a11, a12, a21, a22 = DW(Xf, Yf)
# operator norm of a 2x2 matrix
s1 = a11 ** 2 + a12 ** 2 + a21 ** 2 + a22 ** 2
det = a11 * a22 - a12 * a21
opn = np.sqrt((s1 + np.sqrt(np.maximum(s1 ** 2 - 4 * det ** 2, 0))) / 2)
dgrid = float(opn.max())
d_safe = dgrid * 1.01   # the fine-grid maximum of a trigonometric polynomial of degree 3 is within 1 percent here (FLOAT)
psih = fh(psi(X, Y))
W1 = np.real(ifh(-1j * KY * psih)); W2 = np.real(ifh(1j * KX * psih))
Ksym = np.log1p(K2)
band = (np.abs(KX) <= N // 2 - 8) & (np.abs(KY) <= N // 2 - 8)
rng = np.random.default_rng(81)
ratios = []
for trial in range(10):
    if trial < 4:
        F_ = (rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))) * np.exp(-K2 / (2 * (8.0 * (trial + 1)) ** 2))
    else:
        th = rng.uniform(0, np.pi); kk = 20 + 15 * trial
        c0 = (kk * np.cos(th), kk * np.sin(th))
        F_ = np.exp(-((KX - c0[0]) ** 2 + (KY - c0[1]) ** 2) / (2 * 4.0 ** 2)) * np.exp(1j * rng.uniform(0, 2 * np.pi, size=(N, N)) * 0)
        F_ = F_ * np.exp(-1j * (KX * rng.uniform(0, 6) + KY * rng.uniform(0, 6)))
    F_ = F_ * band
    f = np.real(ifh(F_)); Fh = fh(f) * band; f = np.real(ifh(Fh))
    def DWf(g):
        G_ = fh(g)
        return W1 * np.real(ifh(1j * KX * G_)) + W2 * np.real(ifh(1j * KY * G_))
    Kf = np.real(ifh(Ksym * fh(f)))
    com = np.real(ifh(Ksym * fh(DWf(f)))) - DWf(Kf)
    ratios.append(float(np.linalg.norm(com) / (dgrid * np.linalg.norm(f))))
chk['81 FLOAT: torus ||[K, W.grad] f|| / (||DW||_op ||f||) < 2 for 10 band-limited inputs (random and wave packets)'] = max(ratios) < 2
out['81_FLOAT'] = {'d_grid': dgrid, 'ratios': ratios}
# (ii) frequency-difference bound (5) of topic 82
okq = True; worst = 0.0
for tau_ in (2.0 ** -20, 0.3, 1.0):
    for be in (0.5, 0.75, 1.0):
        xi = rng.normal(size=(200000, 2)) * rng.choice([1e-3, 1e-1, 1, 30, 1e4], size=(200000, 1))
        eta_ = rng.normal(size=(200000, 2)) * rng.choice([1e-3, 1, 1e3, 1e8], size=(200000, 1))
        qf = lambda Z: (1 + tau_ * np.log1p((Z ** 2).sum(1))) ** be
        lhs = np.abs(qf(xi + eta_) - qf(eta_))
        rhs = np.minimum(1, np.sqrt((xi ** 2).sum(1))) * qf(xi)
        okq = okq and bool(np.all(lhs <= rhs * (1 + 1e-12) + 1e-14))
        worst = max(worst, float(np.max(lhs / rhs)))
chk['82 FLOAT: |q(xi + eta) - q(eta)| <= min(1, |xi|) q(xi) on 1.8e6 random pairs'] = okq
out['82_FLOAT_worst_ratio'] = worst
# (iii) weight facts of topic 83 (7)
rr = np.concatenate([np.linspace(0, 10, 20001), np.geomspace(10, 1e14, 20001)])
okw = True; wmax = 0.0
for R_ in (1.0, 2.0 ** 10, 2.0 ** 31):
    om0 = (1 + rr ** 2) ** -0.6; om1 = (1 + rr ** 2) ** -0.1; w = (1 + rr ** 2 / R_ ** 2) ** -1.1
    qv = om0 ** 2 / w
    dq = np.abs(-2.4 * rr * (1 + rr ** 2) ** -2.2 / w + (1 + rr ** 2) ** -1.2 * 2.2 * (rr / R_ ** 2) * (1 + rr ** 2 / R_ ** 2) ** 0.1)
    okw = okw and bool(np.all(qv <= om1 * (1 + 1e-12))) and bool(np.all(dq <= 5 * om0))
    wmax = max(wmax, float(np.max(dq / om0)))
chk['83 FLOAT: omega0^2/w <= omega1 and |D(omega0^2/w)| <= 5 omega0 on a radial grid to 1e14 (R = 1, 2^10, 2^31)'] = okw
out['83_FLOAT_max_Dratio'] = wmax

out['checks'] = {k_: bool(v_) for k_, v_ in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v_ in chk.items() if not v_]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
