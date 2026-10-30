"""c1-t1 R1-025: FLOAT illustration of T4-205 assertion 3, bound (1), and of the E_a divergence in assertions 1, 2.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4205.py > check_T4205.out

The review (nonlinear_closure/REVIEWS_v21.md) is analytic; this script is an illustration, not part of the proof.
Theta = sin(theta) (||Theta||_2^2 = pi), smooth cutoff chi(r) = s(r - 1), s(x) = e^(-1/x)/(e^(-1/x) + e^(-1/(1-x))).
(i) For I = [1/2, 1/c] with c the 007 value, b = 1 + 1/c + eps, eps in {0.05, 0.25}, N = 0..4, gamma = max I:
    ||d_gamma^N T_gamma||_(E_b)^2 = pi int chi^2 r^(2 gamma + 1) (log r)^(2N) (1 + r^2)^(-b) dr (mpmath quad, 30 digits)
    against pi (2N)!/(2 eps)^(2N+1).
(ii) The partial E_a norms on 2 < r < R of T_gamma - chi r^gamma0 P(log r) Theta, gamma0 = 1/c, gamma = 0.5,
    P = first three Taylor terms of exp((gamma - gamma0) log r), at a = 0 and at the endpoint a = 1 + gamma: they
    grow with R.
"""
import mpmath as mp

mp.mp.dps = 30
c = mp.mpf(4076476460239181) / mp.mpf(2) ** 51
g1 = 1 / c


def s(x):
    if x <= 0:
        return mp.mpf(0)
    if x >= 1:
        return mp.mpf(1)
    e0, e1 = mp.e ** (-1 / x), mp.e ** (-1 / (1 - x))
    return e0 / (e0 + e1)


def chi(r):
    return s(r - 1)


print(f"gamma0 = 1/c = {mp.nstr(g1, 15)}")
for eps in (mp.mpf("0.05"), mp.mpf("0.25")):
    b = 1 + g1 + eps
    for N in range(5):
        f = lambda r: chi(r) ** 2 * r ** (2 * g1 + 1) * mp.log(r) ** (2 * N) * (1 + r * r) ** (-b)
        val = mp.pi * mp.quad(f, [1, 2, 10, 100, 1e4, 1e8, 1e16, 1e32, 1e64, 1e128, mp.inf])
        bound = mp.pi * mp.factorial(2 * N) / (2 * eps) ** (2 * N + 1)
        assert val < bound
        print(f"(i) eps = {mp.nstr(eps, 3)}, N = {N}: ||d^N T||_(E_b)^2 = {mp.nstr(val, 12)}"
              f" <= bound {mp.nstr(bound, 12)}"
              f" (ratio {mp.nstr(val / bound, 6)})")
g = mp.mpf("0.5")
for a in (mp.mpf(0), 1 + g):
    row = []
    for R in (1e2, 1e4, 1e8, 1e16):
        def f(r):
            L = mp.log(r)
            P = 1 + (g - g1) * L + ((g - g1) * L) ** 2 / 2
            return (r ** g - r ** g1 * P) ** 2 * (1 + r * r) ** (-a) * r
        row.append(mp.pi * mp.quad(f, [2] + [q for q in (10, 100, 1e4, 1e8) if q < R] + [R]))
    print(f"(ii) a = {mp.nstr(a, 6)}: pi int_2^R |T_gamma - chi r^gamma0 P(log r) Theta|^2 (1+r^2)^(-a) r dr for"
          f" R = 1e2, 1e4, 1e8, 1e16: {', '.join(mp.nstr(v, 8) for v in row)}")
    assert row[0] < row[1] < row[2] < row[3]
print("done")
