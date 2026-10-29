"""Checks for the v10 revision of MATHEMATICAL_FORMULATION.md (independent mathematical review, findings on that document).

Single-threaded SymPy; each check prints PASS or FAIL and the results are written to docrev_M_check_output.json.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import json
import time
import sympy as sp

t0 = time.process_time()
results = {}


def report(name, ok, detail=""):
    results[name] = {"pass": bool(ok), "detail": str(detail)}
    print(("PASS " if ok else "FAIL ") + name + (": " + str(detail) if detail else ""))


x, y, z, c, a = sp.symbols("x y z c a", real=True)
X = (x, y, z)
U = [sp.Function(n)(x, y, z) for n in ("U1", "U2", "U3")]
P = sp.Function("P")(x, y, z)


def grad(f):
    return [sp.diff(f, v) for v in X]


def div(V):
    return sum(sp.diff(V[i], X[i]) for i in range(3))


def adv(Wv, V):
    """(Wv . grad) V for a vector V."""
    return [sum(Wv[j] * sp.diff(V[i], X[j]) for j in range(3)) for i in range(3)]


def momentum(Uv, Pv):
    Wv = [c * X[i] + Uv[i] for i in range(3)]
    A = adv(Wv, Uv)
    G = grad(Pv)
    return [(1 - c) * Uv[i] + A[i] + G[i] for i in range(3)]


# Finding 1: divergence of the linear similarity terms.
ydotgradU = adv(list(X), U)
lhs = div([(1 - c) * U[i] + c * ydotgradU[i] for i in range(3)])
new_rhs = div(U) + c * sum(X[j] * sp.diff(div(U), X[j]) for j in range(3))
old_rhs = c * div(U) + c * sum(X[j] * sp.diff(div(U), X[j]) for j in range(3))
report("F1 div[(1-c)U + c y.grad U] = div U + c y.grad(div U)", sp.expand(lhs - new_rhs) == 0)
report("F1 v9 right side differs by (1-c) div U", sp.expand(lhs - old_rhs - (1 - c) * div(U)) == 0)

# Finding 2: axial translation. In the shifted variable y' = y - a e_z the term c y equals c y' + c a e_z.
M0 = momentum(U, P)
Wsh = [c * x + U[0], c * y + U[1], c * (z + a) + U[2]]
Msh = [(1 - c) * U[i] + adv(Wsh, U)[i] + grad(P)[i] for i in range(3)]
report("F2 plain translate: residual minus original equals c a d_z U",
       all(sp.expand(Msh[i] - M0[i] - c * a * sp.diff(U[i], z)) == 0 for i in range(3)))
Ua = [U[0], U[1], U[2] - c * a]
Pa = P + c * (1 - c) * a * (z + a)
Wa = [c * x + Ua[0], c * y + Ua[1], c * (z + a) + Ua[2]]
Ma = [(1 - c) * Ua[i] + adv(Wa, Ua)[i] + grad(Pa)[i] for i in range(3)]
report("F2 compensated map U(y - a e_z) - c a e_z, P(y - a e_z) + c(1-c) a z solves the equation",
       all(sp.expand(Ma[i] - M0[i]) == 0 for i in range(3)))

# Bernoulli residual identity for arbitrary U, P (no divergence condition used).
Wv = [c * X[i] + U[i] for i in range(3)]
H = sum(u * u for u in U) / 2 + P + c * sum(X[i] * U[i] for i in range(3)) + c * (2 * c - 1) * sum(v * v for v in X) / 2
bern = sum(Wv[i] * sp.diff(H, X[i]) for i in range(3)) - (2 * c - 1) * sum(w * w for w in Wv) - sum(Wv[i] * M0[i] for i in range(3))
report("(e) W.grad H - (2c-1)|W|^2 = W.M for arbitrary U, P", sp.expand(bern) == 0)

# Energy balance used in (f): div(W e + P U) = (5c-2) e + U.M + (e + P) div U.
e = sum(u * u for u in U) / 2
flux = [Wv[i] * e + P * U[i] for i in range(3)]
en = div(flux) - (5 * c - 2) * e - sum(U[i] * M0[i] for i in range(3)) - (e + P) * div(U)
report("(f) div(W |U|^2/2 + P U) = (5c-2)|U|^2/2 + U.M + (|U|^2/2 + P) div U", sp.expand(en) == 0)

# Finding 5: phi = z^2, q = 0, P = 0 satisfies the swirl equation but not the Bernoulli identity.
r = sp.symbols("r", positive=True)
phi = z ** 2
qf = sp.Integer(0)
Ur, Ut, Uz = -r * sp.diff(phi, z), r * qf, 2 * phi + r * sp.diff(phi, r)
Wr, Wz = c * r + Ur, c * z + Uz
advc = lambda f: Wr * sp.diff(f, r) + Wz * sp.diff(f, z)
Rq = qf + advc(qf) + 2 * (Ur / r) * qf
Mr = (1 - c) * Ur + advc(Ur) - Ut ** 2 / r
Mt = (1 - c) * Ut + advc(Ut) + Ur * Ut / r
Mz = (1 - c) * Uz + advc(Uz)
WM = sp.expand(Wr * Mr + Ut * Mt + Wz * Mz)
val = sp.factor(WM.subs({r: 0, z: 1}))
report("F5 phi=z^2, q=0, P=0: R_q = 0 identically", sp.simplify(Rq) == 0)
report("F5 W.M at r=0, z=1 equals 2(c+2)(c+5)", sp.expand(val - 2 * (c + 2) * (c + 5)) == 0, val)
# Cartesian cross-check of the same field: U = (-2xz, -2yz, 2z^2).
Uc = [-2 * x * z, -2 * y * z, 2 * z ** 2]
Mc = momentum(Uc, sp.Integer(0))
Wc = [c * X[i] + Uc[i] for i in range(3)]
WMc = sp.expand(sum(Wc[i] * Mc[i] for i in range(3)).subs({x: 0, y: 0, z: 1}))
report("F5 Cartesian cross-check of W.M at (0,0,1)", sp.expand(WMc - 2 * (c + 2) * (c + 5)) == 0 and div(Uc) == 0, WMc)

# Section 2 component equations: cylindrical forms against the Cartesian momentum equation, polynomial test fields.
s_ = sp.symbols("s_")
Phi = 3 * z + 2 * s_ * z ** 2 - 5 * s_ ** 2 * z ** 3 + 7 * z ** 4
Q = 1 + 4 * s_ - 3 * s_ * z ** 2 + 2 * z ** 3
Pp = 5 * s_ + 2 * s_ * z ** 2 - 3 * z ** 3
sub = {s_: x ** 2 + y ** 2}
Phx, Qx, Ppx = Phi.subs(sub), Q.subs(sub), Pp.subs(sub)
Ucart = [-x * sp.diff(Phi, z).subs(sub) - y * Qx, -y * sp.diff(Phi, z).subs(sub) + x * Qx,
         2 * Phx + 2 * (s_ * sp.diff(Phi, s_)).subs(sub)]
Mcart = momentum(Ucart, Ppx)
# cylindrical, phi(r, z) = Phi(r^2, z)
phr, qr, pr = Phi.subs(s_, r ** 2), Q.subs(s_, r ** 2), Pp.subs(s_, r ** 2)
Ur2, Ut2, Uz2 = -r * sp.diff(phr, z), r * qr, 2 * phr + r * sp.diff(phr, r)
Wr2, Wz2 = c * r + Ur2, c * z + Uz2
advc2 = lambda f: Wr2 * sp.diff(f, r) + Wz2 * sp.diff(f, z)
Mr2 = (1 - c) * Ur2 + advc2(Ur2) - Ut2 ** 2 / r + sp.diff(pr, r)
Mt2 = (1 - c) * Ut2 + advc2(Ut2) + Ur2 * Ut2 / r
Mz2 = (1 - c) * Uz2 + advc2(Uz2) + sp.diff(pr, z)
at = {x: r, y: 0}
ok = (sp.expand(Mcart[0].subs(at) - Mr2) == 0 and sp.expand(Mcart[1].subs(at) - Mt2) == 0
      and sp.expand(Mcart[2].subs(at) - Mz2) == 0 and sp.expand(div(Ucart)) == 0)
report("Section 2 cylindrical component equations agree with the Cartesian momentum equation (polynomial test fields)", ok)

# Finding 3: stream gauge and C^2 examples.
C0 = sp.symbols("C0")
phiC = C0 / r ** 2
report("F3 phi -> phi + C/r^2 leaves U^r and U^z unchanged",
       sp.simplify(-r * sp.diff(phiC, z)) == 0 and sp.simplify(2 * phiC + r * sp.diff(phiC, r)) == 0)
rho, th = sp.symbols("rho theta", positive=True)
pol = {x: rho * sp.cos(th), y: rho * sp.sin(th)}


def homogeneous_degree_ok(expr, deg):
    """expr is homogeneous of degree deg in (x, y): expr(polar) / rho^deg does not depend on rho."""
    e2 = sp.simplify(expr.subs(pol) / rho ** deg)
    return sp.simplify(sp.diff(e2, rho)) == 0


rr = sp.sqrt(x ** 2 + y ** 2)
V3 = [-y * rr ** 3, x * rr ** 3]
d3_ok = all(homogeneous_degree_ok(sp.diff(V3[k], *v), 1)
            for k in range(2) for v in [(x, x, x), (x, x, y), (x, y, y), (y, y, y)])
report("F3 q = r^3: U = (-y r^3, x r^3, 0) is divergence free; third derivatives homogeneous of degree 1 (continuous)",
       sp.simplify(sp.diff(V3[0], x) + sp.diff(V3[1], y)) == 0 and d3_ok)
V32 = [-y * rr ** sp.Rational(3, 2), x * rr ** sp.Rational(3, 2)]
d2_ok = all(homogeneous_degree_ok(sp.diff(V32[k], *v), sp.Rational(1, 2))
            for k in range(2) for v in [(x, x), (x, y), (y, y)])
qrr = sp.diff(r ** sp.Rational(3, 2), r, 2)
report("F3 q = r^(3/2): second derivatives of U homogeneous of degree 1/2 (C^2), q_rr = (3/4) r^(-1/2) unbounded",
       sp.simplify(sp.diff(V32[0], x) + sp.diff(V32[1], y)) == 0 and d2_ok
       and sp.simplify(qrr - sp.Rational(3, 4) * r ** sp.Rational(-1, 2)) == 0)

# Finding 6: a non-integer power of a negative circulation is not real.
report("F6 (-1)^(3/2) is not real", not sp.Pow(-1, sp.Rational(3, 2)).is_real, sp.Pow(-1, sp.Rational(3, 2)))

# Finding 7: transport of G = Gamma R^(alpha-1), given W.grad Gamma = (2c-1) Gamma and W.grad R = c R + U_R.
Gm, Rr, UR, al = sp.symbols("Gamma R U_R alpha")
WgradG = (2 * c - 1) * Gm * Rr ** (al - 1) + Gm * (al - 1) * Rr ** (al - 2) * (c * Rr + UR)
target = -(1 - al) * Gm * Rr ** (al - 1) * UR / Rr
diff7 = sp.expand(sp.powsimp(sp.expand((WgradG - target) / (Gm * Rr ** (al - 2))), force=True))
report("F7 W.grad G = -(1-alpha) G U_R/R with alpha = (1-c)/c (so W.grad G = 0 wherever G = 0)",
       sp.simplify(diff7.subs(al, (1 - c) / c)) == 0, diff7)

# Finding 11: equatorial relations from W_r d_r(r^2 q) = (2c-1) r^2 q and the equatorial swirl equation.
l, phz = sp.symbols("ell phi_z")
sol = sp.solve(sp.Eq((1 - 2 * phz) + (c - phz) * l, 0), phz)[0]
qq = sp.Function("q")(r)
dGam = sp.diff(r ** 2 * qq, r)
report("F11 d_r(r^2 q) = r q (2 + ell), so its sign is the sign of q times sign(2 + ell)",
       sp.simplify(dGam - r * qq * (2 + r * sp.diff(qq, r) / qq)) == 0)
report("F11 phi_z = (1 + c ell)/(2 + ell) and W_r = r(c - phi_z) = (2c-1) r/(2 + ell)",
       sp.simplify(sol - (1 + c * l) / (2 + l)) == 0 and sp.simplify(r * (c - sol) - (2 * c - 1) * r / (2 + l)) == 0)

# Finding 12: axis reconstruction. Exact rational exponents; z = u^m makes all powers integers.
uu = sp.symbols("u", positive=True)
Bs, Ds, As, Cs = sp.symbols("B D A C_star")
f12 = {}
for cval, m in ((sp.Rational(3, 5), 3), (sp.Rational(2, 3), 2), (sp.Rational(7, 10), 7)):
    k = 1 / cval
    zz = uu ** m
    qz = Bs * zz ** (-k) + Ds * zz ** (-2 * k)
    phiz = As * zz ** (1 - k)
    w = cval * zz + 2 * phiz
    # axis swirl equation w q' + (1 - 2 phi_z) q = 0 at order z^(-2k); derivative d/dz = (1/(m u^(m-1))) d/du
    ddz = lambda f: sp.diff(f, uu) / (m * uu ** (m - 1))
    eq = sp.expand(w * ddz(qz) + (1 - 2 * ddz(phiz)) * qz)
    co_k = sp.simplify(eq.coeff(uu, int(-m * k)))
    co_2k = sp.simplify(eq.coeff(uu, int(-2 * m * k)))
    # reconstruction with a finite part C_star
    integral = zz ** (k + 1) / (Bs * (k + 1)) - (Ds / Bs ** 2) * zz + Cs
    wrec = sp.expand((1 + cval) * qz * integral)
    co_lin = sp.simplify(wrec.coeff(uu, m))
    co_1mk = sp.simplify(wrec.coeff(uu, int(m * (1 - k))))
    co_mk = sp.simplify(wrec.coeff(uu, int(-m * k)))
    co_0 = sp.simplify(wrec.coeff(uu, 0))
    ok12 = (co_k == 0 and sp.simplify(co_2k.subs(Ds, -2 * As * Bs)) == 0 and co_lin == cval
            and sp.simplify(co_1mk + Ds / Bs) == 0 and sp.simplify(co_mk - (1 + cval) * Bs * Cs) == 0 and co_0 == 0
            and (1 - 2 * k) < -k)
    f12[str(cval)] = ok12
    report("F12 c=%s: D = -2AB; C_star enters w as (1+c) B C_star z^(-k), no constant term; 1-2k < -k" % cval, ok12,
           "z^(-k) coefficient %s, constant coefficient %s" % (co_mk, co_0))
# (w/q)' = (1+c)/q from w' = c + 2 phi_z and w q' = (2 phi_z - 1) q
wq, qv, phzv, wv = sp.symbols("wq qv phzv wv")
report("F12 (w/q)' = (1+c)/q", sp.simplify(((c + 2 * phzv) * qv - (2 * phzv - 1) * qv) / qv ** 2 - (1 + c) / qv) == 0)

# Finding 28: F(x, c) = (x - c)^2 has the family x = c, a singular x-derivative there, and F xi = 0 forces xi = 0 off it.
xs, cs, xi = sp.symbols("x_s c_s xi")
F28 = (xs - cs) ** 2
fam = sp.simplify(F28.subs(xs, cs)) == 0
sing = sp.simplify(sp.diff(F28, xs).subs(xs, cs)) == 0
forced = sp.solve(sp.Eq(F28 * xi, 0), xi)
report("F28 F = (x-c)^2: family x = c, D_x F = 0 on it, F xi = 0 with x != c forces xi = 0",
       fam and sing and forced == [0], forced)

results["CPU seconds"] = time.process_time() - t0
allpass = all(v["pass"] for k, v in results.items() if isinstance(v, dict))
results["all pass"] = allpass
print("ALL PASS" if allpass else "SOME CHECKS FAILED", "CPU %.2f s" % results["CPU seconds"])
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "docrev_M_check_output.json"), "w") as fh:
    json.dump(results, fh, indent=1)
