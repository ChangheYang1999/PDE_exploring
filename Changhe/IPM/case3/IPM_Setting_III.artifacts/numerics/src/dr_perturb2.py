"""dr_perturb2.py -- linearised growth of a core-localised bump about a DR state under the FULL linearisation J and under the TRANSPORT-ONLY linearisation
J0 (perturbation velocity feedback switched off: dflds = 0, dc = 0).  The far-end pseudo-modes are present in both (pure transport); the Rayleigh-Taylor
feedback -U[h].grad rho is only in J.  Reports the core norm max_{r <= Rc} |delta rho| against tau for both, the ratio, and the e-folding rates.
usage: python3 src/dr_perturb2.py state.pt|const N M C [r0=0.5 s=0.3 ks=0,2,6,10 tau_end=0.5 Rc=1]"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr
torch.set_default_dtype(torch.float64)
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
src, N, M, C = args[0], int(args[1]), int(args[2]), float(args[3]); dev = 'cuda'
r0 = float(kw.get('r0', 0.5)); s = float(kw.get('s', 0.3)); ks = [int(x) for x in kw.get('ks', '0,2,6,10').split(',')]; tau_end = float(kw.get('tau_end', 0.5)); Rc = float(kw.get('Rc', 1.0))
m = dr.DR(N, M, C, device=dev)
if src == 'const':
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = float(kw.get('a0', 1.0)); u = m.beta_to_u(beta0)
else:
    st = torch.load(src, weights_only=False); u = st['u'].to(dev)
du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item(); cw = info['cw'].item(); cx = info['cx'].item()
J = m.jacobian_dr(u); J0 = m.jacobian_dr(u, feedback=False)
ev = torch.linalg.eigvals(J); ev0 = torch.linalg.eigvals(J0); rad = max(ev.abs().max().item(), ev0.abs().max().item()); dt = 0.5 * 2.5 / rad
print(f"# {src} {N}x{M} C={C}: a0 {a0:.5f} c_w {cw:.5f} c_x {cx:.5f}; spectral radius full {ev.abs().max().item():.3e} (max Re {ev.real.max().item():+.3e}), transport-only {ev0.abs().max().item():.3e} (max Re {ev0.real.max().item():+.3e}); dtau {dt:.2e}; bump exp(-(ln(r/r0))^2/(2 s^2)) cos 2k theta, r0 = {r0}, s = {s}; core r <= {Rc}")
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin; th = m.angf.theta; g = torch.exp(-(torch.log(r / r0)) ** 2 / (2 * s ** 2)); core = (r <= Rc)
def field(v):
    bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * m.beta_full(v); return (r * w)[:, None] * sinf[None, :] * (bk @ m.C_f.T)
def rk4(Jm, v):
    k1 = Jm @ v; k2 = Jm @ (v + 0.5 * dt * k1); k3 = Jm @ (v + 0.5 * dt * k2); k4 = Jm @ (v + dt * k3); return v + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
print("#  k   tau   core|drho| full/initial   rate   | transport-only: core|drho|/initial   rate  | far (r>100) full/initial | theta_max/(pi/2) (full)")
for k in ks:
    F = g[:, None] * torch.cos(2 * k * th)[None, :]; v = m.project(F); v0 = v.clone()
    f = field(v); n_init = f[core].abs().max().item(); nf = n_init; n0 = n_init; tau = 0.0; next_rep = 0.05; tp = 0.0
    while tau < tau_end - 1e-12:
        v = rk4(J, v); v0 = rk4(J0, v0); tau += dt
        if tau >= next_rep - 1e-12:
            f = field(v); f0 = field(v0); nF = f[core].abs().max().item(); n0F = f0[core].abs().max().item(); far = f[r > 100].abs().max().item()
            idx = torch.argmax(f[core].abs()); j = idx.item() % f.shape[1]
            print(f"  {k:2d}  {tau:5.2f}  {nF/n_init:12.4e}  {math.log(nF/nf)/(tau-tp):+8.2f} | {n0F/n_init:12.4e}  {math.log(n0F/n0)/(tau-tp):+8.2f} | {far/n_init:10.2e} | {th[j].item()/(math.pi/2):.2f}", flush=True)
            nf, n0, tp = nF, n0F, tau; next_rep += 0.05
