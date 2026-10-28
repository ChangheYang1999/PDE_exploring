"""Third computation for verification topic 62 (explicit weighted residual floors from the finite power
representation, N_(s,R)(F) >= [2048/(1+6s)] E_J D_(J,K,epsilon)/sqrt(2)).

Written from the statement in topic 62 only; no verifier code is imported.
1. Exact scalar facts: 2048*4096 - 2045*4102 = 18; 26*2^22 < 2^53; 23/5 < 5; the first Bessel moment
   sqrt(pi) s sqrt(1+s/2)/(1+s) < 2s for 0 < s <= 1/16 (from pi(1+s/2) < 4(1+s)^2, a polynomial with positive
   coefficients after pi < 22/7); M2 = -Laplacian of (1+|xi|^2)^(-s/2) at 0 equals 2s (sympy); the closed form of M1
   against a direct quadrature of the heat-mixture kernel at s = 1/16 and s = 2^-12.
2. The radial identity P0(F)^2 = (pi/2) sum_m int_0^1 u^(11/5) |v_m|^2/(1-u) du with F_m = sqrt(t) u^(-1/2) H_m,
   v_m = t u^-2 H_m, u = (1+r^2)^-1: checked by mpmath quadrature in r and in u for two test functions.
3. The Muntz distance formula dist(u^b*, span{u^b_i}) = (2b*+1)^(-1/2) prod |b_i - b*|/(b_i + b* + 1), checked in
   exact rationals against the Schur complement G** - g^T G^-1 g (Gaussian elimination) for five exponent sets.
4. For the twelve rows (J, K, epsilon) the exponent set A is built, distinctness, a > -1/2, a* in A and the dimension
   are checked exactly; D^2 is formed as an exact rational (python-flint fmpq, one factor per exponent) and
   bound^2 = 2045^2 pi (sum_m e_m^2) D^2 / 2 is compared with the record endpoints and display floors using rational
   bounds for pi.
5. The six-branch vector e_6 is recomputed from the source potentials of three refits (nb_stableA2_exact,
   nb_Mpen2_exact, nb_d2_exact): the far-field residual sector of exponent gamma - 6 delta is formed exactly from the
   leading potential sectors r^(3+gamma-j delta) sum_m (sum_k a_(j,m,k)) cos(2 m theta), j <= 5, with the Cartesian
   derivative rules of check_p52; its sine coefficients must agree with each other and with the vector used in topic
   62. The seven-branch vector e_7 is read from its record (hash recorded).

Usage: python3 check_p62.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sys.argv = [sys.argv[0], str(ROOT)]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_jet_distance as cj
import sympy as sp
import mpmath
from mpmath import iv, mp
from flint import fmpq, fmpq_poly
sys.set_int_max_str_digits(0)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
fq = lambda x: fmpq(Q(x).numerator, Q(x).denominator)
tq = lambda x: Q(int(x.p), int(x.q))
t_start = time.monotonic()
out = {'inputs': {}}

# ---------- 1. scalar facts ----------
s = sp.symbols('s', positive=True)
p1 = {'2048*4096-2045*4102': 2048 * 4096 - 2045 * 4102, '26*2^22<2^53': 26 * 2 ** 22 < 2 ** 53, '23/5<5': Q(23, 5) < 5}
poly = sp.Poly(sp.expand(4 * (1 + s) ** 2 - sp.Rational(22, 7) * (1 + s / 2)), s)
p1['moment_poly_positive_coefficients'] = all(cf > 0 for cf in poly.all_coeffs())
p1['pi<22/7'] = bool(sp.pi < sp.Rational(22, 7))
xi1, xi2 = sp.symbols('xi1 xi2', real=True)
m_ = (1 + xi1 ** 2 + xi2 ** 2) ** (-s / 2)
p1['M2=2s'] = bool(sp.simplify(-(sp.diff(m_, xi1, 2) + sp.diff(m_, xi2, 2)).subs({xi1: 0, xi2: 0}) - 2 * s) == 0)
mp.dps = 30
for sv in (mpmath.mpf(1) / 16, mpmath.mpf(2) ** -12):
    q = sv / 2
    closed = mpmath.sqrt(mpmath.pi) * mpmath.gamma(q + 0.5) / mpmath.gamma(q)
    # M1 = int_0^inf Gamma(q)^-1 e^-t t^(q-1) sqrt(pi t) dt (mean of |X| under the 2D heat kernel is sqrt(pi t))
    direct = mpmath.quad(lambda t: mpmath.exp(-t) * t ** (q - 1) * mpmath.sqrt(mpmath.pi * t), [0, 1, mpmath.inf]) / mpmath.gamma(q)
    bound = mpmath.sqrt(mpmath.pi) * sv * mpmath.sqrt(1 + sv / 2) / (1 + sv)
    p1[f'M1_s={float(sv)}'] = {'closed': float(closed), 'quadrature': float(direct), 'jensen_bound': float(bound),
                               'rel_diff': float(abs(closed - direct) / closed), 'agree': abs(closed - direct) < 1e-10 * closed, 'below_jensen': closed <= bound, 'below_2s': bound < 2 * sv}
out['part1'] = p1; print('part 1', p1, flush=True)
assert p1['2048*4096-2045*4102'] == 18 and all(v for k, v in p1.items() if isinstance(v, bool))
assert all(v['agree'] and v['below_jensen'] and v['below_2s'] for k, v in p1.items() if isinstance(v, dict))

# ---------- 2. radial identity ----------
mp.dps = 25
p2 = []
for H, label in [(lambda u: u ** mpmath.mpf('0.9') * (1 - u) ** 2, 'u^0.9 t^2'), (lambda u: u ** mpmath.mpf('0.65') * (2 - u), 'u^0.65 (1+t)')]:
    def Fm(r):
        u = 1 / (1 + r * r); t = 1 - u
        return mpmath.sqrt(t) / mpmath.sqrt(u) * H(u)
    lhs = mpmath.quad(lambda r: (1 + r * r) ** mpmath.mpf(-1.2) * Fm(r) ** 2 * r, [0, 1, 10, 100, mpmath.inf])
    def integrand(u):
        t = 1 - u; v = t / u ** 2 * H(u)
        return u ** mpmath.mpf(2.2) * v * v / t / 2
    rhs = mpmath.quad(integrand, [0, mpmath.mpf(1) / 2, 1])
    p2.append({'test': label, 'r_side': float(lhs), 'u_side': float(rhs), 'agree': abs(lhs - rhs) < 1e-12 * abs(lhs)})
out['part2_radial_identity'] = p2; print('part 2', p2, flush=True)
assert all(x['agree'] for x in p2)


# ---------- 3. Muntz distance ----------
def schur(bs, star):
    others = [b for i, b in enumerate(bs) if i != star]; bst = bs[star]
    G = [[Q(1) / (x + y + 1) for y in others] for x in others]; g = [Q(1) / (x + bst + 1) for x in others]
    n = len(others); A = [row[:] + [g[i]] for i, row in enumerate(G)]
    for i in range(n):
        piv = A[i][i]
        for j in range(i + 1, n):
            f = A[j][i] / piv
            A[j] = [a - f * b for a, b in zip(A[j], A[i])]
    x = [Q(0)] * n
    for i in reversed(range(n)):
        x[i] = (A[i][n] - sum((A[i][j] * x[j] for j in range(i + 1, n)), Q(0))) / A[i][i]
    return Q(1) / (2 * bst + 1) - sum((gi * xi for gi, xi in zip(g, x)), Q(0))


def muntz(bs, star):
    bst = bs[star]; v = Q(1) / (2 * bst + 1)
    for i, b in enumerate(bs):
        if i != star: v *= ((b - bst) / (b + bst + 1)) ** 2
    return v


p3 = []
for bs, star in [([Q(-2, 5), Q(1, 3), Q(1, 2), Q(7, 4)], 0), ([Q(-1, 3), Q(1, 7), Q(3, 5), Q(6, 5), Q(13, 4)], 2),
                 ([Q(0), Q(1), Q(2), Q(3), Q(4), Q(5)], 5), ([Q(1, 10), Q(11, 10), Q(21, 10), Q(31, 10), Q(5, 7)], 4),
                 ([Q(-9, 20), Q(-1, 4), Q(1, 9), Q(2), Q(5, 2), Q(19, 6), Q(4)], 3)]:
    a, b = schur(bs, star), muntz(bs, star)
    p3.append({'exponents': [str(x) for x in bs], 'star': star, 'distance_squared': str(b), 'equal': a == b})
out['part3_muntz'] = p3; print('part 3', [x['equal'] for x in p3], flush=True)
assert all(x['equal'] for x in p3)

# ---------- 5 (first): e_6 from the source potentials ----------
ver = ROOT / '62_weighted_cauchy/verification'
rec = json.loads((ver / 'compute.json').read_text()); out['inputs']['62/compute.json'] = sha(ver / 'compute.json')
p6 = ROOT / '23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json'
p7 = ROOT / '32_stationary_order_seven/verification/recur_sine.json'
for p in (p6, p7):
    out['inputs'][str(p.relative_to(ROOT))] = sha(p)
e6_rec = {int(k): Q(v) for k, v in json.loads(p6.read_text())['leading_sine_coefficients'].items()}
e7_rec = {int(k): Q(v) for k, v in json.loads(p7.read_text())['order8_fixed_defect']['sine_coefficients'].items()}


class S:
    """r^p * i^ip * sum_n c[n - lo] e^(i n theta)."""
    def __init__(self, lo_, c, ip=0):
        self.lo, self.c, self.ip = lo_, list(c), ip

    def norm(self):
        while self.c and self.c[-1] == 0: self.c.pop()
        k = 0
        while k < len(self.c) and self.c[k] == 0: k += 1
        self.c = self.c[k:]; self.lo += k
        return self

    def add(self, o):
        if not o.c: return S(self.lo, self.c, self.ip)
        if not self.c: return S(o.lo, o.c, o.ip)
        assert self.ip == o.ip
        l = min(self.lo, o.lo); h = max(self.lo + len(self.c), o.lo + len(o.c))
        r = [fmpq(0)] * (h - l)
        for i, x in enumerate(self.c): r[self.lo - l + i] += x
        for i, x in enumerate(o.c): r[o.lo - l + i] += x
        return S(l, r, self.ip).norm()

    def mul(self, o):
        if not self.c or not o.c: return S(0, [])
        pr = (fmpq_poly(self.c) * fmpq_poly(o.c)).coeffs()
        ip = self.ip + o.ip; sg = 1
        if ip == 2: ip, sg = 0, -1
        return S(self.lo + o.lo, [sg * x for x in pr], ip).norm()


def dxy(s_, p, axis):
    if not s_.c: return S(0, [])
    p = fq(p); r = [fmpq(0)] * (len(s_.c) + 2)
    for i, x in enumerate(s_.c):
        n = s_.lo + i
        r[i] += (p + n) / 2 * x
        r[i + 2] += ((p - n) / 2 if axis == 0 else -(p - n) / 2) * x
    o = S(s_.lo - 1, r, s_.ip)
    if axis == 1:
        o.ip += 1
        if o.ip == 2: o.ip = 0; o.c = [-x for x in o.c]
    return o.norm()


def d(s_, p, ax, ay):
    """d_x^ax d_y^ay of r^p s_ (exponent p - ax - ay)."""
    for i in range(ax): s_ = dxy(s_, p - i, 0)
    for i in range(ay): s_ = dxy(s_, p - ax - i, 1)
    return s_


def e6_from_source(name):
    pth, shs, c, a0, terms = cj.source(name); out['inputs'][str(pth.relative_to(ROOT))] = shs
    g = 1 / c; dl = 1 - g
    pot = {}
    for (j, m, k), a in terms:
        dd = pot.setdefault(j, {})
        if m == 0: dd[0] = dd.get(0, Q(0)) + a
        else:
            dd[2 * m] = dd.get(2 * m, Q(0)) + a / 2; dd[-2 * m] = dd.get(-2 * m, Q(0)) + a / 2
    assert max(pot) == 5
    f = {}
    for j, dd in pot.items():
        p = 3 + g - j * dl; l, h = min(dd), max(dd); sj = S(l, [fq(dd.get(n, Q(0))) for n in range(l, h + 1)]).norm()
        neg = lambda x: S(x.lo, [-y for y in x.c], x.ip)
        rx = neg(d(sj, p, 3, 1).add(d(sj, p, 1, 3)))           # d_x rho, rho = -chi_xxy - chi_yyy
        ry = neg(d(sj, p, 2, 2).add(d(sj, p, 0, 4)))           # d_y rho
        u1 = neg(d(sj, p, 1, 2)); u2 = d(sj, p, 2, 1)          # U = (-chi_xyy, chi_xxy)
        f[j] = (rx, ry, u1, u2)
    sec = S(0, [], 1)
    for j1 in range(6):
        j2 = 5 - j1
        sec = sec.add(f[j1][2].mul(f[j2][0]).add(f[j1][3].mul(f[j2][1])))
    assert sec.ip == 1
    sine = {}
    for i, x in enumerate(sec.c):
        n = sec.lo + i
        if n > 0:
            xm = sec.c[-n - sec.lo] if 0 <= -n - sec.lo < len(sec.c) else fmpq(0)
            assert xm == -x
            if x != 0: sine[n] = tq(xm - x)
        elif n == 0: assert x == 0
    return sine


p5 = {}
vecs = {}
for name in ['nb_stableA2_exact', 'nb_Mpen2_exact', 'nb_d2_exact']:
    vecs[name] = e6_from_source(name)
    p5[name] = {'harmonics': len(vecs[name]), 'equals_topic62_vector': vecs[name] == e6_rec,
                'seconds': round(time.monotonic() - t_start, 1)}
    print('e6', name, p5[name], flush=True)
p5['e7_from_record_harmonics'] = len(e7_rec); p5['e7_nonzero'] = any(v != 0 for v in e7_rec.values())
out['part5_e6'] = p5
assert all(v['equals_topic62_vector'] for k, v in p5.items() if isinstance(v, dict)) and p5['e7_nonzero']

# ---------- 4. exact products ----------
c = Q(4076476460239181, 2251799813685248); g = 1 / c; dl = 1 - g
assert Q(rec['delta']) == dl and dl.denominator == 4076476460239181
iv.prec = 800
pi_lo, pi_hi = cj.lo(iv.pi), cj.hi(iv.pi)
FLOORS = {(6, 75, 0): Q(6, 10 ** 55), (6, 75, 1): Q(139, 10 ** 55), (7, 69, 0): Q(346, 10 ** 77), (7, 69, 1): Q(775, 10 ** 76)}


def dyad(pr):
    m, e = pr
    return Q(m) * Q(2) ** e


rows = []
prev = {}
for r in rec['rows']:
    J, K, eps = r['J'], r['K'], r['epsilon']; M = 2 * K + 4; ast = (J + 1) * dl / 2 - 2
    removed = {(l, 0) for l in range(1, J + 1)} | {(1, 1), (2, 1)} | ({(3, 1)} if eps else set())
    A = [l * dl / 2 + k - 2 for l in range(1, 2 * J + 1) for k in range(M + 1) if (l, k) not in removed]
    assert len(set(A)) == len(A) == r['dimension'] and ast in A and min(A) > Q(-1, 2)
    D2 = fmpq(1) / fq(2 * ast + Q(16, 5))
    for a in A:
        if a == ast: continue
        num, den = abs(a - ast), a + ast + Q(16, 5)
        assert 0 < num < den
        D2 *= fq(num / den) ** 2
    D2 = tq(D2)
    s2 = sum((v * v for v in e6_rec.values()) if J == 6 else (v * v for v in e7_rec.values()), Q(0))
    b2_lo = Q(2045) ** 2 * pi_lo * s2 * D2 / 2; b2_hi = Q(2045) ** 2 * pi_hi * s2 * D2 / 2
    lo_, hi_ = dyad(r['lower_formula_exact_interval']['lo']), dyad(r['lower_formula_exact_interval']['hi'])
    fl = FLOORS.get((J, K, eps))
    rr = {'J': J, 'K': K, 'epsilon': eps, 'dimension': len(A), 'bound_approx': float(mpmath.sqrt(mpmath.mpf(b2_lo.numerator) / b2_lo.denominator)),
          'record_interval_encloses': lo_ > 0 and lo_ ** 2 < b2_lo and b2_hi < hi_ ** 2,
          'below_2^-30': b2_hi < Q(1, 2 ** 60), 'floor': str(fl) if fl else None, 'above_floor': (fl ** 2 < b2_lo) if fl else None}
    if (J, eps) in prev: rr['decreasing_in_K'] = D2 < prev[J, eps]
    prev[J, eps] = D2
    rows.append(rr); print('row', rr, round(time.monotonic() - t_start, 1), flush=True)
out['part4_rows'] = rows
assert all(x['record_interval_encloses'] and x['below_2^-30'] and x['above_floor'] is not False and x.get('decreasing_in_K', True) for x in rows)
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t_start, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
