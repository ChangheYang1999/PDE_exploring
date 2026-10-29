"""Independent holdout diagnostics for a candidate (PROMPT.md sections 8 and 9).

Everything here is evaluated on grids that are NOT the collocation grids (different Gauss orders, exact axis
points mu = +-1, an origin collar, log-spaced far-field radii), with unweighted residuals, so that a small
training cost cannot hide axis, origin, interface, or far-field defects.
"""
from __future__ import annotations

import math
from typing import Dict

import numpy as np
import torch

from . import basis, ops
from .problem import Problem, alpha_of, PHI_KEYS, Q_KEYS


def _stats(v):
    v = np.asarray(v, float)
    if v.size == 0:
        return dict(rms=float("nan"), max=float("nan"), n=0)
    return dict(rms=float(np.sqrt(np.mean(v * v))), max=float(np.max(np.abs(v))), n=int(v.size))


def holdout_points(prob: Problem, factor=1.37, far_decades=6, n_far=60):
    """Holdout grid: ball and shell Gauss grids with a non-integer multiple of the training resolution, plus the
    exterior on log-spaced radii.  Returns dict of arrays: R, mu, kind (0 ball,1 shell,2 exterior)."""
    cfg = prob.cfg
    Rs, mus, kinds = [], [], []
    nmu = int(prob.nmu * factor) + 3
    mu1, _ = basis.gauss_legendre(nmu)
    for i, e in enumerate(prob.elements):
        if e.kind == "ball":
            nR = int((cfg.nR_ball or int(1.3 * (cfg.D // 2) + 4)) * factor) + 3
            x, _ = basis.gauss_legendre(nR)
            R = e.Rhi * np.sqrt(0.5 * (x + 1))
        elif e.kind == "shell":
            nR = int((cfg.nR_shell or int(1.3 * e.params["K"] + 4)) * factor) + 3
            x, _ = basis.gauss_legendre(nR)
            L = math.log(e.Rhi / e.Rlo)
            R = e.Rlo * np.exp(0.5 * (x + 1) * L)
        else:
            R = e.Rlo * np.logspace(0.0, far_decades, n_far)
        RR, MM = np.meshgrid(R, mu1, indexing="ij")
        Rs.append(RR.ravel()); mus.append(MM.ravel()); kinds.append(np.full(RR.size, {"ball": 0, "shell": 1, "exterior": 2}[e.kind]))
    return dict(R=np.concatenate(Rs), mu=np.concatenate(mus), kind=np.concatenate(kinds))


def residual_fields(prob: Problem, x, R, mu, cl=None):
    """Unweighted residuals and auxiliary fields at arbitrary points (CPU torch)."""
    cl = prob.cl if cl is None else cl
    phi, q = prob.eval_all(x, R, mu)
    g = ops.geom(torch.tensor(np.asarray(R, float)), torch.tensor(np.asarray(mu, float)))
    Rq, Reta, aux = ops.reduced_residuals(phi, q, g, cl)
    P = ops.primitive_terms(phi, q, g, cl)
    # per-term magnitudes for relative residuals
    Ur, Uz, Ur_over_r = ops.velocities(phi, g)
    Wr = cl * g["r"] + Ur; Wz = cl * g["z"] + Uz
    qr, qz = ops.grad_rz(q, g)
    q0 = q[(0, 0)]
    terms_q = q0.abs() + (Wr * qr + Wz * qz).abs() + (2 * Ur_over_r * q0).abs()
    eta = ops.eta_and_grad(phi, g)
    er, ez = ops.grad_rz(eta, g)
    terms_eta = ((1 + cl) * eta[(0, 0)]).abs() + (Wr * er + Wz * ez).abs() + (2 * q0 * qz).abs()
    out = dict(Rq=Rq.numpy(), Reta=Reta.numpy(), terms_q=terms_q.numpy(), terms_eta=terms_eta.numpy(),
               q=q0.numpy(), phi=phi[(0, 0)].numpy(), eta=eta[(0, 0)].numpy(), Ur=Ur.numpy(), Uz=Uz.numpy(),
               Ut=P["Ut"].numpy(), Om_theta=P["Om_theta"].numpy(), div=P["div"].numpy(),
               Ur_r=P["Ur_r"].numpy(), Ur_z=P["Ur_z"].numpy(), Uz_r=P["Uz_r"].numpy(), Uz_z=P["Uz_z"].numpy(),
               Ut_r=P["Ut_r"].numpy(), Ut_z=P["Ut_z"].numpy(), S=P["S"].numpy(), Mr=P["Mr"].numpy(), Mt=P["Mt"].numpy(), Mz=P["Mz"].numpy())
    return out


def vorticity_norm2(f, r):
    """|Omega|^2 for axisymmetric flow: Omega^r = -d_z U^theta, Omega^theta, Omega^z = d_r U^theta + U^theta/r."""
    Om_r = -f["Ut_z"]
    Ut_over_r = f["q"]
    Om_z = f["Ut_r"] + Ut_over_r
    return Om_r**2 + f["Om_theta"]**2 + Om_z**2


def report(prob: Problem, x, cl=None) -> Dict:
    """Full holdout diagnostics dictionary (JSON-serializable)."""
    x = x.detach().cpu()
    cl = float(prob.cl if cl is None else cl)
    alpha = alpha_of(cl)
    H = holdout_points(prob)
    R, mu, kind = H["R"], H["mu"], H["kind"]
    f = residual_fields(prob, x, R, mu, cl)
    rep = dict(cl=cl, alpha=alpha, nx=prob.nx, Rm=prob.Rm, R1=prob.cfg.R1, n_holdout=int(R.size))
    inner = kind < 2
    # ---- global residual statistics (inner = ball + shells, unweighted), scaled in the exterior
    rep["Rq_inner"] = _stats(f["Rq"][inner]); rep["Reta_inner"] = _stats(f["Reta"][inner])
    rep["Rq_ext_scaled"] = _stats((R ** (2 * alpha + 2) * f["Rq"])[~inner])
    rep["Reta_ext_scaled"] = _stats((R ** (2 * alpha + 3) * f["Reta"])[~inner])
    # per-term relative (denominator = sum of absolute values of the terms, RMS over inner points)
    den_q = np.sqrt(np.mean(f["terms_q"][inner] ** 2)); den_e = np.sqrt(np.mean(f["terms_eta"][inner] ** 2))
    rep["rel_Rq_inner"] = float(rep["Rq_inner"]["rms"] / den_q) if den_q > 0 else float("nan")
    rep["rel_Reta_inner"] = float(rep["Reta_inner"]["rms"] / den_e) if den_e > 0 else float("nan")
    rep["rel_Rq_inner_pointwise_max"] = float(np.max(np.abs(f["Rq"][inner]) / (f["terms_q"][inner] + 1e-300 + 1e-12 * den_q)))
    rep["rel_Reta_inner_pointwise_max"] = float(np.max(np.abs(f["Reta"][inner]) / (f["terms_eta"][inner] + 1e-300 + 1e-12 * den_e)))
    # ---- shellwise (dyadic in R/R1), including exterior with scaled residuals
    sid = np.clip(np.floor(np.log2(np.maximum(R / prob.cfg.R1, 1e-300))).astype(int), -6, None)
    shells = []
    for s in np.unique(sid):
        m = sid == s
        scq = np.where(kind[m] == 2, R[m] ** (2 * alpha + 2), 1.0)
        sce = np.where(kind[m] == 2, R[m] ** (2 * alpha + 3), 1.0)
        shells.append(dict(shell=int(s), Rlo=float(prob.cfg.R1 * 2.0**s), Rhi=float(prob.cfg.R1 * 2.0 ** (s + 1)),
                           Rq_rms=float(np.sqrt(np.mean((scq * f["Rq"][m]) ** 2))), Rq_max=float(np.max(np.abs(scq * f["Rq"][m]))),
                           Reta_rms=float(np.sqrt(np.mean((sce * f["Reta"][m]) ** 2))), Reta_max=float(np.max(np.abs(sce * f["Reta"][m]))),
                           q_rms=float(np.sqrt(np.mean(f["q"][m] ** 2))), eta_rms=float(np.sqrt(np.mean(f["eta"][m] ** 2))),
                           Ut_rms=float(np.sqrt(np.mean(f["Ut"][m] ** 2))), U_rms=float(np.sqrt(np.mean(f["Ur"][m] ** 2 + f["Uz"][m] ** 2 + f["Ut"][m] ** 2)))))
    rep["shells"] = shells
    # ---- swirl diagnostics (3D measure 2 pi r dr dz approximated by holdout averages with weight r on inner points)
    w3 = (R * np.sqrt(1 - mu**2))[inner]
    U2 = (f["Ur"] ** 2 + f["Uz"] ** 2 + f["Ut"] ** 2)[inner]
    rep["swirl_ratio_inner"] = float(np.sqrt(np.sum(w3 * f["Ut"][inner] ** 2) / max(1e-300, np.sum(w3 * U2))))
    rep["max_abs_Ut_inner"] = float(np.max(np.abs(f["Ut"][inner]))); rep["max_abs_U_inner"] = float(np.sqrt(np.max(U2)))
    rep["max_abs_q_inner"] = float(np.max(np.abs(f["q"][inner]))); rep["max_abs_eta_inner"] = float(np.max(np.abs(f["eta"][inner])))
    rep["max_abs_phi_inner"] = float(np.max(np.abs(f["phi"][inner])))
    Om2 = vorticity_norm2(f, R * np.sqrt(1 - mu**2))
    j = int(np.argmax(np.where(inner, Om2, -1)))
    rep["vorticity_max"] = float(math.sqrt(Om2[j])); rep["vorticity_max_R"] = float(R[j]); rep["vorticity_max_mu"] = float(mu[j])
    # core location and width: vorticity-weighted radius
    wv = np.where(inner, Om2 * w3 if False else Om2, 0.0)
    rep["core_R_mean"] = float(np.sum(wv * R) / max(1e-300, np.sum(wv)))
    rep["core_R_width"] = float(math.sqrt(max(0.0, np.sum(wv * R * R) / max(1e-300, np.sum(wv)) - rep["core_R_mean"] ** 2)))
    # ---- origin and axis collars
    orig = inner & (R < 0.05 * prob.cfg.R1)
    rep["origin_collar"] = dict(Rq=_stats(f["Rq"][orig]), Reta=_stats(f["Reta"][orig]), n=int(orig.sum()))
    # exact axis points: mu = +-1 at many radii (inner region)
    Ra = np.concatenate([np.linspace(0.002, prob.Rm, 200)] * 2); mua = np.concatenate([np.ones(200), -np.ones(200)])
    fa = residual_fields(prob, x, Ra, mua, cl)
    rep["axis"] = dict(Rq=_stats(fa["Rq"]), Reta=_stats(fa["Reta"]), Ur_max=float(np.max(np.abs(fa["Ur"]))),
                       Ut_max=float(np.max(np.abs(fa["Ut"]))), finite=bool(np.all(np.isfinite(fa["Rq"])) and np.all(np.isfinite(fa["Reta"]))),
                       q_axis_max=float(np.max(np.abs(fa["q"]))), eta_axis_max=float(np.max(np.abs(fa["eta"]))))
    # origin Taylor data: phi(0), q(0), DU(0): U^z(0) = 2 phi(0); d_z U^z(0) = 3 phi_z(0) ... from the ball polynomial
    phi0, q0 = prob.eval_all(x, np.array([1e-6]), np.array([1.0]))
    rep["origin"] = dict(phi0=float(phi0[(0, 0)][0]), q0=float(q0[(0, 0)][0]), Uz0=float(2 * phi0[(0, 0)][0]),
                         dUz_dz0=float(3 * phi0[(1, 0)][0]))   # along the axis phi_z = phi_R; U^z = 2phi + r phi_r -> d_z U^z(0) = 2 phi_z + phi_z = 3 phi_z
    # ---- tail diagnostics
    cphi, cq, _ = prob.split(x)
    full, sw, pol = prob.tail_integrals(cphi[-1].to(prob.device), cq[-1].to(prob.device), alpha)
    rep["tail"] = dict(int_F2=full, int_Ftheta2=sw, int_Fpol2=pol, swirl_fraction=(sw / full if full > 0 else float("nan")))
    ext = prob.elements[-1]
    Rm = prob.Rm
    A = np.zeros(prob.cfg.nmax + 1); Bc = np.zeros(prob.cfg.nmax + 1)
    for t, idx in enumerate(prob.ext_lead_idx_phi):
        A[prob.ext_lead_n_phi[t]] = float(cphi[-1][idx]) * Rm ** alpha
    for t, idx in enumerate(prob.ext_lead_idx_q):
        Bc[prob.ext_lead_n_q[t]] = float(cq[-1][idx]) * Rm ** (alpha + 1)
    rep["tail"]["A_legendre"] = A.tolist(); rep["tail"]["B_legendre"] = Bc.tolist()
    by_exp_phi, by_exp_q = {}, {}
    for t, (n, e) in enumerate(prob.ext_labels_phi):
        by_exp_phi.setdefault(round(e, 6), 0.0); by_exp_phi[round(e, 6)] = max(by_exp_phi[round(e, 6)], abs(float(cphi[-1][t])))
    for t, (n, e) in enumerate(prob.ext_labels_q):
        by_exp_q.setdefault(round(e, 6), 0.0); by_exp_q[round(e, 6)] = max(by_exp_q[round(e, 6)], abs(float(cq[-1][t])))
    rep["tail"]["max_coef_by_exponent_phi"] = {str(k): v for k, v in by_exp_phi.items()}
    rep["tail"]["max_coef_by_exponent_q"] = {str(k): v for k, v in by_exp_q.items()}
    # tail connectedness: leading term vs full exterior field at R = 2 Rm and 10 Rm
    conn = {}
    for fac in (1.0, 2.0, 10.0):
        Rt = np.full(41, fac * Rm); mut = np.linspace(-1, 1, 41)
        ph, qq = prob.eval_all(x, Rt, mut)
        Pm = basis.legendre_derivs(mut, prob.cfg.nmax, 0)[0]
        lead_phi = (Pm @ A) * (fac * Rm) ** (-alpha)
        lead_q = (Pm @ Bc) * (fac * Rm) ** (-(alpha + 1))
        conn[str(fac)] = dict(phi_lead_over_total=float(np.linalg.norm(lead_phi) / max(1e-300, np.linalg.norm(ph[(0, 0)].numpy()))),
                              q_lead_over_total=float(np.linalg.norm(lead_q) / max(1e-300, np.linalg.norm(qq[(0, 0)].numpy()))),
                              phi_rms=float(np.sqrt(np.mean(ph[(0, 0)].numpy() ** 2))), q_rms=float(np.sqrt(np.mean(qq[(0, 0)].numpy() ** 2))))
    rep["tail"]["connectedness"] = conn
    # R^alpha U convergence toward a nonzero angular profile: compare at several radii
    conv = []
    for fac in (1.0, 2.0, 4.0, 10.0, 100.0):
        Rt = np.full(41, fac * Rm); mut = np.linspace(-0.99, 0.99, 41)
        ft = residual_fields(prob, x, Rt, mut, cl)
        conv.append(dict(R=float(fac * Rm), RaUt_rms=float(np.sqrt(np.mean((Rt ** alpha * ft["Ut"]) ** 2))),
                         RaUpol_rms=float(np.sqrt(np.mean((Rt ** alpha) ** 2 * (ft["Ur"] ** 2 + ft["Uz"] ** 2))))))
    rep["tail"]["RalphaU_vs_R"] = conv
    # ---- interface mismatch on fresh angular points (unweighted)
    ints = []
    mu_i = np.linspace(-0.97, 0.97, 29)
    for i in range(prob.nel - 1):
        Rint = prob.elements[i].Rhi
        pa, qa = prob.eval_all(x, np.full_like(mu_i, Rint * (1 - 1e-12)), mu_i)
        pb, qb = prob.eval_all(x, np.full_like(mu_i, Rint * (1 + 1e-12)), mu_i)
        pa = {k: v.numpy() for k, v in pa.items()}; pb = {k: v.numpy() for k, v in pb.items()}
        qa = {k: v.numpy() for k, v in qa.items()}; qb = {k: v.numpy() for k, v in qb.items()}
        ints.append(dict(R=float(Rint), dphi=float(np.max(np.abs(pa[(0, 0)] - pb[(0, 0)]))), dphiR=float(np.max(np.abs(pa[(1, 0)] - pb[(1, 0)]))),
                         dphiRR=float(np.max(np.abs(pa[(2, 0)] - pb[(2, 0)]))), dq=float(np.max(np.abs(qa[(0, 0)] - qb[(0, 0)]))),
                         dqR=float(np.max(np.abs(qa[(1, 0)] - qb[(1, 0)]))), phi_scale=float(np.max(np.abs(pa[(0, 0)]))), q_scale=float(np.max(np.abs(qa[(0, 0)])))))
    rep["interfaces"] = ints
    # ---- spectral coefficient decay per element (tail-to-head ratios by angular degree and radial index)
    spec = []
    for i, e in enumerate(prob.elements):
        if e.kind == "exterior":
            continue
        labs = [e.labels[j] for j in prob.cols_phi[i]]; labs_q = [e.labels[j] for j in prob.cols_q[i]]      # phi and q may have different parity masks
        n_arr = np.array([l[0] for l in labs]); k_arr = np.array([l[1] for l in labs])
        nq_arr = np.array([l[0] for l in labs_q]); kq_arr = np.array([l[1] for l in labs_q])
        cp = cphi[i].numpy(); cqv = cq[i].numpy()
        def by(arr, c):
            vals = {}
            for a in np.unique(arr):
                vals[int(a)] = float(np.sqrt(np.sum(c[arr == a] ** 2)))
            return vals
        spec.append(dict(element=i, kind=e.kind, phi_by_n=by(n_arr, cp), phi_by_k=by(k_arr, cp), q_by_n=by(nq_arr, cqv), q_by_k=by(kq_arr, cqv)))
    rep["spectral"] = spec
    # ---- divergence check (should be round-off)
    rep["div_max_inner"] = float(np.max(np.abs(f["div"][inner])))
    return rep


def summarize(rep: Dict) -> str:
    t = rep["tail"]
    return (f"cl={rep['cl']:.6f} Rq_in rms={rep['Rq_inner']['rms']:.2e} max={rep['Rq_inner']['max']:.2e} "
            f"Reta_in rms={rep['Reta_inner']['rms']:.2e} max={rep['Reta_inner']['max']:.2e} rel(q,eta)=({rep['rel_Rq_inner']:.2e},{rep['rel_Reta_inner']:.2e}) "
            f"ext_scaled(q,eta)=({rep['Rq_ext_scaled']['rms']:.1e},{rep['Reta_ext_scaled']['rms']:.1e}) swirl={rep['swirl_ratio_inner']:.3f} "
            f"|q|max={rep['max_abs_q_inner']:.2e} |eta|max={rep['max_abs_eta_inner']:.2e} tail(F2,sw,pol)=({t['int_F2']:.3f},{t['int_Ftheta2']:.3f},{t['int_Fpol2']:.3f}) "
            f"conn(2Rm)=({t['connectedness']['2.0']['phi_lead_over_total']:.2f},{t['connectedness']['2.0']['q_lead_over_total']:.2f}) "
            f"axis(q,eta)=({rep['axis']['Rq']['max']:.1e},{rep['axis']['Reta']['max']:.1e}) origin(q,eta)=({rep['origin_collar']['Rq']['max']:.1e},{rep['origin_collar']['Reta']['max']:.1e})")


def interface_jumps_spec65(prob, x, n_mu=64):
    """SPEC 6.5 interface measure: at every internal element interface, on n_mu Gauss-Legendre angular points, the jumps of phi and its
    R- and mu-derivatives up to total order 3 and of q up to total order 2, each relative to the scale of the same derivative on that
    interface (max over the two one-sided traces and the points).  Returns (worst, where, table) with table[(interface R, field, key)] = rel jump.
    This is the measure that A8, B4 and the F5 class use (lead note 35 item 2 (d))."""
    from numpy.polynomial import legendre as _L
    mu, _ = _L.leggauss(n_mu)
    x_np = x.detach().cpu().numpy() if hasattr(x, "detach") else np.asarray(x)
    worst, where, table = 0.0, "", {}
    for i in range(prob.nel - 1):
        R = prob.elements[i].Rhi
        A = prob.elements[i].eval_at(np.full_like(mu, R), mu); B = prob.elements[i + 1].eval_at(np.full_like(mu, R), mu)
        for fld, maxord in (("phi", 3), ("q", 2)):
            cols_a = prob.cols_phi[i] if fld == "phi" else prob.cols_q[i]; cols_b = prob.cols_phi[i + 1] if fld == "phi" else prob.cols_q[i + 1]
            off_a = prob.off_phi[i] if fld == "phi" else prob.off_q[i]; off_b = prob.off_phi[i + 1] if fld == "phi" else prob.off_q[i + 1]
            ca = x_np[off_a:off_a + len(cols_a)]; cb = x_np[off_b:off_b + len(cols_b)]
            for key in sorted(k for k in A if k[0] + k[1] <= maxord):
                va = A[key][:, cols_a] @ ca; vb = B[key][:, cols_b] @ cb
                sc = max(float(np.max(np.abs(va))), float(np.max(np.abs(vb))), 1e-300)
                j = float(np.max(np.abs(va - vb)) / sc)
                table[(float(R), fld, key)] = j
                if j > worst:
                    worst, where = j, f"{fld} d^{key[0]}_R d^{key[1]}_mu at R={R:g}"
    return worst, where, table
