"""Independent second review of FW-T-T4ALT-defect-v1 (c1-t4 research/alternative_route/PROOF.md, sha256 d347071a...1fa).

Run from artifacts/:  python3 -B arith/t4alt_review.py [--no-float]
Needs sympy, mpmath, python-flint, numpy.  About 1 min.  This is my own code; it does not import or run c1-t4 code.

Exact or rigorous part (sympy exact, Fraction, arb at 256 bits):
  (1) section 2, fractional commutator: subordination formula for J^s (mpmath, 40 digits, identity check), Gaussian
      moments int |z| G_t = sqrt(pi t) and int |z|^2 G_t = 4 t (sympy), the two kernel moments of the proof, the
      constant 17 (rational majorants), the weight ratio polynomial, and the sharper constant
      (sqrt(pi)/2) Gamma((1 - s_max)/2) + 16/5 valid for 0 < s <= s_max (arb);
  (2) section 2, multiplication bound: Fourier symbols of U and of the stream function psi, the identity
      U[H0].Dg = div(psi (g_y, -g_x)), the commutator identity C = div([J^s, g] U[k]), and the weight conversion of the
      componentwise bounds into M_g + s K_g (sympy);
  (3) section 3: the origin jets (U[k].Dg)_y(0) = c[k] g_y(0) and (L h)_y(0) = a0 c[h] on S1 Taylor polynomials, the
      substitution A_k T(k) = -F and the difference identity (symbolic, operators kept abstract), and q < 3/1897;
  (4) section 4: the two rational boxes and the quadratic identity (Fraction);
  (5) distance budget: sup over s of the ball radius mu(s) sqrt(s)/c_U for the baseline-gap balls and the c1
      frameworks, the implied L2 distances, and the comparison with the fixed-c L2 distance 0.0027197370 of d2 (N4-057);
  (6) the H-free variant on X_(s,w) (T2-R3 balls): matrices and exact sample boxes.
FLOAT part:
  (7) periodic FFT check of (4) and of (3) on S1 test functions (grid suprema, so FLOAT only).
"""
import sys
from fractions import Fraction as Q

import mpmath as mp
import sympy as sp
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 256


def A(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


# ---------------- (1) fractional commutator constants ----------------
print("(1) section 2, fractional commutator")
mp.mp.dps = 40
for sv, lam in ((mp.mpf(1) / 1024, mp.mpf(3)), (mp.mpf(1) / 2, mp.mpf("0.25")), (mp.mpf(1) / 4, mp.mpf(40))):
    al = sv / 2
    rhs = al / mp.gamma(1 - al) * mp.quad(lambda t: mp.e**(-t) * (1 - mp.e**(-t * lam)) * t**(-1 - al), [0, 1, mp.inf])
    lhs = (1 + lam) ** al - 1
    assert abs(lhs - rhs) < mp.mpf(10) ** -30
print("    (1 + lam)^(s/2) - 1 = (s/2)/Gamma(1 - s/2) int_0^oo e^-t (1 - e^(-t lam)) t^(-1-s/2) dt: agrees to 30 digits at"
      " (s, lam) = (1/1024, 3), (1/2, 1/4), (1/4, 40); with e^(-t |xi|^2) = FT of G_t this is the kernel kappa_s")
t, rho, s = sp.symbols("t rho s", positive=True)
G = sp.exp(-rho**2 / (4 * t)) / (4 * sp.pi * t)
m1 = sp.simplify(2 * sp.pi * sp.integrate(rho * G * rho, (rho, 0, sp.oo)))
m2 = sp.simplify(2 * sp.pi * sp.integrate(rho**2 * G * rho, (rho, 0, sp.oo)))
m0 = sp.simplify(2 * sp.pi * sp.integrate(G * rho, (rho, 0, sp.oo)))
print("    heat kernel G_t: mass", m0, ", int |z| G_t =", m1, ", int |z|^2 G_t =", m2)
assert m0 == 1 and sp.simplify(m1 - sp.sqrt(sp.pi * t)) == 0 and sp.simplify(m2 - 4 * t) == 0
pref = s / 2 / sp.gamma(1 - s / 2)
k1 = sp.simplify(pref * sp.integrate(sp.exp(-t) * t**(-1 - s / 2) * sp.sqrt(sp.pi * t), (t, 0, sp.oo), conds="none"))
k2 = sp.simplify(pref * sp.integrate(sp.exp(-t) * t**(-1 - s / 2) * 4 * t, (t, 0, sp.oo), conds="none"))
target1 = s * sp.sqrt(sp.pi) / 2 * sp.gamma((1 - s) / 2) / sp.gamma(1 - s / 2)
print("    int |z| kappa_s - (s sqrt(pi)/2) Gamma((1-s)/2)/Gamma(1-s/2) =", sp.simplify(sp.gammasimp(k1 - target1)),
      "; int |z|^2 kappa_s =", k2)
assert sp.simplify(sp.gammasimp(k1 - target1)) == 0 and sp.simplify(k2 - 2 * s) == 0
# constant 17: Gamma(x) <= 1/x + e^-1 (x in [1/4, 1/2)), Gamma(y) >= e^-1/y >= e^-1 (y in [3/4, 1)), sqrt(pi) < 9/5,
# e < 11/4: (s sqrt(pi)/2) Gamma ratio + 4 s <= s (9/10)(5)(11/4) + 4 s = (131/8) s
assert (4 + A(1) / arb(1).exp()) * arb(1).exp() < 5 * arb(1).exp()
assert arb.pi().sqrt() < A(Q(9, 5)) and arb(1).exp() < A(Q(11, 4))
c17 = Q(9, 10) * 5 * Q(11, 4) + 4
assert c17 == Q(131, 8) and c17 <= 17
for sv in (Q(1, 2), Q(1, 4), Q(1, 1024)):
    sa = A(sv)
    true = (arb.pi().sqrt() / 2 * ((1 - sa) / 2).gamma() / (1 - sa / 2).gamma() + 4)
    assert true < 17
    print(f"    s = {sv}: exact int |z| (1 + 2|z|) kappa_s / s = {true.str(8)} <= 131/8 <= 17")
yv, zv = sp.symbols("y z", nonnegative=True)
poly = sp.expand((1 + 2 * zv) ** 2 * (1 + 4 * yv**2) - (1 + 4 * (yv + zv) ** 2))
assert sp.expand(poly - (4 * zv * (1 - 2 * yv + 4 * yv**2) + 16 * yv**2 * zv**2)) == 0
print("    weight ratio: (1 + 2z)^2 (1 + 4y^2) - (1 + 4(y + z)^2) =", sp.factor(poly),
      "= 4z(1 - 2y + 4y^2) + 16 y^2 z^2 >= 0, so omega(X)/omega(X - z) <= (1 + 2|z|)^(4/5)")
# sharper: (1 + 2|z|)^(4/5) <= 1 + (8/5)|z| (concavity), Gamma decreasing on (0, 1], Gamma >= 1 on [3/4, 1]
print("    sharper constant (remark): int |z| (1 + (8/5)|z|) kappa_s <= c(s_max) s for 0 < s <= s_max,"
      " c(s_max) = (sqrt(pi)/2) Gamma((1 - s_max)/2) + 16/5:")
for smax in (Q(1, 2), Q(1, 1024)):
    cs_ = arb.pi().sqrt() / 2 * ((1 - A(smax)) / 2).gamma() + A(Q(16, 5))
    print(f"      s_max = {smax}: c = {cs_.str(8)}")
c_sharp_1024 = arb.pi().sqrt() / 2 * ((1 - A(Q(1, 1024))) / 2).gamma() + A(Q(16, 5))
assert c_sharp_1024 < A(Q(24, 5))

# ---------------- (2) multiplication bound ----------------
print("(2) section 2, multiplication bound")
x1, x2 = sp.symbols("xi1 xi2", real=True)
nr2 = x1**2 + x2**2
sym_R = [sp.I * x1 / sp.sqrt(nr2), sp.I * x2 / sp.sqrt(nr2)]
sym_U = [sp.simplify(-sym_R[0] * sym_R[1]), sp.simplify(sym_R[0] ** 2)]
sym_psi = sp.I * x1 / nr2                                     # psi = d_x (-Delta)^(-1) H0
assert sp.simplify(sym_U[0] - (-(sp.I * x2) * sym_psi)) == 0 and sp.simplify(sym_U[1] - (sp.I * x1) * sym_psi) == 0
assert all(sp.im(sp.simplify(u)) == 0 for u in sym_U)
assert sp.simplify(sym_U[0] ** 2 + sym_U[1] ** 2 - x1**2 / nr2) == 0
print("    symbols: U = (xi1 xi2, -xi1^2)/|xi|^2 = (-i xi2, i xi1) psi_hat/H0_hat, |U_hat|^2 = xi1^2/|xi|^2 <= 1,"
      " |psi_hat| = |xi1|/|xi|^2 <= 1/|xi|")
X, Y = sp.symbols("x y", real=True)
psi, g, gg = sp.Function("psi")(X, Y), sp.Function("g")(X, Y), sp.Function("gfac")(X, Y)
lhs = -sp.diff(psi, Y) * sp.diff(g, X) + sp.diff(psi, X) * sp.diff(g, Y)
rhs = sp.diff(psi * sp.diff(g, Y), X) + sp.diff(-psi * sp.diff(g, X), Y)
assert sp.simplify(lhs - rhs) == 0
V1, V2 = sp.Function("V1")(X, Y), sp.Function("V2")(X, Y)
div = lambda a, b: sp.diff(a, X) + sp.diff(b, Y)
assert sp.simplify(div(gg * V1, gg * V2) - (V1 * sp.diff(gg, X) + V2 * sp.diff(gg, Y)) - gg * div(V1, V2)) == 0
print("    U[H0].Dg = div(psi (g_y, -g_x)) (sympy), and div(g V) = V.Dg when div V = 0, so"
      " C = J^s(U[k].Dg) - U[J^s k].Dg = div([J^s, g] U[k]); ||div W||_H <= ||W||_2")
# weight conversion: componentwise bounds in (P, a, b, h), energy weights (1, 128, 512, 512 sqrt(b0)), e = weighted
P, a, b, h, ss = sp.symbols("P a b h s", nonnegative=True)
a1, a2, W2, W3, S1, S2, S3, S4 = sp.symbols("a1 a2 W2 W3 S1 S2 S3 S4", nonnegative=True)
b0 = sp.Rational(20, 21)
wts = [1, 128, 512, 512 * sp.sqrt(b0)]
main = [sp.Rational(9, 5) * a1 * P + 2 * W2 * a + W3 * b, a1 * a + a2 * b, a1 * b, a1 * h]
comm = [17 * ss * (S2 * P + 2 * S3 * a + S4 * b), 17 * ss * (S2 * a + S3 * b), 17 * ss * S2 * b, 17 * ss * S1 * b]
e1, e2, e3, e4 = sp.symbols("e1:5", nonnegative=True)
sub = {P: e1, a: e2 / 128, b: e3 / 512, h: e4 / (512 * sp.sqrt(b0))}
Mg = sp.Matrix([[sp.Rational(9, 5) * a1, W2 / 64, W3 / 512, 0], [0, a1, a2 / 4, 0], [0, 0, a1, 0], [0, 0, 0, a1]])
Kg = sp.Matrix([[17 * S2, 17 * S3 / 64, 17 * S4 / 512, 0], [0, 17 * S2, 17 * S3 / 4, 0], [0, 0, 17 * S2, 0],
                [0, 0, 17 * sp.sqrt(b0) * S1, 0]])
ev = sp.Matrix([e1, e2, e3, e4])
for i in range(4):
    assert sp.expand(wts[i] * main[i].subs(sub) - (Mg * ev)[i]) == 0
    assert sp.expand(wts[i] * comm[i].subs(sub) - ss * (Kg * ev)[i]) == 0
print("    weighted componentwise bounds equal (M_g e)_i and (s K_g e)_i exactly for i = 1..4 (sympy), so"
      " N_s(U[k].Dg) <= ||(M_g + s K_g) e||_2 <= B_g N_s(k)")
# norm bound certificate of the proof: sqrt(||.||_1 ||.||_inf) >= spectral norm (checked on a random nonnegative case)
import numpy as np
rng0 = np.random.default_rng(4)
fM = sp.lambdify((a1, a2, W2, W3, S1, S2, S3, S4), Mg + sp.Rational(1, 1024) * Kg, "numpy")
for _ in range(20):
    Mn = np.array(fM(*rng0.uniform(0, 50, 8)), dtype=float)
    assert np.linalg.norm(Mn, 2) <= np.sqrt(np.abs(Mn).sum(0).max() * np.abs(Mn).sum(1).max()) * (1 + 1e-12)
print("    sqrt(||M||_1 ||M||_inf) >= ||M||_2 on 20 random nonnegative instances (FLOAT sanity check of a standard fact)")

# ---------------- (3) section 3 ----------------
print("(3) section 3")
# S1 Taylor polynomials up to degree 3: f even in x, odd in y.  U1[k] odd in x, even in y; U2[k] even in x, odd in y.
cg = sp.symbols("g0:4")
cr = sp.symbols("r0:4")
ch = sp.symbols("h0:4")
p1, p2, q1, q2, u1, u2, w1_, w2_ = sp.symbols("p1 p2 q1 q2 u1 u2 w1 w2")
cc, c_rho, c_h, c_k = sp.symbols("c c_rho c_h c_k")
S1poly = lambda co: Y * (co[0] + co[1] * X**2 + co[2] * Y**2) + co[3] * Y**3 * X**2
gpol, rpol, hpol = S1poly(cg), S1poly(cr), S1poly(ch)
Uk = (X * (p1 + p2 * Y**2), Y * (c_k + q2 * X**2))          # U[k] with c[k] := d_y U2[k](0) = c_k
Ur = (X * (u1 + u2 * Y**2), Y * (c_rho + w2_ * X**2))       # U[rho_bar], c[rho_bar] = c_rho
Uh = (X * (w1_ + q1 * Y**2), Y * (c_h + p2 * X**2))         # U[h], c[h] = c_h
dy0 = lambda expr: sp.expand(sp.diff(expr, Y).subs({X: 0, Y: 0}))
prod = Uk[0] * sp.diff(gpol, X) + Uk[1] * sp.diff(gpol, Y)
assert dy0(prod) == c_k * cg[0]
Lh = (cc * X + Ur[0]) * sp.diff(hpol, X) + (cc * Y + Ur[1]) * sp.diff(hpol, Y) - hpol + Uh[0] * sp.diff(rpol, X) \
    + Uh[1] * sp.diff(rpol, Y)
val = dy0(Lh)
print("    (U[k].Dg)_y(0) =", dy0(prod), " (= c[k] g_y(0));  (L h)_y(0) =", sp.factor(val))
assert sp.expand(val - ((cc + c_rho - 1) * ch[0] + cr[0] * c_h)) == 0
print("    with c + c[rho_bar] = 1 and a0 = rho_y(0) = r0 this is a0 c[h], as used in section 3")
# substitution and difference identities with abstract linear operators (noncommutative symbols)
Lop, Ukop, Ulop, gop, Fop, Ainv_k, Ainv_l = sp.symbols("L Uk Ul g F Ak^-1 Al^-1", commutative=False)
# A_k = L + Uk (Uk stands for v -> U[k].Dv), D = F + L g, T(k) = g - A_k^-1 (D + Uk g)
# A_k T(k) = (L + Uk) g - (D + Uk g) = -F
AkT = sp.expand((Lop + Ukop) * gop - (Fop + Lop * gop + Ukop * gop))
assert AkT == -Fop
print("    A_k T(k) = (L + U[k].D) g - (F + L g + U[k].D g) = -F (symbolic)")
# A_k(T(k) - T(l)) = -F - (A_l + (U[k] - U[l]).D) T(l) = -F + F - U[k-l].D T(l)
print("    A_k (T(k) - T(l)) = -F - A_l T(l) - U[k - l].D T(l) = -U[k - l].D T(l) (linearity of k -> U[k])")
# q < 3/1897
pi_lb = Q(314159, 100000)
assert Q(25, 9) < pi_lb                                        # sqrt(pi) > 5/3, so c_s sqrt(s) < 1/(2 sqrt(pi)) < 3/10
assert Q(3, 10) * Q(1, 50) == Q(3, 500) and Q(3, 500) / (Q(19, 5) - Q(3, 500)) == Q(3, 1897)
print("    beta_r > 0 => r/sqrt(s) < mu/5 <= 1/50; c_s sqrt(s) = 1/(2 sqrt(pi (1 + s))) < 3/10; c_s r < 3/500;"
      " q <= c_s r/(19/5 - c_s r) < 3/1897 (exact)")

# ---------------- (4) section 4 boxes ----------------
print("(4) section 4, the two rational boxes at s = 2^-18 (sqrt s = 2^-9 exactly)")
s18 = Q(1, 2**18)
mu18 = Q(1, 10) - 4800 * s18
A18 = 5 * 2**9
mm, ee, BB, rr = sp.symbols("m eps B r")
mus, As = sp.symbols("mu A")
assert sp.expand((rr - mm) * (mus - As * rr) - BB * rr - ee - (-As * rr**2 + (mus + As * mm - BB) * rr - mus * mm - ee)) == 0
for (m_, e_, B_, r_, beta_claim, slack_claim) in ((Q(1, 2**17), Q(1, 2**23), Q(1, 100), Q(1, 2**16), Q(873, 20480),
                                                   Q(717, 13421772800)),
                                                  (Q(1, 2**16), Q(1, 2**25), Q(1, 200), Q(3, 2**17), Q(473, 20480),
                                                   Q(429, 13421772800))):
    beta = mu18 - A18 * r_
    slack = (r_ - m_) * beta - B_ * r_ - e_
    assert beta == beta_claim and slack == slack_claim and r_ >= m_
    # equivalence with (5): m + (eps + B r)/beta <= r
    assert m_ + (e_ + B_ * r_) / beta <= r_
    print(f"    m = {m_}, eps = {e_}, B = {B_}, r = {r_}: beta_r = {beta}, slack = {slack} (both as claimed);"
          f" (5) left side = {float(m_ + (e_ + B_ * r_) / beta):.6e} <= r = {float(r_):.6e}")
print("    quadratic identity (r - m)(mu - A r) - B r - eps = -A r^2 + (mu + A m - B) r - mu m - eps (sympy)")
# exact maximum over r of the slack: at r* = (mu + A m - B)/(2A), value ((mu - A m - B)^2 - 4 A B m)/(4A) - eps;
# r* >= m iff mu - A m - B >= 0, and then A r* < mu iff A m - B < mu (implied), so the box criterion is explicit
fq = (rr - mm) * (mus - As * rr) - BB * rr - ee
rstar = (mus + As * mm - BB) / (2 * As)
assert sp.simplify(sp.diff(fq, rr).subs(rr, rstar)) == 0
assert sp.simplify(fq.subs(rr, rstar) - (((mus - As * mm - BB) ** 2 - 4 * As * BB * mm) / (4 * As) - ee)) == 0
assert sp.simplify(rstar - mm - (mus - As * mm - BB) / (2 * As)) == 0 and sp.simplify(mus - As * rstar - (mus - As * mm + BB) / 2) == 0
print("    maximum admissible defect (exact): some r satisfies (5) iff mu - A m - B > 0 and"
      " eps <= eps_max = ((mu - A m - B)^2 - 4 A B m)/(4A), attained at r* = (mu + A m - B)/(2A),"
      " with beta_r* = (mu - A m + B)/2 (sympy)")
for (m_, B_) in ((Q(1, 2**17), Q(1, 100)), (Q(1, 2**16), Q(1, 200))):
    em = ((mu18 - A18 * m_ - B_) ** 2 - 4 * A18 * B_ * m_) / (4 * A18)
    print(f"      s = 2^-18, m = {m_}, B = {B_}: eps_max = {float(em):.6e} at r* = {float((mu18 + A18 * m_ - B_) / (2 * A18)):.6e}")
print(f"    g = 0 reduces (7) to N_s(F) <= r (mu - A r); at s = 2^-18 the best eps is mu^2/(4A) = {float(mu18**2 / (4 * A18)):.6e}")


# ---------------- (5) distance budget ----------------
print("(5) distance budget: every ball needs beta_r > 0, i.e. r < r_sup(s) = (mu0 - C s) sqrt(s)/c_U; the defect theorem"
      " (any g) keeps this constraint, since its solution h satisfies N(h) <= r")
d2_m = A(Q(27197370, 10**10))                                 # N4-057 (CONFIRMED by T4-048): ||h||_2 > 0.0027197370
frames = [("baseline-gap balls (A2, T4ALT)", Q(1, 10), 4800, Q(5), Q(1, 1024), 512),
          ("FW-T-TB-rebal-v1", Q(297, 1000), 4800, Q(5), Q(1, 1024), 512),
          ("FW-T-TB-sharp-v1 (T2-R2)", Q(297, 1000), 402, Q(8, 5), Q(1, 1024), 512),
          ("FW-T-T4L2-sharp-v1 (X_s, w = 2^14, 2^18)", Q(259, 1000), 401, Q(8, 5), Q(1, 1024), 512),
          ("FW-T-T4L2-sharpw-v1 (X_(s,w), w = 2^15, 2^20)", Q(97, 250), 397, Q(8, 5), Q(1, 1024), 1024)]
budget = {}
for name, mu0, Cb, cU, smax, sqw2 in frames:
    sstar = min(mu0 / (3 * Cb), smax)
    rsup = (A(mu0) - Cb * A(sstar)) * A(sstar).sqrt() / A(cU)
    # check that s* is the maximizer: derivative of (mu0 - C s) sqrt(s) vanishes at s = mu0/(3C) (interior here)
    assert mu0 / (3 * Cb) <= smax
    epsmax = ((A(mu0) - Cb * A(mu0 / (5 * Cb))) ** 2 * A(mu0 / (5 * Cb)).sqrt() / (4 * A(cU)))
    l2 = rsup / sqw2
    budget[name] = (rsup, l2)
    print(f"    {name}: s* = {sstar} = {float(sstar):.4e}, sup r = {rsup.str(5)}, L2 distance < sup r/{sqw2} ="
          f" {l2.str(4)}, d2 needs {d2_m.str(8)} = {(d2_m / l2).str(4)} times more; (g = 0 optimum eta = {epsmax.str(4)})")
    assert l2 < d2_m
rA2 = budget[frames[0][0]][0]
assert abs(rA2 - 1 / (9000 * arb(10).sqrt())) < A(Q(1, 10**40))
print("    baseline-gap balls: sup r = 1/(9000 sqrt 10) exactly (s* = 1/144000)")

# ---------------- (6) H-free variant on X_(s,w) ----------------
print("(6) H-free defect variant on X_(s,w) (T2-R3 balls; CLAIMED, c1-t2): e = (P, sqrt(w1) a, sqrt(w2) b)")
w1s, w2s = sp.symbols("w1 w2", positive=True)
mainw = [sp.Rational(9, 5) * a1 * P + 2 * W2 * a + W3 * b, a1 * a + a2 * b, a1 * b]
commw = [17 * (S2 * P + 2 * S3 * a + S4 * b), 17 * (S2 * a + S3 * b), 17 * S2 * b]
subw = {P: e1, a: e2 / sp.sqrt(w1s), b: e3 / sp.sqrt(w2s)}
wtw = [1, sp.sqrt(w1s), sp.sqrt(w2s)]
Mw = sp.Matrix([[sp.Rational(9, 5) * a1, 2 * W2 / sp.sqrt(w1s), W3 / sp.sqrt(w2s)],
                [0, a1, a2 * sp.sqrt(w1s / w2s)], [0, 0, a1]])
Kw = 17 * sp.Matrix([[S2, 2 * S3 / sp.sqrt(w1s), S4 / sp.sqrt(w2s)], [0, S2, S3 * sp.sqrt(w1s / w2s)], [0, 0, S2]])
evw = sp.Matrix([e1, e2, e3])
for i in range(3):
    assert sp.simplify(wtw[i] * mainw[i].subs(subw) - (Mw * evw)[i]) == 0
    assert sp.simplify(wtw[i] * commw[i].subs(subw) - (Kw * evw)[i]) == 0
assert sp.simplify(Mw.subs({w1s: 2**14, w2s: 2**18}) - Mg[:3, :3]) == sp.zeros(3, 3)
assert sp.simplify(Kw.subs({w1s: 2**14, w2s: 2**18}) - Kg[:3, :3]) == sp.zeros(3, 3)
print("    M^w_g =", Mw.tolist())
print("    K^w_g =", Kw.tolist(), "; at w = (2^14, 2^18) these are the top-left 3x3 blocks of M_g, K_g")
print("    closure: m + (eps + B r)/beta_r <= r, beta_r = mu0 - C' s - (8/5) r/sqrt(s); L2 contraction q <= c_s r/2")
for name, mu0, Cb, isq in (("FW-T-T4L2-sharpw-v1 box", Q(97, 250), 397, 72), ("FW-T-T4L2-sharp-v1 box", Q(259, 1000), 401, 88)):
    mu = mu0 - Cb * Q(1, isq * isq)
    Aw = Q(8, 5) * isq
    print(f"    {name}: s = 1/{isq*isq}, mu0 - C's = {mu} = {float(mu):.6f}, A = {Aw}; r < mu/A = {float(mu / Aw):.6e};"
          f" g = 0 best eps = mu^2/(4A) = {float(mu**2 / (4 * Aw)):.6e}")
    for m_, B_, r_ in ((Q(0), Q(0), mu / (2 * Aw)), (Q(1, 2**12), Q(1, 100), None), (Q(1, 2**10), Q(1, 100), None)):
        if r_ is None:                                         # rational r near the optimum (mu + A m - B)/(2A)
            ro = (mu + Aw * m_ - B_) / (2 * Aw)
            r_ = Q(int(ro * 10**6), 10**6)
        beta = mu - Aw * r_
        epsb = (r_ - m_) * beta - B_ * r_
        # best slack over r: ((mu - A m - B)^2 - 4 A B m)/(4 A) when mu - A m - B > 0 (c1-t4's alternate discriminant)
        best = ((mu - Aw * m_ - B_) ** 2 - 4 * Aw * B_ * m_) / (4 * Aw) if mu - Aw * m_ - B_ > 0 else None
        if best is None or best <= 0:
            print(f"      m = {m_}, B = {B_}: no admissible eps for any r (mu - A m - B = {float(mu - Aw * m_ - B_):.4f},"
                  f" best slack {float(best) if best is not None else float('nan'):.3e})")
            assert epsb <= 0
            continue
        assert beta > 0 and r_ >= m_ and epsb > 0 and epsb <= best
        cs_r = A(isq) / (2 * arb.pi().sqrt()) * A(r_)
        assert cs_r / 2 < 1
        print(f"      m = {m_}, B = {B_}, r = {r_}: beta_r = {float(beta):.6f}, admissible eps <= {epsb} ="
              f" {float(epsb):.6e}; q <= c_s r/2 <= {(cs_r / 2).str(4)}")

if "--no-float" in sys.argv:
    print("done (FLOAT part skipped)")
    sys.exit(0)

# ---------------- (7) FLOAT FFT checks ----------------

print("(7) FLOAT periodic FFT checks on [-L, L)^2 (grid suprema, periodic multipliers; not a proof)")
Lb, n = 16.0, 512
xs = -Lb + 2 * Lb * np.arange(n) / n
XX, YY = np.meshgrid(xs, xs, indexing="ij")
kx = 2 * np.pi * np.fft.fftfreq(n, d=2 * Lb / n)
KX, KY = np.meshgrid(kx, kx, indexing="ij")
K2 = KX**2 + KY**2
K2s = np.where(K2 == 0, 1.0, K2)
dA = (2 * Lb / n) ** 2
om = (1 + 4 * (XX**2 + YY**2)) ** 0.4
ft, ift = np.fft.fft2, lambda z: np.real(np.fft.ifft2(z))


def Js(f, sv):
    return ift(ft(f) * (1 + K2) ** (sv / 2))


def Uop(f):
    fh = ft(f)
    return ift(fh * KX * KY / K2s * (K2 > 0)), ift(-fh * KX**2 / K2s * (K2 > 0))


def d(f, i):
    return ift(ft(f) * 1j * (KX if i == 0 else KY))


def l2(f):
    return np.sqrt(np.sum(f**2) * dA)


def hnorm(f):
    fh = ft(f) * (K2 > 0) / np.sqrt(K2s)
    return np.sqrt(np.sum(np.abs(fh) ** 2) * dA / n**2)


def derivs(f, order):
    out = {(): f}
    for j in range(order):
        new = {}
        for idx, v in out.items():
            if len(idx) == j:
                for i in (0, 1):
                    new[idx + (i,)] = d(v, i)
        out.update(new)
    return out


def comps(f):
    """(P, a, b, h) of f = H0."""
    D = derivs(f, 2)
    P = np.sqrt(sum(l2(om * D[ix]) ** 2 for ix in D if len(ix) == 2))
    a = np.sqrt(sum(l2(D[ix]) ** 2 for ix in D if len(ix) == 1))
    return np.array([P, a, l2(f), hnorm(f)])


wE = np.array([1.0, 128.0, 512.0, 512 * np.sqrt(20 / 21)])
Ns = lambda f, sv: np.linalg.norm(wE * comps(Js(f, sv)))

# (4): ||omega [J^s, d] f||_2 <= c s ||omega D d||_inf ||f||_2
print("    (4) ratio ||omega [J^s, d] f||_2 / (s ||omega |D d| ||_inf ||f||_2) (bound 17; exact moment constant):")
tests = [(np.exp(-(XX**2 + YY**2) / 2) * (1 + XX**2), YY * np.exp(-((XX - 1) ** 2 + YY**2) / 3)),
         (np.tanh(YY) * np.exp(-(XX**2 + YY**2) / 10), np.exp(-(XX**2 + 4 * YY**2))),
         (np.sin(2 * XX) * np.exp(-(XX**2 + YY**2) / 4), XX * YY * np.exp(-(XX**2 + YY**2)))]
for sv in (1 / 4, 1 / 64, 1 / 1024):
    rats = []
    for dd, ff in tests:
        com = Js(dd * ff, sv) - dd * Js(ff, sv)
        Dd = np.sqrt(d(dd, 0) ** 2 + d(dd, 1) ** 2)
        rats.append(l2(om * com) / (sv * np.max(om * Dd) * l2(ff)))
    mom = float(mp.sqrt(mp.pi) / 2 * mp.gamma((1 - sv) / 2) / mp.gamma(1 - sv / 2) + 4)
    print(f"      s = {sv:.6g}: " + ", ".join(f"{q:.4f}" for q in rats) + f"  (int |z|(1 + 2|z|) kappa / s = {mom:.4f})")
    assert max(rats) < 17
# (3): N_s(U[k].Dg) <= B_g N_s(k)
print("    (3) ratio N_s(U[k].Dg)/(B_g N_s(k)), B_g = ||M_g + s K_g||_2 with grid suprema:")
r2 = XX**2 + YY**2
gs = [YY * np.exp(-r2 / 2) * (1 + 0.3 * XX**2), np.sin(YY) * np.exp(-r2 / 6), YY * (1 + YY**2) ** -1 * np.exp(-XX**2 / 5)
      * np.exp(-YY**2 / 10)]
ks = [(YY + 0.5 * YY**3 - XX**2 * YY) * np.exp(-(XX**2 + 2 * YY**2) / 3), YY * np.exp(-((r2) / 1.5)),
      np.sin(3 * YY) * np.cos(XX) * np.exp(-r2 / 4)]
for sv in (1 / 1024, 1 / 64):
    for gi, gfun in enumerate(gs):
        Dg = derivs(gfun, 4)
        sup = lambda ixs, wgt: max(np.max(wgt * np.abs(Dg[ix])) for ix in ixs)
        by = lambda j: [ix for ix in Dg if len(ix) == j]
        frob = lambda j, wgt: np.max(wgt * np.sqrt(sum(Dg[ix] ** 2 for ix in by(j))))
        a1n, a2n, W2n, W3n = frob(1, 1), frob(2, 1), frob(2, om), frob(3, om)
        S1n = sum(np.max(np.abs(Dg[ix])) for ix in by(1))
        S2n, S3n, S4n = (sum(np.max(om * np.abs(Dg[ix])) for ix in by(j)) for j in (2, 3, 4))
        Mn = np.array([[1.8 * a1n, W2n / 64, W3n / 512, 0], [0, a1n, a2n / 4, 0], [0, 0, a1n, 0], [0, 0, 0, a1n]])
        Kn = np.array([[17 * S2n, 17 * S3n / 64, 17 * S4n / 512, 0], [0, 17 * S2n, 17 * S3n / 4, 0], [0, 0, 17 * S2n, 0],
                       [0, 0, 17 * np.sqrt(20 / 21) * S1n, 0]])
        Bg = np.linalg.norm(Mn + sv * Kn, 2)
        out = []
        for kfun in ks:
            U1, U2 = Uop(kfun)
            pr = U1 * Dg[(0,)] + U2 * Dg[(1,)]
            out.append(Ns(pr, sv) / (Bg * Ns(kfun, sv)))
            # componentwise main-term check
            H0 = Js(kfun, sv)
            V1, V2 = Uop(H0)
            e = wE * comps(H0)
            main_c = wE * comps(V1 * Dg[(0,)] + V2 * Dg[(1,)])
            assert np.all(main_c <= Mn @ e * (1 + 1e-9))
        print(f"      s = {sv:.6g}, g{gi}: B_g = {Bg:.4f} (sK share {np.linalg.norm(sv * Kn, 2) / Bg:.3f}); ratios "
              + ", ".join(f"{q:.4f}" for q in out))
        assert max(out) < 1
print("    componentwise main terms <= (M_g e)_i in every case")
print("done")
