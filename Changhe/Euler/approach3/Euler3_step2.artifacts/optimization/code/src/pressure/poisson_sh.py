"""Full-space decaying pressure from -Lap P = f by spherical-harmonic Green's function (SPEC 5.2):

  P_lm(r) = 1/(2l+1) [ r^(-l-1) int_0^r s^(l+2) f_lm(s) ds + r^l int_r^inf s^(1-l) f_lm(s) ds ].

Twisted frame (SPEC 5.3). For the fields of this representation every azimuthal order m of the source carries the
phase m beta(r), beta = omega/(2 c_l) log(1 + r^2/R0^2): f(r, theta, phi) = ftw(r, theta, phi + beta(r)) with ftw
smooth in the map variable x. So the true-azimuth coefficients are
    f^c_lm = ftw^c cos(m beta) + ftw^s sin(m beta),   f^s_lm = -ftw^c sin(m beta) + ftw^s cos(m beta),
and the Green integrals are applied to the smooth factored ftw with the oscillating factors cos(m beta(s)),
sin(m beta(s)) inside the kernels. Kernels are integrated by composite Gauss-Legendre in lambda = log s with panel
lengths <= pi/(M omega/c_l) (resolving the oscillation), in r on the innermost interval [0, r_0], and on the
exterior (lambda > log r_last, exponentially decaying integrand) likewise in lambda until the integrand is below
1e-18 of its start; the factored source is extrapolated there by its Chebyshev interpolant.
Factoring: f_lm = (s/R0)^-p0 (r/s)^l_eff fhat_lm with s = sqrt(r^2+R0^2), l_eff = l (l <= 4) else 4 or 5 by parity
(fhat smooth in x at both ends, limited roundoff amplification). Kernels are evaluated in log space (no overflow).
Both radial terms are kept so that dP/dr follows exactly: dP_lm/dr = (1/r) [ -(l+1) term1 + l term2 ].
Cartesian gradient: grad P = sum_q [ (dP_q/dr - l P_q/r) n P_q(n) + (P_q/r) grad P_q(n) ]  (regular solid harmonics).

D6FP (degree-6 free-parameter campaign, 2026-10-28; frozen Euler3 version kept as poisson_sh.py.frozen_e3):
  The quadrature GEOMETRY (points, weights, Chebyshev interpolation matrix, kernel split masks) is built once in numpy from the
  base parameters with safety margins (kappa_margin on the oscillation resolution, alpha_margin on the exterior length).
  Every parameter-dependent TABLE (Green kernel tables Qc, Qs with the oscillating factors cos/sin(m beta(s)) and the envelope
  (s/R0)^-p0 inside, the node factors sfac = (s/R0)^p0, the frame rotation cos/sin(m beta(node)), the volume weights wr and the
  l = 1 origin moments) is built in torch by build_tables(c_l, omega) from 0-dim tensors, so that torch.func.jvp / autograd
  differentiate the pressure, its gradient, grad P(0) and the volume integrals exactly with respect to c_l and omega
  (SPEC 4.5, PROMPT section 3). The base tables (at the constructor's parameters) are self.tables; solve(f, tables=None)
  uses them unless other tables are passed. Same formulas, same quadrature as the frozen version at kappa_margin = alpha_margin = 1."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..bases.solid_harmonics import mode_list, eval_solid
from ..bases.radial import x_from_r

DT = torch.float64


def _cheb_vander(x, N):
    V = np.zeros((len(x), N))
    t = 2 * x - 1
    V[:, 0] = 1
    if N > 1:
        V[:, 1] = t
    for k in range(2, N):
        V[:, k] = 2 * t * V[:, k - 1] - V[:, k - 2]
    return V


def _leff(l):
    return l if l <= 4 else (4 if l % 2 == 0 else 5)


TANGENT_FP64 = False                                                  # D6FP: True = double-double primal values, float64 forward-mode tangents (cost option; lead 23:08Z)


class _SolveDD(torch.autograd.Function):
    """D6FP D1 v1: double-double pressure chain with exact forward-mode tangents (multilinear structure) and float64 reverse mode.
    With TANGENT_FP64 the tangents are the float64 chain's (torch.func.jvp of _solve_fp64)."""
    generate_vmap_rule = True

    @staticmethod
    def forward(fh, fl, Qc, Qs, sfac, cosb, sinb, solver):
        return solver._solve_dd_core(fh, fl, Qc, Qs, sfac, cosb, sinb)

    @staticmethod
    def setup_context(ctx, inputs, output):
        fh, fl, Qc, Qs, sfac, cosb, sinb, solver = inputs
        ctx.solver = solver
        ctx.save_for_backward(fh, fl, Qc, Qs, sfac, cosb, sinb)
        ctx.save_for_forward(fh, fl, Qc, Qs, sfac, cosb, sinb)

    @staticmethod
    def jvp(ctx, fh_dot, fl_dot, Qc_dot, Qs_dot, sfac_dot, cosb_dot, sinb_dot, _solver_dot):
        fh, fl, Qc, Qs, sfac, cosb, sinb = ctx.saved_tensors
        S = ctx.solver
        if TANGENT_FP64:
            prim = (fh + fl, Qc, Qs, sfac, cosb, sinb)
            tang = tuple(t if t is not None else torch.zeros_like(pz) for t, pz in zip(((fh_dot if fh_dot is not None else 0) + (fl_dot if fl_dot is not None else 0) if (fh_dot is not None or fl_dot is not None) else None, Qc_dot, Qs_dot, sfac_dot, cosb_dot, sinb_dot), prim))
            def f64(f_, Qc_, Qs_, sf_, cb_, sb_):
                return S._solve_fp64(f_, dict(Qc=Qc_, Qs=Qs_, sfac=sf_, cosb=cb_, sinb=sb_))
            return torch.func.jvp(f64, prim, tang)[1]
        outs = None
        def acc(o):
            nonlocal outs
            outs = o if outs is None else tuple(a + b for a, b in zip(outs, o))
        if fh_dot is not None or fl_dot is not None:
            acc(S._solve_dd_core(fh_dot if fh_dot is not None else torch.zeros_like(fh), fl_dot if fl_dot is not None else torch.zeros_like(fl), Qc, Qs, sfac, cosb, sinb))
        if Qc_dot is not None or Qs_dot is not None:
            acc(S._solve_dd_core(fh, fl, Qc_dot if Qc_dot is not None else torch.zeros_like(Qc), Qs_dot if Qs_dot is not None else torch.zeros_like(Qs), sfac, cosb, sinb))
        if sfac_dot is not None:
            acc(S._solve_dd_core(fh, fl, Qc, Qs, sfac_dot, cosb, sinb))
        if cosb_dot is not None or sinb_dot is not None:
            acc(S._solve_dd_core(fh, fl, Qc, Qs, sfac, cosb_dot if cosb_dot is not None else torch.zeros_like(cosb), sinb_dot if sinb_dot is not None else torch.zeros_like(sinb)))
        if outs is None:
            outs = tuple(torch.zeros_like(o) for o in S._solve_dd_core(fh, fl, Qc, Qs, sfac, cosb, sinb))
        return outs

    @staticmethod
    def backward(ctx, gP, gG, gPlm, gdPlm):
        fh, fl, Qc, Qs, sfac, cosb, sinb = ctx.saved_tensors
        S = ctx.solver
        with torch.enable_grad():
            ins = [t.detach().requires_grad_(True) for t in (fh, fl, Qc, Qs, sfac, cosb, sinb)]
            T = dict(Qc=ins[2], Qs=ins[3], sfac=ins[4], cosb=ins[5], sinb=ins[6])
            outs = S._solve_fp64(ins[0] + ins[1], T)
            grads = [g for g in (gP, gG, gPlm, gdPlm)]
            pairs = [(o, g) for o, g in zip(outs, grads) if g is not None]
            gi = torch.autograd.grad([o for o, _ in pairs], ins, [g for _, g in pairs], allow_unused=True)
        return tuple(gi) + (None,)


class PressureSolver:
    def __init__(self, model, p0, nq=32, m_parity=None, Lf=None, device=None, omega=None, c_l=None, max_points=2000000,
                 eval_model=None, ext_factor=1.0, kappa_margin=2.0, alpha_margin=0.7, point_chunk=None, exterior_monopole=False):
        """eval_model: optional Model whose radii/angular grid receive P and grad P (holdout evaluation); the source is
        always sampled on `model` (training nodes, Chebyshev-Gauss in x) and interpolated.
        kappa_margin, alpha_margin (D6FP): the quadrature geometry resolves oscillations up to kappa_margin * |omega/c_l| and the
        exterior length is sized for the decay rate alpha_margin * alpha, so that tables rebuilt at nearby trial parameters
        (build_tables) keep the same accuracy; 1.0 and 1.0 reproduce the frozen Euler3 geometry exactly."""
        self.model = model
        self.eval_model = eval_model if eval_model is not None else model
        self.p0 = float(p0)
        self.R0 = model.R0
        device = device or model.r.device
        self.device = device
        Lf = Lf if Lf is not None else model.Lf
        par = m_parity if m_parity is not None else model.m_parity
        self.Lf = Lf
        self.omega = float(model.omega0 if omega is None else omega)
        self.c_l = float(model.c_l0 if c_l is None else c_l)
        self.kappa = self.omega / self.c_l                      # omega/c_l
        self.kappa_margin, self.alpha_margin = float(kappa_margin), float(alpha_margin)
        # D6FP (lead decision 2026-10-28T22:39Z): exterior-only MONOPOLE at the evaluation radii beyond the last source node (the far anchor rows):
        # P_00(r) = -(1/r) int_r^inf s^2 F_00 ds + int_r^inf s F_00 ds, d_r P_00 = (1/r^2) int_r^inf s^2 F_00 ds, exact when the source monopole
        # vanishes (it does for the represented field); removes the rounding of the interior monopole amplified by r at the anchors. Off by default.
        self.exterior_monopole = bool(exterior_monopole)
        # D6FP: immutable geometry anchors (verifier note 2026-10-28T20:51Z): the layout is sized for |kappa| <= geometry_kappa_max and
        # decay rate p0 - 2 >= geometry_p0m2_min; set_parameters never moves them, so the margin test cannot ratchet.
        self.geometry_kappa_max = abs(self.kappa) * self.kappa_margin
        self.geometry_p0m2_min = (self.p0 - 2.0) * self.alpha_margin
        self.geometry_id = f"kmax{self.geometry_kappa_max:.6g}_p0m2min{self.geometry_p0m2_min:.6g}"
        self.geometry_base = dict(c_l=self.c_l, omega=self.omega, kappa=self.kappa, p0=self.p0)
        self.pmodes = mode_list(Lf, par, l_min=0)
        self.pl = torch.tensor([float(l) for (l, m, t) in self.pmodes], dtype=DT, device=device)
        self.pm = torch.tensor([m for (l, m, t) in self.pmodes], dtype=torch.long, device=device)
        self.pl_idx = [l for (l, m, t) in self.pmodes]
        self.pl_long = torch.tensor(self.pl_idx, dtype=torch.long, device=device)
        self.Mmax = max(m for (l, m, t) in self.pmodes)
        A0p_src = eval_solid(model.grid.n, self.pmodes, Lf, 0, path="dd")[0]
        self.A0pw = A0p_src * model.grid.w[:, None]                           # analysis on the source grid
        A0p, A1p, _ = eval_solid(self.eval_model.grid.n, self.pmodes, Lf, 1, path="dd")   # synthesis on the evaluation grid (production: double-double)
        self.A0p, self.A1p = A0p, A1p
        # partner/sign arrays for the frame rotation (cos <-> sin pairs)
        partner, sign = [], []
        for q, (l, m, t) in enumerate(self.pmodes):
            if m == 0:
                partner.append(q); sign.append(0.0)
            elif t == 0:
                partner.append(q + 1); sign.append(1.0)
            else:
                partner.append(q - 1); sign.append(-1.0)
        self.partner = torch.tensor(partner, dtype=torch.long, device=device)
        self.sign = torch.tensor(sign, dtype=DT, device=device)
        ns = getattr(model, "Nr_src", model.Nr)
        self.Nr_src = ns
        r = model.r.cpu().numpy()[:ns]; x = model.x.cpu().numpy()[:ns]; Nr = len(r)   # source nodes (Chebyshev-Gauss in x)
        re_ = self.eval_model.r.cpu().numpy(); Ne = len(re_)                   # evaluation radii (may include extra far nodes)
        R0, p0 = self.R0, self.p0
        V = _cheb_vander(x, Nr); Vinv = np.linalg.inv(V)
        # ---------- quadrature points (shared by all l, m): composite Gauss in r on [0, r_0], in lambda = log s elsewhere.
        # Panel edges = source nodes UNION evaluation radii (astra review2: the Green kernel jumps at each evaluation
        # radius, so a panel must never straddle one); the exterior (beyond the last source node) is also split at the
        # evaluation radii that lie there.
        xg, wg = np.polynomial.legendre.leggauss(nq)
        kap = self.geometry_kappa_max * max(self.Mmax, 1)
        panel = math.pi / max(kap, 1e-12)                      # max phase change per panel: pi (at the geometry's maximal kappa)
        panel = min(panel, 0.5)
        S_pts, S_w = [], []                                      # radius points and weights for "ds"
        interior_edges = np.unique(np.concatenate([r, re_[(re_ > 0) & (re_ <= r[-1])]]))
        a, b = 0.0, interior_edges[0]
        npan = 2
        for i in range(npan):
            lo, hi = a + (b - a) * i / npan, a + (b - a) * (i + 1) / npan
            S_pts.append(0.5 * (hi - lo) * xg + 0.5 * (hi + lo)); S_w.append(0.5 * (hi - lo) * wg)
        for j in range(1, len(interior_edges)):
            la, lb = math.log(interior_edges[j - 1]), math.log(interior_edges[j])
            if lb - la < 1e-14:
                continue
            npan = max(1, int(math.ceil((lb - la) / panel)))
            for i in range(npan):
                lo, hi = la + (lb - la) * i / npan, la + (lb - la) * (i + 1) / npan
                lam = 0.5 * (hi - lo) * xg + 0.5 * (hi + lo); w = 0.5 * (hi - lo) * wg
                S_pts.append(np.exp(lam)); S_w.append(w * np.exp(lam))           # ds = s dlambda
        # exterior: lambda from log r_last on, until e^{-(p0-2) dlambda} < 1e-18 (slowest decay, l = 0 term2); split at far eval radii.
        # D6FP: the length is sized for the decay rate alpha_margin * (p0 - 2) so that trial parameters with a smaller alpha stay covered.
        la = math.log(r[-1]); L_ext = 41.5 / max(self.geometry_p0m2_min, 0.3) * float(ext_factor)
        ext_edges = np.unique(np.concatenate([[la], np.log(re_[re_ > r[-1]]), [la + L_ext]]))
        ext_edges = ext_edges[ext_edges <= la + L_ext + 1e-12]
        for j in range(1, len(ext_edges)):
            l0, l1 = ext_edges[j - 1], ext_edges[j]
            npan = max(1, int(math.ceil((l1 - l0) / panel)))
            for i in range(npan):
                lo, hi = l0 + (l1 - l0) * i / npan, l0 + (l1 - l0) * (i + 1) / npan
                lam = 0.5 * (hi - lo) * xg + 0.5 * (hi + lo); w = 0.5 * (hi - lo) * wg
                S_pts.append(np.exp(lam)); S_w.append(w * np.exp(lam))
        sg = np.concatenate(S_pts); wsg = np.concatenate(S_w)
        if len(sg) > max_points:          # D6FP: limit raised from 400000 (CPU kernel build of the frozen code) to 2e6; the GPU table build processes the points in chunks
            raise RuntimeError(f"pressure quadrature needs {len(sg)} points (> {max_points}); reduce Mmax*omega/c_l or raise max_points")
        self.n_quad = len(sg)
        ss = np.sqrt(sg ** 2 + R0 ** 2)
        xq = x_from_r(sg, R0)
        Phi = _cheb_vander(np.clip(xq, 0, 1), Nr) @ Vinv            # (Nq_pts, Nr): interpolant values f(nodes) -> f(quad pts)
        logs, logss = np.log(sg), np.log(ss / R0)       # logss is log(s/R0): the source carries (s/R0)^p0
        below = sg[None, :] <= re_[:, None]                                          # (Ne, Nq_pts)
        # D6FP (verifier audit 22:53Z): the far-anchor rows are the appended anchor nodes of the TRAINING grid (indices >= Nr_src of the model, merged
        # far radii 4096, 16384, 65536 R0), by explicit membership; never "beyond the last source node" (4096 R0 lies inside the source range at Nr 48).
        # Holdout/evaluation models have no anchor rows (the option is for the training residual rows only).
        anchors = np.zeros(Ne, dtype=bool)
        if self.eval_model is model and getattr(model, "extra_r", None):
            anchors[model.Nr_src:] = True
        self.anchor_rows = torch.tensor(anchors, device=device)
        self.anchor_radii = [float(v) for v in re_[anchors]]
        self._quad = dict(s=sg, w=wsg, Phi=Phi, logss=logss, r_last=float(r[-1]))     # exposed for the source-moment diagnostics (export_candidate.py)
        t = lambda arr: torch.tensor(np.asarray(arr), dtype=DT, device=device)
        self.q = dict(logs=t(logs), logss=t(logss), logssabs=t(np.log(ss)), w=t(wsg), Phi=t(Phi), below=torch.tensor(below, device=device),
                      log_re=t(np.log(re_)), log1p_q=t(np.log1p(sg ** 2 / R0 ** 2)), s2=t(sg ** 2))   # log1p: no cancellation near the origin
        self.Ne, self.Nr_tab = Ne, Nr
        self.le_l = t([float(_leff(l)) for l in range(Lf + 1)])                  # (Lf+1,)
        self.l_vals = t(np.arange(Lf + 1, dtype=float))
        self.point_chunk = int(point_chunk) if point_chunk else max(2000, int(6e7 // max((Lf + 1) * Ne, 1)))
        rs = model.r[:ns]
        self.log_s_nodes = torch.log((rs ** 2 + model.R0 ** 2).sqrt() / model.R0)    # (Nr_src,)
        self.log1p_nodes = torch.log1p(rs ** 2 / model.R0 ** 2)
        pleff = torch.tensor([float(_leff(l)) for l in self.pl_idx], dtype=DT, device=device)
        self.lfac = ((rs ** 2 + model.R0 ** 2).sqrt() / rs)[:, None] ** pleff[None, :]   # (Nr_src, Nqp), parameter independent
        self.unit_grad_origin = eval_solid(torch.zeros(1, 3, dtype=DT, device=device), self.pmodes, Lf, 1, path="dd")[1][:, 0, :]   # (3, Nqp) gradients of P_q at the origin
        # base tables at the constructor's parameters (p0 as given: the manufactured-source tests use p0 != 2 alpha + 2)
        self.tables = self.build_tables(torch.tensor(self.c_l, dtype=DT, device=device), torch.tensor(self.omega, dtype=DT, device=device), p0=torch.tensor(self.p0, dtype=DT, device=device))
        self._expose(self.tables)

    # ----- D6FP: differentiable parameter-dependent tables -----
    def build_tables(self, c_l, omega, p0=None):
        """All parameter-dependent tables as torch tensors on the fixed quadrature geometry, differentiable in the 0-dim tensors
        c_l and omega (and p0 when given; default p0 = 2 alpha + 2 with alpha = (1 - c_l)/c_l). Returns a dict."""
        dev = self.device
        c_l = torch.as_tensor(c_l, dtype=DT, device=dev); omega = torch.as_tensor(omega, dtype=DT, device=dev)
        alpha = (1.0 - c_l) / c_l
        p0 = (2.0 * alpha + 2.0) if p0 is None else torch.as_tensor(p0, dtype=DT, device=dev)
        q = self.q; Lfp = self.Lf + 1; M = self.Mmax; Ne, Nr = self.Ne, self.Nr_tab
        Nq = q["w"].numel()
        beta_q = (omega / (2.0 * c_l)) * q["log1p_q"]                              # beta(s) at the quadrature points
        mvals = torch.arange(M + 1, dtype=DT, device=dev)
        cm = torch.cos(mvals[:, None] * beta_q[None, :]); sm = torch.sin(mvals[:, None] * beta_q[None, :])   # (M+1, Nq)
        base_l = -p0 * q["logss"][None, :] + self.le_l[:, None] * (q["logs"] - q["logssabs"])[None, :]       # (Lfp, Nq): (s/R0)^-p0 (r/s)^le in log space
        lv = self.l_vals
        acc = [0.0, 0.0, 0.0, 0.0]            # Qc term1, Qc term2, Qs term1, Qs term2, each (M+1, Lfp*Ne, Nr)
        for a0 in range(0, Nq, self.point_chunk):
            sl = slice(a0, min(Nq, a0 + self.point_chunk))
            logs_c = q["logs"][sl]; w_c = q["w"][sl]; below_c = q["below"][:, sl]; base_c = base_l[:, sl]
            # kernel1(j, s) = (s/r_j)^(l+2) r_j (s/R0)^-p0 (s/ss)^le ; kernel2(j, s) = (r_j/s)^l s (s/R0)^-p0 (s/ss)^le   [log space]
            logk1 = (lv[:, None, None] + 2.0) * (logs_c[None, None, :] - q["log_re"][None, :, None]) + q["log_re"][None, :, None] + base_c[:, None, :]
            logk2 = lv[:, None, None] * (q["log_re"][None, :, None] - logs_c[None, None, :]) + logs_c[None, None, :] + base_c[:, None, :]
            neg = torch.full((), -1.0e4, dtype=DT, device=dev)
            k1 = torch.exp(torch.where(below_c[None], torch.clamp(logk1, max=700.0), neg)) * w_c          # masked in log space: exact zeros, zero tangents
            k2 = torch.exp(torch.where(~below_c[None], torch.clamp(logk2, max=700.0), neg)) * w_c
            if self.exterior_monopole and bool(self.anchor_rows.any()):
                # l = 0 term1 at the anchor rows: -(s/r)^2 r (s/R0)^-p0 integrated over s > r (exterior) instead of the interior integral
                k1_ext0 = -torch.exp(torch.where(~below_c, torch.clamp(logk1[0], max=700.0), neg)) * w_c       # (Ne, nc)
                k1 = torch.cat([torch.where(self.anchor_rows[:, None], k1_ext0, k1[0])[None], k1[1:]], 0)
            K1 = k1.reshape(Lfp * Ne, -1); K2 = k2.reshape(Lfp * Ne, -1)
            nc = K1.shape[1]
            # (nc, (M+1) Nr) tables of cos(m beta) Phi and sin(m beta) Phi: one 2-D matmul per kernel (no broadcast copies)
            Pc = (cm[:, sl, None] * q["Phi"][None, sl, :]).permute(1, 0, 2).reshape(nc, (M + 1) * Nr)
            Ps = (sm[:, sl, None] * q["Phi"][None, sl, :]).permute(1, 0, 2).reshape(nc, (M + 1) * Nr)
            acc[0] = acc[0] + K1 @ Pc; acc[1] = acc[1] + K2 @ Pc
            acc[2] = acc[2] + K1 @ Ps; acc[3] = acc[3] + K2 @ Ps
        inv = 1.0 / (2.0 * lv + 1.0)
        def finish(t1, t2):
            # t: (Lfp*Ne, (M+1)*Nr) -> [l, m, term, j, k]
            T = torch.stack([t1.reshape(Lfp, Ne, M + 1, Nr), t2.reshape(Lfp, Ne, M + 1, Nr)], 0).permute(1, 3, 0, 2, 4)
            return T * inv[:, None, None, None, None]
        Qc = finish(acc[0], acc[1]); Qs = finish(acc[2], acc[3])
        # volume weights int_0^inf F r^2 dr for F = (s/R0)^-p0 Ftilde (l = 0, no oscillation)
        wr = (q["s2"] * torch.exp(-p0 * q["logss"]) * q["w"]) @ q["Phi"]
        # l = 1 moments int_0^inf f_1m ds (for grad P at the origin): kernel s^0 (s/R0)^-p0 (s/ss)^1, with twist factors
        base1 = torch.exp(-p0 * q["logss"] + (q["logs"] - q["logssabs"])) * q["w"]
        mom1_0 = base1 @ q["Phi"]; mom1_c = (base1 * torch.cos(beta_q)) @ q["Phi"]; mom1_s = (base1 * torch.sin(beta_q)) @ q["Phi"]
        sfac = torch.exp(p0 * self.log_s_nodes)                                       # (s/R0)^p0 at the source nodes
        beta_nodes = (omega / (2.0 * c_l)) * self.log1p_nodes
        cosb = torch.cos(self.pm[None, :].to(DT) * beta_nodes[:, None]); sinb = torch.sin(self.pm[None, :].to(DT) * beta_nodes[:, None])
        return dict(Qc=Qc, Qs=Qs, wr=wr, mom1_0=mom1_0, mom1_c=mom1_c, mom1_s=mom1_s, sfac=sfac, beta_nodes=beta_nodes, cosb=cosb, sinb=sinb,
                    c_l=c_l, omega=omega, p0=p0)

    def _expose(self, T):
        """Mirror the base tables as attributes (frozen-code names used by the export and moment scripts)."""
        for k in ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "beta_nodes", "cosb", "sinb"):
            setattr(self, k, T[k])

    def set_parameters(self, c_l, omega, p0=None):
        """Rebuild the base tables at new parameters on the SAME quadrature geometry (fast, GPU). Returns True when the new
        parameters lie outside the geometry's (immutable) margins; the caller should then construct a new solver."""
        c_lf, omf = float(c_l), float(omega)
        p0_new = 2.0 * (1.0 - c_lf) / c_lf + 2.0 if p0 is None else float(p0)
        with torch.no_grad():
            self.tables = self.build_tables(torch.tensor(c_lf, dtype=DT, device=self.device), torch.tensor(omf, dtype=DT, device=self.device),
                                            p0=None if p0 is None else torch.tensor(float(p0), dtype=DT, device=self.device))
        self._expose(self.tables)
        self.c_l, self.omega, self.kappa, self.p0 = c_lf, omf, omf / c_lf, p0_new
        return not self.geometry_ok(c_lf, omf, p0=p0_new)

    def geometry_ok(self, c_l, omega, p0=None):
        """True when (c_l, omega) lie inside the immutable margins of this solver's quadrature geometry:
        |omega/c_l| <= 0.98 geometry_kappa_max and p0 - 2 >= 1.02 geometry_p0m2_min."""
        c_lf, omf = float(c_l), float(omega)
        p0n = 2.0 * (1.0 - c_lf) / c_lf + 2.0 if p0 is None else float(p0)
        return (abs(omf / c_lf) <= 0.98 * self.geometry_kappa_max + 1e-12) and ((p0n - 2.0) >= 1.02 * self.geometry_p0m2_min - 1e-12)

    # ----- evaluation -----
    def analyze(self, f):
        """SH analysis of a grid function f (Nr, Na) in the true azimuth -> coefficients (Nr_src, Nqp) on the source nodes."""
        return f[: self.Nr_src] @ self.A0pw

    def to_twisted_frame(self, flm, tables=None):
        """ftw^c = f^c cos(m beta) - f^s sin(m beta);  ftw^s = f^c sin(m beta) + f^s cos(m beta)  (per node)."""
        T = self.tables if tables is None else tables
        fp = flm[:, self.partner]
        # for a cos mode q (sign +1): ftw = f_q cos - f_partner sin ; for a sin mode (sign -1): ftw = f_q cos + f_partner sin
        return flm * T["cosb"] - self.sign[None, :] * fp * T["sinb"]

    chain_precision = "fp64"                                                     # D6FP D1: "fp64" (production) or "dd" (double-double chain, solve_dd)

    def solve(self, f, tables=None):
        """f (Nr,Na) source of -Lap P = f. Returns P (Nr,Na), gradP (3,Nr,Na), P_lm (Nr,Nqp) and dP_lm/dr (true azimuth).
        tables: parameter tables from build_tables (default: the base tables). chain_precision "dd" routes to solve_dd (D6FP D1 v1)."""
        if self.chain_precision == "dd":
            return self.solve_dd(f, tables)
        return self._solve_fp64(f, tables)

    def _solve_fp64(self, f, tables=None):
        T = self.tables if tables is None else tables
        flm = self.analyze(f)
        ftw = self.to_twisted_frame(flm, T) * T["sfac"][:, None] * self.lfac          # smooth factored twisted-frame source (Nr, Nqp)
        ftw_p = ftw[:, self.partner]
        Qc = T["Qc"][self.pl_long, self.pm]                                         # (Nqp, 2, Ne, Nr)
        Qs = T["Qs"][self.pl_long, self.pm]
        # f^c(s) = ftw^c cos + ftw^s sin -> G[f^c] = Qc ftw^c + Qs ftw^s ;  f^s(s) = -ftw^c sin + ftw^s cos -> G[f^s] = -Qs ftw^c + Qc ftw^s
        # for mode q: own = ftw_q, partner = ftw_p; cos modes: Qc own + Qs partner; sin modes: Qc own - Qs partner  (m = 0: Qs = 0)
        t1 = torch.einsum('qjk,kq->jq', Qc[:, 0], ftw) + self.sign[None, :] * torch.einsum('qjk,kq->jq', Qs[:, 0], ftw_p)
        t2 = torch.einsum('qjk,kq->jq', Qc[:, 1], ftw) + self.sign[None, :] * torch.einsum('qjk,kq->jq', Qs[:, 1], ftw_p)
        Plm = t1 + t2
        r = self.eval_model.r[:, None]
        dPlm = (-(self.pl[None, :] + 1) * t1 + self.pl[None, :] * t2) / r
        P = Plm @ self.A0p.T
        n = self.eval_model.grid.n.T
        radial = ((dPlm - self.pl[None, :] * Plm / r) @ self.A0p.T)
        gradP = radial[None] * n[:, None, :] + torch.einsum('jq,iaq->ija', Plm / r, self.A1p)
        return P, gradP, Plm, dPlm

    def solve_dd(self, f, tables=None):
        """D6FP D1 variant v1: double-double pressure chain (see _solve_dd_core) wrapped in an autograd Function whose forward-mode rule pushes the
        tangents through the SAME double-double chain (the chain is linear in f and multilinear in the table groups (Qc, Qs), sfac, (cosb, sinb)),
        so that Jacobian columns are as accurate as the values; the reverse-mode rule uses the float64 chain (gradients are validated at 1e-6)."""
        T = self.tables if tables is None else tables
        if isinstance(f, (tuple, list)):
            fh, fl = f                                                                   # unrounded double-double source (D1 v2, fields_dd.source_dd)
        else:
            fh, fl = f, torch.zeros_like(f)
        return _SolveDD.apply(fh, fl, T["Qc"], T["Qs"], T["sfac"], T["cosb"], T["sinb"], self)

    def _solve_dd_core(self, fh, fl, Qc_full, Qs_full, sfac, cosb, sinb):
        """D6FP D1 variant v1 (lead 23:08Z item 2): the pressure chain of solve() in double-double arithmetic: angular analysis, twisted-frame
        rotation, factored scaling, radial Green sums and the synthesis of P and grad P are evaluated with error-free matrix products (Ozaki
        splitting, src/pressure/exact_matmul.py) and two_sum/two_prod elementwise operations, and rounded ONCE at the outputs. The float64 inputs
        are the source values f at the grid points, the parameter tables (Qc, Qs, sfac, cosb, sinb; built as in production) and the geometry
        matrices (A0pw, A0p, A1p, lfac). Same outputs and shapes as solve(). Cost: about 25 float64 products per product of the chain."""
        from .exact_matmul import matmul_dd, matmul_dd_x, matmul_x_dd, dd_mul_f, dd_add, dd_div_f
        fh, fl = matmul_dd_x(fh[: self.Nr_src], fl[: self.Nr_src], self.A0pw)                     # analysis (Nr_src, Nqp)
        ah, al = dd_mul_f(fh, fl, cosb)                                                           # twisted frame
        bh, bl = dd_mul_f(fh[:, self.partner], fl[:, self.partner], -self.sign[None, :] * sinb)
        th, tl = dd_add(ah, al, bh, bl)
        th, tl = dd_mul_f(th, tl, sfac[:, None]); th, tl = dd_mul_f(th, tl, self.lfac)              # factored smooth source
        ph, pl_ = th[:, self.partner], tl[:, self.partner]
        Qc = Qc_full[self.pl_long, self.pm]; Qs = Qs_full[self.pl_long, self.pm]                   # (Nqp, 2, Ne, Nr)
        def green(Qx, h, l):                                                                      # sum_k Qx[q, j, k] v[k, q] -> (Ne, Nqp)
            H, L = matmul_x_dd(Qx, h.T[:, :, None], l.T[:, :, None])
            return H[:, :, 0].T, L[:, :, 0].T
        def term(idx):
            h1, l1 = green(Qc[:, idx], th, tl); h2, l2 = green(Qs[:, idx], ph, pl_)
            h2, l2 = dd_mul_f(h2, l2, self.sign[None, :])
            return dd_add(h1, l1, h2, l2)
        t1h, t1l = term(0); t2h, t2l = term(1)
        Ph_lm, Pl_lm = dd_add(t1h, t1l, t2h, t2l)                                                 # Plm (Ne, Nqp)
        r = self.eval_model.r[:, None]; pl = self.pl[None, :]
        ah, al = dd_mul_f(t1h, t1l, -(pl + 1)); bh, bl = dd_mul_f(t2h, t2l, pl)
        dh, dl = dd_add(ah, al, bh, bl); dh, dl = dd_div_f(dh, dl, r)                                 # dPlm
        Ph, Pl = matmul_dd_x(Ph_lm, Pl_lm, self.A0p.T)                                            # P (Ne, Na)
        ch, cl = dd_div_f(Ph_lm, Pl_lm, r)                                                        # Plm / r
        eh, el = dd_mul_f(ch, cl, -pl); eh, el = dd_add(dh, dl, eh, el)                             # dPlm - l Plm / r
        rh, rl = matmul_dd_x(eh, el, self.A0p.T)                                                  # radial derivative (Ne, Na)
        n = self.eval_model.grid.n.T
        comps = []
        for i in range(3):
            gh, gl = matmul_dd_x(ch, cl, self.A1p[i].T)                                           # (Ne, Na)
            sh, sl = dd_mul_f(rh, rl, n[i][None, :])
            gh, gl = dd_add(gh, gl, sh, sl)
            comps.append(gh + gl)
        gradP = torch.stack(comps, 0)
        return Ph + Pl, gradP, Ph_lm + Pl_lm, dh + dl

    def gradP_origin(self, f, tables=None):
        """grad P(0) = sum over l = 1 modes of (1/3) int_0^inf f_1m(s) ds * grad P_q (constant unit gradients of r Y_1m)."""
        T = self.tables if tables is None else tables
        flm = self.analyze(f)
        ftw = self.to_twisted_frame(flm, T) * T["sfac"][:, None] * self.lfac
        out = torch.zeros(3, dtype=DT, device=f.device)
        unit = self.unit_grad_origin
        for q, (l, m, t) in enumerate(self.pmodes):
            if l != 1:
                continue
            if m == 0:
                M = T["mom1_0"] @ ftw[:, q]
            else:
                M = T["mom1_c"] @ ftw[:, q] + self.sign[q] * (T["mom1_s"] @ ftw[:, self.partner[q]])
            out = out + (M / 3.0) * unit[:, q]
        return out

    def discrete_moments(self, f, tables=None, lmax=1):
        """D6FP: the discrete l <= lmax moments of the source as the production quadrature sees them: M_lm = int_0^inf s^(l+2) f_lm(s) ds on the
        quadrature points (factored interpolant), with the absolute sum of the integrand as scale. Returns dict mode -> (M, abs_sum, ratio)."""
        T = self.tables if tables is None else tables
        flm = self.analyze(f); ftw = self.to_twisted_frame(flm, T) * T["sfac"][:, None] * self.lfac
        Phi = self.q["Phi"]; sg = self.q["s2"].sqrt(); w = self.q["w"]; logss = self.q["logss"]; logs = self.q["logs"]; logssabs = self.q["logssabs"]
        fq = Phi @ ftw                                                                 # factored TWISTED-frame values at the quadrature points
        beta_q = (T["omega"] / (2.0 * T["c_l"])) * self.q["log1p_q"]
        out = {}
        for i, (l, m, t) in enumerate(self.pmodes):
            if l > lmax:
                continue
            le = float(self.le_l[l]); fac = torch.exp(-T["p0"] * logss + le * (logs - logssabs))
            if m == 0:
                fv = fq[:, i]
            else:                                                                        # rotate back to the true azimuth (verifier audit 22:53Z): f^c = ftw^c cos(m beta) + ftw^s sin(m beta), f^s = -ftw^c sin + ftw^s cos
                j = int(self.partner[i]); cm, sm = torch.cos(m * beta_q), torch.sin(m * beta_q)
                fv = (fq[:, i] * cm + fq[:, j] * sm) if t == 0 else (-fq[:, j] * sm + fq[:, i] * cm)
            integrand = fv * fac * sg ** (l + 2) * w
            M = float(integrand.sum()); A = float(integrand.abs().sum())
            out[f"({l},{m},{t})"] = dict(M=M, abs_sum=A, ratio=M / max(A, 1e-300))
        return out

    def volume_integral(self, g, tables=None):
        """int_R^3 g dy for a grid function g (Nr, Na), using the factored radial weights (source nodes)."""
        T = self.tables if tables is None else tables
        return torch.einsum('j,ja,a->', T["wr"], g[: self.Nr_src] * T["sfac"][:, None], self.model.grid.w)
