"""SPEC 6.1 / 6.2 / 8 holdout metrics for a candidate state (numerics lane's own implementation; acceptance uses the
verifier's independent code).

Evaluation sets (SPEC 8): dyadic shells S_k = [2^k a, 2^(k+1) a), k = -6..11, in units a = a_eff (vorticity half-maximum
radius, SPEC 5), plus the origin ball R < 2^-6 a.  In each shell: Gauss-Legendre nodes in log R (nR) x Gauss-Legendre in mu
(nmu >= max(64, 1.5 x angular resolution)) plus 256 uniformly random points (seeded), and an axis collar
(sin vartheta < 0.05) with measure R^2 dR dvartheta.
Equations: M^r, M^theta, M^z (primitive momentum with the full-space pressure of pressure.py), q, eta, div (and ell = 0
identically for formulation B).  rho_E(S) = RMS_S(R_E) / min(RMS_S(L_E), RMS_S(N_E)); m_E(S) = max_S |R_E| / D_E(S).
Also the scaled far-field residuals of SPEC 6.2 and the single-term ratios.
"""
from __future__ import annotations

import math
from typing import Dict

import numpy as np
import torch

from . import basis, ops, pressure
from .problem import Problem, alpha_of


def _rms(v, w=None):
    v = np.asarray(v, float)
    if v.size == 0:
        return float("nan")
    if w is None:
        return float(np.sqrt(np.mean(v * v)))
    return float(np.sqrt(np.sum(w * v * v) / np.sum(w)))


def a_eff(prob: Problem, x, Rmax=None, n_R=400, n_mu=65):
    """Vorticity half-maximum radius: sup{R : max_{|y|=R} |Omega| >= max|Omega|/2} on a log grid."""
    Rmax = Rmax or 100 * prob.Rm
    R = np.logspace(-3, math.log10(Rmax), n_R)
    mu = np.linspace(-1, 1, n_mu)
    RR, MM = np.meshgrid(R, mu, indexing="ij")
    f = fields(prob, x, RR.ravel(), MM.ravel())
    Om2 = f["Om2"].reshape(len(R), len(mu))
    prof = np.sqrt(np.max(Om2, axis=1))
    j = int(np.argmax(prof))
    half = prof >= 0.5 * prof[j]
    k = np.max(np.nonzero(half)[0])
    return float(R[k]), float(prof[j]), float(R[j]), float(mu[int(np.argmax(Om2[j]))])


def fields(prob: Problem, x, R, mu, cl=None):
    cl = prob.cl if cl is None else cl
    phi, q = prob.eval_all(x, R, mu)
    g = ops.geom(torch.tensor(np.asarray(R, float)), torch.tensor(np.asarray(mu, float)))
    Rq, Reta, aux = ops.reduced_residuals(phi, q, g, cl)
    P = ops.primitive_terms(phi, q, g, cl)
    qr, qz = ops.grad_rz(q, g)
    eta = ops.eta_and_grad(phi, g)
    er, ez = ops.grad_rz(eta, g)
    Ur, Uz, Uror = P["Ur"], P["Uz"], P["Ur_over_r"]
    out = {k: v.numpy() for k, v in P.items()}
    out.update(Rq=Rq.numpy(), Reta=Reta.numpy(), q=q[(0, 0)].numpy(), eta=eta[(0, 0)].numpy(), phi=phi[(0, 0)].numpy())
    # linear and nonlinear parts (SPEC 6.1)
    out["Lq"] = out["q"]; out["Nq"] = (Ur * qr + Uz * qz + 2 * Uror * q[(0, 0)]).numpy()
    out["Leta"] = (1 + cl) * out["eta"]; out["Neta"] = (Ur * er + Uz * ez - 2 * q[(0, 0)] * qz).numpy()
    # momentum: L = (1-c) U ; N = (U . grad) U (cylindrical components with swirl curvature terms)
    out["LM_r"] = (1 - cl) * out["Ur"]; out["LM_t"] = (1 - cl) * out["Ut"]; out["LM_z"] = (1 - cl) * out["Uz"]
    out["NM_r"] = (Ur * P["Ur_r"] + Uz * P["Ur_z"] - P["Ut"] * q[(0, 0)]).numpy()
    out["NM_t"] = (Ur * P["Ut_r"] + Uz * P["Ut_z"] + Ur * q[(0, 0)]).numpy()
    out["NM_z"] = (Ur * P["Uz_r"] + Uz * P["Uz_z"]).numpy()
    out["DU_frob"] = np.sqrt(out["Ur_r"] ** 2 + out["Ur_z"] ** 2 + out["Uz_r"] ** 2 + out["Uz_z"] ** 2 + out["Ur_over_r"] ** 2
                             + out["Ut_r"] ** 2 + out["Ut_z"] ** 2 + out["q"] ** 2)
    Om_r = -out["Ut_z"]; Om_z = out["Ut_r"] + out["q"]
    out["Om2"] = Om_r ** 2 + out["Om_theta"] ** 2 + Om_z ** 2
    return out


def shell_points(prob: Problem, a, k, nR, nmu, rng):
    """Gauss x Gauss points and random points of dyadic shell k (in units of a), with weights."""
    Rlo, Rhi = a * 2.0 ** k, a * 2.0 ** (k + 1)
    t, wt = basis.gauss_legendre(nR, math.log(Rlo), math.log(Rhi))
    mu, wmu = basis.gauss_legendre(nmu)
    RR, MM = np.meshgrid(np.exp(t), mu, indexing="ij")
    WW = np.outer(wt * np.exp(t) ** 3, wmu)                 # dV ~ R^2 dR dmu (2 pi factor irrelevant), R dR from dt
    # 256 random points uniform in the shell VOLUME (R^3 uniform, mu uniform), unweighted RMS is then the volume average
    Rr = (rng.uniform(Rlo ** 3, Rhi ** 3, 256)) ** (1.0 / 3.0); mur = rng.uniform(-1, 1, 256)
    # axis collar: sin(vartheta) < 0.05; measure R^2 dR dvartheta (no sin weight): Gauss in log R (weight w_t R^3) x uniform vartheta
    vth1 = np.linspace(0, math.asin(0.05), 12)
    vth = np.concatenate([vth1, math.pi - vth1])
    Rc, Vc = np.meshgrid(np.exp(t), vth, indexing="ij")
    Wc = np.outer(wt * np.exp(t) ** 3, np.ones_like(vth))
    return dict(R=RR.ravel(), mu=MM.ravel(), w=WW.ravel(), Rr=Rr, mur=mur, Rc=Rc.ravel(), muc=np.cos(Vc).ravel(), wc=Wc.ravel())


def validate(prob: Problem, x, nR=8, nmu=None, seed=12345, kmin=-6, kmax=11, lmax_pressure=None, pressure_order=32) -> Dict:
    x = x.detach().cpu()
    cl = prob.cl_of(x); alpha = alpha_of(cl)
    nmu = nmu or max(64, int(1.5 * (prob.cfg.nmax + 1)))
    rng = np.random.default_rng(seed)
    a, Om_max, R_Ommax, mu_Ommax = a_eff(prob, x)
    ps = pressure.solver_for_candidate(prob, x, lmax=lmax_pressure, order=pressure_order)
    shells = []
    eqs = ["Mr", "Mt", "Mz", "q", "eta", "div"]
    rho_max = {e: float("nan") for e in eqs}; m_max = {e: float("nan") for e in eqs}
    degenerate = []          # (k, tag, equation) shells whose denominator is below 1e-12 x its value in the core shell [a, 2a] (SPEC 6.1)
    core_D = {}
    def nanmax(a_, b_):
        return b_ if (a_ != a_ ) else (a_ if (b_ != b_) else max(a_, b_))
    for k in list(range(kmin, kmax + 1)):
        pts = shell_points(prob, a, k, nR, nmu, rng)
        rec = dict(k=k, Rlo=a * 2.0 ** k, Rhi=a * 2.0 ** (k + 1))
        for tag, (R, mu, w) in dict(gauss=(pts["R"], pts["mu"], pts["w"]), random=(pts["Rr"], pts["mur"], None), collar=(pts["Rc"], pts["muc"], pts["wc"])).items():
            f = fields(prob, x, R, mu, cl)
            pr = ps.evaluate(R, mu)
            RM = dict(Mr=f["Mr"] + pr["P_r"], Mt=f["Mt"], Mz=f["Mz"] + pr["P_z"], q=f["Rq"], eta=f["Reta"], div=f["div"])
            LM_vec = np.sqrt(f["LM_r"] ** 2 + f["LM_t"] ** 2 + f["LM_z"] ** 2); NM_vec = np.sqrt(f["NM_r"] ** 2 + f["NM_t"] ** 2 + f["NM_z"] ** 2)
            D = dict(M=min(_rms(LM_vec, w), _rms(NM_vec, w)), q=min(_rms(f["Lq"], w), _rms(f["Nq"], w)),
                     eta=min(_rms(f["Leta"], w), _rms(f["Neta"], w)), div=_rms(f["DU_frob"], w))
            Dm = dict(Mr=D["M"], Mt=D["M"], Mz=D["M"], q=D["q"], eta=D["eta"], div=D["div"])
            if k == 0 and tag == "gauss":
                core_D = dict(Dm)
            for e in eqs:
                ref = core_D.get(e, Dm[e]) if core_D else Dm[e]
                degen = not (Dm[e] > 0) or (ref > 0 and Dm[e] < 1e-12 * ref) or not math.isfinite(Dm[e])
                if degen:
                    degenerate.append((k, tag, e))
                    rec[f"rho_{e}_{tag}"] = float("nan"); rec[f"m_{e}_{tag}"] = float("nan"); rec[f"degenerate_{e}_{tag}"] = True
                    continue
                rho = _rms(RM[e], w) / Dm[e]; m = float(np.max(np.abs(RM[e]))) / Dm[e]
                rec[f"rho_{e}_{tag}"] = rho; rec[f"m_{e}_{tag}"] = m
                rho_max[e] = nanmax(rho_max[e], rho); m_max[e] = nanmax(m_max[e], m)
            if tag == "gauss":
                rec.update(D_M=D["M"], D_q=D["q"], D_eta=D["eta"], D_div=D["div"], rms_L_M=_rms(LM_vec, w), rms_N_M=_rms(NM_vec, w),
                           rms_U=_rms(np.sqrt(f["Ur"] ** 2 + f["Uz"] ** 2 + f["Ut"] ** 2), w), rms_Ut=_rms(f["Ut"], w),
                           rms_q=_rms(f["q"], w), rms_eta=_rms(f["eta"], w), rms_P=_rms(pr["P"], w),
                           sigma_q=_rms(f["Rq"], w) / max(_rms(f["Lq"], w), 1e-300), sigma_eta=_rms(f["Reta"], w) / max(_rms(f["Leta"], w), 1e-300),
                           sigma_M=_rms(np.sqrt(RM["Mr"] ** 2 + RM["Mt"] ** 2 + RM["Mz"] ** 2), w) / max(_rms(LM_vec, w), 1e-300),
                           scaled_RM=_rms(R ** (2 * alpha + 1) * np.sqrt(RM["Mr"] ** 2 + RM["Mt"] ** 2 + RM["Mz"] ** 2), w),
                           scaled_Rq=_rms(R ** (2 * alpha + 2) * f["Rq"], w), scaled_Reta=_rms(R ** (2 * alpha + 3) * f["Reta"], w))
        shells.append(rec)
    # origin ball R < 2^-6 a: uniform volume sampling (R^3 uniform); normalized ratios with the core-shell denominators as reference
    Ro = 2.0 ** -6 * a * rng.uniform(0, 1, 300) ** (1.0 / 3.0); muo = rng.uniform(-1, 1, 300)
    f = fields(prob, x, Ro, muo, cl); pr = ps.evaluate(Ro, muo)
    RMo = dict(Mr=f["Mr"] + pr["P_r"], Mt=f["Mt"], Mz=f["Mz"] + pr["P_z"], q=f["Rq"], eta=f["Reta"], div=f["div"])
    LMo = np.sqrt(f["LM_r"] ** 2 + f["LM_t"] ** 2 + f["LM_z"] ** 2); NMo = np.sqrt(f["NM_r"] ** 2 + f["NM_t"] ** 2 + f["NM_z"] ** 2)
    Do = dict(M=min(_rms(LMo), _rms(NMo)), q=min(_rms(f["Lq"]), _rms(f["Nq"])), eta=min(_rms(f["Leta"]), _rms(f["Neta"])), div=_rms(f["DU_frob"]))
    Dom = dict(Mr=Do["M"], Mt=Do["M"], Mz=Do["M"], q=Do["q"], eta=Do["eta"], div=Do["div"])
    origin = dict(Rq_max=float(np.max(np.abs(f["Rq"]))), Reta_max=float(np.max(np.abs(f["Reta"]))),
                  Mr_max=float(np.max(np.abs(f["Mr"] + pr["P_r"]))), Mz_max=float(np.max(np.abs(f["Mz"] + pr["P_z"]))), Mt_max=float(np.max(np.abs(f["Mt"]))),
                  U_scale=float(np.max(np.sqrt(f["Ur"] ** 2 + f["Uz"] ** 2 + f["Ut"] ** 2))), q_scale=float(np.max(np.abs(f["q"]))), eta_scale=float(np.max(np.abs(f["eta"]))))
    for e in eqs:
        ref = core_D.get(e, Dom[e]) if core_D else Dom[e]
        degen = not (Dom[e] > 0) or (ref > 0 and Dom[e] < 1e-12 * ref)
        if degen:
            degenerate.append(("origin", "random", e)); origin[f"rho_{e}"] = float("nan"); origin[f"m_{e}"] = float("nan")
        else:
            origin[f"rho_{e}"] = _rms(RMo[e]) / Dom[e]; origin[f"m_{e}"] = float(np.max(np.abs(RMo[e]))) / Dom[e]
            rho_max[e] = nanmax(rho_max[e], origin[f"rho_{e}"]); m_max[e] = nanmax(m_max[e], origin[f"m_{e}"])
    # swirl fractions (SPEC 6.4): s_core on B_{4a} with 3D measure; s_far from the leading tail
    Rc = 4 * a * rng.uniform(0, 1, 4000) ** (1 / 3); muc = rng.uniform(-1, 1, 4000)
    fc = fields(prob, x, Rc, muc, cl)
    s_core = float(math.sqrt(np.sum(fc["Ut"] ** 2) / max(1e-300, np.sum(fc["Ur"] ** 2 + fc["Uz"] ** 2 + fc["Ut"] ** 2))))
    cphi, cq, _ = prob.split(x)
    full, sw, pol = prob.tail_integrals(cphi[-1].to(prob.device), cq[-1].to(prob.device), alpha)
    s_far = math.sqrt(sw / full) if full > 0 else float("nan")
    # pressure multipole diagnostics at large R (SPEC 3.5): coefficients of R^-1 P_0 and R^-2 P_1 beyond R_far
    mc = ps.mode_coefficients_at(ps.edges[-1])
    # elliptic consistency (PROMPT 6, SPEC 6.6 moment checks): phi vs Delta_5^{-1}(-eta) by the 5D Green inverse, on holdout points
    ell = {}
    try:
        gs = pressure.stream_solver_for_candidate(prob, x)
        Re = np.concatenate([a * 2.0 ** rng.uniform(-4, 4, 300), a * 2.0 ** rng.uniform(4, 10, 100)]); mue = rng.uniform(-1, 1, len(Re))
        fe = fields(prob, x, Re, mue, cl); ge = gs.evaluate(Re, mue)
        sc = float(np.max(np.abs(fe["phi"])))
        ell = dict(max_rel_diff_phi=float(np.max(np.abs(ge["P"] - fe["phi"])) / sc), rms_rel_diff_phi=_rms(ge["P"] - fe["phi"]) / sc,
                   max_rel_diff_phi_z=float(np.max(np.abs(ge["P_z"] - (-fe["Ur_over_r"]))) / max(1e-300, float(np.max(np.abs(fe["Ur_over_r"]))))),
                   phi_scale=sc, n_points=int(len(Re)))
        z0 = prob.z0_of(x)
        if z0 is not None:
            Rz = abs(z0) if abs(z0) > 1e-12 else 1e-12
            gz = gs.evaluate(np.array([Rz]), np.array([1.0 if z0 >= 0 else -1.0]))
            ell["s1_moment_phi0"] = dict(green=float(gz["P"][0]), target=-cl * z0 / 2, candidate=float(prob.eval_field(x, "phi", np.array([Rz]), np.array([1.0 if z0 >= 0 else -1.0]))[0]))
            ell["s1_moment_phi_z"] = dict(green=float(gz["P_z"][0]), target=0.5)
    except Exception as ex:
        ell = dict(error=repr(ex))
    finite_rho = [v for v in rho_max.values() if v == v]; finite_m = [v for v in m_max.values() if v == v]
    rho_all = max(finite_rho) if finite_rho else float("nan"); m_all = max(finite_m) if finite_m else float("nan")
    status = "ok" if (len(finite_rho) == len(eqs) and not degenerate) else ("invalid: all shells degenerate" if not finite_rho else f"partially degenerate ({len(degenerate)} shell/equation entries)")
    return dict(cl=cl, alpha=alpha, a_eff=a, Omega_max=Om_max, R_Omega_max=R_Ommax, mu_Omega_max=mu_Ommax, nR=nR, nmu=nmu, seed=seed,
                rho_max=rho_all, m_max=m_all, rho_max_by_eq=rho_max, m_max_by_eq=m_max, status=status, n_degenerate=len(degenerate),
                degenerate=[list(map(str, d)) for d in degenerate[:50]],
                rho_M_max=max(rho_max["Mr"], rho_max["Mt"], rho_max["Mz"]), rho_reduced_max=max(rho_max["q"], rho_max["eta"]),
                shells=shells, origin=origin, s_core=s_core, s_far=s_far, tail_int_F2=full, elliptic=ell,
                pressure=dict(lmax=ps.lmax, R_far=float(ps.edges[-1]), I_in_far=[float(v) for v in mc["I_in"][:3]], I_out_far=[float(v) for v in mc["I_out"][:3]],
                              tail_p=[float(v) for v in mc["tail_p"][:3]]))


def summary_line(v: Dict) -> str:
    return (f"rho_max={v['rho_max']:.3e} (M {v['rho_M_max']:.2e}, q {v['rho_max_by_eq']['q']:.2e}, eta {v['rho_max_by_eq']['eta']:.2e}, div {v['rho_max_by_eq']['div']:.1e}) "
            f"m_max={v['m_max']:.2e} a_eff={v['a_eff']:.3f} s_core={v['s_core']:.3f} s_far={v['s_far']:.3f} |Om|max={v['Omega_max']:.3e}@R={v['R_Omega_max']:.3f}")


def stagnation(prob: Problem, x, Rmax_factor=64.0, n_seed=40) -> Dict:
    """SPEC 6.6: zeros of W_m in the meridional half-plane within R <= Rmax_factor * a_eff: axis zeros of
    W_z(0, z) = c z + 2 phi(0, z) (sign changes on a fine axis grid refined by bisection) and off-axis zeros by 2D Newton
    from a seed grid.  For each zero: position, eigenvalues of D W_m, q, eta, and the checks q (1 + 2A) = 0 (axis, A = -phi_z)
    and q = 0, eta = 0 (off-axis).  Also the swirl-maximum condition (U^r/r = -1/2 at the maximum of |q|, SPEC 6.7)."""
    x = x.detach().cpu()
    cl = prob.cl_of(x)
    a, Om_max, _, _ = a_eff(prob, x)
    Rmax = Rmax_factor * a

    def W_at(r, z):
        r = np.atleast_1d(np.asarray(r, float)); z = np.atleast_1d(np.asarray(z, float))
        R = np.sqrt(r * r + z * z); Rs = np.where(R > 1e-12, R, 1e-12); mu = np.where(R > 1e-12, np.clip(z / Rs, -1, 1), 1.0)
        f = fields(prob, x, Rs, mu, cl)
        return cl * r + f["Ur"], cl * z + f["Uz"], f

    out = dict(a_eff=a, Rmax=Rmax, axis_zeros=[], offaxis_zeros=[])
    # axis zeros
    zg = np.concatenate([-np.geomspace(Rmax, 1e-4, 400), [0.0], np.geomspace(1e-4, Rmax, 400)])
    Wr, Wz, f = W_at(np.zeros_like(zg), zg)
    Wz = np.where(np.abs(Wz) < 1e-13 * (1 + np.abs(cl * zg)), 0.0, Wz)      # exact (or round-off) zeros, e.g. the origin in parity classes
    sgn = np.sign(Wz)
    exact = np.nonzero(sgn == 0)[0]
    for j in exact:
        _, _, fz = W_at(0.0, zg[j])
        A = float(fz["Ur_over_r"][0]); dUz = float(fz["Uz_z"][0])
        lr, lz = cl + A, cl + dUz
        typ = "source" if (lr > 0 and lz > 0) else ("sink" if (lr < 0 and lz < 0) else ("saddle_axial_inflow" if lz < 0 else "saddle_radial_inflow"))
        out["axis_zeros"].append(dict(z0=float(zg[j]), A=A, lambda_r=lr, lambda_z=lz, type=typ, q=float(fz["q"][0]), eta=float(fz["eta"][0]),
                                      check_q_1p2A=float(fz["q"][0] * (1 + 2 * A)), phi_z=-A, swirl_carrying_S1=bool(abs(1 + 2 * A) < 1e-3 and abs(fz["q"][0]) > 1e-6), exact_grid_zero=True))
    for j in np.nonzero(sgn[:-1] * sgn[1:] < 0)[0]:
        lo, hi = zg[j], zg[j + 1]
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if W_at(0.0, lo)[1][0] * W_at(0.0, mid)[1][0] <= 0:
                hi = mid
            else:
                lo = mid
        z0 = 0.5 * (lo + hi)
        _, _, fz = W_at(0.0, z0)
        A = float(fz["Ur_over_r"][0]); dUz = float(fz["Uz_z"][0])
        lr, lz = cl + A, cl + dUz
        typ = "source" if (lr > 0 and lz > 0) else ("sink" if (lr < 0 and lz < 0) else ("saddle_axial_inflow" if lz < 0 else "saddle_radial_inflow"))
        out["axis_zeros"].append(dict(z0=float(z0), A=A, lambda_r=lr, lambda_z=lz, type=typ, q=float(fz["q"][0]), eta=float(fz["eta"][0]),
                                      check_q_1p2A=float(fz["q"][0] * (1 + 2 * A)), phi_z=-A, swirl_carrying_S1=bool(abs(1 + 2 * A) < 1e-3 and abs(fz["q"][0]) > 1e-6)))
    # off-axis zeros: Newton from a seed grid in (r, z)
    rs = np.geomspace(0.05 * a, Rmax, n_seed); zs = np.concatenate([-np.geomspace(0.02 * a, Rmax, n_seed // 2), np.geomspace(0.02 * a, Rmax, n_seed // 2)])
    found = []
    for r0 in rs:
        for z0 in zs:
            r, z = float(r0), float(z0)
            ok = False
            for _ in range(40):
                Wr, Wz, f = W_at(r, z)
                J = np.array([[cl + f["Ur_r"][0], f["Ur_z"][0]], [f["Uz_r"][0], cl + f["Uz_z"][0]]])
                try:
                    d = np.linalg.solve(J, -np.array([Wr[0], Wz[0]]))
                except np.linalg.LinAlgError:
                    break
                r += d[0]; z += d[1]
                if r <= 1e-6 or math.hypot(r, z) > 2 * Rmax or not np.isfinite(r + z):
                    break
                if abs(d[0]) + abs(d[1]) < 1e-12 * (1 + abs(r) + abs(z)):
                    ok = True; break
            if ok:
                Wr, Wz, f = W_at(r, z)
                ok = math.hypot(Wr[0], Wz[0]) <= 1e-9 * (1 + cl * math.hypot(r, z)) and math.hypot(r, z) <= Rmax
            if ok and r > 1e-4 * a and all(math.hypot(r - p[0], z - p[1]) > 1e-6 * (1 + a) for p in found):
                found.append((r, z))
    for (r, z) in found:
        Wr, Wz, f = W_at(r, z)
        J = np.array([[cl + f["Ur_r"][0], f["Ur_z"][0]], [f["Uz_r"][0], cl + f["Uz_z"][0]]])
        ev = np.linalg.eigvals(J)
        re_ = sorted(float(e.real) for e in ev)
        typ = "source" if re_[0] > 0 else ("sink" if re_[1] < 0 else "saddle")
        out["offaxis_zeros"].append(dict(r=r, z=z, R=math.hypot(r, z), eig_re=[float(e.real) for e in ev], eig_im=[float(e.imag) for e in ev], type=typ,
                                         q=float(f["q"][0]), eta=float(f["eta"][0]), W_norm=float(math.hypot(Wr[0], Wz[0]))))
    out["zero_inventory"] = dict(axis={t: sum(1 for z in out["axis_zeros"] if z["type"] == t) for t in ("source", "sink", "saddle_axial_inflow", "saddle_radial_inflow")},
                                 offaxis={t: sum(1 for z in out["offaxis_zeros"] if z["type"] == t) for t in ("source", "sink", "saddle")})
    # swirl maximum condition (SPEC 6.7): at the maximum of |q| in the half-plane, U^r/r = -1/2
    R = np.geomspace(1e-3 * a, Rmax, 300); mu = np.linspace(-1, 1, 101)
    RR, MM = np.meshgrid(R, mu, indexing="ij")
    f = fields(prob, x, RR.ravel(), MM.ravel(), cl)
    j = int(np.argmax(np.abs(f["q"])))
    out["swirl_max"] = dict(q=float(f["q"][j]), R=float(RR.ravel()[j]), mu=float(MM.ravel()[j]), Ur_over_r=float(f["Ur_over_r"][j]),
                            defect=float(f["Ur_over_r"][j] + 0.5), min_Ur_over_r=float(np.min(f["Ur_over_r"])))
    # T1 diagnostics (lead note 15): max|q| relative to the source value K = q(0, z0) of the swirl-carrying S1 source (if any), whether the
    # source is a saddle of q (Hessian signature in (r, z)), and the size of the eta > 0 region (3D measure 2 pi r dr dz on the sampled half-plane)
    s1 = [z for z in out["axis_zeros"] if z["swirl_carrying_S1"]]
    t1 = {}
    if s1:
        z0 = s1[0]["z0"]; K = s1[0]["q"]
        h = 1e-3 * max(a, 1e-3)
        def qat(r_, z_):
            Rr = max(math.hypot(r_, z_), 1e-12); return float(fields(prob, x, np.array([Rr]), np.array([z_ / Rr]), cl)["q"][0])
        q_rr = (qat(2 * h, z0) - 2 * qat(h, z0) + qat(0.0, z0)) / h ** 2          # one-sided in r (q even in r)
        q_zz = (qat(0.0, z0 + h) - 2 * qat(0.0, z0) + qat(0.0, z0 - h)) / h ** 2
        # source jet (lead note 20): phi = z/2 + p_s s z + p_z z^3 + ... about the source (z measured from z0): p_z = phi_zzz/6, p_s = phi_sz;
        # exact closure needs p_s = -(3 p_z/4)(1 + K^2/(1 + c)^2), i.e. jet_ratio = -4 p_s/(3 p_z) - 1 = K^2/(1 + c)^2
        def phi_at(r_, z_):
            Rr = max(math.hypot(r_, z_), 1e-12); return float(fields(prob, x, np.array([Rr]), np.array([z_ / Rr]), cl)["phi"][0])
        hz = 2e-2 * max(a, 1e-3)
        p_z = (phi_at(0.0, z0 + 2 * hz) - 2 * phi_at(0.0, z0 + hz) + 2 * phi_at(0.0, z0 - hz) - phi_at(0.0, z0 - 2 * hz)) / (2 * hz ** 3) / 6.0
        p_s = ((phi_at(hz, z0 + hz) - phi_at(hz, z0 - hz)) - (phi_at(0.0, z0 + hz) - phi_at(0.0, z0 - hz))) / (2 * hz) / hz ** 2
        jet_ratio = (-4 * p_s / (3 * p_z) - 1) if abs(p_z) > 1e-14 else float("nan")
        t1 = dict(K=K, z0=z0, max_abs_q_over_K=float(np.max(np.abs(f["q"])) / max(abs(K), 1e-300)), max_abs_q_R=float(RR.ravel()[j]), max_abs_q_mu=float(MM.ravel()[j]),
                  q_rr=q_rr, q_zz=q_zz, source_is_saddle_of_q=bool(q_rr * q_zz < 0), q_peaks_at_source=bool(np.max(np.abs(f["q"])) <= 1.0001 * abs(K)),
                  p_z=p_z, p_s=p_s, jet_ratio=jet_ratio, jet_ratio_target=K * K / (1 + cl) ** 2, eta_sign_just_above_source=float(np.sign(fields(prob, x, np.array([abs(z0) + 0.05 * a]), np.array([1.0 if z0 + 0.05 * a >= 0 else -1.0]), cl)["eta"][0])))
    pos = f["eta"] > 0
    rr_ = (RR * np.sqrt(np.clip(1 - MM ** 2, 0, None))).ravel()
    t1["eta_positive"] = dict(fraction_of_points=float(np.mean(pos)), max_eta_pos=float(np.max(f["eta"])) if np.any(pos) else 0.0,
                             R_range=[float(np.min(RR.ravel()[pos])), float(np.max(RR.ravel()[pos]))] if np.any(pos) else None,
                             weighted_measure_proxy=float(np.sum(rr_[pos] * f["eta"][pos])) if np.any(pos) else 0.0)
    out["t1_diagnostics"] = t1
    return out
