"""One-step Picard return map c -> c' for the family zeta_0 = x (1 + ay*y/sqrt(1+r^2)) (1+r^2)^{(p/2-1)/2},
with c_l = 1/2 + c(zeta_0^2) (consistent).  Also checks the linear transport solve."""
import sys, math; sys.path.insert(0, 'code')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc
from zetasolve import initial_zeta, weight_zeta
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev)

def strain(qz, cl):
    out = d.zeta_residual_modes(qz, cl, return_all=True)
    U0, pxx, pxy, pyy = d.taylor_psi(out['p'])
    return float(pxy), float(pyy), out

def picard_step(qz, cl, jet_mode='fixed'):
    c, b, out = strain(qz, cl)
    cl_new = 0.5 + c
    Ur, Ut = out['Ur'], out['Ut']
    wz = weight_zeta(d, 1.0/cl_new); res_w = 1.0/wz
    n = d.nunk() - 1
    def Flin(vz):
        qq = d.unpack(torch.cat([vz, torch.zeros(1, device=dev)]))[0]
        z_m, dz_m, tz_m = d.rho_modes(qq)
        z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
        Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
        Rz_m = d.to_modes(Rz) * res_w[None, :]
        parts = [Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1)]
        z0, zx, zy, _, _, _ = d.taylor_rho(qq)
        jet = torch.stack([z0, zx - 1.0, zy]) if jet_mode == 'fixed' else torch.stack([z0, zx - 1.0])
        return torch.cat(parts + [jet])
    vz = d.pack(qz, cl)[:-1]
    L = jacfwd(Flin)(vz)
    b0 = Flin(torch.zeros_like(vz))
    U_, S_, Vh_ = torch.linalg.svd(L, full_matrices=False)
    keep = S_ > S_[0] * 1e-13
    sol = Vh_[keep].T @ ((U_[:, keep].T @ (-b0)) / S_[keep])
    lin_res = (L @ sol + b0)
    qz_new = d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0]
    return qz_new, cl_new, c, b, float(lin_res.norm()), float(lin_res[-3:].abs().max()), float(S_[-1]/S_[0]), int((~keep).sum())

print("Nr %d Nth %d R %g unknowns %d" % (Nr, Nth, R, d.nunk()))
print("one-step return map:")
for ay in (0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0):
    v = initial_zeta(d, 2.0, eps=0.0, ay=ay)
    qz, cl = d.unpack(v)
    c0, b0, _ = strain(qz, cl)
    cl0 = 0.5 + c0
    if cl0 <= 1.0: 
        print("ay=%.2f c0=%.3f -> cl0=%.3f <= 1, skip" % (ay, c0, cl0)); continue
    qz1, cl1, c, b, lres, jetres, scond, ndrop = picard_step(qz, torch.tensor(cl0, device=dev))
    c1, b1, out1 = strain(qz1, torch.tensor(cl1, device=dev))
    rho1 = out1['rho']
    print("ay=%.2f  c0=%.4f cl0=%.4f | lin.res=%.1e jet.res=%.1e smin/smax=%.1e dropped=%d | c1=%.4f (cl=%.4f) b1=%.1e | rho1 min=%.2e max=%.2e zeta1 max=%.2e" %
          (ay, c0, cl0, lres, jetres, scond, ndrop, c1, 0.5+c1, b1, float(rho1.min()), float(rho1.max()), float(out1['zeta'].abs().max())))
