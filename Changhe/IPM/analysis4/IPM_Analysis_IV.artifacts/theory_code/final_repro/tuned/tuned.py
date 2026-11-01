"""Lead: log-free tuned series at rational delta.

Pure power series rho = sum r^{p_n} f_n(theta), psi = sum r^{P_n} g_n(theta) with recursion (5) and Poisson formula (4).
At a resonant order n (n*delta = q+2, q even >= 2) the obstruction is the coefficient of sin((q-1)theta) in f_n; it must
vanish, and the stream coefficient of sin(q theta) at order n is free (H_n). H_n is chosen to make the obstruction at
the next resonant order n + n_r vanish (the obstruction there is affine in H_n since n + n_r < 2n).
Float64 grid implementation (exploration only).
"""
import sys, json
import numpy as np
from fractions import Fraction

def run(a, bden, f1, N, Q=None, tune=True, verbose=False):
    dl = Fraction(a, bden)
    c = 1 / (1 - dl)
    lam = lambda n: float((n - 1) * (c - 1))
    p = lambda n: float(1 - n * dl)
    L = max(f1)
    B = L + 1
    if Q is None:
        Q = 1
        while Q < 4 * B * N + 8:
            Q *= 2
    H = Q // 2 + 1
    m = np.arange(H)
    th = 2 * np.pi * np.arange(Q) / Q
    def s2g(A):  # sine coeffs -> grid
        X = -1j * A * Q / 2
        return np.fft.irfft(X, Q)
    def c2g(A):
        X = A.astype(complex) * Q / 2
        return np.fft.irfft(X, Q)
    def g2s(x):
        X = np.fft.rfft(x)
        return -2 * X.imag / Q
    def res_order(n):
        x = n * dl - 2
        if x.denominator == 1 and x >= 2 and int(x) % 2 == 0:
            return int(x)
        return None
    F = {}
    G = {}
    A1 = np.zeros(H)
    for k, v in f1.items():
        A1[k] = v
    F[1] = A1
    Hfree = {}
    obstr = {}
    def poisson(n, A, Hn=0.0):
        pn = p(n)
        Gc = np.zeros(H)
        q = np.arange(2, H - 1, 2)
        j = q // 2
        num = (pn - 2 * j + 1) * A[2 * j - 1] + (pn + 2 * j + 1) * A[2 * j + 1]
        den = 2 * (4.0 * j * j - (pn + 1) ** 2)
        rq = res_order(n)
        with np.errstate(divide='ignore', invalid='ignore'):
            val = num / den
        if rq is not None:
            jj = rq // 2
            obstr[n] = A[rq - 1]
            val[jj - 1] = Hn
        Gc[q] = val
        return Gc
    # grids cache
    Fg, Fdg, Gg, Gdg = {}, {}, {}, {}
    def setF(n, A):
        F[n] = A; Fg[n] = s2g(A); Fdg[n] = c2g(m * A)
    def setG(n, Gc):
        G[n] = Gc; Gg[n] = s2g(Gc); Gdg[n] = c2g(m * Gc)
    setF(1, A1)
    setG(1, poisson(1, A1))
    nr = None
    def order(n):
        acc = np.zeros(Q)
        for i in range(1, n):
            j = n - i
            acc += -p(j) * Gdg[i] * Fg[j] + (p(i) + 1) * Gg[i] * Fdg[j]
        out = g2s(acc) / lam(n)
        out[B * n:] = 0.0  # exact support: modes <= B n - 1
        return out
    n = 2
    pending = []  # resonant orders whose H is not yet fixed
    stats = []
    while n <= N:
        A = order(n)
        setF(n, A)
        setG(n, poisson(n, A, 0.0))
        rq = res_order(n)
        if rq is not None and tune:
            # find previous resonant order n0 = n - n_r with a free constant still to fix
            prev = [k for k in pending if k < n]
            if prev:
                n0 = prev[-1]
                pending.remove(n0)
                # recompute orders n0+1..n with H_{n0} = 1 to get the affine response
                save = {k: (F[k].copy(), G[k].copy()) for k in range(n0, n + 1)}
                o0 = obstr[n]
                G1 = G[n0].copy(); G1[rq_of[n0]] = 1.0
                setG(n0, G1)
                for k in range(n0 + 1, n + 1):
                    Ak = order(k); setF(k, Ak); setG(k, poisson(k, Ak, 0.0))
                o1 = obstr[n]
                slope = o1 - o0
                Hval = -o0 / slope
                Hfree[n0] = dict(H=Hval, slope=slope, o0=o0)
                G1 = save[n0][1].copy(); G1[rq_of[n0]] = Hval
                setG(n0, G1)
                for k in range(n0 + 1, n + 1):
                    Ak = order(k); setF(k, Ak); setG(k, poisson(k, Ak, 0.0))
            pending.append(n)
        st = dict(n=n, l1=float(np.abs(F[n]).sum()), g1=float(np.abs(G[n]).sum()))
        if rq is not None:
            st['obstr'] = float(obstr[n]); st['q'] = rq
        stats.append(st)
        n += 1
    return F, G, Hfree, stats

rq_of = {}
if __name__ == '__main__':
    a, bd, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    beta = float(sys.argv[4]); M = int(sys.argv[5])
    dl = Fraction(a, bd)
    for n in range(1, 4 * N):
        x = n * dl - 2
        if x.denominator == 1 and x >= 2 and int(x) % 2 == 0:
            rq_of[n] = int(x)
    F, G, Hf, st = run(a, bd, {1: 1.0, M: beta}, N)
    for s in st:
        line = '%4d %.4e %.4e' % (s['n'], s['l1'], s['g1'])
        if 'obstr' in s:
            line += '  res q=%d obstr=%.3e' % (s['q'], s['obstr'])
        if s['n'] in Hf:
            line += '  H=%.4e slope=%.4e' % (Hf[s['n']]['H'], Hf[s['n']]['slope'])
        print(line)
