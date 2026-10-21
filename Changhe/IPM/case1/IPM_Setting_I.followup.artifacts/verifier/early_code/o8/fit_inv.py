# Own check of the fred23 02-radius inventory for the fitted reference (fred22 05 fitted_reference.json):
# origin algebra norms (16) at r = 1/2, sigma = 1 (abs t-series sums with 400 terms, and the sampled true norm),
# tail suprema on [1/2, 1] by dense sampling of exact polynomial/rational forms (mpmath, 40 digits), and the
# derived bounds g*, g_min, H_max, a_*, W_0.  Compared with radius_certificate.json inventory_exact.
import json
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 40
d = json.load(open('fred23/01-obstruction/data/fitted_reference.json'))
A0 = mp.mpf(d['A0_exact']); q = [mp.mpf(s) for s in d['q_power_coefficients_exact_decimal']]
inv = {k: Fr(v) for k, v in json.load(open('fred23/02-radius/verification/radius_certificate.json'))['inventory_exact'].items()}
NT = 400
r = mp.mpf(1)/2; R = r*r

def smul(a, b, n=NT):
    c = [mp.mpf(0)]*n
    for i, x in enumerate(a[:n]):
        if x == 0: continue
        for j, y in enumerate(b[:n - i]):
            c[i + j] += x*y
    return c
def sinv(a, n=NT):
    b = [mp.mpf(0)]*n; b[0] = 1/a[0]
    for k in range(1, n):
        b[k] = -sum(a[j]*b[k - j] for j in range(1, min(k, len(a) - 1) + 1))/a[0]
    return b
# z0 = (1-t)/(1+t) - t (1-t)^2 q(t)/A0 as a t-series
z = [mp.mpf(1)] + [2*(-1)**k for k in range(1, NT)]
p = smul([0, 1, -2, 1], q + [0]*NT)
z = [z[k] - p[k]/A0 for k in range(NT)]
zi = sinv(z)
D0 = [2*k*z[k] for k in range(NT)]
J0 = [z[k + 1]*(2*k + 3)*(2*k + 2) for k in range(NT - 1)] + [0]
E0 = [0] + [zi[k]/(2*k) for k in range(1, NT)]

def anorm(f):
    absum = abs(f[0]) + abs(f[1])*R + abs(f[2])*R**2 + sum(abs(f[k])*R**k for k in range(3, NT))
    # sampled true norm: sup over u in (0, r] of |R_F(u)| / (u/r)^5
    best = mp.mpf(0)
    for i in range(1, 401):
        u = r*i/400; t = u*u
        rf = sum(f[k]*t**k for k in range(3, NT))
        best = max(best, abs(rf)/(u/r)**5)
    return absum, abs(f[0]) + abs(f[1])*R + abs(f[2])*R**2 + best, abs(f[NT - 1])*R**(NT - 1)

out = {}
for name, f in [('Z', z), ('n', zi), ('D', D0), ('J', J0), ('Eo', E0)]:
    a, s, last = anorm(f)
    out[name] = (a, s)
    print('%-3s abs-series %s  sampled %s  last term %s  referee %s  ok %s' % (name, mp.nstr(a, 10), mp.nstr(s, 10), mp.nstr(last, 3),
          float(inv[name]), a <= mp.mpf(inv[name].numerator)/inv[name].denominator), flush=True)

# tail: exact polynomial forms.  P = (1+u^2) w0 (polynomial), w0 = P/(1+u^2)
def pmul(a, b):
    c = [mp.mpf(0)]*(len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x*y
    return c
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def pder(a): return [k*a[k] for k in range(1, len(a))]
def pev(a, x): return mp.polyval(a[::-1], x)
qu = []
for k, c in enumerate(q):
    qu += [c, 0]
P = padd(pmul([0, -A0], [1, 0, -1]), pmul(pmul([0, 0, 0, 1], pmul([1, 0, -2, 0, 1], [1, 0, 1])), qu))
def w0(u): return pev(P, u)/(1 + u*u)
def w1(u): return mp.diff(w0, u)
# P/(u-1)
def sdiv(c):  # divide polynomial c (low->high) by (u - 1), assert remainder 0
    hi = c[::-1]; outc = [hi[0]]
    for x in hi[1:]:
        outc.append(x + outc[-1])
    rem = outc.pop()
    return outc[::-1], rem
Pd, rem = sdiv(P)
print('P(1) remainder', mp.nstr(rem, 3))
a0f = lambda u: pev(Pd, u)/(1 + u*u)      # -w0/(1-u) = P/((u-1)(1+u^2))
# N = (w0' - A0)(1+u^2)^2 = P'(1+u^2) - 2u P - A0 (1+u^2)^2
N = padd(padd(pmul(pder(P), [1, 0, 1]), [-x for x in pmul([0, 2], P)]), [-A0*x for x in [1, 0, 2, 0, 1]])
Nd, rem2 = sdiv(N)
print('N(1) remainder', mp.nstr(rem2, 3))
k0f = lambda u: pev(Nd, u)/((1 + u*u)*pev(Pd, u))   # k0 = N/((1+u^2) P)
w2f = lambda u: mp.diff(w0, u, 2)
grid = [r + (1 - r)*mp.mpf(i)/4000 for i in range(4001)]
def tail(fn, dfn, name, key_S=None, key_H=None):
    vals = [fn(u) for u in grid]
    S = max(abs(v) for v in vals)
    F1 = vals[-1]
    H = max(abs(vals[i] - F1)/(1 - grid[i])**mp.mpf('0.9') for i in range(len(grid) - 1))
    dS = max(abs(dfn(u)) for u in grid[::4])
    s = '%-6s S %-14s H(sampled) %-14s sup|F\'| %-14s' % (name, mp.nstr(S, 8), mp.nstr(H, 8), mp.nstr(dS, 8))
    if key_S: s += ' referee S %s ok %s' % (float(inv[key_S]), S <= float(inv[key_S]))
    if key_H: s += ' referee H %s ok %s' % (float(inv[key_H]), max(H, dS) <= float(inv[key_H]))
    print(s, flush=True)
    return S, H, dS
tail(a0f, lambda u: mp.diff(a0f, u), 'a0', None, 'Ha')
tail(k0f, lambda u: mp.diff(k0f, u), 'k0', 'K0', 'Hk')
tail(w2f, lambda u: mp.diff(w0, u, 3), 'w0pp', 'w2S', 'w2H')
astar = min(a0f(u) for u in grid)
print('a_* sampled min %s at u = %s, referee %s, A0*3/5 = %s' % (mp.nstr(astar, 12), mp.nstr(grid[[a0f(u) for u in grid].index(astar)], 4),
      float(inv['astar']), mp.nstr(A0*3/5, 12)))
# H(t) = A0 - t(1-t^2) q(t) on [0,1]; T(t) = 1/2 int_0^t (1+s)^2 q/H
Hf = lambda t: A0 - t*(1 - t*t)*mp.polyval(q[::-1], t)
Hs = [Hf(mp.mpf(i)/2000) for i in range(2001)]
print('H on [0,1]: min %s max %s (referee H_min A0, H_max 11)' % (mp.nstr(min(Hs), 12), mp.nstr(max(Hs), 10)))
T1 = mp.quad(lambda s: (1 + s)**2*mp.polyval(q[::-1], s)/Hf(s), [0, 0.5, 1])/2
gs = mp.exp(T1)/2
print('T(1) = %s, g* = e^T(1)/2 = %s (referee g* lower 2/5)' % (mp.nstr(T1, 20), mp.nstr(gs, 20)))
w2s = w2f(mp.mpf(1)); print('w0\'\'(1) = %s, referee %s' % (mp.nstr(w2s, 16), mp.nstr(mp.mpf(inv['w2star'].numerator)/inv['w2star'].denominator, 16)))
# g0 on [r,1] by (41): g0 = u^2 H(u^2) e^T(u^2)/(A0 (1+u^2))
def g0(u):
    t = u*u
    return t*Hf(t)*mp.exp(mp.quad(lambda s: (1 + s)**2*mp.polyval(q[::-1], s)/Hf(s), [0, t])/2)/(A0*(1 + t))
gg = [g0(u) for u in grid[::40]]
print('g0 on [r,1]: min %s (referee g_min 4/25), max %s' % (mp.nstr(min(gg), 10), mp.nstr(max(gg), 10)))
bm, bp = 2/(A0 + mp.mpf('0.06') + 1), 2/(A0 - mp.mpf('0.06') - 1)
W0 = max(max((a0f(u)/A0)**(b - 2)*g0(u)**(1 - b) for u in grid[::40]) for b in (bm, bp))
print('W0 sampled %s (referee 25/9 = %s)' % (mp.nstr(W0, 10), mp.nstr(mp.mpf(25)/9, 10)))
