"""
taylorpatch.py -- local Taylor rows at the x-axis source P (astra charpin remedy (c): an analytic local representation).

Near P = (x*, 0) write xi = x - x*, W_1 = sum u_ab xi^a y^b, W_2 = sum v_ab xi^a y^b (u_00 = v_00 = 0, u_10 = w'(P) =: A_P, v_01 = h(P)),
rho = sum rho_ij xi^i y^j (j odd).  The transport equation W.grad rho = rho gives, for (i, j) != (0, 1),
   (A_P i + h j - 1) rho_ij = -[ sum_{(a,b) != (1,0)} u_ab (i-a+1) rho_{i-a+1, j-b} + sum_{(a,b) != (0,1)} v_ab (j-b+1) rho_{i-a, j-b+1} ],
a triangular recursion in the total degree, with the single free amplitude rho_01 = g(P) = rho_y(P).  (Non-resonant: A_P i + j - 1 != 0
for (i, j) != (0, 1) when h = 1.)  So the smooth solution near P is determined by the jets of W and g(P).
The jets of W at P are obtained by a polynomial least-squares fit of the spectral W_1, W_2 on a disk of radius r_fit around P (W is
smooth and well resolved there), degree K.  Rows: rho_spectral(X_m) - Taylor_K(X_m) = 0 at points X_m on the upper half circle
|X - P| = r_patch (normalised by the local scale g(P) y_m + small).  These rows impose the shape of rho across the characteristic stem
above P, which the PDE rows cannot see (NUM_REPORT 3.16 item 4b).  Everything is differentiable in torch (b, c_l, x* as leaves).
"""
import math, numpy as np, torch
import ipm1


class TaylorPatch:
    def __init__(self, ls, K=8, r_fit=2.0, r_patch=2.0, n_patch=48, n_fit=400, verbose=True):
        self.ls, self.m = ls, ls.m
        self.K, self.r_fit, self.r_patch, self.n_patch, self.verbose = K, r_fit, r_patch, n_patch, verbose
        dev = ls.dev
        self.wbar = torch.tensor(ipm1.bary_weights(self.m.rad.tR_np), device=dev)
        # monomial exponent lists for W (all (a,b) with a+b <= K) and for rho (j odd, i+j <= K)
        self.ab = [(a, b) for d in range(K + 1) for a in range(d + 1) for b in [d - a]]
        self.ij = [(i, j) for d in range(1, K + 1) for i in range(d + 1) for j in [d - i] if j % 2 == 1]
        # fit points: Halton-like scattered points in the disk of radius r_fit (upper half + mirrored by parity below)
        g = torch.Generator().manual_seed(1)
        rr = r_fit * torch.sqrt(torch.rand(n_fit, generator=g)); th = math.pi * torch.rand(n_fit, generator=g)
        self.fit_xi = (rr * torch.cos(th)).to(dev); self.fit_y = (rr * torch.sin(th)).to(dev)
        # patch points on the upper half circle
        thp = (torch.arange(n_patch, dtype=torch.float64) + 0.5) * math.pi / n_patch
        self.p_xi = (r_patch * torch.cos(thp)).to(dev); self.p_y = (r_patch * torch.sin(thp)).to(dev)
        self.Kr = n_patch

    def _interp(self, r):
        m = self.m
        t = m.rad.t_of_r(r)
        d = t[:, None] - m.rad.tR[None, :]
        small = d.abs() < 1e-14
        d = torch.where(small, torch.ones_like(d), d)
        Wt = self.wbar[None, :] / d
        Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt)
        return Wt / Wt.sum(1, keepdim=True), r / m.rad.drdt(t)

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
        m = self.m
        r = torch.sqrt(x ** 2 + y ** 2); th = torch.atan2(y.abs(), x.abs())
        P, _ = self._interp(r)
        Cb = m.ang.to_coef(b, 'EE'); n = m.ang.n['EE']
        bval = ((P @ Cb) * torch.cos(th[:, None] * n[None, :])).sum(1)
        w = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return r ** 3 * w * torch.cos(th) ** 2 * torch.sin(th) * bval * torch.sign(y)

    def gP(self, b, x_star):
        m = self.m
        xs = x_star.reshape(1) if torch.is_tensor(x_star) else torch.tensor([float(x_star)], device=self.ls.dev)
        P, _ = self._interp(xs)
        Cb = m.ang.to_coef(b, 'EE'); b0 = (P @ Cb).sum(1)
        w = (1 + xs ** 2 / m.L ** 2) ** ((m.gamma - 3) / 2)
        return (xs ** 2 * w * b0)[0]

    def monomials(self, xi, y, exps):
        return torch.stack([xi ** a * y ** b for (a, b) in exps], 1)        # (n, len(exps))

    def W_jets(self, cl, x_star, PsiC_R, DPsiC_R):
        """least-squares polynomial fit of W_1, W_2 on the fit disk around P; returns coefficient dicts u, v (tensors indexed by self.ab)."""
        xs = x_star if torch.is_tensor(x_star) else torch.tensor(float(x_star), device=self.ls.dev)
        X = xs + self.fit_xi; Y = self.fit_y
        W1, W2 = self.velocity(X, Y, cl, PsiC_R, DPsiC_R)
        rf = self.r_fit
        Vm = self.monomials(self.fit_xi / rf, self.fit_y / rf, self.ab)       # scaled monomials (unit disk): well conditioned
        # parity: W_1 even in y, W_2 odd in y -> restrict exponents accordingly (zero the others)
        idx1 = [k for k, (a, b) in enumerate(self.ab) if b % 2 == 0]; idx2 = [k for k, (a, b) in enumerate(self.ab) if b % 2 == 1]
        nab = len(self.ab)
        # full-rank least squares on the allowed columns only (lstsq 'gels' needs full rank), via QR (differentiable)
        def lsq(cols, rhs):
            Vc = Vm[:, cols]; Qc, Rc = torch.linalg.qr(Vc)
            x = torch.linalg.solve_triangular(Rc, (Qc.T @ rhs)[:, None], upper=True)[:, 0]
            out = torch.zeros(nab, device=self.ls.dev, dtype=Vm.dtype)
            return out.index_put((torch.tensor(cols, device=self.ls.dev),), x)
        sol1 = lsq(idx1, W1); sol2 = lsq(idx2, W2)
        # residual of the fits (diagnostic), then unscale the coefficients: u_ab = sol_ab / rf^(a+b)
        res1 = (Vm @ sol1 - W1).abs().max(); res2 = (Vm @ sol2 - W2).abs().max()
        scl = torch.tensor([rf ** (a + b) for (a, b) in self.ab], device=self.ls.dev, dtype=Vm.dtype)
        return sol1 / scl, sol2 / scl, res1, res2

    def taylor_rho(self, u, v, gP):
        """recursion for rho_ij (dict over self.ij), differentiable; returns tensor of coefficients ordered as self.ij."""
        idx_ab = {ab: k for k, ab in enumerate(self.ab)}
        A_P = u[idx_ab[(1, 0)]]; h = v[idx_ab[(0, 1)]]
        coef = {}
        coef[(0, 1)] = gP
        for (i, j) in self.ij:
            if (i, j) == (0, 1): continue
            acc = 0.0
            for (a, b), k in idx_ab.items():
                if (a, b) != (1, 0):
                    ii, jj = i - a + 1, j - b
                    if (ii, jj) in coef and ii >= 1: acc = acc + u[k] * ii * coef[(ii, jj)]
                if (a, b) != (0, 1):
                    ii, jj = i - a, j - b + 1
                    if (ii, jj) in coef and jj >= 1: acc = acc + v[k] * jj * coef[(ii, jj)]
            coef[(i, j)] = -acc / (A_P * i + h * j - 1.0)
        return torch.stack([coef[ij] for ij in self.ij])

    def values(self, b, cl, x_star, PsiC_R=None, DPsiC_R=None):
        m = self.m
        if PsiC_R is None:
            fl = m.fields(b); PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        xs = x_star if torch.is_tensor(x_star) else torch.tensor(float(x_star), device=self.ls.dev)
        u, v, res1, res2 = self.W_jets(cl, xs, PsiC_R, DPsiC_R)
        g = self.gP(b, xs)
        rc = self.taylor_rho(u, v, g)
        Vp = self.monomials(self.p_xi, self.p_y, self.ij)
        rho_T = Vp @ rc
        rho_s = self.rho_at(xs + self.p_xi, self.p_y, b)
        scale = (g * self.p_y).abs() + 1e-300
        rows = (rho_s - rho_T) / scale
        return rows, dict(u=u, v=v, g=g, fit_res=(res1, res2), rho_T=rho_T, rho_s=rho_s)

    def evaluate(self, b, cl, x_star, dcl_db, need_grad=True):
        ls, m, M = self.ls, self.m, self.ls.M
        k0 = 1.0 / cl
        bb = b.detach().clone().requires_grad_(True)
        s_t = torch.tensor(float(cl), device=ls.dev, requires_grad=True)
        xs_t = torch.tensor(float(x_star), device=ls.dev, requires_grad=True)
        m.k_tail = k0
        fl = m.fields(bb); PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        rows, inf = self.values(bb, s_t, xs_t, PsiC_R, DPsiC_R)
        info = dict(g=inf['g'].item(), fit_res=(inf['fit_res'][0].item(), inf['fit_res'][1].item()), A_P=inf['u'][[k for k, ab in enumerate(self.ab) if ab == (1, 0)][0]].item(), hP=inf['v'][[k for k, ab in enumerate(self.ab) if ab == (0, 1)][0]].item())
        if not need_grad:
            return rows.detach(), None, info
        K = rows.shape[0]
        eye = torch.eye(K, device=ls.dev)
        gb, gs, gx = torch.autograd.grad(rows, [bb, s_t, xs_t], grad_outputs=eye, is_grads_batched=True, allow_unused=True)
        R_b = gb.reshape(K, -1)[:, M:].clone()
        R_s = torch.zeros(K, device=ls.dev) if gs is None else gs.reshape(K).clone()
        R_x = torch.zeros(K, device=ls.dev) if gx is None else gx.reshape(K).clone()
        bb2 = b.detach().clone().requires_grad_(True)
        fl2 = m.fields(bb2); P2 = fl2['PsiC_R']; D2 = m.rad.DR @ P2
        xsP = torch.tensor([float(x_star)], device=ls.dev)
        W1P, _ = self.velocity(xsP, torch.zeros(1, device=ls.dev), 0.0, P2, D2)
        U_b = torch.autograd.grad(W1P[0], bb2)[0].reshape(-1)[M:]
        with torch.no_grad():
            dk = 1e-5 * k0
            def U1P(k):
                m.k_tail = k; f_ = m.fields(b); Pk = f_['PsiC_R']; return self.velocity(xsP, torch.zeros(1, device=ls.dev), 0.0, Pk, m.rad.DR @ Pk)[0][0].item()
            U_k = (U1P(k0 + dk) - U1P(k0 - dk)) / (2 * dk)
            def vals_k(k):
                m.k_tail = k; f_ = m.fields(b); Pk = f_['PsiC_R']; return self.values(b, cl, x_star, Pk, m.rad.DR @ Pk)[0]
            R_k = (vals_k(k0 + dk) - vals_k(k0 - dk)) / (2 * dk)
            hx = 1e-6 * float(x_star)
            m.k_tail = k0; f_ = m.fields(b); Pk = f_['PsiC_R']; Dk = m.rad.DR @ Pk
            wP = (self.velocity(xsP + hx, torch.zeros(1, device=ls.dev), cl, Pk, Dk)[0][0] - self.velocity(xsP - hx, torch.zeros(1, device=ls.dev), cl, Pk, Dk)[0][0]).item() / (2 * hx)
        m.k_tail = k0
        a = dcl_db
        dxs_db = -(U_b + (float(x_star) - U_k / cl ** 2) * a) / wP
        grads = R_b + R_s[:, None] * a[None, :] + R_x[:, None] * dxs_db[None, :] - (R_k / cl ** 2)[:, None] * a[None, :]
        info['wP'] = wP
        if self.verbose:
            print(f"[patch] K={self.K}, r_fit={self.r_fit}, r_patch={self.r_patch}: W fit residual max {info['fit_res'][0]:.2e}, {info['fit_res'][1]:.2e}; A_P {info['A_P']:.5f} (2c_l-1 {2*cl-1:.5f}), h(P) {info['hP']:.7f}, g(P) {info['g']:.6f}; rows (rho_s - rho_T)/(g y): range {rows.min().item():+.2e}..{rows.max().item():+.2e}, rms {rows.pow(2).mean().sqrt().item():.2e}", flush=True)
        return rows.detach(), grads, info
