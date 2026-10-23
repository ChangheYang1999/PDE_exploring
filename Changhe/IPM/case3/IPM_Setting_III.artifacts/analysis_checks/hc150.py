# Independent hand-check arithmetic for checker result 150 (pure first trace, resonant numerator g_*).
# Density terms r^{s_k} P_k(th), P_k = {n: coeff of sin n th}; streams r^{s_k+1} H_k, H_k = {m: coeff of sin m th}.
from fractions import Fraction as F
import sys
def run(ell, kstar, mstar):
    p = 1/ell; d = 1-p
    s = lambda k: p - k*d
    P = {0: {1: F(1)}}; H = {}
    def dx(Pk, sk):  # d_x (r^s sin n th) = r^{s-1}[(s-n)/2 sin(n+1) + (s+n)/2 sin(n-1)]
        G = {}
        for n, c in Pk.items():
            for mm, w in ((n+1, (sk-n)/2), (n-1, (sk+n)/2)):
                if mm != 0: G[mm] = G.get(mm, 0) + c*w
        return G
    def stream(k):
        G = dx(P[k], s(k)); Hk = {}
        for m, g in G.items():
            den = m*m - (s(k)+1)**2
            assert den != 0
            Hk[m] = g/den
        return Hk
    for k in range(1, kstar+1):
        H[k-1] = stream(k-1)
        acc = {}
        for i in range(k):
            j = k-1-i
            si, sj = s(i), s(j)
            for m, h in H[i].items():
                for n, c in P[j].items():
                    for f, w in ((n+m, (-m*sj+(si+1)*n)/2), (n-m, (-m*sj-(si+1)*n)/2)):
                        if f == 0: continue
                        sg = 1
                        if f < 0: f, sg = -f, -1
                        acc[f] = acc.get(f, 0) + sg*h*c*w
        P[k] = {n: v/(ell*k*d) for n, v in acc.items() if v != 0}
    sk = s(kstar); assert sk == -mstar-1
    G = dx(P[kstar], sk)
    return G.get(mstar, 0), P[1]
for ell, ks, ms in ((F(3), 5, 2), (F(5, 2), 9, 4)):
    g, P1 = run(ell, ks, ms)
    print(ell, ks, ms, "g* =", g, float(g), "P1 =", P1)
