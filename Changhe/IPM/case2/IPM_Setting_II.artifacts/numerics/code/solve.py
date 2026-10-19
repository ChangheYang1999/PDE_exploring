"""
solve.py -- Levenberg-Marquardt (Gauss-Newton) solver for the discretized moving-center IPM profile
problem (see ipm2polar.py).  Unknowns: all modal values q_m(xi_j) (no symmetry imposed) and c_l.
Equations: transport residual modes at all nodes (weighted) + 6 jet conditions.  The system is
overdetermined by 5 rows (see the numerical record for the counting); the least-squares residual at
convergence is itself a diagnostic.

Usage: python3 solve.py --Nr 48 --Nth 32 --R 30 --cl0 1.5 --eps 0.1 --name test1
"""
import sys, os, time, json, math, argparse
import numpy as np
import torch
from torch.func import jacfwd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipm2polar import Disc

torch.set_default_dtype(torch.float64)


def weight_profile(d, alpha):
    """Expected magnitude of rho at the nodes: ~ r^2 near 0, ~ r^alpha at infinity."""
    r = d.r
    return r ** 2 / (1.0 + r ** 2) ** (1.0 - alpha / 2.0)


def initial_guess(d, cl0, eps=0.0, seed=0, kind="x2"):
    """rho0 = x^2 (1+r^2)^{(alpha-2)/2} + eps * asymmetric cubic/quartic perturbation, alpha = 1/cl0."""
    alpha = 1.0 / cl0
    th = d.theta_p[:, None]
    r = d.r[None, :]
    X, Y = r * torch.cos(th), r * torch.sin(th)
    if kind == "x2":
        rho0 = X ** 2 * (1 + r ** 2) ** ((alpha - 2) / 2)
    elif kind == "x2y":
        rho0 = X ** 2 * (1 + 0.5 * Y) * (1 + r ** 2) ** ((alpha - 2) / 2)
    else:
        raise ValueError(kind)
    if eps != 0.0:
        g = torch.Generator().manual_seed(seed)
        c = torch.randn(6, generator=g).to(d.dev)
        pert = (c[0] * X ** 3 + c[1] * Y ** 3 + c[2] * X * Y ** 2 + c[3] * X ** 2 * Y) * (1 + r ** 2) ** ((alpha - 3) / 2) \
            + (c[4] * X * Y ** 3 + c[5] * X ** 3 * Y) * (1 + r ** 2) ** ((alpha - 4) / 2)
        rho0 = rho0 + eps * pert
    q = d.to_modes(rho0) / d.rk
    return d.pack(q, cl0)


def diagnostics(d, v, w):
    q, cl = d.unpack(v)
    out = d.residual_modes(q, cl, return_all=True)
    R_m, rho_m, p = out["R_m"], out["rho_m"], out["p"]
    Rphys = out["Rphys"]
    rho = out["rho"]
    r = d.r
    dg = {}
    dg["cl"] = float(cl)
    rho0, rx, ry, rxx, rxy, ryy = [float(t) for t in d.taylor_rho(q)]
    dg["jet"] = dict(rho0=rho0, rx=rx, ry=ry, rxx=rxx, rxy=rxy, ryy=ryy)
    dg["hess_angle_deg"] = 0.5 * math.degrees(math.atan2(2 * rxy, rxx - ryy))
    dg["hess_det"] = rxx * ryy - rxy ** 2
    dg["hess_tr"] = rxx + ryy
    U0, pxx, pxy, pyy = d.taylor_psi(p)
    dg["U0"] = (float(U0[0]), float(U0[1]))
    dg["psi_xx0"], dg["psi_xy0"], dg["psi_yy0"] = float(pxx), float(pxy), float(pyy)
    dg["cl_identity"] = float(cl) - 0.5 - float(pxy)
    # residual norms (physical grid, padded theta): absolute and normalized by w(r)
    absR = Rphys.abs()
    dg["R_max_abs"] = float(absR.max())
    dg["R_max_norm"] = float((absR / w[None, :]).max())
    # L2 with polar measure r dr dtheta approximated by node weights ~ r * dr (use trapezoid in r)
    rn = r.cpu().numpy()[::-1]
    dr = np.gradient(rn)
    wq = torch.tensor(dr[::-1].copy(), device=d.dev) * r * (2 * math.pi / d.Np)
    dg["R_L2_abs"] = float(torch.sqrt((absR ** 2 * wq[None, :]).sum()))
    dg["rho_L2"] = float(torch.sqrt((rho ** 2 * wq[None, :]).sum()))
    dg["R_L2_rel"] = dg["R_L2_abs"] / max(dg["rho_L2"], 1e-300)
    # regions: central r<1, mid 1<r<R/4, outer r>R/4
    for nm, msk in (("central", r < 1.0), ("mid", (r >= 1.0) & (r < d.R / 4)), ("outer", r >= d.R / 4)):
        if msk.any():
            dg["Rn_max_" + nm] = float((absR[:, msk] / w[None, msk]).max())
    # symmetry: x-reflection odd part and y-reflection odd part
    mm = torch.arange(d.M + 1, device=d.dev)
    sgn = (-1.0) ** mm
    refl_x = sgn[:, None] * rho_m.conj()
    odd_x = 0.5 * (rho_m - refl_x)
    odd_y = 0.5 * (rho_m - rho_m.conj())
    nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum() * 2)
    dg["asym_x"] = float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum() * 2) / nrm)
    dg["asym_y"] = float(torch.sqrt((odd_y.abs() ** 2 * wq[None, :]).sum() * 2) / nrm)
    # distance from the polynomial x^2 on r<2
    th = d.theta_p[:, None]
    X = r[None, :] * torch.cos(th)
    msk = r < 2.0
    dg["dist_x2_central"] = float(((rho - X ** 2)[:, msk]).abs().max() / (X ** 2)[:, msk].abs().max())
    # far-field exponents of modes 0 and 2 (log-derivative at the two outermost nodes)
    def logslope(a):
        a0, a1 = a[0].abs(), a[2].abs()
        if float(a0) < 1e-300 or float(a1) < 1e-300:
            return float("nan")
        return float((torch.log(a0) - torch.log(a1)) / (torch.log(r[0]) - torch.log(r[2])))
    dg["slope_m0"], dg["slope_m2"], dg["slope_m1"] = logslope(rho_m[0]), logslope(rho_m[2]), logslope(rho_m[1])
    dg["rho_max"] = float(rho.abs().max())
    dg["rho_at_R"] = float(rho[:, 0].abs().max())
    # leading Taylor coefficients of modes >= 3 (should vanish for Cartesian smoothness): q_m(0)
    q0m = (q @ d.ell0c).abs()
    dg["q_origin_m3plus_max"] = float(q0m[3:].max()) if d.M >= 3 else 0.0
    # mode spectrum decay
    spec = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum(dim=1))
    dg["spec_tail_ratio"] = float(spec[-3:].max() / spec.max())
    return dg


def lm_solve(d, v0, alpha_w, maxit=40, lam0=1e-2, tol=1e-13, verbose=True, logf=None, jet_weight=1.0,
             jet_mode="fixed"):
    w = weight_profile(d, alpha_w)
    res_w = 1.0 / w

    def F(v):
        return d.residual_vec(v, jet_weight=jet_weight, res_weight=res_w, jet_mode=jet_mode)

    v = v0.clone()
    lam = lam0
    r = F(v)
    hist = []
    t0 = time.time()
    for it in range(maxit):
        J = jacfwd(F)(v)
        colnorm = J.norm(dim=0)
        colnorm = torch.where(colnorm > 0, colnorm, torch.ones_like(colnorm))
        Js = J / colnorm[None, :]
        U, S, Vh = torch.linalg.svd(Js, full_matrices=False)
        Utr = U.T @ r
        accepted = False
        for _ in range(12):
            delta = -(Vh.T @ (S / (S ** 2 + lam) * Utr)) / colnorm
            vn = v + delta
            rn = F(vn)
            if torch.isfinite(rn).all() and rn.norm() < r.norm():
                v, r = vn, rn
                lam = max(lam / 3.0, 1e-15)
                accepted = True
                break
            lam *= 4.0
        dg = diagnostics(d, v, w)
        dg.update(it=it, lam=lam, res_norm=float(r.norm()), step=float(delta.norm()), accepted=accepted,
                  smin=float(S[-1]), smax=float(S[0]), time=time.time() - t0)
        hist.append(dg)
        if verbose:
            msg = ("it %2d |res|=%.3e step=%.2e lam=%.1e cl=%.6f psi_xy0=%.6f cl-id=%.1e psi_yy0=%.2e "
                   "Rn_max=%.2e (c %.1e m %.1e o %.1e) asym_x=%.2e asym_y=%.2e dist_x2=%.2e slopes m0 %.3f m2 %.3f "
                   "rhoR=%.2e smin=%.1e q3+=%.1e ang=%.3f det=%.1e" %
                   (it, dg["res_norm"], dg["step"], lam, dg["cl"], dg["psi_xy0"], dg["cl_identity"], dg["psi_yy0"],
                    dg["R_max_norm"], dg.get("Rn_max_central", 0), dg.get("Rn_max_mid", 0), dg.get("Rn_max_outer", 0),
                    dg["asym_x"], dg["asym_y"], dg["dist_x2_central"], dg["slope_m0"], dg["slope_m2"],
                    dg["rho_at_R"], dg["smin"], dg["q_origin_m3plus_max"], dg["hess_angle_deg"], dg["hess_det"]))
            print(msg, flush=True)
            if logf:
                logf.write(msg + "\n"); logf.flush()
        if not accepted:
            if verbose:
                print("LM: no decrease found, stopping", flush=True)
            break
        if r.norm() < tol or dg["step"] < 1e-14:
            break
    return v, r, hist


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nr", type=int, default=48)
    ap.add_argument("--Nth", type=int, default=32)
    ap.add_argument("--R", type=float, default=30.0)
    ap.add_argument("--L", type=float, default=1.0)
    ap.add_argument("--K", type=int, default=2)
    ap.add_argument("--cl0", type=float, default=1.5)
    ap.add_argument("--alpha_w", type=float, default=None, help="weight exponent (default 1/cl0)")
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--kind", default="x2")
    ap.add_argument("--maxit", type=int, default=40)
    ap.add_argument("--tail", default="zero")
    ap.add_argument("--tail_alpha", type=float, default=None)
    ap.add_argument("--renorm", default="0,1")
    ap.add_argument("--gauge2", type=float, nargs=2, default=(0.0, 0.0))
    ap.add_argument("--init", default=None, help="load initial state from a .pt file (interpolated if needed)")
    ap.add_argument("--name", default="run")
    ap.add_argument("--jet", default="fixed", help="fixed | rotating")
    ap.add_argument("--lam0", type=float, default=1e-2)
    args = ap.parse_args()
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    renorm = tuple(int(s) for s in args.renorm.split(","))
    d = Disc(args.Nr, args.Nth, args.R, L=args.L, K=args.K, renorm_modes=renorm, tail=args.tail,
             tail_alpha=args.tail_alpha, gauge2=complex(*args.gauge2), device=dev)
    alpha_w = args.alpha_w if args.alpha_w is not None else 1.0 / args.cl0
    if args.init:
        st = torch.load(args.init, map_location=dev, weights_only=False)
        if st.get("formulation") == "zeta":
            # build rho = zeta^2 from a saved zeta state on the SAME grid (Nr, Nth, R, L must match)
            from ipm2polar import Disc as _D
            dz = _D(st["args"]["Nr"], st["args"]["Nth"], st["args"]["R"], L=st["args"]["L"], K=args.K, renorm_modes=renorm,
                    tail=args.tail, tail_alpha=args.tail_alpha, device=dev, smooth=st["args"].get("smooth", False))
            qz = st["q"].to(dev)
            vz = dz.pack(qz, float(st["cl"])); qz2, _ = dz.unpack(vz)
            z_m, _, _ = dz.rho_modes(qz2)
            rho = d.to_phys(z_m) ** 2 if (dz.Np == d.Np and dz.Nr == d.Nr) else None
            assert rho is not None, "grid mismatch between the zeta state and this run"
            q_rho = d.to_modes(rho) / d.rk
            v0 = d.pack(q_rho, float(st["cl"]))
            print("initialised rho = zeta^2 from %s (c_l = %.5f)" % (args.init, float(st["cl"])), flush=True)
        else:
            v0 = interpolate_state(st, d)
    else:
        v0 = initial_guess(d, args.cl0, eps=args.eps, seed=args.seed, kind=args.kind)
    os.makedirs("runs", exist_ok=True)
    logf = open("runs/%s.log" % args.name, "a")
    logf.write("# %s\n# args: %s\n# unknowns %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), vars(args), d.nunk()))
    print("unknowns", d.nunk(), "modes", d.M, "r_min %.3g r_max %.3g" % (d.r_np[-1], d.r_np[0]), flush=True)
    v, r, hist = lm_solve(d, v0, alpha_w, maxit=args.maxit, logf=logf, jet_mode=args.jet, lam0=args.lam0)
    q, cl = d.unpack(v)
    torch.save(dict(q=q.cpu(), cl=float(cl), args=vars(args), hist=hist, r=d.r_np, xi=d.xi_np, kappa=d.kappa_np),
               "runs/%s.pt" % args.name)
    with open("runs/%s.json" % args.name, "w") as f:
        json.dump(dict(args=vars(args), final=hist[-1] if hist else None), f, indent=1, default=float)
    logf.close()


def interpolate_state(st, d):
    """Interpolate a saved state (q on its own grid) onto the grid of d (same L required for exactness of
    the xi-polynomial interpolation; otherwise interpolate in r)."""
    from ipm2polar import bary_weights
    q_old = st["q"].to(d.dev)
    r_old = st["r"]; xi_old = st["xi"]; kappa_old = st["kappa"]
    Mo = q_old.shape[0] - 1
    # evaluate old modes at new radii: rho_m(r) = r^kappa_old q_old(xi_old(r)) with xi_old = log(1+r^2/L_old^2)
    L_old = st["args"]["L"]
    xi_new_in_old = np.log(1.0 + d.r_np ** 2 / L_old ** 2)
    ximax_old = xi_old.max()
    x_old = 2.0 * xi_old / ximax_old - 1.0
    x_new = 2.0 * xi_new_in_old / ximax_old - 1.0
    w = bary_weights(x_old)
    P = np.zeros((d.Nr, len(x_old)))
    for i, xe in enumerate(x_new):
        dd = xe - x_old
        if np.any(np.abs(dd) < 1e-14):
            P[i, np.argmin(np.abs(dd))] = 1.0
        else:
            t = w / dd
            P[i] = t / t.sum()
    P = torch.tensor(P, device=d.dev, dtype=torch.complex128)
    q_new = torch.zeros((d.M + 1, d.Nr), dtype=torch.complex128, device=d.dev)
    rn = torch.tensor(d.r_np, device=d.dev)
    for mm in range(min(Mo, d.M) + 1):
        rho_m_new = (rn ** float(kappa_old[mm])) * (P @ q_old[mm])
        q_new[mm] = rho_m_new / d.rk[mm]
    # outside old domain: extrapolation by the polynomial (fine if R_new <= R_old; else crude)
    return d.pack(q_new, st["cl"])


if __name__ == "__main__":
    main()
