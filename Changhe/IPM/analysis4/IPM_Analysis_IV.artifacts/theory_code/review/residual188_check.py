"""Independent check of verifier topic 188 (finite stationary residual bound).
Exact prefix at delta=2/7 (non-resonant below n=14), f_1 = sin + (1/3) sin 3, J=6.
Evaluates R_J = c r d_r rho_J + u.grad rho_J - rho_J with u = (-psi_y, psi_x) directly in Cartesian
form at sample points, compares with the order J+1..2J ordered-pair formula, and with the bound T_(a,b)."""
import sys, math
from fractions import Fraction as Fr
sys.path.insert(0, '../oddnum')
from kappa_odd import run

a, p, J, B = 2, 7, 6, 4
delta = Fr(a, p); c = 1 / (1 - delta)
f, g = run(a, p, {1: Fr(1), 3: Fr(1, 3)}, J + 1)   # g[n] for n <= J
pn = lambda n: 1 - n * delta
Pn = lambda n: 2 - n * delta
bw = max(max(abs(k) for k in f[n]) / n for n in range(1, J + 1))
bwg = max(max(abs(k) for k in g[n]) / n for n in range(1, J + 1))
assert bw <= B and bwg <= B, (bw, bwg)

def ev(series, r, th, pw, dr=0, dth=0):
    """sum_n r^pw(n) * sum_k coef * sin(k th); returns (r d/dr)^dr d_th^dth of it."""
    s = 0.0
    for n, modes in series.items():
        e = float(pw(n))
        for k, v in modes.items():
            ang = [math.sin, math.cos, lambda x: -math.sin(x), lambda x: -math.cos(x)][dth % 4](k * th) * k ** dth
            s += float(v) * e ** dr * r ** e * ang
    return s

F = {n: f[n] for n in range(1, J + 1)}; G = {n: g[n] for n in range(1, J + 1)}
def residual_direct(r, th):
    rho_r = ev(F, r, th, pn, 1) / r; rho_t = ev(F, r, th, pn, 0, 1)
    psi_r = ev(G, r, th, Pn, 1) / r; psi_t = ev(G, r, th, Pn, 0, 1)
    co, si = math.cos(th), math.sin(th)
    rx, ry = co * rho_r - si / r * rho_t, si * rho_r + co / r * rho_t
    px, py = co * psi_r - si / r * psi_t, si * psi_r + co / r * psi_t
    return c * r * rho_r + (-py) * rx + px * ry - ev(F, r, th, pn)

def residual_formula(r, th):
    s = 0.0
    for n in range(J + 1, 2 * J + 1):
        for i in range(n - J, J + 1):
            j = n - i
            Gi, Gip = ev({i: g[i]}, 1, th, Pn), ev({i: g[i]}, 1, th, Pn, 0, 1)
            Fj, Fjp = ev({j: f[j]}, 1, th, pn), ev({j: f[j]}, 1, th, pn, 0, 1)
            s += r ** float(pn(n)) * (float(Pi := Pn(i)) * Gi * Fjp - float(pn(j)) * Gip * Fj)
    return s

def poisson_res(r, th, n, h=1e-4):
    # -Lap(r^P g_n) - d_x(r^p f_n) via polar formulas (central differences in r)
    def psi(rr, tt): return ev({n: g[n]}, rr, tt, Pn)
    lap = (psi(r + h, th) - 2 * psi(r, th) + psi(r - h, th)) / h ** 2 + (psi(r + h, th) - psi(r - h, th)) / (2 * h) / r \
        + ev({n: g[n]}, r, th, Pn, 0, 2) / r ** 2
    rho_r = ev({n: f[n]}, r, th, pn, 1) / r; rho_t = ev({n: f[n]}, r, th, pn, 0, 1)
    dx = math.cos(th) * rho_r - math.sin(th) / r * rho_t
    return -lap - dx, abs(dx)

alpha = {n: sum(abs(float(v)) for v in f[n].values()) for n in f}
beta = {n: sum(abs(float(v)) for v in g[n].values()) for n in g}
def T(z, A=0, Bb=0):
    tot = 0.0
    for n in range(J + 1, 2 * J + 1):
        Cn = sum((abs(float(Pn(i))) * B * (n - i) + abs(float(pn(n - i))) * B * i) * beta[i] * alpha[n - i]
                 for i in range(n - J, J + 1))
        tot += z ** (n - 1) * abs(float(pn(n))) ** A * (B * n) ** Bb * Cn
    return tot

worst = 0.0; ok = True
for r in [1.5, 3.0, 10.0, 100.0]:
    gam = float(1 - delta); z = r ** (-float(delta))
    for th in [0.1, 0.7, 1.9, 2.6, 4.0, 5.5]:
        d, fo = residual_direct(r, th), residual_formula(r, th)
        scale = max(1.0, abs(ev(F, r, th, pn)))
        worst = max(worst, abs(d - fo) / scale)
        if r ** (-gam) * abs(d) > T(z) * (1 + 1e-12): ok = False
print('max |direct - formula| / scale =', worst)
print('bound T_(0,0) holds at all samples:', ok)
for n in range(1, J + 1):
    e, s = poisson_res(2.0, 0.9, n)
    print('Poisson n=%d residual %.2e (scale %.2e)' % (n, e, s))
# derivative bound sample: (r d_r)^1 d_th^1 of the formula residual vs T_(1,1)
r, th = 3.0, 0.7; hh = 1e-5
def RF(rr, tt): return residual_formula(rr, tt)
mixed = (rr := r) * ((RF(r + hh, th + hh) - RF(r + hh, th - hh)) - (RF(r - hh, th + hh) - RF(r - hh, th - hh))) / (4 * hh * hh)
print('weighted (r d_r)(d_th) residual %.3e <= T_(1,1) %.3e :' % (r ** (-float(1 - delta)) * abs(mixed), T(r ** (-float(delta)), 1, 1)),
      r ** (-float(1 - delta)) * abs(mixed) <= T(r ** (-float(delta)), 1, 1))
