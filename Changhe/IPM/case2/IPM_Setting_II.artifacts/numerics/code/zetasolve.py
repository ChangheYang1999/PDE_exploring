"""
zetasolve.py -- solver for the signed-square-root formulation (specification 4.5):
    rho = zeta^2,   (c_l X + W[rho]) . grad zeta = zeta / 2,   zeta = x + O(|X|^2),
with W the class-S (once-subtracted) Biot-Savart velocity of specification 4.2 (per-mode, analytic tail).
No symmetry is imposed: all Fourier modes of zeta are unknowns.  c_l is an unknown (its identity
c_l = 1/2 + psi_xy(0) is monitored, not imposed) unless --impose_cl is given.

Methods:  lm      Levenberg-Marquardt on the full nonlinear system (autodiff Jacobian, SVD, column scaling)
          picard  freeze V = c_l X + W[zeta_n^2], solve the LINEAR transport problem for zeta_{n+1} in the
                  least-squares sense with the jet rows, c_l from the eigenvalue condition, mix, repeat.
Usage: python3 zetasolve.py --Nr 48 --Nth 32 --R 100 --cl0 2.0 --eps 0.1 --method lm --name z1
"""
import sys, os, time, json, math, argparse
import numpy as np
import torch
from torch.func import jacfwd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipm2polar import Disc, bary_weights

torch.set_default_dtype(torch.float64)


def weight_zeta(d, p):
    """Expected magnitude of zeta: ~ r near 0, ~ r^{p/2} at infinity."""
    r = d.r
    return r / (1.0 + r ** 2) ** ((1.0 - p / 2.0) / 2.0)


def initial_zeta(d, cl0, eps=0.0, seed=0, ay=0.0, kind="A", terms=None):
    p = 1.0 / cl0
    th = d.theta_p[:, None]
    r = d.r[None, :]
    X, Y = r * torch.cos(th), r * torch.sin(th)
    fac = (1 + r ** 2) ** ((p / 2 - 1) / 2)
    if kind == "A":
        z0 = X * (1 + ay * Y / (1 + r ** 2) ** 0.5) * fac
    elif kind == "terms":
        # terms: list of (kind, A, sc) as in tests/picard_random.py, e.g. sample 109: [('y',2.58,10.0),('x2y',-1.39,1.0)]
        g = torch.ones_like(X)
        for tk, A, sc in terms:
            rr2 = 1 + r ** 2 / sc ** 2
            if tk == 'y':     g = g + A * Y / rr2 ** 0.5 / sc
            elif tk == 'y3':  g = g + A * Y ** 3 / rr2 ** 1.5 / sc ** 3
            elif tk == 'x2y': g = g + A * X ** 2 * Y / rr2 ** 1.5 / sc ** 3
            elif tk == 'xy':  g = g + A * X * Y / rr2 / sc ** 2
            elif tk == 'yr':  g = g + A * Y / rr2 / sc
            elif tk == 'y3':  g = g + A * Y ** 3 / rr2 ** 1.5 / sc ** 3
        z0 = X * g * fac
    else:
        raise ValueError(kind)
    if eps != 0.0:
        g = torch.Generator().manual_seed(seed)
        c = torch.randn(5, generator=g).to(d.dev)
        pert = (c[0] * X ** 2 + c[1] * Y ** 2 + c[2] * X * Y) * (1 + r ** 2) ** ((p / 2 - 2) / 2) \
            + (c[3] * X ** 3 + c[4] * Y ** 3) * (1 + r ** 2) ** ((p / 2 - 3) / 2)
        z0 = z0 + eps * pert
    qz = d.to_modes(z0) / d.rk
    return d.pack(qz, cl0)


def quad_weights(d):
    """Node weights for int f r dr dtheta on the padded grid (trapezoid in r, exact in theta)."""
    r = d.r
    rn = r.cpu().numpy()[::-1]
    dr = np.gradient(rn)
    return torch.tensor(dr[::-1].copy(), device=d.dev) * r * (2 * math.pi / d.Np)


def diagnostics(d, v, wz, formulation="zeta", cl_override=None):
    """Diagnostics from the state v (zeta modes + c_l).  Residuals of both the zeta equation and the
    original rho equation; jet; identities; symmetry; far field; zeros of V (approximate)."""
    qz, cl = d.unpack(v)
    if cl_override is not None:
        cl = torch.as_tensor(cl_override, dtype=torch.float64, device=d.dev)
    out = d.zeta_residual_modes(qz, cl, return_all=True)
    r = d.r
    wq = quad_weights(d)
    dg = dict(cl=float(cl))
    z0, zx, zy, _, _, _ = [float(t) for t in d.taylor_rho(qz)]
    dg["zeta_jet"] = dict(z0=z0, zx=zx, zy=zy)
    dg["zeta_angle_deg"] = math.degrees(math.atan2(zy, zx))
    rho0, rx, ry, rxx, rxy, ryy = [float(t) for t in d.taylor_rho(out["q_rho"])]
    dg["rho_jet"] = dict(rho0=rho0, rx=rx, ry=ry, rxx=rxx, rxy=rxy, ryy=ryy)
    U0, pxx, pxy, pyy = d.taylor_psi(out["p"])
    dg["U0"] = (float(U0[0]), float(U0[1]))
    dg["psi_xx0"], dg["psi_xy0"], dg["psi_yy0"] = float(pxx), float(pxy), float(pyy)
    dg["cl_identity"] = float(cl) - 0.5 - float(pxy)
    dg["cl_eig"] = 0.5 + math.sqrt(float(pxy) ** 2 + float(pyy) ** 2)   # eigenvalue form (rotating jet)
    # zeta residual, normalized by wz
    Rz = out["Rz"].abs()
    dg["Rz_max_norm"] = float((Rz / wz[None, :]).max())
    dg["Rz_L2_rel"] = float(torch.sqrt((Rz ** 2 * wq[None, :]).sum() / (out["zeta"] ** 2 * wq[None, :]).sum()))
    # rho residual (original equation), specification 4.4 normalization |R|/(|rho| + |V.grad rho|) and weighted norms
    Rp = out["Rphys"].abs()
    rho = out["rho"]
    Vgrad = (Rp * 0 + (cl * r[None, :] * out["dr"] + out["Ur"] * out["dr"] + out["Ut"] * out["dt"]).abs())
    den = rho.abs() + Vgrad
    dg["R_max_abs"] = float(Rp.max())
    dg["R_rel_max"] = float((Rp / (den + 1e-300)).max())
    p = 1.0 / float(cl)
    wR = (1.0 + r) ** (-p)
    dg["R_wsup"] = float((Rp * wR[None, :]).max())
    dg["R_wL2"] = float(torch.sqrt(((Rp * wR[None, :]) ** 2 * wq[None, :]).sum()))
    dg["rho_wL2"] = float(torch.sqrt(((rho.abs() * wR[None, :]) ** 2 * wq[None, :]).sum()))
    for nm, msk in (("central", r < 1.0), ("inter", (r >= 1.0) & (r < 10.0)), ("far", r >= 10.0)):
        if msk.any():
            dg["R_rel_max_" + nm] = float((Rp[:, msk] / (den[:, msk] + 1e-300)).max())
            dg["R_wsup_" + nm] = float((Rp[:, msk] * wR[None, msk]).max())
    # symmetry of rho: x-odd and y-odd fractions
    rho_m = out["rho_m"]
    mm = torch.arange(d.M + 1, device=d.dev)
    sgn = (-1.0) ** mm
    odd_x = 0.5 * (rho_m - sgn[:, None] * rho_m.conj())
    odd_y = 0.5 * (rho_m - rho_m.conj())
    nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum())
    dg["asym_x"] = float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum()) / nrm)
    dg["asym_y"] = float(torch.sqrt((odd_y.abs() ** 2 * wq[None, :]).sum()) / nrm)
    # distance from the polynomial x^2 on r<2 ; positivity of rho (zeta^2 >= 0 trivially: check rho_rep min)
    th = d.theta_p[:, None]
    X = r[None, :] * torch.cos(th)
    msk = r < 2.0
    dg["dist_x2_central"] = float(((rho - X ** 2)[:, msk]).abs().max() / (X ** 2)[:, msk].abs().max())
    dg["rho_min"] = float(rho.min())
    # far field exponents from modes 0, 2 of rho and mode 1 of zeta
    def logslope(a, i0=0, i1=4):
        a0, a1 = a[i0].abs(), a[i1].abs()
        if float(a0) < 1e-300 or float(a1) < 1e-300:
            return float("nan")
        return float((torch.log(a0) - torch.log(a1)) / (torch.log(r[i0]) - torch.log(r[i1])))
    dg["slope_rho_m0"], dg["slope_rho_m2"] = logslope(rho_m[0]), logslope(rho_m[2])
    dg["p_expected"] = p
    dg["rho_at_R"] = float(rho[:, 0].abs().max())
    dg["zeta_max"] = float(out["zeta"].abs().max())
    # leading Taylor coefficients of zeta modes >= 2 at the origin (Cartesian smoothness: should be 0 for m>=3,
    # for m=2 the quadratic part of zeta is allowed)
    q0m = (qz @ d.ell0c).abs()
    dg["qz_origin_m3plus_max"] = float(q0m[3:].max()) if d.M >= 3 else 0.0
    spec = torch.sqrt((out["rho_m"].abs() ** 2 * wq[None, :]).sum(dim=1))
    dg["spec_tail_ratio"] = float(spec[-3:].max() / spec.max())
    # zeros of V away from 0: min over grid of |V|/r  (V ~ c_l r near 0)
    Vr = cl * r[None, :] + out["Ur"]
    Vt = out["Ut"]
    Vmag = torch.sqrt(Vr ** 2 + Vt ** 2) / r[None, :]
    dg["min_V_over_r"] = float(Vmag.min())
    dg["min_Vr_over_r"] = float((Vr / r[None, :]).min())
    # lead's moment law: Q = int rho W.grad(r^-3 sin 3th) dX ; a profile needs Q/(pi c^2) = 1 - 1/(2c)
    thp = d.theta_p[:, None]; rr = r[None, :]
    Wgp = out["Ur"] * (-3 * rr ** -4 * torch.sin(3 * thp)) + out["Ut"] * (3 * rr ** -4 * torch.cos(3 * thp))
    integ = (rho * Wgp).mean(dim=0) * 2 * math.pi
    dg["Q_int"] = float(torch.sum(integ * wq_r(d)))
    # exterior estimate: integrand * r ~ A r^{s}, fitted on the two outermost nodes (indices 0, 2)
    r0, r2 = float(r[0]), float(r[2]); i0, i2 = float(integ[0] * r0), float(integ[2] * r2)
    Qext = 0.0
    if i0 * i2 > 0:
        sl = math.log(abs(i0) / abs(i2)) / math.log(r0 / r2)
        if sl < -1.0:
            Qext = -i0 * r0 / (sl + 1.0)
    dg["Q_ext"] = Qext
    c_ = float(pxy)
    dg["Q_ratio"] = (dg["Q_int"] + Qext) / (math.pi * c_ * c_) if c_ != 0 else float("nan")
    # zeros of V other than the origin: local minima of |V|/r on the grid, refined by Newton on the interpolant
    dg["V_zeros"] = find_V_zeros(d, out, cl)
    dg["Q_target"] = 1 - 1 / (2 * c_) if c_ != 0 else float("nan")
    return dg


def find_V_zeros(d, out, cl, nmax=4, tol=1e-9):
    """Candidate stagnation points of V = c_l X + W away from the origin: grid points where |V|/r is a local minimum
    and small; refined by a damped Newton iteration on the spectral interpolant (bilinear in the modal values).
    Returns a list of (x, y, |V|, det DV, trace DV) for converged zeros with r > r_min."""
    import numpy as np
    r = d.r; thp = d.theta_p[:, None]
    Vr = cl * r[None, :] + out["Ur"]; Vt = out["Ut"]
    Vmag = torch.sqrt(Vr ** 2 + Vt ** 2) / r[None, :]
    Vm = Vmag.cpu().numpy()
    cand = []
    Np, Nr = Vm.shape
    for i in range(Np):
        for j in range(1, Nr - 1):
            v = Vm[i, j]
            if v < 0.25 and v <= Vm[(i - 1) % Np, j] and v <= Vm[(i + 1) % Np, j] and v <= Vm[i, j - 1] and v <= Vm[i, j + 1]:
                cand.append((v, i, j))
    cand.sort()
    zeros = []
    if not cand:
        return zeros
    # interpolant for V components (Cartesian) at arbitrary points via modal evaluation
    Ur_m = d.to_modes(out["Ur"]); Ut_m = d.to_modes(out["Ut"])
    kap0 = np.zeros(d.M + 1)
    def Vxy(xy):
        rr = float(np.hypot(xy[0], xy[1])); th = float(np.arctan2(xy[1], xy[0]))
        ur = d.eval_modes_at(Ur_m, kap0, np.array([rr]), np.array([th]))[0]
        ut = d.eval_modes_at(Ut_m, kap0, np.array([rr]), np.array([th]))[0]
        vr = float(cl) * rr + ur
        return np.array([vr * np.cos(th) - ut * np.sin(th), vr * np.sin(th) + ut * np.cos(th)])
    for v, i, j in cand[:nmax]:
        rr = float(r[j]); th = float(thp[i, 0])
        X = np.array([rr * np.cos(th), rr * np.sin(th)])
        ok = False
        for it in range(30):
            F = Vxy(X); h = 1e-6 * max(1.0, np.hypot(*X))
            Jm = np.column_stack([(Vxy(X + np.array([h, 0])) - F) / h, (Vxy(X + np.array([0, h])) - F) / h])
            try:
                dX = np.linalg.solve(Jm, -F)
            except np.linalg.LinAlgError:
                break
            step = min(1.0, 0.5 * rr / max(np.linalg.norm(dX), 1e-300))
            X = X + step * dX
            if np.hypot(*X) < 2.0 * float(r[-1]) or np.hypot(*X) > d.R:   # inside 2 r_min the interpolant is extrapolated: exclude
                break
            if np.linalg.norm(F) < tol * max(1.0, np.hypot(*X)):
                ok = True; break
        if ok:
            F = Vxy(X); h = 1e-6 * max(1.0, np.hypot(*X))
            Jm = np.column_stack([(Vxy(X + np.array([h, 0])) - F) / h, (Vxy(X + np.array([0, h])) - F) / h])
            zeros.append((float(X[0]), float(X[1]), float(np.linalg.norm(F)), float(np.linalg.det(Jm)), float(np.trace(Jm))))
    return zeros


def wq_r(d):
    """weights for int h(r) r dr over the nodes (trapezoid in r)."""
    r = d.r
    rn = r.cpu().numpy()[::-1]
    dr = np.gradient(rn)
    return torch.tensor(dr[::-1].copy(), device=d.dev) * r


def fmt(dg, it, extra=""):
    return ("it %3d %s cl=%.7f id=%.1e pyy0=%.2e eig=%.6f | Rz_n=%.2e Rz_L2=%.2e | R_rel=%.2e (c %.1e i %.1e f %.1e) "
            "R_wsup=%.2e | asym_x=%.2e asym_y=%.2e zang=%.3f | slopes %.3f %.3f (p=%.3f) rhoR=%.2e | minV/r=%.2e q3+=%.1e | Q/(pi c^2)=%.3f tgt=%.3f | Vzeros=%s" %
            (it, extra, dg["cl"], dg["cl_identity"], dg["psi_yy0"], dg["cl_eig"], dg["Rz_max_norm"], dg["Rz_L2_rel"],
             dg["R_rel_max"], dg.get("R_rel_max_central", 0), dg.get("R_rel_max_inter", 0), dg.get("R_rel_max_far", 0),
             dg["R_wsup"], dg["asym_x"], dg["asym_y"], dg["zeta_angle_deg"], dg["slope_rho_m0"], dg["slope_rho_m2"],
             dg["p_expected"], dg["rho_at_R"], dg["min_V_over_r"], dg["qz_origin_m3plus_max"], dg["Q_ratio"], dg["Q_target"],
             ";".join("(%.3g,%.3g|det %.2g)" % (zz[0], zz[1], zz[3]) for zz in dg["V_zeros"]) or "none"))


def residual_vec_zeta_imposed(d, v, jet_weight=1.0, res_weight=None, jet_mode="fixed"):
    """Residual with c_l := 1/2 + psi_xy(0)[zeta^2] imposed (specification 4.3); the c_l slot of v is ignored except as the
    tail-exponent estimate.  For jet_mode 'rotating' the eigenvalue form c_l = 1/2 + sqrt(c^2 + b^2) is used."""
    qz, cl_est = d.unpack(v)
    z_m, dz_m, tz_m = d.rho_modes(qz)
    z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
    rho = z * z
    rho_m = d.to_modes(rho)
    q_rho = rho_m / d.rk
    rho_m2, drho_m, tth_m = d.rho_modes(q_rho, constrained=False)
    f_m = d.dx_modes(drho_m, tth_m)
    p = d.poisson(f_m, rho_m2, cl_est)
    U0, pxx, pxy, pyy = d.taylor_psi(p)
    cl = 0.5 + (pxy if jet_mode == "fixed" else torch.sqrt(pxy ** 2 + pyy ** 2))
    p = d.poisson(f_m, rho_m2, cl)                 # second pass with the consistent tail exponent
    U0, pxx, pxy, pyy = d.taylor_psi(p)
    cl = 0.5 + (pxy if jet_mode == "fixed" else torch.sqrt(pxy ** 2 + pyy ** 2))
    psi_m, Ur_m, Ut_m = d.velocity_modes(p)
    Ur = d.to_phys(Ur_m); Ut = d.to_phys(Ut_m)
    Rz = cl * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
    Rz_m = d.to_modes(Rz)
    if res_weight is not None:
        Rz_m = Rz_m * res_weight[None, :]
    parts = [Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1)]
    z0, zx, zy, _, _, _ = d.taylor_rho(qz)
    jet = torch.stack([z0, zx - 1.0, zy]) if jet_mode == "fixed" else torch.stack([z0, zx - 1.0])
    # keep the c_l slot consistent: row forcing v[-1] = cl (so that diagnostics read the right c_l)
    return torch.cat(parts + [jet * jet_weight, (v[-1] - cl)[None]])


def lm_solve(d, v0, p_w, maxit=40, lam0=1e-2, tol=1e-13, logf=None, jet_mode="fixed", jet_weight=1.0,
             fix_cl=False, impose_cl=False, f0=None, hlam=0.0, svd_cut=1e-10, compat_weight=0.0, cl_fixed=None, f0_modes=None):
    wz = weight_zeta(d, p_w)
    res_w = 1.0 / wz
    n = d.nunk()

    def F(v):
        if impose_cl:
            r_ = residual_vec_zeta_imposed(d, v, jet_weight=jet_weight, res_weight=res_w, jet_mode=jet_mode)
        elif cl_fixed is not None:
            r_ = d.residual_vec_zeta(v, jet_weight=jet_weight, res_weight=res_w, jet_mode=jet_mode, compat_weight=compat_weight,
                                     cl_fixed=cl_fixed, f0=f0_modes)
        else:
            r_ = d.residual_vec_zeta(v, jet_weight=jet_weight, res_weight=res_w, jet_mode=jet_mode, compat_weight=compat_weight)
        if f0 is not None and hlam != 0.0:
            r_ = r_ - hlam * f0                 # homotopy F(v) = lambda F(v0): f0 has zero jet rows
        return r_

    v = v0.clone()
    lam = lam0
    r = F(v)
    hist = []
    t0 = time.time()
    for it in range(maxit):
        J = jacfwd(F)(v)
        if fix_cl:
            J = J[:, :-1]
        colnorm = J.norm(dim=0)
        # floor the column scaling: columns with norm < 1e-8 * max are numerically null (high modes at inner nodes);
        # do not inflate them
        colnorm = torch.clamp(colnorm, min=1e-8 * float(colnorm.max()))
        Js = J / colnorm[None, :]
        U, S, Vh = torch.linalg.svd(Js, full_matrices=False)
        keep = S > svd_cut * S[0]
        U, S, Vh = U[:, keep], S[keep], Vh[keep]
        Utr = U.T @ r
        accepted = False
        for _ in range(14):
            delta = -(Vh.T @ (S / (S ** 2 + lam) * Utr)) / colnorm
            if fix_cl:
                delta = torch.cat([delta, torch.zeros(1, device=d.dev)])
            vn = v + delta
            rn = F(vn)
            if torch.isfinite(rn).all() and rn.norm() < r.norm():
                v, r = vn, rn
                lam = max(lam / 3.0, 1e-16)
                accepted = True
                break
            lam *= 4.0
        dg = diagnostics(d, v, wz, cl_override=cl_fixed)
        if cl_fixed is not None:
            dg["lambda_unknown"] = float(v[-1])
        dg.update(it=it, lam=lam, res_norm=float(r.norm()), step=float(delta.norm()), accepted=accepted,
                  smin=float(S[-1]), smax=float(S[0]), s2=float(S[-2]), s5=float(S[-5]), nkeep=int(keep.sum()),
                  ndrop=int((~keep).sum()), time=time.time() - t0)
        hist.append(dg)
        msg = fmt(dg, it, "|res|=%.3e step=%.1e lam=%.0e smin=%.1e drop=%d%s" % (dg["res_norm"], dg["step"], lam, dg["smin"], dg["ndrop"],
                  (" LAMBDA=%.5f" % dg["lambda_unknown"]) if cl_fixed is not None else ""))
        print(msg, flush=True)
        if logf:
            logf.write(msg + "\n"); logf.flush()
        if not accepted:
            print("LM: no decrease found, stopping", flush=True)
            break
        if r.norm() < tol or dg["step"] < 1e-14:
            break
    return v, r, hist


def lin_lstsq(Lmat, rhs, cutoff=1e-10):
    """Least-squares solve with column scaling and (essentially) untruncated SVD.  The discrete linear transport
    operator is consistent but ill-conditioned (cond ~ 1e14 at 4500 unknowns); truncating at 1e-13 discards real
    information (tests/lin_cond.py), so only numerically zero singular values are dropped."""
    colnorm = Lmat.norm(dim=0)
    colnorm = torch.where(colnorm > 0, colnorm, torch.ones_like(colnorm))
    Ls = Lmat / colnorm[None, :]
    U_, S_, Vh_ = torch.linalg.svd(Ls, full_matrices=False)
    keep = S_ > S_[0] * cutoff
    sol = (Vh_[keep].T @ ((U_[:, keep].T @ rhs) / S_[keep])) / colnorm
    lres = float((Lmat @ sol - rhs).norm())
    return sol, lres


def picard_solve(d, v0, p_w, maxit=30, mix=1.0, logf=None, jet_mode="fixed", cl_rule="identity", f0_modes=None, hlam=0.0,
                 stop_tol=1e-9):
    """Picard / forced Picard (referee protocol): freeze V_q = c_l X + W[q^2] with c_l = 1/2 + c[q^2]; solve the LINEAR
    transport problem T_q eta = lambda f0 (f0_modes: fixed physical forcing as residual modes, unweighted) with the jet
    rows; q <- (1-mix) q + mix eta; recompute c_l from the updated square.  Returns when |q_new - q| < stop_tol."""
    """Freeze V from the current zeta, solve the linear transport problem for zeta (least squares with
    the jet rows), update c_l from the identity, mix."""
    wz = weight_zeta(d, p_w)
    res_w = 1.0 / wz ** 2          # stronger weight at the origin: better conditioned linear solves (tests/lin_cond.py)
    v = v0.clone()
    hist = []
    t0 = time.time()
    n = d.nunk() - 1
    for it in range(maxit):
        qz, cl = d.unpack(v)
        out = d.zeta_residual_modes(qz, cl, return_all=True)
        # c_l update
        U0, pxx, pxy, pyy = d.taylor_psi(out["p"])
        if cl_rule == "identity":
            cl_new = 0.5 + float(pxy)
        elif cl_rule == "eig":
            cl_new = 0.5 + math.sqrt(float(pxy) ** 2 + float(pyy) ** 2)
        else:
            cl_new = float(cl)
        Ur, Ut = out["Ur"].detach(), out["Ut"].detach()

        def Flin(vz):
            qq = d.unpack(torch.cat([vz, torch.zeros(1, device=d.dev)]))[0]
            z_m, dz_m, tz_m = d.rho_modes(qq)
            z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
            Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
            Rz_m = d.to_modes(Rz)
            if f0_modes is not None and hlam != 0.0:
                Rz_m = Rz_m - hlam * f0_modes
            Rz_m = Rz_m * res_w[None, :]
            parts = [Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1)]
            z0, zx, zy, _, _, _ = d.taylor_rho(qq)
            jet = torch.stack([z0, zx - 1.0, zy]) if jet_mode == "fixed" else torch.stack([z0, zx - 1.0])
            return torch.cat(parts + [jet])

        vz = v[:-1]
        Lmat = jacfwd(Flin)(vz)
        rhs = -(Flin(vz) - Lmat @ vz)          # affine part: F(v) = L v + b  ->  solve L v = -b
        sol, lres = lin_lstsq(Lmat, rhs)
        v_new = torch.cat([sol, torch.tensor([cl_new], device=d.dev)])
        change = float((v_new[:-1] - v[:-1]).norm())
        v = (1 - mix) * v + mix * v_new
        # recompute c_l from the UPDATED square (referee: mixing c_l independently loses compatibility)
        qz_u, _ = d.unpack(v)
        out_u = d.zeta_residual_modes(qz_u, torch.tensor(cl_new, device=d.dev), return_all=True)
        pxy_u = d.taylor_psi(out_u["p"])[2]
        v = torch.cat([v[:-1], torch.tensor([0.5 + float(pxy_u)], device=d.dev)])
        dg = diagnostics(d, v, wz)
        dg.update(it=it, time=time.time() - t0, change=change, lin_res=lres, hlam=hlam)
        hist.append(dg)
        msg = fmt(dg, it, "picard dv=%.2e lres=%.1e" % (dg["change"], lres))
        print(msg, flush=True)
        if logf:
            logf.write(msg + "\n"); logf.flush()
        if not np.isfinite(dg["Rz_max_norm"]):
            break
        if change < stop_tol:
            break
    return v, hist


def interpolate_state(st, d):
    q_old = st["q"].to(d.dev)
    xi_old = st["xi"]; kappa_old = st["kappa"]
    Mo = q_old.shape[0] - 1
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
    pre_old = st["args"].get("prefactor", "r") if isinstance(st.get("args"), dict) else "r"
    for mm in range(min(Mo, d.M) + 1):
        k_old = float(kappa_old[mm])
        fac = (rn / torch.sqrt(1.0 + rn ** 2)) ** k_old if pre_old == "s" else rn ** k_old     # OLD prefactor at the new radii
        q_new[mm] = fac * (P @ q_old[mm]) / d.rk[mm]
    return d.pack(q_new, st["cl"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nr", type=int, default=48)
    ap.add_argument("--Nth", type=int, default=32)
    ap.add_argument("--R", type=float, default=100.0)
    ap.add_argument("--L", type=float, default=1.0)
    ap.add_argument("--K", type=int, default=2)
    ap.add_argument("--cl0", type=float, default=2.0)
    ap.add_argument("--p_w", type=float, default=None, help="weight exponent p (default 1/cl0)")
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--ay", type=float, default=0.0)
    ap.add_argument("--kind", default="A")
    ap.add_argument("--terms", default="", help="kind:A:sc,... for --kind terms")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--maxit", type=int, default=40)
    ap.add_argument("--tail", default="power2")
    ap.add_argument("--tail_alpha", type=float, default=None)
    ap.add_argument("--jet", default="fixed")
    ap.add_argument("--method", default="lm", help="lm | picard | picard+lm")
    ap.add_argument("--mix", type=float, default=1.0)
    ap.add_argument("--cl_rule", default="identity")
    ap.add_argument("--lam0", type=float, default=1e-2)
    ap.add_argument("--svd_cut", type=float, default=1e-10)
    ap.add_argument("--compat", type=float, default=0.0, help="weight of the explicit compatibility row c_l - 1/2 - psi_xy(0)")
    ap.add_argument("--cl_path", type=str, default="", help="continuation in c_l: comma list of prescribed c_l; lambda is the unknown")
    ap.add_argument("--prefactor", default="r", help="radial prefactor of the unknown modes: 'r' (r^kappa) or 's' ((r/sqrt(1+r^2))^kappa, verifier V24)")
    ap.add_argument("--fix_cl", action="store_true")
    ap.add_argument("--impose_cl", action="store_true", help="c_l := 1/2 + psi_xy(0) inside the residual (specification 4.3)")
    ap.add_argument("--cl_init_auto", action="store_true", help="start c_l at 1/2 + psi_xy(0) of the initial data")
    ap.add_argument("--smooth", action="store_true", help="smoothness-constrained representation (q_m = O(xi^{(|m|-kappa)/2}))")
    ap.add_argument("--homotopy", type=str, default="", help="comma list of lambda values (1 -> 0): solve F(v) = lambda F(v0)")
    ap.add_argument("--init", default=None)
    ap.add_argument("--name", default="zrun")
    args = ap.parse_args()
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    d = Disc(args.Nr, args.Nth, args.R, L=args.L, K=args.K, renorm_modes=(0, 1), tail=args.tail,
             tail_alpha=args.tail_alpha, device=dev, smooth=args.smooth, prefactor=args.prefactor)
    p_w = args.p_w if args.p_w is not None else 1.0 / args.cl0
    if args.init:
        st = torch.load(args.init, map_location=dev, weights_only=False)
        v0 = interpolate_state(st, d)
        if args.cl0 is not None and "cl_override" in vars(args):
            pass
    else:
        terms = [(t.split(':')[0], float(t.split(':')[1]), float(t.split(':')[2])) for t in args.terms.split(',') if t]
        v0 = initial_zeta(d, args.cl0, eps=args.eps, seed=args.seed, ay=args.ay, kind=args.kind, terms=terms)
        if args.cl_init_auto:
            qz0, _ = d.unpack(v0)
            d.tail_exps = (1.0 / args.cl0, 1.0 / args.cl0 - 1.0)
            o0 = d.zeta_residual_modes(qz0, torch.tensor(args.cl0, device=dev), return_all=True)
            c_init = float(d.taylor_psi(o0["p"])[2]); d.tail_exps = None
            v0[-1] = 0.5 + c_init
            print("initial data: c = %.5f -> c_l start %.5f" % (c_init, 0.5 + c_init), flush=True)
            p_w = 1.0 / max(0.5 + c_init, 1.05)
    os.makedirs("runs", exist_ok=True)
    logf = open("runs/%s.log" % args.name, "a")
    logf.write("# %s\n# args: %s\n# unknowns %d  M %d  r_min %.4g\n" % (
        time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), vars(args), d.nunk(), d.M, d.r_np[-1]))
    print("unknowns", d.nunk(), "M", d.M, "r_min %.4g r_max %.4g k_tail r=%.3g" % (d.r_np[-1], d.r_np[0], d.r_np[d.k_tail]), flush=True)
    hist = []
    v = v0
    if args.method.startswith("picard"):
        if args.homotopy:
            qz0, cl0_ = d.unpack(v)
            f0_modes = d.zeta_residual_modes(qz0, cl0_).detach()        # fixed physical forcing (modal, unweighted)
            for lam_h in [float(s) for s in args.homotopy.split(",")]:
                msg = "=== forced Picard lambda = %.4f ===" % lam_h
                print(msg, flush=True); logf.write(msg + "\n"); logf.flush()
                v, h = picard_solve(d, v, p_w, maxit=args.maxit, mix=args.mix, logf=logf, jet_mode=args.jet,
                                    cl_rule=args.cl_rule, f0_modes=f0_modes, hlam=lam_h)
                for hh in h: hh["lambda"] = lam_h
                hist += h
                torch.save(dict(q=d.unpack(v)[0].cpu(), cl=float(d.unpack(v)[1]), args=vars(args), hist=hist, r=d.r_np,
                                xi=d.xi_np, kappa=d.kappa_np, formulation="zeta", lam=lam_h), "runs/%s_lam%.3f.pt" % (args.name, lam_h))
        else:
            v, h = picard_solve(d, v, p_w, maxit=args.maxit, mix=args.mix, logf=logf, jet_mode=args.jet, cl_rule=args.cl_rule)
            hist += h
    if args.method.endswith("lm") and args.cl_path:
        # continuation in c_l (referee: pass folds in lambda).  f0 = F(seed) as unweighted residual modes; v[-1] := lambda.
        if args.init:
            # backward/forward continuation from a saved stage: f0 from the SEED (recomputed), lambda from the saved state
            st_ = torch.load(args.init, map_location=dev, weights_only=False)
            vseed = initial_zeta(d, args.cl0, eps=0.0, ay=args.ay)
            qzs, cls = d.unpack(vseed)
            f0_modes = d.zeta_residual_modes(qzs, cls).detach()
            v = torch.cat([v[:-1], torch.tensor([float(st_.get("lam", 1.0))], device=dev)])
        else:
            qz0, cl0_ = d.unpack(v)
            f0_modes = d.zeta_residual_modes(qz0, cl0_).detach()
            v = torch.cat([v[:-1], torch.tensor([1.0], device=dev)])          # lambda = 1 at the seed
        for cl_fixed in [float(s) for s in args.cl_path.split(",")]:
            msg = "=== c_l continuation: c_l = %.4f (unknown lambda) ===" % cl_fixed
            print(msg, flush=True); logf.write(msg + "\n"); logf.flush()
            v, r, h = lm_solve(d, v, 1.0 / cl_fixed, maxit=args.maxit, lam0=args.lam0, logf=logf, jet_mode=args.jet,
                               svd_cut=args.svd_cut, compat_weight=args.compat, cl_fixed=cl_fixed, f0_modes=f0_modes)
            for hh in h: hh["cl_fixed"] = cl_fixed
            hist += h
            torch.save(dict(q=d.unpack(v)[0].cpu(), cl=cl_fixed, lam=float(v[-1]), args=vars(args), hist=hist, r=d.r_np,
                            xi=d.xi_np, kappa=d.kappa_np, formulation="zeta"), "runs/%s_cl%.3f.pt" % (args.name, cl_fixed))
    elif args.method.endswith("lm"):
        if args.homotopy:
            lams = [float(s) for s in args.homotopy.split(",")]
            wz = weight_zeta(d, p_w)
            f0 = d.residual_vec_zeta(v, jet_weight=1.0, res_weight=1.0 / wz, jet_mode=args.jet, compat_weight=args.compat).detach()
            njet = (3 if args.jet == "fixed" else 2) + (1 if args.compat > 0 else 0)
            f0[-njet:] = 0.0
            for lam_h in lams:
                msg = "=== homotopy lambda = %.4f ===" % lam_h
                print(msg, flush=True); logf.write(msg + "\n"); logf.flush()
                v, r, h = lm_solve(d, v, p_w, maxit=args.maxit, lam0=args.lam0, logf=logf, jet_mode=args.jet,
                                   fix_cl=args.fix_cl, impose_cl=args.impose_cl, f0=f0, hlam=lam_h, svd_cut=args.svd_cut,
                                   compat_weight=args.compat)
                for hh in h: hh["lambda"] = lam_h
                hist += h
                torch.save(dict(q=d.unpack(v)[0].cpu(), cl=float(d.unpack(v)[1]), args=vars(args), hist=hist, r=d.r_np, xi=d.xi_np,
                                kappa=d.kappa_np, formulation="zeta", lam=lam_h), "runs/%s_lam%.3f.pt" % (args.name, lam_h))
        else:
            v, r, h = lm_solve(d, v, p_w, maxit=args.maxit, lam0=args.lam0, logf=logf, jet_mode=args.jet, fix_cl=args.fix_cl,
                               impose_cl=args.impose_cl, svd_cut=args.svd_cut, compat_weight=args.compat)
            hist += h
    qz, cl = d.unpack(v)
    torch.save(dict(q=qz.cpu(), cl=float(cl), args=vars(args), hist=hist, r=d.r_np, xi=d.xi_np, kappa=d.kappa_np,
                    formulation="zeta"), "runs/%s.pt" % args.name)
    with open("runs/%s.json" % args.name, "w") as f:
        json.dump(dict(args=vars(args), final=hist[-1] if hist else None), f, indent=1, default=float)
    logf.close()


if __name__ == "__main__":
    main()
