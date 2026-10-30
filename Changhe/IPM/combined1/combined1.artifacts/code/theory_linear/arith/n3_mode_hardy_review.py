"""Review of c1-n3's mode-n Hardy lemma (c1-n3 NOTES_FOR_TEAM.md 05:52Z item 1; reviews/REVIEW_N3_MODE_HARDY.md):
for g = f(r) sin(n theta), n >= 1, g and r g in L2(R^2): ||g||_(Hdot^-1) <= ||r g||_2 / n.

Run from artifacts/:  python3 -B -u arith/n3_mode_hardy_review.py
Needs sympy and mpmath.

Parts:
  (A) sympy, exact: Laplacian of U(r) sin(n theta) with U(r) = V(log r) is r^-2 (V'' - n^2 V) sin(n theta); the
      Dirichlet form of psi(r) sin(n theta); the changes of variable giving ||g||_H^2 = pi int G V dt and
      ||r g||_2^2 = pi int G^2 dt with G(t) = e^(2t) f(e^t); the Green function of the mode equation.
  (B) for f = r^n exp(-r^2): exact (sympy, n = 1, 3, 5, 21, 63) ||g||_H^2 = pi int f u r dr = pi n!/(n 2^(n+3)) from
      the Green function and ||r g||_2^2 = pi (n+1)!/2^(n+3), so n^2 ||g||_H^2/||r g||_2^2 = n/(n+1); the same ratio
      from the Mellin formula by mpmath quadrature (FLOAT, 30 digits).
  (C) sympy, exact: the Gaussian family G(t) = exp(-t^2/(2 L^2)) has ratio sqrt(pi) x e^(x^2) erfc(x), x = n L, and
      this tends to 1 as x -> infinity; mpmath values (FLOAT) for a few x.
Output: logs/n3_mode_hardy_review.log (stdout).
"""
import time

import mpmath as mp
import sympy as sp

T0 = time.monotonic()
r, t, th, n, tau = sp.symbols("r t theta n tau", positive=True)
V = sp.Function("V")
psi = sp.Function("psi")

# (A1) Laplacian in log variables
U = V(sp.log(r))
lap = sp.diff(U, r, 2) + sp.diff(U, r) / r - n**2 * U / r**2
target = (sp.diff(V(t), t, 2) - n**2 * V(t)).subs(t, sp.log(r)) / r**2
d = sp.simplify((lap - target).doit())
assert d == 0, d
print("(A1) Delta(V(log r) sin(n th)) = r^-2 (V'' - n^2 V)(log r) sin(n th): True")

# (A2) Dirichlet form: |grad(psi sin n th)|^2 = psi'^2 sin^2 + n^2 psi^2 cos^2 / r^2,
# angular integral pi (psi'^2 + n^2 psi^2/r^2)
ph = psi(r) * sp.sin(n * th)
x, y = r * sp.cos(th), r * sp.sin(th)
gr2 = sp.diff(ph, r)**2 + sp.diff(ph, th)**2 / r**2
nint = 3
ang = sp.integrate(gr2.subs(n, nint), (th, 0, 2 * sp.pi))
assert sp.simplify(ang - sp.pi * (sp.diff(psi(r), r)**2 + nint**2 * psi(r)**2 / r**2)) == 0
print("(A2) int_0^2pi |grad(psi sin(n th))|^2 d th = pi (psi'^2 + n^2 psi^2/r^2) (checked at n = 3): True")

# (A3) changes of variable r = e^t: f = G e^(-2t), U = V(t), r dr = e^(2t) dt
G = sp.Function("G")
fr = G(t) * sp.exp(-2 * t)
assert sp.simplify(fr * V(t) * sp.exp(2 * t) - G(t) * V(t)) == 0
assert sp.simplify(sp.exp(2 * t) * fr**2 * sp.exp(2 * t) - G(t)**2) == 0
print("(A3) pi int f U r dr = pi int G V dt and pi int r^2 f^2 r dr = pi int G^2 dt with G(t) = e^(2t) f(e^t): True")

# (A4) Green function of -(U'' + U'/r - n^2 U/r^2) = f
s = sp.symbols("s", positive=True)
ff = sp.Function("f")
Ug = (r**(-n) * sp.Integral(s**(n + 1) * ff(s), (s, 0, r))
      + r**n * sp.Integral(s**(1 - n) * ff(s), (s, r, sp.oo))) / (2 * n)
res = -(sp.diff(Ug, r, 2) + sp.diff(Ug, r) / r - n**2 * Ug / r**2)
assert sp.simplify(res.doit() - ff(r)) == 0
print("(A4) U = (r^-n int_0^r s^(n+1) f + r^n int_r^oo s^(1-n) f)/(2n) solves the mode equation: True")
print("(A) done, %.1f s" % (time.monotonic() - T0))

# (B) exact Green-function values and FLOAT Mellin quadrature for f = r^n exp(-r^2)
T1 = time.monotonic()
q, u_ = sp.symbols("q u", positive=True)
mp.mp.dps = 30
for nn in (1, 3, 5, 21, 63):
    fq = q**nn * sp.exp(-q**2)
    # u(r) = (1/(2n)) int (min/max)^n s f(s) ds, so
    # pi int f u r dr = (pi/n) int_0^oo r f(r) int_0^r (s/r)^n s f(s) ds dr
    inner = sp.integrate(s**(2 * nn + 1) * sp.exp(-s**2), (s, 0, q))
    H2 = sp.pi / nn * sp.integrate(sp.expand(q * fq * q**(-nn) * inner), (q, 0, sp.oo))
    R2 = sp.pi * sp.integrate(q**3 * fq**2, (q, 0, sp.oo))
    assert sp.simplify(H2 - sp.pi * sp.factorial(nn) / (nn * 2**(nn + 3))) == 0
    assert sp.simplify(R2 - sp.pi * sp.factorial(nn + 1) / 2**(nn + 3)) == 0
    ratio = sp.nsimplify(sp.simplify(nn**2 * H2 / R2))
    assert ratio == sp.Rational(nn, nn + 1)
    w = lambda z: abs(mp.gamma(mp.mpf(nn + 2) / 2 - 1j * z / 2))**2
    num = mp.quad(lambda z: nn**2 / (z**2 + nn**2) * w(z), [-mp.inf, -nn, 0, nn, mp.inf])
    den = mp.quad(w, [-mp.inf, -nn, 0, nn, mp.inf])
    rm = num / den
    print("(B) n = %2d: n^2 ||g||_H^2/||r g||^2 = %s exactly (Green); Mellin quadrature %s, difference %.1e"
          % (nn, ratio, mp.nstr(rm, 15), float(abs(rm - mp.mpf(nn) / (nn + 1)))))
    assert abs(rm - mp.mpf(nn) / (nn + 1)) < mp.mpf(10)**-20
print("(B) done, %.1f s" % (time.monotonic() - T1))

# (C) Gaussian sharpness family
T2 = time.monotonic()
Lp, xp, z = sp.symbols("L x z", positive=True)
# |Ghat|^2 proportional to exp(-L^2 tau^2) for G = exp(-t^2/(2 L^2))
Gt = sp.exp(-t**2 / (2 * Lp**2))
Ghat = sp.integrate(Gt * sp.exp(-sp.I * tau * t), (t, -sp.oo, sp.oo)) / sp.sqrt(2 * sp.pi)
assert sp.simplify(Ghat - Lp * sp.exp(-Lp**2 * tau**2 / 2)) == 0
# I(L) = int e^(-L^2 tau^2)/(tau^2 + n^2) d tau = (pi/n) e^(n^2 L^2) erfc(n L): both sides solve
# dI/d(L^2) = -sqrt(pi)/L + n^2 I with I -> pi/n as L -> 0
rhs = sp.pi / n * sp.exp(n**2 * Lp**2) * sp.erfc(n * Lp)
rhs_d = sp.diff(rhs, Lp) / (2 * Lp)
# lhs_d = -int e^(-L^2 tau^2) d tau + n^2 int e^(-L^2 tau^2)/(tau^2 + n^2) d tau
lhs_d2 = -sp.sqrt(sp.pi) / Lp + n**2 * rhs
assert sp.simplify(rhs_d - lhs_d2) == 0
assert sp.limit(rhs, Lp, 0) == sp.pi / n
ratio_g = sp.simplify(n**2 * rhs / (sp.sqrt(sp.pi) / Lp))
assert sp.simplify(ratio_g - sp.sqrt(sp.pi) * n * Lp * sp.exp(n**2 * Lp**2) * sp.erfc(n * Lp)) == 0
lim = sp.limit(sp.sqrt(sp.pi) * xp * sp.exp(xp**2) * sp.erfc(xp), xp, sp.oo)
assert lim == 1
print("(C) Gaussian family: ratio sqrt(pi) x e^(x^2) erfc(x), x = n L, limit 1 as x -> oo: True")
for xx in ("0.1", "1", "3", "10", "30", "100"):
    xv = mp.mpf(xx)
    val = mp.sqrt(mp.pi) * xv * mp.exp(xv**2) * mp.erfc(xv)
    gap = 1 - val
    print("(C) x = %5s: ratio %s, 1 - ratio %s, 2 x^2 (1 - ratio) %s"
          % (xx, mp.nstr(val, 12), mp.nstr(gap, 6), mp.nstr(2 * xv**2 * gap, 8)))
    assert 0 < val < 1
print("(C) done, %.1f s; total %.1f s" % (time.monotonic() - T2, time.monotonic() - T0))
