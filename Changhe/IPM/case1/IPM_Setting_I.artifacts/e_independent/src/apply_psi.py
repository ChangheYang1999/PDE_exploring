"""Lead request 22:08Z: apply the doubly consistent characteristics map Psi ONCE to a disk-format state.
Psi: c_l chosen so that h(P) = 1 (bracketing + bisection), amplitude by the identity, transport from P (rho = C y on the
box of size delta), spatial renormalisation a(0) = 1. Reports c_l(Psi) vs input c_l, max/rms of |Psi(rho)-rho|/rho by radial
band and by 15-degree angular strip, and the rescaling factor.  Usage: python3 src/apply_psi.py <state.npz> <delta> [dt]"""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, batchmap
dev = 'cuda'
path, delta = sys.argv[1], float(sys.argv[2]); dt = float(sys.argv[3]) if len(sys.argv) > 3 else 0.005
d = np.load(path)
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
t0 = time.time()
bnew, cl_psi, info = batchmap.psi_batch(m, b[None], cl_lo=4.0, cl_hi=8.0, ngrid=17, nbis=45, dt=dt, delta=delta)
cl_psi = cl_psi[0].item(); bnew = bnew[0]
ratio = (bnew / b - 1.0)                       # Psi(rho)/rho - 1 pointwise (same grid; rho = pref * b)
ratio[0, :] = 0.0
rr = m.rad.rR.cpu().numpy(); thd = np.degrees(m.ang.theta_np)
print(f"[psi] {path}: N={m.N} M={m.M} R={float(d['R'])} dt={dt} delta={delta:g}: input c_l (identity) = {cl:.10f}; Psi: c_l (h(P)=1) = {cl_psi:.10f} (diff {cl_psi-cl:+.3e}); x* = {info['x_star'][0].item():.8f}, mu1 = {info['mu1'][0].item():.6f}, h(P)-1 = {(info['h'][0]-1).item():+.2e}; amplitude C = {info['C'][0].item():.8f}, a0(C=1) = {info['a0'][0].item():.8f}, rescale L = {info['Lsc'][0].item():.8f}; all trajectories entered: {bool(info['ok'][0])} ({time.time()-t0:.0f}s)", flush=True)
print("[psi] |Psi(rho)-rho|/rho by radial band (max, rms):", flush=True)
for name, (a_, b_) in {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), '100<r<=R': (100, np.inf)}.items():
    mask = torch.tensor((rr > a_) & (rr <= b_), device=dev)
    if mask.sum():
        x = ratio[mask]; print(f"       {name:10s} n={int(mask.sum())*m.M:6d} max {x.abs().max().item():.3e} rms {x.pow(2).mean().sqrt().item():.3e}", flush=True)
print("[psi] by 15-degree angular strip (max, rms over all r>0):", flush=True)
for lo in range(0, 90, 15):
    cols = torch.tensor((thd >= lo) & (thd < lo + 15), device=dev)
    x = ratio[1:][:, cols]; print(f"       [{lo:2d},{lo+15:2d}) deg: max {x.abs().max().item():.3e} rms {x.pow(2).mean().sqrt().item():.3e}", flush=True)
i, j = np.unravel_index(ratio.abs().argmax().item(), ratio.shape)
print(f"[psi] largest defect at r = {rr[i]:.4g}, theta = {thd[j]:.1f} deg: {ratio[i, j].item():+.3e}", flush=True)
import os
np.savez('' + os.path.basename(path).replace('.npz', f'_psi_d{delta:g}.npz'), bnew=bnew.cpu().numpy(), cl_psi=cl_psi, cl_in=cl, ratio=ratio.cpu().numpy(), delta=delta, dt=dt, x_star=info['x_star'][0].item())
