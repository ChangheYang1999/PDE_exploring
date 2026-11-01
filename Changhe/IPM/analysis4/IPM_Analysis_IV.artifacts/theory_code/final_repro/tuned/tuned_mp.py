"""High-precision check (mpmath, coefficient space) of the tuned log-free series at delta=2/3, f_1 = sin + b sin3.

Each H_n (n = 3k) is computed directly as -R_n/sigma_k, with R_n the obstruction-mode coefficient of f_{n+3} computed
with H_n = 0 and sigma_k the exact response coefficient (sigma_sym.py); this checks the float run, which used two
evaluations per resonance instead.
"""
import sys, json
import mpmath as mp
mp.mp.dps = int(sys.argv[2]) if len(sys.argv) > 2 else 40
N = int(sys.argv[1]) if len(sys.argv) > 1 else 45
root = int(sys.argv[3]) if len(sys.argv) > 3 else 0
coef = [176703765525000, -222533688701250, 96180432855375, -20675598499400, 2783057141280, -243275209320, 10532171936]
O6 = lambda x: mp.polyval(coef, x)
bstar = mp.findroot(O6, [mp.mpf('0.2806'), mp.mpf('0.6463')][root])
dl = mp.mpf(2) / 3
p = lambda n: 1 - n * dl
P = lambda n: 2 - n * dl
lam = lambda n: 2 * (n - 1)
B = 4
def T(g, Pi, f, pj, out):
    # g: list stream sine coeffs by mode, f: density sine coeffs by mode
    for l, bb in enumerate(g):
        if bb == 0:
            continue
        for m, a in enumerate(f):
            if a == 0:
                continue
            ba = bb * a / 2
            s = l + m
            out[s] += (Pi * m - pj * l) * ba
            d = m - l
            v = (-pj * l - Pi * m) * ba
            if d > 0:
                out[d] += v
            elif d < 0:
                out[-d] -= v
def pois(f, n, Hval=None):
    Pn = P(n)
    g = [mp.mpf(0)] * (len(f) + 1)
    rq = None
    x = n * 2 - 6  # 3*(n*delta - 2) = 2n - 6
    if n % 3 == 0 and n >= 6:
        rq = (2 * n) // 3 - 2
    for M, a in enumerate(f):
        if a == 0:
            continue
        if M + 1 != rq:
            g[M + 1] += -a / (2 * (M + 1 + Pn))
        if M > 1 and M - 1 != rq:
            g[M - 1] += a / (2 * (M - 1 - Pn))
    if rq is not None:
        g[rq] = Hval if Hval is not None else mp.mpf(0)
    return g
F = {1: [mp.mpf(0)] * (B)}
F[1][1] = mp.mpf(1); F[1][3] = bstar
G = {1: pois(F[1], 1)}
def order(n, G, F):
    out = [mp.mpf(0)] * (B * n + 1)
    for i in range(1, n):
        T(G[i], P(i), F[n - i], p(n - i), out)
    return [v / lam(n) for v in out]
import sympy as sp
sys.path.insert(0, '.')
import sigma_sym as ss
kk = ss.kk
Fs, Gs = ss.low_orders(3)
sig = {}
def sigma(k):
    if k not in sig:
        s, _ = ss.sigma(k, Fs, Gs)
        sig[k] = mp.mpf(sp.N(s.subs(ss.b, sp.Float(mp.nstr(bstar, mp.mp.dps + 5), mp.mp.dps + 5)), mp.mp.dps))
    return sig[k]
res = []
n = 2
while n <= N:
    F[n] = order(n, G, F)
    if n % 3 == 0 and n >= 6:
        k = n // 3
        rq = 2 * k - 2
        obs = F[n][rq - 1]
        # trial orders n+1..n+3 with H_n = 0
        Gt = dict(G); Ft = dict(F)
        Gt[n] = pois(F[n], n, mp.mpf(0))
        for m in range(n + 1, n + 4):
            Ft[m] = order(m, Gt, Ft)
            if m < n + 3:
                Gt[m] = pois(Ft[m], m)
        R = Ft[n + 3][rq + 1]
        H = -R / sigma(k)
        G[n] = pois(F[n], n, H)
        res.append(dict(n=n, obs=mp.nstr(obs, 5), H=mp.nstr(H, 25), sigma=mp.nstr(sigma(k), 15),
                        l1=mp.nstr(sum(abs(v) for v in F[n]), 8)))
        print(res[-1], flush=True)
    else:
        G[n] = pois(F[n], n)
    n += 1
json.dump(dict(b=mp.nstr(bstar, 30), dps=mp.mp.dps, rows=res), open('tuned_mp_root%d_N%d.json' % (root, N), 'w'), indent=1)
