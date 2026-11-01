"""Top-mode radius R_H (Proposition 8.2, Section 14.22) at delta = 2/3, 2/5, 1/2, 1/3, 4/9 for B = 4 (f_1 = sin + b sin 3),
two ways: the beta-integral formula R_H = 4d [a B(a,b)]^(1/a) and the ratio h_n/h_(n+1) of the scalar top recursion
  (n-1) d h_n = (1/4) sum_{i+j=n} [2Bj/(eta i+2) - 1] h_i h_j,  h_1 = 1
(corrected by the known n^(-1-nu) law).  Then the necessary condition r > (|b_i| / R_H)^(1/delta) of Section 14.22(f)
for the explicit roots of Corollaries T.3, T_5, T_4, T_6 and T_{9,2}, and a check of h_2, h_3 against the actual top
coefficients of f_2, f_3 at delta = 4/9 from the direct Fourier recurrence.
"""
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 40
B = 4
ROOTS = {
    (2, 3): [0.280661662731966, 0.646352289880934],
    (2, 5): [-0.48976, 0.04900, 0.12533, 0.21209, 0.31528, 0.55998],
    (1, 2): [-0.27964, 0.03994, 0.07715, 0.18776, 0.35150, 0.62679],
    (1, 3): [-0.60873, 0.08856, 0.14072, 0.19652, 0.27850, 0.51216],
    (4, 9): [0.0634372745, 0.1524299875, 0.2698308394, 0.4223764828, 1.8566753384],
}


def RH_beta(dl):
    d = 1 / (1 - dl) - 1
    eta = B - dl
    a, b = 2 / eta, 2 * (B - 1) / eta
    return 4 * d * (a * mp.beta(a, b)) ** (1 / a), b


def RH_rec(dl, N=4000):
    d = 1 / (1 - dl) - 1
    eta = B - dl
    h = [mp.mpf(0), mp.mpf(1)]
    for n in range(2, N + 1):
        s = mp.mpf(0)
        for i in range(1, n):
            j = n - i
            s += (2 * B * j / (eta * i + 2) - 1) * h[i] * h[j]
        h.append(s / (4 * (n - 1) * d))
    return h


for (p, q), roots in ROOTS.items():
    dl = mp.mpf(p) / q
    R, bb = RH_beta(dl)
    nu = 1 / bb
    h = RH_rec(dl, 1500)
    n = 1500
    # h_n ~ K R^-n n^(-1-nu): R ~ (h_(n-1)/h_n) * ((n-1)/n)^(1+nu)
    Rrec = h[n - 1] / h[n] * (mp.mpf(n - 1) / n) ** (1 + nu)
    print('delta = %d/%d: R_H = %s (beta), %s (recursion n=1500, corrected), 1/R_H = %s' %
          (p, q, mp.nstr(R, 12), mp.nstr(Rrec, 8), mp.nstr(1 / R, 8)))
    print('   |b_i|/R_H:', ', '.join(mp.nstr(abs(x) / R, 5) for x in roots))
    print('   necessary radius (|b_i|/R_H)^(1/delta):', ', '.join(mp.nstr((abs(x) / R) ** (1 / dl), 4) for x in roots))

# check h_2, h_3 against the top coefficients of the actual recurrence at delta = 4/9
dl = Fr(4, 9)
d = 1 / (1 - dl) - 1
eta = B - dl
h1, h2 = Fr(1), Fr(1, 4 * d) * (2 * B * 1 / (eta * 1 + 2) - 1)
h3 = Fr(1, 8 * d) * ((2 * B * 2 / (eta * 1 + 2) - 1) * h2 + (2 * B * 1 / (eta * 2 + 2) - 1) * h2)
print('h_2 =', h2, float(h2), '; h_3 =', h3, float(h3))

# direct Fourier recurrence (as in code/tuned/cand_sigma.py) at delta = 4/9, f_1 = sin + b sin 3: top coefficients
import json
dlm = mp.mpf(4) / 9
bq = mp.mpf('0.7')


def addm(dct, m, v):
    if m == 0:
        return
    if m < 0:
        m, v = -m, -v
    dct[m] = dct.get(m, 0) + v


def T(g, Pi, f, pj):
    out = {}
    for mu, x in g.items():
        for nu_, y in f.items():
            xy = x * y / 2
            addm(out, mu + nu_, (-pj * mu + Pi * nu_) * xy)
            addm(out, nu_ - mu, (-pj * mu - Pi * nu_) * xy)
    return out


def poisson(f, n):
    pn, Pn = 1 - n * dlm, 2 - n * dlm
    g = {}
    for j in set([m + 1 for m in f] + [m - 1 for m in f if m > 1]):
        g[j] = ((pn - (j - 1)) / 2 * f.get(j - 1, 0) + (pn + (j + 1)) / 2 * f.get(j + 1, 0)) / (j * j - Pn * Pn)
    return g


F, G = {1: {1: mp.mpf(1), 3: bq}}, {}
G[1] = poisson(F[1], 1)
for n in range(2, 6):
    acc = {}
    for i in range(1, n):
        for m, v in T(G[i], 2 - i * dlm, F[n - i], 1 - (n - i) * dlm).items():
            acc[m] = acc.get(m, 0) + v
    F[n] = {m: v / (dlm * (n - 1) / (1 - dlm)) for m, v in acc.items()}
    G[n] = poisson(F[n], n)
hh = RH_rec(dlm, 5)
for n in range(2, 6):
    An = F[n].get(4 * n - 1, 0)
    print('n=%d: top coefficient %s, (-1)^(n-1) b^n h_n = %s' % (n, mp.nstr(An, 15), mp.nstr((-1) ** (n - 1) * bq ** n * hh[n], 15)))
