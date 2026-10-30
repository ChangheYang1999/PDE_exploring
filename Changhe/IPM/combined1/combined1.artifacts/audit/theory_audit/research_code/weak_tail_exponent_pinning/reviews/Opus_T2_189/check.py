"""Checks for the c1-t2 review of T4-189 (a weighted L2 correction fixes the similarity exponent).

Source (read only):
  c1-t4/research/weak_tail_exponent_pinning/PROOF.md  sha256 b516639410c86d01c393cd9c10b7c5de9079f2150912f7a3af684f40bb814577

The proof is analytic; these checks only test its algebra and illustrate its limits. Nothing here is a proof.
  C1 sympy: divergence form (2) equals c' X.grad f - f + W.grad f when div W = 0; the limit pairing
     <c' div(Y g) - (2c'+1) g, psi> = (c' gamma - 1) J for g = |Y|^gamma Theta, psi = chi(|Y|) Theta (polar form).
  C2 sympy: the R-exponents of the five bounds in (6) from the change of variables X = R Y, and their signs for
     0 <= a <= 1 + gamma, 0 < gamma < 1. Also the exponents of the two alternative bounds that use |rho| <= C0 r^gamma
     instead of |grad rho| <= C_rho r^(gamma - 1) (review remark R2).
  C3 mpmath FLOAT: rho = (1 + r^2)^((gamma - 1)/2) y (smooth, S1, leading term r^gamma sin theta). The linear background
     pairing at R = 10^k for c' = 1.3 and c' = 1/gamma, against the limit (c' gamma - 1) J.
  C4 mpmath FLOAT: endpoint a = 1 + gamma. h = y (1 + r^2)^((gamma - 1)/2) / log(e + r^2) lies in L2(w_a^2) (the radial
     integrand is about pi/(4 r log(r)^2)). Its linear pairing (the bound with exponent R^0) tends to 0 only
     logarithmically: about (c' gamma - 1) J/(2 log R) for c' != 1/gamma, and about -2 c' J/(2 log R)^2 for c' = 1/gamma.
  C5 mpmath FLOAT: the sharpness example. int_1^Rmax r^(2 gamma) (1 + r^2)^(-a) r dr grows without bound at
     a = 1 + gamma and converges for a = 1 + gamma + 0.05.
  C6 sympy: exponents for the weighted residual threshold of review remark R3 (tests R^-1 psi(X/R), as in T4-049):
     each correction term against the left side R^(q+1), and the resulting condition q >= a - 1 for a <= 2; the
     values a_max = q + 1 for the residual exponents e_F printed by artifacts/arith/t4_094_review.py.
Runtime: a few seconds on one core.
"""
import sys
import time

import mpmath as mp
import sympy as sp

T0 = time.time()
print("t4_189_review.py start", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
mp.mp.dps = 30
c_val = sp.Rational(4076476460239181, 2 ** 51)
gam_val = 1 / c_val

# ---------------------------------------------------------------- C1
x, y = sp.symbols("x y", real=True)
cp = sp.symbols("cprime", real=True)
f = sp.Function("f")(x, y)
W1 = sp.Function("W1")(x, y)
W2 = sp.Function("W2")(x, y)
div_form = cp * (sp.diff(x * f, x) + sp.diff(y * f, y)) - (2 * cp + 1) * f + sp.diff(W1 * f, x) + sp.diff(W2 * f, y)
nondiv = cp * (x * sp.diff(f, x) + y * sp.diff(f, y)) - f + W1 * sp.diff(f, x) + W2 * sp.diff(f, y)
diffr = sp.expand(div_form - nondiv - f * (sp.diff(W1, x) + sp.diff(W2, y)))
print("C1 divergence form (2) - [c' X.grad f - f + W.grad f] - f div W =", sp.simplify(diffr))

s, g_ = sp.symbols("s gamma", positive=True)
chi = (s - 1) ** 4 * (2 - s) ** 4          # C^3 bump on [1, 2]; enough for this algebraic check
# polar form with Theta^2 integrated to T2 = int Theta^2 dtheta (a common factor):
# <c' div(Y g) - (2c'+1) g, psi> = -int g [c' Y.grad psi + (2c'+1) psi] = -T2 int s^gamma [c' s chi' + (2c'+1) chi] s ds
T2 = sp.symbols("T2", positive=True)
pair = -T2 * sp.integrate(sp.expand(s ** g_ * (cp * s * sp.diff(chi, s) + (2 * cp + 1) * chi) * s), (s, 1, 2))
Jval = T2 * sp.integrate(sp.expand(s ** (g_ + 1) * chi), (s, 1, 2))
print("C1 pairing - (c' gamma - 1) J =", sp.simplify(sp.expand(pair - (cp * g_ - 1) * Jval)))

# ---------------------------------------------------------------- C2
R, a = sp.symbols("R a", positive=True)
# scalings: phi_R = R^(-gamma-2) psi(X/R); ||phi_R||_1 = R^(-gamma)||psi||_1, ||phi_R||_2 = R^(-gamma-1)||psi||_2,
# ||X.grad phi_R||_2 = R^(-gamma-1)||Y.grad psi||_2, ||grad phi_R||_2 = R^(-gamma-2)||grad psi||_2,
# ||grad phi_R||_inf = R^(-gamma-3)||grad psi||_inf; on A_R: |u| <= C_u (2R)^gamma, |grad rho| <= C_rho R^(gamma-1),
# |rho| <= C0 (2R)^gamma, w_a^(-1) <= 5^(a/2) R^a.
ex = {
    "u.grad rho":        g_ + (g_ - 1) - g_,
    "h linear":          a - g_ - 1,
    "h u.grad phi":      a + g_ - g_ - 2,
    "phi v.grad rho":    a + (g_ - 1) - g_ - 1,
    "h v.grad phi":      2 * a - g_ - 3,
    "R2: rho u.grad phi": 2 * g_ + (-g_ - 1),   # |rho||u| <= C0 C_u (2R)^(2 gamma); ||grad phi_R||_1 = R^(-gamma-1)||grad psi||_1
    "R2: rho v.grad phi": a + g_ - g_ - 2,
}
printed = {"u.grad rho": g_ - 1, "h linear": a - g_ - 1, "h u.grad phi": a - 2, "phi v.grad rho": a - 2,
           "h v.grad phi": 2 * a - g_ - 3, "R2: rho u.grad phi": g_ - 1, "R2: rho v.grad phi": a - 2}
for k_, e_ in ex.items():
    print(f"C2 exponent of R in bound '{k_}': {sp.simplify(e_)}  (printed/expected {printed[k_]}, difference {sp.simplify(e_ - printed[k_])})")
# signs on 0 <= a <= 1 + gamma, 0 < gamma < 1: maximize each exponent at a = 1 + gamma
for k_, e_ in ex.items():
    worst = sp.simplify(e_.subs(a, 1 + g_))
    print(f"C2 '{k_}' at a = 1 + gamma: {worst}; at gamma = 1/c: {sp.nsimplify(worst.subs(g_, gam_val)).evalf(12)}")
print("C2 note: 'h linear' has exponent 0 at the endpoint; it tends to 0 only through m_R -> 0.")

# ---------------------------------------------------------------- C3, C4
gam = mp.mpf(4076476460239181) / mp.mpf(2) ** 51
gam = 1 / gam
bump = lambda t: mp.exp(-1 / ((t - 1) * (2 - t))) if 1 < t < 2 else mp.mpf(0)
dbump = lambda t: bump(t) * (-(2 * t - 3) / ((t - 1) * (2 - t)) ** 2) if 1 < t < 2 else mp.mpf(0)
J = mp.pi * mp.quad(lambda t: t ** (gam + 1) * bump(t), [1, 1.5, 2])        # Theta = sin theta, int sin^2 = pi


def lin_pair(fr, cpr, Rr):
    """-int fr(r) sin(theta) [c' r d_r phi_R + (2c'+1) phi_R] dX, phi_R = R^(-gamma-2) bump(r/R) sin(theta)."""
    integ = lambda t: fr(Rr * t) * Rr ** (-gam) * (cpr * t * dbump(t) + (2 * cpr + 1) * bump(t)) * t
    return -mp.pi * mp.quad(integ, [1, 1.5, 2])


rho_r = lambda r: (1 + r * r) ** ((gam - 1) / 2) * r            # rho = (1+r^2)^((gamma-1)/2) y = rho_r(r) sin(theta)
for cpr in [mp.mpf("1.3"), 1 / gam]:
    vals = [lin_pair(rho_r, cpr, mp.mpf(10) ** k) for k in (1, 2, 4, 8)]
    lim = (cpr * gam - 1) * J
    print(f"C3 c' = {mp.nstr(cpr, 10)}: pairing at R = 1e1, 1e2, 1e4, 1e8:", [mp.nstr(v, 10) for v in vals], " limit (c' gamma - 1) J =", mp.nstr(lim, 10))

h_r = lambda r: rho_r(r) / mp.log(mp.e + r * r)
for cpr, pw in [(mp.mpf("1.3"), 1), (1 / gam, 2)]:
    lim = (cpr * gam - 1) * J if pw == 1 else -2 * cpr * J
    for k in (1, 2, 4, 8, 16):
        Rr = mp.mpf(10) ** k
        v = lin_pair(h_r, cpr, Rr)
        print(f"C4 endpoint h, c' = {mp.nstr(cpr, 8)}: R = 1e{k}: pairing {mp.nstr(v, 8)}, times (2 log R)^{pw}: {mp.nstr(v * (2 * mp.log(Rr)) ** pw, 8)} (limit {mp.nstr(lim, 8)})")
# membership of h in L2(w_a^2), a = 1 + gamma: radial integrand int pi r h_r^2 (1+r^2)^(-a) dr, finite
a_end = 1 + gam
tail = lambda r: mp.pi * h_r(r) ** 2 * (1 + r * r) ** (-a_end) * r
logq = lambda fun, lo, hi: mp.quad(lambda t: fun(mp.exp(t)) * mp.exp(t), mp.linspace(mp.log(lo), mp.log(hi), 9))
cum = mp.quad(tail, [0, 1])
row = []
edges = [1, 1e3, 1e6, 1e12, 1e24, 1e48]
for i in range(len(edges) - 1):
    cum += logq(tail, edges[i], edges[i + 1])
    if edges[i + 1] >= 1e6:
        row.append(f"r < {edges[i + 1]:.0e}: {mp.nstr(cum, 8)} (+ pi/(4 log r) = {mp.nstr(cum + mp.pi / (4 * mp.log(edges[i + 1])), 8)})")
print("C4 ||w_a h||^2 (a = 1 + gamma), partial integrals:", "; ".join(row))
print("   the tail beyond r is about pi/(4 log r), so the sum in parentheses should be nearly constant")

# ---------------------------------------------------------------- C5
for da in [mp.mpf(0), mp.mpf("0.05")]:
    aa = 1 + gam + da
    vals = [logq(lambda r: r ** (2 * gam) * (1 + r * r) ** (-aa) * r, 1, mp.mpf(10) ** k) for k in (8, 16, 32)]
    print(f"C5 a = 1 + gamma + {da}: int_1^Rmax r^(2 gamma)(1+r^2)^(-a) r dr at Rmax = 1e8, 1e16, 1e32:", [mp.nstr(v, 8) for v in vals])

# ---------------------------------------------------------------- C6
q = sp.symbols("q", real=True)
aa_ = sp.symbols("a", real=True)
# phi_R = R^-1 psi(X/R): ||phi_R||_2 = ||psi||_2, ||X.grad phi_R||_2 = ||Y.grad psi||_2, ||grad phi_R||_2 = R^-1 ||grad psi||_2,
# ||grad phi_R||_inf = R^-2 ||grad psi||_inf; w_a^(-1) <= 5^(a/2) R^a on A_R for a >= 0 and <= R^a for a < 0.
terms6 = {"h linear": aa_, "h u.grad phi": aa_ + g_ - 1, "phi v.grad rho": aa_ + g_ - 1, "h v.grad phi": 2 * aa_ - 2}
for k_, e_ in terms6.items():
    print(f"C6 term '{k_}': R-exponent {e_}; minus (q + 1) at q = a - 1: {sp.simplify(e_ - aa_)}")
print("C6 so with q >= a - 1 every term is O(R^(q+1)) times a factor m_R or n_R -> 0, if gamma < 1 and a <= 2.")
dl = 1 - gam_val
for name, eF in [("state131", 1 - 2 * dl), ("d2, Mpen2", 1 - 7 * dl), ("005", 1 - 4 * dl - 2)]:
    print(f"C6 {name}: e_F = {sp.N(eF, 12)}; no correction in L2(w_a^2) for a <= a_max = e_F + 1 = {sp.N(eF + 1, 12)}"
          f" (growing weights (1+r^2)^(p/2) with p >= {sp.N(-eF - 1, 12)})")

print(f"EXIT 0 elapsed {time.time() - T0:.1f} s")
sys.exit(0)
