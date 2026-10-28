"""Third computation for verification topics 78 (sharp half-logarithmic multiplication H_(1/2) x H^1 -> L2 in two
dimensions, constant 5) and 79 (commutators of Q_beta with moderate weights; the weighted product estimate).

Written from the statements of topics 78 and 79 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): the disk bound constant (2 pi)^-2 sqrt(pi 4^j) (2 pi) = 2^j/(2 sqrt(pi)); the annular
   support [3, 9] 2^(j-3) and disjointness of annuli two indices apart; 1 + log(1 + 4^(j-1)) >= (j + 1)/2 (log 2 > 1/2);
   sum_(m >= 3) 4^-m = 1/48; the three constants and (7 + 1/sqrt 24)/sqrt(pi) <= 8/sqrt(pi) < 5; the polar integrals of
   the Moser function (||D phi_L||^2 = 2 pi, ||phi_L||^2 formula, H^1 norm squared < 3 pi for L >= 1); the scaling
   inequality 1 + log(1 + z/eps^2) <= (1 + 2L)(1 + log(1 + z)) and (1 + 2L)/L <= 3; the product norm L^(1/2 - beta);
   topic 79: the derivative of (6), the beta = 1 Frullani form, the beta integral bound Gamma(t + 1/2)/Gamma(t + 1) <=
   sqrt(pi), the commutator constant a pi beta and a pi, E sqrt(Exp(1)) = sqrt(pi)/2, (1 + a pi/2)^2 composition, the
   weight-ratio inequality for omega1, omega2 with a = 2, and the Hardy step ||psi||_(H1)^2 <= 5 ||D phi||^2.
2. FLOAT: (6) by quadrature; (1) on an FFT grid for random band-limited and concentrated pairs (ratio below
   8/sqrt(pi)); the commutator bound (2) with omega2 on an FFT grid; random sampling of the weight-ratio inequality.

Usage: python3 check_p78_p79.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
chk, out = {}, {}
j, L, r, t, k, u, bt, a = sp.symbols('j L r t k u beta a', positive=True)

# 1. topic 78 exact
chk['(2): (2 pi)^-2 sqrt(pi 4^j) (2 pi) = 2^j/(2 sqrt(pi))'] = \
    sp.simplify((2 * sp.pi) ** -2 * sp.sqrt(sp.pi * 4 ** j) * 2 * sp.pi - 2 ** j / (2 * sp.sqrt(sp.pi))) == 0
chk['annulus of T_j: 2^(j-1) - 2^(j-3) = 3 2^(j-3), 2^j + 2^(j-3) = 9 2^(j-3); 9 2^(j-3) < 3 2^(j-1) (overlap 2)'] = \
    sp.simplify(2 ** (j - 1) - 2 ** (j - 3) - 3 * 2 ** (j - 3)) == 0 and sp.simplify(2 ** j + 2 ** (j - 3) - 9 * 2 ** (j - 3)) == 0 and 9 < 12
chk['log 2 > 1/2 and 1 + log(1 + 4^(j-1)) >= 1 + 2 (j - 1) log 2 >= (j + 1)/2 for j >= 1'] = \
    sp.log(2) > sp.Rational(1, 2) and all(1 + sp.log(1 + 4 ** (jj - 1)) >= sp.Rational(jj + 1, 2) for jj in range(1, 60))
chk['sum_(m >= 3) 4^-m = 1/48'] = sp.summation(sp.Integer(4) ** -sp.Symbol('m', integer=True), (sp.Symbol('m', integer=True), 3, sp.oo)) == sp.Rational(1, 48)
c_hi = 2 / sp.sqrt(sp.pi); c_lo = 1 / sp.sqrt(24 * sp.pi); c_nb = 5 / sp.sqrt(sp.pi)
chk['constants: high-low 2/sqrt(pi) [from sqrt(2 * 2/pi)], low-high 1/sqrt(24 pi) [from sqrt(2 * 4/(4 * 48 pi))], neighbors 5/sqrt(pi)'] = \
    sp.simplify(sp.sqrt(2 * 2 / sp.pi) - c_hi) == 0 and sp.simplify(sp.sqrt(2 * 4 / (4 * 48 * sp.pi)) - c_lo) == 0 and \
    sp.simplify(5 * 2 / (2 * sp.sqrt(sp.pi)) - c_nb) == 0
chk['(7 + 1/sqrt 24)/sqrt(pi) <= 8/sqrt(pi) < 5 (64 < 25 pi since pi > 3)'] = \
    sp.simplify(c_hi + c_lo + c_nb - (7 + 1 / sp.sqrt(24)) / sp.sqrt(sp.pi)) == 0 and 1 / sp.sqrt(24) < 1 and 64 < 25 * 3
eps = sp.exp(-L)
Dn = sp.integrate((1 / (r * sp.sqrt(L))) ** 2 * 2 * sp.pi * r, (r, eps, 1))
chk['Moser: ||D phi_L||^2 = 2 pi'] = sp.simplify(Dn - 2 * sp.pi) == 0
tt = sp.symbols('tt', positive=True)
L2a = sp.pi * eps ** 2 * L + sp.integrate(sp.log(1 / r) ** 2 / L * 2 * sp.pi * r, (r, eps, 1))
L2b = sp.pi * L * sp.exp(-2 * L) + 2 * sp.pi / L * sp.integrate(tt ** 2 * sp.exp(-2 * tt), (tt, 0, L))
chk['Moser: ||phi_L||^2 = pi L e^-2L + (2 pi/L) int_0^L t^2 e^-2t dt'] = sp.simplify(L2a - L2b) == 0
chk['int_0^oo t^2 e^-2t = 1/4; L e^-2L <= e^-2 < 1/4 for L >= 1; so H1 norm^2 < 2 pi + pi/4 + pi/2 < 3 pi'] = \
    sp.integrate(tt ** 2 * sp.exp(-2 * tt), (tt, 0, sp.oo)) == sp.Rational(1, 4) and sp.exp(-2) < sp.Rational(1, 4) and \
    sp.diff(L * sp.exp(-2 * L), L).subs(L, 1) < 0 and 2 + sp.Rational(1, 4) + sp.Rational(1, 2) < 3
zz = sp.symbols('z', positive=True)
chk['1 + z/eps^2 <= (1 + z)/eps^2 so 1 + log(1 + z/eps^2) <= 1 + 2L + log(1 + z) <= (1 + 2L)(1 + log(1 + z))'] = \
    sp.simplify((1 + zz) * sp.exp(2 * L) - (1 + zz * sp.exp(2 * L)) - (sp.exp(2 * L) - 1)) == 0 and \
    sp.expand((1 + 2 * L) * (1 + sp.log(1 + zz)) - (1 + 2 * L + sp.log(1 + zz)) - 2 * L * sp.log(1 + zz)) == 0
chk['(1 + 2L)/L <= 3 for L >= 1; ||g_L||_2 = L^-beta ||chi||; product L^(1/2 - beta)'] = \
    sp.simplify((3 * L - (1 + 2 * L)) - (L - 1)) == 0 and sp.simplify(sp.sqrt(L) * L ** -bt - L ** (sp.Rational(1, 2) - bt)) == 0
# 1. topic 79 exact
chk['(6): d/dk of the right side = beta (1 + k)^(beta - 1) (Gamma integral)'] = \
    sp.simplify(sp.integrate(sp.exp(-t) * t * sp.exp(-t * k) * t ** (-1 - sp.Rational(1, 3)), (t, 0, sp.oo)) * sp.Rational(1, 3) / sp.gamma(1 - sp.Rational(1, 3))
                - sp.Rational(1, 3) * (1 + k) ** (sp.Rational(1, 3) - 1)) == 0
chk['beta = 1: log(1 + lam) = int e^-v (1 - e^(-v lam)) dv/v (derivative)'] = \
    sp.simplify(sp.integrate(sp.exp(-t) * sp.exp(-t * k), (t, 0, sp.oo)) - 1 / (1 + k)) == 0
chk['(8): Gamma(t + 1/2)/Gamma(t + 1) = B(t + 1/2, 1/2)/sqrt(pi) <= B(1/2, 1/2)/sqrt(pi) = sqrt(pi)'] = \
    sp.simplify(sp.gamma(sp.Rational(1, 2)) ** 2 / sp.gamma(1) / sp.sqrt(sp.pi) - sp.sqrt(sp.pi)) == 0
chk['commutator constant: [beta/Gamma(1 - beta)] int e^-t pi t t^(-1 - beta) dt = pi beta (beta = 1/3, 2/3)'] = \
    all(sp.simplify(be / sp.gamma(1 - be) * sp.integrate(sp.exp(-t) * sp.pi * t * t ** (-1 - be), (t, 0, sp.oo)) - sp.pi * be) == 0
        for be in (sp.Rational(1, 3), sp.Rational(2, 3)))
chk['beta = 1: int e^-v sqrt(pi v)/v dv = pi'] = sp.simplify(sp.integrate(sp.exp(-t) * sp.sqrt(sp.pi * t) / t, (t, 0, sp.oo)) - sp.pi) == 0
chk['(10): E sqrt(U) for U ~ Exp(1) is sqrt(pi)/2, so M1 <= pi/2'] = sp.simplify(sp.integrate(sp.sqrt(u) * sp.exp(-u), (u, 0, sp.oo)) - sp.sqrt(sp.pi) / 2) == 0
c1 = 1 + a * sp.pi / 2
chk['(3): (1 + a pi/2) + (a pi/2)(1 + a pi/2) = (1 + a pi/2)^2'] = sp.expand(c1 + a * sp.pi / 2 * c1 - c1 ** 2) == 0
X1, X2, Y1, Y2, b = sp.symbols('X1 X2 Y1 Y2 b', real=True)
chk['|(1, bX)| <= |(1, bY)| + b|X - Y| (triangle inequality in the augmented vector)'] = True
chk['|z - 1| <= 2d if z, 1/z <= 1 + 2d: 1 - 1/(1 + 2d) = 2d/(1 + 2d)'] = sp.simplify(1 - 1 / (1 + 2 * t) - 2 * t / (1 + 2 * t)) == 0
chk['Hardy step: r/<r>^3 <= 1/r since <r>^6 - r^4 = 1 + 3r^2 + 2r^4 + r^6 > 0; H1 norm^2 <= 1 + 2^2 = 5'] = \
    sp.expand((1 + r ** 2) ** 3 - r ** 4 - (1 + 3 * r ** 2 + 2 * r ** 4 + r ** 6)) == 0 and 1 + 2 ** 2 == 5
del chk['|(1, bX)| <= |(1, bY)| + b|X - Y| (triangle inequality in the augmented vector)']
out['constants'] = {'(7 + 1/sqrt24)/sqrt(pi)': float((7 + 1 / np.sqrt(24)) / np.sqrt(np.pi)), '8/sqrt(pi)': float(8 / np.sqrt(np.pi)),
                    '5(1+pi)^2': float(5 * (1 + np.pi) ** 2), '5 sqrt5 (1+pi)^2': float(5 * np.sqrt(5) * (1 + np.pi) ** 2)}

# 2. FLOAT
mpmath.mp.dps = 25
ok6 = True
for be in (mpmath.mpf('0.25'), mpmath.mpf('0.6')):
    for kk in (mpmath.mpf('0.3'), mpmath.mpf(50)):
        # s = exp(w): the integrand is O(exp((1 - beta) w)) at w -> -oo and doubly exponentially small for w > 6
        rhs = be / mpmath.gamma(1 - be) * mpmath.quad(lambda w: mpmath.exp(-mpmath.exp(w)) * (-mpmath.expm1(-mpmath.exp(w) * kk))
                                                      * mpmath.exp(-be * w), [-300, -40, -10, -3, 0, 3, 7])
        ok6 = ok6 and abs(rhs - ((1 + kk) ** be - 1)) < 1e-15
chk['(6) by quadrature (FLOAT)'] = ok6
okg = all(mpmath.gamma(tv + 0.5) / mpmath.gamma(tv + 1) <= mpmath.sqrt(mpmath.pi) for tv in np.linspace(1e-6, 30, 300))
chk['(8) Gamma(t + 1/2)/Gamma(t + 1) <= sqrt(pi) on a grid (FLOAT)'] = okg
rng = np.random.default_rng(78)
P1 = rng.normal(size=(200000, 2)) * rng.exponential(3, size=(200000, 1)); P2 = P1 + rng.normal(size=(200000, 2)) * rng.exponential(2, size=(200000, 1))
d = np.linalg.norm(P1 - P2, axis=1)
w1 = lambda P: (1 + (P ** 2).sum(1)) ** -0.1
w2 = lambda P: (1 + 4 * (P ** 2).sum(1)) ** 0.4
okw = all(np.all(np.abs(w(P1) / w(P2) - 1) <= 2 * d * (1 + 1e-12)) for w in (w1, w2))
chk['(1) with a = 2 for omega1 and omega2 on 2e5 random pairs (FLOAT)'] = okw
Nn, Lb = 512, 16.0
g1 = (np.arange(Nn) - Nn // 2) * (2 * Lb / Nn)
X, Y = np.meshgrid(g1, g1, indexing='ij'); dA = (2 * Lb / Nn) ** 2
k1 = 2 * np.pi * np.fft.fftfreq(Nn, d=2 * Lb / Nn)
KX, KY = np.meshgrid(k1, k1, indexing='ij'); K2 = KX ** 2 + KY ** 2
fh = np.fft.fft2; ifh = lambda f: np.real(np.fft.ifft2(f))
nrm = lambda f: np.sqrt(np.sum(np.abs(f) ** 2) * dA)
Qh = lambda f, be: ifh((1 + np.log1p(K2)) ** be * fh(f))
H1 = lambda f: np.sqrt(np.sum((1 + K2) * np.abs(fh(f)) ** 2) * dA / Nn ** 2)
ratios = []
for trial in range(12):
    if trial < 6:
        # random smooth fields concentrated in |X| < 6
        env = np.exp(-(X ** 2 + Y ** 2) / 8)
        g = ifh(fh(rng.normal(size=X.shape)) * np.exp(-K2 / (2 * (0.5 + trial) ** 2))) * env
        ph = ifh(fh(rng.normal(size=X.shape)) * np.exp(-K2 / 2)) * env
    else:
        sc = 2.0 ** -(trial - 5)
        g = np.exp(-(X ** 2 + Y ** 2) / (2 * sc ** 2)) / sc
        ph = np.log1p(1 / np.sqrt(X ** 2 + Y ** 2 + sc ** 2)) * np.exp(-(X ** 2 + Y ** 2) / 4)
    ratios.append(nrm(g * ph) / (nrm(Qh(g, 0.5)) * H1(ph)))
chk['(1) FLOAT: ||g phi|| / (||Q_(1/2) g|| ||phi||_H1) < 8/sqrt(pi) for 12 random and concentrated pairs'] = max(ratios) < 8 / np.sqrt(np.pi)
cr = []
for be in (0.5, 1.0):
    for trial in range(4):
        c0 = rng.uniform(-4, 4, size=2)
        f = np.exp(-((X - c0[0]) ** 2 + (Y - c0[1]) ** 2) / (0.5 + trial)) * np.cos(3 * trial * X)
        om = (1 + 4 * (X ** 2 + Y ** 2)) ** 0.4
        com = Qh(om * f, be) - om * Qh(f, be)
        m = (np.abs(X) < 10) & (np.abs(Y) < 10)
        cr.append(float(np.sqrt(np.sum(com[m] ** 2) * dA) / (2 * np.pi * be * nrm(om * f))))
chk['(2) FLOAT: ||[Q_beta, omega2] f|| (on |X|, |Y| < 10) below 2 pi beta ||omega2 f|| (beta = 1/2, 1; 8 inputs)'] = max(cr) < 1
out['FLOAT'] = {'product_ratios': [float(v) for v in ratios], 'bound_8_over_sqrt_pi': float(8 / np.sqrt(np.pi)),
                'commutator_ratios_to_bound': cr}
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
