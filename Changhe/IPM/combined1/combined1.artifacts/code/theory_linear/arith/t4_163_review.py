"""Checks for the c1-t2 review of T4-163 (c1-t4 research/weighted_symmetric_coupling/PROOF.md, sha256
c37e645d...619617): the symmetric weighted coupling error is Hilbert-Schmidt (reviews/REVIEW_T4_163.md).

Run from artifacts/:  python3 -B arith/t4_163_review.py   (under a minute)
Parts:
  (1) sympy: the off-diagonal kernel of U = (-R1R2, R1^2) from the fundamental solution -(log|z|)/(2 pi) of -Delta;
      |K| = 1/(2 pi |z|^2); the local term of R1^2 is -1/2 (symbol identity); the kernel identity (4); the radial
      integral of Section 2; the Taylor bounds used in (5) on a grid.
  (2) FLOAT: the increment integral I(f, g) by direct quadrature for two explicit pairs, against J of (1).
  (3) FLOAT: the bound (2) against the coarse bound G(exp(Psi) - 1) for a model weight, a tent in log r of height
      Psi and ramp log-length S_r starting at r0 (the cost model of notes/T2_localized_BL2.md section 6.2), as a
      function of Psi, S_r and lambda = 2G/(H r0).
Output: logs/t4_163_review.log (stdout), data/t4_163_review_results.json.
"""
import json
import time
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (1) sympy ===============================
z1, z2 = sp.symbols("z1 z2", real=True)
x1, x2 = sp.symbols("xi1 xi2", real=True)
Phi = -sp.log(sp.sqrt(z1**2 + z2**2)) / (2 * sp.pi)
K = sp.Matrix([-sp.diff(Phi, z1, z2), sp.diff(Phi, z1, 2)])          # off-diagonal kernels of -d1 d2 and d1^2 of (-Delta)^-1
Kc = sp.Matrix([-2 * z1 * z2, z1**2 - z2**2]) / (2 * sp.pi * (z1**2 + z2**2) ** 2)
assert sp.simplify(K - Kc) == sp.zeros(2, 1)
assert sp.simplify(Kc.dot(Kc) - 1 / (2 * sp.pi * (z1**2 + z2**2)) ** 2) == 0
# symbols: R_j = d_j (-Delta)^(-1/2) has symbol i xi_j/|xi|; R1^2 = -xi1^2/|xi|^2 = -1/2 - (xi1^2 - xi2^2)/(2|xi|^2)
n2 = x1**2 + x2**2
assert sp.simplify(-x1**2 / n2 - (-sp.Rational(1, 2) - (x1**2 - x2**2) / (2 * n2))) == 0
assert sp.simplify((sp.I * x1 / sp.sqrt(n2)) * (sp.I * x2 / sp.sqrt(n2)) + x1 * x2 / n2) == 0     # -R1R2 = xi1 xi2/|xi|^2
# the angular means of both kernel components vanish (so the principal values exist and carry no extra delta)
th = sp.symbols("theta", real=True)
for comp in (-2 * sp.cos(th) * sp.sin(th), sp.cos(th) ** 2 - sp.sin(th) ** 2):
    assert sp.integrate(comp, (th, 0, 2 * sp.pi)) == 0
print("(1) K = (-2 z1 z2, z1^2 - z2^2)/(2 pi |z|^4) from -(log|z|)/(2 pi); |K| = 1/(2 pi |z|^2); R1^2 = -1/2 - (R1^2 - R2^2)/2"
      " on the symbol side, so the local term of U is (0, -h/2); both kernel components have zero angular mean")
d, a, b = sp.symbols("d a b", real=True)
lhs = sp.exp(d) * a + sp.exp(-d) * b - a - b
rhs = (sp.cosh(d) - 1) * (a + b) + sp.sinh(d) * (a - b)
assert sp.simplify((lhs - rhs).rewrite(sp.exp)) == 0
print("    kernel identity (4): e^d a + e^-d b - a - b = (cosh d - 1)(a + b) + sinh d (a - b)")
r, m, M = sp.symbols("r m M", positive=True)
tot = (sp.integrate(r**4 / r**3, (r, 0, m)) + sp.integrate(m**2 * r**2 / r**3, (r, m, M))
       + sp.integrate(m**2 * M**2 / r**3, (r, M, sp.oo)))
assert sp.simplify(tot - m**2 * (1 + sp.log(M / m))) == 0
print("    Section 2: int_0^inf min(r, m)^2 min(r, M)^2 r^-3 dr = m^2 (1 + log(M/m)) for m <= M:", sp.simplify(tot))
dd = np.linspace(-6, 6, 24001)
for Ps in (0.1, 0.5, 1.0, 2.0, 6.0):
    sel = np.abs(dd) <= Ps
    assert np.all(np.cosh(dd[sel]) - 1 <= np.cosh(Ps) * dd[sel] ** 2 / 2 * (1 + 1e-14) + 1e-300)
    assert np.all(np.abs(np.sinh(dd[sel])) <= np.cosh(Ps) * np.abs(dd[sel]) * (1 + 1e-14) + 1e-300)
print("    Taylor bounds |cosh d - 1| <= cosh(Psi) d^2/2 and |sinh d| <= cosh(Psi)|d| on |d| <= Psi (grid check;"
      " the proof is the Lagrange remainder)")


# =============================== (2) the increment integral ===============================
def J(A, B, H0, D):
    R, S = 2 * B / A, D / H0
    lo, hi = min(R, S), max(R, S)
    return np.sqrt(2 * np.pi) * A * H0 * lo * np.sqrt(1 + np.log(hi / lo))


def incr_integral(f, g, fg2, rmax=12.0, Lbox=21.0, nx=281, nr=64, nth=32):
    """I(f, g)^2 for |z| <= rmax by quadrature (x on [-Lbox, Lbox]^2, which contains supp f + {|z| <= rmax} up to
    Gaussian tails below 1e-15), plus the exact large-|z| limit for |z| > rmax: there the two increments have
    separated supports, so int dx = 2 int f^2 g^2 = 2 fg2 and int_(|z| > rmax) |z|^-4 dz = pi/rmax^2."""
    xs = np.linspace(-Lbox, Lbox, nx)
    hx = xs[1] - xs[0]
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    f0, g0 = f(X, Y), g(X, Y)
    u, wu = np.polynomial.legendre.leggauss(nr)
    lr0, lr1 = np.log(1e-3), np.log(rmax)
    lr = (lr1 - lr0) / 2 * u + (lr1 + lr0) / 2
    wr = (lr1 - lr0) / 2 * wu
    tot = 0.0
    for rr, wl in zip(np.exp(lr), wr):
        acc = 0.0
        for k in range(nth):
            t = 2 * np.pi * k / nth
            zx, zy = rr * np.cos(t), rr * np.sin(t)
            acc += np.sum(np.abs(f(X + zx, Y + zy) - f0) ** 2 * np.abs(g(X + zx, Y + zy) - g0) ** 2) * hx * hx
        acc *= 2 * np.pi / nth
        tot += wl * rr * rr * acc / rr**4          # dz = r dr dth = r^2 d(log r) dth
    return tot + 2 * fg2 * np.pi / rmax**2


def gauss(s):
    return lambda X, Y: np.exp(-(X**2 + Y**2) / (2 * s * s))


rows2 = []
for (sf, sg, amp) in ((1.0, 1.0, 1.0), (0.7, 1.5, 2.0)):
    f = gauss(sf)
    g = (lambda X, Y, sg=sg, amp=amp: amp * np.exp(-(X**2 + Y**2) / (2 * sg * sg)))
    A = np.sqrt(np.pi)                                # ||grad exp(-r^2/(2 s^2))||_2 = sqrt(pi), independent of s
    B = sf * np.sqrt(np.pi)                           # ||exp(-r^2/(2 s^2))||_2 = s sqrt(pi)
    H0 = amp * np.exp(-0.5) / sg                      # Lipschitz constant of amp exp(-r^2/(2 sg^2))
    D = amp                                           # its oscillation
    fg2 = amp**2 * np.pi / (1 / sf**2 + 1 / sg**2)       # int f^2 g^2 = amp^2 int exp(-r^2 (1/sf^2 + 1/sg^2))
    I2 = incr_integral(f, g, fg2)
    rows2.append(dict(s_f=sf, s_g=sg, amp=amp, I=float(np.sqrt(I2)), J=float(J(A, B, H0, D))))
    print(f"(2) f = exp(-r^2/(2*{sf}^2)), g = {amp} exp(-r^2/(2*{sg}^2)): I(f, g) = {np.sqrt(I2):.6f} (FLOAT quadrature)"
          f" <= J = {J(A, B, H0, D):.6f}; ratio {np.sqrt(I2) / J(A, B, H0, D):.4f}")
    assert np.sqrt(I2) <= J(A, B, H0, D)
OUT["increment_integral"] = rows2


# =============================== (3) model comparison ===============================
# psi(r) = Psi * tent(log(r/r0)/S_r), tent(s) = s on [0, 1], 2 - s on [1, 2], 0 otherwise.  Units r0 = 1.
# A^2 = 2 pi int (d psi/d log r)^2 d log r = 4 pi Psi^2/S_r;  L = Psi/S_r (at r = r0);  oscillation Psi;
# B^2 = 2 pi int psi^2 r dr.  Background: G = ||grad rho||_inf, H = Lip(grad rho), lambda = 2G/(H r0).
def model(Ps, Sr, lam, G=1.0):
    A = Ps * np.sqrt(4 * np.pi / Sr)
    L = Ps / Sr
    f1 = lambda t: (t / Sr) ** 2 * np.exp(2 * t)
    f2 = lambda t: ((2 * Sr - t) / Sr) ** 2 * np.exp(2 * t)
    B2 = 2 * np.pi * Ps**2 * (integrate.quad(f1, 0, Sr, epsrel=1e-12)[0] + integrate.quad(f2, Sr, 2 * Sr, epsrel=1e-12)[0])
    B = np.sqrt(B2)
    H = 2 * G / lam
    new = np.cosh(Ps) / (4 * np.pi) * (G * J(A, B, L, Ps) + J(A, B, H, 2 * G))
    lin = np.cosh(Ps) / (4 * np.pi) * J(A, B, H, 2 * G)
    coarse = G * (np.exp(Ps) - 1)
    return dict(Psi=Ps, S_r=Sr, lam=lam, A=A, B=B, R=2 * B / A, new=new, new_linear_term=lin, coarse=coarse,
                ratio=new / coarse)


rows3 = []
print("(3) model weight: tent in log r (height Psi, ramp log-length S_r, inner radius r0 = 1); lambda = 2G/(H r0);"
      " ratio = bound (2) / G(exp(Psi) - 1)  (FLOAT)")
print(f"    {'Psi':>5s} {'S_r':>5s} | " + " | ".join(f"lambda = {lam:g}" for lam in (0.01, 0.1, 1.0, 10.0, 100.0, 1e4)))
for Ps in (0.1, 0.5, 1.0):
    for Sr in (0.25, 0.5, 1.0, 2.0, 4.0):
        cells = []
        for lam in (0.01, 0.1, 1.0, 10.0, 100.0, 1e4):
            e = model(Ps, Sr, lam)
            rows3.append(e)
            cells.append(f"{e['ratio']:12.4f}")
        print(f"    {Ps:5.2f} {Sr:5.2f} | " + " | ".join(cells))
OUT["model"] = rows3
# large S_r limit of the linear term: cosh(Psi)/(4 pi) J(A, B; H, 2G) / (G Psi) -> 2 cosh(Psi) (2D capacity)
for Sr in (4.0, 8.0, 16.0, 32.0):
    e = model(0.01, Sr, 1.0)
    print(f"    S_r = {Sr:5.1f}, Psi = 0.01, lambda = 1: linear term / (G Psi) = {e['new_linear_term'] / 0.01:.4f}"
          f" (log R = {np.log(e['R']):.3f})")
OUT["elapsed_seconds"] = time.monotonic() - T0
(HERE / "data/t4_163_review_results.json").write_text(json.dumps(OUT, indent=1))
print(f"done in {time.monotonic() - T0:.1f} s; wrote data/t4_163_review_results.json")
