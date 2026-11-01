"""Floating-point tuned continuation of the pure density/stream series at delta = 2h/Q (gcd(h,Q) = 1, 2h < Q), h >= 2,
for a finite odd sine profile f_1, in the polar Fourier form of the recursion of hh_tune.py (same conventions: the
resonant output sin((2hk-2) theta) is dropped from the particular stream at n = kQ and H_kQ sin((2hk-2) theta) is added,
with H_kQ = -R_k/sigma_k fixed by the next obstruction).  Dense coefficient arrays (index = frequency), direct
convolutions.  Purpose: finite-order growth constants (NUMERICAL EVIDENCE only; nothing here is a proof).

Homogeneity: with f_1 = eps*profile, f_n scales as eps^n, H_kQ as eps^(kQ), sigma_k as eps^Q and R_k as eps^((k+1)Q).
The run uses the amplitude eps given on the command line (to keep the coefficients near unit size) and reports all
quantities rescaled to unit amplitude.

usage: hh_float.py Q h profile N eps [dtype]     profile: 'M' or 'm1:c1,m2:c2'; dtype: float64 (default) or longdouble
output: one line per order n: n, log10 ||f_n||_1, log10 ||g_n||_1 (unit amplitude); one line per block: k, sign and log10|R_k|, sigma_k, sign and
log10|H_kQ| (unit amplitude), relative residual of the tuned obstruction
"""
import sys, time
import numpy as np
from fractions import Fraction as Fr

Q, H = int(sys.argv[1]), int(sys.argv[2])
prof = sys.argv[3]
N = int(sys.argv[4])
EPS = float(Fr(sys.argv[5]))
DT = np.longdouble if (len(sys.argv) > 6 and sys.argv[6] == 'longdouble') else np.float64
if ':' in prof:
    F1 = {int(a): float(Fr(b)) for a, b in (x.split(':') for x in prof.split(','))}
else:
    F1 = {int(prof): 1.0}
assert H >= 2 and Q > 2 * H
dl = DT(2 * H) / DT(Q)
cm1 = DT(2 * H) / DT(Q - 2 * H)
LOGEPS = np.log10(EPS)


def p_(n):
    return 1 - n * dl


def P_(n):
    return 2 - n * dl


def T(b, Pi, a, pj):
    """sine coefficients of P_i g_i f_j' - p_j g_i' f_j for g_i = sum b_l sin(l theta), f_j = sum a_m sin(m theta)"""
    lb = np.arange(len(b), dtype=DT) * b
    ma = np.arange(len(a), dtype=DT) * a
    s = 0.5 * (Pi * np.convolve(b, ma) - pj * np.convolve(lb, a))        # index l+m
    d = -0.5 * (pj * np.convolve(a, lb[::-1]) + Pi * np.convolve(ma, b[::-1]))   # index (m-l) + len(b)-1
    out = np.zeros(max(len(s), len(a)), dtype=DT)
    out[:len(s)] += s
    z = len(b) - 1
    out[:len(d) - z] += d[z:]                 # m - l >= 0
    neg = d[:z][::-1]                          # m - l = -1, -2, ..., -z
    out[1:1 + len(neg)] -= neg
    out[0] = 0
    return out


def pois(f, n, drop=None):
    L = len(f)
    out = np.zeros(L + 1, dtype=DT)
    Pn = P_(n)
    l = np.arange(L, dtype=DT)
    nz = f != 0
    with np.errstate(divide='ignore', invalid='ignore'):
        up = np.where(nz, -f / (2 * (l + 1 + Pn)), 0)
        dn = np.where(nz, f / (2 * (l - 1 - Pn)), 0)
    if drop is not None:
        up[drop - 1] = 0
        if drop + 1 < L:
            dn[drop + 1] = 0
    up[0] = 0
    dn[0] = 0
    dn[1] = 0
    out[1:L + 1] += up
    out[0:L - 1] += dn[1:]
    out[0] = 0
    assert np.all(np.isfinite(out)), n
    return out


def resonant(n):
    return n % Q == 0


def order(F, G, n):
    acc = np.zeros(1, dtype=DT)
    for i in range(1, n):
        t = T(G[i], P_(i), F[n - i], p_(n - i))
        if len(t) > len(acc):
            t[:len(acc)] += acc
            acc = t
        else:
            acc[:len(t)] += t
    return acc / ((n - 1) * cm1)


def stream(F, n, Hval):
    if resonant(n):
        k = n // Q
        g = pois(F[n], n, drop=2 * H * k - 2)
        g[2 * H * k - 2] = Hval
        return g
    return pois(F[n], n)


def l1(x):
    return float(np.sum(np.abs(x)))


t0 = time.time()
m1 = max(F1)
f1 = np.zeros(m1 + 1, dtype=DT)
for m, v in F1.items():
    f1[m] = DT(v) * DT(EPS)
F, G = {1: f1}, {}
G[1] = stream(F, 1, 0)
print('# Q=%d h=%d delta=%d/%d f_1=%s N=%d eps=%s dtype=%s' % (Q, H, 2 * H, Q, prof, N, sys.argv[5], DT.__name__), flush=True)


def report(n, f, g):
    sc = n * LOGEPS
    print('n %d %.10f %.10f' % (n, np.log10(l1(f)) - sc, np.log10(l1(g)) - sc if g is not None else float('nan')), flush=True)


report(1, F[1], G[1])
n = 1
while n < Q:
    n += 1
    F[n] = order(F, G, n)
    if n < Q:
        G[n] = stream(F, n, 0)
        report(n, F[n], G[n])
nrm = l1(F[Q])
print('# first obstruction O_%d (unit amplitude) = %.6e, relative to ||f_Q|| %.3e' % (Q, float(F[Q][2 * H - 3]) / EPS ** Q,
      float(F[Q][2 * H - 3]) / nrm), flush=True)
k = 1
while (k + 1) * Q <= N:
    n0 = k * Q
    mode = 2 * H * (k + 1) - 3
    htrial = DT(max(l1(F[n0]), 1e-300))
    runs = []
    for Hv in (DT(0), htrial):
        Fc, Gc = dict(F), dict(G)
        Gc[n0] = stream(Fc, n0, Hv)
        for n in range(n0 + 1, n0 + Q + 1):
            Fc[n] = order(Fc, Gc, n)
            if n < n0 + Q:
                Gc[n] = stream(Fc, n, 0)
        runs.append((Fc, Gc))
    (F0, G0), (Fh, Gh) = runs
    R0 = F0[n0 + Q][mode]
    sig = (Fh[n0 + Q][mode] - R0) / htrial
    Hk = -R0 / sig
    G[n0] = stream(F, n0, Hk)
    report(n0, F[n0], G[n0])
    w = Hk / htrial
    for n in range(n0 + 1, n0 + Q + 1):
        a, b = F0[n], Fh[n]
        L = max(len(a), len(b))
        a = np.pad(a, (0, L - len(a)))
        b = np.pad(b, (0, L - len(b)))
        F[n] = a + w * (b - a)
        if n < n0 + Q:
            a, b = G0[n], Gh[n]
            L = max(len(a), len(b))
            a = np.pad(a, (0, L - len(a)))
            b = np.pad(b, (0, L - len(b)))
            G[n] = a + w * (b - a)
            report(n, F[n], G[n])
    resid = float(F[n0 + Q][mode]) / l1(F[n0 + Q])
    lr = np.log10(abs(float(R0))) - (k + 1) * Q * LOGEPS if R0 != 0 else float('-inf')
    lh = np.log10(abs(float(Hk))) - n0 * LOGEPS if Hk != 0 else float('-inf')
    print('k %d R %+d %.12f sigma %.12e H %+d %.12f relres %.2e t %.1f' % (k, np.sign(float(R0)), lr, float(sig) / EPS ** Q,
          np.sign(float(Hk)), lh, resid, time.time() - t0), flush=True)
    F[n0 + Q][mode] = 0
    k += 1
print('# done, last density order %d, time %.1fs' % (k * Q, time.time() - t0))
