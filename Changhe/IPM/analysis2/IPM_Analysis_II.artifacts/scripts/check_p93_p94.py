"""Third computation for verification topics 93 (audit of the numerical polar covering C10 of the state 131 matrix
bound) and 94 (the sharp global margin M >= (c + 2) I for the exact original state 131, equality only at 0).

Written from the statements of topics 93 and 94 only; no verifier code is imported. Routes:

1. Exact (Fraction, sympy):
   Topic 93: the four C10 matrix numbers as exact binary64 rationals and their comparisons with c + 2, 38103/10000
   (topic 92) and 19/5; binary64 0.005 > 1/200 and t0 = (1/200)^2/(1 + (1/200)^2) = 1/40001; the radial and angular
   grids regenerated from the producer formula r_i = 0.005 * 1.02^i, theta_k = k pi/2/80 (733 radial intervals, the
   last ending beyond 10^4); the padded sine at the last angular endpoint exceeds 1 (so the last box reaches the
   axis; directed, with mpmath interval arithmetic); the N4 endpoint gaps of V201 reproduced; the Bernstein
   restriction formula of section 3 against direct re-expansion for random rational polynomials of degrees 4 to 12;
   the box bounds of section 2 by monotonicity.
   The C10 record itself (read only): every expected (i, k) with 0 <= i < 733, 0 <= k < 80 occurs exactly once at
   depth 0, every status is ok, every lower bound is finite and at least 19/5, and the minimum over the cells is the
   reported lambda_cells.
   Topic 94: the origin identities b(0) = 1 - c, q(0) = 0, a(0) = c - 1 + a0 from the 860 exact coefficients; the
   exact quadratic Taylor coefficients of b = chi_xxyy and of chi_xxxy at 0 (from the degree-6 part of chi), which
   give d_t b(0, z) >= min(beta_xx, beta_yy) > 1/4 and |d_t q(0, z)| = |gamma_xy|/2 < 20; c - 1 + a(0) = 2c - 2 + a0
   >= 10; the determinant inequality 10 t/4 - (20 t)^2 >= t(5/2 - 400/40001) > 0 on 0 < t <= 1/40001; 3c + a0 > c + 2;
   (1 - t)^-1 <= 40001/40000; lambda_cells > c + 2 (so the annulus r >= 1/200 has a strictly larger margin).
2. FLOAT: the three bounds (1) of topic 94 and lambda_min(M) > c + 2 on a polar sample of 0 < r <= 1/200, by
   mpmath numerical differentiation (80 digits) of the exact potential.

Usage: python3 check_p93_p94.py VERIFIER_RESEARCH_DIR NUMERICS_DATA_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math, random
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath
ROOT = Path(sys.argv[1]); NUM = Path(sys.argv[2])
OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(__file__).with_suffix('.json')
t00 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}
rng = random.Random(9394)

ps = ROOT / 'source_audit/state131_exact.json'
src = json.loads(ps.read_text()); out['inputs']['source_audit/state131_exact.json'] = sha(ps)
cl = Q(src['exact_parameters']['cl']); a0 = Q(src['exact_parameters']['a0'])
coef = [(tuple(t), Q(v)) for t, v in zip(src['canonical_order'], src['canonical_coefficients'])]
chk['input: 860 canonical coefficients, c = 4076476460239181/2^51'] = len(coef) == 860 and cl == Q(4076476460239181, 2 ** 51)
cp2 = cl + 2
chk['94: c + 2 = 8580076087609677/2251799813685248'] = cp2 == Q(8580076087609677, 2251799813685248)

# 1. topic 93 exact
psum = NUM / 'certM_131_summary.json'
summ = json.loads(psum.read_text()); out['inputs']['certM_131_summary.json'] = sha(psum)
m0, lc, lo_, lf = (Q(summ[k]) for k in ('m0', 'lambda_cells', 'lambda_origin', 'lambda_far'))
chk['93: the C10 numbers are the binary64 rationals of V200 (m0, lambda_cells, lambda_far over 2^48)'] = \
    m0 == Q(1072463607937759, 2 ** 48) and lc == Q(1072512771322849, 2 ** 48) and lf == Q(1281151128927917, 2 ** 48)
chk['93 claims 1, 3: m0 and lambda_origin are below 38103/10000 (topic 92 global bound), so they follow from topic 92'] = \
    m0 < Q(38103, 10000) and lo_ < Q(38103, 10000)
chk['93/94: m0 <= c + 2 (consistent with sharpness); lambda_cells > c + 2; lambda_far > c + 2; all >= 19/5'] = \
    m0 <= cp2 < lc < lf and min(m0, lc, lo_, lf) >= Q(19, 5)
h = Q(0.005)
chk['93: binary64 0.005 exceeds 1/200; t0 = (1/200)^2/(1 + (1/200)^2) = 1/40001'] = \
    h > Q(1, 200) and Q(1, 200) ** 2 / (1 + Q(1, 200) ** 2) == Q(1, 40001)
nr, nt = 733, 80
radii = [0.005 * 1.02 ** i for i in range(nr + 1)]
thetas = [k * math.pi / 2 / nt for k in range(nt + 1)]
chk['93: 733 radial intervals from r_0 = 0.005, increasing, the last endpoint beyond 10^4 and the previous one below'] = \
    radii[0] == 0.005 and all(radii[i] < radii[i + 1] for i in range(nr)) and radii[nr] > 10 ** 4 > radii[nr - 1]
out['93_radial_outer_FLOAT_display'] = radii[nr]
chk['93: theta_0 = 0, theta_80 = pi_float/2 (the float), angles increasing'] = \
    thetas[0] == 0 and thetas[nt] == math.pi / 2 and all(thetas[k] < thetas[k + 1] for k in range(nt))
iv = mpmath.iv
iv.dps = 60
pi_f2 = iv.mpf(Q(thetas[nt]).numerator) / Q(thetas[nt]).denominator  # exact: a 53-bit numerator over a power of 2
chk['93: pi_float/2 < pi/2 and sin(pi_float/2) (1 + 2^-40) > 1 (directed, mpmath.iv), so the last box reaches the axis'] = \
    pi_f2.a == pi_f2.b and pi_f2.b < (iv.pi / 2).a and (iv.sin(pi_f2) * (1 + iv.mpf(2) ** -40)).a > 1
# N4 endpoint gaps (V201): largest selected r_hi with r_hi <= r0 (1 + 1e-12)
n4 = {}
for r0 in (0.05, 0.1, 0.2, 0.5, 1.0):
    n4[r0] = max(r for r in radii[1:] if r <= r0 * (1 + 1e-12))
v201 = {0.05: 0.049726733147885095, 0.1: 0.09944797411048927, 0.2: 0.19888496445701392, 0.5: 0.4945495979121949, 1.0: 0.989044574138017}
chk['93 (V201): the selected N4 unions end at the five reported endpoints, each strictly below its r0'] = \
    all(n4[r0] == v201[r0] and Q(n4[r0]) < Q(r0) for r0 in v201)
# box bounds by monotonicity on [0, pi/2]
okbox = True
for _ in range(400):
    rl = Q(rng.randint(1, 10 ** 6), 1000); rh = rl * Q(102, 100)
    tl = rng.uniform(0, math.pi / 2); th_ = min(math.pi / 2, tl + rng.uniform(0, 0.05))
    for _ in range(5):
        rr = float(rl + (rh - rl) * Q(rng.random())); tt = tl + (th_ - tl) * rng.random()
        xv, yv = rr * math.cos(tt), rr * math.sin(tt)
        okbox = okbox and float(rl) * math.cos(th_) - 1e-9 * rr <= xv <= float(rh) * math.cos(tl) + 1e-9 * rr \
            and float(rl) * math.sin(tl) - 1e-9 * rr <= yv <= float(rh) * math.sin(th_) + 1e-9 * rr
chk['93 section 2 FLOAT: random points of polar cells lie in the monotonicity boxes (2000 points)'] = okbox
# Bernstein restriction formula
tt, ss = sp.symbols('t s')
okb = True
for n in range(4, 13):
    bj = [Q(rng.randint(-1000, 1000), rng.randint(1, 50)) for _ in range(n + 1)]
    t0r = Q(rng.randint(1, 999), 1000)
    Bt = sum(sp.Rational(b.numerator, b.denominator) * sp.binomial(n, j) * tt ** j * (1 - tt) ** (n - j) for j, b in enumerate(bj))
    bp = [sum(math.comb(n - i, j - i) * t0r ** (j - i) * (1 - t0r) ** (n - j) * bj[j] for j in range(i, n + 1)) for i in range(n + 1)]
    Bs = sum(sp.Rational(b.numerator, b.denominator) * sp.binomial(n, i) * ss ** i * (1 - ss) ** (n - i) for i, b in enumerate(bp))
    T0 = sp.Rational(t0r.numerator, t0r.denominator)
    okb = okb and sp.expand(Bt.subs(tt, T0 + (1 - T0) * ss) - Bs) == 0
chk['93 section 3: b_i\' = sum_(j >= i) binom(n - i, j - i) t0^(j - i) (1 - t0)^(n - j) b_j restricts to [t0, 1] (degrees 4 to 12)'] = okb
# the C10 record
pj = NUM / 'certM_131.jsonl'
out['inputs']['certM_131.jsonl'] = sha(pj)
seen = {}; origin = []; bad = 0; finite = True; mins = []
for line in pj.read_text().splitlines():
    d = json.loads(line)
    if d['i'] == -1:
        origin.append(d); continue
    key = (d['i'], d['k'])
    seen[key] = seen.get(key, 0) + 1
    bad += d['status'] != 'ok' or d['depth'] != 0 or bool(d.get('split'))
    v = d['lam_min_lo']; finite = finite and isinstance(v, float) and math.isfinite(v)
    mins.append(v)
expected = {(i, k) for i in range(nr) for k in range(nt)}
chk['93: the C10 record has every expected (i, k) exactly once at depth 0, all ok, no split, plus 3 origin squares'] = \
    set(seen) == expected and all(v == 1 for v in seen.values()) and bad == 0 and len(origin) == 3
chk['93: every cell lower bound is finite and >= 19/5; their minimum is the reported lambda_cells'] = \
    finite and min(Q(v) for v in mins) >= Q(19, 5) and Q(min(mins)) == lc
og = {d['origin_box_h']: d for d in origin}
chk['93: the origin square of half-width 0.005 has the reported lambda_origin'] = Q(og[0.005]['lam_min_lo']) == lo_

# 1. topic 94 exact
gam = 1 / cl; dl = 1 - gam


def ff(q, n):
    p = Q(1)
    for i in range(n):
        p *= q - i
    return p


x, y = sp.symbols('x y', real=True)
P = {4: {}, 6: {}}
for (j, m, k), a in coef:
    if a == 0:
        continue
    q = (3 + gam - j * dl) / 2 - k
    for deg in (4, 6):
        n = deg // 2 - k
        if n < 0:
            continue
        Pm = sp.Poly(sp.expand((x ** 2 + y ** 2) ** (k - m) * sp.re(sp.expand((x + sp.I * y) ** (2 * m))) * (x ** 2 + y ** 2) ** n), x, y)
        w = a * ff(q, n) / math.factorial(n)
        for (e1, e2), cv in Pm.terms():
            P[deg][(e1, e2)] = P[deg].get((e1, e2), Q(0)) + w * Q(int(cv))
T = {d: sum(sp.Rational(v.numerator, v.denominator) * x ** e1 * y ** e2 for (e1, e2), v in P[d].items()) for d in (4, 6)}
chi_T = T[4] + T[6]
b_T = sp.expand(sp.diff(chi_T, x, 2, y, 2)); q_T = sp.expand(sp.diff(chi_T, x, 3, y, 1)); y4_T = sp.expand(sp.diff(chi_T, y, 4))
a_T = sp.expand(-2 * b_T - y4_T)
R = lambda e: Q(int(sp.fraction(e)[0]), int(sp.fraction(e)[1]))
b00 = R(b_T.subs({x: 0, y: 0})); q00 = R(q_T.subs({x: 0, y: 0})); a00 = R(a_T.subs({x: 0, y: 0}))
chk['94: b(0) = chi_xxyy(0) = 1 - c, q(0) = chi_xxxy(0) = 0, a(0) = -2 chi_xxyy(0) - chi_yyyy(0) = c - 1 + a0'] = \
    b00 == 1 - cl and q00 == 0 and a00 == cl - 1 + a0
bxx = R(sp.Poly(b_T, x, y).coeff_monomial(x ** 2)); byy = R(sp.Poly(b_T, x, y).coeff_monomial(y ** 2))
bxy = R(sp.Poly(b_T, x, y).coeff_monomial(x * y)); gxy = R(sp.Poly(q_T, x, y).coeff_monomial(x * y))
qxx = R(sp.Poly(q_T, x, y).coeff_monomial(x ** 2)); qyy = R(sp.Poly(q_T, x, y).coeff_monomial(y ** 2))
chk['94: parity: b has no xy term and chi_xxxy has no x^2, y^2 terms at second order'] = bxy == 0 and qxx == 0 and qyy == 0
chk['94 (1) at t = 0: d_t b(0, z) = beta_xx (1 + z)/2 + beta_yy (1 - z)/2 >= min(beta_xx, beta_yy) > 1/4'] = min(bxx, byy) > Q(1, 4)
chk['94 (1) at t = 0: chi_xxxy = gamma xy + O(r^4), q = chi_xxxy/|sin 2 theta| -> (gamma/2) t, |gamma|/2 < 20'] = abs(gxy) / 2 < 20
chk['94 (1): c - 1 + a(0) = 2c - 2 + a0 >= 10'] = 2 * cl - 2 + a0 >= 10
out['94_origin_derivatives_FLOAT_display'] = {'beta_xx': float(bxx), 'beta_yy': float(byy), 'gamma_xy_over_2': float(gxy / 2),
                                              'c_minus_1_plus_a0': float(2 * cl - 2 + a0)}
t0q = Q(1, 40001)
okdet = all(10 * t / 4 - (20 * t) ** 2 >= t * (Q(5, 2) - Q(400, 40001)) for t in (t0q, t0q / 2, t0q / 1000, Q(1, 10 ** 30)))
chk['94: 10 t/4 - 400 t^2 = t(5/2 - 400 t) >= t(5/2 - 400/40001) > 0 for 0 < t <= 1/40001'] = \
    okdet and Q(5, 2) > Q(400, 40001) and sp.expand(10 * tt / 4 - 400 * tt ** 2 - tt * (sp.Rational(5, 2) - 400 * tt)) == 0
chk['94: (1 - t)^-1 <= 40001/40000 at t = 1/40001; 3c + a0 > c + 2'] = 1 / (1 - t0q) == Q(40001, 40000) and 3 * cl + a0 > cp2
chk['94: reflections x -> -x, y -> -y change only the sign of chi_xxxy (odd in x and in y), so eigenvalues are kept'] = \
    sp.expand(q_T.subs(x, -x) + q_T) == 0 and sp.expand(q_T.subs(y, -y) + q_T) == 0 and sp.expand(b_T.subs(x, -x) - b_T) == 0

# 2. FLOAT near the origin
mpmath.mp.dps = 80
mc = mpmath.mpf(cl.numerator) / cl.denominator
mg = 1 / mc
groups = {}
for (j, m, k), a in coef:
    if a != 0:
        groups.setdefault((j, m), []).append((k - m, mpmath.mpf(a.numerator) / a.denominator))
gl = []
for (j, m), terms in groups.items():
    deg = max(l for l, _ in terms)
    cf = [mpmath.mpf(0)] * (deg + 1)
    for l, a in terms:
        cf[l] += a
    gl.append(((3 + mg - j * (1 - mg)) / 2 - m, m, cf[::-1]))


def chi_f(xv, yv):
    qv = xv * xv + yv * yv; oq = 1 + qv; v = qv / oq
    zz = mpmath.mpc(xv, yv)
    tot = mpmath.mpf(0)
    for e, m, cf in gl:
        tot += (zz ** (2 * m)).real * oq ** e * mpmath.polyval(cf, v)
    return tot


hd = mpmath.mpf(10) ** -14
worst = {'b_slope_min': mpmath.inf, 'q_slope_max': mpmath.mpf(0), 'diag1_min': mpmath.inf, 'shift_min_over_t': mpmath.inf}
oks = True; ns = 0; small = {}
for e in range(0, 26):
    r = mpmath.mpf(1) / 200 * mpmath.mpf(10) ** (-mpmath.mpf(e) / 6)
    t = r * r / (1 + r * r)
    for it in range(13):
        th = mpmath.pi / 2 * it / 12
        xv, yv = r * mpmath.cos(th), r * mpmath.sin(th)
        d22 = mpmath.diff(chi_f, (xv, yv), (2, 2), h=hd)
        d04 = mpmath.diff(chi_f, (xv, yv), (0, 4), h=hd)
        d31 = mpmath.diff(chi_f, (xv, yv), (3, 1), h=hd)
        aa = -2 * d22 - d04; bb = d22
        s2 = abs(mpmath.sin(2 * th))
        A1 = mc - 1 + aa; B1 = bb - (1 - mc)
        lam = (A1 + B1 - mpmath.sqrt((A1 - B1) ** 2 + 4 * d31 ** 2)) / 2
        worst['b_slope_min'] = min(worst['b_slope_min'], B1 / t)
        if s2 > mpmath.mpf(10) ** -30:
            worst['q_slope_max'] = max(worst['q_slope_max'], abs(d31) / (s2 * t))
        else:
            oks = oks and abs(d31) < mpmath.mpf(10) ** -30
        if e == 25:
            small['b'] = min(small.get('b', mpmath.inf), B1 / t)
            if s2 > mpmath.mpf(10) ** -30:
                small['q'] = max(small.get('q', mpmath.mpf(0)), abs(d31) / (s2 * t))
        worst['diag1_min'] = min(worst['diag1_min'], A1); worst['shift_min_over_t'] = min(worst['shift_min_over_t'], lam / t)
        ns += 1
chk[f'94 (1) FLOAT: on {ns} polar samples of 0 < r <= 1/200: (b - (1 - c))/t >= 1/4, |chi_xxxy|/(|sin 2 theta| t) <= 20, c - 1 + a >= 10'] = \
    oks and worst['b_slope_min'] >= mpmath.mpf(1) / 4 and worst['q_slope_max'] <= 20 and worst['diag1_min'] >= 10
chk['94 FLOAT: lambda_min(M) - (c + 2) > 0 at every sample (r > 0), with ratio to t bounded below'] = worst['shift_min_over_t'] > 0
chk['94 FLOAT: at the smallest sampled radius the slopes agree with the exact origin coefficients to 1e-3'] = \
    abs(small['b'] - mpmath.mpf(min(bxx, byy).numerator) / min(bxx, byy).denominator) < 1e-3 and \
    abs(small['q'] - abs(mpmath.mpf(gxy.numerator) / gxy.denominator) / 2) < 1e-3
out['94_FLOAT'] = {k: float(v) for k, v in worst.items()}; out['94_FLOAT']['samples'] = ns
out['94_FLOAT']['smallest_radius_slopes'] = {k: float(v) for k, v in small.items()}
for name in ('93_polar_covering_audit', '94_sharp_original_matrix'):
    pth = ROOT / name / 'verification/status.json'
    out['inputs'][f'{name}/verification/status.json'] = sha(pth)
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t00, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
