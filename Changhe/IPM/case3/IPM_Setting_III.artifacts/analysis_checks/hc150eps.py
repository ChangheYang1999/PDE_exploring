# Check of the external audit's high-mode claim: trace sin th + eps sin N th, g_* to order eps^2.
# Same recurrence as hc150.py, coefficients are truncated polynomials in eps (lists of length 3).
from fractions import Fraction as F
import sys
def mul(a,b): return [a[0]*b[0], a[0]*b[1]+a[1]*b[0], a[0]*b[2]+a[1]*b[1]+a[2]*b[0]]
def add(a,b): return [x+y for x,y in zip(a,b)]
def sc(a,w): return [x*w for x in a]
Z=lambda: [F(0)]*3
def run(ell, kstar, mstar, N):
    p = 1/ell; d = 1-p
    s = lambda k: p - k*d
    P = {0: {1: [F(1),F(0),F(0)], N: [F(0),F(1),F(0)]}}; H = {}
    def dx(Pk, sk):
        G = {}
        for n, c in Pk.items():
            for mm, w in ((n+1, (sk-n)/2), (n-1, (sk+n)/2)):
                if mm != 0: G[mm] = add(G.get(mm, Z()), sc(c,w))
        return G
    def stream(k):
        G = dx(P[k], s(k)); Hk = {}
        for m, g in G.items():
            den = m*m - (s(k)+1)**2; assert den != 0
            Hk[m] = sc(g, 1/den)
        return Hk
    for k in range(1, kstar+1):
        H[k-1] = stream(k-1); acc = {}
        for i in range(k):
            j = k-1-i; si, sj = s(i), s(j)
            for m, h in H[i].items():
                for n, c in P[j].items():
                    hc = mul(h,c)
                    if not any(hc): continue
                    for f, w in ((n+m, (-m*sj+(si+1)*n)/2), (n-m, (-m*sj-(si+1)*n)/2)):
                        if f == 0: continue
                        sg = 1
                        if f < 0: f, sg = -f, -1
                        acc[f] = add(acc.get(f, Z()), sc(hc, sg*w))
        P[k] = {n: sc(v, 1/(ell*k*d)) for n, v in acc.items() if any(v)}
    sk = s(kstar); assert sk == -mstar-1
    return dx(P[kstar], sk).get(mstar, Z())
q=1000003
N=int(sys.argv[1]) if len(sys.argv)>1 else 101
for ell, ks, ms in ((F(3), 5, 2), (F(5, 2), 9, 4)):
    g = run(ell, ks, ms, N)
    r = [ (x.numerator*pow(x.denominator,-1,q))%q if x.denominator%q else None for x in g]
    print(ell, "N=",N, "g0 float", float(g[0]), "g1 =", g[1], "g2 float", float(g[2]), "g2 mod q", r[2])
