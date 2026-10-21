# Own sampled N-distances (fred22 02 (12), r = 1/2, sigma = 1, theta = 9/10) between polynomial references
# w = -A u (1-u^2)/(1+u^2) + u^3 (1-u^2)^2 q(u^2).  For a pair (a, b): v = w_a - (A_a/A_b) w_b = u^3 (1-u^2)^2 p(u^2),
# p = q_a - (A_a/A_b) q_b (the -A u (1-u^2)/(1+u^2) parts cancel exactly).  Exact Taylor coefficients of v (mpmath,
# 40 digits); the remainder R_v = v - c3 u^3 - c5 u^5 - c7 u^7 (monomial convention of (12)); variant 'phi' uses
# R = v - sum c_j phi_j.  Suprema by dense sampling (mpmath at the sample points) plus local refinement.
import json, sys, itertools
import mpmath as mp
mp.mp.dps = 40
L = 'lead'
refs = {'R12': (mp.mpf('10.150725'), [])}
for K in (10, 12, 14, 16, 18):
    d = json.load(open(L + '/b3_functional/xref/ref_c6g_K%d.json' % K))
    refs['K%d' % K] = (mp.mpf(repr(d['A'])), [mp.mpf(s) for s in d['q_monomial']])
d = json.load(open(L + '/exclusion_certificates/reference_fit/data/fitted_reference.json'))
refs['fit'] = (mp.mpf(d['A0_exact']), [mp.mpf(s) for s in d['q_power_coefficients_exact_decimal']])

def poly_mul(a, b):
    c = [mp.mpf(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

def v_coeffs(p):
    # coefficients in u of u^3 (1-u^2)^2 p(u^2)
    pu = [mp.mpf(0)] * (2 * len(p) - 1 if p else 1)
    for j, x in enumerate(p):
        pu[2 * j] = x
    c = poly_mul([mp.mpf(0)] * 3 + [mp.mpf(1)], poly_mul([1, 0, -2, 0, 1], pu))
    return [mp.mpf(x) for x in c]

def ev(c, x):
    return mp.polyval(c[::-1], x)

def deriv(c, n=1):
    for _ in range(n):
        c = [k * c[k] for k in range(1, len(c))]
    return c

def sup_abs(c, lo, hi, n=4000, f=None):
    f = f or (lambda x: abs(ev(c, x)))
    xs = [lo + (hi - lo) * mp.mpf(i) / n for i in range(n + 1)]
    vals = [f(x) for x in xs]
    i = max(range(len(xs)), key=lambda k: vals[k])
    best = vals[i]; xb = xs[i]
    a, b = xs[max(i - 1, 0)], xs[min(i + 1, n)]
    for _ in range(60):   # golden-section refinement of the sampled maximum
        m1, m2 = a + (b - a) * 0.382, a + (b - a) * 0.618
        if f(m1) > f(m2): b = m2
        else: a = m1
    xm = (a + b) / 2
    if f(xm) > best: best, xb = f(xm), xm
    return best, xb

def ndist(c, variant='mono'):
    c = c + [mp.mpf(0)] * max(0, 12 - len(c))
    cj = [c[3], c[5], c[7]]
    t1 = sum(abs(x) for x in cj)
    R = list(c); R[3] = R[5] = R[7] = mp.mpf(0)
    if variant == 'phi':
        R = R + [mp.mpf(0)] * max(0, 12 - len(R))
        for j, x in zip((3, 5, 7), cj):
            R[9] -= x * mp.mpf(j - 11) / 2; R[11] -= x * mp.mpf(9 - j) / 2
    assert all(abs(R[k]) == 0 for k in range(9))
    R2 = deriv(R, 2)                      # starts at u^7
    R2s = R2[6:]                          # u^-6 R''
    t2, x2 = sup_abs(R2s, mp.mpf(0), mp.mpf(1) / 2)
    v2 = deriv(c, 2)
    t3, x3 = sup_abs(v2, mp.mpf(1) / 2, mp.mpf(1))
    v21 = ev(v2, 1)
    th = mp.mpf(9) / 10
    f4 = lambda x: abs(ev(v2, x) - v21) / (1 - x) ** th if x < 1 else mp.mpf(0)
    t4, x4 = sup_abs(v2, mp.mpf(1) / 2, mp.mpf(1), f=f4)
    return t1 + t2 + t3 + t4, dict(jet=mp.nstr(t1, 6), origin=mp.nstr(t2, 6), u_origin=mp.nstr(x2, 4), C2=mp.nstr(t3, 6),
                                     endpoint=mp.nstr(t4, 6), u_end=mp.nstr(x4, 4))

pairs = [('R12', 'K12'), ('R12', 'K18'), ('R12', 'fit'), ('fit', 'K18'), ('fit', 'K12'), ('K12', 'K18'),
         ('K10', 'K12'), ('K14', 'K16'), ('K16', 'K18'), ('K10', 'fit')]
ALL = len(sys.argv) > 1 and sys.argv[1] == 'all'
if ALL:   # all 21 pairs among R12, K10..K18 and the fitted reference
    pairs = list(itertools.combinations(['R12', 'K10', 'K12', 'K14', 'K16', 'K18', 'fit'], 2))
out = {}
for a, b in pairs:
    Aa, qa = refs[a]; Ab, qb = refs[b]
    s = Aa / Ab
    n = max(len(qa), len(qb))
    p = [(qa[k] if k < len(qa) else 0) - s * (qb[k] if k < len(qb) else 0) for k in range(n)]
    c = v_coeffs(p)
    for var in ('mono', 'phi'):
        tot, parts = ndist(c, var)
        out['%s-%s-%s' % (a, b, var)] = dict(total=mp.nstr(tot, 6), **parts)
        print('%-4s - %-4s (%s): N = %s  %s' % (a, b, var, mp.nstr(tot, 6), parts), flush=True)
json.dump(out, open('verifier/early_runs/ndist_ver%s.json' % ('_all' if ALL else ''), 'w'), indent=1)
