"""Exact tuned continuation of the pure density/stream series at delta = 2h/Q (gcd(h,Q) = 1, 2h < Q) for a finite odd
sine profile f_1, in the polar Fourier form of the recursion (independent of the Cartesian Laurent implementation).

Recursion: lambda_n f_n = sum_{i+j=n} [P_i g_i f_j' - p_j g_i' f_j], lambda_n = (n-1)(c-1), p_n = 1 - n delta,
P_n = 2 - n delta; Poisson inverse Pi_n sin(l theta) = sin((l-1) theta)/(2(l-1-P_n)) - sin((l+1) theta)/(2(l+1+P_n))
(no first term for l = 1).  Resonances at n = kQ (k >= 1 if h >= 2, k >= 2 if h = 1): the density mode 2hk-3 must
vanish (obstruction O_kQ), the resonant output sin((2hk-2) theta) is dropped from the particular stream, and
H_kQ sin((2hk-2) theta) is added with H_kQ free.  Each H_kQ is tuned exactly: two provisional continuations to (k+1)Q with
H_kQ = 0 and H_kQ = 1 give R_k and R_k + sigma_k (the block is affine in H_kQ); if sigma_k != 0, H_kQ = -R_k/sigma_k and
the tuned block is the affine combination; if sigma_k = 0 the run stops and reports R_k (nonzero R_k = obstruction for
every choice of the free constants, given that all earlier sigma were nonzero).

usage: hh_tune.py Q h profile kmax      profile: 'M' (f_1 = sin M theta) or 'm1:c1,m2:c2,...' with rational c_i
"""
import sys, time, json
from fractions import Fraction as Fr

Q, H = int(sys.argv[1]), int(sys.argv[2])
prof = sys.argv[3]
KMAX = int(sys.argv[4])
if ':' in prof:
    F1 = {int(a): Fr(b) for a, b in (x.split(':') for x in prof.split(','))}
else:
    F1 = {int(prof): Fr(1)}
assert all(m % 2 == 1 and m > 0 for m in F1)
dl = Fr(2 * H, Q)
cm1 = Fr(2 * H, Q - 2 * H)
k1 = 1 if H >= 2 else 2


def p_(n):
    return 1 - n * dl


def P_(n):
    return 2 - n * dl


def add(d, m, v):
    if m == 0 or v == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[m] = d.get(m, 0) + v


def T(g, Pi, f, pj):
    out = {}
    for l, bb in g.items():
        for m, a in f.items():
            w = bb * a / 2
            add(out, l + m, (Pi * m - pj * l) * w)
            add(out, m - l, (-pj * l - Pi * m) * w)
    return {m: v for m, v in out.items() if v != 0}


def pois(f, n, drop=None):
    out = {}
    Pn = P_(n)
    for l, a in f.items():
        if l + 1 != drop:
            den = 2 * (l + 1 + Pn)
            assert den != 0, (n, l)
            add(out, l + 1, -a / den)
        if l != 1 and l - 1 != drop:
            den = 2 * (l - 1 - Pn)
            assert den != 0, (n, l)
            add(out, l - 1, a / den)
    return {m: v for m, v in out.items() if v != 0}


def resonant(n):
    return n % Q == 0 and n // Q >= k1


def order(F, G, n):
    acc = {}
    for i in range(1, n):
        for m, v in T(G[i], P_(i), F[n - i], p_(n - i)).items():
            acc[m] = acc.get(m, 0) + v
    lam = (n - 1) * cm1
    return {m: v / lam for m, v in acc.items() if v != 0}


def stream(F, n, Hval):
    if resonant(n):
        k = n // Q
        assert F[n].get(2 * H * k - 3, 0) == 0, ('obstruction not zero at', n)
        g = pois(F[n], n, drop=2 * H * k - 2)
        if Hval:
            add(g, 2 * H * k - 2, Hval)
        return {m: v for m, v in g.items() if v != 0}
    return pois(F[n], n)


t0 = time.time()
F, G = {1: dict(F1)}, {}
G[1] = stream(F, 1, 0)
n = 1
res = []
# orders up to the first resonance
while n < k1 * Q:
    n += 1
    F[n] = order(F, G, n)
    if n < k1 * Q:
        G[n] = stream(F, n, 0)
O1 = F[k1 * Q].get(2 * H * k1 - 3, 0)
print('Q=%d h=%d delta=%s f_1=%s; first obstruction O_%d = %s' % (Q, H, dl, prof, k1 * Q, float(O1)), flush=True)
if O1 != 0:
    print('OBSTRUCTED at the first resonance (no free constant precedes it)')
    sys.exit(0)
for k in range(k1, KMAX + 1):
    n0 = k * Q
    runs = []
    for Hv in (Fr(0), Fr(1)):
        Fc, Gc = dict(F), dict(G)
        Gc[n0] = stream(Fc, n0, Hv)
        for n in range(n0 + 1, n0 + Q + 1):
            Fc[n] = order(Fc, Gc, n)
            if n < n0 + Q:
                Gc[n] = stream(Fc, n, 0)
        runs.append((Fc, Gc))
    mode = 2 * H * (k + 1) - 3
    R0 = runs[0][0][n0 + Q].get(mode, 0)
    sig = runs[1][0][n0 + Q].get(mode, 0) - R0
    rec = {'k': k, 'n': n0, 'R_k': float(R0), 'sigma_k': float(sig)}
    print('k=%d (order %d): R_k = %.12e, sigma_k = %.12e, obstruction mode %d at order %d; %.1fs'
          % (k, n0, float(R0), float(sig), mode, n0 + Q, time.time() - t0), flush=True)
    if sig == 0:
        rec['R_exact_num_digits'] = len(str(abs(R0.numerator)))
        rec['R_exact_den_digits'] = len(str(R0.denominator))
        rec['R_sign'] = (R0 > 0) - (R0 < 0)
        res.append(rec)
        print('sigma_%d = 0 exactly; R_%d %s 0 exactly (numerator %d digits, denominator %d digits)'
              % (k, k, '!=' if R0 != 0 else '==', rec['R_exact_num_digits'], rec['R_exact_den_digits']))
        exact_name = 'hh_tune_Q%dh%d_%s_R%d_exact.json' % (Q, H, prof.replace(':', '_').replace(',', '-'), k)
        json.dump({'Q': Q, 'h': H, 'profile': prof, 'k': k, 'order': n0 + Q, 'mode': mode, 'sigma_k': '0',
                   'R_k_numerator': str(R0.numerator), 'R_k_denominator': str(R0.denominator),
                   'earlier': res[:-1]}, open(exact_name, 'w'))
        print('exact R_%d written to %s' % (k, exact_name))
        if R0 != 0:
            print('OBSTRUCTED at order %d for every choice of the free constants' % (n0 + Q))
        break
    Hk = -R0 / sig
    rec['H'] = float(Hk)
    res.append(rec)
    print('   H_%d = %.15e' % (n0, float(Hk)), flush=True)
    # affine combination of the two runs (exact through order n0 + Q)
    (F0, G0), (F1_, G1_) = runs
    G[n0] = stream(F, n0, Hk)
    for n in range(n0 + 1, n0 + Q + 1):
        F[n] = {m: F0[n].get(m, 0) + Hk * (F1_[n].get(m, 0) - F0[n].get(m, 0))
                for m in set(F0[n]) | set(F1_[n])}
        F[n] = {m: v for m, v in F[n].items() if v != 0}
        if n < n0 + Q:
            G[n] = {m: G0[n].get(m, 0) + Hk * (G1_[n].get(m, 0) - G0[n].get(m, 0))
                    for m in set(G0[n]) | set(G1_[n])}
            G[n] = {m: v for m, v in G[n].items() if v != 0}
    # direct check: recompute the tuned block and compare
    Fd, Gd = dict(F), dict(G)
    for n in range(n0 + 1, n0 + Q + 1):
        Fd[n] = order(Fd, Gd, n)
        assert Fd[n] == F[n], ('affine combination differs from direct recomputation at', n)
        if n < n0 + Q:
            Gd[n] = stream(Fd, n, 0)
            assert Gd[n] == G[n]
    assert F[n0 + Q].get(mode, 0) == 0
    print('   tuned block recomputed directly: identical; obstruction at order %d is 0' % (n0 + Q), flush=True)
print('time %.1fs' % (time.time() - t0))
