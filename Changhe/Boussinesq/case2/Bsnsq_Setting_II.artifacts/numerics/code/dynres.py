"""Dynamic rescaling (pseudo-time) solver for Setting A2. Third, independent method.

Rescaled dynamics (pseudo-time s; stationary states are profiles of (P) with beta = c_l / c_w):
  d_s Omega + (c_l X + U) . grad Omega + c_w Omega = Theta_x,
  d_s Theta + (c_l X + U) . grad Theta = (c_l - 2 c_w) Theta,
  U from Omega by the canonical modal Green inverse (a2core_t.A2ModelT), U = o(|X|).
Desingularized fields Theta = x^2 y a, Omega = x y G, transported in the normalized form
  A = a / t^{e_a},  B = G / t^{e_G}   (t = (1 + r^2/L^2)^{-1/(2 beta_map)}, so A, B = O(1) for a natural-tail state):
  d_s A + W . grad A = lamA A,   lamA = c_l - 2 c_w - 2 w1 - w2 - W_r d_r log t^{e_a},
  d_s B + W . grad B = lamB B + S, lamB = -(w1 + w2 + c_w) - W_r d_r log t^{e_G},  S = (2 a + x a_x) / t^{e_G},
  w1 = c_l + U1/x, w2 = c_l + U2/y, W_r = c_l r + U_r.
Semi-Lagrangian step: backward RK4 characteristics over ds with the velocity frozen at time s; exponent integrals and the
source integral by Simpson (end points and a cubic-Hermite midpoint). Values at arbitrary points come from the spectral
representation itself (no interpolation of a, G); the velocity modes h_k, h_k' are Chebyshev-interpolated in eta from a
fine (Nf) radial grid where the exact Green quadrature is evaluated. Coefficients are recovered on the square
collocation grid by an angular inverse DCT and per-mode SVD-truncated pseudo-inverses (modes l >= 1 vanish like
rho^{2l} at the origin and are invisible on the innermost nodes).
Normalizations (two scalings: space and time):
  mode 'a0'   : c_w = 1 and c_l(s) = (c(s) - 2 c_w)/2 with c = Psi_xy(0) from the inverse. Then d_s a(0) = 0 exactly
                for the continuous equations (the x^2 y jet identity), so a_0 stays 1 and beta := c_l(s) is an OUTPUT.
  mode 'fixed': c_l = beta_map, c_w = 1 (profile equations at fixed beta); a_0 drifts at rate c - 2 beta - 2 and the
                state is rescaled in space (an exact symmetry) whenever |a_0 - 1| exceeds a tolerance.
The G(0) jet identity (2 c_l + 1) G_0 = 2 a_0 is NOT imposed: it is approached dynamically (rate 2 c_l + 1).
"""
import sys, time, json, math, argparse
import numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT, cheb_gauss_nodes, cheb_T
from a2core_t import A2ModelT
from lm_solve import LMProblem, load_state, save_state, problem_from_state, initial_guess, dev


def chebT_torch(eta, n):
    eta = torch.clamp(eta, -1.0, 1.0)
    phi = torch.arccos(eta)
    nn = torch.arange(n, dtype=eta.dtype, device=eta.device)
    return torch.cos(phi[:, None] * nn[None, :])


def chebT_deriv_torch(eta, n):
    eta_c = torch.clamp(eta, -1.0 + 1e-13, 1.0 - 1e-13)
    phi = torch.arccos(eta_c); s = torch.sin(phi)
    nn = torch.arange(n, dtype=eta.dtype, device=eta.device)
    return nn[None, :] * torch.sin(phi[:, None] * nn[None, :]) / s[:, None]


class DynRes:
    def __init__(self, N, M, L, beta_map, sigma_a=None, sigma_G=None, ov=2.0, c_w=1.0, mode='a0', pinv_tol=1e-10,
                 filt=None):
        self.N, self.M, self.L, self.beta_map = N, M, float(L), float(beta_map)
        b = self.beta_map
        self.sigma_a = (1.0 + 1.0 / b) if sigma_a is None else float(sigma_a)
        self.sigma_G = (1.0 + 1.0 / (2 * b)) if sigma_G is None else float(sigma_G)
        self.ov = ov
        self.Ne, self.Me = int(round(ov * N)), int(round(ov * M))
        self.eta_e = cheb_gauss_nodes(self.Ne); self.th_e = (np.arange(self.Me) + 0.5) * np.pi / (2 * self.Me)
        # one model on the over-collocated grid: transport grid, exact Green quadrature (velocity interpolation source)
        self.mg = A2ModelT(N, M, L, b, self.sigma_a, self.sigma_G, device=dev, eta_eval=self.eta_e, th_eval=self.th_e)
        self.Nf = self.Ne
        self.mu, self.e_a, self.e_G = self.mg.mu, self.mg.e_a, self.mg.e_G
        self.c_w, self.mode, self.filt = float(c_w), mode, filt
        m = self.mg
        self.Cpinv = torch.linalg.pinv(m.C)                     # [M, Me] angular least squares
        self.Tf = torch.tensor(cheb_T(self.eta_e, self.Nf), dtype=DT, device=dev)
        self.Tfinv = torch.linalg.inv(self.Tf)                  # [Nf, Nf] square interpolation of the velocity modes
        rf = torch.tensor(m.r, dtype=DT, device=dev); tf = torch.tensor(m.t, dtype=DT, device=dev)
        self.normH = rf ** 2 * tf ** self.mu; self.normD = rf * tf ** self.mu
        # per-mode truncated least-squares pseudo-inverses on the 2N grid: A_l(eta_e) = rho2(eta_e)^l q_l(eta_e)
        rho2 = 1 - tf ** (2 * b)
        self.rho2 = rho2
        self.pinvs = []; self.ranks = []
        for l in range(M):
            Bm = (rho2 ** l)[:, None] * m.T                     # [Ne, N]
            U_, S_, Vh = torch.linalg.svd(Bm, full_matrices=False)
            keep = S_ > pinv_tol * S_[0]
            self.pinvs.append(Vh[keep].T @ torch.diag(1.0 / S_[keep]) @ U_[:, keep].T)
            self.ranks.append(int(keep.sum()))
        # constrained least squares for mode 0: min |B0 c - v| s.t. c . e = target (e = T_n(1)); KKT solution
        B0 = m.T; self.e0 = m.origin_T
        BtB = B0.T @ B0; K = torch.zeros((N + 1, N + 1), dtype=DT, device=dev)
        K[:N, :N] = BtB; K[:N, N] = self.e0; K[N, :N] = self.e0
        self.K0inv = torch.linalg.inv(K); self.B0t = B0.T
        self.pin_a0 = None; self.pin_G0 = None
        # grid in Cartesian form
        r = rf; th = torch.tensor(m.th, dtype=DT, device=dev)
        self.rg, self.thg = r, th
        R, TH = torch.meshgrid(r, th, indexing='ij')
        self.Xg = (R * torch.cos(TH)).reshape(-1); self.Yg = (R * torch.sin(TH)).reshape(-1)
        self.P0a_g = (tf ** self.e_a)[:, None]
        self.P0G_g = (tf ** self.e_G)[:, None]
        self.l = torch.arange(M, dtype=DT, device=dev)
        self.kk = 2 * (self.l + 1)
        if filt is not None:
            alpha, p = filt
            n = torch.arange(N, dtype=DT, device=dev); lf = torch.arange(M, dtype=DT, device=dev)
            self.filt_r = torch.exp(-alpha * ((n + 1) / N) ** (2 * p))[None, :]
            self.filt_a = torch.exp(-alpha * ((lf + 1) / M) ** (2 * p))[:, None]

    # ---------- state ----------
    def set_state(self, ca, cG, c_l=None):
        self.ca, self.cG = ca, cG
        ff = self.mg.fields(ca, cG, self.beta_map)
        self.a0 = float(ff['a0']); self.G0 = float(ff['G0'])
        if getattr(self, 'freeze', False) and hasattr(self, 'coefH'):
            return
        self.c = float(ff['c'])
        if c_l is None:
            c_l = (self.c - 2 * self.c_w) / 2 if self.mode == 'a0' else self.beta_map
        self.c_l = float(c_l)
        self.coefH = (ff['h'] / self.normH[None, :]) @ self.Tfinv.T     # [M, Nf]
        self.coefD = (ff['hd'] / self.normD[None, :]) @ self.Tfinv.T

    def coeffs_from_grid(self, A, B):
        """A, B: normalized nodal values [Ne, Me] -> Chebyshev-Fourier coefficients ca, cG [M, N] (least squares)."""
        out = []
        for V, pin in ((A, self.pin_a0), (B, self.pin_G0)):
            Vl = (V @ self.Cpinv.T).T                    # [M, Ne] angular modes at the radial nodes
            c = torch.stack([self.pinvs[l] @ Vl[l] for l in range(self.M)])
            if pin is not None:                           # pinned origin value for the l = 0 mode (KKT)
                rhs = torch.cat([self.B0t @ Vl[0], torch.tensor([pin], dtype=DT, device=dev)])
                c0 = (self.K0inv @ rhs)[:self.N]
                c = torch.cat([c0[None, :], c[1:]], 0)
            if self.filt is not None:
                c = c * self.filt_r * self.filt_a
            out.append(c)
        return out[0], out[1]

    # ---------- evaluation at arbitrary points ----------
    def eval_pts(self, x, y, need_fields=True):
        b, L, N, M = self.beta_map, self.L, self.N, self.M
        r = torch.sqrt(x * x + y * y); th = torch.atan2(y, x)
        t = (1 + (r / L) ** 2) ** (-1 / (2 * b)); eta = 2 * t - 1
        cth, sth = torch.cos(th), torch.sin(th)
        rho2 = 1 - t ** (2 * b)
        Tfp = chebT_torch(eta, self.Nf)
        h = (Tfp @ self.coefH.T) * (r ** 2 * t ** self.mu)[:, None]      # [P, M] modes k = 2(l+1)
        hd = (Tfp @ self.coefD.T) * (r * t ** self.mu)[:, None]
        kth = th[:, None] * self.kk[None, :]
        Psi_r = (hd * torch.sin(kth)).sum(1); Psi_th = (h * self.kk[None, :] * torch.cos(kth)).sum(1)
        U1 = -(sth * Psi_r + cth * Psi_th / r); U2 = cth * Psi_r - sth * Psi_th / r; U_r = -Psi_th / r
        c_l = self.c_l
        W1 = c_l * x + U1; W2 = c_l * y + U2
        out = dict(W1=W1, W2=W2, U1=U1, U2=U2, r=r, t=t)
        if not need_fields:
            return out
        w1 = c_l + U1 / x; w2 = c_l + U2 / y
        W_r = c_l * r + U_r
        dlogt_dr = -r * t ** (2 * b) / (b * L ** 2)
        TN = chebT_torch(eta, N); dTN = chebT_deriv_torch(eta, N)
        Qa = TN @ self.ca.T; dQa = dTN @ self.ca.T; QG = TN @ self.cG.T; dQG = dTN @ self.cG.T   # [P, M]
        rho2l = rho2[:, None] ** self.l[None, :]
        dlogrho = -2 * b * self.l[None, :] * (t ** (2 * b - 1))[:, None] / rho2[:, None]      # d/dt log rho2^l
        c2 = torch.cos(2 * th[:, None] * self.l[None, :]); s2 = torch.sin(2 * th[:, None] * self.l[None, :])
        Al = rho2l * Qa; Bl = rho2l * QG
        A = (Al * c2).sum(1); B = (Bl * c2).sum(1)
        P0a = t ** self.e_a; P0G = t ** self.e_G
        a = A * P0a; G = B * P0G
        # a_eta: d/deta = (1/2) d/dt; a_l = t^{e_a} rho2^l q_l
        dlogPa_deta = 0.5 * (dlogrho + self.e_a / t[:, None])
        al_eta = (P0a[:, None] * rho2l) * (dlogPa_deta * Qa + dQa)
        a_eta = (al_eta * c2).sum(1); a_th = (P0a[:, None] * Al * (-2 * self.l[None, :]) * s2).sum(1)
        detadr = -2 * r * t ** (2 * b + 1) / (b * L ** 2)
        a_r = a_eta * detadr
        a_x = cth * a_r - sth * a_th / r
        lamA = (c_l - 2 * self.c_w - 2 * w1 - w2) - W_r * self.e_a * dlogt_dr
        lamB = -(w1 + w2 + self.c_w) - W_r * self.e_G * dlogt_dr
        S = (2 * a + x * a_x) / P0G
        out.update(A=A, B=B, a=a, G=G, a_x=a_x, w1=w1, w2=w2, lamA=lamA, lamB=lamB, S=S)
        return out

    # ---------- one semi-Lagrangian step ----------
    def step(self, ds):
        X, Y = self.Xg, self.Yg
        fi = self.eval_pts(X, Y)
        k1x, k1y = -fi['W1'], -fi['W2']
        o = self.eval_pts(X + 0.5 * ds * k1x, Y + 0.5 * ds * k1y, need_fields=False); k2x, k2y = -o['W1'], -o['W2']
        o = self.eval_pts(X + 0.5 * ds * k2x, Y + 0.5 * ds * k2y, need_fields=False); k3x, k3y = -o['W1'], -o['W2']
        o = self.eval_pts(X + ds * k3x, Y + ds * k3y, need_fields=False); k4x, k4y = -o['W1'], -o['W2']
        Xf = X + ds * (k1x + 2 * k2x + 2 * k3x + k4x) / 6; Yf = Y + ds * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        # keep feet in the open quadrant (parity: reflect)
        Xf = Xf.abs(); Yf = Yf.abs()
        ff = self.eval_pts(Xf, Yf)
        kfx, kfy = -ff['W1'], -ff['W2']
        # cubic Hermite midpoint of the backward path (sigma from 0 at X to ds at Xf)
        Xm = 0.5 * (X + Xf) + 0.125 * ds * (k1x - kfx); Ym = 0.5 * (Y + Yf) + 0.125 * ds * (k1y - kfy)
        Xm = Xm.abs(); Ym = Ym.abs()
        fm = self.eval_pts(Xm, Ym)
        # exponent integrals along the path from the foot (sigma = ds) back to the grid point (sigma = 0)
        LamA = ds / 6 * (ff['lamA'] + 4 * fm['lamA'] + fi['lamA'])
        LamB = ds / 6 * (ff['lamB'] + 4 * fm['lamB'] + fi['lamB'])
        LamB_mid = ds / 4 * (fm['lamB'] + fi['lamB'])          # from midpoint to the grid point
        A_new = ff['A'] * torch.exp(LamA)
        I_src = ds / 6 * (torch.exp(LamB) * ff['S'] + 4 * torch.exp(LamB_mid) * fm['S'] + fi['S'])
        B_new = ff['B'] * torch.exp(LamB) + I_src
        Ne, Me = self.Ne, self.Me
        dA = (A_new - fi['A']).reshape(Ne, Me); dB = (B_new - fi['B']).reshape(Ne, Me)
        ca, cG = self.coeffs_from_grid(A_new.reshape(Ne, Me), B_new.reshape(Ne, Me))
        return ca, cG, dA, dB, fi

    def rescale_a0(self):
        """Spatial rescaling X -> lam X with lam = sqrt(a0) so that a(0) -> 1 (exact symmetry of the stationary problem)."""
        lam = math.sqrt(abs(self.a0))
        f = self.eval_pts(self.Xg / lam, self.Yg / lam)
        A = (f['a'] / lam ** 2 / self.P0a_g.reshape(-1).repeat_interleave(self.Me)).reshape(self.Ne, self.Me)
        B = (f['G'] / lam ** 2 / self.P0G_g.reshape(-1).repeat_interleave(self.Me)).reshape(self.Ne, self.Me)
        ca, cG = self.coeffs_from_grid(A, B)
        self.set_state(ca, cG, None if self.mode == 'a0' else self.beta_map)
        return lam

    # ---------- diagnostics ----------
    def axis_zeros(self, rmin=0.05, rmax=3000.0, n=400):
        rr = torch.tensor(np.geomspace(rmin, rmax, n), dtype=DT, device=dev)
        eps = torch.full_like(rr, 1e-9)
        fx = self.eval_pts(rr, eps); fy = self.eval_pts(eps, rr)
        w1 = fx['w1'].cpu().numpy(); w2 = fy['w2'].cpu().numpy(); r = rr.cpu().numpy()
        def zeros(v):
            idx = np.where(np.diff(np.sign(v)) != 0)[0]
            lr = np.log(r)
            return [float(np.exp(lr[i] + (lr[i + 1] - lr[i]) * v[i] / (v[i] - v[i + 1]))) for i in idx]
        zx, zy = zeros(w1), zeros(w2)
        lam = float('nan')
        if zx:
            x0 = zx[0]; h = 1e-5 * x0
            o = self.eval_pts(torch.tensor([x0 + h, x0 - h], dtype=DT, device=dev), torch.tensor([1e-9, 1e-9], dtype=DT, device=dev))
            lam = float((o['W1'][0] - o['W1'][1]) / (2 * h))
        return zx, zy, lam, float(w2.min())

    def tails(self):
        ca, cG = self.ca, self.cG
        return dict(a_rtail=float(ca[:, -2:].abs().max() / ca.abs().max()), a_atail=float(ca[-2:].abs().max() / ca.abs().max()),
                    G_rtail=float(cG[:, -2:].abs().max() / cG.abs().max()), G_atail=float(cG[-2:].abs().max() / cG.abs().max()))


def lm_residual(prob, ca, cG, beta):
    z = prob.pack(ca, cG, beta)
    d = prob.diagnostics(z)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', type=str, default=None)
    ap.add_argument('--N', type=int, default=None); ap.add_argument('--M', type=int, default=None)
    ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--beta', type=float, default=2.0, help='map beta (and c_l in fixed mode)')
    ap.add_argument('--kind', type=str, default='gauss'); ap.add_argument('--RG', type=float, default=None)
    ap.add_argument('--ds', type=float, default=0.02); ap.add_argument('--nsteps', type=int, default=1000)
    ap.add_argument('--mode', type=str, default='a0'); ap.add_argument('--c_w', type=float, default=1.0)
    ap.add_argument('--ov', type=float, default=2.0); ap.add_argument('--filt', type=float, nargs=2, default=None)
    ap.add_argument('--pinv_tol', type=float, default=1e-10)
    ap.add_argument('--diag_every', type=int, default=25); ap.add_argument('--save_every', type=int, default=100)
    ap.add_argument('--rescale_tol', type=float, default=1e-2)
    ap.add_argument('--name', type=str, default='dyn'); ap.add_argument('--test', action='store_true')
    ap.add_argument('--Rw', type=float, default=30.0)
    ap.add_argument('--freeze_vel', action='store_true', help='keep the initial velocity and c_l fixed (linear transport test)')
    ap.add_argument('--pin_a0', action='store_true', help='pin a(0) = 1 in the l=0 least-squares fit (exact invariant in mode a0)')
    args = ap.parse_args()
    log = open(f'runs/{args.name}.log', 'a')
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n'); log.flush()
    P(f"# {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} dynres args: {vars(args)}")
    if args.init:
        d = load_state(args.init)
        N = args.N or int(d['N']); M = args.M or int(d['M']); L = float(d['L']) if args.N is None else args.L
        beta_map = args.beta
        sa, sG = float(d['sigma_a']), float(d['sigma_G'])
        if abs(float(d['beta_map']) - beta_map) > 1e-12:
            sa = sG = None       # new map: default sigmas of the new beta
        dyn = DynRes(N, M, L, beta_map, sa, sG, ov=args.ov, c_w=args.c_w, mode=args.mode, pinv_tol=args.pinv_tol, filt=tuple(args.filt) if args.filt else None)
        prob = LMProblem(N, M, L, beta_map, dyn.sigma_a, dyn.sigma_G, 1.0, 30.0, None, ov=args.ov, mapname='t', Rw=args.Rw)
        if int(d['N']) == N and int(d['M']) == M and abs(float(d['L']) - L) < 1e-12 and abs(float(d['beta_map']) - beta_map) < 1e-12:
            ca = torch.tensor(d['ca'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
        else:
            from lm_solve import refit
            prob_old, z_old = problem_from_state(d)
            z = refit(prob_old, z_old, prob, beta_map)
            ca, cG, _ = prob.unpack(z)
    else:
        N, M, L, beta_map = args.N or 64, args.M or 16, args.L, args.beta
        dyn = DynRes(N, M, L, beta_map, None, None, ov=args.ov, c_w=args.c_w, mode=args.mode, pinv_tol=args.pinv_tol, filt=tuple(args.filt) if args.filt else None)
        prob = LMProblem(N, M, L, beta_map, dyn.sigma_a, dyn.sigma_G, 1.0, 30.0, None, ov=args.ov, mapname='t', Rw=args.Rw)
        z = initial_guess(prob, beta_map, RG=args.RG, kind=args.kind)
        ca, cG, _ = prob.unpack(z)
    P(f"grid N={N} M={M} L={L} beta_map={beta_map} Ne={dyn.Ne} Me={dyn.Me} ranks(min/max)={min(dyn.ranks)}/{max(dyn.ranks)} mode={args.mode} c_w={args.c_w}")
    dyn.set_state(ca, cG)
    dyn.freeze = args.freeze_vel
    if args.pin_a0: dyn.pin_a0 = 1.0
    P(f"initial: c={dyn.c:.6f} c_l={dyn.c_l:.6f} a0={dyn.a0:.6f} G0={dyn.G0:.6f}")
    if args.test:
        # (1) evaluation at the collocation grid vs the exact model
        f_ex = dyn.mg.fields(ca, cG, dyn.c_l)
        f = dyn.eval_pts(dyn.Xg, dyn.Yg)
        for nm in ('a', 'G', 'a_x', 'U1', 'U2', 'w1', 'w2'):
            ex = f_ex[nm].reshape(-1); ap_ = f[nm]
            P(f"  test eval {nm:3s}: max|diff|={float((ex - ap_).abs().max()):.3e}  max|exact|={float(ex.abs().max()):.3e}")
        # (2) one small step vs the LM residual: d_s A = -Ra / t^{e_a}, d_s B = -RG / t^{e_G}
        for ds in (1e-3, 2e-3):
            ca1, cG1, dA, dB, fi = dyn.step(ds)
            dA_pred = -(f_ex['Ra'] / dyn.P0a_g); dB_pred = -(f_ex['RG'] / dyn.P0G_g)
            ea = (dA / ds - dA_pred); eb = (dB / ds - dB_pred)
            P(f"  test step ds={ds}: |dA/ds + Ra/P0|max={float(ea.abs().max()):.3e} (|Ra/P0|max={float(dA_pred.abs().max()):.3e}); "
              f"|dB/ds + RG/P0|max={float(eb.abs().max()):.3e} (|RG/P0|max={float(dB_pred.abs().max()):.3e})")
            # projection error: values recovered from unchanged grid values, checked on a shifted (between-node) grid
            Ne, Me = dyn.Ne, dyn.Me
            ca0, cG0 = dyn.coeffs_from_grid(fi['A'].reshape(Ne, Me), fi['B'].reshape(Ne, Me))
            eta_s = np.sort(np.cos(np.pi * np.arange(1, Ne) / Ne)); th_s = np.arange(1, Me) * np.pi / (2 * Me)
            ms = A2ModelT(N, M, L, beta_map, dyn.sigma_a, dyn.sigma_G, device=dev, eta_eval=eta_s, th_eval=th_s)
            fe0 = ms.fields(ca, cG, dyn.c_l); fe1 = ms.fields(ca0, cG0, dyn.c_l)
            P0a_e = ms.Pa[0][:, None]; P0G_e = ms.PG[0][:, None]
            P(f"  test projection (between-node grid, normalized fields): |dA|max={float(((fe1['a'] - fe0['a']) / P0a_e).abs().max()):.3e} "
              f"|dB|max={float(((fe1['G'] - fe0['G']) / P0G_e).abs().max()):.3e}  |dU1|/max={float((fe1['U1'] - fe0['U1']).abs().max() / fe0['U1'].abs().max()):.3e}  "
              f"coef norms before/after: a {float(ca.abs().max()):.2e}/{float(ca0.abs().max()):.2e} G {float(cG.abs().max()):.2e}/{float(cG0.abs().max()):.2e}")
        return
    hist = []; t0 = time.time(); s = 0.0
    for it in range(args.nsteps):
        ca, cG, dA, dB, fi = dyn.step(args.ds)
        s += args.ds
        dyn.set_state(ca, cG)
        if (it + 1) % args.diag_every == 0 or it == 0 or it == args.nsteps - 1:
            rateA = float(dA.pow(2).mean().sqrt() / args.ds); rateB = float(dB.pow(2).mean().sqrt() / args.ds)
            maxA = float(dA.abs().max() / args.ds); maxB = float(dB.abs().max() / args.ds)
            iA = np.unravel_index(int(dA.abs().argmax()), dA.shape); iB = np.unravel_index(int(dB.abs().argmax()), dB.shape)
            locA = (float(dyn.mg.r[iA[0]]), float(dyn.mg.th[iA[1]])); locB = (float(dyn.mg.r[iB[0]]), float(dyn.mg.th[iB[1]]))
            # rates restricted to r < 100 (absolute far-field amplification excluded)
            msk = torch.tensor(dyn.mg.r < 100.0, device=dev)
            maxA_in = float(dA[msk].abs().max() / args.ds); maxB_in = float(dB[msk].abs().max() / args.ds)
            dres = lm_residual(prob, ca, cG, dyn.c_l)
            zx, zy, lam, w2min = dyn.axis_zeros()
            tl = dyn.tails()
            rec = dict(it=it + 1, s=s, c=dyn.c, c_l=dyn.c_l, a0=dyn.a0, G0=dyn.G0, jetG=(2 * dyn.c_l + 1) * dyn.G0 - 2 * dyn.a0,
                       rateA=rateA, rateB=rateB, maxA=maxA, maxB=maxB, RMS=dres['Fnorm'], Ra_max=dres['Ra_max'], RG_max=dres['RG_max'],
                       zx=zx[:3], zy=zy[:3], lam=lam, w2min=w2min, t=time.time() - t0, **tl)
            hist.append(rec)
            P(f"it {it + 1:5d} s={s:7.3f} c_l={dyn.c_l:.6f} c={dyn.c:.5f} a0={dyn.a0:.6f} G0={dyn.G0:.5f} jetG={rec['jetG']:+.2e} "
              f"rate A/B={rateA:.2e}/{rateB:.2e} max={maxA:.2e}@({locA[0]:.1e},{locA[1]:.2f})/{maxB:.2e}@({locB[0]:.1e},{locB[1]:.2f}) max(r<100)={maxA_in:.2e}/{maxB_in:.2e} LM RMS={dres['Fnorm']:.3e} Ra/RG max={dres['Ra_max']:.2e}/{dres['RG_max']:.2e} "
              f"x*={zx[:2]} lam/(cl+2)={lam / (dyn.c_l + 2):.4f} yz={[round(v, 2) for v in zy[:3]]} w2min={w2min:.3f} "
              f"tails a {tl['a_rtail']:.1e}/{tl['a_atail']:.1e} G {tl['G_rtail']:.1e}/{tl['G_atail']:.1e} t={rec['t']:.0f}s")
            if not math.isfinite(rateA) or not math.isfinite(dyn.c):
                P("non-finite state; stopping"); break
        if args.mode == 'fixed' and abs(dyn.a0 - 1.0) > args.rescale_tol:
            lam_ = dyn.rescale_a0(); P(f"   rescaled by lam={lam_:.6f}: a0={dyn.a0:.6f} c={dyn.c:.5f}")
        if (it + 1) % args.save_every == 0 or it == args.nsteps - 1:
            z = prob.pack(dyn.ca, dyn.cG, dyn.c_l)
            save_state(f'runs/{args.name}.npz', prob, z, hist, extra=dict(vars(args), s=s, method='dynres'))
    P("done")


if __name__ == '__main__':
    main()
