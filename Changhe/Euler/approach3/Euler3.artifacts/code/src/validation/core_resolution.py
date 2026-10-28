"""SPEC v1.21 (a)-(c) core-resolution diagnostics (lead 2026-10-25T02:24Z item 2):
 (a) a_eff = 2 sqrt2 max|U| / max|Omega| (gauge-aligned maxima; the located continuous maximum of |Omega| when available), y_* = the point of
     largest |Omega|;
 (b) core-resolved sets: the balls B(y_*, a_eff/2), B(y_*, a_eff/4) (sigma_u = RMS(R_u)/RMS((1-c_l)U); a_max with the centre weight
     (1 + |y_*|)^(2 alpha + 1) and, reported alongside, the upper-radius weight (1 + |y_*| + radius)^(2 alpha + 1); sigma_Om restricted to
     B(y_*, a_eff/2)), and, when r_core 2^-5 > a_eff/16, dyadic shells extending the 7.1 family inward to a_eff/16 plus the ball r < a_eff/16;
 (c) quadrature stability: every RMS on an added set is recomputed with doubled radial and angular node counts; a change above 10 per cent
     marks the state "core unresolved" (fails every tier, not ordered under 7.3b). The a_eff stability across levels (L2 -> L3) is a ladder
     comparison made by the shortlist, not here.
Pressure at the ball points: the full-space Green solution of the training-grid source is computed on Chebyshev radii covering the ball
(P_lm(r), dP_lm/dr), interpolated in r (Chebyshev interpolation, exact to roundoff for the smooth radial coefficients on a small interval)
and synthesized at each point's own direction with the solid harmonics; the same formula as PressureSolver.solve, verified against it in
tests/test_core_resolution.py. Fields at the points: Model.fields_points (the representation's own derivatives)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver
from ..bases.solid_harmonics import eval_solid

DT = torch.float64


def ball_points(center, radius, n_rad, n_theta, n_phi, device):
    """Quadrature nodes and weights for B(center, radius): Gauss-Legendre in s on [0, radius] with weight s^2, Gauss-Legendre x uniform angles."""
    xs, ws = np.polynomial.legendre.leggauss(n_rad)
    s = 0.5 * radius * (xs + 1.0); w_s = 0.5 * radius * ws * s ** 2
    xt, wt = np.polynomial.legendre.leggauss(n_theta)
    phi = 2 * np.pi * (np.arange(n_phi) + 0.5) / n_phi
    ct = xt; st = np.sqrt(1 - ct ** 2)
    n = np.stack([np.outer(st, np.cos(phi)), np.outer(st, np.sin(phi)), np.repeat(ct[:, None], n_phi, 1)], -1).reshape(-1, 3)   # (Nang, 3)
    w_n = np.repeat(wt[:, None], n_phi, 1).reshape(-1) * (2 * np.pi / n_phi)
    pts = center[None, None, :] + s[:, None, None] * n[None, :, :]
    w = (w_s[:, None] * w_n[None, :]).reshape(-1)
    return torch.tensor(pts.reshape(-1, 3), dtype=DT, device=device), torch.tensor(w, dtype=DT, device=device)


def gradP_points(prob, z, c_l, omega, pts, n_cheb=24):
    """Full-space pressure gradient (and P) at arbitrary points pts (Np, 3) from the training-grid source: Chebyshev radii covering
    [min|pts|, max|pts|], Green solution there, Chebyshev interpolation of P_lm and dP_lm/dr in r, synthesis at the point directions."""
    model = prob.model; dev = pts.device
    alpha = alpha_of(float(c_l))
    rp = pts.norm(dim=1)
    r_lo = max(float(rp.min()) * 0.98, 0.0); r_hi = float(rp.max()) * 1.02
    if r_hi - r_lo < 1e-12 * r_hi:
        r_lo, r_hi = 0.9 * r_lo, 1.1 * r_hi
    k = np.arange(n_cheb); t_nodes = np.cos((2 * k + 1) * np.pi / (2 * n_cheb))              # Chebyshev nodes of the first kind in (-1, 1)
    r_nodes = 0.5 * (r_hi - r_lo) * t_nodes + 0.5 * (r_hi + r_lo)
    order = np.argsort(r_nodes); r_nodes = r_nodes[order]
    em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=r_nodes, ntheta=4, nphi=4, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=dev)
    ps = PressureSolver(model, p0=2 * alpha + 2, omega=float(omega), c_l=float(c_l), eval_model=em)
    f_src = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    _, _, Plm, dPlm = ps.solve(f_src)                                                           # (n_cheb, Nqp) at r_nodes
    # Chebyshev interpolation in t = (2 r - (r_hi + r_lo)) / (r_hi - r_lo)
    t_n = torch.tensor((2 * r_nodes - (r_hi + r_lo)) / (r_hi - r_lo), dtype=DT, device=dev)
    t_p = (2 * rp - (r_hi + r_lo)) / (r_hi - r_lo)
    def cheb_vander(t, n):
        V = [torch.ones_like(t), t]
        for j in range(2, n):
            V.append(2 * t * V[-1] - V[-2])
        return torch.stack(V[:n], 1)
    Vn = cheb_vander(t_n, n_cheb); Vp = cheb_vander(t_p, n_cheb)
    coefP = torch.linalg.solve(Vn, Plm); coefdP = torch.linalg.solve(Vn, dPlm)
    Plm_p = Vp @ coefP; dPlm_p = Vp @ coefdP                                                   # (Np, Nqp)
    n_p = pts / rp[:, None]
    A0, A1, _ = eval_solid(n_p, ps.pmodes, ps.Lf, 1)                                           # (Np, Nqp), (3, Np, Nqp)
    P = (Plm_p * A0).sum(1)
    radial = ((dPlm_p - ps.pl[None, :] * Plm_p / rp[:, None]) * A0).sum(1)
    gradP = radial[None, :] * n_p.T + torch.einsum('pq,ipq->ip', Plm_p / rp[:, None], A1)
    return P, gradP, dict(r_lo=r_lo, r_hi=r_hi, n_cheb=n_cheb, interp_cond=float(torch.linalg.cond(Vn)))


def _terms_at_points(prob, z, c_l, omega, pts):
    from .spec_diagnostics import five_term_split, vorticity_split
    model = prob.model
    F = model.fields_points(z, pts, need_vort=True)
    P, gradP, info = gradP_points(prob, z, c_l, omega, pts)
    T = five_term_split(F, gradP); V = vorticity_split(F)
    return F, T, V, info


def _ball_rms_set(prob, z, c_l, omega, center, radius, n_rad, n_theta, n_phi):
    pts, w = ball_points(center, radius, n_rad, n_theta, n_phi, prob.model.r.device)
    F, T, V, info = _terms_at_points(prob, z, c_l, omega, pts)
    def rms(X):
        return math.sqrt(float(((X ** 2).sum(0) * w).sum() / w.sum()))
    Ru = sum(T); ROm = sum(V)
    return dict(rms_Ru=rms(Ru), rms_T1=rms(T[0]), rms_U=rms(F['U']), rms_ROm=rms(ROm), rms_Om=rms(F['Om']), rms_T=[rms(t) for t in T],
                n_points=int(pts.shape[0]), pressure_interp_cond=info["interp_cond"])


def core_resolution(prob, z, c_l, omega, y_star, max_U, max_Omega, core_ball_radius, n_rad=6, n_theta=8, n_phi=16, inner_shells=True, n_per_shell=6):
    """Returns the v1.21 dict. core_ball_radius: the 7.1 core ball radius of the holdout family (r_core 2^-5 rounded to the dyadic edge)."""
    c_lf, omf = float(c_l), float(omega); alpha = alpha_of(c_lf)
    dev = prob.model.r.device
    a_eff = 2 * math.sqrt(2) * float(max_U) / max(float(max_Omega), 1e-300)
    ys = np.asarray(y_star, dtype=float); r_star = float(np.linalg.norm(ys))
    out = dict(a_eff=a_eff, y_star=[float(v) for v in ys], r_star=r_star, max_U=float(max_U), max_Omega=float(max_Omega), core_ball_radius=core_ball_radius,
               core_ball_over_a_eff=core_ball_radius / a_eff, balls={}, inner_shells=None, note="SPEC v1.21 (a)-(c); a_max centre weight (1 + |y_*|)^(2 alpha + 1), upper weight (1 + |y_*| + radius)^(2 alpha + 1)")
    changes = []
    for name, frac in (("half", 0.5), ("quarter", 0.25)):
        R = frac * a_eff
        s1 = _ball_rms_set(prob, z, c_lf, omf, ys, R, n_rad, n_theta, n_phi)
        s2 = _ball_rms_set(prob, z, c_lf, omf, ys, R, 2 * n_rad, 2 * n_theta, 2 * n_phi)
        ch = {k: abs(s1[k] - s2[k]) / max(abs(s2[k]), 1e-300) for k in ("rms_Ru", "rms_T1", "rms_ROm", "rms_Om")}
        changes += [ch["rms_Ru"], ch["rms_T1"]]
        b = dict(radius=R, sigma_u=s2["rms_Ru"] / max(s2["rms_T1"], 1e-300), a_max_centre=(1 + r_star) ** (2 * alpha + 1) * s2["rms_Ru"],
                 a_max_upper=(1 + r_star + R) ** (2 * alpha + 1) * s2["rms_Ru"], sigma_Om=s2["rms_ROm"] / max(s2["rms_Om"], 1e-300),
                 rms=s2, rms_single=s1, doubling_rel_change=ch, resolved=bool(ch["rms_Ru"] < 0.1 and ch["rms_T1"] < 0.1))
        out["balls"][name] = b
    a16 = a_eff / 16.0
    if inner_shells and core_ball_radius > a16:
        from .holdout import HoldoutGrid
        from .spec_diagnostics import spec_diagnostics
        j0 = int(math.floor(math.log2(a16))); j1 = int(round(math.log2(core_ball_radius)))
        edges = [(0.0, 2.0 ** j0)] + [(2.0 ** j, 2.0 ** (j + 1)) for j in range(j0, j1)]
        model = prob.model; Lx = getattr(model, "L_ext", model.L)
        res_sets = []
        for lvl in (1, 2):
            hg = HoldoutGrid(model, r_core=model.R0, n_per_shell=n_per_shell * lvl, ntheta=(2 * Lx + 12) * lvl, nphi=(4 * Lx + 18) * lvl, edges=edges)
            sd = spec_diagnostics(prob, z, holdout=hg, extras=False)
            res_sets.append(sd)
        s1, s2 = res_sets
        chR = [abs(a_ - b_) / max(abs(b_), 1e-300) for a_, b_ in zip(s1["rms"]["R_u"], s2["rms"]["R_u"])]
        chT = [abs(a_ - b_) / max(abs(b_), 1e-300) for a_, b_ in zip(s1["rms"]["T"][0], s2["rms"]["T"][0])]
        changes += chR + chT
        out["inner_shells"] = dict(edges=edges, sigma_u=s2["sigma_u"], a_fixed_gauge=s2["a_fixed_gauge"], rms_Ru=s2["rms"]["R_u"], rms_T1=s2["rms"]["T"][0],
                                   doubling_rel_change_Ru=chR, doubling_rel_change_T1=chT, sigma_u_max=max(v for v in s2["sigma_u"] if v is not None), a_max=max(s2["a_fixed_gauge"]))
    out["max_doubling_rel_change"] = max(changes) if changes else None
    out["core_resolved"] = bool(out["max_doubling_rel_change"] is not None and out["max_doubling_rel_change"] < 0.1)
    vals_s = [out["balls"]["half"]["sigma_u"], out["balls"]["quarter"]["sigma_u"]] + ([out["inner_shells"]["sigma_u_max"]] if out["inner_shells"] else [])
    vals_a = [out["balls"]["half"]["a_max_centre"], out["balls"]["quarter"]["a_max_centre"]] + ([out["inner_shells"]["a_max"]] if out["inner_shells"] else [])
    vals_au = [out["balls"]["half"]["a_max_upper"], out["balls"]["quarter"]["a_max_upper"]] + ([out["inner_shells"]["a_max"]] if out["inner_shells"] else [])
    out.update(sigma_u_max_added=max(vals_s), a_max_added_centre=max(vals_a), a_max_added_upper=max(vals_au))
    return out


def core_text(cr):
    if not cr or "a_eff" not in cr:
        return "core resolution n/a"
    b = cr["balls"]; h = b["half"]; q = b["quarter"]
    s = (f"a_eff={cr['a_eff']:.4f} (max|U| {cr['max_U']:.3f}, max|Omega| {cr['max_Omega']:.2f}), |y_*|={cr['r_star']:.3f}, core ball/a_eff={cr['core_ball_over_a_eff']:.2f} | "
         f"B(y_*, a_eff/2): sigma_u {h['sigma_u']:.3f}, a_max centre {h['a_max_centre']:.3f} upper {h['a_max_upper']:.3f}, sigma_Om {h['sigma_Om']:.3f}, doubling change {max(h['doubling_rel_change'].values()):.1e} | "
         f"B(y_*, a_eff/4): sigma_u {q['sigma_u']:.3f}, a_max centre {q['a_max_centre']:.3f} upper {q['a_max_upper']:.3f}, doubling change {max(q['doubling_rel_change'].values()):.1e}")
    if cr.get("inner_shells"):
        i = cr["inner_shells"]
        s += f" | inner shells to a_eff/16 ({len(i['edges'])} sets): sigma_u max {i['sigma_u_max']:.3f}, a_max {i['a_max']:.3f}, doubling change {max(i['doubling_rel_change_Ru'] + i['doubling_rel_change_T1']):.1e}"
    else:
        s += " | no inner shells added (core ball <= a_eff/16)"
    s += f" | core {'RESOLVED' if cr['core_resolved'] else 'UNRESOLVED'} (max doubling change {cr['max_doubling_rel_change']:.1e})"
    return s
