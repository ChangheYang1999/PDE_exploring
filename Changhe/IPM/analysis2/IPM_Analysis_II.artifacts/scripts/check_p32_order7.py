"""Independent check of the seventh stationary order and of the (7,0) residual invariant (P32).

Usage: python3 check_p32_order7.py STATE131_EXACT_JSON RECUR_SINE_JSON [OUTPUT_JSON]
(for example certificates/P1_source/state131_exact.json certificates/P32_stationary_order_seven/recur_sine.json)

Inputs: the exact state 131 record (canonical order and rational coefficients) and the record recur_sine.json of the
recurrence (densities Theta_n, streams Psi_n and potentials C_n for n = 1..8 and the order 8 defect E_7). Checks:
(1) C_1 equals sum_k a_(0,m,k) of the original coefficients (exact rationals);
(2) at several points, by numerical Cartesian differentiation in mpmath (60 digits), rho_n = -d_y Laplace(r^(p_n+3) C_n),
    psi_n = d_x d_y (r^(p_n+3) C_n), -Laplace psi_n = d_x rho_n, the stationary equations
    c X.grad rho_n - rho_n + sum_(i+j=n) (psi_i,x rho_j,y - psi_i,y rho_j,x) = 0 for n = 2..7, and
    sum_(i+j=8) (psi_i,x rho_j,y - psi_i,y rho_j,x) = r^(p_8) E_7(theta) = 7(c-1) rho_8;
(3) the full-circle and first-quadrant norms of E_7 from the exact coefficients, and by trapezoidal quadrature (exact
    for these trigonometric polynomials) of the angular functions built from the polar formula, together with the
    six-branch residual at the same power (orders i, j <= 6 only).
"""
import json, sys, random
from fractions import Fraction as Fr
import mpmath as mp

sys.set_int_max_str_digits(0)
mp.mp.dps = 60
ex = json.load(open(sys.argv[1])); rs = json.load(open(sys.argv[2]))
c = Fr(ex["exact_parameters"]["cl"]); delta = 1 - 1 / c
assert str(c) == rs["c"] and str(delta) == rs["delta"]
out = {}

# (1) leading potential from the original coefficients
C1 = {}
for (j, m, k), v in zip(ex["canonical_order"], ex["canonical_coefficients"]):
    if j == 0:
        C1[2 * m] = C1.get(2 * m, Fr(0)) + Fr(v)
C1 = {m: v for m, v in C1.items() if v}
rec = {int(m): Fr(v) for m, v in rs["orders"]["1"]["potential"].items()}
assert C1 == rec, "C_1 mismatch"
out["C1_matches_original"] = True

O = {n: {key: {int(m): Fr(v) for m, v in rs["orders"][str(n)][key].items()} for key in ("density", "stream", "potential")}
     for n in range(1, 9)}
E7 = {int(m): Fr(v) for m, v in rs["order8_fixed_defect"]["sine_coefficients"].items()}
p = {n: 1 - n * delta for n in range(1, 9)}
mpf = lambda q: mp.mpf(q.numerator) / q.denominator
P = {n: mpf(p[n]) for n in p}; cc = mpf(c)


def polar(coef, kind, power):
    def f(x, y):
        r = mp.sqrt(x * x + y * y); t = mp.atan2(y, x)
        s = mp.fsum(mpf(v) * (mp.cos(m * t) if kind == "cos" else mp.sin(m * t)) for m, v in coef.items())
        return r ** power * s
    return f


rho = {n: polar(O[n]["density"], "sin", P[n]) for n in O}
psi = {n: polar(O[n]["stream"], "sin", P[n] + 1) for n in O}
chi = {n: polar(O[n]["potential"], "cos", P[n] + 3) for n in O}
d = lambda f, x, y, a, b: mp.diff(f, (x, y), (a, b))

random.seed(20261028)
pts = [(mp.mpf(random.uniform(-2, 2)), mp.mpf(random.uniform(-2, 2))) for _ in range(4)]
worst = {}
def rel(name, lhs, rhs, scale):
    e = abs(lhs - rhs) / scale
    worst[name] = max(worst.get(name, 0), float(e))
for x, y in pts:
    D = {n: (d(rho[n], x, y, 1, 0), d(rho[n], x, y, 0, 1)) for n in O}
    S = {n: (d(psi[n], x, y, 1, 0), d(psi[n], x, y, 0, 1)) for n in O}
    for n in O:
        r_n = rho[n](x, y)
        r_from_chi = -(d(chi[n], x, y, 2, 1) + d(chi[n], x, y, 0, 3))
        rel("density_from_potential", r_from_chi, r_n, abs(r_n) + 1)
        rel("stream_from_potential", d(chi[n], x, y, 1, 1), psi[n](x, y), abs(psi[n](x, y)) + 1)
        lap = d(psi[n], x, y, 2, 0) + d(psi[n], x, y, 0, 2)
        rel("poisson", -lap, D[n][0], abs(D[n][0]) + 1)
    for n in range(2, 9):
        J = mp.fsum(S[i][0] * D[n - i][1] - S[i][1] * D[n - i][0] for i in range(1, n))
        if n <= 7:
            lin = cc * (x * D[n][0] + y * D[n][1]) - rho[n](x, y)
            rel("stationary_orders_2_to_7", lin + J, 0, abs(J) + 1)
        else:
            e7 = polar(E7, "sin", P[8])(x, y)
            rel("order8_defect_equals_E7", J, e7, abs(e7) + 1)
            rel("E7_equals_7(c-1)rho8", e7, 7 * (cc - 1) * rho[8](x, y), abs(e7) + 1)
out["max_relative_errors_at_4_points"] = worst
assert all(v < 1e-15 for v in worst.values()), worst

# (3) norms
mp.mp.dps = 40
sq = sum(v * v for v in E7.values())
full = mp.sqrt(mp.pi * mpf(sq)); out["E7_full_circle_exact_coefficients"] = mp.nstr(full, 25)
out["E7_first_quadrant_exact_coefficients"] = mp.nstr(full / 2, 25)
N = 512
num = {"E7": mp.mpf(0), "six_branch": mp.mpf(0), "E7_quadrant_simpson": None}
vals = []
for k in range(N):
    t = 2 * mp.pi * k / N
    def ang(coef, deriv):
        return mp.fsum(mpf(v) * (m * mp.cos(m * t) if deriv else mp.sin(m * t)) for m, v in coef.items())
    Th = {n: (ang(O[n]["density"], 0), ang(O[n]["density"], 1)) for n in range(1, 8)}
    Ps = {n: (ang(O[n]["stream"], 0), ang(O[n]["stream"], 1)) for n in range(1, 8)}
    terms = {i: (P[i] + 1) * Ps[i][0] * Th[8 - i][1] - P[8 - i] * Ps[i][1] * Th[8 - i][0] for i in range(1, 8)}
    e = mp.fsum(terms.values()); old = mp.fsum(terms[i] for i in range(2, 7))
    num["E7"] += e * e; num["six_branch"] += old * old
    vals.append(e)
    assert abs(e - ang(E7, 0)) < mp.mpf(10) ** -25 * (1 + abs(e))
for key in ("E7", "six_branch"):
    f = mp.sqrt(num[key] * 2 * mp.pi / N)
    out[key + "_full_circle_quadrature"] = mp.nstr(f, 25); out[key + "_first_quadrant_quadrature"] = mp.nstr(f / 2, 25)
# first quadrant directly: integrate over [0, pi/2] by Gauss-Legendre
fE = lambda t: mp.fsum(mpf(v) * mp.sin(m * t) for m, v in E7.items()) ** 2
mp.mp.dps = 30
out["E7_first_quadrant_direct_quad"] = mp.nstr(mp.sqrt(mp.quad(fE, mp.linspace(0, mp.pi / 2, 41))), 20)
sq7 = sum(v * v for v in O[7]["density"].values()) * (6 * (c - 1)) ** 2
f7 = mp.sqrt(mp.pi * mpf(sq7))
out["six_branch_(6,0)_invariant_6(c-1)Theta7_full_circle"] = mp.nstr(f7, 20)
out["six_branch_(6,0)_invariant_first_quadrant"] = mp.nstr(f7 / 2, 20)
out["power_p8"] = mp.nstr(mpf(p[8]), 20); out["power_(2,1)"] = mp.nstr(mpf(1 - 3 * delta - 2), 20)
assert 5 * delta - 2 > 0 and 2 - 4 * delta > 0 and 4 - 7 * delta > 0
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[3] if len(sys.argv) > 3 else "check_v119.json", "w"), indent=1)
