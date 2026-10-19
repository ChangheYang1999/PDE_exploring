"""
ipm1lsq.py -- oversampled least-squares (Gauss-Newton / Levenberg-Marquardt) solver for the disk closure (ipm1disk.IPM1Disk).

Why: the square collocation system (solve.py) is numerically singular (smallest singular values 1e-7 .. 5e-9) and its
solutions satisfy the equation only AT the Radau x midpoint nodes; between nodes the field has residual 1e-5 .. 4e-3
(verifier G16/G24).  Here the divided transport equation E[b, c_l] is evaluated on a finer quadrature grid
(Chebyshev-Gauss points in t, Qr of them, times midpoint angles, Qth of them; default Qr = 2N, Qth = 2M) and the sum of
squares of the pointwise-normalised residual is minimised over the Radau values b (rows >= 1; b(0, theta) = 1 fixed).
The identity 3 c_l - 1 = c[b] is eliminated exactly: c_l = (1 + c[b]) / 3 with c[b] = psi_xy(0) from the Green function
(k_tail = 1/c_l made self-consistent by a short fixed-point loop).  No free parameter, no fitted c_l.

Row normalisation (frozen at the start, refreshed on request): den = |b| + |r b_r + (3 + om) b| + |(U_r/r)(r b_r + (3+om) b)|
+ |(U_th/r) b_th| + floor, i.e. the sizes of the terms of E (the N4 denominator divided by x^2 y w, without the
axis-singular pieces).  Rows get weight 1/den.  Uniform quadrature weights (Chebyshev-Gauss points carry the Chebyshev
measure, so this is the L2 norm with weight 1/sqrt(1 - t^2) dt dtheta).

Jacobian: exact (velocity maps are linear in b; the map b -> psi mode functions PsiC on the Lobatto grid is stored as a dense
matrix Lpsi), built column-chunk by column-chunk directly on the quadrature grid, plus the rank-one c_l terms
(dc_l/db = cvec/3) and a finite-difference term for the dependence of the tail exponent k = 1/c_l.
"""
import math, time
import numpy as np
import torch
import ipm1, ipm1disk
from ipm1 import bary_weights, interp_matrix


class LSQ:
    def __init__(self, m: 'ipm1disk.IPM1Disk', Qr=None, Qth=None, chunk=256, verbose=True, points='gauss', den_floor=1e-3, centre_weight=True):
        self.m = m; N, M = m.N, m.M; self.N, self.M = N, M
        self.centre_weight = centre_weight
        self.n_all = (N + 1) * M; self.n = N * M            # free unknowns: rows 1..N of b
        self.chunk, self.verbose, self.den_floor = chunk, verbose, den_floor
        dev = m.dev; self.dev = dev
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=dev)
        if points == 'radau':                                 # test mode: the Radau nodes (t > -1) and the coarse angles
            Qr, Qth = N, M
            tq = m.rad.tR_np[1:]; thq = m.ang.theta_np
        else:
            Qr = Qr or 2 * N; Qth = Qth or 2 * M + 1          # 2M + 1: the residual's cos(4M theta) content vanishes on 2M midpoints
            tq = -np.cos(np.pi * (np.arange(Qr) + 0.5) / Qr)
            thq = (np.arange(Qth) + 0.5) * np.pi / (2 * Qth)
        self.Qr, self.Qth, self.Q = Qr, Qth, Qr * Qth
        wR = bary_weights(m.rad.tR_np); wL = bary_weights(m.rad.tL_np)
        self.Pq_R = T(interp_matrix(m.rad.tR_np, tq, wR))            # Radau values -> quadrature radii   (Qr, N+1)
        self.PDq = self.Pq_R @ m.rad.DR                                # Radau values -> d/dt at quadrature radii
        self.PLq = T(interp_matrix(m.rad.tL_np, tq, wL))             # Lobatto values -> quadrature radii  (Qr, N+1)
        self.PLDq = self.PLq @ m.rad.DL
        self.tq = T(tq); self.rq = m.rad.rmap(self.tq); self.Sq = self.rq / m.rad.drdt(self.tq)
        self.thq = T(thq)
        k = torch.arange(M, device=dev, dtype=torch.float64)
        self.Tq = torch.cos(self.thq[:, None] * (2 * k)[None, :]) @ m.ang.A['EE']                       # (Qth, M) values -> values at thq
        self.Tdq = (-(2 * k)[None, :] * torch.sin(self.thq[:, None] * (2 * k)[None, :])) @ m.ang.A['EE']  # -> d/dtheta at thq
        nf = m.nf
        self.sinq = torch.sin(self.thq[:, None] * nf[None, :])            # (Qth, nmodes)
        self.ncosq = nf[None, :] * torch.cos(self.thq[:, None] * nf[None, :])
        L, g = m.L, m.gamma
        self.s2q = self.rq ** 2 / (L ** 2 + self.rq ** 2)
        self.vq = (1 + self.rq ** 2 / L ** 2) ** ((g - 1) / 2)
        self.omq = (g - 3) * self.s2q; self.kapq = 2 + (g - 1) * self.s2q
        self.cq, self.sq = torch.cos(self.thq), torch.sin(self.thq)
        self.Lpsi = None; self.k_frozen = None
        self.wrow = None
        self.step_method = 'qr2'
        self.extra_rows = []          # list of ('h', weight) and/or ('char', weight): extra residual rows with exact gradients
        self.char_rows = None         # charrows.CharRows instance for 'char'
        self.cfix_target = None       # target c_l for the 'cfix' row

    # ------------------------------------------------------------------ fields on the quadrature grid
    def quad_fields(self, PsiC):
        """PsiC: (..., N+1, nmodes) Lobatto mode functions -> Ur/r, Uth/r, coefU on the quadrature grid (..., Qr, Qth)."""
        Psi_n = self.PLq @ PsiC; rPsi_n = self.Sq[:, None] * (self.PLDq @ PsiC)
        Psi = Psi_n @ self.sinq.T; rPsi_r = rPsi_n @ self.sinq.T; Psi_th = Psi_n @ self.ncosq.T
        G = self.kapq[:, None] * Psi + rPsi_r
        c, s = self.cq[None, :], self.sq[None, :]
        U1h = -(s * G + c * Psi_th); U2h = c * G - s * Psi_th
        v = self.vq[:, None]
        return v * (U1h * c + U2h * s), v * (-U1h * s + U2h * c), v * (2 * U1h / c + U2h / s)

    def bq_fields(self, b):
        """b (..., N+1, M) -> b, r b_r, b_theta at the quadrature grid."""
        bq = self.Pq_R @ b @ self.Tq.T
        rbr = self.Sq[:, None] * (self.PDq @ b @ self.Tq.T)
        bth = self.Pq_R @ b @ self.Tdq.T
        return bq, rbr, bth

    def c_of_b(self, b, k):
        self.m.k_tail = k
        fl = self.m.fields(b)
        return self.m.psi_xy0(fl).item(), fl

    def cl_of_b(self, b, cl_guess, iters=30, tol=1e-14):
        """self-consistent c_l = (1 + c[b; k = 1/c_l]) / 3 (fixed point; the dependence on k is very weak), fields at the final k."""
        cl = cl_guess
        for _ in range(iters):
            c, fl = self.c_of_b(b, 1.0 / cl)
            cl_new = (1.0 + c) / 3.0
            done = abs(cl_new - cl) < tol * max(1.0, abs(cl)); cl = cl_new
            if done: break
        c, fl = self.c_of_b(b, 1.0 / cl)
        return cl, c, fl

    def residual_q(self, b, cl, fl=None):
        """E on the quadrature grid (Qr, Qth) and the fields."""
        if fl is None:
            self.m.k_tail = 1.0 / cl; fl = self.m.fields(b)
        Ur, Uth, coefU = self.quad_fields(fl['PsiC'])
        bq, rbr, bth = self.bq_fields(b)
        om = self.omq[:, None]
        A0 = cl * om + Ur * om + (3 * cl - 1) + coefU
        E = (cl + Ur) * rbr + Uth * bth + A0 * bq
        return E, dict(Ur=Ur, Uth=Uth, coefU=coefU, bq=bq, rbr=rbr, bth=bth, fl=fl)

    def denominators(self, b, cl, q):
        om = self.omq[:, None]
        X = q['rbr'] + (3 + om) * q['bq']
        den = q['bq'].abs() + X.abs() + (q['Ur'] * X).abs() + (q['Uth'] * q['bth']).abs()
        den = den + self.den_floor * den.max()
        if self.centre_weight:
            # E = O(r^2) near the centre for a smooth (Cartesian-compatible) b with a(0) = 1 and the identity; weight rows by
            # (1 + r^2)/(r^2 + r_c^2) so that the objective sees E/r^2 there (D14 and the compatibility of the centre expansion), capped
            # below r_c = 1e-3 against roundoff amplification; nothing changes for r >> 1
            r2 = (self.rq ** 2)[:, None]
            den = den * ((r2 + 1e-6) / (1.0 + r2))
        return den

    def set_weights(self, b, cl):
        E, q = self.residual_q(b, cl)
        self.wrow = (1.0 / self.denominators(b, cl, q)).reshape(-1)
        return E, q

    def F(self, b, cl, fl=None):
        E, q = self.residual_q(b, cl, fl)
        F = E.reshape(-1) * self.wrow
        if self.extra_rows:
            vals = []
            q['extra'] = []
            for name, wgt in self.extra_rows:
                if name == 'h':
                    hr = h_row(self, b, cl, with_k=True) if self.Lpsi is not None else None
                    if hr is None:
                        self.build_Lpsi(1.0 / cl); hr = h_row(self, b, cl, with_k=True)
                    vals.append(torch.tensor([wgt * hr['H']], device=self.dev)); q['extra'].append((name, wgt, hr))
                elif name == 'cfix':                         # fix c_l: row weight * (c_l(b) - target)
                    vals.append(torch.tensor([wgt * (cl - self.cfix_target)], device=self.dev)); q['extra'].append((name, wgt, cl))
                elif name == 'char':
                    cr = self.char_rows                       # charrows.CharRows object (set by the driver)
                    import charac
                    self.m.k_tail = 1.0 / cl
                    xs = charac.FieldEval(self.m, b, cl).find_P()['x_star']
                    with torch.no_grad():
                        C, inf = cr.values(b, cl, xs, k_tail=1.0 / cl)
                    vals.append(wgt * C); q['extra'].append((name, wgt, dict(x_star=xs, C=C, info=inf)))
            F = torch.cat([F] + vals)
        return F, E, q

    # ------------------------------------------------------------------ linear map b -> PsiC and the Jacobian
    def build_Lpsi(self, k):
        m = self.m; m.k_tail = k
        n_all = self.n_all; dev = self.dev
        nm = m.nf.shape[0]
        self.Lpsi = torch.empty((self.N + 1) * nm, n_all, device=dev)
        self.cvec = torch.empty(n_all, device=dev)
        t0 = time.time()
        for s in range(0, n_all, self.chunk):
            e = min(n_all, s + self.chunk)
            B = torch.zeros(e - s, n_all, device=dev); B[torch.arange(e - s), torch.arange(s, e)] = 1.0
            fl = m.fields(B.reshape(e - s, self.N + 1, self.M))
            self.Lpsi[:, s:e] = fl['PsiC'].reshape(e - s, -1).T
            self.cvec[s:e] = m.psi_xy0(fl)
        self.k_frozen = k
        if self.verbose: print(f"[LSQ] Lpsi built: {(self.N+1)*nm} x {n_all}, k = {k:.8f}, {time.time()-t0:.1f}s", flush=True)

    def jacobian(self, b, cl, q, with_k=True):
        """Weighted Jacobian (Q, n) with respect to the free unknowns b[1:, :] (row-major), c_l eliminated."""
        m = self.m; dev = self.dev; N, M = self.N, self.M
        if self.Lpsi is None or self.k_frozen != 1.0 / cl:        # the map depends on the tail exponent: rebuild whenever k changes (0.5 s at (256,64))
            self.build_Lpsi(1.0 / cl)
        nm = m.nf.shape[0]
        om = self.omq[:, None]
        Ur, Uth, coefU, bq, rbr, bth = q['Ur'], q['Uth'], q['coefU'], q['bq'], q['rbr'], q['bth']
        A0 = cl * om + Ur * om + (3 * cl - 1) + coefU
        X = rbr + om * bq                       # multiplies Ur[delta]
        J = torch.empty(self.Q, self.n, device=dev)
        t0 = time.time()
        for s in range(0, self.n, self.chunk):
            e = min(self.n, s + self.chunk); B = e - s
            cols = torch.arange(M + s, M + e, device=dev)             # indices in the full (N+1)M vector
            D = torch.zeros(B, self.n_all, device=dev); D[torch.arange(B), cols] = 1.0
            D = D.reshape(B, N + 1, M)
            dq, drbr, dbth = self.bq_fields(D)                           # (B, Qr, Qth)
            PsiC = self.Lpsi[:, cols].T.reshape(B, N + 1, nm)
            dUr, dUth, dcoef = self.quad_fields(PsiC)
            dE = (cl + Ur) * drbr + Uth * dbth + A0 * dq + dUr * X + dUth * bth + dcoef * bq
            J[:, s:e] = dE.reshape(B, -1).T
        # c_l terms: d c_l / d b = cvec / 3 ; dE/dc_l at fixed k = rbr + om b + 3 b
        dEdcl = (rbr + om * bq + 3 * bq).reshape(-1)
        factor = 1.0
        if with_k:
            h = 1e-5
            flp = self._fields_k(b, 1.0 / cl + h); flm = self._fields_k(b, 1.0 / cl - h)
            Ep, _ = self.residual_q(b, cl, flp); Em, _ = self.residual_q(b, cl, flm)
            dEdk = ((Ep - Em) / (2 * h)).reshape(-1)
            dEdcl = dEdcl - dEdk / cl ** 2                      # dk/dc_l = -1/c_l^2
            # implicit function: c_l = (1 + c[b; k(c_l)])/3  =>  dc_l/db = (cvec/3) / (1 + (dc/dk)/(3 c_l^2))
            dcdk = (m.psi_xy0(flp) - m.psi_xy0(flm)).item() / (2 * h)
            factor = 1.0 / (1.0 + dcdk / (3.0 * cl ** 2))
            m.k_tail = 1.0 / cl
        self.dcl_db = (self.cvec[M:] / 3.0) * factor
        J.addr_(dEdcl, self.dcl_db)                     # in-place rank-one update (no Q x n temporary: memory at (384,96))
        J *= self.wrow[:, None]
        if self.extra_rows:
            rows = []
            for name, wgt in self.extra_rows:
                if name == 'h':
                    hr = h_row(self, b, cl, with_k=with_k)        # uses self.dcl_db just set
                    rows.append((wgt * hr['grad'])[None, :])
                elif name == 'cfix':
                    rows.append((wgt * self.dcl_db)[None, :])
                elif name == 'char':
                    hr = h_row(self, b, cl, with_k=False)          # for x* and w'(P)
                    C, G, inf = self.char_rows.evaluate(b, cl, hr['x_star'], hr['wP'], self.dcl_db, need_grad=True)
                    rows.append(wgt * G)
            J = torch.cat([J] + rows, 0)
        if self.verbose: print(f"[LSQ] Jacobian {self.Q} x {self.n} built in {time.time()-t0:.1f}s", flush=True)
        return J

    def _fields_k(self, b, k):
        self.m.k_tail = k; return self.m.fields(b)

    def compute_dcl_db(self, b, cl):
        """dc_l/db over the free unknowns (implicit-function factor for the tail exponent included) WITHOUT building the Jacobian."""
        m = self.m; M = self.M
        if self.Lpsi is None or self.k_frozen != 1.0 / cl: self.build_Lpsi(1.0 / cl)
        h = 1e-5
        dcdk = (m.psi_xy0(self._fields_k(b, 1.0 / cl + h)) - m.psi_xy0(self._fields_k(b, 1.0 / cl - h))).item() / (2 * h)
        m.k_tail = 1.0 / cl
        self.dcl_db = (self.cvec[M:] / 3.0) / (1.0 + dcdk / (3.0 * cl ** 2))
        return self.dcl_db

    # ------------------------------------------------------------------ Gauss-Newton / LM
    def solve(self, b, cl, maxit=30, lam=1e-6, tol_step=1e-12, refresh_weights=False, log=None, every=1, svd_at_end=True, rel_stop=1e-4):
        m = self.m; M = self.M
        b = b.clone(); b[0, :] = 1.0
        cl, c, fl = self.cl_of_b(b, cl)
        if self.wrow is None or refresh_weights:
            self.set_weights(b, cl)
        F, E, q = self.F(b, cl, fl)
        Q = self.Q
        def parts(F):   # PDE rms over the Q quadrature rows, and the rms of the extra rows (unweighted by their weight)
            pde = math.sqrt((F[:Q] ** 2).sum().item() / Q)
            ex = ''
            if F.shape[0] > Q and self.extra_rows:
                vals = F[Q:]; ws = []
                for name, wgt in self.extra_rows: ws += [wgt] * (1 if name in ('h', 'cfix') else self.char_rows.K)
                ws = torch.tensor(ws, device=self.dev); ex = f" extra rms(unweighted) {math.sqrt(((vals / ws) ** 2).mean().item()):.3e}"
            return pde, ex
        obj = (F ** 2).sum().item(); hist = [(math.sqrt(obj / self.Q), F.abs().max().item(), cl, lam)]
        if self.verbose:
            pde, ex = parts(F); print(f"[LSQ] it 0: total rms {hist[-1][0]:.3e} PDE rms {pde:.3e}{ex} max {hist[-1][1]:.3e} c_l {cl:.10f}", flush=True)
        info = dict(hist=hist)
        for it in range(1, maxit + 1):
            J = self.jacobian(b, cl, q)
            colnorm = J.norm(dim=0).clamp_min(1e-30)                    # column scaling for the damping (as in LM with D = diag(J^T J))
            if self.step_method == 'qr2':
                # one QR of J per outer iteration (R has the singular values of J); each damping trial then solves the small stacked
                # problem [R; sqrt(lam) D^(1/2)] d = -[Q^T F; 0] through a second (2n x n) QR: (R2^T R2) d = -J^T F with R2 triangular,
                # i.e. the normal equations are never formed; peak memory 2 |J| (torch copies J inside qr)
                Rf = torch.linalg.qr(J, mode='r')[1]; g = J.T @ F
                del J; torch.cuda.empty_cache()                 # J is not needed in the damping loop (memory: (384,96) needs this)
            accepted = False
            for _ in range(16):
                if self.step_method == 'qr2':
                    R2 = torch.linalg.qr(torch.cat([Rf, torch.diag(math.sqrt(lam) * colnorm)], 0), mode='r')[1]
                    d = -torch.linalg.solve_triangular(R2, torch.linalg.solve_triangular(R2.T, g[:, None], upper=False), upper=True)[:, 0]
                elif self.step_method == 'qr':
                    # damped least squares min |J d + F|^2 + lam |D^(1/2) d|^2 solved as one augmented QR problem (no normal equations:
                    # the soft directions, condition number ~1e8..1e9, are lost in J^T J in double precision; astra review lsqpin)
                    Aaug = torch.cat([J, torch.diag(math.sqrt(lam) * colnorm)], 0)
                    rhs = torch.cat([-F, torch.zeros(self.n, device=self.dev)])[:, None]
                    d = torch.linalg.lstsq(Aaug, rhs, driver='gels').solution[:, 0]
                    del Aaug
                else:
                    JtJ = J.T @ J; g = J.T @ F
                    A = JtJ + lam * torch.diag(colnorm ** 2)
                    d = torch.linalg.solve(A, -g)
                bt = b.clone(); bt.reshape(-1)[M:] += d
                clt, ct, flt = self.cl_of_b(bt, cl)
                Ft, Et, qt = self.F(bt, clt, flt)
                objt = (Ft ** 2).sum().item()
                if objt < obj:
                    b, cl, F, E, q, obj = bt, clt, Ft, Et, qt, objt
                    lam = max(lam / 4, 1e-16); accepted = True
                    break
                lam *= 5
            step = d.abs().max().item()
            if self.step_method == 'qr2':
                del Rf, R2, g; torch.cuda.empty_cache()          # free the factors before the next Jacobian (memory at (384,96))
            hist.append((math.sqrt(obj / self.Q), F.abs().max().item(), cl, lam))
            if self.verbose and (it % every == 0 or not accepted):
                pde, ex = parts(F)
                print(f"[LSQ] it {it}: total rms {hist[-1][0]:.3e} PDE rms {pde:.3e}{ex} max {hist[-1][1]:.3e} c_l {cl:.10f} lam {lam:.1e} |step| {step:.2e} accepted {accepted} min b {b[1:].min().item():.4g}", flush=True)
            if log is not None:
                log.write(f"{it} {hist[-1][0]:.6e} {hist[-1][1]:.6e} {cl:.12f} {lam:.3e} {step:.3e} {int(accepted)}\n"); log.flush()
            if not accepted or step < tol_step:
                break
            if it >= 6 and hist[-6][0] > 0 and (hist[-6][0] - hist[-1][0]) / hist[-6][0] < rel_stop:
                if self.verbose: print(f"[LSQ] stop: rms decreased by less than {rel_stop:.0e} relative over 5 iterations", flush=True)
                break
        info.update(cl=cl, obj=obj, rms=hist[-1][0], max=hist[-1][1], E=E, q=q)
        if svd_at_end:
            try:
                J = self.jacobian(b, cl, q)
                Rf = torch.linalg.qr(J, mode='r')[1]
                info.update(self.conditioning(J, F, nvec=4, R=Rf))
                del J, Rf
            except Exception as ex:
                print("[LSQ] singular-value estimate skipped:", ex, flush=True)
        return b, cl, info

    def conditioning(self, J, F, nvec=4, iters=60, R=None):
        """Smallest nvec singular triplets of J from its R factor (J = QR, so J and R share singular values/right vectors):
        block inverse iteration with triangular solves; sigma_j = |J v_j| computed from J itself. Also sigma_max by power iteration.
        Returns dict(sig_min, sig_small (array), sig_max, vmin, dcl_dv (array: dc_l along each small direction), uF (array: u_j . F))."""
        if R is None: R = torch.linalg.qr(J, mode='r')[1]                   # (n, n) upper triangular
        V = torch.randn(self.n, nvec, device=self.dev)
        V, _ = torch.linalg.qr(V)
        for _ in range(iters):
            # right singular vectors of J: inverse iteration with (R^T R)^{-1} = R^{-1} R^{-T}: first R^T y = v, then R x = y
            # (the earlier order R^{-T} R^{-1} = (R R^T)^{-1} was wrong: astra review charpin)
            Y = torch.linalg.solve_triangular(R.T, V, upper=False, left=True)      # R^{-T} V
            Y = torch.linalg.solve_triangular(R, Y, upper=True, left=True)         # R^{-1} R^{-T} V
            V, _ = torch.linalg.qr(Y)
        # Rayleigh-Ritz on the small subspace
        JV = J @ V
        Bm = JV.T @ JV; ev, W = torch.linalg.eigh(Bm)
        V = V @ W; JV = JV @ W
        sig = torch.sqrt(ev.clamp_min(0))
        v = torch.randn(self.n, device=self.dev); v /= v.norm()
        for _ in range(40):
            v = R.T @ (R @ v); v /= v.norm()
        smax = (J @ v).norm().item()
        dcl = (self.dcl_db @ V).cpu().numpy()
        uF = ((JV / sig.clamp_min(1e-300)[None, :]).T @ F).cpu().numpy()
        # cheapest direction for a unit change of c_l: min |J v| s.t. dcl_db . v = 1  ->  v_cl = R^{-1} y / |y|^2, y = R^{-T} dcl_db,
        # cost (residual norm per unit c_l) = 1/|y|; also the first-order c_l shift that the current residual F "asks for": -(u_cl . F)/cost
        y = torch.linalg.solve_triangular(R.T, self.dcl_db[:, None], upper=False)[:, 0]
        cost_cl = 1.0 / y.norm().item()
        v_cl = torch.linalg.solve_triangular(R, y[:, None], upper=True)[:, 0] / (y @ y)
        Jv = J @ v_cl
        out = dict(sig_min=sig[0].item(), sig_small=sig.cpu().numpy(), sig_max=smax, vmin=V[:, 0].cpu().numpy(), dcl_dv=dcl, uF=uF, Vsmall=V.cpu().numpy(),
                   cost_cl=cost_cl, v_cl=v_cl.cpu().numpy(), Jv_cl_norm=Jv.norm().item(), uF_cl=((Jv @ F) / Jv.norm()).item())
        if self.verbose:
            print(f"[LSQ] c_l softness: residual-norm cost per unit c_l change = {cost_cl:.3e} (|F|_2 {F.norm().item():.2e}; a c_l change of 1e-3 costs {cost_cl*1e-3:.2e}); |v_cl| = {v_cl.norm().item():.3e}", flush=True)
        if self.verbose:
            print(f"[LSQ] conditioning (QR): sigma_max {smax:.3e}; smallest singular values {sig.cpu().numpy()}; dc_l per unit norm along them {dcl}; u_j.F {uF} (|F|_2 {F.norm().item():.2e})", flush=True)
        del R
        return out


# ---------------------------------------------------------------------------------------------- axis functionals and the h(P) row
def _axis_rows(ls: 'LSQ', x, cl):
    """Linear functionals (rows over all (N+1)M unknowns, through Lpsi) for U_1(x, 0) and for h(x) - c_l = d_y U_2(x, 0), at a
    single x > 0 on the x-axis.  From charac.FieldEval.uhat at theta = 0:  U_1 = -x v sum_n n Psi_n(x),
    h - c_l = v sum_n n [(kappa - 1) Psi_n(x) + r Psi_n'(x)],  Psi_n = psi_n/(r^2 v) the Lobatto mode functions."""
    m = ls.m; dev = ls.dev; N = ls.N; nm = m.nf.shape[0]
    xt = torch.as_tensor([float(x)], device=dev)
    t = m.rad.t_of_r(xt)
    wL = torch.tensor(ipm1.bary_weights(m.rad.tL_np), device=dev)
    d = t[:, None] - m.rad.tL[None, :]; small = d.abs() < 1e-14; d = torch.where(small, torch.ones_like(d), d)
    Wt = wL[None, :] / d; Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt); P = (Wt / Wt.sum(1, keepdim=True))[0]   # (N+1,)
    PD = P @ m.rad.DL                                    # derivative of the interpolant (in t) at t
    S = (xt / m.rad.drdt(t))[0]
    s2 = xt[0] ** 2 / (m.L ** 2 + xt[0] ** 2); v = (1 + xt[0] ** 2 / m.L ** 2) ** ((m.gamma - 1) / 2); kap = 2 + (m.gamma - 1) * s2
    n = m.nf
    q1 = (P[:, None] * n[None, :]).reshape(-1)                                   # sum_n n Psi_n
    q2 = ((kap - 1) * P[:, None] * n[None, :] + S * PD[:, None] * n[None, :]).reshape(-1)
    row_U1 = -(xt[0] * v) * (q1 @ ls.Lpsi)
    row_h = v * (q2 @ ls.Lpsi)
    return row_U1, row_h


def h_row(ls: 'LSQ', b, cl, x_star=None, with_k=True):
    """H(b) = h(P(b)) - 1 with P = (x*(b), 0) the first zero of W_1(x, 0) = c_l x + U_1(x, 0), and its exact gradient with respect to
    the free unknowns (b rows >= 1), c_l eliminated (dc_l/db = ls.dcl_db, set by ls.jacobian) and the tail exponent k = 1/c_l:
      dH = dh_b + (dh/dc_l) dc_l + h_x dx*,   dx* = -(dW1_b + (x* + dU_1/dc_l) dc_l)/w'(P),
    where dh/dc_l = 1 + (dh/dk)(-1/c_l^2) and dU_1/dc_l = (dU_1/dk)(-1/c_l^2) (finite differences in k).
    Returns dict(H, grad (n,), x_star, wP (= w'(P)), hP, h_x)."""
    import charac
    m = ls.m; M = ls.M; dev = ls.dev
    m.k_tail = 1.0 / cl
    fe = charac.FieldEval(m, b, cl)
    if x_star is None:
        Pi = fe.find_P(); x_star = Pi['x_star']
    xs = torch.tensor([x_star], device=dev)
    def scal(k):
        m.k_tail = k; fe_ = charac.FieldEval(m, b, cl)
        W1, W2, h = fe_.velocity(xs, torch.zeros(1, device=dev)); return W1[0].item() - cl * x_star, h[0].item()
    U1P, hP = scal(1.0 / cl)
    hx = 1e-6 * x_star
    _, hp = scal.__call__(1.0 / cl) if False else (None, None)
    W1p, _, hp = fe.velocity(xs + hx, torch.zeros(1, device=dev)); W1m, _, hm = fe.velocity(xs - hx, torch.zeros(1, device=dev))
    wP = (W1p[0] - W1m[0]).item() / (2 * hx); h_x = (hp[0] - hm[0]).item() / (2 * hx)
    if with_k:
        dk = 1e-5 * (1.0 / cl)
        U1p_, hp_ = scal(1.0 / cl + dk); U1m_, hm_ = scal(1.0 / cl - dk)
        dU1dk = (U1p_ - U1m_) / (2 * dk); dhdk = (hp_ - hm_) / (2 * dk)
    else:
        dU1dk = 0.0; dhdk = 0.0
    m.k_tail = 1.0 / cl
    if ls.Lpsi is None or ls.k_frozen != 1.0 / cl: ls.build_Lpsi(1.0 / cl)
    row_U1, row_h = _axis_rows(ls, x_star, cl)
    dcl = ls.dcl_db                                                  # (n,) over free unknowns
    dW1_b = row_U1[M:]; dh_b = row_h[M:]
    dcl_fac_h = 1.0 - dhdk / cl ** 2; dcl_fac_U1 = -dU1dk / cl ** 2
    dxs = -(dW1_b + (x_star + dcl_fac_U1) * dcl) / wP
    grad = dh_b + dcl_fac_h * dcl + h_x * dxs
    return dict(H=hP - 1.0, grad=grad, x_star=x_star, wP=wP, hP=hP, h_x=h_x, dhdk=dhdk, dU1dk=dU1dk)


def h_row_check(ls: 'LSQ', b, cl, k_list=(0, 7, 1000, 5000), h=1e-6):
    """finite-difference check of the h_row gradient along a few unit directions (full nonlinear recomputation of x*(b))."""
    M = ls.M
    out = h_row(ls, b, cl)
    errs = []
    for k in k_list:
        bp = b.clone(); bp.reshape(-1)[M + k] += h; bm = b.clone(); bm.reshape(-1)[M + k] -= h
        clp, _, _ = ls.cl_of_b(bp, cl); clm, _, _ = ls.cl_of_b(bm, cl)
        Hp = h_row(ls, bp, clp, with_k=False)['H']; Hm = h_row(ls, bm, clm, with_k=False)['H']
        fd = (Hp - Hm) / (2 * h)
        errs.append((k, fd, out['grad'][k].item()))
    return out, errs


def cheapest_cl_cost(ls, J, a, G=None, w=1.0):
    """alpha = min |J v| (or min sqrt(|J v|^2 + w^2 |G v|^2)) subject to a . v = 1, from the QR factor of the (augmented) matrix:
    alpha = 1/|R^{-T} a|.  Also the hard-constraint version min |J v| s.t. a.v = 1, G v = 0 (null-space of G by QR of G^T)."""
    A = J if G is None else torch.cat([J, w * G], 0)
    R = torch.linalg.qr(A, mode='r')[1]
    y = torch.linalg.solve_triangular(R.T, a[:, None], upper=False)[:, 0]
    out = dict(alpha=1.0 / y.norm().item())
    if G is not None:
        # null space of G: Z = Q2[:, Kg:] from the full QR of G^T (n x Kg)
        Qf, _ = torch.linalg.qr(G.T, mode='complete'); Z = Qf[:, G.shape[0]:]
        JZ = J @ Z; aZ = Z.T @ a
        Rz = torch.linalg.qr(JZ, mode='r')[1]
        yz = torch.linalg.solve_triangular(Rz.T, aZ[:, None], upper=False)[:, 0]
        out['alpha_hard'] = 1.0 / yz.norm().item()
        del Qf, Z, JZ, Rz
    del R
    return out
