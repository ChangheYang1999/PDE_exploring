"""reconstruction_audit.py -- symbolic audit (sympy) of the moving-centre self-similar reconstruction of PROMPT.md sec. 3 (shift 6; prompt sec. 4 item 5).
Checks, for generic smooth profiles (Omega, Theta, Psi) and generic beta, v0:
 (1) with tau = T - t, z_c(t) = z_* - (v0/beta) tau^beta, X = (z - z_c(t))/tau^beta and the ansatz
     omega = tau^-1 Omega(X), theta = tau^(beta-2) Theta(X), psi = tau^(2beta-1) Psi(X), u = (-psi_z2, psi_z1),
     the physical Boussinesq residuals equal tau^-2 [W.grad Omega + Omega - Theta_x] and tau^(beta-3) [W.grad Theta - (beta-2) Theta] with
     W = beta X + U(X) - v0, U = (-Psi_y, Psi_x), and -Lap_z psi = tau^-1 (-Lap_X Psi): the ansatz solves the PDE iff (B2-P) holds with v0 = U(0);
 (2) z_c'(t) = u(t, z_c(t)) holds iff v0 = U(0) (the centre is material exactly when the subtracted constant is the canonical centre velocity);
 (3) translation equivalence: X' = (z - z_*)/tau^beta = X - v0/beta; in X' the same fields solve the FIXED-centre system (P) with the field
     beta X' + U'(X'), whose stagnation point is X' = -v0/beta (= the material centre), not X' = 0 (the blow-up point) unless U(0) = 0 (B1);
 (4) the scaling family Theta_l = l Theta(X/l), Omega_l = Omega(X/l), U_l = l U(X/l), Psi_l = l^2 Psi(X/l) maps solutions of (B2-P) to solutions
     with the same beta, and a0 -> a0/l, v0 -> l v0.
Output: printed residual identities (all should simplify to 0)."""
import sympy as sp
tau, beta, l = sp.symbols('tau beta l', positive=True)      # tau = T - t > 0, beta > 0, scale l > 0; d/dt = -d/dtau
z1, z2, zs1, zs2, v01, v02 = sp.symbols('z1 z2 zs1 zs2 v01 v02', real=True)
x, y = sp.symbols('x y', real=True)
Om = sp.Function('Omega'); Th = sp.Function('Theta'); Ps = sp.Function('Psi')
zc1 = zs1 - v01 / beta * tau ** beta; zc2 = zs2 - v02 / beta * tau ** beta
X1 = (z1 - zc1) / tau ** beta; X2 = (z2 - zc2) / tau ** beta
omega = tau ** -1 * Om(X1, X2); theta = tau ** (beta - 2) * Th(X1, X2); psi = tau ** (2 * beta - 1) * Ps(X1, X2)
u1 = -sp.diff(psi, z2); u2 = sp.diff(psi, z1)
R_om = -sp.diff(omega, tau) + u1 * sp.diff(omega, z1) + u2 * sp.diff(omega, z2) - sp.diff(theta, z1)
R_th = -sp.diff(theta, tau) + u1 * sp.diff(theta, z1) + u2 * sp.diff(theta, z2)
R_ps = -(sp.diff(psi, z1, 2) + sp.diff(psi, z2, 2)) - omega
# profile-level expressions in X = (x, y)
U1 = -sp.diff(Ps(x, y), y); U2 = sp.diff(Ps(x, y), x)
W1 = beta * x + U1 - v01; W2 = beta * y + U2 - v02
P_om = W1 * sp.diff(Om(x, y), x) + W2 * sp.diff(Om(x, y), y) + Om(x, y) - sp.diff(Th(x, y), x)
P_th = W1 * sp.diff(Th(x, y), x) + W2 * sp.diff(Th(x, y), y) - (beta - 2) * Th(x, y)
P_ps = -(sp.diff(Ps(x, y), x, 2) + sp.diff(Ps(x, y), y, 2)) - Om(x, y)
sub = {x: X1, y: X2}
def check(name, expr):
    e = sp.simplify(sp.powsimp(sp.expand(expr), force=True))
    print(f"  {name}: {'0 (identity holds)' if e == 0 else e}")
print("(1) physical residuals minus tau-power x (B2-P) residuals (W = beta X + U - v0):")
check("omega equation: R_om - tau^-2 P_om", R_om - tau ** -2 * P_om.subs(sub, simultaneous=True))
check("theta equation: R_th - tau^(beta-3) P_th", R_th - tau ** (beta - 3) * P_th.subs(sub, simultaneous=True))
check("Poisson: R_ps - tau^-1 P_ps", R_ps - tau ** -1 * P_ps.subs(sub, simultaneous=True))
print("(2) material centre: z_c'(t) - u(t, z_c(t)) with u = tau^(beta-1) U(X), X(z_c) = 0:")
U1_0 = -sp.Derivative(Ps(x, y), y).subs({x: 0, y: 0}); U2_0 = sp.Derivative(Ps(x, y), x).subs({x: 0, y: 0})
c1 = sp.simplify(-sp.diff(zc1, tau) - tau ** (beta - 1) * U1_0); c2 = sp.simplify(-sp.diff(zc2, tau) - tau ** (beta - 1) * U2_0)
print(f"  component 1: {c1}  -> zero iff v01 = U_1(0) (= 0 by the x-parity of Psi)")
print(f"  component 2: {c2}  -> zero iff v02 = U_2(0)")
print(f"  limit: z_c - z_* = {sp.simplify(zc2 - zs2)} -> 0 as tau -> 0 (beta > 0): {sp.limit(zc2 - zs2, tau, 0) == 0}")
print("(3) translation equivalence (fixed limiting centre z_*): X' = (z - z_*)/tau^beta = X - v0/beta; fields Omega'(X') = Omega(X' + v0/beta) etc.")
xp, yp = sp.symbols('xp yp', real=True)
Omp = Om(xp + v01 / beta, yp + v02 / beta); Thp = Th(xp + v01 / beta, yp + v02 / beta); Psp = Ps(xp + v01 / beta, yp + v02 / beta)
U1p = -sp.diff(Psp, yp); U2p = sp.diff(Psp, xp)
Q_om = (beta * xp + U1p) * sp.diff(Omp, xp) + (beta * yp + U2p) * sp.diff(Omp, yp) + Omp - sp.diff(Thp, xp)      # system (P), no subtraction
Q_th = (beta * xp + U1p) * sp.diff(Thp, xp) + (beta * yp + U2p) * sp.diff(Thp, yp) - (beta - 2) * Thp
subp = {x: xp + v01 / beta, y: yp + v02 / beta}
check("(P) residual of the translate - (B2-P) residual: omega", Q_om - P_om.subs(subp, simultaneous=True))
check("(P) residual of the translate - (B2-P) residual: theta", Q_th - P_th.subs(subp, simultaneous=True))
Vp1 = beta * xp + U1p; Vp2 = beta * yp + U2p
print(f"  fixed-centre field at X' = -v0/beta (material centre): ({sp.simplify(Vp1.subs({xp: -v01 / beta, yp: -v02 / beta}))}, {sp.simplify(Vp2.subs({xp: -v01 / beta, yp: -v02 / beta}))}) -> vanishes iff v0 = U(0): the material centre is the stagnation point of (P)")
print(f"  fixed-centre field at X' = 0 (blow-up point z_*): ({sp.simplify(Vp1.subs({xp: 0, yp: 0}))}, {sp.simplify(Vp2.subs({xp: 0, yp: 0}))}) = U(v0/beta) -> nonzero in general; it is U(0) = 0 only in B1 (then v0 = 0 and both points coincide)")
print("(4) scaling family (same beta): Theta_l = l Theta(X/l), Omega_l = Omega(X/l), Psi_l = l^2 Psi(X/l), v0_l = l v0")
Oml = Om(x / l, y / l); Thl = l * Th(x / l, y / l); Psl = l ** 2 * Ps(x / l, y / l)
U1l = -sp.diff(Psl, y); U2l = sp.diff(Psl, x)
W1l = beta * x + U1l - l * v01; W2l = beta * y + U2l - l * v02
S_om = W1l * sp.diff(Oml, x) + W2l * sp.diff(Oml, y) + Oml - sp.diff(Thl, x)
S_th = W1l * sp.diff(Thl, x) + W2l * sp.diff(Thl, y) - (beta - 2) * Thl
S_ps = -(sp.diff(Psl, x, 2) + sp.diff(Psl, y, 2)) - Oml
subl = {x: x / l, y: y / l}
check("omega: S_om - P_om(X/l)", S_om - P_om.subs(subl, simultaneous=True))
check("theta: S_th - l P_th(X/l)", S_th - l * P_th.subs(subl, simultaneous=True))
check("Poisson: S_ps - P_ps(X/l)", S_ps - P_ps.subs(subl, simultaneous=True))
a0 = sp.symbols('a0'); print(f"  jet: Theta_l = l a0 (x/l)^2 + ... = (a0/l) x^2: a0 -> a0/l; U_l(0) = l U(0): v0 -> l v0; the centre strain Psi_xy(0) is scale invariant")
print("(5) local centre identities (PROMPT sec. 3) with Theta = a0 x^2 + ..., Omega = b0 x + ..., Psi = c x y + ... (W(0) = 0):")
a0s, b0s, cs = sp.symbols('a0 b0 c')
Th0 = a0s * x ** 2; Om0 = b0s * x; Ps0 = cs * x * y
W10 = beta * x + (-sp.diff(Ps0, y)); W20 = beta * y + sp.diff(Ps0, x)
e_th = sp.expand(W10 * sp.diff(Th0, x) + W20 * sp.diff(Th0, y) - (beta - 2) * Th0); e_om = sp.expand(W10 * sp.diff(Om0, x) + W20 * sp.diff(Om0, y) + Om0 - sp.diff(Th0, x))
print(f"  theta x^2 coefficient: {sp.factor(e_th.coeff(x, 2))} = 0 -> c = {sp.solve(e_th.coeff(x, 2), cs)[0]}")
print(f"  omega x coefficient: {sp.factor(e_om.coeff(x, 1))} = 0 -> b0 = {sp.simplify(sp.solve(e_om.coeff(x, 1).subs(cs, 1 + beta / 2), b0s)[0])}")
