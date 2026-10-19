"""Kinematic test of the vdr transport discretization: fixed W = cl X + U, U = grad^perp psi_f,
psi_f = c x y exp(-r^2/16) (odd/odd, divergence free), rho_tau = rho - W.grad rho from rho0 = x^2 y (1+r^2/4)^{-1.2}.
Exact solution by characteristics: rho(tau, X) = e^tau rho0(Phi_{-tau} X)."""
import numpy as np, sys
from scipy.integrate import solve_ivp
from vdr import DR
cl, c = 1.4, 3 * 1.4 - 1
def Ucart(x, y):
    e = np.exp(-(x**2 + y**2) / 16)
    psx = c * y * e * (1 - x**2 / 8); psy = c * x * e * (1 - y**2 / 8)
    return -psy, psx
rho0 = lambda x, y: x**2 * y * (1 + (x**2 + y**2) / 4) ** (-1.2)
def run(N, M, tau_end=1.0, cfl=0.5):
    dr = DR(N=N, r0=1e-5, R=1e3, M=M)
    r = dr.r[:, None]; th = dr.th[None, :]
    X, Y = r * np.cos(th), r * np.sin(th)
    U1, U2 = Ucart(X, Y)
    Ur = np.cos(th) * U1 + np.sin(th) * U2; Ut = -np.sin(th) * U1 + np.cos(th) * U2
    spd = cl + Ur / r
    F = (rho0(X, Y) @ dr.P.T).T
    def rhs(F):
        rho = F.T @ dr.S; rho_t = (F * dr.ms[:, None]).T @ dr.C
        Fhi = F[:, -1:] * dr.rh_ratio[None, :] ** (1 / cl)
        Fe = np.concatenate([dr.jet_lo, F, Fhi], axis=1); idx = np.arange(dr.N) + 4
        Dp = sum(dr.wp[q] * Fe[:, idx + (q - 4)] for q in range(8)); Dm = sum(dr.wm[q] * Fe[:, idx + (q - 3)] for q in range(8))
        rho_u = np.where(spd > 0, Dp.T @ dr.S, Dm.T @ dr.S)
        return ((rho - spd * rho_u - (Ut / r) * rho_t) @ dr.P.T).T
    dt = cfl / max(np.abs(spd).max() / dr.g.h, np.abs(Ut / r).max() * M)
    nst = int(np.ceil(tau_end / dt)); dt = tau_end / nst
    for _ in range(nst):
        k1 = rhs(F); k2 = rhs(F + dt/2*k1); k3 = rhs(F + dt/2*k2); k4 = rhs(F + dt*k3)
        F = F + dt/6*(k1 + 2*k2 + 2*k3 + k4)
    return dr, F
def exact(pts, tau):
    def f(t, z):
        x, y = z[:len(z)//2], z[len(z)//2:]
        u1, u2 = Ucart(x, y)
        return -np.concatenate([cl * x + u1, cl * y + u2])
    sol = solve_ivp(f, (0, tau), np.concatenate([pts[:, 0], pts[:, 1]]), rtol=1e-12, atol=1e-14, method='DOP853')
    z = sol.y[:, -1]; n = len(pts)
    return np.exp(tau) * rho0(z[:n], z[n:])
for N, M in ((300, 15), (600, 31), (1200, 47)):
    dr, F = run(N, M)
    sel = [np.argmin(abs(dr.r - v)) for v in (0.01, 0.1, 0.5, 1, 2, 5, 10, 50, 200)]
    ths = np.array([0.1, 0.4, 0.8, 1.2, 1.5, 2.0, 2.9])
    pts = np.array([[dr.r[j] * np.cos(t), dr.r[j] * np.sin(t)] for j in sel for t in ths])
    num = np.array([sum(F[i, j] * np.sin(m * t) for i, m in enumerate(dr.ms)) for j in sel for t in ths])
    ex = exact(pts, 1.0)
    scale = np.array([np.abs(ex[a*len(ths):(a+1)*len(ths)]).max() for a in range(len(sel)) for _ in ths])
    err = np.abs(num - ex) / scale
    print(f"N={N} M={M}: max rel err (per-radius scaled) {err.max():.2e}; by radius:", " ".join(f"{err[a*len(ths):(a+1)*len(ths)].max():.1e}" for a in range(len(sel))))
