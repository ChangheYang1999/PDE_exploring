"""Return map of the Picard (characteristic fixed point) iteration for several initial families, with
iteration, at a given resolution.  Prints c_k = psi_xy(0)[rho_k], b_k, cl_k and asymmetry fractions."""
import sys, math, time; sys.path.insert(0, 'code')
import torch, numpy as np
from torch.func import jacfwd
from ipm2polar import Disc
from zetasolve import weight_zeta, quad_weights
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
niter = int(sys.argv[4]) if len(sys.argv) > 4 else 3
d = Disc(Nr, Nth, R, K=2, tail='power2', tail_exps=(0.5, -1.5), device=dev)
th = d.theta_p[:, None]; r = d.r[None, :]
X, Y = r * torch.cos(th), r * torch.sin(th)

def fam(name, a, p, eps=0.0, seed=0):
    fac = (1 + r ** 2) ** ((p / 2 - 1) / 2)
    if name == 'A':   z = X * (1 + a * Y / (1 + r ** 2) ** 0.5) * fac
    elif name == 'B': z = X * (1 + a * Y / (1 + r ** 2)) * fac
    elif name == 'C': z = X * (1 + a * Y / (1 + r ** 2) ** 0.5 + 0.3 * a * X * Y / (1 + r ** 2)) * fac
    elif name == 'D': z = X * (1 + a * Y / (1 + r ** 2 / 9) ** 0.5) * fac
    elif name == 'E': z = X * (1 + a * torch.tanh(Y)) * fac
    else: raise ValueError
    if eps:
        g = torch.Generator().manual_seed(seed); c = torch.randn(5, generator=g).to(dev)
        z = z + eps * ((c[0]*X**2 + c[1]*Y**2 + c[2]*X*Y) * (1+r**2)**((p/2-2)/2) + (c[3]*X**3 + c[4]*Y**3)*(1+r**2)**((p/2-3)/2))
    return d.to_modes(z) / d.rk

def strain(qz, cl, exps=None):
    if exps is not None: d.tail_exps = exps
    out = d.zeta_residual_modes(qz, cl, return_all=True)
    U0, pxx, pxy, pyy = d.taylor_psi(out['p'])
    return float(pxy), float(pyy), out

def asym(rho_m):
    wq = quad_weights(d)
    mm = torch.arange(d.M + 1, device=dev); sgn = (-1.0) ** mm
    odd_x = 0.5 * (rho_m - sgn[:, None] * rho_m.conj()); odd_y = 0.5 * (rho_m - rho_m.conj())
    nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum())
    return float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum()) / nrm), float(torch.sqrt((odd_y.abs() ** 2 * wq[None, :]).sum()) / nrm)

def picard_step(qz, cl, jet_mode, p_in):
    c, b, out = strain(qz, cl, (p_in, p_in - 1.0))
    cl_new = 0.5 + (c if jet_mode == 'fixed' else math.sqrt(c*c + b*b))
    Ur, Ut = out['Ur'], out['Ut']
    wz = weight_zeta(d, 1.0 / max(cl_new, 0.3)); res_w = 1.0 / wz ** 2
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
    L = jacfwd(Flin)(vz); b0 = Flin(torch.zeros_like(vz))
    from zetasolve import lin_lstsq
    sol, lres = lin_lstsq(L, -b0)
    return d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0], cl_new, c, b, lres

print("# Nr %d Nth %d R %g unknowns %d  %s" % (Nr, Nth, R, d.nunk(), time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())), flush=True)
cases = [('A', 1.5, 0.5, 0.0, 'fixed'), ('A', 3.0, 0.5, 0.0, 'fixed'), ('A', 1.5, 0.3, 0.0, 'fixed'), ('A', 1.5, 0.8, 0.0, 'fixed'),
         ('B', 3.0, 0.5, 0.0, 'fixed'), ('C', 1.5, 0.5, 0.0, 'rotating'), ('D', 1.0, 0.5, 0.0, 'fixed'), ('E', 1.0, 0.5, 0.0, 'fixed'),
         ('A', 1.5, 0.5, 0.2, 'rotating'), ('A', 3.0, 0.5, 0.5, 'rotating')]
for name, a, p, eps, jm in cases:
    qz = fam(name, a, p, eps)
    c0, b0, out0 = strain(qz, torch.tensor(1.0 / p, device=dev), (p, p - 1.0))   # input exterior exponents
    cl = 0.5 + (c0 if jm == 'fixed' else math.sqrt(c0*c0 + b0*b0))
    ax, ay_ = asym(out0['rho_m'])
    line = "fam %s a=%.2f p=%.1f eps=%.1f jet=%s | k=0: c=%.4f b=%.1e cl=%.4f asym_x=%.1e asym_y=%.2e" % (name, a, p, eps, jm, c0, b0, cl, ax, ay_)
    if cl <= 1.0:
        print(line + "  (cl<=1 at start: outside S, skipped)", flush=True); continue
    cl_t = torch.tensor(cl, device=dev)
    for k in range(1, niter + 1):
        try:
            qz, cl_new, c, b, lres = picard_step(qz, cl_t, jm, p)
        except Exception as e:
            line += " | k=%d: step failed (%s)" % (k, str(e)[:40]); break
        qo = 1.0 / cl_new
        c1, b1, out1 = strain(qz, torch.tensor(cl_new, device=dev), (qo, qo + p - 1.0))
        ax, ay_ = asym(out1['rho_m'])
        line += " | k=%d: c=%.4f b=%.1e cl=%.4f lres=%.0e asym_x=%.1e asym_y=%.2e rho_max=%.1e" % (k, c1, b1, 0.5 + c1, lres, ax, ay_, float(out1['rho'].abs().max()))
        cl_t = torch.tensor(max(0.5 + c1, 1.0001), device=dev)   # keep the velocity law in S for the next step
        if 0.5 + c1 <= 1.0:
            line += " [cl<=1: next step uses cl=1.0001]"
    print(line, flush=True)
