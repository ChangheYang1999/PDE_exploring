"""Dynamic rescaling (pseudo-time) solver for Setting A2, local-grid version. Third, independent method.

Equations and normalizations as in dynres.py (whose global spectral projection proved unstable as a time-stepper):
  d_s A + W . grad A = lamA A,          A = a / t^{e_a},   a = Theta/(x^2 y),
  d_s B + W . grad B = lamB B + S,      B = G / t^{e_G},   G = Omega/(x y),
  W = c_l X + U,  c_w = 1,  c_l(s) = (c(s) - 2)/2  (mode a0; keeps a(0) = 1 exactly; beta := c_l is an output),
  or c_l = beta fixed (mode fixed; a(0) then drifts at rate c - 2 beta - 2 and is renormalized by spatial rescaling).
Transport grid: phi_i = i pi / Ni (eta = cos phi; t = (1 + eta)/2; r = L sqrt(t^{-2 beta} - 1)), i = 0 (origin) .. Ni
(infinity); theta_j = (j + 1/2) pi / (2 Nj). The grid is uniform in r near the origin and logarithmic at infinity (one
point per factor exp(2 beta dphi/phi') in r). Semi-Lagrangian: backward RK4 characteristics with the velocity of the
current state; A, B and the source S interpolated at the feet by 4-point Lagrange (cubic) interpolation in (phi, theta)
with even reflection across the axes and one-sided stencils at the ends; exponent integrals by Simpson. The velocity
comes from the canonical modal Green inverse (a2core_t) applied to the least-squares spectral fit (N x M) of B on the
grid; the same fit gives the origin strain c and the LM residual diagnostics. The origin row is advanced exactly
(d_s a0 = (c - 2 c_l - 2) a0, d_s G0 = -(2 c_l + 1) G0 + 2 a0); the infinity row is extrapolated from the interior.
"""
import sys, time, json, math, argparse
import numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT, cheb_gauss_nodes, cheb_T
from a2core_t import A2ModelT
from lm_solve import LMProblem, load_state, save_state, problem_from_state, initial_guess, dev, make_model, rad_of_r
from dynres import chebT_torch


def lagrange4_weights(x, p):
    """x: [P], p: [P, 4] node positions -> weights [P, 4]."""
    w = torch.ones_like(p)
    for k in range(4):
        for m in range(4):
            if m != k:
                w[:, k] = w[:, k] * (x - p[:, m]) / (p[:, k] - p[:, m])
    return w


class DynResGrid:
    def __init__(self, Ni, Nj, N, M, L, beta_map, sigma_a=None, sigma_G=None, Nf=None, c_w=1.0, mode='a0', pinv_tol=1e-10):
        self.Ni, self.Nj, self.N, self.M, self.L, self.beta_map = Ni, Nj, N, M, float(L), float(beta_map)
        b = self.beta_map
        self.sigma_a = (1.0 + 1.0 / b) if sigma_a is None else float(sigma_a)
        self.sigma_G = (1.0 + 1.0 / (2 * b)) if sigma_G is None else float(sigma_G)
        self.c_w, self.mode = float(c_w), mode
        # transport grid
        self.dphi = math.pi / Ni; self.dth = math.pi / (2 * Nj)
        self.phi = torch.arange(Ni + 1, dtype=DT, device=dev) * self.dphi
        self.th = (torch.arange(Nj, dtype=DT, device=dev) + 0.5) * self.dth
        self.eta = torch.cos(self.phi); self.t = (1 + self.eta) / 2
        self.t[0] = 1.0; self.t[-1] = 0.0
        tt = self.t.clone(); tt[-1] = 1e-300
        self.r = self.L * torch.sqrt(torch.clamp(tt ** (-2 * b) - 1.0, min=0.0)); self.r[0] = 0.0; self.r[-1] = float('inf')
        self.rho2 = 1 - self.t ** (2 * b)
        # spectral velocity model on a Chebyshev-Gauss radial grid (exact Green quadrature) and interpolation to points
        self.Nf = Nf or 2 * N
        self.eta_f = cheb_gauss_nodes(self.Nf)
        self.mf = A2ModelT(N, M, L, b, self.sigma_a, self.sigma_G, device=dev, eta_eval=self.eta_f, th_eval=np.array([0.3]))
        self.mu, self.e_a, self.e_G = self.mf.mu, self.mf.e_a, self.mf.e_G
        self.Tf = torch.tensor(cheb_T(self.eta_f, self.Nf), dtype=DT, device=dev); self.Tfinv = torch.linalg.inv(self.Tf)
        rf = torch.tensor(self.mf.r, dtype=DT, device=dev); tf = torch.tensor(self.mf.t, dtype=DT, device=dev)
        self.normH = rf ** 2 * tf ** self.mu; self.normD = rf * tf ** self.mu
        self.l = torch.arange(M, dtype=DT, device=dev); self.kk = 2 * (self.l + 1)
        # least-squares spectral fit of grid fields: angular (uniform midpoints, exact orthogonality) and radial per mode
        C = torch.cos(2 * self.th[:, None] * self.l[None, :])        # [Nj, M]
        self.Cpinv = torch.linalg.pinv(C)                           # [M, Nj]
        Tg = torch.tensor(cheb_T(self.eta.cpu().numpy(), N), dtype=DT, device=dev)   # [Ni+1, N]
        self.pinvs = []; self.ranks = []
        for l in range(M):
            Bm = (self.rho2 ** l)[:, None] * Tg
            U_, S_, Vh = torch.linalg.svd(Bm, full_matrices=False)
            keep = S_ > pinv_tol * S_[0]
            self.pinvs.append(Vh[keep].T @ torch.diag(1.0 / S_[keep]) @ U_[:, keep].T)
            self.ranks.append(int(keep.sum()))
        self.Tg = Tg
        # Cartesian grid points (interior rows 1..Ni-1 only are transported)
        PH, TH = torch.meshgrid(self.phi[1:-1], self.th, indexing='ij')
        R = self.r[1:-1][:, None].expand_as(PH)
        self.Xg = (R * torch.cos(TH)).reshape(-1); self.Yg = (R * torch.sin(TH)).reshape(-1)
        self.PHg = PH.reshape(-1); self.THg = TH.reshape(-1)
        # geometric factors for the source on the grid: dr/dphi
        # r = L sqrt(t^{-2b} - 1), dt/dphi = -sin(phi)/2, dr/dt = -b L^2 t^{-2b-1}/r  =>  dr/dphi = b L^2 t^{-2b-1} sin(phi)/(2 r)
        drdphi = b * self.L ** 2 * tt ** (-2 * b - 1) * torch.sin(self.phi) / (2 * torch.clamp(self.r, min=1e-300))
        drdphi[0] = self.L * math.sqrt(b / 2.0); drdphi[-1] = float('inf')
        self.drdphi = drdphi
        self.origin_T = torch.tensor(cheb_T(np.array([1.0]), N)[0], dtype=DT, device=dev)

    # ---------- spectral fit and velocity ----------
    def fit(self, F):
        """grid field [Ni+1, Nj] (normalized) -> coefficients [M, N] by least squares."""
        Fl = (F @ self.Cpinv.T).T                         # [M, Ni+1]
        return torch.stack([self.pinvs[l] @ Fl[l] for l in range(self.M)])

    def fit_misfit(self, F, c):
        Fl = (F @ self.Cpinv.T).T
        rec = torch.stack([(self.rho2 ** l) * (self.Tg @ c[l]) for l in range(self.M)])
        return float((rec - Fl).abs().max()), float(Fl.abs().max())

    def set_velocity(self, cG, c_l=None):
        ff = self.mf.fields(torch.zeros_like(cG), cG, self.beta_map)
        self.c = float(ff['c'])
        if self.mode == 'jet':            # two-jet normalization a0, b0 fixed: c_w = c - K, c_l = K - c/2, K = 2 a0/b0
            self.c_w = self.c - self.K; c_l = self.K - self.c / 2
        elif self.mode == 'beta':         # beta = beta_map fixed and a0 fixed: c_w = c/(2 beta + 2), c_l = beta c_w (no free symmetry mode)
            self.c_w = self.c / (2 * self.beta_map + 2); c_l = self.beta_map * self.c_w
        elif c_l is None:
            c_l = (self.c - 2 * self.c_w) / 2 if self.mode == 'a0' else self.beta_map
        self.c_l = float(c_l)
        self.coefH = (ff['h'] / self.normH[None, :]) @ self.Tfinv.T
        self.coefD = (ff['hd'] / self.normD[None, :]) @ self.Tfinv.T

    def velocity(self, x, y):
        b, L = self.beta_map, self.L
        r = torch.sqrt(x * x + y * y); th = torch.atan2(y, x)
        t = (1 + (r / L) ** 2) ** (-1 / (2 * b)); eta = 2 * t - 1
        cth, sth = torch.cos(th), torch.sin(th)
        Tfp = chebT_torch(eta, self.Nf)
        h = (Tfp @ self.coefH.T) * (r ** 2 * t ** self.mu)[:, None]
        hd = (Tfp @ self.coefD.T) * (r * t ** self.mu)[:, None]
        kth = th[:, None] * self.kk[None, :]
        Psi_r = (hd * torch.sin(kth)).sum(1); Psi_th = (h * self.kk[None, :] * torch.cos(kth)).sum(1)
        U1 = -(sth * Psi_r + cth * Psi_th / r); U2 = cth * Psi_r - sth * Psi_th / r; U_r = -Psi_th / r
        c_l = self.c_l
        W1 = c_l * x + U1; W2 = c_l * y + U2
        w1 = c_l + U1 / x; w2 = c_l + U2 / y
        W_r = c_l * r + U_r
        dlogt_dr = -r * t ** (2 * b) / (b * L ** 2)
        lamA = (c_l - 2 * self.c_w - 2 * w1 - w2) - W_r * self.e_a * dlogt_dr
        lamB = -(w1 + w2 + self.c_w) - W_r * self.e_G * dlogt_dr
        return dict(W1=W1, W2=W2, U1=U1, U2=U2, w1=w1, w2=w2, lamA=lamA, lamB=lamB, r=r, th=th, t=t)

    # ---------- local interpolation ----------
    def interp(self, F, phi, th):
        """F: [Ni+1, Nj]; phi, th: [P] -> values [P] by 4-point Lagrange in phi (one-sided at the ends) and theta (even reflection)."""
        Ni, Nj = self.Ni, self.Nj
        fi = phi / self.dphi
        i0 = torch.clamp(torch.floor(fi).long() - 1, 0, Ni - 3)
        ii = i0[:, None] + torch.arange(4, device=dev)[None, :]                  # [P, 4]
        wi = lagrange4_weights(fi, ii.to(DT))
        fj = th / self.dth - 0.5
        j0 = torch.floor(fj).long() - 1
        jj = j0[:, None] + torch.arange(4, device=dev)[None, :]
        wj = lagrange4_weights(fj, jj.to(DT))
        jj = torch.where(jj < 0, -1 - jj, jj); jj = torch.where(jj > Nj - 1, 2 * Nj - 1 - jj, jj)
        vals = F[ii[:, :, None], jj[:, None, :]]                                   # [P, 4, 4]
        return (wi[:, :, None] * wj[:, None, :] * vals).sum((1, 2))

    # ---------- derivatives on the grid (for the source) ----------
    def source(self, A):
        """S = (2 a + x a_x)/t^{e_G} = t [2A + cos^2 th (r A_r) - cos th sin th A_th - (e_a/b) cos^2 th (1 - t^{2b}) A]."""
        Ni, Nj = self.Ni, self.Nj
        # A_phi: 4th-order centered, one-sided at the ends (2nd order there)
        Aph = torch.zeros_like(A)
        Aph[2:-2] = (-A[4:] + 8 * A[3:-1] - 8 * A[1:-3] + A[:-4]) / (12 * self.dphi)
        Aph[1] = (A[2] - A[0]) / (2 * self.dphi); Aph[-2] = (A[-1] - A[-3]) / (2 * self.dphi)
        Aph[0] = (-3 * A[0] + 4 * A[1] - A[2]) / (2 * self.dphi); Aph[-1] = (3 * A[-1] - 4 * A[-2] + A[-3]) / (2 * self.dphi)
        # A_theta: 4th-order centered with even reflection
        Ae = torch.cat([A[:, [1, 0]], A, A[:, [-1, -2]]], 1)     # two reflected columns each side (even in theta)
        Ath = (-Ae[:, 4:] + 8 * Ae[:, 3:-1] - 8 * Ae[:, 1:-3] + Ae[:, :-4]) / (12 * self.dth)
        rAr = (self.r / self.drdphi)[:, None] * Aph
        rAr[0] = 0.0; rAr[-1] = 0.0
        c2 = torch.cos(self.th)[None, :] ** 2; cs = (torch.cos(self.th) * torch.sin(self.th))[None, :]
        S = self.t[:, None] * (2 * A + c2 * rAr - cs * Ath - (self.e_a / self.beta_map) * c2 * self.rho2[:, None] * A)
        return S

    # ---------- one step ----------
    def step(self, A, B, ds):
        X, Y = self.Xg, self.Yg
        vi = self.velocity(X, Y)
        k1x, k1y = -vi['W1'], -vi['W2']
        o = self.velocity(X + 0.5 * ds * k1x, Y + 0.5 * ds * k1y); k2x, k2y = -o['W1'], -o['W2']
        o = self.velocity(X + 0.5 * ds * k2x, Y + 0.5 * ds * k2y); k3x, k3y = -o['W1'], -o['W2']
        o = self.velocity(X + ds * k3x, Y + ds * k3y); k4x, k4y = -o['W1'], -o['W2']
        Xf = (X + ds * (k1x + 2 * k2x + 2 * k3x + k4x) / 6).abs(); Yf = (Y + ds * (k1y + 2 * k2y + 2 * k3y + k4y) / 6).abs()
        vf = self.velocity(Xf, Yf)
        Xm = (0.5 * (X + Xf) + 0.125 * ds * (k1x + vf['W1'])).abs(); Ym = (0.5 * (Y + Yf) + 0.125 * ds * (k1y + vf['W2'])).abs()
        vm = self.velocity(Xm, Ym)
        S = self.source(A)
        def ph_th(v):
            t = v['t']; eta = 2 * t - 1
            return torch.arccos(torch.clamp(eta, -1.0, 1.0)), v['th']
        pf, tf_ = ph_th(vf); pm, tm_ = ph_th(vm)
        Af = self.interp(A, pf, tf_); Bf = self.interp(B, pf, tf_); Sf = self.interp(S, pf, tf_); Sm = self.interp(S, pm, tm_)
        Si = S[1:-1].reshape(-1)
        LamA = ds / 6 * (vf['lamA'] + 4 * vm['lamA'] + vi['lamA'])
        LamB = ds / 6 * (vf['lamB'] + 4 * vm['lamB'] + vi['lamB'])
        LamB_mid = ds / 4 * (vm['lamB'] + vi['lamB'])
        A_new = Af * torch.exp(LamA)
        B_new = Bf * torch.exp(LamB) + ds / 6 * (torch.exp(LamB) * Sf + 4 * torch.exp(LamB_mid) * Sm + Si)
        Ni, Nj = self.Ni, self.Nj
        An = A.clone(); Bn = B.clone()
        An[1:-1] = A_new.reshape(Ni - 1, Nj); Bn[1:-1] = B_new.reshape(Ni - 1, Nj)
        # origin row: exact ODEs
        a0 = float(A[0, 0]); G0 = float(B[0, 0]); c_l = self.c_l; c = self.c
        d = c - 2 * c_l - 2 * self.c_w; k = 2 * c_l + self.c_w        # exact coupled origin ODEs over the step (frozen c)
        An[0] = a0 * math.exp(d * ds)
        if abs(d + k) > 1e-12:
            Bn[0] = G0 * math.exp(-k * ds) + 2 * a0 * (math.exp(d * ds) - math.exp(-k * ds)) / (d + k)
        else:
            Bn[0] = G0 * math.exp(-k * ds) + 2 * a0 * ds * math.exp(-k * ds)
        # infinity row: quadratic extrapolation in phi from the three last interior rows
        An[-1] = 3 * An[-2] - 3 * An[-3] + An[-4]; Bn[-1] = 3 * Bn[-2] - 3 * Bn[-3] + Bn[-4]
        return An, Bn

    def rescale(self, A, B, lam):
        """X -> lam X: a_new(X) = a(X/lam)/lam^2, G_new(X) = G(X/lam)/lam^2 (normalized fields re-evaluated by interpolation)."""
        b = self.beta_map
        r_src = self.r[1:-1] / lam
        t_src = (1 + (r_src / self.L) ** 2) ** (-1 / (2 * b)); phi_src = torch.arccos(torch.clamp(2 * t_src - 1, -1.0, 1.0))
        PH, TH = torch.meshgrid(phi_src, self.th, indexing='ij')
        fac_a = ((t_src ** self.e_a) / (self.t[1:-1] ** self.e_a) / lam ** 2)[:, None]
        fac_G = ((t_src ** self.e_G) / (self.t[1:-1] ** self.e_G) / lam ** 2)[:, None]
        An = A.clone(); Bn = B.clone()
        An[1:-1] = self.interp(A, PH.reshape(-1), TH.reshape(-1)).reshape(self.Ni - 1, self.Nj) * fac_a
        Bn[1:-1] = self.interp(B, PH.reshape(-1), TH.reshape(-1)).reshape(self.Ni - 1, self.Nj) * fac_G
        An[0] = A[0] / lam ** 2; Bn[0] = B[0] / lam ** 2
        An[-1] = 3 * An[-2] - 3 * An[-3] + An[-4]; Bn[-1] = 3 * Bn[-2] - 3 * Bn[-3] + Bn[-4]
        return An, Bn

    # ---------- diagnostics ----------
    def axis_zeros(self, rmin=0.05, rmax=3000.0, n=400):
        rr = torch.tensor(np.geomspace(rmin, rmax, n), dtype=DT, device=dev); eps = torch.full_like(rr, 1e-9)
        fx = self.velocity(rr, eps); fy = self.velocity(eps, rr)
        w1 = fx['w1'].cpu().numpy(); w2 = fy['w2'].cpu().numpy(); r = rr.cpu().numpy(); lr = np.log(r)
        def zeros(v):
            idx = np.where(np.diff(np.sign(v)) != 0)[0]
            return [float(np.exp(lr[i] + (lr[i + 1] - lr[i]) * v[i] / (v[i] - v[i + 1]))) for i in idx]
        zx, zy = zeros(w1), zeros(w2); lam = float('nan')
        if zx:
            x0 = zx[0]; h = 1e-5 * x0
            o = self.velocity(torch.tensor([x0 + h, x0 - h], dtype=DT, device=dev), torch.tensor([1e-9, 1e-9], dtype=DT, device=dev))
            lam = float((o['W1'][0] - o['W1'][1]) / (2 * h))
        return zx, zy, lam, float(w2.min())


def grid_from_state(dyn, d):
    """Evaluate a saved spectral state on the transport grid (normalized fields A, B)."""
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    beta_map = float(d['beta_map']); sa, sG = float(d['sigma_a']), float(d['sigma_G'])
    r = dyn.r[1:-1].cpu().numpy()
    m = make_model('t', N, M, L, beta_map, sa, sG, rad_of_r(dyn.mf, 't', r) if abs(beta_map - dyn.beta_map) < 1e-12 and abs(L - dyn.L) < 1e-12 else
                   2 * (1 + (r / L) ** 2) ** (-1 / (2 * beta_map)) - 1, dyn.th.cpu().numpy())
    ca = torch.tensor(d['ca'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    f = m.fields(ca, cG, float(d['beta']))
    A = torch.zeros((dyn.Ni + 1, dyn.Nj), dtype=DT, device=dev); B = torch.zeros_like(A)
    A[1:-1] = f['a'] / (dyn.t[1:-1] ** dyn.e_a)[:, None]; B[1:-1] = f['G'] / (dyn.t[1:-1] ** dyn.e_G)[:, None]
    A[0] = float(f['a0']); B[0] = float(f['G0'])
    A[-1] = 3 * A[-2] - 3 * A[-3] + A[-4]; B[-1] = 3 * B[-2] - 3 * B[-3] + B[-4]
    return A, B


def grid_gaussian(dyn, beta0, RG=None, kind='gauss'):
    a0 = 1.0; G0 = 2 * a0 / (2 * beta0 + 1)
    if RG is None:
        RG = math.sqrt(8 * (2 * beta0 + 2) / abs(G0)) if kind == 'gauss' else math.sqrt(8 * (2 * beta0 + 2) * (dyn.sigma_G - 1) / abs(G0))
    r = dyn.r.clone(); r[-1] = 1e300
    if kind == 'gauss':
        fa = a0 * torch.exp(-r ** 2 / RG ** 2); fG = G0 * torch.exp(-r ** 2 / RG ** 2)
    else:
        fa = a0 * (1 + r ** 2 / RG ** 2) ** (-dyn.sigma_a); fG = G0 * (1 + r ** 2 / RG ** 2) ** (-dyn.sigma_G)
    t = dyn.t.clone(); t[-1] = 1e-300
    A = (fa / t ** dyn.e_a)[:, None].expand(-1, dyn.Nj).clone(); B = (fG / t ** dyn.e_G)[:, None].expand(-1, dyn.Nj).clone()
    A[-1] = 3 * A[-2] - 3 * A[-3] + A[-4]; B[-1] = 3 * B[-2] - 3 * B[-3] + B[-4]
    return A, B


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', type=str, default=None)
    ap.add_argument('--Ni', type=int, default=512); ap.add_argument('--Nj', type=int, default=96)
    ap.add_argument('--N', type=int, default=64); ap.add_argument('--M', type=int, default=16)
    ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--beta', type=float, default=2.0)
    ap.add_argument('--kind', type=str, default='gauss'); ap.add_argument('--RG', type=float, default=None)
    ap.add_argument('--ds', type=float, default=0.01); ap.add_argument('--nsteps', type=int, default=1000)
    ap.add_argument('--mode', type=str, default='a0', help='a0 | fixed | jet | beta'); ap.add_argument('--c_w', type=float, default=1.0)
    ap.add_argument('--K', type=float, default=None, help='jet mode: K = 2 a0/b0 (default from the initial state)')
    ap.add_argument('--diag_every', type=int, default=50); ap.add_argument('--save_every', type=int, default=200)
    ap.add_argument('--rescale_tol', type=float, default=1e-2); ap.add_argument('--Rw', type=float, default=30.0)
    ap.add_argument('--name', type=str, default='dyn2'); ap.add_argument('--test', action='store_true')
    ap.add_argument('--freeze_vel', action='store_true')
    args = ap.parse_args()
    log = open(f'runs/{args.name}.log', 'a')
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n'); log.flush()
    P(f"# {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} dynres2 args: {vars(args)}")
    dyn = DynResGrid(args.Ni, args.Nj, args.N, args.M, args.L, args.beta, c_w=args.c_w, mode=args.mode)
    prob = LMProblem(args.N, args.M, args.L, args.beta, dyn.sigma_a, dyn.sigma_G, 1.0, 30.0, None, ov=2.0, mapname='t', Rw=args.Rw)
    if args.init:
        d = load_state(args.init); A, B = grid_from_state(dyn, d)
    else:
        A, B = grid_gaussian(dyn, args.beta, args.RG, args.kind)
    P(f"grid Ni={args.Ni} Nj={args.Nj} (r[1]={float(dyn.r[1]):.4f}, r[Ni-1]={float(dyn.r[-2]):.3e}); spectral N={args.N} M={args.M} ranks {min(dyn.ranks)}..{max(dyn.ranks)}; mode={args.mode}")
    dyn.K = 2 * float(A[0, 0]) / float(B[0, 0]) if args.K is None else args.K
    cG = dyn.fit(B); dyn.set_velocity(cG)
    mA = dyn.fit_misfit(A, dyn.fit(A)); mB = dyn.fit_misfit(B, cG)
    P(f"initial: c={dyn.c:.6f} c_l={dyn.c_l:.6f} c_w={dyn.c_w:.6f} K={dyn.K:.6f} a0={float(A[0,0]):.6f} G0={float(B[0,0]):.6f}; fit misfit A {mA[0]:.2e}/{mA[1]:.2e} B {mB[0]:.2e}/{mB[1]:.2e}")
    if args.test:
        # velocity vs exact model at some points; one step vs LM residual (if init given)
        xs = torch.tensor([0.5, 2.0, 5.0, 10.0, 18.0, 50.0], dtype=DT, device=dev); ys = torch.tensor([0.3, 1.0, 5.0, 2.0, 0.5, 20.0], dtype=DT, device=dev)
        v = dyn.velocity(xs, ys)
        r = torch.sqrt(xs ** 2 + ys ** 2).cpu().numpy(); th = torch.atan2(ys, xs).cpu().numpy()
        m2 = make_model('t', args.N, args.M, args.L, args.beta, dyn.sigma_a, dyn.sigma_G, dyn.mf.eta_of_r(r), th)
        f2 = m2.fields(dyn.fit(A), cG, dyn.c_l)
        U1ex = torch.diagonal(f2['U1']); U2ex = torch.diagonal(f2['U2'])
        P("  velocity check (interp vs exact quadrature):", [(f"{float(a):.3e}", f"{float(b):.3e}") for a, b in zip(v['U1'] - U1ex, U1ex)])
        if args.init:
            dd = load_state(args.init); pr0, z0 = problem_from_state(dd)
            ca0, cG0, b0 = pr0.unpack(z0)
            mm = make_model('t', int(dd['N']), int(dd['M']), float(dd['L']), float(dd['beta_map']), float(dd['sigma_a']), float(dd['sigma_G']),
                            dyn.mf.eta_of_r(dyn.r[1:-1].cpu().numpy()), dyn.th.cpu().numpy())
            fe = mm.fields(ca0, cG0, float(dd['beta']))
            for ds in (2e-3, 1e-3):
                An, Bn = dyn.step(A, B, ds)
                dA = (An - A)[1:-1] / ds; dB = (Bn - B)[1:-1] / ds
                pA = -fe['Ra'] / (dyn.t[1:-1] ** dyn.e_a)[:, None]; pB = -fe['RG'] / (dyn.t[1:-1] ** dyn.e_G)[:, None]
                rr = dyn.r[1:-1]; msk = (rr < 100)[:, None].expand_as(dA)
                P(f"  step ds={ds}: |dA/ds + Ra/P0|max={float((dA - pA).abs().max()):.3e} (r<100: {float((dA - pA)[msk].abs().max()):.3e}; |pred|max {float(pA[msk].abs().max()):.3e}) "
                  f"|dB/ds + RG/P0|max={float((dB - pB).abs().max()):.3e} (r<100: {float((dB - pB)[msk].abs().max()):.3e}; |pred| {float(pB[msk].abs().max()):.3e})")
        return
    hist = []; t0 = time.time(); s = 0.0
    for it in range(args.nsteps):
        An, Bn = dyn.step(A, B, args.ds); s += args.ds
        dA = (An - A) / args.ds; dB = (Bn - B) / args.ds
        A, B = An, Bn
        if not args.freeze_vel:
            cG = dyn.fit(B); dyn.set_velocity(cG)
        if args.mode == 'fixed' and abs(float(A[0, 0]) - 1.0) > args.rescale_tol:
            lam = math.sqrt(abs(float(A[0, 0]))); A, B = dyn.rescale(A, B, lam)
            cG = dyn.fit(B); dyn.set_velocity(cG); P(f"   rescaled by {lam:.6f}")
        if (it + 1) % args.diag_every == 0 or it == 0 or it == args.nsteps - 1:
            ca = dyn.fit(A); cG = dyn.fit(B)
            mA = dyn.fit_misfit(A, ca); mB = dyn.fit_misfit(B, cG)
            rr = dyn.r.clone(); rr[-1] = 1e300
            msk = (rr < 100)[:, None].expand_as(dA)
            z = prob.pack(ca, cG, dyn.c_l); dres = prob.diagnostics(z)
            zx, zy, lam, w2min = dyn.axis_zeros()
            a0 = float(A[0, 0]); G0 = float(B[0, 0])
            rec = dict(it=it + 1, s=s, c=dyn.c, c_l=dyn.c_l, c_w=dyn.c_w, beta=dyn.c_l / dyn.c_w if dyn.c_w != 0 else float('nan'), a0=a0, G0=G0, jetG=(2 * dyn.c_l + dyn.c_w) * G0 - 2 * a0,
                       rateA_in=float(dA[msk].abs().max()), rateB_in=float(dB[msk].abs().max()), rateA_rms=float(dA[1:-1].pow(2).mean().sqrt()),
                       rateA_all=float(dA[1:-1].abs().max()), rateB_all=float(dB[1:-1].abs().max()),
                       misfitA=mA[0], misfitB=mB[0], RMS=dres['Fnorm'], Ra_max=dres['Ra_max'], RG_max=dres['RG_max'],
                       zx=zx[:3], zy=zy[:3], lam=lam, w2min=w2min, Amax=float(A.abs().max()), Bmax=float(B.abs().max()), t=time.time() - t0)
            hist.append(rec)
            P(f"it {it + 1:5d} s={s:7.3f} c_l={dyn.c_l:.6f} c_w={dyn.c_w:.5f} beta={rec['beta']:.5f} c={dyn.c:.5f} a0={a0:.6f} G0={G0:.5f} jetG={rec['jetG']:+.2e} "
              f"rate(r<100) A/B={rec['rateA_in']:.2e}/{rec['rateB_in']:.2e} rate(all) {rec['rateA_all']:.2e}/{rec['rateB_all']:.2e} rmsA={rec['rateA_rms']:.2e} "
              f"fitmis A/B={mA[0]:.1e}/{mB[0]:.1e} LM RMS={dres['Fnorm']:.3e} Ra/RG={dres['Ra_max']:.2e}/{dres['RG_max']:.2e} "
              f"x*={[round(v, 3) for v in zx[:2]]} lam/(cl+2cw)={lam / (dyn.c_l + 2 * dyn.c_w):.4f} yz={[round(v, 2) for v in zy[:3]]} w2min={w2min:.3f} |A|max={rec['Amax']:.2e} |B|max={rec['Bmax']:.2e} t={rec['t']:.0f}s")
            if not math.isfinite(dyn.c) or not math.isfinite(a0):
                P("non-finite; stop"); break
        if (it + 1) % args.save_every == 0 or it == args.nsteps - 1:
            ca = dyn.fit(A); cG = dyn.fit(B); z = prob.pack(ca, cG, dyn.c_l)
            save_state(f'runs/{args.name}.npz', prob, z, hist, extra=dict(vars(args), s=s, method='dynres2'))
            np.savez(f'runs/{args.name}_grid.npz', A=A.cpu().numpy(), B=B.cpu().numpy(), phi=dyn.phi.cpu().numpy(), th=dyn.th.cpu().numpy(),
                     c_l=dyn.c_l, c=dyn.c, s=s, beta_map=dyn.beta_map, L=dyn.L, e_a=dyn.e_a, e_G=dyn.e_G)
    P("done")


if __name__ == '__main__':
    main()
