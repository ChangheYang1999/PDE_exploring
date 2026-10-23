# Growth of the formal xi-Taylor coefficients of 3.73(c) for the axis data v = c y - D arctan y (3.73(b)).
# Truncated Taylor series in t = y - y0, mpmath; recursion of 3.73(c) in its general form.
import sys
from mpmath import mp, mpf, atan, quad, exp, log, fabs
mp.dps = int(sys.argv[4]) if len(sys.argv) > 4 else 60
c = mpf(sys.argv[1]) if len(sys.argv) > 1 else mpf(2)
y0 = mpf(sys.argv[2]) if len(sys.argv) > 2 else mpf(1)
NMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 14
D = c - 1
N = 3 * NMAX + 12
def mul(a, b):
    r = [mpf(0)] * N
    for i, ai in enumerate(a):
        if ai == 0: continue
        for j in range(N - i):
            r[i + j] += ai * b[j]
    return r
def inv(a):
    r = [mpf(0)] * N; r[0] = 1 / a[0]
    for k in range(1, N):
        s = sum(a[j] * r[k - j] for j in range(1, k + 1))
        r[k] = -s / a[0]
    return r
def der(a): return [a[k + 1] * (k + 1) for k in range(N - 1)] + [mpf(0)]
def integ(a, c0=0): return [mpf(c0)] + [a[k] / (k + 1) for k in range(N - 1)]
def expo(a):  # exp of series with a[0] given
    r = [mpf(0)] * N; r[0] = exp(a[0]); da = der(a)
    for k in range(1, N):  # r' = a' r
        r[k] = sum(da[j] * r[k - 1 - j] for j in range(k)) / k
    return r
def add(*s): return [sum(x) for x in zip(*s)]
def sc(a, s): return [s * x for x in a]
one = [mpf(1)] + [mpf(0)] * (N - 1)
ys = [y0, mpf(1)] + [mpf(0)] * (N - 2)
q = add(sc(one, 1 + y0**2), [mpf(0), 2 * y0, mpf(1)] + [mpf(0)] * (N - 3))
at = integ(inv(q), atan(y0))
v = add(sc(ys, c), sc(at, -D))
lnG0 = log(y0) + quad(lambda t: 1 / (c * t - D * atan(t)) - 1 / t, [0, y0])
G = expo(integ(inv(v), lnG0))
Gp = mul(G, inv(v)); iGp = inv(Gp)
g = {0: G}; h = {1: add(sc(one, c), sc(der(v), -1))}; b = {0: v}
out = []
for n in range(1, NMAX + 1):
    g[2 * n] = sc(der(h[2 * n - 1]), mpf(1) / (2 * n))
    An = [mpf(0)] * N
    for l in range(1, n + 1):
        i = n - l
        coef = h[2 * i + 1] if i > 0 else add(sc(one, c), h[1])
        An = add(An, sc(mul(coef, g[2 * l]), 2 * l))
    S = [mpf(0)] * N
    for j in range(0, n):
        S = add(S, mul(b[2 * j], der(g[2 * (n - j)])))
    b[2 * n] = mul(add(g[2 * n], sc(An, -1), sc(S, -1)), iGp)
    h[2 * n + 1] = sc(der(b[2 * n]), mpf(-1) / (2 * n + 1))
    out.append((n, g[2 * n][0]))
# checks against 3.73(c) closed forms
vp, vpp, vppp = der(v), der(der(v)), der(der(der(v)))
b2 = mul(add(mul(add(sc(one, 4 * c - 1), sc(vp, -2)), vpp), mul(v, vppp)), sc(iGp, mpf(1) / 2))
print('check g2 = -v\'\'/2:', mp.nstr(g[2][0] + vpp[0] / 2, 5), ' check b2:', mp.nstr(b[2][0] - b2[0], 5))
print('c =', c, 'y0 =', y0, 'dps =', mp.dps)
prev = None
for n, val in out:
    lv = log(fabs(val)) if val != 0 else None
    r = (fabs(val) / fabs(prev)) if prev not in (None, 0) else None
    print(n, mp.nstr(val, 12), ' |g_2n|^(1/2n) =', mp.nstr(fabs(val) ** (mpf(1) / (2 * n)), 6),
          ' ratio/n =', mp.nstr(r / n, 6) if r is not None else '-')
    prev = val
