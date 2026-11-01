"""Numerical check of the fixed-order zero-delta limit for f_1 = sin(3 theta) (review): pure recursion
lambda_n f_n = sum T(g_i, f_j), Fourier Poisson inverse, at small delta in mpmath; compares delta^(2n-2) [sin] f_n with
[x^(n-1)] of -x^2/sqrt(1+x^2) - x(2+x^2)/(1+x^2), and delta^(2n-2) [sin 3] f_n with [x^(n-1)] (1+x^2)^(-3/2)."""
import mpmath as mp
mp.mp.dps = 80
NMAX = 9


def run(dl):
    p = lambda n: 1 - n * dl
    P = lambda n: 2 - n * dl
    lam = lambda n: dl * (n - 1) / (1 - dl)

    def T(g, Pi, f, pj):
        out = {}
        for mu, x in g.items():
            for nu, y in f.items():
                for mm, v in ((mu + nu, (-pj * mu + Pi * nu) * x * y / 2), (nu - mu, (-pj * mu - Pi * nu) * x * y / 2)):
                    if mm == 0:
                        continue
                    if mm < 0:
                        mm, v = -mm, -v
                    out[mm] = out.get(mm, 0) + v
        return out

    def poisson(f, n):
        g = {}
        for j in {m + 1 for m in f} | {m - 1 for m in f if m > 1}:
            g[j] = -f.get(j - 1, 0) / (2 * (j + P(n))) - f.get(j + 1, 0) / (2 * (P(n) - j))
        return g
    F, G = {1: {3: mp.mpf(1)}}, {}
    G[1] = poisson(F[1], 1)
    for n in range(2, NMAX + 1):
        acc = {}
        for i in range(1, n):
            for m, v in T(G[i], P(i), F[n - i], p(n - i)).items():
                acc[m] = acc.get(m, 0) + v
        F[n] = {m: v / lam(n) for m, v in acc.items()}
        G[n] = poisson(F[n], n)
    return F


x = mp.mpf(0)
c1 = mp.taylor(lambda x: -x**2 / mp.sqrt(1 + x**2) - x * (2 + x**2) / (1 + x**2), 0, NMAX)
c3 = mp.taylor(lambda x: (1 + x**2) ** mp.mpf(-1.5), 0, NMAX)
for dl in (mp.mpf('1e-10'), mp.mpf('1e-12')):
    F = run(dl)
    print('delta =', mp.nstr(dl, 3))
    for n in range(1, NMAX + 1):
        s1 = F[n].get(1, 0) * dl ** (2 * n - 2)
        s3 = F[n].get(3, 0) * dl ** (2 * n - 2)
        print('  n=%d: delta^(2n-2)[sin]f_n = %s (limit %s); [sin3]: %s (limit %s)' % (
            n, mp.nstr(s1, 10), mp.nstr(c1[n - 1], 10), mp.nstr(s3, 10), mp.nstr(c3[n - 1], 10)))
