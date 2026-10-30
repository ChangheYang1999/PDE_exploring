"""FLOAT sanity check of T4-170 Theorem C (c1-t4 research/bounded_orbit_weight/PROOF.md, sha256 149da490...).

Toy instance (not an S1 background): V(X) = (x, 3/2 y) + (x y^2/(1+|X|^2)) e_x / 4, which is reflection
equivariant, V(0) = 0, V.X >= |X|^2 (m = 1).  theta_1 is a smooth even bump of height 0.8 on the annulus
1 <= |X| <= 2 (radial C^1 profile, angular factor), lambda = 0.5, so f = theta_1 - lambda <= -delta with
delta = 0.5 outside the annulus.  psi is computed by the finite-window formula
    psi(X) = max over 0 <= tau <= T_* of int_{-tau}^0 f(Phi_t X) dt
with RK4 backward integration.  Checks: 0 <= psi <= C; psi = 0 for |X| <= r1 and |X| >= R; the Lipschitz bound
(C3) against finite differences; g = V.grad psi >= f - tol at differentiability points (central differences);
osc psi equals the forward orbit budget (C4) on sampled orbits.  FLOAT only.
"""
import numpy as np

r1, r2, lam, H0 = 1.0, 2.0, 0.5, 0.8

def V(X):
    x, y = X[..., 0], X[..., 1]
    q = x * y * y / (1.0 + x * x + y * y) / 4.0
    return np.stack([x + q, 1.5 * y], axis=-1)

def theta1(X):
    x, y = X[..., 0], X[..., 1]
    r = np.sqrt(x * x + y * y)
    s = np.clip((r - r1) / (r2 - r1), 0.0, 1.0)
    rad = (np.sin(np.pi * s)) ** 2          # C^1, zero outside the annulus
    rr = x * x + y * y
    ang = 1.0 - 0.3 * np.where(rr > 0, (x * x - y * y) ** 2 / np.where(rr > 0, rr, 1.0) ** 2, 0.0)  # even, in [0.7, 1]
    return H0 * rad * ang

def f(X):
    return theta1(X) - lam

# constants of Theorem C
m = 1.0
# Lipschitz constant of V: DV = [[1 + dq/dx, dq/dy],[0, 3/2]]; bound numerically on a grid (FLOAT)
g1 = np.linspace(-40, 40, 801)
XX, YY = np.meshgrid(g1, g1)
P = np.stack([XX, YY], axis=-1)
eps = 1e-6
Jx = (V(P + np.array([eps, 0])) - V(P - np.array([eps, 0]))) / (2 * eps)
Jy = (V(P + np.array([0, eps])) - V(P - np.array([0, eps]))) / (2 * eps)
J = np.stack([Jx, Jy], axis=-1)
L = np.max(np.linalg.norm(J, ord=2, axis=(-2, -1)))
H = max(0.0, H0 - lam)
delta = lam  # theta_1 = 0 outside the annulus
T_ann = np.log(r2 / r1) / m
C = H * T_ann
R = r2 * np.exp(L * C / delta)
T_star = np.log(R / r1) / m
# Lipschitz constant of theta_1 (FLOAT, grid)
th = theta1(P)
gx = np.gradient(th, g1, axis=1)
gy = np.gradient(th, g1, axis=0)
Lip_th = np.max(np.sqrt(gx ** 2 + gy ** 2)) * 1.05
Lip_psi_bound = Lip_th * (np.exp(L * T_star) - 1.0) / L
print(f"L = {L:.6f}, H = {H}, T_ann = {T_ann:.6f}, C = {C:.6f}, R = {R:.6f}, T_* = {T_star:.6f}")
print(f"Lip(theta_1) <= {Lip_th:.6f} (FLOAT grid), (C3) Lipschitz bound {Lip_psi_bound:.4f}")

NT = 4000
dt = T_star / NT

def psi(X):
    """X: (n,2). Backward RK4 to time -T_*, running integral of f, max over the window."""
    Y = np.array(X, dtype=float)
    I = np.zeros(len(Y))
    best = np.zeros(len(Y))
    fy = f(Y)
    for _ in range(NT):
        k1 = -V(Y); k2 = -V(Y + 0.5 * dt * k1); k3 = -V(Y + 0.5 * dt * k2); k4 = -V(Y + dt * k3)
        Yn = Y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        fn = f(Yn)
        I = I + 0.5 * dt * (fy + fn)
        best = np.maximum(best, I)
        Y, fy = Yn, fn
    return best

rng = np.random.default_rng(1)
ok = True
# 1. bounds and support
rad = np.concatenate([rng.uniform(0, r1, 200), rng.uniform(r1, R, 600), rng.uniform(R, 2 * R, 200)])
ang = rng.uniform(0, 2 * np.pi, len(rad))
X = np.stack([rad * np.cos(ang), rad * np.sin(ang)], axis=-1)
p = psi(X)
c1 = (p.min() >= -1e-12) and (p.max() <= C + 1e-9)
c2 = np.all(p[rad <= r1] <= 1e-12) and np.all(p[rad >= R] <= 1e-12)
print(f"[{'PASS' if c1 else 'FAIL'}] 0 <= psi <= C: min {p.min():.3e}, max {p.max():.6f}, C {C:.6f}")
print(f"[{'PASS' if c2 else 'FAIL'}] psi = 0 on |X| <= r1 and |X| >= R (max there {max(p[rad<=r1].max(), p[rad>=R].max()):.2e})")
ok &= c1 and c2
print(f"(info) largest sampled radius with psi > 1e-12: {rad[p > 1e-12].max():.4f} (r2 = {r2}, R = {R:.4f})")
# 2. Lipschitz: finite differences on random pairs in the annulus r1/2 .. R
A = X[(rad > r1 / 2) & (rad < R)]
Dd = rng.normal(size=A.shape); Dd /= np.linalg.norm(Dd, axis=1, keepdims=True); Dd *= 1e-3
q = np.abs(psi(A + Dd) - psi(A)) / 1e-3
c3 = q.max() <= Lip_psi_bound
print(f"[{'PASS' if c3 else 'FAIL'}] (C3): max difference quotient {q.max():.4f} <= bound {Lip_psi_bound:.4f}")
ok &= c3
# 3. g = V.grad psi >= f at sampled points (central difference along V)
B = A[:300]
hstep = 1e-4
vb = V(B)
gb = (psi(B + hstep * vb) - psi(B - hstep * vb)) / (2 * hstep)
pb = psi(B)
viol = gb - f(B)
c4 = viol.min() >= -5e-3
print(f"[{'PASS' if c4 else 'FAIL'}] g >= theta_1 - lambda (sampled, tol 5e-3): min(g - f) = {viol.min():.3e}; "
      f"where psi > 1e-3: max |g - f| = {np.max(np.abs(viol[pb > 1e-3])) if np.any(pb > 1e-3) else 0:.3e}")
ok &= c4
# 4. (C4): sup psi versus forward orbit budgets sup_T int_0^T f(Phi_t Z) dt over start points Z in the annulus
Th, Rs = np.meshgrid(np.linspace(0, 2 * np.pi, 64, endpoint=False), np.linspace(r1, r2, 41))
Z = np.stack([(Rs * np.cos(Th)).ravel(), (Rs * np.sin(Th)).ravel()], axis=-1)
I = np.zeros(len(Z)); best = np.zeros(len(Z)); fz = f(Z); Y = Z.copy()
for _ in range(NT):
    k1 = V(Y); k2 = V(Y + 0.5 * dt * k1); k3 = V(Y + 0.5 * dt * k2); k4 = V(Y + dt * k3)
    Yn = Y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    fn = f(Yn); I = I + 0.5 * dt * (fz + fn); best = np.maximum(best, I); Y, fz = Yn, fn
c5 = abs(best.max() - p.max()) <= 0.02 * max(best.max(), 1e-9) + 1e-3
print(f"[{'PASS' if c5 else 'FAIL'}] (C4): max sampled forward budget {best.max():.6f} vs sampled max psi {p.max():.6f} "
      f"(both are lower estimates of the common supremum)")
ok &= c5
print("ALL PASS" if ok else "SOME FAIL")
