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
Cartesian gradient: grad P = sum_q [ (dP_q/dr - l P_q/r) n P_q(n) + (P_q/r) grad P_q(n) ]  (regular solid harmonics)."""
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


class PressureSolver:
    def __init__(self, model, p0, nq=32, m_parity=None, Lf=None, device=None, omega=None, c_l=None, max_points=400000,
                 eval_model=None, ext_factor=1.0):
        """eval_model: optional Model whose radii/angular grid receive P and grad P (holdout evaluation); the source is
        always sampled on `model` (training nodes, Chebyshev-Gauss in x) and interpolated."""
        self.model = model
        self.eval_model = eval_model if eval_model is not None else model
        self.p0 = float(p0)
        self.R0 = model.R0
        device = device or model.r.device
        Lf = Lf if Lf is not None else model.Lf
        par = m_parity if m_parity is not None else model.m_parity
        self.Lf = Lf
        self.omega = float(model.omega0 if omega is None else omega)
        self.c_l = float(model.c_l0 if c_l is None else c_l)
        self.kappa = self.omega / self.c_l                      # omega/c_l
        self.pmodes = mode_list(Lf, par, l_min=0)
        self.pl = torch.tensor([float(l) for (l, m, t) in self.pmodes], dtype=DT, device=device)
        self.pm = torch.tensor([m for (l, m, t) in self.pmodes], dtype=torch.long, device=device)
        self.pl_idx = [l for (l, m, t) in self.pmodes]
        self.pl_long = torch.tensor(self.pl_idx, dtype=torch.long, device=device)
        self.Mmax = max(m for (l, m, t) in self.pmodes)
        A0p_src = eval_solid(model.grid.n, self.pmodes, Lf, 0)[0]
        self.A0pw = A0p_src * model.grid.w[:, None]                           # analysis on the source grid
        A0p, A1p, _ = eval_solid(self.eval_model.grid.n, self.pmodes, Lf, 1)   # synthesis on the evaluation grid
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
        self.beta_nodes = torch.tensor(self.omega / (2 * self.c_l) * np.log(1 + r ** 2 / R0 ** 2), dtype=DT, device=device)
        # ---------- quadrature points (shared by all l, m): composite Gauss in r on [0, r_0], in lambda = log s elsewhere.
        # Panel edges = source nodes UNION evaluation radii (astra review2: the Green kernel jumps at each evaluation
        # radius, so a panel must never straddle one); the exterior (beyond the last source node) is also split at the
        # evaluation radii that lie there.
        xg, wg = np.polynomial.legendre.leggauss(nq)
        kap = abs(self.kappa) * max(self.Mmax, 1)
        panel = math.pi / max(kap, 1e-12)                      # max phase change per panel: pi
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
        # exterior: lambda from log r_last on, until e^{-(p0-2) dlambda} < 1e-18 (slowest decay, l = 0 term2); split at far eval radii
        la = math.log(r[-1]); L_ext = 41.5 / max(p0 - 2.0, 0.3) * float(ext_factor)     # ext_factor > 1 only for the source-moment diagnostics (2026-10-25T19:10Z); default unchanged
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
        if len(sg) > max_points:
            raise RuntimeError(f"pressure quadrature needs {len(sg)} points (> {max_points}); reduce Mmax*omega/c_l or raise max_points")
        self.n_quad = len(sg)
        ss = np.sqrt(sg ** 2 + R0 ** 2)
        xq = x_from_r(sg, R0)
        le_fix = None
        Phi = _cheb_vander(np.clip(xq, 0, 1), Nr) @ Vinv            # (Nq_pts, Nr): interpolant values f(nodes) -> f(quad pts)
        beta_q = self.omega / (2 * self.c_l) * np.log(1 + sg ** 2 / R0 ** 2)
        logs, logss = np.log(sg), np.log(ss / R0)       # logss is log(s/R0): the source carries (s/R0)^p0
        # kernel tables per l: term1 at node j needs sum over s <= r_j, term2 over s > r_j
        Lfp = Lf + 1
        Qc = np.zeros((Lfp, self.Mmax + 1, 2, Ne, Nr)); Qs = np.zeros_like(Qc)   # [l, m, term, j(eval), k(source node)]
        below = sg[None, :] <= re_[:, None]                                          # (Ne, Nq_pts)
        for l in range(Lfp):
            le = _leff(l)
            # kernel1(j, s) = (s/r_j)^(l+2) r_j (s/R0)^-p0 (s/ss)^le ; kernel2(j, s) = (r_j/s)^l s (s/R0)^-p0 (s/ss)^le   [log space]
            base = -p0 * logss + le * (logs - np.log(ss))                              # (Nq_pts,): (s/R0)^-p0 (r/s)^le
            logk1 = (l + 2) * (logs[None, :] - np.log(re_)[:, None]) + np.log(re_)[:, None] + base[None, :]
            logk2 = l * (np.log(re_)[:, None] - logs[None, :]) + logs[None, :] + base[None, :]
            k1 = np.where(below, np.exp(np.minimum(logk1, 700)), 0.0) * wsg[None, :]
            k2 = np.where(~below, np.exp(np.minimum(logk2, 700)), 0.0) * wsg[None, :]
            for m in range(self.Mmax + 1):
                cm, sm = np.cos(m * beta_q), np.sin(m * beta_q)
                Qc[l, m, 0] = (k1 * cm[None, :]) @ Phi / (2 * l + 1); Qs[l, m, 0] = (k1 * sm[None, :]) @ Phi / (2 * l + 1)
                Qc[l, m, 1] = (k2 * cm[None, :]) @ Phi / (2 * l + 1); Qs[l, m, 1] = (k2 * sm[None, :]) @ Phi / (2 * l + 1)
        self.Qc = torch.tensor(Qc, dtype=DT, device=device); self.Qs = torch.tensor(Qs, dtype=DT, device=device)
        # volume weights int_0^inf F r^2 dr for F = (s/R0)^-p0 Ftilde (l = 0, no oscillation)
        wr = (sg ** 2 * np.exp(-p0 * logss) * wsg) @ Phi                             # (s/R0)^-p0
        self._quad = dict(s=sg, w=wsg, Phi=Phi, logss=logss, r_last=float(r[-1]))     # 2026-10-25T18:40Z: exposed for the source-moment diagnostics (no change of any computation)
        self.wr = torch.tensor(wr, dtype=DT, device=device)
        # l = 1 moments int_0^inf f_1m ds (for grad P at the origin): kernel s^0 (s/R0)^-p0 (s/ss)^1, with twist factors
        base1 = np.exp(-p0 * logss + (logs - np.log(ss))) * wsg                       # (s/R0)^-p0 (r/s)
        self.mom1_0 = torch.tensor(base1 @ Phi, dtype=DT, device=device)                      # m = 0: no twist factor
        self.mom1_c = torch.tensor((base1 * np.cos(beta_q)) @ Phi, dtype=DT, device=device)   # m = 1 (odd-m runs)
        self.mom1_s = torch.tensor((base1 * np.sin(beta_q)) @ Phi, dtype=DT, device=device)
        rs = model.r[:ns]
        self.sfac = ((rs ** 2 + model.R0 ** 2).sqrt() / model.R0) ** self.p0   # (Nr_src,)
        pleff = torch.tensor([float(_leff(l)) for l in self.pl_idx], dtype=DT, device=device)
        self.lfac = ((rs ** 2 + model.R0 ** 2).sqrt() / rs)[:, None] ** pleff[None, :]   # (Nr_src, Nqp)
        self.cosb = torch.cos(self.pm[None, :].to(DT) * self.beta_nodes[:, None])    # (Nr_src, Nqp)
        self.sinb = torch.sin(self.pm[None, :].to(DT) * self.beta_nodes[:, None])

    def analyze(self, f):
        """SH analysis of a grid function f (Nr, Na) in the true azimuth -> coefficients (Nr_src, Nqp) on the source nodes."""
        return f[: self.Nr_src] @ self.A0pw

    def to_twisted_frame(self, flm):
        """ftw^c = f^c cos(m beta) - f^s sin(m beta);  ftw^s = f^c sin(m beta) + f^s cos(m beta)  (per node)."""
        fp = flm[:, self.partner]
        # for a cos mode q (sign +1): ftw = f_q cos - f_partner sin ; for a sin mode (sign -1): ftw = f_q cos + f_partner sin
        return flm * self.cosb - self.sign[None, :] * fp * self.sinb

    def solve(self, f):
        """f (Nr,Na) source of -Lap P = f. Returns P (Nr,Na), gradP (3,Nr,Na), P_lm (Nr,Nqp) and dP_lm/dr (true azimuth)."""
        flm = self.analyze(f)
        ftw = self.to_twisted_frame(flm) * self.sfac[:, None] * self.lfac          # smooth factored twisted-frame source (Nr, Nqp)
        ftw_p = ftw[:, self.partner]
        Qc = self.Qc[self.pl_long, self.pm]                                         # (Nqp, 2, Nr, Nr)
        Qs = self.Qs[self.pl_long, self.pm]
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

    def gradP_origin(self, f):
        """grad P(0) = sum over l = 1 modes of (1/3) int_0^inf f_1m(s) ds * grad P_q (constant unit gradients of r Y_1m)."""
        flm = self.analyze(f)
        ftw = self.to_twisted_frame(flm) * self.sfac[:, None] * self.lfac
        out = torch.zeros(3, dtype=DT, device=f.device)
        unit = eval_solid(torch.zeros(1, 3, dtype=DT, device=f.device), self.pmodes, self.Lf, 1)[1][:, 0, :]     # (3, Nqp) gradients at origin
        for q, (l, m, t) in enumerate(self.pmodes):
            if l != 1:
                continue
            if m == 0:
                M = self.mom1_0 @ ftw[:, q]
            else:
                M = self.mom1_c @ ftw[:, q] + self.sign[q] * (self.mom1_s @ ftw[:, self.partner[q]])
            out = out + (M / 3.0) * unit[:, q]
        return out

    def volume_integral(self, g):
        """int_R^3 g dy for a grid function g (Nr, Na), using the factored radial weights (source nodes)."""
        return torch.einsum('j,ja,a->', self.wr, g[: self.Nr_src] * self.sfac[:, None], self.model.grid.w)
