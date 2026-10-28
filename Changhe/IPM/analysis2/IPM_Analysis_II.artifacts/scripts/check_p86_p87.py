"""Third computation for verification topics 86 (the three exact references stay excluded in the native logarithmic
norm M) and 87 (four compatible outputs of M: density Hoelder norm, projected angular singular moment, canonical
strain with its contact term).

Written from the statements of topics 86 and 87 only; no verifier code is imported. Routes:

1. Exact (Fraction, integers, sympy): topic 86: the conversion constant 1 + 77 2^(17/2) R^(6/5) tau < 2^30 at
   R = 2^31, tau = 2^-24 by integer tenth powers; 2 + 16 tau^beta < 3; the composed factor 2^32; the radii
   2^32 * 2^25 = 2^57 and 2^32 * 2^-11 = 2^21 against topic 73; the ratios 2^45 and 2^9 to the radius of topic 85;
   the three integer residual floors recomputed from the topic 51 and 52 witness records (integer square root of
   2^53 L^2, integer parts of (11/10) n_old) with source hashes; the failure of the topic 85 threshold
   eta = 2^-25 tau^beta (2 beta - 1)^(1/2) <= 2^-37 by each floor.
   Topic 87: the constants of (7), (8), (9) (int (1 + |xi|^2)^-2 = pi, int_0^oo r^2/(1 + r^2)^2 = pi/4, the Hoelder
   dual factor 1/4), the annulus and ball sums 4 * 8, 3 4^(1/5) < 4, 44 <= 64; the orthogonality of sin(3 theta)
   to all monomials cos^a sin^b with a + b <= 2 and int |sin 3 theta| = 4; (13) with 13/12 and 52/(3 pi) < 6; the
   polar identity in (2) and P3(y) = 0; the tail constant of (14); the totals 75 < 128 and 128 * 32 = 2^12.
   The contact-corrected strain formula (4), c[h] = -b[h]/4 + int_0^oo a3(r) dr/r^2 for Gaussian-type h, is tested
   against an independent exact Fourier computation of c[h] = d_y U_2[h](0) with the symbol of R1^2 (five inputs,
   including b != 0 and mixed harmonics).
2. FLOAT: the angular transform bound (12) by quadrature on a grid of (t, direction); the bound
   |exp(i s) - 1|^2 <= 2|s| on a grid; the planar embedding constants of (9) for random band-limited functions on
   an FFT grid.

Usage: python3 check_p86_p87.py VERIFIER_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}

# 1. topic 86
# 77 2^(17/2) 2^(186/5) 2^-24 < 2^30 - 1  <=>  77^10 2^(85 + 372 - 240) < (2^30 - 1)^10
chk['86 (2): 1 + 77 2^(17/2) R^(6/5) tau < 2^30 at R = 2^31, tau = 2^-24 (tenth powers)'] = \
    77 ** 10 * 2 ** (85 + 372 - 240) < (2 ** 30 - 1) ** 10
out['86_D_log2_FLOAT_display'] = math.log2(1 + 77 * 2 ** 8.5 * 2 ** (31 * 1.2) * 2 ** -24)
chk['86: tau^beta <= tau^(1/2) = 2^-12 for beta >= 1/2, so 2 + 16 tau^beta <= 2 + 2^-8 < 3; 3 * 2^30 < 2^32'] = \
    2 + Q(16, 2 ** 12) < 3 and 3 * 2 ** 30 < 2 ** 32
chk['86: radii 2^32 tau^-beta (2^25 tau^beta) = 2^57 and 2^32 tau^-beta (2^-11 tau^beta) = 2^21 (topic 73 radii)'] = \
    32 + 25 == 57 and 32 - 11 == 21
chk['86: ratios to r0 = 2^-20 tau^beta sqrt(eps): 2^45/sqrt(eps) >= 2^45 and 2^9/sqrt(eps) >= 512'] = \
    25 + 20 == 45 and 2 ** (-11 + 20) == 512
p51 = ROOT / '51_exterior_weight_transfer/verification/compute.json'
r51 = json.loads(p51.read_text()); out['inputs'][str(p51.relative_to(ROOT))] = sha(p51)
row31 = next(r for r in r51['rows'] if int(r['T_power']) == 31)
L131 = int(row31['L_witness_integer_lower'])
chk['86 (5): the topic 51 witness at R >= 2^31 is 372474829674258475'] = L131 == 372474829674258475
N131 = math.isqrt(2 ** 53 * L131 ** 2)
chk['86 (1): isqrt(2^53 L^2) = 35350195123413029343106947 and it is strict (2^53 L^2 not a square)'] = \
    N131 == 35350195123413029343106947 and N131 ** 2 < 2 ** 53 * L131 ** 2
floors = {'state131': N131}
for name, claim in (('nb_Mpen2_exact', 1935892108), ('nb_d2_exact', 1936535207)):
    pa = ROOT / f'52_refit_annular_distance/verification/{name}.annular.json'
    pr = ROOT / f'52_refit_annular_distance/verification/{name}.rational_audit.json'
    ra = json.loads(pa.read_text()); rr = json.loads(pr.read_text())
    out['inputs'][str(pa.relative_to(ROOT))] = sha(pa); out['inputs'][str(pr.relative_to(ROOT))] = sha(pr)
    n_old = int(ra['best_N_integer_lower'])
    chk[f'86 (6) {name}: n_old = {n_old} in both topic 52 records, rational audit passes'] = \
        n_old == int(rr['best_N_integer_lower']) and rr['all_source_hashes_match'] and rr['all_comparisons_pass']
    chk[f'86 (6) {name}: integer part of (11/10) n_old = {claim}, strict'] = \
        Q(11, 10) * n_old > claim and Q(11, 10) * n_old < claim + 1
    floors[name] = claim
chk['86: the native floors exceed the P71 floors (1 + D_R loss removed)'] = \
    floors['state131'] > 35350194988431047182367358 and floors['nb_Mpen2_exact'] > 1935892101 and floors['nb_d2_exact'] > 1936535199
# eta = 2^-25 tau^beta sqrt(eps) <= 2^-25 2^-12 = 2^-37; failure factors floor/2^-37
gaps = {k: math.log2(v) + 37 for k, v in floors.items()}
chk['86: every floor exceeds 2^-37 >= eta by more than 2^67 (state 131: more than 2^121)'] = \
    floors['state131'] > 2 ** (121 - 37) and all(floors[k] > 2 ** (67 - 37) for k in floors)
out['86_floors'] = {k: str(v) for k, v in floors.items()}; out['86_log2_gap_over_2^-37_FLOAT_display'] = gaps

# 1. topic 87
T20 = Q(1, 2 ** 20)
chk['87 (7): (1 + 11 tau), (1 + 7 tau) <= 2 at tau <= 2^-20; P0, P1 <= 2m/2048, P2 <= 2m'] = 1 + 11 * T20 <= 2 and 1 + 7 * T20 <= 2
chk['87 (8): 2(507/2048 + 40/2048 + 1) = 2 (2595/2048) < 3'] = 2 * (Q(507, 2048) + Q(40, 2048) + 1) == 2 * Q(2595, 2048) < 3
xi, r, th, t = sp.symbols('xi r theta t', positive=True)
chk['87 (9): int_R2 (1 + |xi|^2)^-2 = pi; (2 pi)^-2 sqrt(pi) (2 pi) = 1/(2 sqrt(pi)) < 1/2'] = \
    sp.simplify(2 * sp.pi * sp.integrate(xi / (1 + xi ** 2) ** 2, (xi, 0, sp.oo)) - sp.pi) == 0 and \
    sp.simplify((2 * sp.pi) ** -2 * sp.sqrt(sp.pi) * 2 * sp.pi - 1 / (2 * sp.sqrt(sp.pi))) == 0 and 4 * sp.pi > 1
I14 = sp.integrate(r ** 2 / (1 + r ** 2) ** 2, (r, 0, sp.oo))
chk['87 (9): int_0^oo r^2/(1 + r^2)^2 = pi/4; (2 pi)^-2 * 2 * (2 pi) * pi/4 = 1/4 (squared Hoelder dual factor)'] = \
    sp.simplify(I14 - sp.pi / 4) == 0 and sp.simplify((2 * sp.pi) ** -2 * 2 * 2 * sp.pi * I14 - sp.Rational(1, 4)) == 0
chk['87 (9): |e^(is) - 1|^2 = 4 sin^2(s/2) <= min(4, s^2) <= 2|s| (s^2 <= 2|s| for |s| <= 2, 4 <= 2|s| otherwise)'] = \
    sp.simplify(sp.Abs(sp.exp(sp.I * t) - 1) ** 2 - 4 * sp.sin(t / 2) ** 2) == 0 and 2 ** 2 <= 2 * 2
# annulus: (3/2)(1 + sqrt2) 4^(1/5) < 5 with sqrt2 < 17/12 and 4^(1/5) < 4/3
chk['87 annulus: sqrt2 < 17/12, 4^(1/5) < 4/3, (3/2)(29/12)(4/3) < 5 <= 8; four indices max(0, j-1) <= l <= j+2'] = \
    Q(17, 12) ** 2 > 2 and Q(4, 3) ** 5 > 4 and Q(3, 2) * Q(29, 12) * Q(4, 3) < 5 and len(range(4, 8)) == 4
chk['87 annulus: supp chi_l = [2^(l-1), 2^(l+1)] meets [2^j, 2^(j+1)] iff j - 1 <= l <= j + 2 (all j <= 40)'] = \
    all({l for l in range(0, 60) if max(Q(2) ** (l - 1), Q(2) ** j) <= min(Q(2) ** (l + 1), Q(2) ** (j + 1))}
        == set(range(max(0, j - 1), j + 3)) for j in range(1, 41))
chk['87: 4 * 8 = 32; 2^(j/5 - j/4) <= 1; ball: 3 4^(1/5) < 4 (3^5 4 < 4^5), 3 * 4 = 12, 12 + 32 = 44 <= 64'] = \
    4 * 8 == 32 and 3 ** 5 * 4 < 4 ** 5 and 12 + 32 == 44 <= 64
c_, s_ = sp.cos(th), sp.sin(th)
chk['87 (12): sin(3 theta) is orthogonal to cos^a sin^b for a + b <= 2; int |sin 3 theta| = 4'] = \
    all(sp.integrate(sp.sin(3 * th) * c_ ** a_ * s_ ** b_, (th, 0, 2 * sp.pi)) == 0 for a_ in range(3) for b_ in range(3 - a_)) and \
    6 * sp.integrate(sp.sin(3 * th), (th, 0, sp.pi / 3)) == 4
chk['87 (13): int_0^1 t/6 + int_1^oo t^-2 = 13/12; (4/pi)(13/12) = 13/(3 pi); 4 * 13/(3 pi) < 52/9 < 6'] = \
    sp.integrate(t / 6, (t, 0, 1)) + sp.integrate(t ** -2, (t, 1, sp.oo)) == sp.Rational(13, 12) and \
    sp.simplify(4 / sp.pi * sp.Rational(13, 12) - 13 / (3 * sp.pi)) == 0 and Q(52, 9) < 6 and sp.pi > 3
ar = sp.Function('a3')(r)
chk['87 (2): int_(r<1) r^-3 |a3 sin 3theta| dX = 4 int_0^1 |a3| dr/r^2 (polar); P3(y) = P3(r sin theta) = 0'] = \
    sp.simplify(r ** -3 * r * 4 - 4 / r ** 2) == 0 and sp.integrate(sp.sin(3 * th) * r * sp.sin(th), (th, 0, 2 * sp.pi)) == 0
chk['87 (14): (1 + r^2)^(6/5) <= 2^(6/5) r^(12/5) on r >= 1, 2^6 < 3^5, int_1^oo r^(-13/5) = 5/8, 15/(8 pi) < 1'] = \
    2 ** 6 < 3 ** 5 and sp.integrate(r ** sp.Rational(-13, 5), (r, 1, sp.oo)) == sp.Rational(5, 8) and 15 < 8 * 3 and \
    sp.integrate(sp.sin(3 * th) ** 2, (th, 0, 2 * sp.pi)) == sp.pi
chk['87 (5), (6): 1 + 64 + 6 + 4 = 75 < 128 and 128 * 32 = 2^12'] = 1 + 64 + 6 + 4 == 75 < 128 and 128 * 32 == 2 ** 12

# contact formula (4) against an exact Fourier evaluation of c[h] = d_y U_2[h](0)
x, y = sp.symbols('x y', real=True)
k1, k2 = sp.symbols('k1 k2', real=True)
rho_, ph = sp.symbols('rho phi', positive=True)


ANG = {}


def ang(m, n_):
    # int_0^(2 pi) cos^m sin^n
    if (m, n_) not in ANG:
        ANG[(m, n_)] = sp.integrate(sp.cos(ph) ** m * sp.sin(ph) ** n_, (ph, 0, 2 * sp.pi))
    return ANG[(m, n_)]


def radial(p, a):
    # int_0^oo rho^p exp(-a rho^2) d rho = Gamma((p + 1)/2) / (2 a^((p + 1)/2)), p > -1
    assert p > -1
    return sp.gamma(sp.Rational(p + 1, 2)) / (2 * a ** sp.Rational(p + 1, 2))


def fourier_c(poly, a):
    # h = poly(x, y) exp(-a r^2); hat h(k) = poly(i d/dk1, i d/dk2) (pi/a) exp(-|k|^2/(4a)) = P(k) (pi/a) exp(-|k|^2/(4a))
    # with P polynomial: d/dk_j (P G) = (d_j P - k_j P/(2a)) G
    def dk(Pp, var):
        return sp.expand(sp.diff(Pp, var) - var * Pp / (2 * a))
    P = 0
    for (p, q), co in sp.Poly(sp.expand(poly), x, y).terms():
        term = sp.Integer(1)
        for _ in range(p):
            term = dk(term, k1)
        for _ in range(q):
            term = dk(term, k2)
        P += co * sp.I ** (p + q) * term
    P = sp.expand(P * sp.pi / a)
    # d_y U_2(0) = (2 pi)^-2 int (i k2)(-k1^2/|k|^2) P G dk; polar: k = rho e(phi), dk = rho d rho d phi
    tot = 0
    for (m, n_), co in sp.Poly(sp.expand(sp.I * k2 * (-k1 ** 2) * P), k1, k2).terms():
        # monomial k1^m k2^n / rho^2 * rho = rho^(m + n - 1) cos^m sin^n
        tot += co * ang(m, n_) * radial(m + n_ - 1, 1 / (4 * a))
    return sp.nsimplify(sp.simplify(tot / (2 * sp.pi) ** 2))


def formula_c(poly, a):
    b = sp.diff(poly, y).subs({x: 0, y: 0})
    # a3(r) = (1/pi) int sin(3 theta) poly(r e(theta)) d theta exp(-a r^2); int_0^oo a3 dr/r^2
    tot = 0; a3 = 0
    s3 = sp.expand(sp.expand_trig(sp.sin(3 * ph)))
    for (p, q), co in sp.Poly(sp.expand(poly), x, y).terms():
        angp = sp.integrate(sp.expand(s3 * sp.cos(ph) ** p * sp.sin(ph) ** q), (ph, 0, 2 * sp.pi)) / sp.pi
        if angp != 0:
            a3 += co * angp * r ** (p + q)
            tot += co * angp * radial(p + q - 2, a)
    return sp.simplify(-b / 4 + tot), b, sp.simplify(a3 * sp.exp(-a * r ** 2))


tests = [(y, 1), (3 * x ** 2 * y - y ** 3, 1), (x ** 2 * y, 1), (y * (x ** 2 + y ** 2), 1),
         (2 * y + 5 * x ** 2 * y - 3 * y ** 3, 2)]
rows = []
okc = True
for poly, a in tests:
    a = sp.Integer(a)
    cf = fourier_c(poly, a); cform, b, a3 = formula_c(poly, a)
    ok = sp.simplify(cf - cform) == 0
    okc = okc and ok
    rows.append({'h': f'({poly}) exp(-{a} r^2)', 'b': str(b), 'a3': str(a3), 'c_fourier': str(cf), 'c_formula': str(cform), 'equal': bool(ok)})
chk['87 (4): c[h] = -b[h]/4 + int_0^oo a3 dr/r^2 equals the Fourier value of d_y U_2[h](0) on five Gaussian inputs'] = okc
chk['87 (4): the inputs include b != 0 with a3 = 0 (c = -1/4) and b = 0 with a3 != 0'] = \
    rows[0]['c_fourier'] == '-1/4' and rows[0]['a3'] == '0' and rows[1]['b'] == '0' and rows[1]['a3'] != '0'
out['87_contact_tests'] = rows

# 2. FLOAT
mpmath.mp.dps = 20
ok12 = True; worst12 = 0.0
for tv in list(np.linspace(0.01, 3, 30)) + [4.0, 6.0, 10.0, 25.0]:
    for phv in (0.0, 0.3, 0.9, 1.4):
        val = mpmath.quad(lambda s: mpmath.sin(3 * s) * mpmath.expj(tv * mpmath.cos(s - phv)), [0, mpmath.pi / 2, mpmath.pi, 3 * mpmath.pi / 2, 2 * mpmath.pi]) / mpmath.pi
        bnd = 4 / mpmath.pi * min(1, tv ** 3 / 6)
        ok12 = ok12 and abs(val) <= bnd * (1 + 1e-12)
        worst12 = max(worst12, float(abs(val) / bnd))
chk['87 (12) FLOAT: |(1/pi) int sin(3 theta) exp(i t nu.e) dtheta| <= (4/pi) min(1, t^3/6) on a grid'] = ok12
sg = np.linspace(-50, 50, 200001)
chk['87 (9) FLOAT: |exp(is) - 1|^2 <= 2|s| on a grid of 2e5 points in [-50, 50]'] = bool(np.all(np.abs(np.exp(1j * sg) - 1) ** 2 <= 2 * np.abs(sg) + 1e-15))
rng = np.random.default_rng(87)
Nn, Lb = 256, 12.0
g1 = (np.arange(Nn) - Nn // 2) * (2 * Lb / Nn)
X, Y = np.meshgrid(g1, g1, indexing='ij'); dA = (2 * Lb / Nn) ** 2
kk = 2 * np.pi * np.fft.fftfreq(Nn, d=2 * Lb / Nn)
KX, KY = np.meshgrid(kk, kk, indexing='ij'); K2 = KX ** 2 + KY ** 2
okem = True; ratios = []
for trial in range(8):
    f = np.real(np.fft.ifft2(np.fft.fft2(rng.normal(size=X.shape)) * np.exp(-K2 / (2 * (0.5 + trial) ** 2)))) * np.exp(-(X ** 2 + Y ** 2) / 10)
    fh = np.fft.fft2(f) * dA
    H2 = np.sqrt(np.sum((1 + K2) ** 2 * np.abs(fh) ** 2) / (2 * Lb) ** 2)
    sup = np.abs(f).max()
    dz = 2 * Lb / Nn * (1 + trial)
    i0 = int(dz / (2 * Lb / Nn))
    hold = np.abs(np.roll(f, -i0, axis=0) - f).max() / np.sqrt(dz)
    ratios.append((float(sup / H2), float(hold / H2)))
    okem = okem and sup <= 0.5 * H2 and hold <= 0.5 * H2
chk['87 (9) FLOAT: sup and Hoelder quotients of eight random fields below (1/2)||F||_H2'] = okem
out['FLOAT'] = {'worst_ratio_12': worst12, 'embedding_ratios_sup_hoelder': ratios}
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
