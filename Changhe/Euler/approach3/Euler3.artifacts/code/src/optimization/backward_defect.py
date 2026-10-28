"""Stage II arms S2 and S3 (lead reports/stage2_plan_draft.md, notes 2026-10-25T02:54Z item 8 and 03:17Z item 1): the backward defect
    d(U) = U + G N(U),  N(U) = (U.grad)U + grad P,  G = L^-1 (twisted-ray inverse, azimuthal-mode form, SPEC v1.22),
so that R_u = L U + N(U) and d(U) = G R_u (G L U = U for U bounded near 0). Prototype implementation:
 * dense radial grid = geometric grid (n_per_octave radii per octave from R0 2^-k_in to R0 2^k_out) UNION the training radii of the model,
   with the model's own angular grid, so d(U) is available exactly at the training nodes for the Galerkin projection P_n (weighted least-squares
   fit onto the basis, fixed-gauge weights as in transfer.fit_field; tail-constrained reduced coordinates);
 * G in the azimuthal-mode form with the composite trapezoid rule in log rho on the non-uniform union grid; the cut-off [0, rho_min] is omitted;
 * everything is differentiable in the coefficient vector (torch), so JVPs come from forward-mode AD (torch.func.jvp) and the dense Jacobian of
   a -> P_n d(U(a)) from jacobian_fwd; S2 bordered Newton system (n + 2 unknowns: reduced coefficients and the two border scalars mu_D, mu_R;
   n projected equations P_n d + mu_D P_n Z_D + mu_R P_n Z_R = 0 and the two gauge rows g_1 = (||F_U||^2 - 1)/2, g_2 = pivot sin amplitude);
 * S3 stabilized fixed point U <- S[P_n m(U)^2 T(U)], T = -G N(U), m = <U,U>_eta/<U,T>_eta (weight |y|^-eta), S = unit-tail dilation + phase
   alignment; plain normalized control U <- S[P_n T(U)].
No loss is minimized here; the readings are the GMRES counts, sigma_min, step lengths, projection defects and the S3 change ratios."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver
from .lm import jacobian_fwd

DT = torch.float64


class BackwardDefect:
    def __init__(self, prob, tc=None, n_per_octave=16, k_in=14, k_out=16, eta=2.0):
        self.prob = prob; self.model = model = prob.model; self.tc = tc; self.eta = float(eta)
        dev = model.r.device; R0 = model.R0
        self.c_l = float(model.c_l0); self.omega = float(model.omega0); self.alpha = alpha_of(self.c_l); self.kappa = self.omega / self.c_l
        radii = R0 * 2.0 ** np.linspace(-k_in, k_out, n_per_octave * (k_in + k_out) + 1)     # uniform in log r
        r_tr = model.r.detach().cpu().numpy()
        assert r_tr.min() >= radii[0] and r_tr.max() <= radii[-1] * (1 + 1e-12), "training radii outside the dense grid"
        self.radii = radii
        lr_d = np.log(radii); h = lr_d[1] - lr_d[0]
        # cubic Lagrange interpolation in log r from the dense grid to the training radii (fixed linear map, O(h^4))
        Pint = np.zeros((len(r_tr), len(radii)))
        for i, rv in enumerate(r_tr):
            x = math.log(rv); j = int(np.clip(np.floor((x - lr_d[0]) / h), 1, len(radii) - 3))
            idx = [j - 1, j, j + 1, j + 2]
            for a_ in idx:
                w_ = 1.0
                for b_ in idx:
                    if b_ != a_:
                        w_ *= (x - lr_d[b_]) / (lr_d[a_] - lr_d[b_])
                Pint[i, a_] = w_
        self.Pint = torch.tensor(Pint, dtype=DT, device=dev)
        # cumulative integration weights in log r: each interval [j-1, j] integrates the cubic through j-2..j+1 (O(h^4)); W lower triangular
        n_d = len(radii); W = np.zeros((n_d, n_d))
        def cubic_weights(x0, x1, nodes):
            ws = []
            for a_ in range(4):
                # integral of the Lagrange basis polynomial over [x0, x1] by 4-point Gauss (exact for cubics)
                xg, wg = np.polynomial.legendre.leggauss(4); xs = 0.5 * (x1 - x0) * xg + 0.5 * (x0 + x1)
                val = np.ones_like(xs)
                for b_ in range(4):
                    if b_ != a_:
                        val *= (xs - nodes[b_]) / (nodes[a_] - nodes[b_])
                ws.append(0.5 * (x1 - x0) * (wg * val).sum())
            return ws
        row = np.zeros(n_d)
        for j in range(1, n_d):
            j0 = int(np.clip(j - 2, 0, n_d - 4)); idx = [j0, j0 + 1, j0 + 2, j0 + 3]
            ws = cubic_weights(lr_d[j - 1], lr_d[j], lr_d[idx])
            for a_, w_ in zip(idx, ws):
                row[a_] += w_
            W[j] = row
        self.Wcum = torch.tensor(W, dtype=DT, device=dev)
        phi0 = float(model.grid.phi[0].item())
        self.em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=R0, r_nodes=radii, ntheta=model.ntheta, nphi=model.nphi, c_l=model.c_l0, omega=model.omega0,
                        free_params=model.free_params, channels=model.channels, device=dev, phi0=phi0)
        assert float((self.em.grid.n - model.grid.n).abs().max()) < 1e-12, "angular grids differ"
        self.ps = PressureSolver(model, p0=2 * self.alpha + 2, omega=self.omega, c_l=self.c_l, eval_model=self.em)
        self.r = self.em.r; self.lr = torch.log(self.r)
        self.ntheta, self.nphi = model.ntheta, model.nphi
        er, eth, eph = self.em.grid.sph_basis(); self.sph = (er, eth, eph)
        self.mvals = torch.arange(self.nphi // 2 + 1, dtype=DT, device=dev)
        dlr = self.lr[1:] - self.lr[:-1]
        self.dlr = dlr
        self.rho_min = float(self.r[0])
        # weights of <., .>_eta: int f |y|^-eta dy = sum_j w_j r_j^(3-eta) * (angular mean * 4 pi); trapezoid in log r
        wlog = torch.zeros_like(self.r); wlog[1:] += 0.5 * dlr; wlog[:-1] += 0.5 * dlr
        self.w_eta = wlog * self.r ** (3.0 - self.eta)                     # (Nr,)
        self.w_ang = self.em.grid.w                                        # (Na,) sum 4 pi
        # projection P_n: basis matrix at the training nodes in reduced coordinates, fixed-gauge weights (transfer.fit_field)
        n = model.n_coef if tc is None else tc.n_red
        self.n_red = n
        def to_full(zc):
            zc = tc.expand(zc) if tc is not None else zc
            return torch.cat([zc, torch.tensor([model.c_l0, model.omega0], dtype=DT, device=dev)]) if model.free_params else zc
        self.to_full = to_full
        def field_flat(zc):
            return model.fields_grid(to_full(zc), need_vort=False)['U'].reshape(-1)
        z0 = torch.zeros(n, dtype=DT, device=dev)
        B = jacobian_fwd(field_flat, z0, chunk=128)                        # (3 Nr Na, n), linear (no constant term for the tail-constrained map)
        self.B_const = field_flat(z0)                                      # exactly zero for a linear map
        w = ((1 + model.rho / R0 ** 2) ** self.alpha)[:, None] * (model.grid.w / (4 * math.pi))[None, :]
        self.wv = w.expand(3, -1, -1).reshape(-1).sqrt()
        Bw = B * self.wv[:, None]
        self.cs = Bw.norm(dim=0).clamp_min(1e-300)
        Q, R = torch.linalg.qr(Bw / self.cs[None, :], mode="reduced")      # column-scaled QR for the projection
        self.Q, self.R = Q, R
        self.B = B
        self.proj_cond = float(torch.linalg.cond(R))

    # ----- fields, pressure, N(U), G -----
    def fields(self, z):
        return self.em.fields_grid(z, need_vort=False)

    def terms(self, z):
        F = self.fields(z)
        f_src = res.pressure_source(self.model.fields_grid(z, need_vort=False)['GU'])
        P, gradP, _, _ = self.ps.solve(f_src)
        from ..validation.spec_diagnostics import five_term_split
        T = five_term_split(F, gradP)
        return F, T

    def _modes(self, X):
        er, eth, eph = self.sph
        Xs = torch.stack([torch.einsum('ija,ai->ja', X, e) for e in (er, eth, eph)], 0).reshape(3, X.shape[1], self.ntheta, self.nphi)
        return torch.fft.rfft(Xs, dim=-1) / self.nphi

    def _from_modes(self, M):
        Xs = torch.fft.irfft(M * self.nphi, n=self.nphi, dim=-1).reshape(3, M.shape[1], -1)      # spherical components (3, Nr, Na)
        er, eth, eph = self.sph
        return Xs[0][None] * er.T[:, None, :] + Xs[1][None] * eth.T[:, None, :] + Xs[2][None] * eph.T[:, None, :]

    def apply_G(self, X):
        """Cartesian (3, Nr, Na) on the dense grid -> G X (Cartesian), azimuthal-mode form: (G f)_m(r) = (1/c_l) r^-alpha int_0^r rho^(alpha-1)
        (r/rho)^(i m kappa) f_m(rho) d rho; cumulative O(h^4) quadrature in log rho plus the analytic cut-off part [0, rho_min] with
        f_m(rho) ~ f_m(rho_min) (constant extrapolation; exact for the regular m = 0 components, O(rho_min^alpha) overall)."""
        M = self._modes(X)                                                                           # (3, Nr, ntheta, Mm) complex
        phase = torch.exp(-1j * (self.mvals[None, :] * self.kappa) * self.lr[:, None])                # rho^(-i m kappa)
        g = M * (self.r ** self.alpha)[None, :, None, None] * phase[None, :, None, :]                 # rho^(alpha-1) f_m * rho (d rho = rho dlog rho)
        c = torch.einsum('jk,ikam->ijam', self.Wcum.to(g.dtype), g)                                  # cumulative integral from rho_min
        zc = self.alpha - 1j * self.mvals * self.kappa                                                # int_0^rho_min rho^(alpha-1-i m kappa) d rho = rho_min^(alpha - i m kappa)/(alpha - i m kappa)
        c0 = M[:, 0] * (self.rho_min ** zc)[None, None, :] / zc[None, None, :]                         # (3, ntheta, Mm)
        c = c + c0[:, None]
        GM = (1.0 / self.c_l) * (self.r ** (-self.alpha))[None, :, None, None] * torch.exp(1j * (self.mvals[None, :] * self.kappa) * self.lr[:, None])[None, :, None, :] * c
        return self._from_modes(GM)

    def to_train(self, X):
        """Dense-grid field (3, Nr, Na) -> training radii (3, Nr_train, Na) by the fixed cubic interpolation in log r."""
        return torch.einsum('tj,ija->ita', self.Pint, X)

    def defect(self, z):
        """d(U) = U + G N(U) on the dense grid (Cartesian); also returns U, N, L U and G R_u for checks."""
        F, T = self.terms(z)
        U = F['U']; N = T[3] + T[4]; LU = T[0] + T[1] + T[2]
        GN = self.apply_G(N)
        return dict(d=U + GN, U=U, N=N, LU=LU, GN=GN, Ru=LU + N)

    def defect_train(self, zc):
        """Reduced coefficients -> d(U) at the training nodes, flattened (3 Nr Na,), differentiable."""
        z = self.to_full(zc)
        out = self.defect(z)
        return self.to_train(out["d"]).reshape(-1)

    # ----- projection -----
    def project(self, X_train_flat):
        """Weighted least-squares coefficients (reduced) of a field given at the training nodes; returns (zc, projection defect)."""
        bw = X_train_flat * self.wv
        y = self.Q.T @ bw
        zc = torch.linalg.solve_triangular(self.R, y[:, None], upper=True)[:, 0] / self.cs
        resid = (self.Q @ y - bw).norm() / bw.norm().clamp_min(1e-300)
        return zc, float(resid)

    def project_differentiable(self, X_train_flat):
        bw = X_train_flat * self.wv
        y = self.Q.T @ bw
        return torch.linalg.solve_triangular(self.R, y[:, None], upper=True)[:, 0] / self.cs

    # ----- inner product and gauges -----
    def inner_eta(self, X, Y):
        """<X, Y>_eta = int X.Y |y|^-eta dy on the dense grid."""
        per_node = ((X * Y).sum(0) * self.w_ang[None, :]).sum(1)         # (Nr,)
        return float((per_node * self.w_eta).sum())

    def generators(self, z):
        """Dilation generator Z_D = U - (y.grad)U and rotation generator Z_R = J U - (J y.grad)U on the dense grid."""
        F = self.fields(z); U, GU = F['U'], F['GU']; yv = res.yvec(F['y']); Jy = res.Jvec(yv)
        ZD = U - torch.einsum('m...,mi...->i...', yv, GU)
        ZR = res.Jvec(U) - torch.einsum('m...,mi...->i...', Jy, GU)
        return ZD, ZR

    def normalize(self, z):
        """S: dilate to the unit tail norm (int_S2 |F|^2 = 1), then align the phase (Problem.phase_align). The dilated field L U(y/L) is refitted."""
        prob = self.prob; model = self.model
        aT, aS, c_l, omega = model.unpack(z)
        F2 = float(prob.tail_norm2(aT, aS, c_l, omega))
        Lfac = F2 ** (-1.0 / (2 * (self.alpha + 1)))                       # tail norm scales by L^(2 (alpha + 1))
        if abs(Lfac - 1.0) > 1e-14:
            em2 = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=model.r.detach().cpu().numpy() / Lfac, ntheta=model.ntheta, nphi=model.nphi,
                        c_l=model.c_l0, omega=model.omega0, free_params=model.free_params, channels=model.channels, device=z.device, phi0=float(model.grid.phi[0].item()))
            UL = Lfac * em2.fields_grid(z, need_vort=False)['U']           # L U(y/L) at the training nodes
            zc, pdef = self.project(UL.reshape(-1))
            z = self.to_full(zc)
        else:
            pdef = 0.0
        if prob.pivot is None:
            prob.pivot = prob.choose_pivot(z)
        z = prob.phase_align(z)
        aT, aS, c_l, omega = model.unpack(z)
        return z, dict(dilation=Lfac, tail_norm2_after=float(prob.tail_norm2(aT, aS, c_l, omega)), refit_defect=pdef)

    def gauge_rows(self, zc):
        z = self.to_full(zc); model = self.model; prob = self.prob
        aT, aS, c_l, omega = model.unpack(z)
        g1 = 0.5 * (prob.tail_norm2(aT, aS, c_l, omega) - 1.0)
        if prob.pivot is None:
            prob.pivot = prob.choose_pivot(z)
        q = prob.pivot["q"]; arr = aT if prob.pivot["pot"] == "T" else aS
        g2 = arr[:, q + 1].sum() * model.R0 ** (self.alpha + float(model.l_arr[q]) - (0.0 if prob.pivot["pot"] == "T" else 1.0))
        return torch.stack([g1, g2])
