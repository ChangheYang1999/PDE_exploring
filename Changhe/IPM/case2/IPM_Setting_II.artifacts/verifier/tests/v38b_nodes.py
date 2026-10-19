"""v38b: checks for referee result 11 02-nodes and the zero-curve law of 03-jets.
Test field: V = DPhi^{-1} L(Phi) with Phi an area-preserving composition of shears and L = diag(alpha, beta),
alpha + beta = 2 ell.  Then div V = 2 ell, xi = Phi_1 solves V xi = alpha xi, and {xi = 0} is a curved line.
(The test field is not a Darcy velocity; the zero-curve law and the weak-coordinate construction only use
V xi = alpha xi and div V = 2 ell.)"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

res = []
def rep(ok, name, extra=""):
    res.append(bool(ok)); print(("PASS" if ok else "FAIL"), name, extra)
def chk(name, expr):
    e = sp.simplify(expr); rep(e == 0, name, "" if e == 0 else str(e))

x, y = sp.symbols('x y', real=True)
u, v = sp.symbols('u v', positive=True)
al, be, l, g = sp.symbols('alpha beta ell gamma', positive=True)

# (1) 02: linear-field rough example R = u^2 G(v/|u|^(2 beta)) solves V R = R for V = (u/2, beta v)
G = sp.Function('G')
R = u**2*G(v/u**(2*be))
chk("02 G-example transport (u>0)", sp.simplify(u/2*sp.diff(R, u) + be*v*sp.diff(R, v) - R))
Rv = sp.simplify(sp.diff(R, v))
chk("02 G-example R_v = u^(2-2beta) G'(tau)", sp.simplify(Rv - u**(2 - 2*be)*sp.Subs(sp.Derivative(G(sp.Symbol('z')), sp.Symbol('z')), sp.Symbol('z'), v/u**(2*be)).doit()))
# eta/|xi|^(beta/alpha) is invariant for V = (alpha u, beta v)
chk("02 orbit label invariant", sp.simplify(al*u*sp.diff(v/u**(be/al), u) + be*v*sp.diff(v/u**(be/al), v)))

# (2) pulled-back nonlinear source
a1, b1 = sp.Rational(7, 10), sp.Rational(-1, 2)
Phi1 = x + a1*y**2
Phi2 = y + b1*Phi1**2 + sp.Rational(1, 5)*Phi1**3
Phi = sp.Matrix([Phi1, Phi2])
J = Phi.jacobian([x, y])
chk("pullback map is area preserving", sp.simplify(J.det() - 1))
lv, gv = sp.Rational(3, 2), sp.Integer(2)       # ell, gamma (alpha = 1/gamma)
alv = 1/gv; bev = 2*lv - alv
L = sp.diag(alv, bev)
V = sp.simplify(J.inv()*L*Phi)
chk("pullback div V = 2 ell", sp.simplify(sp.diff(V[0], x) + sp.diff(V[1], y) - 2*lv))
xi = Phi1
chk("pullback V xi = alpha xi", sp.simplify(V[0]*sp.diff(xi, x) + V[1]*sp.diff(xi, y) - alv*xi))
DV0 = V.jacobian([x, y]).subs({x: 0, y: 0})
chk("pullback DV(0) = diag(alpha, beta)", (DV0 - L).norm())

# (3) zero-curve law on the curved zero line xi = 0 (x = -a1 y^2), two gamma values
for gam, lam_ in [(sp.Integer(2), sp.Rational(3, 2)), (sp.Rational(9, 2), sp.Rational(13, 10))]:
    alq = 1/gam; beq = 2*lam_ - alq
    Vq = sp.simplify(J.inv()*sp.diag(alq, beq)*Phi)
    grad = sp.Matrix([sp.diff(xi, x), sp.diff(xi, y)])
    fn = gam/2*sp.log(grad.dot(grad)) - gam/2*sp.log(Vq.dot(Vq))      # log(h_gamma/|V|^gamma)
    Dfn = Vq[0]*sp.diff(fn, x) + Vq[1]*sp.diff(fn, y)
    vals = []
    for yy in [-1.3, -0.4, 0.25, 0.9, 2.1]:
        vals.append(float(Dfn.subs({x: -a1*yy**2, y: yy}).evalf()))
    target = float(1 - 2*gam*lam_)
    err = max(abs(vv - target) for vv in vals)
    rep(err < 1e-10, f"03 zero-curve law d/ds log(h/|V|^g) = 1-2 g l on curved Gamma, g={gam}, l={lam_}",
        f"target {target:.6f}, max err {err:.2e}")
    # off the zero curve the law fails (sanity: it is a statement on Gamma only)
    off = float(Dfn.subs({x: 0.3, y: 0.2}).evalf())
    rep(abs(off - target) > 1e-3, "03 zero-curve law is specific to Gamma (off-curve value differs)", f"{off:.4f}")

# (4) 02: weak coordinate xi = lim e^{alpha t} (q_t)_1, q_t backward flow; compare with Phi_1
Vf = sp.lambdify((x, y), list(V), 'numpy')
def back(t, q): return [-c for c in Vf(q[0], q[1])]
errs = []
for X0 in [(0.05, 0.03), (-0.04, 0.06), (0.08, -0.05)]:
    T = 60.0
    sol = solve_ivp(back, (0, T), X0, rtol=1e-12, atol=1e-30, method='LSODA')
    est = np.exp(float(alv)*T)*sol.y[0, -1]
    exact = float(xi.subs({x: X0[0], y: X0[1]}))
    errs.append(abs(est - exact)/abs(exact))
rep(max(errs) < 1e-6, "02 weak coordinate limit formula reproduces the C^2 eigenfunction", f"rel err {max(errs):.2e}")

# (5) 02: two backward orbits on the same xi-level approach like e^{-beta t}; different levels like e^{-alpha t}
def sep(X0, Y0, T):
    s1 = solve_ivp(back, (0, T), X0, rtol=1e-12, atol=1e-40, method='LSODA', dense_output=True)
    s2 = solve_ivp(back, (0, T), Y0, rtol=1e-12, atol=1e-40, method='LSODA', dense_output=True)
    ts = np.linspace(T/2, T, 5)
    d = np.linalg.norm(s1.sol(ts) - s2.sol(ts), axis=0)
    return np.polyfit(ts, np.log(d), 1)[0]
yA, yB = 0.05, -0.03
xA = -float(a1)*yA**2 + 0.02; xB = -float(a1)*yB**2 + 0.02      # same xi = 0.02
rate_same = sep((xA, yA), (xB, yB), 12.0)
rate_diff = sep((xA, yA), (xA + 0.01, yA), 12.0)
rep(abs(rate_same + float(bev)) < 0.05, "02 same-leaf contraction rate = -beta", f"{rate_same:.4f} vs {-float(bev):.4f}")
rep(abs(rate_diff + float(alv)) < 0.05, "02 different-leaf rate = -alpha", f"{rate_diff:.4f} vs {-float(alv):.4f}")

# (6) 02: Hessian relation and C^3 classification (diagonal M): (m_i + m_j - 1) H_ij = 0
m1, m2 = sp.symbols('m1 m2')
H = sp.Matrix(2, 2, sp.symbols('h11 h12 h12b h22')); H[1, 0] = H[0, 1]
M = sp.diag(m1, m2)
E = M.T*H + H*M - H
chk("02 Hessian relation entrywise (m_i+m_j-1)H_ij", (E - sp.Matrix(2, 2, lambda i, j: ([m1, m2][i] + [m1, m2][j] - 1)*H[i, j])).norm())

print("SUMMARY: %d/%d PASS" % (sum(res), len(res)))
