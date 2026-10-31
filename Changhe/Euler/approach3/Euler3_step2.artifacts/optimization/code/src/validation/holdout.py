"""Holdout evaluation grid and SPEC 7.1 shells with exact volume quadrature (astra review, finding 4).

Shells: core ball [0, r_core 2^-5) and dyadic shells [2^j, 2^(j+1)) covering [r_core 2^-5, r_max]; each shell carries
Gauss-Legendre nodes in r (normalized volume measure r^2 dr) times an angular Gauss grid with a rotated azimuth
(phi0 = pi/(2 nphi)) and more theta nodes than the training grid: none of these points was used for training.
Fields come from a Model built on the holdout radii; the pressure is the Green solution with the source sampled on the
training nodes and evaluated at the holdout radii/angles (PressureSolver(eval_model=...)); grad P(0) from l = 1 moments."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of
from ..pressure.poisson_sh import PressureSolver

DT = torch.float64


def holdout_radii(r_core, r_max, n_per_shell=6, core_octaves=5):
    """Shell edges and Gauss-Legendre radii per shell (core ball + dyadic shells); returns (edges, r, w_vol, shell_id)."""
    lo = r_core * 2.0 ** (-core_octaves)
    j0 = int(math.floor(math.log2(lo))); j1 = int(math.ceil(math.log2(r_max)))
    edges = [(0.0, 2.0 ** j0)] + [(2.0 ** j, 2.0 ** (j + 1)) for j in range(j0, j1)]
    xg, wg = np.polynomial.legendre.leggauss(n_per_shell)
    r, w, sid = [], [], []
    for k, (a, b) in enumerate(edges):
        rr = 0.5 * (b - a) * xg + 0.5 * (a + b); ww = 0.5 * (b - a) * wg
        r.append(rr); w.append(rr ** 2 * ww / ((b ** 3 - a ** 3) / 3.0)); sid += [k] * n_per_shell   # normalized volume measure
    return edges, np.concatenate(r), np.concatenate(w), np.array(sid)


class HoldoutGrid:
    def __init__(self, train_model: Model, r_core, r_max=None, n_per_shell=6, ntheta=None, nphi=None, device=None, edges=None):
        """edges: optional explicit shell edges [(a, b), ...] (e.g. a reference grid's edges scaled by a dilation factor for
        the T04 regression); default absolute dyadic shells around r_core (SPEC 7.1)."""
        device = device or train_model.r.device
        r_max = r_max or float(train_model.r.max())
        if edges is not None:
            xg, wg = np.polynomial.legendre.leggauss(n_per_shell)
            rr_, ww_, ss_ = [], [], []
            for k, (a, b) in enumerate(edges):
                rr = 0.5 * (b - a) * xg + 0.5 * (a + b); ww = 0.5 * (b - a) * wg
                rr_.append(rr); ww_.append(rr ** 2 * ww / ((b ** 3 - a ** 3) / 3.0)); ss_ += [k] * n_per_shell
            self.edges, r, wv, sid = list(edges), np.concatenate(rr_), np.concatenate(ww_), np.array(ss_)
        else:
            self.edges, r, wv, sid = holdout_radii(r_core, r_max, n_per_shell)
        L = train_model.L; Lx = getattr(train_model, "L_ext", L)
        ntheta = ntheta or (2 * Lx + 12); nphi = nphi or (4 * Lx + 18)
        self.model = Model(L=L, Nk=train_model.Nk, m_parity=train_model.m_parity, R0=train_model.R0, r_nodes=r,
                           ntheta=ntheta, nphi=nphi, c_l=train_model.c_l0, omega=train_model.omega0,
                           free_params=train_model.free_params, channels=train_model.channels, device=device, phi0=math.pi / (2 * nphi))
        self.w_vol = torch.tensor(wv, dtype=DT, device=device)
        self.shell_id = torch.tensor(sid, dtype=torch.long, device=device)
        self.n_shells = len(self.edges); self.n = self.n_shells
        self.rmid = [math.sqrt(max(a, b / 64.0) * b) for (a, b) in self.edges]
        self.w_ang = self.model.grid.w / (4 * math.pi)
        self.masks = [self.shell_id == k for k in range(self.n_shells)]

    def rms(self, X):
        sq = (X ** 2).sum(0) if X.dim() == 3 else X ** 2
        per_node = (sq * self.w_ang[None, :]).sum(1)
        return [((per_node[m] * self.w_vol[m]).sum() / self.w_vol[m].sum()).sqrt().item() for m in self.masks]

    def maxabs(self, X):
        a = X.norm(dim=0) if X.dim() == 3 else X.abs()
        return [a[m].max().item() for m in self.masks]

    def pressure_solver(self, train_model, c_l, omega):
        return PressureSolver(train_model, p0=2 * alpha_of(float(c_l)) + 2, omega=float(omega), c_l=float(c_l), eval_model=self.model)


def half_offset_edges(r_core, r_max, core_octaves=5):
    """SPEC 7.3a half-offset dyadic family: core ball [0, 2^(j0+1/2)) and shells [2^(j+1/2), 2^(j+3/2)) covering
    [r_core 2^-core_octaves, r_max]; the standard family of holdout_radii is [2^j, 2^(j+1))."""
    lo = r_core * 2.0 ** (-core_octaves)
    j0 = int(math.floor(math.log2(lo) - 0.5)); j1 = int(math.ceil(math.log2(r_max) - 0.5))
    return [(0.0, 2.0 ** (j0 + 0.5))] + [(2.0 ** (j + 0.5), 2.0 ** (j + 1.5)) for j in range(j0, j1)]


def sphere_diagnostics(prob, z, radii, ntheta=None, nphi=None, device=None):
    """Single-sphere momentum ratios (SPEC 7.3a: the largest single-sphere rho_u is reported with the two shell families).
    For every radius r_j: rho_u(r_j) = RMS_{S_r}(R_u) / sum_i RMS_{S_r}(T_i) and rho_nl(r_j) = RMS_{S_r}(R_u)/(RMS(T4)+RMS(T5)),
    with the angular Gauss weights of a rotated holdout grid; the pressure is the full-space Green solution of the source on
    the training nodes evaluated at the sphere radii. Returns per-sphere lists and the maxima with their radii."""
    from .spec_diagnostics import five_term_split
    from ..equations import residuals as res
    model = prob.model
    device = device or model.r.device
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega)
    L = model.L; Lx = getattr(model, "L_ext", L)
    ntheta = ntheta or (2 * Lx + 12); nphi = nphi or (4 * Lx + 18)
    radii = np.asarray(sorted(float(v) for v in radii))
    em = Model(L=L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=radii, ntheta=ntheta, nphi=nphi, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=device, phi0=math.pi / (2 * nphi))
    F = em.fields_grid(z, need_vort=False)
    ps = PressureSolver(model, p0=2 * alpha_of(c_lf) + 2, omega=omf, c_l=c_lf, eval_model=em)
    f_src = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    P, gradP, _, _ = ps.solve(f_src)
    T = five_term_split(F, gradP); Ru = sum(T)
    w = em.grid.w / (4 * math.pi)
    def rms(X):
        return ((X ** 2).sum(0) * w[None, :]).sum(1).sqrt()
    rT = [rms(t) for t in T]; rRu = rms(Ru)
    den5 = sum(rT); dnl = rT[3] + rT[4]
    rho_u = (rRu / den5.clamp_min(1e-300)).cpu().numpy(); rho_nl = (rRu / dnl.clamp_min(1e-300)).cpu().numpy()
    ju = int(np.argmax(rho_u)); jn = int(np.argmax(rho_nl))
    return dict(radii=[float(v) for v in radii], rho_u=[float(v) for v in rho_u], rho_nl=[float(v) for v in rho_nl],
                rms_R_u=[float(v) for v in rRu.cpu().numpy()], den5=[float(v) for v in den5.cpu().numpy()],
                rho_u_max=float(rho_u[ju]), r_at_rho_u_max=float(radii[ju]), rho_nl_max=float(rho_nl[jn]), r_at_rho_nl_max=float(radii[jn]),
                ntheta=ntheta, nphi=nphi, note="single spheres are diagnostics (SPEC 7.3a), not shell acceptance numbers")


def exchange_radii(r_core, r_lo, r_hi):
    """Exchange-grid radii r_core 2^(j/4) (SPEC 10) restricted to [r_lo, r_hi]."""
    j = np.arange(-24, 81)
    r = r_core * 2.0 ** (j / 4.0)
    return [float(v) for v in r if r_lo <= v <= r_hi]


def two_family_summary(sdh, sdh_half, sph):
    """Compact dict of the quantities every summary line must carry (lead 22:40Z item (c))."""
    g = sdh["global_"]; gh = (sdh_half or {}).get("global_", {})
    both = [v for v in (g.get("rho_u_max"), gh.get("rho_u_max")) if v is not None]
    bothnl = [v for v in (g.get("rho_nl_max"), gh.get("rho_nl_max")) if v is not None]
    return dict(rho_u_max_std=g.get("rho_u_max"), rho_u_max_half=gh.get("rho_u_max"), rho_u_max_both=(max(both) if both else None),
                rho_nl_max_std=g.get("rho_nl_max"), rho_nl_max_half=gh.get("rho_nl_max"), rho_nl_max_both=(max(bothnl) if bothnl else None),
                sphere_rho_u_max=(sph or {}).get("rho_u_max"), sphere_r_at_max=(sph or {}).get("r_at_rho_u_max"),
                sphere_rho_nl_max=(sph or {}).get("rho_nl_max"), sphere_r_at_nl_max=(sph or {}).get("r_at_rho_nl_max"),
                rho_lin_max_std=g.get("rho_lin_max"), rho_lin_max_half=gh.get("rho_lin_max"), rho_sp_max_std=g.get("rho_sp_max"), rho_sp_max_half=gh.get("rho_sp_max"),
                rho_lin_max_r1_std=g.get("rho_lin_max_r1"), rho_sp_max_r1_std=g.get("rho_sp_max_r1"), rho_lin_max_r1_half=gh.get("rho_lin_max_r1"), rho_sp_max_r1_half=gh.get("rho_sp_max_r1"),
                d30_Ru_over_T1_r1=g.get("d30_Ru_over_T1_r1"), d30_ROm_over_Om=g.get("d30_ROm_over_Om"), d30_Ru_over_T1_r1_half=gh.get("d30_Ru_over_T1_r1"),
                gram_gamma_std=(sdh.get("gram") or {}).get("gamma"), gram_a_std=(sdh.get("gram") or {}).get("a_rms_L"), gram_b_std=(sdh.get("gram") or {}).get("b_rms_N"),
                gram_check_max=(max([v for v in ((sdh.get("gram") or {}).get("check_rel") or []) if v is not None] or [None])),
                sigma_u_max_std=g.get("sigma_u_max"), sigma_u_max_shell_std=g.get("sigma_u_max_shell"), sigma_u_max_half=gh.get("sigma_u_max"), sigma_u_max_shell_half=gh.get("sigma_u_max_shell"),
                sigma_u_max_r1_std=g.get("sigma_u_max_r1"), sigma_Om=g.get("sigma_Om"), a_max_std=g.get("a_max"), a_max_shell_std=g.get("a_max_shell"), a_max_half=gh.get("a_max"),
                origin_U_rms=g.get("origin_U_rms"), origin_B=g.get("origin_B"), origin_L=g.get("origin_L"), structure=sdh.get("structure"),
                peak_max_std=g.get("peak_max"), max_abs_Omega=(sdh.get("guards") or {}).get("N2_max_abs_Omega"), max_U=(sdh.get("guards") or {}).get("N4_max_U"),
                max_DU=(sdh.get("guards") or {}).get("N4_max_DU"))


def structure_text(tf):
    st = (tf or {}).get("structure") or {}
    def f(v, fmt="%.3f"):
        return (fmt % v) if isinstance(v, (int, float)) else "n/a"
    gs = st.get("grad_scale_T4_over_U") or []
    return (f"grad scale RMS T4/RMS U (origin ball, shells 1, 2)={' '.join(f(v, '%.2f') for v in gs)} | ||U||_L2(r<1)={f(st.get('U_L2_r_lt_1'))} | helicity r<1={f(st.get('helicity_r_lt_1'), '%+.3e')} "
            f"1<=r<8={f(st.get('helicity_1_8'), '%+.3e')} | r_core(half U_rms)={f(st.get('r_core_half'), '%.3g')} | axial/planar vorticity={f(st.get('axial_to_planar_vorticity'))} | dominant m core={st.get('core_dominant_m')} "
            f"tail={st.get('tail_dominant_m')} | near-linear={st.get('near_linear')} (b/a core min {f(st.get('b_over_a_core_min'), '%.2f')} max {f(st.get('b_over_a_core_max'), '%.2f')}) | peak factor max={f(tf.get('peak_max_std'), '%.1f')} "
            f"max|U|={f(tf.get('max_U'))} max|Omega|={f(tf.get('max_abs_Omega'))} max|DU|={f(tf.get('max_DU'))}")


def summary_text(tf):
    def f(v, fmt="%.3e"):
        return (fmt % v) if isinstance(v, (int, float)) else "n/a"
    return (f"rho_u_max std={f(tf['rho_u_max_std'])} half={f(tf['rho_u_max_half'])} | rho_nl_max(all shells) std={f(tf['rho_nl_max_std'])} "
            f"half={f(tf['rho_nl_max_half'])} | single-sphere rho_u max={f(tf['sphere_rho_u_max'])} at r={f(tf['sphere_r_at_max'], '%.3g')} "
            f"rho_nl max={f(tf['sphere_rho_nl_max'])} at r={f(tf['sphere_r_at_nl_max'], '%.3g')} | rho_lin_max std={f(tf.get('rho_lin_max_std'))} half={f(tf.get('rho_lin_max_half'))} "
            f"(r<1: {f(tf.get('rho_lin_max_r1_std'))}) | rho_sp_max std={f(tf.get('rho_sp_max_std'))} half={f(tf.get('rho_sp_max_half'))} (r<1: {f(tf.get('rho_sp_max_r1_std'))}) "
            f"| d30 ||R_u||/||(1-c_l)U|| (r<1)={f(tf.get('d30_Ru_over_T1_r1'), '%.3f')} ||R_Om||/||Om||={f(tf.get('d30_ROm_over_Om'), '%.3f')} | Gram closure max={f(tf.get('gram_check_max'), '%.1e')} "
            f"| v1.19 sigma_u_max std={f(tf.get('sigma_u_max_std'), '%.3f')} at {tf.get('sigma_u_max_shell_std')} half={f(tf.get('sigma_u_max_half'), '%.3f')} at {tf.get('sigma_u_max_shell_half')} (r<1: {f(tf.get('sigma_u_max_r1_std'), '%.3f')}) sigma_Om={f(tf.get('sigma_Om'), '%.3f')} "
            f"| v1.17 a_max std={f(tf.get('a_max_std'), '%.3f')} at {tf.get('a_max_shell_std')} half={f(tf.get('a_max_half'), '%.3f')}; origin ball U_rms={f(tf.get('origin_U_rms'), '%.3f')} B={f(tf.get('origin_B'), '%.3f')} L={f(tf.get('origin_L'), '%.3f')}")
