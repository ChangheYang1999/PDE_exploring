"""Lead request (notes 19:29Z item 2): for the sample-109 input rho_0 and its one-step output rho_1 = zeta_1^2:
(a) zeros of V other than the origin with eigenvalues of DV, (b) kappa vs the target 2(1-p)/(2-p), (c) does the extra
zero curve of zeta_1 pass through a near-zero of V_0?"""
import sys, math; sys.path.insert(0, 'code')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc
from zetasolve import weight_zeta, lin_lstsq, find_V_zeros, wq_r
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
p_in = 0.71; terms = [('y', 2.58, 10.0), ('x2y', -1.39, 1.0)]
d = Disc(Nr, Nth, R, K=2, tail='power2', tail_exps=(p_in, p_in - 1.0), device=dev)
th = d.theta_p[:, None]; r = d.r[None, :]
X, Y = r * torch.cos(th), r * torch.sin(th)
g = torch.ones_like(X)
for kind, A, sc in terms:
    rr2 = 1 + r ** 2 / sc ** 2
    if kind == 'y': g = g + A * Y / rr2 ** 0.5 / sc
    elif kind == 'x2y': g = g + A * X ** 2 * Y / rr2 ** 1.5 / sc ** 3
z0 = X * g * (1 + r ** 2) ** ((p_in / 2 - 1) / 2)
qz = d.to_modes(z0) / d.rk
thp = d.theta_p[:, None]; rr = d.r[None, :]
phi_r = -3 * rr ** -4 * torch.sin(3 * thp); phi_t = 3 * rr ** -4 * torch.cos(3 * thp); wr = wq_r(d)

def report(label, out, cl, zeta=None):
    U0, pxx, pxy, pyy = d.taylor_psi(out['p']); c = float(pxy)
    rho, Ur, Ut = out['rho'], out['Ur'], out['Ut']
    integ = (rho * (Ur * phi_r + Ut * phi_t)).mean(dim=0) * 2 * math.pi
    Q = float(torch.sum(integ * wr)); kap = Q / (math.pi * c * c)
    p = 1.0 / cl
    Vr = cl * rr + Ur; Vmag = torch.sqrt(Vr ** 2 + Ut ** 2) / rr
    zeros = find_V_zeros(d, out, cl, nmax=6)
    print("%s: c=%.4f cl=%.4f p=%.4f | kappa=%.4f target 2(1-p)/(2-p)=%.4f (=1-1/(2c)=%.4f) | min|V|/r=%.3f at r=%.3g th=%.2f" %
          (label, c, cl, p, kap, 2 * (1 - p) / (2 - p), 1 - 1 / (2 * c), float(Vmag.min()), float(d.r[int(torch.argmin(Vmag.min(dim=0).values))]), float(d.theta_p[int(torch.argmin(Vmag.min(dim=1).values))])))
    for zz in zeros:
        x_, y_, nv, det, tr = zz
        disc = tr * tr - 4 * det
        ev = "%.3f, %.3f" % ((tr - math.sqrt(disc)) / 2, (tr + math.sqrt(disc)) / 2) if disc >= 0 else "complex %.3f +- %.3fi" % (tr / 2, math.sqrt(-disc) / 2)
        kind = "saddle" if det < 0 else ("source" if tr > 0 else "sink")
        print("    zero of V at (%.4f, %.4f) r=%.4f |V|=%.1e  eigenvalues %s  (%s)" % (x_, y_, math.hypot(x_, y_), nv, ev, kind))
    if not zeros: print("    no zero of V found away from the origin (candidates with |V|/r < 0.25: none converged)")
    if zeta is not None:
        # zero curve of zeta: sign changes along theta at each radius; report the angle(s) at a few radii and the value of |V|/r there
        zc = zeta.cpu().numpy(); thv = d.theta_p.cpu().numpy(); Vm = Vmag.cpu().numpy()
        print("    zero set of zeta_1 (angles in degrees where zeta changes sign) and |V|/r there:")
        for j in [int(np.argmin(np.abs(d.r_np - rv))) for rv in (0.3, 1.0, 3.0, 10.0, 30.0, 100.0)]:
            col = zc[:, j]; s = np.where(np.sign(col[:-1]) * np.sign(col[1:]) < 0)[0]
            angs = ["%.1f(|V|/r=%.2f)" % (math.degrees(0.5 * (thv[i] + thv[i + 1])), 0.5 * (Vm[i, j] + Vm[i + 1, j])) for i in s]
            print("      r=%.3g: %s" % (d.r_np[j], " ".join(angs)))
    return c

out0 = d.zeta_residual_modes(qz, torch.tensor(1.0 / p_in, device=dev), return_all=True)
c0 = report("input rho_0 ", out0, 1.0 / p_in)
cl_new = 0.5 + c0
d.tail_exps = (p_in, p_in - 1.0)
out0 = d.zeta_residual_modes(qz, torch.tensor(cl_new, device=dev), return_all=True)
c0 = float(d.taylor_psi(out0['p'])[2]); cl_new = 0.5 + c0
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
print("frozen field V_0 = c_l X + W[rho_0] with c_l = %.4f (lres %.1e):" % (cl_new, lres))
# zeros of the frozen field V_0 (as used in the transport) -- report with out0 but using cl_new
c0b = report("frozen V_0  ", out0, cl_new, zeta=out1['zeta'])
c1 = float(d.taylor_psi(out1['p'])[2])
report("output rho_1 (its own V_1 = (1/2+c1) X + W[rho_1])", out1, 0.5 + c1)
