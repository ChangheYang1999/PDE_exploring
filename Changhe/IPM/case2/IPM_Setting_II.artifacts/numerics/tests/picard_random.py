"""Randomized one-step Picard map over richer input families (referee suggestion 4), with frozen-consistent tails.
Input zeta_0 = x (1 + sum_k A_k h_k(X)) f_p  with random smooth asymmetric terms h_k at random scales (y, xy, y^3,
x^2 y, bumps), random exponent p_in in [0.25, 0.8]; optional x-odd terms (rotating jet).  For each sample:
c0 = c[rho_0] (computed with the input's exterior exponents (p_in, p_in - 1)), one frozen transport step with
c_l = 1/2 + c0 (fixed jet) or the eigenvalue form (rotating), output moment c1 with exponents (q, q + p_in - 1).
Prints (c0, c1, b1, asymmetries, lres, rho_min of the output).  Nonnegativity of the INPUT rho_0 = zeta_0^2 holds
by construction (signed zeta)."""
import sys, math, time; sys.path.insert(0, 'code')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc
from zetasolve import weight_zeta, lin_lstsq, quad_weights
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R, nsamp, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
xodd = len(sys.argv) > 6 and sys.argv[6] == 'xodd'
d = Disc(Nr, Nth, R, K=2, tail='power2', tail_exps=(0.5, -0.5), device=dev)
th = d.theta_p[:, None]; r = d.r[None, :]
X, Y = r * torch.cos(th), r * torch.sin(th)
rng = np.random.default_rng(seed)

def strain(qz, cl, exps):
    d.tail_exps = exps
    out = d.zeta_residual_modes(qz, cl, return_all=True)
    U0, pxx, pxy, pyy = d.taylor_psi(out['p'])
    return float(pxy), float(pyy), out

def asym(rho_m):
    wq = quad_weights(d)
    mm = torch.arange(d.M + 1, device=dev); sgn = (-1.0) ** mm
    odd_x = 0.5 * (rho_m - sgn[:, None] * rho_m.conj()); odd_y = 0.5 * (rho_m - rho_m.conj())
    nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum())
    return float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum()) / nrm), float(torch.sqrt((odd_y.abs() ** 2 * wq[None, :]).sum()) / nrm)

print("# Nr %d Nth %d R %g nsamp %d seed %d xodd %s  %s" % (Nr, Nth, R, nsamp, seed, xodd, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())), flush=True)
for isamp in range(nsamp):
    p_in = rng.uniform(0.25, 0.8)
    fac = (1 + r ** 2) ** ((p_in / 2 - 1) / 2)
    g = torch.ones_like(X)
    nterms = rng.integers(1, 4)
    desc = []
    for k in range(nterms):
        A = rng.normal() * rng.choice([0.5, 1.0, 2.0, 4.0]); sc = rng.choice([0.3, 1.0, 3.0, 10.0])
        kind = rng.choice(['y', 'y3', 'x2y', 'bump', 'ysq'])
        rr2 = 1 + r ** 2 / sc ** 2
        if kind == 'y':     h = A * Y / rr2 ** 0.5 / sc
        elif kind == 'y3':  h = A * Y ** 3 / rr2 ** 1.5 / sc ** 3
        elif kind == 'x2y': h = A * X ** 2 * Y / rr2 ** 1.5 / sc ** 3
        elif kind == 'ysq': h = A * Y * X ** 2 / rr2 ** 1.5 / sc ** 3 * torch.sign(Y)   # non-smooth, exploratory
        else:
            x0, y0 = rng.normal() * sc, rng.normal() * sc
            h = A * torch.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / (0.3 * sc) ** 2)
        g = g + h; desc.append("%s(A=%.2f,sc=%.1f)" % (kind, A, sc))
    if xodd:
        A = rng.normal() * 0.5; sc = rng.choice([0.3, 1.0, 3.0])
        g = g + A * X * Y / (1 + r ** 2 / sc ** 2) / sc ** 2; desc.append("xodd(A=%.2f,sc=%.1f)" % (A, sc))
    z0 = X * g * fac
    qz = d.to_modes(z0) / d.rk
    c0, b0, out0 = strain(qz, torch.tensor(1.0 / p_in, device=dev), (p_in, p_in - 1.0))
    jm = 'rotating' if xodd else 'fixed'
    cl_new = 0.5 + (c0 if jm == 'fixed' else math.sqrt(c0 * c0 + b0 * b0))
    ax0, ay0 = asym(out0['rho_m'])
    if cl_new <= 1.0:
        print("sample %3d p_in=%.2f %s | c0=%.4f b0=%.1e cl=%.3f <= 1: outside S, skipped" % (isamp, p_in, " ".join(desc), c0, b0, cl_new), flush=True); continue
    Ur, Ut = out0['Ur'], out0['Ut']
    wz = weight_zeta(d, 1.0 / cl_new); res_w = 1.0 / wz ** 2
    def Flin(vz):
        qq = d.unpack(torch.cat([vz, torch.zeros(1, device=dev)]))[0]
        z_m, dz_m, tz_m = d.rho_modes(qq)
        z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
        Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
        Rz_m = d.to_modes(Rz) * res_w[None, :]
        zz0, zx, zy, _, _, _ = d.taylor_rho(qq)
        jet = torch.stack([zz0, zx - 1.0, zy]) if jm == 'fixed' else torch.stack([zz0, zx - 1.0])
        return torch.cat([Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1), jet])
    vz = d.pack(qz, torch.tensor(cl_new, device=dev))[:-1]
    try:
        L = jacfwd(Flin)(vz); b_ = Flin(torch.zeros_like(vz))
        sol, lres = lin_lstsq(L, -b_)
    except Exception as e:
        print("sample %3d: solve failed %s" % (isamp, str(e)[:60]), flush=True); continue
    qz1 = d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0]
    q = 1.0 / cl_new
    c1, b1, out1 = strain(qz1, torch.tensor(cl_new, device=dev), (q, q + p_in - 1.0))
    ax1, ay1 = asym(out1['rho_m'])
    Vr = cl_new * d.r[None, :] + Ur
    print("sample %3d p_in=%.2f %-60s | c0=%.4f b0=%.2e cl=%.3f asym_x0=%.2e asym_y0=%.2e | c1=%.4f b1=%.2e lres=%.0e asym_x1=%.2e asym_y1=%.2e minVr/r=%.2f zmax=%.1e" %
          (isamp, p_in, " ".join(desc)[:60], c0, b0, cl_new, ax0, ay0, c1, b1, lres, ax1, ay1, float((Vr / d.r[None, :]).min()), float(out1['zeta'].abs().max())), flush=True)
