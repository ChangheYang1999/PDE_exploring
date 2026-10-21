"""
charmap.py -- the Psi-map formulation: rho = C eta_P[W[rho]] on the basin of P (SPEC Lemma 4 / R6), computed by backward
integration of the characteristics of W = c_l X + U from every collocation node to the source P = (x*, 0).

    eta_P(X) = y exp(-I(X)),   I(X) = int_0^inf (btil(X(tau)) - h_P) dtau,   dX/dtau = -W(X),  X(0) = X,   btil = W_2 / y,
    (h_P = btil(P); the integrand b - h_P converges at every iterate, W.grad eta = h_P eta; the row h_P = 1 closes the system)
with the tail beyond the cut-off |X - P| < delta_P added analytically from the linearization at P
(DW(P) = diag(w'(P), h(P)); btil - 1 ~ h'(x*) (x - x*), so I_tail = h'(x*) (x_c - x*)/w'(P)).
Rows: b(q_i, theta_j) - C exp(-I)/(r^2 w cos^2 theta) = 0 at the nodes with r < inf, the collocation row Ehat at q = 1,
h(P) - 1 = 0 and 3 c_l - 1 - psi_xy(0) = 0.  Unknowns: b (i >= 1), c_l, C.
Everything is torch (float64, GPU) and differentiable by forward-mode AD (torch.func.jvp) for Newton-Krylov.
"""
import math, time
import numpy as np
import torch
import ipm_newton as ipn

# Orbit step schedule (2026-10-20T13:00Z). TAU_SWITCH = 7.5: the backward-time step is dt for tau < 7.5 and dt_near after, the
# same schedule for every orbit, so the residual is a smooth function of the unknowns (every orbit is inside the linear region of P by
# tau = 7.5: the step cut check of jac_dense found |F_full - F_cut| = 0 at tau_far = 7.5). TAU_SWITCH = None restores the earlier
# position-dependent switch (dt_near within r_near of P), which made F only piecewise smooth (jumps of 1e-6 to 1e-5 per affected
# row, runs/noise_dnC.json) and corrupted finite-difference Jacobian columns and soft-direction actions.
TAU_SWITCH = 7.5


class Charac:
    def __init__(self, model):
        self.m = model
        self.dev = model.dev
        self.qn = model.qpsi                      # (Npsi+1,) nodes of the mode tables
        self.wq = torch.tensor(model.wqpsi_np, device=self.dev)
        self.nf = model.nf                        # (nmodes,) frequencies nu
        self.L = model.L

    # ---- state preparation ---------------------------------------------------------------------
    def prepare(self, b, cl):
        m = self.m
        g = m.geom(cl)
        fl = m.fields(b, cl, g)
        psit = fl['psit_n']                                            # (Npsi+1, nmodes)
        psitq = fl['psit_nq']
        st = dict(cl=cl, k=1.0 / cl, psit=psit, psitq=psitq, c=fl['c'], g=g, fl=fl)
        return st

    # ---- interpolation of mode tables at arbitrary q --------------------------------------------
    def lagrange(self, q):
        """Barycentric Lagrange weights (P, N+1) for points q (P,)."""
        d = q[:, None] - self.qn[None, :]
        hit = d.abs() < 1e-14
        dsafe = torch.where(hit, torch.ones_like(d), d)
        wd = self.wq[None, :] / dsafe
        wd = torch.where(hit, torch.full_like(wd, 1e300), wd)
        return wd / wd.sum(dim=1, keepdim=True)

    def geom_at(self, r, k):
        u2 = (r / self.L) ** 2
        P1 = 1.0 / (1.0 + u2)
        q = 1.0 - P1 ** ((1.0 - k) / 2.0)
        v = 1.0 - q
        omP1 = u2 * P1
        S = (1.0 - k) * v * omP1
        ov = (k - 1.0) * omP1
        return q, v, S, ov

    def Uhat(self, st, r, th):
        """Uhat_r, Uhat_theta/sin(theta) (regular on the axis) and Uhat_theta at points (r, theta)."""
        q, v, S, ov = self.geom_at(r, st['k'])
        Lg = self.lagrange(q)                                          # (P, N+1)
        ps = Lg @ st['psit']; psq = Lg @ st['psitq']                   # (P, nmodes)
        nt = self.nf[None, :] * th[:, None]
        sn = torch.sin(nt); cs = torch.cos(nt)
        sth = torch.sin(th)
        small = sth.abs() < 1e-13
        sths = torch.where(small, torch.ones_like(sth), sth)
        ratio = torch.where(small[:, None], self.nf[None, :].expand_as(sn), sn / sths[:, None])   # sin(nu th)/sin th
        Ur = -(ps * self.nf[None, :] * cs).sum(1)
        Uth_over_sin = (2.0 + ov) * (ps * ratio).sum(1) + S * (psq * ratio).sum(1)
        Uth = Uth_over_sin * sth
        return Ur, Uth_over_sin, Uth, v

    def Wfield(self, st, X):
        """W_1, W_2, btil = W_2/y at points X (P, 2) with x > 0 (y may be tiny or slightly negative)."""
        x, y = X[:, 0], X[:, 1]
        r = torch.sqrt(x * x + y * y); th = torch.atan2(y, x)
        Ur, Uth_s, Uth, v = self.Uhat(st, r, th)
        cth, sth = torch.cos(th), torch.sin(th)
        U1 = r * v * (Ur * cth - Uth * sth)
        U2 = r * v * (Ur * sth + Uth * cth)
        cl = st['cl']
        W1 = cl * x + U1; W2 = cl * y + U2
        btil = cl + v * (Ur + Uth_s * cth)
        return W1, W2, btil

    def axis(self, st, x):
        """w(x) = W_1(x, 0), h(x) = d_y W_2(x, 0) for tensor x > 0."""
        th = torch.zeros_like(x)
        Ur, Uth_s, Uth, v = self.Uhat(st, x, th)
        w = st['cl'] * x + x * v * Ur
        h = st['cl'] + v * (Ur + Uth_s)
        return w, h

    def find_P(self, st, x0=8.6, iters=30):
        x = torch.as_tensor([x0], device=self.dev, dtype=torch.float64)
        for _ in range(iters):
            w, h = self.axis(st, x)
            dx = 1e-6
            w2, _ = self.axis(st, x + dx)
            wp = (w2 - w) / dx
            x = x - w / wp
        w, h = self.axis(st, x)
        # derivatives at P by central differences (smooth functions of x)
        dx = 1e-5
        wp_, hp_ = self.axis(st, x + dx); wm_, hm_ = self.axis(st, x - dx)
        wprime = (wp_ - wm_) / (2 * dx); hprime = (hp_ - hm_) / (2 * dx)
        return x[0], h[0], wprime[0], hprime[0]

    # ---- backward characteristics ----------------------------------------------------------------
    def integrate(self, st, X0, xstar, hP, dt=0.005, dt_near=0.02, r_near=0.5, tau_max=14.0, verbose=False):
        """Backward RK4 in tau from X0 (P, 2) for a fixed total backward time tau_max per point, with a per-point step: dt while
        |X - P| > r_near, dt_near inside (the flow near P is linear with eigenvalues -A, -1 in tau).  Points that have used
        their time get h = 0.  NOTE (verifier dtsens, 07:40Z): the state-dependent step switch at |X - P| = r_near makes F only
        piecewise smooth in the unknowns (one step of 4h differs from four steps of h by an O(h^5) local error), with jumps of
        that size between the pieces; the analytic tail (linear invariant I + h'(P) zeta / w'(P)) cancels the near-P linear
        integration error, which is why dt_near hardly matters (the research record 07:28Z).
        Returns I (P,), end points, number of loop steps, final distances to P."""
        xs = xstar.reshape(())
        X = X0
        I = torch.zeros(X0.shape[0], device=self.dev, dtype=torch.float64)
        tau = torch.zeros(X0.shape[0], device=self.dev, dtype=torch.float64)

        def rhs(Xc):
            W1, W2, bt = self.Wfield(st, Xc)
            return torch.stack([-W1, -W2], dim=1), bt - hP        # integrand b - h_P: convergent at every iterate (W.grad eta = h_P eta)

        nmax = int(tau_max / dt_near) + int(tau_max / dt) + 10
        nused = 0
        for n in range(nmax):
            remaining = tau_max - tau
            if n % 25 == 0 and bool((remaining <= 0).all()): break
            dist = torch.sqrt((X[:, 0] - xs) ** 2 + X[:, 1] ** 2)
            if TAU_SWITCH is None:
                h = torch.where(dist < r_near, torch.full_like(dist, dt_near), torch.full_like(dist, dt))
            else:
                h = torch.where(tau < TAU_SWITCH - 1e-9, torch.full_like(dist, dt), torch.full_like(dist, dt_near))
            h = torch.clamp(torch.minimum(h, remaining), min=0.0)[:, None]
            k1, f1 = rhs(X)
            k2, f2 = rhs(X + 0.5 * h * k1)
            k3, f3 = rhs(X + 0.5 * h * k2)
            k4, f4 = rhs(X + h * k3)
            X = X + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            I = I + (h[:, 0] / 6.0) * (f1 + 2 * f2 + 2 * f3 + f4)
            tau = tau + h[:, 0]
            nused = n + 1
            if verbose and n % 500 == 0:
                print(f'   step {n}: points with time left {int((remaining > 0).sum())}, max dist {dist.max().item():.3e}', flush=True)
        dist = torch.sqrt((X[:, 0] - xs) ** 2 + X[:, 1] ** 2)
        return I, X, nused, dist

    def psi_map(self, b, cl, C, dt=0.005, dt_near=0.02, tau_max=14.0, verbose=False, far_cut=None, far_psi=False, r_far=1e10):
        """Returns dict with b_psi (N+1, M) [row 0 and q = 1 row filled with b itself], h(P), x*, identity defect, flags."""
        m = self.m
        st = self.prepare(b, cl)
        xstar, hP, wpP, hpP = self.find_P(st)
        N, M = m.N, m.M
        if far_psi:
            P1n = st['g']['P1'][1:N + 1].clone()                        # include the q = 1 node, placed at r_far
            P1n[-1] = 1.0 / (1.0 + (r_far / self.L) ** 2)
            Nrows = N
        else:
            P1n = st['g']['P1'][1:N]                                   # 1/(1+u^2) at the nodes i = 1..N-1 (tensor, depends on c_l)
            Nrows = N - 1
        rr = self.L * torch.sqrt((1.0 - P1n) / P1n)                    # radii of the Psi rows
        th = m.ang.theta
        R, TH = torch.meshgrid(rr, th, indexing='ij')
        X0 = torch.stack([(R * torch.cos(TH)).reshape(-1), (R * torch.sin(TH)).reshape(-1)], dim=1)
        if far_cut is not None:
            sel = (R.reshape(-1) <= far_cut)
            X0s = X0[sel]
        else:
            sel = torch.ones(X0.shape[0], dtype=torch.bool, device=self.dev); X0s = X0
        t0 = time.time()
        I, Xe, nsteps, dist = self.integrate(st, X0s, xstar, hP, dt=dt, dt_near=dt_near, tau_max=tau_max, verbose=verbose)
        bad = dist > 1e-3
        # analytic tail from the linearization at P
        I = I + hpP * (Xe[:, 0] - xstar) / wpP
        if verbose: print(f'   characteristics: {X0s.shape[0]} points, {time.time()-t0:.1f}s, steps {nsteps}, final dist max {dist.max().item():.2e} median {dist.median().item():.2e}', flush=True)
        # b_psi = C exp(-I) / (r^2 w cos^2 theta)
        k = 1.0 / cl
        rs = torch.sqrt(X0s[:, 0] ** 2 + X0s[:, 1] ** 2)
        P1s = 1.0 / (1.0 + (rs / self.L) ** 2)
        ws = P1s ** ((3.0 - k) / 2.0)
        cth2 = (X0s[:, 0] / rs) ** 2
        bpsi_s = C * torch.exp(-I) / (rs ** 2 * ws * cth2)
        bpsi = b.clone()
        full = torch.zeros(X0.shape[0], device=self.dev, dtype=torch.float64)
        full = full.masked_scatter(sel, bpsi_s)
        inner = full.reshape(Nrows, M)
        bpsi = torch.cat([b[:1], torch.where(sel.reshape(Nrows, M), inner, b[1:Nrows + 1]), b[Nrows + 1:]], dim=0)
        return dict(bpsi=bpsi, hP=hP, xstar=xstar, wpP=wpP, hpP=hpP, ident=3.0 * cl - 1.0 - st['c'], bad=bad, nsteps=nsteps,
                    sel=sel.reshape(Nrows, M), I=I, X0=X0s, dist=dist)


    # ---- Newton-Krylov residual --------------------------------------------------------------------
    def unpack(self, z):
        N, M = self.m.N, self.m.M
        b = torch.cat([torch.ones(1, M, device=self.dev, dtype=torch.float64), z[:N * M].reshape(N, M)], dim=0)
        return b, z[N * M], z[N * M + 1]

    def pack(self, b, cl, C):
        return torch.cat([b[1:].reshape(-1), torch.stack([torch.as_tensor(cl, device=self.dev, dtype=torch.float64).reshape(()),
                                                           torch.as_tensor(C, device=self.dev, dtype=torch.float64).reshape(())])])

    def F(self, z, dt=0.005, dt_near=0.02, tau_max=14.0, far_psi=False, r_far=1e10, n_coll=0, coll_scale=1.0):
        """Residual of the Psi formulation: [b - b_psi at i = 1..N-1 (and at q = 1 placed at r_far if far_psi, else Ehat at q = 1) ;
        h(P) - 1 ; identity]."""
        b, cl, C = self.unpack(z)
        out = self.psi_map(b, cl, C, dt=dt, dt_near=dt_near, tau_max=tau_max, far_psi=far_psi, r_far=r_far)
        N = self.m.N
        if far_psi:
            if n_coll > 0:
                # hybrid: collocation rows Ehat at the n_coll innermost radial nodes (they carry b(0) = 1 and the Taylor structure),
                # Psi rows elsewhere
                E, ident = self.m.residual(b, cl)
                rows = torch.cat([coll_scale * E[1:n_coll + 1].reshape(-1), (b - out['bpsi'])[n_coll + 1:N + 1].reshape(-1), (out['hP'] - 1.0).reshape(1), out['ident'].reshape(1)])
            else:
                rows = torch.cat([(b - out['bpsi'])[1:N + 1].reshape(-1), (out['hP'] - 1.0).reshape(1), out['ident'].reshape(1)])
        else:
            E, ident = self.m.residual(b, cl)
            rows = torch.cat([(b - out['bpsi'])[1:N].reshape(-1), E[N].reshape(-1), (out['hP'] - 1.0).reshape(1), ident.reshape(1)])
        return rows


    # ---- variant with c_l eliminated through the identity ---------------------------------------------
    def cl_of_b(self, b, cl0, iters=6):
        """c_l = (1 + psi_xy(0)[b])/3 with the far-field exponent k = 1/c_l made self-consistent (fixed point, unrolled)."""
        cl = cl0
        for _ in range(iters):
            g = self.m.geom(cl); fl = self.m.fields(b, cl, g)
            cl = (1.0 + fl['c']) / 3.0
        return cl

    def unpack2(self, z):
        N, M = self.m.N, self.m.M
        b = torch.cat([torch.ones(1, M, device=self.dev, dtype=torch.float64), z[:N * M].reshape(N, M)], dim=0)
        return b, z[N * M]

    def pack2(self, b, C):
        return torch.cat([b[1:].reshape(-1), torch.as_tensor(C, device=self.dev, dtype=torch.float64).reshape(1)])

    def F2(self, z, cl0, dt=0.005, dt_near=0.02, tau_max=14.0):
        """Residual with c_l eliminated: [b - b_psi at i = 1..N-1 ; Ehat at q = 1 ; h(P) - 1], unknowns (b, C)."""
        b, C = self.unpack2(z)
        cl = self.cl_of_b(b, cl0)
        out = self.psi_map(b, cl, C, dt=dt, dt_near=dt_near, tau_max=tau_max)
        N = self.m.N
        E, ident = self.m.residual(b, cl)
        return torch.cat([(b - out['bpsi'])[1:N].reshape(-1), E[N].reshape(-1), (out['hP'] - 1.0).reshape(1)]), cl


    # ---- vmap-friendly residual (fixed step count, no data-dependent control flow) for batched finite differences --------
    def integrate_fixed(self, st, X0, xstar, hP, dt=0.01, dt_near=0.04, r_near=0.5, tau_max=14.0, nsteps=None):
        xs = xstar.reshape(())
        X = X0
        I = torch.zeros(X0.shape[0], device=self.dev, dtype=torch.float64)
        tau = torch.zeros(X0.shape[0], device=self.dev, dtype=torch.float64)
        if nsteps is None: nsteps = int(tau_max / dt_near) + int(tau_max / dt) + 10
        def rhs(Xc):
            W1, W2, bt = self.Wfield(st, Xc)
            return torch.stack([-W1, -W2], dim=1), bt - hP
        for n in range(nsteps):
            remaining = tau_max - tau
            dist = torch.sqrt((X[:, 0] - xs) ** 2 + X[:, 1] ** 2)
            if TAU_SWITCH is None:
                h = torch.where(dist < r_near, torch.full_like(dist, dt_near), torch.full_like(dist, dt))
            else:
                h = torch.where(tau < TAU_SWITCH - 1e-9, torch.full_like(dist, dt), torch.full_like(dist, dt_near))
            h = torch.clamp(torch.minimum(h, remaining), min=0.0)[:, None]
            k1, f1 = rhs(X); k2, f2 = rhs(X + 0.5 * h * k1); k3, f3 = rhs(X + 0.5 * h * k2); k4, f4 = rhs(X + h * k3)
            X = X + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            I = I + (h[:, 0] / 6.0) * (f1 + 2 * f2 + 2 * f3 + f4)
            tau = tau + h[:, 0]
        return I, X

    def F_fixed(self, z, dt=0.01, dt_near=0.04, tau_max=14.0, r_far=1e10, n_coll=3, coll_scale=0.02, nsteps=None):
        """Hybrid residual (Psi rows at i > n_coll incl. q = 1 at r_far; scaled Ehat rows at i <= n_coll; h(P) - 1; identity),
        written without data-dependent control flow so that torch.func.vmap can batch it over perturbed states."""
        m = self.m; N, M = m.N, m.M
        b, cl, C = self.unpack(z)
        st = self.prepare(b, cl)
        xstar, hP, wpP, hpP = self.find_P(st)
        P1n = st['g']['P1'][1:N + 1]
        P1n = torch.cat([P1n[:-1], torch.full((1,), 1.0 / (1.0 + (r_far / self.L) ** 2), device=self.dev, dtype=torch.float64)])
        rr = self.L * torch.sqrt((1.0 - P1n) / P1n)
        R, TH = torch.meshgrid(rr, m.ang.theta, indexing='ij')
        X0 = torch.stack([(R * torch.cos(TH)).reshape(-1), (R * torch.sin(TH)).reshape(-1)], dim=1)
        I, Xe = self.integrate_fixed(st, X0, xstar, hP, dt=dt, dt_near=dt_near, tau_max=tau_max, nsteps=nsteps)
        I = I + hpP * (Xe[:, 0] - xstar) / wpP
        k = 1.0 / cl
        rs = torch.sqrt(X0[:, 0] ** 2 + X0[:, 1] ** 2)
        P1s = 1.0 / (1.0 + (rs / self.L) ** 2)
        ws = P1s ** ((3.0 - k) / 2.0)
        cth2 = (X0[:, 0] / rs) ** 2
        bpsi = (C * torch.exp(-I) / (rs ** 2 * ws * cth2)).reshape(N, M)
        E, ident = m.residual(b, cl)
        rows = torch.cat([coll_scale * E[1:n_coll + 1].reshape(-1), (b[1:] - bpsi)[n_coll:].reshape(-1), (hP - 1.0).reshape(1), ident.reshape(1)])
        return rows


if __name__ == '__main__':
    import sys
    sys.path.insert(0, './src')
    import run_newton as rn
    N, M, beta = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    model = ipn.Model(N, M, 8.0, device='cuda', beta=beta)
    x = rn.seed_from_x3(model)
    b, cl = model.unpack(x)
    ch = Charac(model)
    st = ch.prepare(b, cl)
    xstar, hP, wpP, hpP = ch.find_P(st)
    print(f'X3 seed on ({N},{M},beta={beta}): c_l {cl.item():.8f}  x* {xstar.item():.7f}  h(P) {hP.item():.9f}  w\'(P) {wpP.item():.6f} (A = {2*cl.item()-1:.6f})  h\'(P) {hpP.item():.5f}')
    # c_l from h(P) = 1 at fixed b (secant)
    c0 = cl.clone(); st0 = ch.prepare(b, c0); _, h0, _, _ = ch.find_P(st0)
    c1 = c0 + 1e-3; st1 = ch.prepare(b, c1); _, h1, _, _ = ch.find_P(st1)
    cH = c0 - (h0 - 1) * (c1 - c0) / (h1 - h0)
    cid = ((1 + st['c']) / 3).item()
    print(f'  dh/dc_l = {((h1-h0)/(c1-c0)).item():.5f};  c_l with h(P) = 1 (fixed density): {cH.item():.8f}  (identity value {cid:.8f})')
    # Psi defect with C = g(P) from the density itself: rho_y(P) = x*^2 w(x*) b(x*, 0)
    r, w, v = model.radii(float(cl)); k = 1 / float(cl)
    gP = float(xstar) ** 2 * (1 + (float(xstar) / 8.0) ** 2) ** ((k - 3) / 2) * model.eval_EE(b, model.q_of_r(np.array([float(xstar)]), float(cl)), np.array([0.0]))[0]
    print(f'  g(P) = rho_y(P) = {gP:.6f}')
    t0 = time.time()
    out = ch.psi_map(b, cl, torch.tensor(gP, device=model.dev), verbose=True)
    print(f'  final distances to P: max {out["dist"].max().item():.2e}')
    print(f'  psi_map {time.time()-t0:.1f}s; not converged: {int(out["bad"].sum())}; identity defect {out["ident"].item():.3e}')
    bp = out['bpsi'].cpu().numpy(); bn = b.cpu().numpy()
    rel = np.abs(bp - bn) / np.abs(bn)
    thd = model.ang.theta_np * 180 / np.pi
    for lo, hi in [(0, 0.5), (0.5, 2), (2, 5), (5, 10), (10, 30), (30, 100), (100, 1e3), (1e3, 1e5), (1e5, 1e300)]:
        selr = (r[1:N] >= lo) & (r[1:N] < hi)
        if selr.any():
            blk = rel[1:N][selr]
            print(f'  Psi defect |b_psi - b|/|b|  r in [{lo:g},{hi:g}): max {blk.max():.3e} rms {np.sqrt((blk**2).mean()):.3e}  (at theta {thd[np.unravel_index(blk.argmax(), blk.shape)[1]]:.1f})')
