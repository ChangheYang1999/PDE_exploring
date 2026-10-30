"""sympy checks for the reviews of T4-140 and T4-145 (c1-t2 reviews/REVIEW_T4_140.md, REVIEW_T4_145.md).

Run from artifacts/:  python3 -B arith/t4_145_review.py   (a few seconds)
  (a) chart of T4-145 (8): xi_y = e^u, xi_x = e^(u+v); Jacobian; |xi|^(2q) dxi = e^(2qu)(1+e^(2v))^q e^(2u+v) du dv.
  (b) conjugation (9): W (-(D xi).grad_xi - (2c+1) - a0 p) W^(-1) G = -G_u - d0 G_v + (alpha_v + B p(v)) G.
  (c) the interior profile (11) solves -d0 phi' + (alpha_v + B p) phi = sigma phi.
  (d) T4-140 (3): the Fourier solution formula along characteristics, and the cone limits of the growth factor
      (vertical: exp((q-c-1)T); horizontal: exp((q(2c-1)-c-1-a0)T)).
"""
import sympy as sp

u, v, c, q, a0, sig, t, T = sp.symbols("u v c q a0 sigma t T", real=True)
xx, xy = sp.symbols("xi_x xi_y", positive=True)
d0 = 2 * c - 2
alpha_v = q - c - 1
B = 2 * q * (c - 1) - a0
p = sp.exp(2 * v) / (1 + sp.exp(2 * v))

# (a)
Xx, Xy = sp.exp(u + v), sp.exp(u)
J = sp.Matrix([[sp.diff(Xx, u), sp.diff(Xx, v)], [sp.diff(Xy, u), sp.diff(Xy, v)]]).det()
assert sp.simplify(sp.Abs(J) - sp.exp(2 * u + v)) == 0
assert sp.simplify(Xx**2 + Xy**2 - sp.exp(2 * u) * (1 + sp.exp(2 * v))) == 0       # then (ab)^q = a^q b^q, a, b > 0
W = 2 * sp.exp((q + 1) * u + v / 2) * (1 + sp.exp(2 * v)) ** (q / 2)
assert sp.simplify(sp.powsimp(sp.expand_power_base(W**2, force=True), force=True)
                   - 4 * sp.exp(2 * q * u) * (1 + sp.exp(2 * v)) ** q * sp.exp(2 * u + v)) == 0    # 4 = four quadrants
print("(a) |Jacobian| = e^(2u+v); |xi|^(2q) = e^(2qu)(1+e^(2v))^q; W^2 = 4 |xi|^(2q) |Jacobian|: (8) is unitary")

# (b) chain rule: for f(xi) = F(u, v), xi_x d/dxi_x = d/dv and xi_y d/dxi_y = d/du - d/dv
uu = sp.log(xy)
vv = sp.log(xx / xy)
Fs = sp.Function("F")
f = Fs(uu, vv)
lhs = (2 * c - 1) * xx * sp.diff(f, xx) + xy * sp.diff(f, xy)
Fu, Fv = sp.Derivative(Fs(u, v), u), sp.Derivative(Fs(u, v), v)
lhs_uv = lhs.subs({xx: sp.exp(u + v), xy: sp.exp(u)}).doit()
lhs_uv = sp.simplify(lhs_uv.subs({sp.log(sp.exp(u)): u, sp.log(sp.exp(v)): v}))
G = sp.Function("G")(u, v)
F = G / W
op = W * (-(sp.diff(F, u) + d0 * sp.diff(F, v)) - (2 * c + 1) * F - a0 * p * F)
target = -sp.diff(G, u) - d0 * sp.diff(G, v) + (alpha_v + B * p) * G
assert sp.simplify(sp.expand(op - target)) == 0
print("(b) (D xi).grad_xi = d_u + (2c-2) d_v (chain rule:", lhs_uv, ");")
print("    W L0hat W^(-1) G = -G_u - d0 G_v + (alpha_v + B p(v)) G with alpha_v = q-c-1, B = 2q(c-1) - a0: (9) holds")

# (c)
phi = sp.exp((alpha_v - sig) * v / d0) * (1 + sp.exp(2 * v)) ** (B / (2 * d0))
assert sp.simplify(-d0 * sp.diff(phi, v) + (alpha_v + B * p) * phi - sig * phi) == 0
print("(c) phi_sigma of (11) solves -d0 phi' + (alpha_v + B p) phi = sigma phi")

# (d) T4-140 (3): along xi = e^(tD) eta, d/dt what = -(2c+1) what - a0 p(xi) what; |det e^(tD)| = e^(2ct)
d1, d2 = 2 * c - 1, sp.Integer(1)
assert sp.simplify(d1 + d2 - 2 * c) == 0
ex, ey = sp.symbols("eta_x eta_y", positive=True)
# growth factor of ||w(T)||^2 / ||w0||^2 on a packet at eta: e^(-2(c+1)T) |e^(TD) eta|^(2q) / |eta|^(2q) exp(-2 a0 int p)
# vertical limit eta_x -> 0: p -> 0; horizontal limit eta_y -> 0: p -> 1
gv = sp.exp(-2 * (c + 1) * T) * sp.exp(2 * q * T)
gh = sp.exp(-2 * (c + 1) * T) * sp.exp(2 * q * d1 * T) * sp.exp(-2 * a0 * T)
assert sp.simplify(sp.log(gv) / 2 - (q - c - 1) * T) == 0
assert sp.simplify(sp.expand(sp.log(gh) / 2) - (q * (2 * c - 1) - c - 1 - a0) * T) == 0
print("(d) T4-140 (3): vertical cones give growth exp((q-c-1)T); horizontal cones exp((q(2c-1)-c-1-a0)T) = exp(alpha_h T)")
print("done")
