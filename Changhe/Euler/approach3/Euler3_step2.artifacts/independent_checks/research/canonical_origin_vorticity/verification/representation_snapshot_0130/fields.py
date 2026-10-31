"""Divergence-free representation U = curl(T y) + curl curl(S y) and its derivatives in Cartesian components.

Scalars built from the potentials (all of the form sum_q h_q(rho) P_q(y) with P_q real solid harmonics):
  K   = d_r(r S) = S + y.grad S     radial function  k = (l+1) g + 2 rho g'
  D   = Laplacian S                 radial function  d = (6+4l) g' + 4 rho g''
  K_T, D_T likewise from T.
Then (Einstein summation, GU[m,i] = d_m U_i):
  U_i   = -eps_ijk y_j d_k T + d_i K - y_i D
  Om_i  =  d_i K_T - y_i D_T + eps_ijk y_j d_k D
  d_m U_i  = -eps_ijk (delta_jm d_k T + y_j d_m d_k T) + d_m d_i K - delta_im D - y_i d_m D
  d_m Om_i =  d_m d_i K_T - delta_im D_T - y_i d_m D_T + eps_ijk (delta_jm d_k D + y_j d_m d_k D)
Everything is float64 and differentiable in the coefficients, c_l and omega."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..bases.solid_harmonics import mode_list, eval_solid, AngularGrid, angular_matrices
from ..bases.radial import RadialBasis, cheb_gauss_nodes_x, r_from_x

DT = torch.float64
EPS = torch.zeros(3, 3, 3, dtype=DT)
for (i, j, k, s) in [(0, 1, 2, 1), (1, 2, 0, 1), (2, 0, 1, 1), (0, 2, 1, -1), (2, 1, 0, -1), (1, 0, 2, -1)]:
    EPS[i, j, k] = s


def alpha_of(c_l):
    return (1.0 - c_l) / c_l


class Model:
    """Spectral representation on a product grid (radial Chebyshev-Gauss nodes in x) x (Gauss-Legendre x uniform)."""

    def __init__(self, L, Nk, m_parity="even", R0=1.0, Nr=None, ntheta=None, nphi=None, Lf=None,
                 device="cpu", c_l=0.45, omega=1.0, free_params=False, channels=None, r_nodes=None, phi0=0.0, extra_r=None):
        """channels: dict(NkB=0, NkD=0, NkE=0, core_damp=2, R1=None, LB=None, LD=None, LE=None, Mch=None). Extra radial channels of SPEC 4.4:
        T: + r^l (s/R0)^-(2alpha+1+l) damp B(x) (twisted); S: + r^l (s/R0)^-(2alpha+l) damp D(x) (twisted)
                                                       + r^l (s/R0)^-(2l+1) damp E(x) (untwisted, l >= 2).
        Channel angular degrees (SPEC 4.4 angular closure, lead 2026-10-24T22:40Z (a)): LB, LD, LE are the maximum l of the B, D, E
        channels (default L: every channel shares the leading mode set, the behaviour before 2026-10-24T23:30Z); Mch is the maximum m
        of the B/D/E modes with l > L (default 2 M_max of the leading set). The leading channels A, C keep degree L. Internally the
        mode list is the union; each channel owns the columns chan_cols[name], and unpack_all scatters its coefficients into the
        union (zeros elsewhere), so every consumer sees (n, Nq) arrays over self.modes."""
        self.L, self.Nk, self.m_parity, self.device = L, Nk, m_parity, device
        ch = dict(NkB=0, NkD=0, NkE=0, core_damp=2, R1=None, LB=None, LD=None, LE=None, Mch=None)
        ch.update(channels or {})
        self.channels = ch
        self.R0 = float(R0)
        LB = ch["LB"] if (ch["LB"] is not None and ch["NkB"] > 0) else L
        LD = ch["LD"] if (ch["LD"] is not None and ch["NkD"] > 0) else L
        LE = ch["LE"] if (ch["LE"] is not None and ch["NkE"] > 0) else L
        self.L_ext = max(L, LB, LD, LE)
        lead_modes = mode_list(L, m_parity, l_min=1)
        Mlead = max([m for (l, m, t) in lead_modes] + [0])
        Mch = ch["Mch"] if ch["Mch"] is not None else 2 * Mlead
        self.chan_deg = dict(A=(L, Mlead), C=(L, Mlead), B=(LB, max(Mlead, Mch) if LB > L else Mlead), D=(LD, max(Mlead, Mch) if LD > L else Mlead),
                             E=(LE, max(Mlead, Mch) if LE > L else Mlead))
        def carried(name, l, m):
            Lc, Mc = self.chan_deg[name]
            return l <= Lc and (m <= Mc or l <= L)
        self.modes = [q for q in mode_list(self.L_ext, m_parity, l_min=1) if any(carried(nm, q[0], q[1]) for nm in ("A", "B", "D", "E"))]
        self.Nq = len(self.modes)
        self.chan_cols = {nm: torch.tensor([i for i, (l, m, t) in enumerate(self.modes) if carried(nm, l, m)], dtype=torch.long, device=device) for nm in ("A", "C", "B", "D", "E")}
        self.ncols = {nm: int(self.chan_cols[nm].numel()) for nm in self.chan_cols}
        self.l_arr = torch.tensor([float(l) for (l, m, t) in self.modes], dtype=DT, device=device)
        self.m_arr = torch.tensor([m for (l, m, t) in self.modes], dtype=torch.long, device=device)
        self.l_idx = torch.tensor([l for (l, m, t) in self.modes], dtype=torch.long, device=device)
        # twist pairs
        self.pair_c = torch.tensor([q for q, (l, m, t) in enumerate(self.modes) if m > 0 and t == 0], dtype=torch.long, device=device)
        self.pair_s = self.pair_c + 1
        self.pair_m = self.m_arr[self.pair_c]
        # gather-based twist: partner index and sign (+1 cos-mode, -1 sin-mode, 0 for m = 0)
        partner = []; sign = []
        for q, (l, m, t) in enumerate(self.modes):
            if m == 0:
                partner.append(q); sign.append(0.0)
            elif t == 0:
                partner.append(q + 1); sign.append(1.0)
            else:
                partner.append(q - 1); sign.append(-1.0)
        self.partner = torch.tensor(partner, dtype=torch.long, device=device)
        self.tw_sign = torch.tensor(sign, dtype=DT, device=device)
        self.Mmax = max([m for (l, m, t) in self.modes] + [0])
        # radial nodes
        from ..bases.radial import x_from_r
        if r_nodes is not None:                        # explicit radii (holdout / diagnostic grids)
            r = np.asarray(r_nodes, dtype=float); self.Nr = len(r)
            x = x_from_r(r, self.R0)
        else:
            self.Nr = Nr if Nr is not None else int(1.5 * Nk)
            x = cheb_gauss_nodes_x(self.Nr)
            r = r_from_x(x, self.R0)
        self.Nr_src = self.Nr                          # Chebyshev-Gauss source nodes (pressure interpolation uses these only)
        if extra_r:                                    # far anchoring nodes appended (residual rows only; SPEC far checkpoints)
            er = np.asarray([float(v) for v in extra_r]) * self.R0
            r = np.concatenate([r, er]); x = np.concatenate([x, x_from_r(er, self.R0)]); self.Nr = len(r)
        self.extra_r = list(extra_r) if extra_r else None
        self.x = torch.tensor(x, dtype=DT, device=device)
        self.r = torch.tensor(r, dtype=DT, device=device)
        self.rho = self.r ** 2
        self.rl = self.r[:, None] ** self.l_arr[None, :]      # (Nr, Nq)
        # angular grid: Cartesian components of U have angular degree <= L+2, grad U <= L+3, so the pressure source
        # tr((DU)^2) has degree <= 2L+6 = Lf; the grid integrates products of degree (2L+6)+(2L+6) exactly.
        # (with channel degrees above L the Cartesian degree of U is L_ext + 2; all grids are sized by L_ext)
        self.Lf = Lf if Lf is not None else 2 * self.L_ext + 6
        self.ntheta = ntheta if ntheta is not None else 2 * self.L_ext + 8
        self.nphi = nphi if nphi is not None else 4 * self.L_ext + 14
        self.grid = AngularGrid(self.ntheta, self.nphi, device=device, phi0=phi0)
        A0, A1, A2 = angular_matrices(self.grid, self.modes, self.L_ext, 2)
        self.A0, self.A1, self.A2 = A0, A1, A2            # (Na,Nq), (3,Na,Nq), (3,3,Na,Nq)
        self.n = self.grid.n                              # (Na,3)
        self.Na = self.grid.Na
        self.y = self.r[:, None, None] * self.n[None, :, :]    # (Nr, Na, 3)
        self.rb = RadialBasis(Nk)
        self.free_params = free_params
        self.c_l0, self.omega0 = float(c_l), float(omega)
        # coefficient layout: [A (Nk x Nq), C (Nk x Nq), B (NkB x Nq), D (NkD x Nq), E (NkE x Nq), (c_l, omega)]
        self.layout = [("A", Nk), ("C", Nk), ("B", ch["NkB"]), ("D", ch["NkD"]), ("E", ch["NkE"])]
        self.n_coef = sum(n * self.ncols[name] for name, n in self.layout)
        self.extended_channels = any(self.ncols[nm] != self.Nq for nm in self.ncols)
        self.n_z = self.n_coef + (2 if free_params else 0)
        self.eps = EPS.to(device)

    # ----- parameter handling -----
    def unpack_all(self, z):
        """dict with A, C (leading channels, Nk x Nq), B, D, E (extra channels, possibly 0 x Nq), c_l, omega."""
        Nq = self.Nq
        out = {}; off = 0
        for name, n in self.layout:
            nc = self.ncols[name]
            a = z[off: off + n * nc].reshape(n, nc); off += n * nc
            if nc != Nq:        # scatter the channel's columns into the union mode set (differentiable)
                a = torch.zeros(n, Nq, dtype=z.dtype, device=z.device).index_copy(1, self.chan_cols[name], a)
            out[name] = a
        if self.free_params:
            out["c_l"], out["omega"] = z[-2], z[-1]
        else:
            out["c_l"] = torch.tensor(self.c_l0, dtype=DT, device=z.device)
            out["omega"] = torch.tensor(self.omega0, dtype=DT, device=z.device)
        return out

    def unpack(self, z):
        """Leading channels only (backward compatible): aT = A, aS = C, c_l, omega."""
        d = self.unpack_all(z)
        return d["A"], d["C"], d["c_l"], d["omega"]

    def pack(self, aT, aS, c_l=None, omega=None, extra=None):
        """extra: dict with B, D, E arrays (zeros when absent)."""
        extra = extra or {}
        def gather(name, a):
            return a if self.ncols[name] == self.Nq else a[:, self.chan_cols[name]]
        parts = [gather("A", aT).reshape(-1), gather("C", aS).reshape(-1)]
        for name, n in self.layout[2:]:
            arr = extra.get(name)
            parts.append(gather(name, arr).reshape(-1) if arr is not None else torch.zeros(n * self.ncols[name], dtype=DT, device=aT.device))
        if self.free_params:
            parts.append(torch.stack([torch.as_tensor(c_l, dtype=DT), torch.as_tensor(omega, dtype=DT)]).to(aT.device))
        return torch.cat(parts)

    # ----- radial functions -----
    def radial_derivs(self, aT, aS, c_l, omega, rho=None, K=4, extra=None):
        """Twisted radial derivative arrays gT[n] (n<=3) and gS[n] (n<=4), each (Nr, Nq), including extra channels."""
        rho = self.rho if rho is None else rho
        alpha = alpha_of(c_l)
        R0 = torch.tensor(self.R0, dtype=DT, device=aT.device)
        ch = self.channels
        BT = self.rb.matrices(rho, alpha, R0, self.L_ext, K, shift=0.0)   # (L_ext+1, K+1, Nr, Nk)
        BS = self.rb.matrices(rho, alpha, R0, self.L_ext, K, shift=1.0)
        gT = torch.einsum('qnjk,kq->njq', BT[self.l_idx], aT)
        gS = torch.einsum('qnjk,kq->njq', BS[self.l_idx], aS)
        extra = extra or {}
        if ch["NkB"] > 0 and "B" in extra:
            BB = self.rb.matrices(rho, alpha, R0, self.L_ext, K, power=lambda l: 2 * alpha + 1 + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkB"])
            gT = gT + torch.einsum('qnjk,kq->njq', BB[self.l_idx], extra["B"])
        if ch["NkD"] > 0 and "D" in extra:
            BD = self.rb.matrices(rho, alpha, R0, self.L_ext, K, power=lambda l: 2 * alpha + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkD"])
            gS = gS + torch.einsum('qnjk,kq->njq', BD[self.l_idx], extra["D"])
        C, S = self.rb.twist_tables(rho, omega, c_l, R0, self.Mmax, K)      # (Mmax+1, K+1, Nr)
        gT = self._twist(gT, C, S, K)
        gS = self._twist(gS, C, S, K)
        if ch["NkE"] > 0 and "E" in extra:     # untwisted harmonic channel, l >= 2
            BE = self.rb.matrices(rho, alpha, R0, self.L_ext, K, power=lambda l: torch.as_tensor(2.0 * l + 1.0, dtype=DT, device=rho.device),
                                  core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkE"], lmask=[0, 1])
            gS = gS + torch.einsum('qnjk,kq->njq', BE[self.l_idx], extra["E"])
        return gT, gS

    def _twist(self, g, C, S, K):
        """field = gc cos(m(phi+beta)) + gs sin(m(phi+beta)) = gc' cos(m phi) + gs' sin(m phi) with
        gc' = gc cos(m beta) + gs sin(m beta), gs' = -gc sin(m beta) + gs cos(m beta). Leibniz rule for derivatives."""
        if self.pair_c.numel() == 0:
            return g
        gp = g[:, :, self.partner]                                     # partner radial functions (K+1, Nr, Nq)
        Cm = C[self.m_arr].permute(1, 2, 0)                            # (K+1, Nr, Nq) cos(m beta) derivatives
        Sm = S[self.m_arr].permute(1, 2, 0) * self.tw_sign[None, None, :]
        out = []
        for n in range(K + 1):
            t = 0
            for k in range(n + 1):
                b = math.comb(n, k)
                t = t + b * (g[k] * Cm[n - k] + gp[k] * Sm[n - k])
            out.append(t)
        return torch.stack(out, 0)

    @staticmethod
    def scalar_sets(gT, gS, l, rho):
        """Radial derivative arrays (value, d/drho, d2/drho2) for the scalars T, K_T, D_T, K, D."""
        rho = rho[:, None]; l = l[None, :]
        T = (gT[0], gT[1], gT[2])
        KT = ((l + 1) * gT[0] + 2 * rho * gT[1], (l + 3) * gT[1] + 2 * rho * gT[2], (l + 5) * gT[2] + 2 * rho * gT[3])
        DT_ = ((6 + 4 * l) * gT[1] + 4 * rho * gT[2], (10 + 4 * l) * gT[2] + 4 * rho * gT[3], None)
        K = ((l + 1) * gS[0] + 2 * rho * gS[1], (l + 3) * gS[1] + 2 * rho * gS[2], (l + 5) * gS[2] + 2 * rho * gS[3])
        D = ((6 + 4 * l) * gS[1] + 4 * rho * gS[2], (10 + 4 * l) * gS[2] + 4 * rho * gS[3], (14 + 4 * l) * gS[3] + 4 * rho * gS[4])
        return T, KT, DT_, K, D

    # ----- scalar evaluation on the product grid -----
    def scalar_grid(self, h, need_hess=True):
        """h = (h0, h1, h2) radial arrays (Nr,Nq). Returns f (Nr,Na), grad (3,Nr,Na), hess (3,3,Nr,Na) or None."""
        h0, h1, h2 = h
        r = self.r[:, None]; rl = self.rl; n = self.n.T              # n: (3, Na)
        A0, A1, A2 = self.A0, self.A1, self.A2
        f = (rl * h0) @ A0.T
        G1 = (rl * r * h1) @ A0.T                                     # r^{l+1} g'  -> times n_i
        Gm1 = (rl / r * h0)                                           # r^{l-1} g
        grad = 2 * G1[None] * n[:, None, :] + torch.einsum('jq,iaq->ija', Gm1, A1)
        if not need_hess:
            return f, grad, None
        G2 = (rl * r * r * h2) @ A0.T                                 # r^{l+2} g''
        H1 = (rl * h1)                                                # r^l g'
        H1A0 = H1 @ A0.T
        H1A1 = torch.einsum('jq,iaq->ija', H1, A1)                    # (3,Nr,Na)
        Hm2 = (rl / (r * r) * h0)
        hess = 4 * G2[None, None] * n[:, None, None, :] * n[None, :, None, :]
        eye = torch.eye(3, dtype=DT, device=f.device)
        hess = hess + 2 * (eye[:, :, None, None] * H1A0[None, None] + H1A1[None, :, :, :] * n[:, None, None, :] + H1A1[:, None, :, :] * n[None, :, None, :])
        hess = hess + torch.einsum('jq,ikaq->ikja', Hm2, A2)
        return f, grad, hess

    def fields_grid(self, z, need_vort=True):
        d = self.unpack_all(z)
        gT, gS = self.radial_derivs(d["A"], d["C"], d["c_l"], d["omega"], K=4, extra=d)
        return self._assemble(gT, gS, self.rho, d["c_l"], d["omega"], need_vort, grid=True)

    def _assemble(self, gT, gS, rho, c_l, omega, need_vort, grid=True, pts=None):
        T, KT, DT_, K, D = self.scalar_sets(gT, gS, self.l_arr, rho)
        ev = (lambda h, hh=True: self.scalar_grid(h, hh)) if grid else (lambda h, hh=True: self.scalar_points(h, pts, hh))
        y = self.y if grid else pts
        if grid:
            yv = y.permute(2, 0, 1)                     # (3, Nr, Na)
        else:
            yv = y.T                                    # (3, Np)
        eps = self.eps
        _, gT_, hT_ = ev(T)
        kK, gK, hK = ev(K)
        dD, gD, hD = ev(D, need_vort)
        # U_i = -eps_ijk y_j d_k T + d_i K - y_i D
        U = -torch.einsum('ijk,j...,k...->i...', eps, yv, gT_) + gK - yv * dD[None]
        # d_m U_i = -eps_ijk (delta_jm d_k T + y_j d_m d_k T) + d_m d_i K - delta_im D - y_i d_m D
        GU = -torch.einsum('imk,k...->mi...', eps, gT_) - torch.einsum('ijk,j...,mk...->mi...', eps, yv, hT_) \
             + hK - torch.eye(3, dtype=DT, device=U.device).reshape(3, 3, *([1] * (U.dim() - 1))) * dD[None, None] \
             - yv[None, :] * gD[:, None]
        out = dict(U=U, GU=GU, y=y, c_l=c_l, omega=omega)
        if need_vort:
            _, gKT, hKT = ev(KT)
            dDT, gDT, _ = ev(DT_, False)
            Om = gKT - yv * dDT[None] + torch.einsum('ijk,j...,k...->i...', eps, yv, gD)
            GOm = hKT - torch.eye(3, dtype=DT, device=U.device).reshape(3, 3, *([1] * (U.dim() - 1))) * dDT[None, None] \
                  - yv[None, :] * gDT[:, None] + torch.einsum('imk,k...->mi...', eps, gD) \
                  + torch.einsum('ijk,j...,mk...->mi...', eps, yv, hD)
            out.update(Om=Om, GOm=GOm)
        return out

    # ----- Laplacian of the velocity (Stage II S8 artificial viscosity, lead 2026-10-25T04:55Z / 05:18Z) -----
    @staticmethod
    def _laplacian_radial(g, l, rho, K_out):
        """Radial derivative arrays of the Laplacian of a potential: for f(rho) P_q(y) (P_q a degree-l solid harmonic, rho = r^2),
        Delta[f P_q] = [(6 + 4 l) f' + 4 rho f''] P_q (' = d/drho); the n-th rho-derivative of that radial function is
        (6 + 4 l + 4 n) f^(n+1) + 4 rho f^(n+2). g: (K+1, Nr, Nq) derivative arrays of f (K >= K_out + 2)."""
        rho = rho[:, None]; l = l[None, :]
        return torch.stack([(6 + 4 * l + 4 * n) * g[n + 1] + 4 * rho * g[n + 2] for n in range(K_out + 1)], 0)

    def _laplacian_assemble(self, z, rho, grid, pts=None):
        d = self.unpack_all(z)
        gT, gS = self.radial_derivs(d["A"], d["C"], d["c_l"], d["omega"], rho=rho, K=6, extra=d)
        gDT = self._laplacian_radial(gT, self.l_arr, rho, 4); gDS = self._laplacian_radial(gS, self.l_arr, rho, 4)
        # Delta U = curl((Delta T) y) + curl curl((Delta S) y): the same assembly with the Laplacian radial functions
        return self._assemble(gDT, gDS, rho, d["c_l"], d["omega"], False, grid=grid, pts=pts)["U"]

    def laplacian_grid(self, z):
        """Delta U (3, Nr, Na) on the product grid."""
        return self._laplacian_assemble(z, self.rho, True)

    def laplacian_points(self, z, pts, table_path="dd"):
        """Delta U (3, Np) at arbitrary Cartesian points. table_path: angular-table path ("dd" production; "fp64" for diagnostics that request it by name)."""
        pts = torch.as_tensor(pts, dtype=DT, device=self.r.device)
        rho = (pts ** 2).sum(-1)
        self._pt_cache = eval_solid(pts, self.modes, self.L_ext, 2, path=table_path)
        return self._laplacian_assemble(z, rho, False, pts=pts)

    # ----- evaluation at arbitrary Cartesian points (validation; regular at origin and axis) -----
    def scalar_points(self, h, pts, need_hess=True):
        h0, h1, h2 = h
        P0, P1, P2 = self._pt_cache
        f = (h0 * P0).sum(-1)
        grad = 2 * torch.einsum('pq,pq->p', h1, P0)[None] * pts.T + torch.einsum('pq,ipq->ip', h0, P1)
        if not need_hess:
            return f, grad, None
        yy = pts.T
        eye = torch.eye(3, dtype=DT, device=pts.device)
        hess = 4 * torch.einsum('pq,pq->p', h2, P0)[None, None] * yy[:, None] * yy[None, :]
        H1P0 = torch.einsum('pq,pq->p', h1, P0)
        H1P1 = torch.einsum('pq,ipq->ip', h1, P1)
        hess = hess + 2 * (eye[:, :, None] * H1P0[None, None] + yy[:, None] * H1P1[None, :] + yy[None, :] * H1P1[:, None])
        hess = hess + torch.einsum('pq,ikpq->ikp', h0, P2)
        return f, grad, hess

    def fields_points(self, z, pts, need_vort=True, table_path="dd"):
        """pts: (Np, 3) Cartesian points (may include the origin and axis points). table_path: angular-table path ("dd" production double-double;
        "fp64" only for diagnostics that request the frozen float64 tables by name, e.g. the ray-integral cross-check on 5e5 scattered points)."""
        pts = torch.as_tensor(pts, dtype=DT, device=self.r.device)
        d = self.unpack_all(z)
        rho = (pts ** 2).sum(-1)
        gT, gS = self.radial_derivs(d["A"], d["C"], d["c_l"], d["omega"], rho=rho, K=4, extra=d)
        self._pt_cache = eval_solid(pts, self.modes, self.L_ext, 2, path=table_path)
        out = self._assemble(gT, gS, rho, d["c_l"], d["omega"], need_vort, grid=False, pts=pts)
        return out
