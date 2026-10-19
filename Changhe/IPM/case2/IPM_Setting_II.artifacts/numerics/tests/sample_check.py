"""Re-examine randomized inputs with c1 > c0 (runs/picard_random_40_24_100_s1.log) at several sizes, with the
cumulative moment C(R) = int_0^R f_3 r^-2 dr of the output and the modeled exterior part."""
import sys, math; sys.path.insert(0, 'code'); sys.path.insert(0, 'tests')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc, bary_weights
from zetasolve import weight_zeta, lin_lstsq
from bench_analytic import gl_xi, moment_c_interior
torch.set_default_dtype(torch.float64)
dev = 'cuda'
samples = {
 109: (0.71, [('y', 2.58, 10.0), ('x2y', -1.39, 1.0)]),
 81:  (0.75, [('ysq', 1.55, 1.0), ('y3', 3.72, 3.0)]),
 106: (0.69, [('ysq', -5.97, 1.0), ('y3', -1.48, 1.0), ('y', -0.27, 3.0)]),
 39:  (0.44, [('y', 3.13, 3.0), ('x2y', 0.26, 3.0), ('x2y', 3.57, 1.0)]),
 0:   (0.53, [('ysq', 1.32, 10.0), ('y3', 3.62, 1.0), ('x2y', 2.32, 3.0)]),
}
which = [int(s) for s in sys.argv[1].split(',')]
sizes = [(40, 24, 100.0), (64, 32, 300.0), (64, 32, 1000.0), (96, 48, 1000.0)]
if len(sys.argv) > 2:
    sizes = [tuple(float(v) if i == 2 else int(v) for i, v in enumerate(sz.split('x'))) for sz in sys.argv[2].split(',')]
for sid in which:
    p_in, terms = samples[sid]
    for (Nr, Nth, R) in sizes:
        d = Disc(Nr, Nth, R, K=2, tail='power2', tail_exps=(p_in, p_in - 1.0), device=dev)
        th = d.theta_p[:, None]; r = d.r[None, :]
        X, Y = r * torch.cos(th), r * torch.sin(th)
        g = torch.ones_like(X)
        for kind, A, sc in terms:
            rr2 = 1 + r ** 2 / sc ** 2
            if kind == 'y':     g = g + A * Y / rr2 ** 0.5 / sc
            elif kind == 'y3':  g = g + A * Y ** 3 / rr2 ** 1.5 / sc ** 3
            elif kind == 'x2y': g = g + A * X ** 2 * Y / rr2 ** 1.5 / sc ** 3
            elif kind == 'ysq': g = g + A * Y * X ** 2 / rr2 ** 1.5 / sc ** 3 * torch.sign(Y)
        z0 = X * g * (1 + r ** 2) ** ((p_in / 2 - 1) / 2)
        qz = d.to_modes(z0) / d.rk
        out0 = d.zeta_residual_modes(qz, torch.tensor(1.0 / p_in, device=dev), return_all=True)
        c0 = float(d.taylor_psi(out0['p'])[2]); b0 = float(d.taylor_psi(out0['p'])[3])
        c0_int = moment_c_interior(d, out0['rho_m'])
        cl_new = 0.5 + c0
        if cl_new <= 1.0:
            print("sample %d size %s: c0=%.4f -> cl<=1" % (sid, (Nr, Nth, R), c0)); continue
        Ur, Ut = out0['Ur'], out0['Ut']
        wz = weight_zeta(d, 1.0 / cl_new); res_w = 1.0 / wz ** 2
        def Flin(vz):
            qq = d.unpack(torch.cat([vz, torch.zeros(1, device=dev)]))[0]
            z_m, dz_m, tz_m = d.rho_modes(qq)
            z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
            Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
            Rz_m = d.to_modes(Rz) * res_w[None, :]
            zz0, zx, zy, _, _, _ = d.taylor_rho(qq)
            return torch.cat([Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1), torch.stack([zz0, zx - 1.0, zy])])
        vz = d.pack(qz, torch.tensor(cl_new, device=dev))[:-1]
        L = jacfwd(Flin)(vz); b_ = Flin(torch.zeros_like(vz)); sol, lres = lin_lstsq(L, -b_)
        qz1 = d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0]
        q = 1.0 / cl_new
        d.tail_exps = (q, q + p_in - 1.0)
        out1 = d.zeta_residual_modes(qz1, torch.tensor(cl_new, device=dev), return_all=True)
        c1 = float(d.taylor_psi(out1['p'])[2])
        c1_int = moment_c_interior(d, out1['rho_m'])
        # cumulative interior moment at a few radii: C(r) = -2 int_0^r Im rho_3 r^-2 dr via partial GL integration
        xi, w, P = gl_xi(d)
        q3 = P @ (out1['rho_m'][3] / d.rk[3])
        s = d.L ** 2 * (torch.exp(xi) - 1.0); rg = torch.sqrt(s)
        integ = -2.0 * q3.imag * d.L ** 2 * torch.exp(xi) / 2.0
        cum = torch.cumsum(w * integ, 0)
        def Cat(rv):
            i = int(torch.searchsorted(rg, torch.tensor(rv, device=dev)))
            return float(cum[min(i, len(cum) - 1)])
        print("sample %3d Nr=%3d Nth=%2d R=%6g | c0=%.4f (int %.4f) b0=%.1e cl=%.3f q=%.3f | lres=%.0e | c1=%.4f  C(1)=%.4f C(3)=%.4f C(10)=%.4f C(30)=%.4f C(R)=%.4f ext=%.4f | zeta1 max %.1e minVr/r %.2f" %
              (sid, Nr, Nth, R, c0, c0_int, b0, cl_new, q, lres, c1, Cat(1.0), Cat(3.0), Cat(10.0), Cat(30.0), c1_int, c1 - c1_int, float(out1['zeta'].abs().max()), float(((cl_new * d.r[None, :] + Ur) / d.r[None, :]).min())), flush=True)
