"""Manufactured-solution tests of the modal full-plane inverse and of the radial basis derivatives."""
import torch, math, sys
sys.path.insert(0, '.')
from polarlib import *
device = dev()
P = Params(beta=3.0, L=1.0)
# radii: geometric-ish grid with many points, up to 12 (e^{-144} tail negligible)
N = 600
r = torch.linspace(0.0, 1.0, N + 1, dtype=DT, device=device)[1:]
r = 12.0 * r ** 2   # denser near 0
K = 1
def g1(t):  # (6t - 2t^2) e^{-t}, shape (...,1)
    return ((6 * t - 2 * t * t) * torch.exp(-t))[..., None]
def g2(t):
    return ((5 * t * t - t ** 3) * torch.exp(-t))[..., None]
tail = torch.zeros(1, dtype=DT, device=device)
for m, g, psi_exact, name in [(2, g1, lambda t: 0.5 * t * torch.exp(-t), 'psi1=(r^2/2)e^{-r^2}'),
                              (4, g2, lambda t: 0.25 * t * t * torch.exp(-t), 'psi2=(r^4/4)e^{-r^2}')]:
    for ngl in (4, 8, 16):
        Jin, Jout = modal_inverse(P, r, m, g, tail, ngl=ngl)
        psi = (Jin + Jout) / (2.0 * m)
        dpsi = (Jout - Jin) / (2.0 * r[:, None])
        t = r * r
        ex = psi_exact(t)
        # exact derivative
        dex = torch.autograd.functional.jacobian(lambda rr: psi_exact(rr * rr).sum(), r) if False else None
        rr = r.clone().requires_grad_(True)
        pe = psi_exact(rr * rr); pe.sum().backward(); dex = rr.grad
        err = (psi[:, 0] - ex).abs().max().item(); derr = (dpsi[:, 0] - dex).abs().max().item()
        print(f'{name} m={m} ngl={ngl}: max|psi err|={err:.3e}  max|dpsi err|={derr:.3e}  max|psi|={ex.abs().max().item():.3e}')
# c = Psi_xy(0) for test 1 should be 1:  c = lim J_out/(2 r^2)
Jin, Jout = modal_inverse(P, r, 2, g1, tail, ngl=16)
print('c from J_out at smallest r:', (Jout[0, 0] / (2 * r[0] ** 2)).item(), ' (exact 1)')

# --- basis consistency: c_row vs inverse at small r, and tail closure consistency (truncate at different r_N)
Kb = 12
for beta in (2.5, 3.0, 5.0):
    P = Params(beta=beta, L=1.0)
    crow = c_row(P, P.gamma_O, Kb).to(device)
    coef = torch.randn(Kb, dtype=DT, device=device)
    # inverse with radii to u_max = 1e3, 1e5 (q-uniform grid)
    out = []
    for umax in (1e3, 1e5, 1e7):
        qmax = P.q_of_u(torch.tensor(umax, dtype=DT))
        q = torch.linspace(0, qmax.item(), 2001, dtype=DT, device=device)[1:]
        rr = P.u_of_q(q) * P.L
        tail = basis_tail(P, rr[-1], 2, P.gamma_O, Kb)
        Jin, Jout = modal_inverse(P, rr, 2, basis_gfun(P, 2, P.gamma_O, Kb), tail, ngl=16)
        c_num = ((Jout @ coef)[0] / (2 * rr[0] ** 2)).item()
        out.append(c_num)
        # psi at a fixed radius r=1 : compare across domains
    print(f'beta={beta}: c_row={float(crow @ coef):.12f}  c from inverse (umax=1e3,1e5,1e7): {out}')
    # tail-less truncation error for comparison: drop the tail
    qmax = P.q_of_u(torch.tensor(1e3, dtype=DT)); q = torch.linspace(0, qmax.item(), 2001, dtype=DT, device=device)[1:]
    rr = P.u_of_q(q) * P.L
    Jin, Jout0 = modal_inverse(P, rr, 2, basis_gfun(P, 2, P.gamma_O, Kb), torch.zeros(Kb, dtype=DT, device=device), ngl=16)
    print(f'   c with tail dropped at u=1e3: {((Jout0 @ coef)[0] / (2 * rr[0] ** 2)).item():.12f}  (shows nonlocal truncation error)')

# --- radial basis derivative check by autograd
P = Params(beta=3.0, L=1.3)
r = torch.linspace(0.01, 50, 300, dtype=DT, device=device).requires_grad_(True)
for m, gamma in ((1, P.gamma_T), (5, P.gamma_T), (2, P.gamma_O), (8, P.gamma_O)):
    H, dH = radial_basis(P, r, m, gamma, 10)
    dH_auto = torch.zeros_like(H)
    for k in range(10):
        g, = torch.autograd.grad(H[:, k].sum(), r, retain_graph=True)
        dH_auto[:, k] = g
    print(f'basis m={m} gamma={gamma:.3f}: max rel deriv err = {((dH - dH_auto).abs().max() / dH_auto.abs().max()).item():.2e}')
