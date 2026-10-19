"""
hybrid.py -- interior collocation + far field slaved by characteristics.

Unknowns: b on the compactified grid (all (N+1) x M values) and c_l, but the EQUATIONS differ by region:
  rows at r_i <= R_i (interior, i >= 1):   collocation residual E[b, c_l] - (1 - eps) S0 (S0 cut off to the interior)
  rows at r_i >  R_i (far field):          b_i - T_i(b, c_l) = 0, where T_i is the value obtained by transporting rho along
                                            the backward characteristic from X_i to its entry point into the disk r <= R_i
                                            (rho(X_i) = e^{T} rho(X_entry), rho(X_entry) from the spectral interpolant of b)
  row 0 (r = 0):                           b(0, theta_j) = 1
  last row:                                3 c_l - 1 - c[b] = 0
The far-field rows have no near-null space: a far-field perturbation changes b_i - T_i by itself (T depends on the far field
only through the velocity).  Jacobian: analytic for collocation/normalisation/identity rows (solve.Newton.jacobian),
batched finite differences for the T rows (all perturbed fields integrated together, src/batchmap.BatchFieldEval).
"""
import sys, math, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, batchmap, charac


class Hybrid:
    def __init__(self, m, R_i, dt=0.01, verbose=True):
        self.m, self.R_i, self.dt = m, R_i, dt
        self.nw = solve.Newton(m, verbose=False, chunk=1024)
        N, M = m.N, m.M
        self.N, self.M = N, M
        rr = m.rad.rR
        self.far_idx = torch.where(rr > R_i)[0]                 # radial indices of far points
        self.int_idx = torch.where((rr <= R_i) & (rr > 0))[0]
        self.n = (N + 1) * M
        # flattened indices of far rows
        self.far_rows = (self.far_idx[:, None] * M + torch.arange(M, device=m.dev)[None, :]).reshape(-1)
        self.verbose = verbose
        cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
        r = rr[:, None]
        self.Xf = (r * cos)[self.far_idx].reshape(-1); self.Yf = (r * sin)[self.far_idx].reshape(-1)
        self.pref = (r ** 3 * m.wR[:, None] * cos ** 2 * sin)    # rho = pref * b
        if verbose:
            print(f"[Hybrid] N={N} M={M} R_i={R_i}: {len(self.int_idx)} interior radii, {len(self.far_idx)} far radii, {len(self.far_rows)} far rows", flush=True)

    # ---- transport of the far field ------------------------------------------------------------------------
    def transport(self, Bb, cl_col):
        """For a batch of fields Bb (B, N+1, M) with per-column c_l: returns T (B, nfar) = transported b at far points."""
        m = self.m; B = Bb.shape[0]; dev = m.dev
        fe = batchmap.BatchFieldEval(m, Bb, cl_col)
        K = self.Xf.shape[0]
        col = torch.arange(B, device=dev).repeat_interleave(K)
        X = self.Xf.repeat(B); Y = self.Yf.repeat(B)
        # backward integration until r <= R_i  (entry point), exact entry time by log interpolation in r
        x = X.clone(); y = Y.clone(); T = torch.zeros(B * K, device=dev); done = torch.zeros(B * K, dtype=torch.bool, device=dev)
        xe = torch.zeros_like(x); ye = torch.zeros_like(y)
        dt = self.dt; nsteps = int(60.0 / dt)
        for step in range(nsteps):
            act = torch.where(~done)[0]
            if len(act) == 0: break
            xa, ya, ca = x[act], y[act], col[act]
            def rhs(xx, yy):
                W1, W2, _ = fe.velocity(xx, yy, ca); return -W1, -W2
            k1x, k1y = rhs(xa, ya); k2x, k2y = rhs(xa + 0.5 * dt * k1x, ya + 0.5 * dt * k1y)
            k3x, k3y = rhs(xa + 0.5 * dt * k2x, ya + 0.5 * dt * k2y); k4x, k4y = rhs(xa + dt * k3x, ya + dt * k3y)
            xn = xa + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x); yn = ya + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
            ra = torch.sqrt(xa ** 2 + ya ** 2); rn = torch.sqrt(xn ** 2 + yn ** 2)
            inside = rn <= self.R_i
            # entry fraction by log-linear interpolation of r
            tau = torch.where(inside, torch.log(ra / self.R_i) / torch.log((ra / rn).clamp_min(1 + 1e-15)), torch.zeros_like(ra)).clamp(0, 1)
            xe_ = xa + tau * (xn - xa); ye_ = ya + tau * (yn - ya)
            idx_in = act[inside]
            xe[idx_in] = xe_[inside]; ye[idx_in] = ye_[inside]; T[idx_in] += (tau * dt)[inside]; done[idx_in] = True
            keep = ~inside
            x[act[keep]] = xn[keep]; y[act[keep]] = yn[keep]; T[act[keep]] += dt
        # rho at entry points from the spectral interpolant of each column's b, then rho(X) = e^T rho(entry)
        rho_e = self._rho_at(Bb, xe, ye, col)
        rho_X = torch.exp(T) * rho_e
        # convert to b at the far points
        pref_far = self.pref[self.far_idx].reshape(-1).repeat(B)
        Tb = (rho_X / pref_far).reshape(B, K)
        self._last = dict(T=T, xe=xe, ye=ye, pref_far=pref_far)
        return Tb, done.reshape(B, K).all(1)

    def _rho_at(self, Bb, x, y, col):
        """rho from the spectral representation of column col at points (x, y) (x, y >= 0 assumed; parity otherwise)."""
        m = self.m
        xa, ya = x.abs(), y.abs()
        r = torch.sqrt(xa ** 2 + ya ** 2); th = torch.atan2(ya, xa)
        fe0 = charac.FieldEval.__new__(charac.FieldEval); fe0.m = m
        fe0.tR = m.rad.tR; fe0.wbar = torch.tensor(ipm1.bary_weights(m.rad.tR_np), device=m.dev)
        t = fe0.t_of_r(r); P = fe0.radial_interp_matrix(t)                     # (K, Nr)
        C = m.ang.to_coef(Bb, 'EE')                                             # (B, Nr, M)
        Cn = torch.einsum('kn,knm->km', P, C[col])                               # (K, M)
        sv = m.ang.s_of_theta(th); k = torch.arange(m.M, device=m.dev, dtype=torch.float64)
        bval = (Cn * torch.cos(sv[:, None] * (2 * k)[None, :])).sum(1)
        w = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return r ** 3 * w * torch.cos(th) ** 2 * torch.sin(th) * bval * torch.sign(y)

    # ---- residual and Jacobian -----------------------------------------------------------------------------
    def residual(self, b, cl, S0=None, eps=1.0, flds=None):
        """Full residual vector (n+1,): collocation rows (interior) with homotopy source, far rows b - T, norm rows, identity."""
        m = self.m
        F, flds = self.nw.residual_full(b, cl, flds=flds, hom=(None if S0 is None else (eps, S0, 0.0)))
        Tb, ok = self.transport(b[None], torch.tensor([cl], device=m.dev))
        F = F.clone()
        F[self.far_rows] = b.reshape(-1)[self.far_rows] - Tb[0]
        return F, flds, ok[0].item()

    def far_jacobian_analytic(self, b, cl):
        """d(T)/db at frozen trajectories: T_i = e^{T_i} pref(X_e)/pref_i * L_i b, L_i = interpolation row at the entry point."""
        m = self.m; dev = m.dev
        Tb, ok = self.transport(b[None], torch.tensor([cl], device=dev))
        d = self._last; T = d['T']; xe, ye = d['xe'], d['ye']
        r = torch.sqrt(xe ** 2 + ye ** 2); th = torch.atan2(ye.abs(), xe.abs())
        fe0 = charac.FieldEval.__new__(charac.FieldEval); fe0.m = m; fe0.tR = m.rad.tR; fe0.wbar = torch.tensor(ipm1.bary_weights(m.rad.tR_np), device=dev)
        t = fe0.t_of_r(r); P = fe0.radial_interp_matrix(t)                                   # (K, Nr)
        sv = m.ang.s_of_theta(th); k = torch.arange(m.M, device=dev, dtype=torch.float64)
        Aang = torch.cos(sv[:, None] * (2 * k)[None, :]) @ m.ang.A['EE']                       # (K, M): values -> b(theta_e)
        w = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        pref_e = r ** 3 * w * torch.cos(th) ** 2 * torch.sin(th) * torch.sign(ye)
        fac = torch.exp(T) * pref_e / d['pref_far']                                           # (K,)
        L = (P[:, :, None] * Aang[:, None, :]).reshape(P.shape[0], -1)                        # (K, n) kron rows
        return fac[:, None] * L, Tb[0]

    def jacobian(self, b, cl, flds, S0=None, eps=1.0, fd_eps=1e-6, chunk=400, mode='analytic'):
        m = self.m; n = self.n; dev = m.dev
        J = self.nw.jacobian(b, cl, flds)                      # analytic (collocation, norm, identity rows)
        bf = b.reshape(-1)
        Jfar = torch.zeros(len(self.far_rows), n + 1, device=dev)
        if mode == 'analytic':
            dT, T0 = self.far_jacobian_analytic(b, cl)
            Jfar[:, :n] = -dT
            epsc = 1e-6 * max(1.0, abs(cl))
            Tc, _ = self.transport(b[None], torch.tensor([cl + epsc], device=dev))
            Jfar[:, n] = -(Tc[0] - T0) / epsc
            Jfar[torch.arange(len(self.far_rows)), self.far_rows] += 1.0
            J[self.far_rows, :] = Jfar
            return J
        # far rows: d(b_far - T)/d(b, cl) by batched FD (exact, slow)
        T0, _ = self.transport(b[None], torch.tensor([cl], device=dev)); T0 = T0[0]
        cols = torch.arange(n, device=dev)
        for s in range(0, n, chunk):
            e = min(n, s + chunk); idxs = cols[s:e]
            Bb = bf[None, :].repeat(e - s, 1)
            epsv = fd_eps * torch.maximum(torch.ones(e - s, device=dev), bf[idxs].abs())
            Bb[torch.arange(e - s), idxs] += epsv
            TB, _ = self.transport(Bb.reshape(e - s, self.N + 1, self.M), torch.full((e - s,), cl, device=dev))
            Jfar[:, s:e] = -((TB - T0[None, :]) / epsv[:, None]).T
        epsc = 1e-6 * max(1.0, abs(cl))
        Tc, _ = self.transport(b[None], torch.tensor([cl + epsc], device=dev))
        Jfar[:, n] = -(Tc[0] - T0) / epsc
        Jfar[torch.arange(len(self.far_rows)), self.far_rows] += 1.0
        J[self.far_rows, :] = Jfar
        return J

    def solve(self, b, cl, S0=None, eps=1.0, tol=1e-9, maxit=20, log=None):
        m = self.m
        F, flds, ok = self.residual(b, cl, S0, eps)
        nrm = F.abs().max().item(); hist = [nrm]
        if self.verbose: print(f"[Hybrid] eps={eps:.4f} it 0 |F|_inf={nrm:.3e} (far rows max {F[self.far_rows].abs().max().item():.2e}) c_l={cl:.8f} ok={ok}", flush=True)
        for it in range(1, maxit + 1):
            if nrm < tol: break
            t0 = time.time()
            J = self.jacobian(b, cl, flds, S0, eps)
            d = torch.linalg.solve(J, -F)
            alpha = 1.0; accepted = False
            for _ in range(8):
                bt = b + alpha * d[:-1].reshape(self.N + 1, self.M); clt = cl + alpha * d[-1].item()
                Ft, fldst, okt = self.residual(bt, clt, S0, eps)
                nt = Ft.abs().max().item()
                if nt < nrm * (1 - 1e-4 * alpha):
                    b, cl, F, flds, nrm, accepted = bt, clt, Ft, fldst, nt, True; break
                alpha *= 0.5
            hist.append(nrm)
            if self.verbose: print(f"[Hybrid] eps={eps:.4f} it {it} |F|_inf={nrm:.3e} (far {F[self.far_rows].abs().max().item():.2e}, coll {F[:self.far_rows[0]].abs().max().item():.2e}) c_l={cl:.8f} alpha={alpha:.3g} ({time.time()-t0:.0f}s)", flush=True)
            if log is not None: log.write(f"{eps:.5f} {it} {nrm:.6e} {cl:.12f}\n"); log.flush()
            if not accepted: break
        return b, cl, dict(converged=nrm < tol, nrm=nrm, hist=hist)
