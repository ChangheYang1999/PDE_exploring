"""Modular version of hh_tune.py: the same tuned continuation of the pure density/stream series at delta = 2h/Q, carried
out in the prime field F_p instead of Q.  Every exact quantity of hh_tune.py is a rational function of the profile data
whose denominators are products of the nonresonant Poisson divisors, the lambda_n and the responses sigma_k; if none of
them vanishes mod p (checked at every division), each computed residue is the reduction mod p of the exact rational.
Hence a nonzero residue of R_k or sigma_k proves the exact value nonzero.  A zero residue proves nothing by itself.

usage: hh_tune_mod.py Q h profile kmax p      profile as in hh_tune.py (integer coefficients only)
"""
import sys, time
from fractions import Fraction as Fr

Q, H = int(sys.argv[1]), int(sys.argv[2])
prof = sys.argv[3]
KMAX = int(sys.argv[4])
PR = int(sys.argv[5])
if ':' in prof:
    F1r = {int(a): Fr(b) for a, b in (x.split(':') for x in prof.split(','))}
else:
    F1r = {int(prof): Fr(1)}
dl = Fr(2 * H, Q)
cm1 = Fr(2 * H, Q - 2 * H)
k1 = 1 if H >= 2 else 2


def md(x):
    """reduce a rational mod PR, checking that its denominator is invertible"""
    x = Fr(x)
    assert x.denominator % PR != 0, ('denominator divisible by p', x)
    return x.numerator % PR * pow(x.denominator, PR - 2, PR) % PR


def inv(a):
    assert a % PR != 0, 'division by a zero residue'
    return pow(a, PR - 2, PR)


F1 = {m: md(v) for m, v in F1r.items()}
assert all(m % 2 == 1 and m > 0 for m in F1)
HALF = inv(2)


def p_(n):
    return md(1 - n * dl)


def P_(n):
    return md(2 - n * dl)


def add(d, m, v):
    if m == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[m] = (d.get(m, 0) + v) % PR


def clean(d):
    return {m: v for m, v in d.items() if v % PR != 0}


def T(g, Pi, f, pj):
    out = {}
    for l, bb in g.items():
        for m, a in f.items():
            w = bb * a % PR * HALF % PR
            add(out, l + m, (Pi * m - pj * l) * w)
            add(out, m - l, (-pj * l - Pi * m) * w)
    return clean(out)


def pois(f, n, drop=None):
    out = {}
    Pn = 2 - n * dl
    for l, a in f.items():
        if l + 1 != drop:
            den = 2 * (l + 1 + Pn)
            assert den != 0, (n, l)
            add(out, l + 1, -a * md(1 / den))
        if l != 1 and l - 1 != drop:
            den = 2 * (l - 1 - Pn)
            assert den != 0, (n, l)
            add(out, l - 1, a * md(1 / den))
    return clean(out)


def resonant(n):
    return n % Q == 0 and n // Q >= k1


def order(F, G, n):
    acc = {}
    for i in range(1, n):
        for m, v in T(G[i], P_(i), F[n - i], p_(n - i)).items():
            acc[m] = (acc.get(m, 0) + v) % PR
    il = md(1 / ((n - 1) * cm1))
    return clean({m: v * il % PR for m, v in acc.items()})


def stream(F, n, Hval):
    if resonant(n):
        k = n // Q
        assert F[n].get(2 * H * k - 3, 0) % PR == 0, ('obstruction residue not zero at', n)
        g = pois(F[n], n, drop=2 * H * k - 2)
        if Hval:
            add(g, 2 * H * k - 2, Hval)
        return clean(g)
    return pois(F[n], n)


t0 = time.time()
F, G = {1: dict(F1)}, {}
G[1] = stream(F, 1, 0)
n = 1
while n < k1 * Q:
    n += 1
    F[n] = order(F, G, n)
    if n < k1 * Q:
        G[n] = stream(F, n, 0)
O1 = F[k1 * Q].get(2 * H * k1 - 3, 0)
print('p=%d Q=%d h=%d delta=%s f_1=%s; first obstruction O_%d residue %d' % (PR, Q, H, dl, prof, k1 * Q, O1), flush=True)
if O1 != 0:
    print('OBSTRUCTED at the first resonance (nonzero residue)')
    sys.exit(0)
for k in range(k1, KMAX + 1):
    n0 = k * Q
    runs = []
    for Hv in (0, 1):
        Fc, Gc = dict(F), dict(G)
        Gc[n0] = stream(Fc, n0, Hv)
        for n in range(n0 + 1, n0 + Q + 1):
            Fc[n] = order(Fc, Gc, n)
            if n < n0 + Q:
                Gc[n] = stream(Fc, n, 0)
        runs.append((Fc, Gc))
    mode = 2 * H * (k + 1) - 3
    R0 = runs[0][0][n0 + Q].get(mode, 0)
    sig = (runs[1][0][n0 + Q].get(mode, 0) - R0) % PR
    print('k=%d (order %d): R_k residue %d, sigma_k residue %d (mode %d at order %d); %.1fs'
          % (k, n0, R0, sig, mode, n0 + Q, time.time() - t0), flush=True)
    if sig == 0:
        print('sigma_%d residue is 0; R_%d residue %d %s' % (k, k, R0, '(nonzero: R_k != 0 exactly)' if R0 else '(zero)'))
        break
    Hk = (-R0) * inv(sig) % PR
    print('   H_%d residue %d' % (n0, Hk), flush=True)
    (F0, G0), (F1_, G1_) = runs
    G[n0] = stream(F, n0, Hk)
    for n in range(n0 + 1, n0 + Q + 1):
        F[n] = clean({m: (F0[n].get(m, 0) + Hk * (F1_[n].get(m, 0) - F0[n].get(m, 0))) % PR
                      for m in set(F0[n]) | set(F1_[n])})
        if n < n0 + Q:
            G[n] = clean({m: (G0[n].get(m, 0) + Hk * (G1_[n].get(m, 0) - G0[n].get(m, 0))) % PR
                          for m in set(G0[n]) | set(G1_[n])})
    assert F[n0 + Q].get(mode, 0) == 0
print('time %.1fs' % (time.time() - t0))
