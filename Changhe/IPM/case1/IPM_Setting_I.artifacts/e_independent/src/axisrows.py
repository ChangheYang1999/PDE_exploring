"""
axisrows.py -- transport rows ON the invariant axes (1-D characteristic matching, no time integration), for the LSQ solver.

y-axis (invariant line x = 0, flow away from the origin): write rho = x^2 y a(x, y). The x^2 y coefficient of W.grad rho = rho on x = 0
gives, with h2(y) = W_2(0, y)/y = c_l + U_2(0, y)/y and w1(y) = d_x W_1(0, y) = c_l + d_x U_1(0, y),
    d/dy log a(0, y) = f(y) := [1 - h2(y) - 2 w1(y)] / (y h2(y)),      a(0, 0) = 1,
and f(y) -> 0 as y -> 0 exactly because 1 - (c_l + c) - 2 (c_l - c) = -(3 c_l - 1 - c) = 0 (the identity, eliminated exactly in the
solver). Row:  A_y(y_j) = log a(0, y_j) - int_0^{y_j} f(s) ds  (a(0, y) = w(y) b(y, pi/2); should vanish).  These rows tie the far-field
amplitude along the y-axis to the centre normalisation (the softest directions of the PDE Jacobian live there).

x-axis (invariant line y = 0, source P = (x*, 0)): g(x) = rho_y(x, 0) satisfies w g' = (1 - h) g (SPEC Lemma 3), w = W_1(x, 0),
h = d_y W_2(x, 0). Near P, (1 - h)/w = (1 - h(P))/(w'(P) (x - x*)) + regular, so
    log g(x) - log g(P) = int_{x*}^{x} [(1 - h)/w - (1 - h(P))/(w'(P)(s - x*))] ds + ((1 - h(P))/w'(P)) log|x - x*|  (+ const from the cutoff).
For an exact solution h(P) = 1 and the log term vanishes; for a discrete state the term is a smooth g's inability to follow
|x - x*|^((1-h(P))/A), i.e. the rows also act as an h(P) row.  Row:  A_x(x_j) = log g(x_j) - log g(P) - I_reg(x_j) - ((1 - h(P))/w'(P)) log|x_j - x*|,
for x_j on both sides of P (inner segment (x_lo, x*), outer (x*, x_hi)), g(x) = x^2 w(x) b(x, 0) (theta -> 0 limit of rho/(r sin theta)).
All quantities are differentiable functions of b (velocity on the axes from the psi mode functions; stable theta -> 0, pi/2 limits).
Gradients by torch autograd (c_l and x* as separate leaves; chain rule as in charrows.evaluate).
"""
import math, numpy as np, torch
import ipm1


class AxisRows:
    def __init__(self, ls, y_pts, x_pts, n_gl=200, s_min=1e-6, verbose=True):
        self.ls, self.m = ls, ls.m
        self.y_pts = torch.as_tensor(np.asarray(y_pts, dtype=np.float64), device=ls.dev)
        self.x_pts = torch.as_tensor(np.asarray(x_pts, dtype=np.float64), device=ls.dev)
        self.n_gl, self.s_min, self.verbose = n_gl, s_min, verbose
        gl_x, gl_w = np.polynomial.legendre.leggauss(n_gl)
        self.gl_x = torch.tensor(gl_x, device=ls.dev); self.gl_w = torch.tensor(gl_w, device=ls.dev)
        self.wbar = torch.tensor(ipm1.bary_weights(self.m.rad.tR_np), device=ls.dev)
        self.K = len(y_pts) + len(x_pts)

    def _interp(self, r):
        m = self.m
        t = m.rad.t_of_r(r)
        d = t[:, None] - m.rad.tR[None, :]
        small = d.abs() < 1e-14
        d = torch.where(small, torch.ones_like(d), d)
        Wt = self.wbar[None, :] / d
        Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt)
        return Wt / Wt.sum(1, keepdim=True), r / m.rad.drdt(t)

    def axis_modes(self, r, PsiC_R, DPsiC_R):
        """Psi_n(r), r Psi_n'(r), v(r), kappa(r) at radii r (vectorised)."""
        m = self.m
        P, S = self._interp(r)
        Psi_n = P @ PsiC_R; rPsi_n = S[:, None] * (P @ DPsiC_R)
        s2 = r ** 2 / (m.L ** 2 + r ** 2); kap = 2 + (m.gamma - 1) * s2
        v = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 1) / 2)
        return Psi_n, rPsi_n, v, kap

    # ---- x-axis traces (theta = 0): U_1(x,0) = -x v sum n Psi_n ; h - c_l = v sum n [(kappa-1) Psi_n + r Psi_n']
    def x_axis(self, x, cl, PsiC_R, DPsiC_R):
        m = self.m; n = m.nf[None, :]
        Psi_n, rPsi_n, v, kap = self.axis_modes(x, PsiC_R, DPsiC_R)
        W1 = cl * x - x * v * (n * Psi_n).sum(1)
        h = cl + v * (n * ((kap[:, None] - 1) * Psi_n + rPsi_n)).sum(1)
        return W1, h

    # ---- y-axis traces (theta = pi/2): h2 = W_2(0,y)/y = c_l + v sum (-1)^(n/2) n ... derived from U2h/sin at theta = pi/2;
    #      w1 = d_x W_1(0,y) = c_l + v sum (-1)^(n/2) n [(kappa-1) Psi_n + r Psi_n']
    def y_axis(self, y, cl, PsiC_R, DPsiC_R):
        m = self.m; n = m.nf[None, :]; sgn = torch.cos(math.pi * n / 2)        # (-1)^(n/2) for even n
        Psi_n, rPsi_n, v, kap = self.axis_modes(y, PsiC_R, DPsiC_R)
        # U2h = cos G - sin Psi_th; at theta = pi/2: U2h = -Psi_th = -sum n Psi_n cos(n pi/2) = -sum sgn n Psi_n ; U_2/y = v U2h
        h2 = cl - v * (sgn * n * Psi_n).sum(1)
        # U1h = -(sin G + cos Psi_th); U_1/x = v U1h/cos -> -v [G/cos + Psi_th]; G/cos at pi/2: sum (kap Psi_n + rPsi_n) sin(n th)/cos th -> -sum sgn n (...)
        w1 = cl - v * (-(sgn * n * (kap[:, None] * Psi_n + rPsi_n)).sum(1) + (sgn * n * Psi_n).sum(1))
        return h2, w1

    def b_axis(self, r, b, theta):
        """b(r, theta) for theta = 0 or pi/2 from the EE modes (cos 2k theta -> 1 or (-1)^k)."""
        m = self.m
        P, _ = self._interp(r)
        Cb = m.ang.to_coef(b, 'EE'); k = torch.arange(m.M, device=self.ls.dev, dtype=torch.float64)
        fac = torch.ones_like(k) if theta == 0.0 else torch.cos(math.pi * k)
        return (P @ Cb * fac[None, :]).sum(1)

    def values(self, b, cl, x_star, PsiC_R=None, DPsiC_R=None, wP=None, hP=None):
        """A_y (len y_pts) and A_x (len x_pts) rows."""
        m = self.m; dev = self.ls.dev
        if PsiC_R is None:
            fl = m.fields(b); PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        L = m.L; g_ = m.gamma
        # ---- y-axis rows
        ys = self.y_pts
        # quadrature in log s from s_min to y_j: nodes s = exp(u), u in [log s_min, log y_j]
        lo = math.log(self.s_min); hi = torch.log(ys)                       # (Ky,)
        u = 0.5 * (hi[:, None] + lo) + 0.5 * (hi[:, None] - lo) * self.gl_x[None, :]      # (Ky, n_gl)
        wq = 0.5 * (hi[:, None] - lo) * self.gl_w[None, :]
        s = torch.exp(u).reshape(-1)
        h2, w1 = self.y_axis(s, cl, PsiC_R, DPsiC_R)
        f = (1 - h2 - 2 * w1) / (s * h2)
        Iy = ((f * s).reshape(u.shape) * wq).sum(1)                           # int f ds = int f s du
        a0y = ((1 + ys ** 2 / L ** 2) ** ((g_ - 3) / 2)) * self.b_axis(ys, b, math.pi / 2)
        Ay = torch.log(a0y.clamp_min(1e-300)) - Iy
        # ---- x-axis rows
        xs = self.x_pts
        xsP = torch.as_tensor([x_star], device=dev) if not torch.is_tensor(x_star) else x_star.reshape(1)
        if wP is None or hP is None:
            hx = 1e-6 * xsP
            W1p, hp = self.x_axis(xsP + hx, cl, PsiC_R, DPsiC_R); W1m, hm = self.x_axis(xsP - hx, cl, PsiC_R, DPsiC_R)
            wP_ = ((W1p - W1m) / (2 * hx))[0]; W1P, hP_ = self.x_axis(xsP, cl, PsiC_R, DPsiC_R); hP_ = hP_[0]
        else:
            wP_ = torch.as_tensor(wP, device=dev); hP_ = torch.as_tensor(hP, device=dev)
        # regular integrand on [x*, x_j] (or [x_j, x*]) in the variable q = log|s - x*| from log(eps) to log|x_j - x*|
        eps = 1e-6
        d = xs - xsP                                                           # signed distances
        hi = torch.log(d.abs()); lo = math.log(eps)
        u = 0.5 * (hi[:, None] + lo) + 0.5 * (hi[:, None] - lo) * self.gl_x[None, :]
        wq = 0.5 * (hi[:, None] - lo) * self.gl_w[None, :]
        sgn = torch.sign(d)
        s = (xsP + sgn[:, None] * torch.exp(u)).reshape(-1)
        W1, h = self.x_axis(s, cl, PsiC_R, DPsiC_R)
        reg = (1 - h) / W1 - (1 - hP_) / (wP_ * (s - xsP))
        Ix = ((reg.reshape(u.shape) * (sgn[:, None] * torch.exp(u))) * wq).sum(1)        # int reg ds, ds = sgn e^u du
        gx = xs ** 2 * (1 + xs ** 2 / L ** 2) ** ((g_ - 3) / 2) * self.b_axis(xs, b, 0.0)
        gP = xsP ** 2 * (1 + xsP ** 2 / L ** 2) ** ((g_ - 3) / 2) * self.b_axis(xsP, b, 0.0)
        Ax = torch.log(gx.clamp_min(1e-300)) - torch.log(gP.clamp_min(1e-300)) - Ix - ((1 - hP_) / wP_) * torch.log(d.abs())
        return Ay, Ax, dict(hP=hP_, wP=wP_, Iy=Iy, Ix=Ix)

    def evaluate(self, b, cl, x_star, dcl_db, need_grad=True):
        """rows and gradients wrt the free unknowns (chain rule as in charrows.evaluate: b, c_l, x* as leaves; k by FD)."""
        ls, m, M = self.ls, self.m, self.ls.M
        k0 = 1.0 / cl
        bb = b.detach().clone().requires_grad_(True)
        s_t = torch.tensor(float(cl), device=ls.dev, requires_grad=True)
        xs_t = torch.tensor(float(x_star), device=ls.dev, requires_grad=True)
        m.k_tail = k0
        fl = m.fields(bb); PsiC_R = fl['PsiC_R']; DPsiC_R = m.rad.DR @ PsiC_R
        Ay, Ax, inf = self.values(bb, s_t, xs_t, PsiC_R, DPsiC_R)
        Avals = torch.cat([Ay, Ax])
        info = dict(hP=inf['hP'].item(), wP=inf['wP'].item())
        if not need_grad:
            return Avals.detach(), None, info
        K = Avals.shape[0]
        eye = torch.eye(K, device=ls.dev)
        gb, gs, gx = torch.autograd.grad(Avals, [bb, s_t, xs_t], grad_outputs=eye, is_grads_batched=True, allow_unused=True)
        A_b = gb.reshape(K, -1)[:, M:].clone()
        A_s = torch.zeros(K, device=ls.dev) if gs is None else gs.reshape(K).clone()
        A_x = torch.zeros(K, device=ls.dev) if gx is None else gx.reshape(K).clone()
        # motion of x*: W_1(x*, 0) = 0; U_b by autograd, U_k by FD
        bb2 = b.detach().clone().requires_grad_(True)
        fl2 = m.fields(bb2); P2 = fl2['PsiC_R']; D2 = m.rad.DR @ P2
        xsP = torch.tensor([float(x_star)], device=ls.dev)
        W1P, _ = self.x_axis(xsP, 0.0, P2, D2)
        U_b = torch.autograd.grad(W1P[0], bb2)[0].reshape(-1)[M:]
        with torch.no_grad():
            dk = 1e-5 * k0
            def U1P(k):
                m.k_tail = k; f_ = m.fields(b); Pk = f_['PsiC_R']; return self.x_axis(xsP, 0.0, Pk, m.rad.DR @ Pk)[0][0].item()
            U_k = (U1P(k0 + dk) - U1P(k0 - dk)) / (2 * dk)
            def vals_k(k):
                m.k_tail = k; f_ = m.fields(b); Pk = f_['PsiC_R']; Ayk, Axk, _ = self.values(b, cl, x_star, Pk, m.rad.DR @ Pk); return torch.cat([Ayk, Axk])
            A_k = (vals_k(k0 + dk) - vals_k(k0 - dk)) / (2 * dk)
        m.k_tail = k0
        a = dcl_db
        wP = info['wP']
        dxs_db = -(U_b + (float(x_star) - U_k / cl ** 2) * a) / wP
        grads = A_b + A_s[:, None] * a[None, :] + A_x[:, None] * dxs_db[None, :] - (A_k / cl ** 2)[:, None] * a[None, :]
        if self.verbose:
            print(f"[axis] {len(self.y_pts)} y-axis rows: A_y range {Ay.min().item():+.2e}..{Ay.max().item():+.2e}; {len(self.x_pts)} x-axis rows: A_x range {Ax.min().item():+.2e}..{Ax.max().item():+.2e}; h(P)-1 {info['hP']-1:+.3e}, w'(P) {wP:.5f}", flush=True)
        return Avals.detach(), grads, info


def default_axis_points(x_star, R, ny=24, nx_out=12, nx_in=8):
    y = np.exp(np.linspace(np.log(0.05), np.log(0.5 * R), ny))
    x_out = x_star + np.exp(np.linspace(np.log(0.5), np.log(0.5 * R - x_star), nx_out))
    x_in = x_star - np.exp(np.linspace(np.log(0.5), np.log(0.9 * x_star), nx_in))
    return y, np.concatenate([x_in[::-1], x_out])
