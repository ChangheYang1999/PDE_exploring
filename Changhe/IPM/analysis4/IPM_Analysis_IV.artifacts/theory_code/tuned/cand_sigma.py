"""Floating (mpmath) responses sigma_k at delta = 2h/Q, h >= 2, for a general finite sine profile, from the Fourier
form of the recurrence (theory Section 12.6):
  (m^2 - P_n^2) g_{n,m} = (p_n-(m-1))/2 f_{n,m-1} + (p_n+(m+1))/2 f_{n,m+1}         (stream, even m)
  lambda_n f_n = sum_{i+j=n} T(g_i, f_j),  T(g,f) = -p_j g' f + P_i g f'            (density, odd m)
with p_n = 1-n delta, P_n = 2-n delta, lambda_n = delta(n-1)/(1-delta).  The first obstruction is O_Q = [sin((2h-3)theta)] f_Q.
At n = kQ a unit stream harmonic sin(q theta), q = 2hk-2, is inserted, the linear response phi_r at order n+r is
  lambda_{n+r} phi_r = T(e, F_r) + sum_{s<r} [T(G_{r-s}, phi_s) + T(Pi_{n+s} phi_s, F_{r-s})]
and sigma_k = [sin((2h(k+1)-3) theta)] phi_Q.  Independent of tq_symh.py (no symbolic k; plain dictionaries).

usage: cand_sigma.py Q h dps profile b0 kmax [klarge ...]
  profile: 'two' (f_1 = sin + b sin 3) or a JSON file with {"density": {"1": a_1, "3": a_3, ...}} (exact rationals);
  the profile is normalized by a_1 and its sin 3 coefficient replaced by b.  b0: starting guess for the root of O_Q
  (found by the secant method in mpmath); then sigma_k for k = 1..kmax and k in klarge.
"""
import sys, json, time
from fractions import Fraction as Fr
import mpmath as mp

Q, H = int(sys.argv[1]), int(sys.argv[2])
mp.mp.dps = int(sys.argv[3])
PROF, B0, KMAX = sys.argv[4], mp.mpf(sys.argv[5]), int(sys.argv[6])
KLARGE = [int(x) for x in sys.argv[7:]]
dl = mp.mpf(2 * H) / Q
t0 = time.time()

if PROF == 'two':
    HIGHER = {}
else:
    dens = {int(j): Fr(v) for j, v in json.load(open(PROF))['density'].items()}
    a1 = dens[1]
    HIGHER = {j: mp.mpf(v.numerator) / v.denominator / (mp.mpf(a1.numerator) / a1.denominator)
              for j, v in dens.items() if j >= 5}
    print('a_1 =', mp.nstr(mp.mpf(a1.numerator) / a1.denominator, 15), '; original normalized b =',
          mp.nstr(mp.mpf(dens[3].numerator) / dens[3].denominator / (mp.mpf(a1.numerator) / a1.denominator), 15))


def p_(n):
    return 1 - n * dl


def P_(n):
    return 2 - n * dl


def lam(n):
    return dl * (n - 1) / (1 - dl)


def addm(d, m, v):
    """add v sin(m theta) to dict d (m may be <= 0)"""
    if m == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[m] = d.get(m, 0) + v


def T(g, Pi, f, pj):
    """T(g_i, f_j) = -p_j g' f + P_i g f' for sine dicts g (stream, P_i = Pi) and f (density, p_j = pj)"""
    out = {}
    for mu, x in g.items():
        if x == 0:
            continue
        for nu, y in f.items():
            if y == 0:
                continue
            xy = x * y / 2
            addm(out, mu + nu, (-pj * mu + Pi * nu) * xy)
            addm(out, nu - mu, (-pj * mu - Pi * nu) * xy)
    return out


def poisson(f, n, skip=None):
    """stream g_n from density f at order n; skip = resonant mode to delete"""
    pn, Pn = p_(n), P_(n)
    g = {}
    modes = set()
    for m in f:
        modes.add(m + 1)
        if m > 1:
            modes.add(m - 1)
    for j in modes:
        if j == skip:
            continue
        num = (pn - (j - 1)) / 2 * f.get(j - 1, 0) + (pn + (j + 1)) / 2 * f.get(j + 1, 0)
        den = j * j - Pn * Pn
        assert abs(den) > mp.mpf(10) ** (-mp.mp.dps // 2), (n, j)
        g[j] = num / den
    return g


def addto(acc, d, c=1):
    for m, v in d.items():
        acc[m] = acc.get(m, 0) + c * v


def low_fields(b):
    f1 = {1: mp.mpf(1), 3: b}
    f1.update(HIGHER)
    F, G = {1: f1}, {1: poisson(f1, 1)}
    for n in range(2, Q + 1):
        acc = {}
        for i in range(1, n):
            addto(acc, T(G[i], P_(i), F[n - i], p_(n - i)))
        F[n] = {m: v / lam(n) for m, v in acc.items()}
        if n < Q:
            G[n] = poisson(F[n], n)
    return F, G


def O(b):
    F, _ = low_fields(b)
    return F[Q].get(2 * H - 3, 0)


def sigma(k, F, G):
    n = k * Q
    q = 2 * H * k - 2
    assert abs(P_(n) + q) < mp.mpf(10) ** (-mp.mp.dps // 2)
    e = {q: mp.mpf(1)}
    phi, psi = {}, {}
    for r in range(1, Q + 1):
        acc = T(e, P_(n), F[r], p_(r))
        for s in range(1, r):
            addto(acc, T(G[r - s], P_(r - s), phi[s], p_(n + s)))
            addto(acc, T(psi[s], P_(n + s), F[r - s], p_(r - s)))
        phi[r] = {m: v / lam(n + r) for m, v in acc.items()}
        if r < Q:
            psi[r] = poisson(phi[r], n + r)
    return phi[Q].get(2 * H * (k + 1) - 3, 0)


b = mp.findroot(O, (B0, B0 * (1 + mp.mpf(10) ** -6)), solver='secant', tol=mp.mpf(10) ** (-mp.mp.dps + 5))
print('root of O_%d: b = %s, |O(b)| = %s, O(b0) = %s' % (Q, mp.nstr(b, 30), mp.nstr(abs(O(b)), 3), mp.nstr(O(B0), 6)))
norm = 1 + abs(b) + sum(abs(v) for v in HIGHER.values())
print('||f_1||_1 (normalized) =', mp.nstr(norm, 20))
F, G = low_fields(b)
vals = {}
for k in list(range(1, KMAX + 1)) + KLARGE:
    vals[k] = sigma(k, F, G)
print('sigma_k:', ' '.join('%d:%s' % (k, mp.nstr(v, 8)) for k, v in vals.items()))
kmin = min(vals, key=lambda k: abs(vals[k]))
print('min |sigma_k| over computed k: %s at k = %d' % (mp.nstr(abs(vals[kmin]), 10), kmin))
print('time %.1fs' % (time.time() - t0))
