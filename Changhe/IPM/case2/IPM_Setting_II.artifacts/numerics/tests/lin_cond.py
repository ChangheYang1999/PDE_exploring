"""Diagnose the linear transport solve (Picard step) at a given size: singular value spectrum, residual
vs SVD cutoff, GPU vs CPU solve, effect of weights."""
import sys, math, time; sys.path.insert(0, 'code')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc
from zetasolve import initial_zeta, weight_zeta
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev)
v = initial_zeta(d, 2.0, eps=0.0, ay=1.5)
qz, cl = d.unpack(v)
out = d.zeta_residual_modes(qz, cl, return_all=True)
c = float(d.taylor_psi(out['p'])[2]); cl_new = 0.5 + c
Ur, Ut = out['Ur'], out['Ut']
for wmode in ('r', 'none', 'r2'):
    if wmode == 'r': res_w = 1.0 / weight_zeta(d, 1.0 / cl_new)
    elif wmode == 'none': res_w = torch.ones_like(d.r)
    else: res_w = 1.0 / weight_zeta(d, 1.0 / cl_new) ** 2 * d.r.max() ** 0
    def Flin(vz):
        qq = d.unpack(torch.cat([vz, torch.zeros(1, device=dev)]))[0]
        z_m, dz_m, tz_m = d.rho_modes(qq)
        z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
        Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
        Rz_m = d.to_modes(Rz) * res_w[None, :]
        parts = [Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1)]
        z0, zx, zy, _, _, _ = d.taylor_rho(qq)
        return torch.cat(parts + [torch.stack([z0, zx - 1.0, zy])])
    vz = v[:-1]
    t0 = time.time(); L = jacfwd(Flin)(vz); b0 = Flin(torch.zeros_like(vz)); tj = time.time() - t0
    # check linearity: F(2v) - 2F(v) + F(0) = 0
    lin_err = float((Flin(2 * vz) - 2 * Flin(vz) + b0).abs().max())
    t0 = time.time(); U_, S_, Vh_ = torch.linalg.svd(L, full_matrices=False); ts = time.time() - t0
    S = S_.cpu().numpy()
    print("weights=%s  n=%d  jac %.1fs svd %.1fs  linearity err %.1e  smax=%.2e  s[-1]=%.2e s[-5]=%.2e s[-20]=%.2e s[-100]=%.2e" % (wmode, L.shape[1], tj, ts, lin_err, S[0], S[-1], S[-5], S[-20], S[-100]), flush=True)
    for cut in (1e-15, 1e-13, 1e-11, 1e-9, 1e-7):
        keep = S_ > S_[0] * cut
        sol = Vh_[keep].T @ ((U_[:, keep].T @ (-b0)) / S_[keep])
        res = L @ sol + b0
        qs = d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0]
        o2 = d.zeta_residual_modes(qs, torch.tensor(cl_new, device=dev), return_all=True)
        c1 = float(d.taylor_psi(o2['p'])[2])
        print("   cutoff %.0e: dropped %4d  |L sol + b| = %.2e  jet rows %.1e  zeta_max %.2e  rho_max %.2e  c1 = %.5f" % (cut, int((~keep).sum()), float(res.norm()), float(res[-3:].abs().max()), float(o2['zeta'].abs().max()), float(o2['rho'].abs().max()), c1), flush=True)
    # CPU reference solve (numpy lstsq, gelsd)
    if L.shape[1] <= 5000:
        Ln = L.cpu().numpy(); bn = (-b0).cpu().numpy()
        t0 = time.time(); soln, resid, rank, sv = np.linalg.lstsq(Ln, bn, rcond=1e-13); tc = time.time() - t0
        qs = d.unpack(torch.cat([torch.tensor(soln, device=dev), torch.zeros(1, device=dev)]))[0]
        o2 = d.zeta_residual_modes(qs, torch.tensor(cl_new, device=dev), return_all=True)
        print("   numpy gelsd rcond 1e-13: rank %d/%d  |L sol + b| = %.2e  rho_max %.2e  c1 = %.5f  (%.1fs)" % (rank, L.shape[1], float(np.linalg.norm(Ln @ soln - bn)), float(o2['rho'].abs().max()), float(d.taylor_psi(o2['p'])[2]), tc), flush=True)
