"""Independent checks for c1-t4 T4-314 (far-out tail repair), c1-t1 review R1-035.

Usage (from artifacts/checks): python3 -B check_T4314.py [data/T4295_007_tail_repair.json]
(a copy of c1-t4 research/far_out_tail_repair/data/007_tail_repair.json, identical to the T4-295 file, sha256
bad9b06a...). Reads the exact A1_m of 007, writes nothing outside stdout.
(1) exact exponent arithmetic; (2) symbolic Fourier check that v = (-d_y psi, d_x psi), psi = d_x d_y chi,
h = -d_y Lap chi is the IPM multiplier velocity u = -grad p - rho e_2 of h; (3) mpmath quadrature (not interval
certified) of C_(0,0) = ||h_1||_2 for A = sum A1_m cos(2 m theta) of 007 and a direct quadrature of ||h_L||_2 for
L = 2, 4 against L^(q+1) C_(0,0); (4) the L needed for ||h_L||_2 below 1e-3 and 1e-6.
"""
import sys, json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath as mp

c = Q(4076476460239181, 2**51); g = 1 / c; d = 1 - g
q = 4 * g - 5; e9 = 1 - 9 * d; mixed = q + g - 1; quad = 2 * q - 1
print("q =", q, float(q))
print("e9 =", float(e9), " mixed 5g-6 =", float(mixed), " 2q-1 =", float(quad))
assert -3 < q < -1 and quad < mixed < e9 < -3 and mixed == 5 * g - 6
for name, e in [("L2 q+1", q + 1), ("mixed q+gamma", q + g), ("quad 2q", 2 * q),
                ("graded q+6/5", q + Q(6, 5)), ("sharp q+3/5", q + Q(3, 5)), ("sharpw w~r^(4/5): q-1/5", q - Q(1, 5))]:
    assert e < 0, name
    print("exponent", name, float(e))

# (2) Fourier symbols: d_j -> i xi_j, Lap -> -|xi|^2
x1, x2 = sp.symbols("xi1 xi2", real=True)
chi = sp.Symbol("chihat")
I = sp.I
lap = -(x1**2 + x2**2)
hh = -(I * x2) * lap * chi
psi = (I * x1) * (I * x2) * chi
v1 = -(I * x2) * psi; v2 = (I * x1) * psi
u1 = x1 * x2 / (x1**2 + x2**2) * hh          # u = -grad p - rho e_2, div u = 0
u2 = -x1**2 / (x1**2 + x2**2) * hh
assert sp.simplify(v1 - u1) == 0 and sp.simplify(v2 - u2) == 0
print("Fourier multiplier identity v = U[h]: OK (convention u = -grad p - rho e_2)")

# (3) quadrature
mp.mp.dps = 40
src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "data/T4295_007_tail_repair.json"
mom = json.loads(src.read_text())["moment_checks"]
A = {int(x["m"]): mp.mpf(Q(x["A1"]).numerator) / Q(x["A1"]).denominator for x in mom}
p = mp.mpf(q.numerator) / q.denominator + 3
rs = sp.Symbol("r", positive=True)
b = lambda s: sp.exp(-1 / s)
def fderivs(L):
    zeta = b(rs / L - 1) / (b(rs / L - 1) + b(2 - rs / L))
    f = -zeta * rs**sp.Float(str(p), 45)
    fs = [f] + [sp.diff(f, rs, j) for j in (1, 2, 3)]
    return [sp.lambdify(rs, e, "mpmath") for e in fs]
def Hcoef(r, F):
    f0, f1, f2, f3 = F
    H = {}
    for m, a in A.items():
        k = 2 * m
        gk = f2 + f1 / r - k * k * f0 / r**2
        gp = f3 + f2 / r - f1 / r**2 - k * k * f1 / r**2 + 2 * k * k * f0 / r**3
        for n, cf in ((k + 1, -a * (gp - k * gk / r) / 2), (k - 1, a * (gp + k * gk / r) / 2)):
            if n < 0:
                n, cf = -n, -cf
            H[n] = H.get(n, 0) + cf
    return H
def norm_sq_annulus(L):
    F = fderivs(L)
    def integrand(r):
        H = Hcoef(r, [fn(r) for fn in F])
        return mp.pi * sum(v * v for v in H.values()) * r
    return mp.quad(integrand, mp.linspace(L, 2 * L, 9))
def norm_sq_tail(L):
    # r >= 2L: f = -r^p exactly
    F = [lambda r: -r**p, lambda r: -p * r**(p - 1), lambda r: -p * (p - 1) * r**(p - 2),
         lambda r: -p * (p - 1) * (p - 2) * r**(p - 3)]
    H = Hcoef(mp.mpf(1), [fn(mp.mpf(1)) for fn in F])   # coefficients of r^q at r = 1
    s = mp.pi * sum(v * v for v in H.values())
    qq = p - 3
    return s * (2 * L)**(2 * qq + 2) / (-(2 * qq + 2)), s
C00sq_ann = norm_sq_annulus(1); C00sq_tail, ang = norm_sq_tail(1)
C00 = mp.sqrt(C00sq_ann + C00sq_tail)
print("angular L^2 norm of the r^q profile (sqrt(pi sum h_n^2)):", mp.nstr(mp.sqrt(ang), 12))
print("C00 = ||h_1||_2 (007):", mp.nstr(C00, 15), " annulus part", mp.nstr(mp.sqrt(C00sq_ann), 10))
qf = p - 3
for L in (2, 4):
    direct = mp.sqrt(norm_sq_annulus(L) + norm_sq_tail(L)[0])
    pred = mp.mpf(L)**(qf + 1) * C00
    print("L =", L, " direct", mp.nstr(direct, 15), " L^(q+1) C00", mp.nstr(pred, 15),
          " rel diff", mp.nstr(abs(direct / pred - 1), 3))
    assert abs(direct / pred - 1) < mp.mpf(10)**-20
for eps in (mp.mpf("1e-3"), mp.mpf("1e-6")):
    print("||h_L||_2 <", mp.nstr(eps, 2), "for L >", mp.nstr((C00 / eps)**(1 / (-qf - 1)), 8))
