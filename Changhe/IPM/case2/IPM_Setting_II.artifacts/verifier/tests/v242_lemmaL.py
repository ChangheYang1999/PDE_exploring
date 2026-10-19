# V242: numerical test of referee result 47 Lemma L (local square) for nonlinear fields V = D X + N(X), D = diag(1/2, beta),
# N(0) = 0, DN(0) = 0, including the resonant case beta = 1 (1 = 2 * 1/2) with an x^2 term in V_2.
# u(Z) = lim exp(t/2) z_1(t, Z) along the backward flow z' = -V(z) (RK4, fixed step), then checks
# (1) V.grad u = u/2 (centred differences), (2) u - x = O(r^2), (3) rho := u^2 has the jet x^2 + O(r^3) and
# solves V.grad rho = rho, (4) uniqueness content: for an independently built solution rho2 (by transport of the
# initial data along forward orbits from a small circle) rho2 = u^2.
import numpy as np
def make(beta, a):
    def V(X):
        x, y = X[..., 0], X[..., 1]
        return np.stack([x / 2 + a[0] * x * y + a[1] * y**2 + a[2] * x**2,
                         beta * y + a[3] * x**2 + a[4] * x * y + a[5] * y**2], -1)
    return V
def u_of(V, Z, T=40.0, dt=0.01):
    z = np.array(Z, float); n = int(T / dt)
    f = lambda z: -V(z)
    for _ in range(n):
        k1 = f(z); k2 = f(z + dt / 2 * k1); k3 = f(z + dt / 2 * k2); k4 = f(z + dt * k3)
        z = z + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.exp(T / 2) * z[..., 0]
for beta, a in [(1.0, (0.3, 0.7, -0.4, 0.5, -0.2, 0.6)), (0.8, (0.5, -0.3, 0.2, 0.9, 0.4, -0.5)),
                (1.0, (0.0, 0.0, 0.0, 1.0, 0.0, 0.0))]:
    V = make(beta, a)
    print('beta', beta, 'N coeffs', a)
    rng = np.random.default_rng(1)
    for rad in [0.08, 0.04, 0.02, 0.01]:
        th = rng.uniform(0, 2 * np.pi, 8)
        Z = np.stack([rad * np.cos(th), rad * np.sin(th)], -1)
        h = 1e-5 * rad
        u0 = u_of(V, Z)
        ux = (u_of(V, Z + [h, 0]) - u_of(V, Z - [h, 0])) / (2 * h)
        uy = (u_of(V, Z + [0, h]) - u_of(V, Z - [0, h])) / (2 * h)
        Vz = V(Z)
        res = Vz[:, 0] * ux + Vz[:, 1] * uy - u0 / 2
        print('  r=%.3f  max|V.grad u - u/2|/r^2 = %.2e   max|u - x|/r^2 = %.3f   max|Du - (1,0)|/r = %.3f'
              % (rad, np.max(np.abs(res)) / rad**2, np.max(np.abs(u0 - Z[:, 0])) / rad**2,
                 np.max(np.hypot(ux - 1, uy)) / rad))
