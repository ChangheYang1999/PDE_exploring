"""Dynamic rescaling probe in the zeta formulation (notes of the lead analyst 2026-10-17T18:12Z and 18:39Z):
    zeta_s = -( V . grad zeta - zeta/2 ),   V = c_l(s) X + W[zeta^2],   c_l(s) = 1/2 + c(s),  c = psi_xy(0)[zeta^2],
(equivalently rho_s = rho - V.grad rho for rho = zeta^2).  Explicit RK4 in s on the spectral representation.
Monitors c(s), b = psi_yy(0), the jet of zeta, the exact moment law dc/ds = c(1/2 - c) + Q/pi with
Q = int rho W.grad(r^-3 sin 3th) dX (quadrature on the grid + power-law exterior estimate), the x-odd fraction.
Runs while c_l > cl_min (class S; self-consistent tail exponents (q, 2q-1), q = 1/c_l); stops otherwise.
Usage: python3 dynrescale.py --Nr 40 --Nth 24 --R 100 --ay 1.5 --p0 0.5 --smax 3 --name dyn1
"""
import sys, os, time, json, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch
from ipm2polar import Disc, bary_weights
from zetasolve import quad_weights
torch.set_default_dtype(torch.float64)


class Probe:
    def __init__(self, d):
        self.d = d
        dev = d.dev
        # GL quadrature in xi for radial integrals of the interpolant
        xg, wg = np.polynomial.legendre.leggauss(400)
        xi = 0.5 * d.xi_max * (xg + 1.0); w = 0.5 * d.xi_max * wg
        xx = 2.0 * xi / d.xi_max - 1.0
        wb = bary_weights(d.x)
        T = wb[None, :] / (xx[:, None] - d.x[None, :]); P = T / T.sum(axis=1, keepdims=True)
        self.xi_g = torch.tensor(xi, device=dev); self.w_g = torch.tensor(w, device=dev)
        self.P = torch.tensor(P, device=dev)
        self.s_g = d.L ** 2 * (torch.exp(self.xi_g) - 1.0)
        thp = d.theta_p[:, None]; rr = d.r[None, :]
        self.phi_r = -3 * rr ** -4 * torch.sin(3 * thp)
        self.phi_t_over_r = 3 * rr ** -4 * torch.cos(3 * thp)          # (1/r) d_theta phi

    def radial_int(self, h_r):
        """int_0^R h(r) r dr for h given at the nodes (interpolant in xi)."""
        hg = self.P @ h_r
        return float(torch.sum(self.w_g * hg * self.d.L ** 2 * torch.exp(self.xi_g) / 2.0))

    def Q(self, out):
        """Q = int rho W.grad phi dX on r<R plus exterior power-law estimate; also c from the m=3 moment."""
        d = self.d
        rho = out['rho']; Ur, Ut = out['Ur'], out['Ut']
        integrand = (rho * (Ur * self.phi_r + Ut * self.phi_t_over_r)).mean(dim=0) * 2 * math.pi   # function of r
        Qin = self.radial_int(integrand)
        # exterior: integrand * r ~ A r^{2p-3}: fit on the two outermost nodes (indices 0 and 2)
        r0, r2 = float(d.r[0]), float(d.r[2]); i0, i2 = float(integrand[0] * r0), float(integrand[2] * r2)
        Qext = float('nan')
        if i0 * i2 > 0:
            slope = math.log(abs(i0) / abs(i2)) / math.log(r0 / r2)
            if slope < -1.0:
                Qext = -i0 * r0 / (slope + 1.0)
        return Qin, Qext


def rhs_and_diag(d, qz, probe=None, full=False):
    """Right-hand side of zeta_s = -(V.grad zeta - zeta/2) with c_l = 1/2 + c[zeta^2].  Returns (rhs modes, info)."""
    z_m, dz_m, tz_m = d.rho_modes(qz)
    z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
    rho = z * z
    rho_m = d.to_modes(rho)
    q_rho = rho_m / d.rk
    rho_m2, drho_m, tth_m = d.rho_modes(q_rho, constrained=False)
    f_m = d.dx_modes(drho_m, tth_m)
    # c_l from the current strain; tail needs c_l: two-pass (first pass with previous estimate stored on d)
    cl_prev = getattr(d, "_cl_dyn", 2.0)
    p = d.poisson(f_m, rho_m2, torch.tensor(cl_prev, device=d.dev))
    U0, pxx, pxy, pyy = d.taylor_psi(p)
    cl = 0.5 + float(pxy)
    if abs(cl - cl_prev) > 1e-6 and cl > 1.0:
        p = d.poisson(f_m, rho_m2, torch.tensor(cl, device=d.dev))
        U0, pxx, pxy, pyy = d.taylor_psi(p)
        cl = 0.5 + float(pxy)
    d._cl_dyn = cl if cl > 1.0 else cl_prev
    psi_m, Ur_m, Ut_m = d.velocity_modes(p)
    Ur = d.to_phys(Ur_m); Ut = d.to_phys(Ut_m)
    Rz = cl * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
    rhs = -d.to_modes(Rz) / d.rk          # increment of the reduced coefficients q_m (zeta_m = r^kappa q_m)
    info = dict(cl=cl, c=float(pxy), b=float(pyy))
    if full:
        dr = d.to_phys(drho_m); dt = d.to_phys(tth_m); rho_rep = d.to_phys(rho_m2)
        Rphys = cl * d.r[None, :] * dr + Ur * dr + Ut * dt - rho_rep
        out = dict(rho=rho_rep, Ur=Ur, Ut=Ut, zeta=z, rho_m=rho_m2, Rz=Rz, Rphys=Rphys, p=p)
        info['out'] = out
    return rhs, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nr", type=int, default=40); ap.add_argument("--Nth", type=int, default=24)
    ap.add_argument("--R", type=float, default=100.0); ap.add_argument("--L", type=float, default=1.0)
    ap.add_argument("--ay", type=float, default=1.5); ap.add_argument("--p0", type=float, default=0.5)
    ap.add_argument("--eps", type=float, default=0.0); ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--smax", type=float, default=3.0); ap.add_argument("--dt", type=float, default=None)
    ap.add_argument("--cl_min", type=float, default=1.02); ap.add_argument("--every", type=float, default=0.05)
    ap.add_argument("--name", default="dyn")
    ap.add_argument("--symx", action="store_true", help="PROBE ONLY: enforce x-odd zeta (x-even rho) each step")
    ap.add_argument("--jetproj", action="store_true", help="re-impose the jet (zeta(0)=0, Re zeta_x(0)=1, q_m(0)=0 for m>=3) each step")
    args = ap.parse_args()
    dev = 'cuda'
    d = Disc(args.Nr, args.Nth, args.R, L=args.L, K=2, tail='power2', device=dev)
    probe = Probe(d)
    th = d.theta_p[:, None]; r = d.r[None, :]
    X, Y = r * torch.cos(th), r * torch.sin(th)
    z0 = X * (1 + args.ay * Y / (1 + r ** 2) ** 0.5) * (1 + r ** 2) ** ((args.p0 / 2 - 1) / 2)
    if args.eps:
        g = torch.Generator().manual_seed(args.seed); cc = torch.randn(5, generator=g).to(dev)
        z0 = z0 + args.eps * ((cc[0] * X ** 2 + cc[1] * Y ** 2 + cc[2] * X * Y) * (1 + r ** 2) ** ((args.p0 / 2 - 2) / 2)
                              + (cc[3] * X ** 3 + cc[4] * Y ** 3) * (1 + r ** 2) ** ((args.p0 / 2 - 3) / 2))
    qz = d.to_modes(z0) / d.rk
    d._cl_dyn = 1.0 / args.p0
    # time step from a CFL estimate in xi
    xi_np = d.xi_np; dxi_min = float(np.min(np.abs(np.diff(xi_np))))
    dt = args.dt if args.dt else 0.4 * dxi_min / (2.0 * max(d._cl_dyn, 2.0))
    print("unknowns %d dxi_min %.2e dt %.2e" % (d.nunk(), dxi_min, dt), flush=True)
    logf = open("runs/%s.log" % args.name, "w")
    logf.write("# dynrescale %s args %s\n# s cl c b zx zy Qin Qext Qratio target dc_ds_num dc_ds_law asym_x asym_y zmax Rz_max\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), vars(args)))
    s = 0.0; next_out = 0.0; c_prev = None; s_prev = None
    wq = quad_weights(d)
    mm = torch.arange(d.M + 1, device=dev); sgn = (-1.0) ** mm
    t0 = time.time()
    while s <= args.smax + 1e-12:
        if s >= next_out - 1e-12:
            rhs, info = rhs_and_diag(d, qz, probe, full=True)
            out = info['out']
            Qin, Qext = probe.Q(out)
            Qtot = Qin + (Qext if np.isfinite(Qext) else 0.0)
            c = info['c']
            law = c * (0.5 - c) + Qtot / math.pi
            num = (c - c_prev) / (s - s_prev) if c_prev is not None else float('nan')
            z0_, zx, zy, _, _, _ = [float(t) for t in d.taylor_rho(qz)]
            rho_m = out['rho_m']
            odd_x = 0.5 * (rho_m - sgn[:, None] * rho_m.conj()); odd_y = 0.5 * (rho_m - rho_m.conj())
            nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum())
            ax = float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum()) / nrm); ay_ = float(torch.sqrt((odd_y.abs() ** 2 * wq[None, :]).sum()) / nrm)
            line = "%.4f %.6f %.6f %.3e %.6f %.3e %.5f %.2e %.4f %.4f %.4f %.4f %.2e %.3e %.3e %.3e" % (
                s, info['cl'], c, info['b'], zx, zy, Qin, Qext, Qtot / (math.pi * c * c) if c != 0 else float('nan'),
                1 - 1 / (2 * c) if c != 0 else float('nan'), num, law, ax, ay_, float(out['zeta'].abs().max()), float(out['Rz'].abs().max()))
            print(line, flush=True); logf.write(line + "\n"); logf.flush()
            c_prev, s_prev = c, s
            next_out += args.every
            if info['cl'] <= args.cl_min:
                print("c_l = %.4f <= cl_min: left class S, stopping" % info['cl'], flush=True); break
            if not np.isfinite(float(out['zeta'].abs().max())) or float(out['zeta'].abs().max()) > 1e6:
                print("blow-up, stopping", flush=True); break
        # RK4 step
        k1, _ = rhs_and_diag(d, qz)
        k2, _ = rhs_and_diag(d, qz + 0.5 * dt * k1)
        k3, _ = rhs_and_diag(d, qz + 0.5 * dt * k2)
        k4, _ = rhs_and_diag(d, qz + dt * k3)
        qz = qz + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        qz[0] = qz[0].real.to(torch.complex128)          # keep the m=0 mode real
        if args.symx:
            ev = (torch.arange(d.M + 1, device=dev) % 2 == 0)[:, None]
            qz = torch.where(ev, 1j * qz.imag, qz.real.to(torch.complex128))
        if args.jetproj:
            N = d.Nr - 1
            e0 = d.ell0c; eN = e0[N]
            cur = qz @ e0
            tgt = cur.clone(); tgt[0] = 0.0; tgt[1] = 0.5 + 1j * cur[1].imag; tgt[3:] = 0.0
            qz[:, N] = qz[:, N] + (tgt - cur) / eN
        s += dt
    print("done %.0fs" % (time.time() - t0), flush=True)
    torch.save(dict(q=qz.cpu(), cl=d._cl_dyn, args=vars(args), r=d.r_np, xi=d.xi_np, kappa=d.kappa_np, s=s), "runs/%s.pt" % args.name)


if __name__ == "__main__":
    main()
