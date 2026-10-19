"""
charrows.py -- characteristic-matching rows for the LSQ solver (fixed-W rigidity, SPEC Lemma 4; astra lsqpin remedy (d)).

For target points X_i in the open quadrant, integrate the backward characteristic of W = c_l X + U[b] (RK4, dt) until it enters the
disk |X - P| < delta around the x-axis stagnation point P = (x*, 0); the entry time T_i and entry point X_e,i are interpolated inside
the last step (log-linear in the distance).  Trajectories arrive along the slow manifold (the y direction), so rho(X_e) = g(P) y_e
(1 + O(delta^2)) with g(P) = rho_y(P).  The exact transport relation along the characteristic is rho(X_i) = e^{T_i} rho(X_e,i), so

    C_i(b) = log rho(X_i) - T_i - log(y_e,i) - log g(P)   must vanish for a solution (all i; one common g(P)).

Everything is computed in torch with b as a leaf tensor, so autograd gives the exact gradient of each C_i with respect to b
INCLUDING the motion of the trajectory and of the entry point (c_l = (1 + c[b])/3 is part of the graph with the tail exponent k
frozen; x* is held fixed in the graph and its motion is added by the implicit-function rule dx*/db = -(dW_1(P)/db)/w'(P);
the dependence on k is added by finite differences).
"""
import math, time, numpy as np, torch
import ipm1


class CharRows:
    def __init__(self, ls, targets, delta=1e-4, dt=0.005, tmax=40.0, verbose=True):
        """ls: ipm1lsq.LSQ; targets: (K, 2) array of (x, y) points in the open quadrant."""
        self.ls, self.m = ls, ls.m
        self.X0 = torch.as_tensor(np.asarray(targets, dtype=np.float64), device=ls.dev)
        self.K = self.X0.shape[0]
        self.delta, self.dt, self.tmax, self.verbose = delta, dt, tmax, verbose
        self.wbar = torch.tensor(ipm1.bary_weights(self.m.rad.tR_np), device=ls.dev)

    # ---- differentiable field evaluation (same formulas as charac.FieldEval.uhat, derivative of the interpolant)
    def _interp(self, r):
        m = self.m
        t = m.rad.t_of_r(r)
        d = t[:, None] - m.rad.tR[None, :]
        small = d.abs() < 1e-14
        d = torch.where(small, torch.ones_like(d), d)
        Wt = self.wbar[None, :] / d
        Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt)
        P = Wt / Wt.sum(1, keepdim=True)
        S = r / m.rad.drdt(t)
        return P, S

    def velocity(self, x, y, cl, PsiC_R, DPsiC_R):
        m = self.m
        xa, ya = x.abs(), y.abs()
        r = torch.sqrt(xa ** 2 + ya ** 2); th = torch.atan2(ya, xa)
        P, S = self._interp(r)
        Psi_n = P @ PsiC_R; rPsi_n = S[:, None] * (P @ DPsiC_R)
        nf = m.nf
        sn = torch.sin(th[:, None] * nf[None, :]); cn = torch.cos(th[:, None] * nf[None, :])
        Psi = (Psi_n * sn).sum(1); rPsi_r = (rPsi_n * sn).sum(1); Psi_th = (Psi_n * nf[None, :] * cn).sum(1)
        s2 = r ** 2 / (m.L ** 2 + r ** 2); kap = 2 + (m.gamma - 1) * s2
        G = kap * Psi + rPsi_r
        cs, si = torch.cos(th), torch.sin(th)
        U1h = -(si * G + cs * Psi_th); U2h = cs * G - si * Psi_th
        v = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 1) / 2)
        sx = torch.where(x == 0, torch.ones_like(x), torch.sign(x)); sy = torch.where(y == 0, torch.ones_like(y), torch.sign(y))
        return cl * x + r * v * U1h * sx, cl * y + r * v * U2h * sy

    def rho_at(self, x, y, b):
        """rho(x, y) from the spectral representation of b (differentiable)."""
        m = self.m
        r = torch.sqrt(x ** 2 + y ** 2); th = torch.atan2(y.abs(), x.abs())
        P, _ = self._interp(r)
        Cb = m.ang.to_coef(b, 'EE'); n = m.ang.n['EE']
        bval = ((P @ Cb) * torch.cos(th[:, None] * n[None, :])).sum(1)
        w = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return r ** 3 * w * torch.cos(th) ** 2 * torch.sin(th) * bval * torch.sign(y)

    def gP(self, b, cl, x_star, PsiC_R=None):
        """g(P) = rho_y(x*, 0) = x*^2 w(x*) a(x*, 0) with a = w b: the theta -> 0 limit of rho/(r sin theta) = r^2 w cos^2 b(r, 0)."""
        m = self.m
        xs = x_star.reshape(1) if torch.is_tensor(x_star) else torch.tensor([float(x_star)], device=self.ls.dev)
        P, _ = self._interp(xs)
        Cb = m.ang.to_coef(b, 'EE')
        b0 = (P @ Cb).sum(1)          # cos(0) = 1 for all modes
        w = (1 + xs ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return (xs ** 2 * w * b0)[0]

    def integrate(self, b, cl, x_star, PsiC_R, DPsiC_R):
        """backward RK4 from the targets to the entry disk; returns T (K,), y_e (K,), x_e (K,), ok mask, steps used."""
        dev = self.ls.dev; K = self.K; dt = self.dt; delta = self.delta
        x = self.X0[:, 0].clone(); y = self.X0[:, 1].clone()
        T = torch.zeros(K, device=dev); ye = torch.zeros(K, device=dev); xe = torch.zeros(K, device=dev)
        active = torch.ones(K, dtype=torch.bool, device=dev)
        nsteps = int(self.tmax / dt)
        def rhs(x, y):
            W1, W2 = self.velocity(x, y, cl, PsiC_R, DPsiC_R); return -W1, -W2
        for step in range(nsteps):
            if not bool(active.any()): break
            k1x, k1y = rhs(x, y)
            k2x, k2y = rhs(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
            k3x, k3y = rhs(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
            k4x, k4y = rhs(x + dt * k3x, y + dt * k3y)
            xn = x + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
            yn = (y + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)).clamp_min(1e-300)
            dn = torch.sqrt((xn - x_star) ** 2 + yn ** 2); da = torch.sqrt((x - x_star) ** 2 + y ** 2)
            inside = active & (dn < delta)
            # entry fraction (log-linear in the distance to P) and the entry point / time
            tau = (torch.log(da / delta) / torch.log((da / dn).clamp_min(1 + 1e-15))).clamp(0.0, 1.0)
            y_entry = y * (yn / y) ** tau; x_entry = x_star + (x - x_star) * ((xn - x_star) / (x - x_star)).abs().clamp_min(1e-300) ** tau
            T_entry = T + tau * dt
            ye = torch.where(inside, y_entry, ye); xe = torch.where(inside, x_entry, xe); T = torch.where(inside, T_entry, T)
            active = active & ~inside
            x = torch.where(active, xn, x); y = torch.where(active, yn, y); T = torch.where(active, T + dt, T)
        return T, ye, xe, ~active, step + 1

    def values(self, b, cl, x_star, k_tail=None):
        """C_i for given (b, c_l, x*) with the current graph (b may require grad)."""
        m = self.m
        if k_tail is not None: m.k_tail = k_tail
        fl = m.fields(b)
        PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        T, ye, xe, ok, nst = self.integrate(b, cl, x_star, PsiC_R, DPsiC_R)
        rho0 = self.rho_at(self.X0[:, 0], self.X0[:, 1], b)
        g = self.gP(b, cl, x_star)
        C = torch.log(rho0.clamp_min(1e-300)) - T - torch.log(ye.clamp_min(1e-300)) - torch.log(g.clamp_min(1e-300))
        return C, dict(T=T, ye=ye, xe=xe, ok=ok, nsteps=nst, g=g, rho0=rho0)

    def evaluate(self, b, cl, x_star, wP, dcl_db, need_grad=True):
        """C_i and their gradients (K, n) with respect to the free unknowns b[1:, :].  Chain rule assembled from separate partials
        (astra review charpin): with s = c_l, k = 1/s, a = ds/db (= ls.dcl_db, which includes the implicit factor of the tail exponent),
          DC = C_b + C_s a + C_x dx*/db - C_k a/s^2,   dx*/db = -[U_b + (x* - U_k/s^2) a]/w'(P),
        where C_b, C_s, C_x are autograd partials (b, c_l and x* as independent leaves, k frozen), C_k and U_k (= dU_1(P)/dk) by central
        finite differences in k, U_b the autograd gradient of U_1(P) at fixed k.  Returns (C, grads, info)."""
        ls, m, M = self.ls, self.m, self.ls.M
        t0 = time.time()
        k0 = 1.0 / cl
        bb = b.detach().clone().requires_grad_(True)
        xs_t = torch.tensor(float(x_star), device=ls.dev, requires_grad=True)
        s_t = torch.tensor(float(cl), device=ls.dev, requires_grad=True)
        m.k_tail = k0
        fl = m.fields(bb)
        PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        T, ye, xe, ok, nst = self.integrate(bb, s_t, xs_t, PsiC_R, DPsiC_R)
        rho0 = self.rho_at(self.X0[:, 0], self.X0[:, 1], bb)
        g = self.gP(bb, s_t, xs_t)
        valid = bool(ok.all()) and bool((rho0 > 0).all()) and bool(g > 0)
        C = torch.log(rho0.clamp_min(1e-300)) - T - torch.log(ye.clamp_min(1e-300)) - torch.log(g.clamp_min(1e-300))
        info = dict(T=T.detach(), ye=ye.detach(), xe=xe.detach(), ok=ok, nsteps=nst, g=g.item(), rho0=rho0.detach(), valid=valid)
        if not need_grad:
            return C.detach(), None, info
        K = self.K
        try:        # batched reverse mode over the K rows (vmap over grad_outputs): 5x faster than K sequential passes, identical to 5e-13
            eye = torch.eye(K, device=ls.dev)
            gb, gs, gx = torch.autograd.grad(C, [bb, s_t, xs_t], grad_outputs=eye, is_grads_batched=True, allow_unused=True)
            C_b = gb.reshape(K, -1)[:, M:].clone()
            C_s = torch.zeros(K, device=ls.dev) if gs is None else gs.reshape(K).clone()
            C_x = torch.zeros(K, device=ls.dev) if gx is None else gx.reshape(K).clone()
        except Exception as ex:
            if self.verbose: print("[char] batched autograd failed (" + str(ex)[:80] + "); sequential fallback", flush=True)
            C_b = torch.empty(K, ls.n, device=ls.dev); C_s = torch.empty(K, device=ls.dev); C_x = torch.empty(K, device=ls.dev)
            for i in range(K):
                gb, gs, gx = torch.autograd.grad(C[i], [bb, s_t, xs_t], retain_graph=(i < K - 1), allow_unused=True)
                C_b[i] = gb.reshape(-1)[M:]; C_s[i] = 0.0 if gs is None else gs; C_x[i] = 0.0 if gx is None else gx
        # U_1(P) partials: U_b by autograd at fixed k; U_k by finite differences
        bb2 = b.detach().clone().requires_grad_(True)
        fl2 = m.fields(bb2); PsiC2 = fl2['PsiC_R']; D2 = m.rad.DR @ PsiC2
        xsP = torch.tensor([float(x_star)], device=ls.dev)
        W1P, _ = self.velocity(xsP, torch.zeros(1, device=ls.dev), 0.0, PsiC2, D2)
        U_b = torch.autograd.grad(W1P[0], bb2)[0].reshape(-1)[M:]
        with torch.no_grad():
            dk = 1e-5 * k0
            def U1P_at(k):
                m.k_tail = k; flk = m.fields(b); Pk = flk['PsiC_R']; Dk = m.rad.DR @ Pk
                return self.velocity(xsP, torch.zeros(1, device=ls.dev), 0.0, Pk, Dk)[0][0].item()
            U_k = (U1P_at(k0 + dk) - U1P_at(k0 - dk)) / (2 * dk)
            Cp, _ = self.values(b, cl, x_star, k_tail=k0 + dk); Cm, _ = self.values(b, cl, x_star, k_tail=k0 - dk)
            C_k = (Cp - Cm) / (2 * dk)
        m.k_tail = k0
        a = dcl_db
        dxs_db = -(U_b + (float(x_star) - U_k / cl ** 2) * a) / wP
        grads = C_b + C_s[:, None] * a[None, :] + C_x[:, None] * dxs_db[None, :] - (C_k / cl ** 2)[:, None] * a[None, :]
        info.update(time=time.time() - t0, C_k=C_k, U_k=U_k, C_s=C_s, C_x=C_x)
        if self.verbose:
            print(f"[char] {K} trajectories: steps {nst}, all entered {bool(ok.all())}, valid {valid}, T range {T.min().item():.2f}..{T.max().item():.2f}, g(P) {g.item():.6f}; C range {C.min().item():+.2e}..{C.max().item():+.2e} (mean {C.mean().item():+.2e}, spread {(C.max()-C.min()).item():.2e}); grads in {info['time']:.1f}s", flush=True)
        return C.detach(), grads, info


def default_targets(x_star, R, n_circle=16, r_circles=(20.0, 60.0, 200.0), theta_min_deg=3.0, theta_max_deg=75.0, angles_deg=None):
    """targets on a few circles; angles either n_circle equispaced in [theta_min, theta_max] or an explicit list angles_deg
    (near-axis angles sample the labels that pass the origin saddle (theta -> 90) or leave P along the x-axis (theta -> 0))."""
    pts = []
    angs = np.radians(angles_deg) if angles_deg is not None else np.linspace(math.radians(theta_min_deg), math.radians(theta_max_deg), n_circle)
    for rc in r_circles:
        if rc >= R: continue
        for th in angs:
            pts.append((rc * math.cos(th), rc * math.sin(th)))
    return np.array(pts)
