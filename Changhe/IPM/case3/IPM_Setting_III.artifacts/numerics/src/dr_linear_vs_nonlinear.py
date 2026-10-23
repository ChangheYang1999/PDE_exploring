"""dr_linear_vs_nonlinear.py -- does the frozen-Jacobian growth (positive eigenvalues of J at the constant start) occur in the nonlinear flow?
(a) frozen linear: d/dtau v = J(u_0) v from a random coefficient perturbation; core (r <= 1) and far (r > 100) field norms against tau.
(b) nonlinear: two DR runs from u_0 and u_0 + eps v (eps = 1e-8), the difference's core/far norms against tau (same dtau).
usage: python3 src/dr_linear_vs_nonlinear.py N M C tau_end"""
import sys, math, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr
torch.set_default_dtype(torch.float64)
N, M, C, tau_end = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]); dev = 'cuda'
m = dr.DR(N, M, C, device=dev); beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = 1.0; u0 = m.beta_to_u(beta0)
J = m.jacobian_dr(u0); ev = torch.linalg.eigvals(J); rad = ev.abs().max().item(); dt = 0.5 * 2.5 / rad
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin; core = r <= 1; far = r > 100
def field(v):
    bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * m.beta_full(v); return (r * w)[:, None] * sinf[None, :] * (bk @ m.C_f.T)
torch.manual_seed(3); v = torch.randn(m.nu, device=dev); fv = field(v); v = v / fv.abs().max()      # field-normalised random perturbation
def rk4lin(v):
    k1 = J @ v; k2 = J @ (v + 0.5 * dt * k1); k3 = J @ (v + 0.5 * dt * k2); k4 = J @ (v + dt * k3); return v + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
def rk4nl(u):
    k1 = m.rhs(u); k2 = m.rhs(u + 0.5 * dt * k1); k3 = m.rhs(u + 0.5 * dt * k2); k4 = m.rhs(u + dt * k3); return u + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
eps = 1e-8; ua = u0.clone(); ub = u0 + eps * v; vl = v.clone(); tau = 0.0; nxt = 0.25
f0 = field(v); c0 = f0[core].abs().max().item(); a0 = f0[far].abs().max().item()
print(f"# {N}x{M} C={C} constant start: max Re J {ev.real.max().item():+.3e}, radius {rad:.3e}, dtau {dt:.2e}; perturbation field-normalised (max 1; core {c0:.2e}, far {a0:.2e}); eps = {eps}")
print("#  tau | frozen linear: core |dv| / far |dv|  (relative to initial core/far) | nonlinear difference/eps: core / far | nonlinear |rho_tau|inf")
while tau < tau_end - 1e-12:
    vl = rk4lin(vl); ua = rk4nl(ua); ub = rk4nl(ub); tau += dt
    if tau >= nxt - 1e-12:
        fl = field(vl); fd = field(ub - ua) / eps; _, info = m.rhs(ua, want=True)
        rt = ((r * w)[:, None] * sinf[None, :] * info['F']).abs().max().item()
        print(f"  {tau:5.2f} | {fl[core].abs().max().item()/c0:10.3e} / {fl[far].abs().max().item()/a0:10.3e} | {fd[core].abs().max().item()/c0:10.3e} / {fd[far].abs().max().item()/a0:10.3e} | {rt:.3e}", flush=True)
        nxt += 0.25
