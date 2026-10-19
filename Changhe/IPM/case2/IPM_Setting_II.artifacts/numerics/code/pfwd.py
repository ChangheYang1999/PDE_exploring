"""GPU forward self-similar IPM evolution (numerical researcher's version of the lead analyst's explore/pforward.py, specification M22).

Self-similar variables: d_s rho = V.grad rho - rho,  V = c_l X + W[rho],  W = U - U(0) the canonical once-subtracted
Biot-Savart velocity of class S (specification 1.1), c_l = 1/p FIXED.  With rho = r^p g:
        d_s g = V.grad g + p (W_r / r) g,
inflow g = A(theta) at r_max (the far-field datum; characteristics of the evolution move along -V, i.e. inward).
Steady states are generalized profiles with far field r^p A: the node structure DV(0) = diag(m1, 2 c_l - m1) is an OUTPUT.
Setting II needs m1 = 1/2 (equivalently psi_xy(0) = c_l - 1/2, the compatibility identity) with the x^2 jet.
Nothing is imposed: no symmetry, no jet, no square root.

Grid: lr = log r uniform on [lo, hi] (Nr points), theta uniform (Nth points, FFT).  Velocity: per-mode Green formulas
in log r by product integration (piecewise-linear integrand, exact exponential kernel weights), precomputed as
lower/upper triangular matrices per mode and applied as batched matmuls; one-term tail f_m ~ r^{p-1} beyond r_max;
m = +-1 renormalised (W(0) = 0).  d_x rho from 6th-order finite differences in lr and the FFT in theta.
Transport: semi-Lagrangian, RK2 (midpoint) foot point, periodic cubic Lagrange interpolation, optional bilinear-hull
limiter (as in the lead's code), datum A at feet beyond r_max.
"""
import math, json, time, sys
import numpy as np
import torch
torch.set_default_dtype(torch.float64)


# ---------------------------------------------------------------------------------------------------------------
def fd_dlr(F, d):
    """d/dlr along axis 0 (uniform spacing d): 6th-order centred inside, 6th-order one-sided 7-point stencils at the ends."""
    G = torch.empty_like(F)
    G[3:-3] = (F[6:] - 9 * F[5:-1] + 45 * F[4:-2] - 45 * F[2:-4] + 9 * F[1:-5] - F[:-6]) / (60 * d)
    c0 = torch.tensor([-147, 360, -450, 400, -225, 72, -10], dtype=F.dtype, device=F.device) / 60
    c1 = torch.tensor([-10, -77, 150, -100, 50, -15, 2], dtype=F.dtype, device=F.device) / 60
    c2 = torch.tensor([2, -24, -35, 80, -30, 8, -1], dtype=F.dtype, device=F.device) / 60
    top = F[:7]; bot = F[-7:].flip(0)
    for i, c in enumerate((c0, c1, c2)):
        G[i] = torch.tensordot(c, top, dims=([0], [0])) / d
        G[-1 - i] = -torch.tensordot(c, bot, dims=([0], [0])) / d
    return G


def datum(th, kind, par, table=None):
    c, s = torch.cos(th), torch.sin(th)
    if kind == 'cos2':
        return c ** 2
    if kind == 'cosk':
        return c.abs() ** par
    if kind == 'rhoa':                       # far field of the family-A seed: cos^2 (1 + a sin)^2
        return c ** 2 * (1 + par * s) ** 2
    if kind == 'cos2sin':                    # cos^2 (1 + a sin), |a| < 1 keeps A >= 0
        return c ** 2 * (1 + par * s)
    if kind == 'plateau':
        return torch.tanh(par * c ** 2) / math.tanh(par)
    if kind == 'plateau_a':
        return torch.tanh(par * c ** 2) / math.tanh(par) * (1 + 0.5 * s) ** 2
    if kind == 'asym':                       # x-odd part: cos^2 (1 + 0.5 sin + a cos sin)^2
        return c ** 2 * (1 + 0.5 * s + par * c * s) ** 2
    if kind == 'asym2':                      # cos^2 (1 + a sin)^2 (1 + 0.3 cos sin)^2  (par = a)
        return c ** 2 * (1 + par * s) ** 2 * (1 + 0.3 * c * s) ** 2
    if kind == 'fourier':                    # cos^2 (1 + sum_k a_k sin k th + b_k cos k th)^2, par = list [a1, b1, a2, b2, ...]
        f = torch.ones_like(th)
        for k in range(len(par) // 2):
            f = f + par[2 * k] * torch.sin((k + 1) * th) + par[2 * k + 1] * torch.cos((k + 1) * th)
        return c ** 2 * f ** 2
    if kind == 'expf':                       # cos^2 exp(x1 sin th + x2 cos 2th + x3 sin 3th + x4 cos 4th + ...) (x-even basis; par = list)
        f = torch.zeros_like(th)
        for k, xk in enumerate(par):
            n = k + 1
            f = f + xk * (torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th))
        return c ** 2 * torch.exp(f)
    if kind == 'table':
        thA, AA = table
        thm = torch.remainder(th, 2 * math.pi)
        return torch.tensor(np.interp(thm.cpu().numpy(), thA, AA, period=2 * math.pi), device=th.device)
    raise ValueError(kind)


# ---------------------------------------------------------------------------------------------------------------
class PFwd:
    def __init__(self, Nr, Nth, lo, hi, p, dev='cuda', limiter=True, thshift=0.0, tail2=False):
        self.dev = torch.device(dev)
        self.thshift = float(thshift)
        self.tail2 = bool(tail2)
        self.Nr, self.Nth, self.lo, self.hi, self.p = Nr, Nth, float(lo), float(hi), float(p)
        self.cl = 1.0 / p
        self.limiter = limiter
        self.lr = torch.linspace(lo, hi, Nr, device=self.dev)
        self.d = float(self.lr[1] - self.lr[0])
        self.th = (torch.arange(Nth, device=self.dev) + self.thshift) * (2 * math.pi / Nth)
        self.dth = 2 * math.pi / Nth
        self.r = torch.exp(self.lr)
        self.cos, self.sin = torch.cos(self.th), torch.sin(self.th)
        self.Mm = Nth // 2                                 # kept modes m = 0 .. Mm-1 (Nyquist dropped)
        self.m = torch.arange(self.Mm, device=self.dev, dtype=torch.float64)
        self._build_kernels()
        self.ii = torch.arange(Nr, device=self.dev, dtype=torch.float64)[:, None]
        self.jj = torch.arange(Nth, device=self.dev, dtype=torch.float64)[None, :]

    def _build_kernels(self):
        Nr, Mm, d = self.Nr, self.Mm, self.d
        a = self.m.clone()                                  # decay rate |m| of the kernel e^{-|m| |u-v|}
        z = a * d
        small = z < 1e-8
        zz = torch.where(small, torch.ones_like(z), z)
        wprev = d * (1 - torch.exp(-zz) * (1 + zz)) / zz ** 2          # weight of h at the far end of the cell
        wcur = d * (zz - 1 + torch.exp(-zz)) / zz ** 2                  # weight of h at the near end
        wprev = torch.where(small, torch.full_like(z, d / 2), wprev)
        wcur = torch.where(small, torch.full_like(z, d / 2), wcur)
        lam = torch.exp(-z)
        I = torch.eye(Nr, device=self.dev)
        # inward kernel: Al[k] = sum_j Kin[k,j] h_j  (h = f_m e^{2v});  inner contribution h_0/(|m|+2)
        Kin = torch.zeros(Mm, Nr, Nr, device=self.dev)
        Kin[:, 0, :] = (1.0 / (a + 2.0))[:, None] * I[0][None, :]
        for k in range(1, Nr):
            Kin[:, k, :] = lam[:, None] * Kin[:, k - 1, :] + wprev[:, None] * I[k - 1][None, :] + wcur[:, None] * I[k][None, :]
        self.Kin = Kin
        # outward kernel for |m| >= 2: Ag[k] = sum_j Kout[k,j] h_j; tail h ~ e^{(p+1)(v-hi)}: Ag[Nr-1] = h_{Nr-1}/(|m|-1-p)
        Kout = torch.zeros(Mm, Nr, Nr, device=self.dev)
        tailc = torch.where(a >= 2, 1.0 / torch.clamp(a - 1.0 - self.p, min=1e-12), torch.zeros_like(a))
        Kout[:, Nr - 1, :] = tailc[:, None] * I[Nr - 1][None, :]
        for k in range(Nr - 2, -1, -1):
            Kout[:, k, :] = lam[:, None] * Kout[:, k + 1, :] + wcur[:, None] * I[k][None, :] + wprev[:, None] * I[k + 1][None, :]
        self.Kout = Kout
        # m = 1 renormalised: Ag = -r I1, I1[k] = int_{-inf}^{v_k} f_1 e^v dv (trapezoid, inner term hq_0)
        K1 = torch.zeros(Nr, Nr, device=self.dev)
        K1[0, 0] = 1.0
        for k in range(1, Nr):
            K1[k] = K1[k - 1] + 0.5 * d * (I[k - 1] + I[k])
        self.K1 = K1

    # -----------------------------------------------------------------------------------------------------------
    def to_modes(self, f):
        """f real [Nr, Nth] -> complex modes [Mm, Nr] (coefficients of e^{i m th}, m = 0..Mm-1)."""
        F = torch.fft.rfft(f, dim=1) / self.Nth
        return F[:, :self.Mm].T.contiguous()

    def to_phys(self, cm):
        full = torch.zeros(self.Nr, self.Nth // 2 + 1, dtype=torch.complex128, device=self.dev)
        full[:, :self.Mm] = cm.T
        return torch.fft.irfft(full, n=self.Nth, dim=1) * self.Nth

    def d_theta(self, f):
        F = torch.fft.rfft(f, dim=1)
        k = torch.arange(self.Nth // 2 + 1, device=self.dev, dtype=torch.float64)
        F = F * (1j * k)[None, :]
        F[:, -1] = 0.0
        return torch.fft.irfft(F, n=self.Nth, dim=1)

    def dx_rho(self, rho):
        rho_r = fd_dlr(rho, self.d) / self.r[:, None]
        rho_t = self.d_theta(rho) / self.r[:, None]
        return self.cos[None, :] * rho_r - self.sin[None, :] * rho_t

    def velocity(self, rho, return_modes=False):
        """Canonical W = U - U(0) for the density rho [Nr, Nth] (growth r^p beyond r_max).  Returns W_r, W_theta [Nr, Nth]."""
        f = self.dx_rho(rho)
        F = self.to_modes(f)                                # [Mm, Nr]
        e2 = torch.exp(2 * self.lr)
        h = F * e2[None, :]
        def mm(K, v):
            return torch.matmul(K, v.real[..., None])[..., 0] + 1j * torch.matmul(K, v.imag[..., None])[..., 0]
        Al = mm(self.Kin, h)                                # [Mm, Nr]
        Ag = mm(self.Kout, h)                               # zero rows for m = 0, 1
        if self.tail2:
            # two-term closure (specification 2): h(v) = alpha e^{(p+1) v} + beta e^{2p v} beyond hi, fitted at v = hi and v1 = hi - 0.5;
            # replace the one-term tail h(hi)/(|m|-1-p) (built into Kout) by alpha e^{(p+1)hi}/(|m|-1-p) + beta e^{2p hi}/(|m|-2p)
            k1 = int(round(0.5 / self.d)); v0 = float(self.lr[-1]); v1 = float(self.lr[-1 - k1])
            h0 = h[:, -1]; h1 = h[:, -1 - k1]
            det = math.exp((self.p + 1) * v0 + 2 * self.p * v1) - math.exp((self.p + 1) * v1 + 2 * self.p * v0)
            alpha = (h0 * math.exp(2 * self.p * v1) - h1 * math.exp(2 * self.p * v0)) / det
            beta = (h1 * math.exp((self.p + 1) * v0) - h0 * math.exp((self.p + 1) * v1)) / det
            a = self.m
            big = a >= 2
            tail1 = torch.where(big, h0 / torch.clamp(a - 1.0 - self.p, min=1e-12), torch.zeros_like(h0))
            tail2 = torch.where(big, alpha * math.exp((self.p + 1) * v0) / torch.clamp(a - 1.0 - self.p, min=1e-12)
                                     + beta * math.exp(2 * self.p * v0) / torch.clamp(a - 2.0 * self.p, min=1e-12), torch.zeros_like(h0))
            decay = torch.exp(-a[:, None] * self.d * (self.Nr - 1 - torch.arange(self.Nr, device=self.dev, dtype=torch.float64))[None, :])
            Ag = Ag + decay * (tail2 - tail1)[:, None]
        hq = F[1] * self.r
        I1 = (self.K1 @ hq.real) + 1j * (self.K1 @ hq.imag)
        Ag = Ag.clone(); Ag[1] = -self.r * I1
        mpos = self.m.clone(); mpos[0] = 1.0
        psi = (Al + Ag) / (2.0 * mpos[:, None])
        dpsi = (-Al + Ag) / (2.0 * self.r[None, :])
        Wr = -1j * self.m[:, None] * psi / self.r[None, :]
        Wt = dpsi.clone()
        Wr[0] = 0.0
        Wt[0] = -Al[0] / self.r
        psi[0] = 0.0
        out = (self.to_phys(Wr), self.to_phys(Wt))
        if return_modes:
            return out + (psi, Wr, Wt)
        return out

    # -----------------------------------------------------------------------------------------------------------
    def interp(self, F, ci, cj, top_rows):
        """Cubic Lagrange interpolation of F [Nr, Nth] at fractional indices (ci, cj) (periodic in j).
        top_rows: [2, Nth] values used for rows Nr, Nr+1 (beyond hi); row -1 is a copy of row 0."""
        Nr, Nth = self.Nr, self.Nth
        Fp = torch.cat([F[:1], F, top_rows], 0)            # rows -1 .. Nr+1  -> index +1
        i0 = torch.floor(ci); t = ci - i0; i0 = i0.long()
        j0 = torch.floor(cj); u = cj - j0; j0 = j0.long()
        i0 = torch.clamp(i0, 0, Nr)                        # stencil rows i0-1 .. i0+2 within -1 .. Nr+1
        t = torch.where((ci - i0.double()) > 1.0, torch.ones_like(t), ci - i0.double())
        def lw(t):
            return (-t * (t - 1) * (t - 2) / 6, (t + 1) * (t - 1) * (t - 2) / 2, -(t + 1) * t * (t - 2) / 2, (t + 1) * t * (t - 1) / 6)
        wi = lw(t); wj = lw(u)
        out = torch.zeros_like(ci)
        for a in range(4):
            ia = (i0 + (a - 1) + 1).clamp(0, Nr + 2)
            rowv = torch.zeros_like(ci)
            for b in range(4):
                jb = torch.remainder(j0 + (b - 1), Nth)
                rowv = rowv + wj[b] * Fp[ia, jb]
            out = out + wi[a] * rowv
        if self.limiter:
            ia0 = (i0 + 1).clamp(0, Nr + 2); ia1 = (i0 + 2).clamp(0, Nr + 2)
            ja0 = torch.remainder(j0, Nth); ja1 = torch.remainder(j0 + 1, Nth)
            c00 = Fp[ia0, ja0]; c01 = Fp[ia0, ja1]; c10 = Fp[ia1, ja0]; c11 = Fp[ia1, ja1]
            lo = torch.minimum(torch.minimum(c00, c01), torch.minimum(c10, c11))
            hi = torch.maximum(torch.maximum(c00, c01), torch.maximum(c10, c11))
            out = torch.minimum(torch.maximum(out, lo), hi)
        return out

    def step(self, g, ds, A, Afun):
        """One semi-Lagrangian step.  A: datum on the grid [Nth]; Afun(theta) evaluates the datum at arbitrary angles."""
        rho = self.r[:, None] ** self.p * g
        Wr, Wt = self.velocity(rho)
        ar = self.cl + Wr / self.r[:, None]
        at = Wt / self.r[:, None]
        src = self.p * Wr / self.r[:, None]
        top2 = lambda X: X[-1:].expand(2, -1)
        ci0 = self.ii + 0.5 * ds * ar / self.d
        cj0 = self.jj + 0.5 * ds * at / self.dth
        arm = self.interp(ar, ci0, cj0, top2(ar)); atm = self.interp(at, ci0, cj0, top2(at)); srm = self.interp(src, ci0, cj0, top2(src))
        ci = self.ii + ds * arm / self.d
        cj = self.jj + ds * atm / self.dth
        gn = self.interp(g, ci, cj, A[None, :].expand(2, -1)) * torch.exp(ds * srm)
        out = ci > self.Nr - 1
        if out.any():
            gn = torch.where(out, Afun((cj + self.thshift) * self.dth), gn)
        return gn, (Wr, Wt)

    # -----------------------------------------------------------------------------------------------------------
    def node_matrix(self, ar_row, at_row):
        """Fit V = M X on a ring: V_r/r = n.M n, V_th/r = t.M n."""
        c, s = self.cos, self.sin
        rows = torch.stack([c * c, c * s, s * c, s * s], 1)          # n (x) n
        rows2 = torch.stack([-s * c, -s * s, c * c, c * s], 1)       # t (x) n
        Amat = torch.cat([rows, rows2], 0); b = torch.cat([ar_row, at_row], 0)
        M = torch.linalg.lstsq(Amat, b[:, None]).solution[:, 0].reshape(2, 2)
        return M

    def diagnostics(self, g, Wr=None, Wt=None, krings=(8, 20, 40)):
        rho = self.r[:, None] ** self.p * g
        if Wr is None:
            Wr, Wt = self.velocity(rho)
        ar = self.cl + Wr / self.r[:, None]; at = Wt / self.r[:, None]
        out = {}
        for k in krings:
            M = self.node_matrix(ar[k], at[k])
            Ms = 0.5 * (M + M.T); ev, evec = torch.linalg.eigh(Ms)
            e1 = evec[:, 0]
            ang = math.degrees(math.atan2(float(e1[1]), float(e1[0]))) % 180
            out['ring%d' % k] = dict(r=float(self.r[k]), M=[round(float(v), 6) for v in M.flatten()], m1=round(float(ev[0]), 6),
                                     m2=round(float(ev[1]), 6), e1_deg=round(ang, 3), antisym=round(float(M[1, 0] - M[0, 1]), 6))
        # strain moments (exact identities I2): c = psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX, d = psi_xx(0) = (1/pi) int rho r^-3 cos 3th dX
        w = (self.r ** (-1))[:, None] * self.d * self.dth / math.pi            # dX r^-3 = r^-1 dlr dth
        c_grid = float((rho * torch.sin(3 * self.th)[None, :] * w).sum())
        d_grid = float((rho * torch.cos(3 * self.th)[None, :] * w).sum())
        # outer tail rho ~ r^p A(th): int_{rmax}^inf r^{p-2} dr = rmax^{p-1}/(1-p)
        A_end = g[-1]
        a3s = float((A_end * torch.sin(3 * self.th)).sum() * self.dth / math.pi)
        a3c = float((A_end * torch.cos(3 * self.th)).sum() * self.dth / math.pi)
        rmax = float(self.r[-1]); tail = rmax ** (self.p - 1) / (1 - self.p)
        out['c_moment'] = c_grid + a3s * tail; out['c_moment_tail'] = a3s * tail
        out['d_moment'] = d_grid + a3c * tail
        out['c_target'] = self.cl - 0.5
        # stationarity residual of the ORIGINAL equation V.grad rho - rho, relative to rho scale per radial band
        rho_lr = fd_dlr(rho, self.d); rho_t = self.d_theta(rho)
        Vr = self.cl * self.r[:, None] + Wr; Vt = Wt
        Rres = Vr * rho_lr / self.r[:, None] + Vt * rho_t / self.r[:, None] - rho
        scale = rho.abs().max(dim=1).values + 1e-300
        rel = Rres.abs().max(dim=1).values / scale
        bands = {}
        for lo_, hi_ in ((1e-4, 1e-2), (1e-2, 1), (1, 1e2), (1e2, 1e4)):
            msk = (self.r >= lo_) & (self.r < hi_)
            if msk.any():
                bands['%g-%g' % (lo_, hi_)] = float(rel[msk].max())
        out['R_rel_bands'] = bands
        out['gmin'] = float(g.min()); out['gmax'] = float(g.max())
        # crease diagnostic (x-even states): kappa(r) = rho on the x axis / (Q0 r^2), Q0 from the off-axis x^2 law on 30 < |th| < 60 deg;
        # kappa = 1 means the node is the smooth x^2 jet; kappa != 1 means a crease (layer) along the weak axis.
        thn = self.th.cpu().numpy(); cs2 = np.cos(thn) ** 2
        band = (np.abs(np.cos(thn)) > 0.5) & (np.abs(np.cos(thn)) < 0.87)
        axis = np.argsort(np.minimum(np.abs(np.angle(np.exp(1j * thn))), np.abs(np.angle(np.exp(1j * (thn - math.pi))))))[:2]
        kap = {}
        rn = self.r.cpu().numpy(); rho_n = rho.cpu().numpy()
        for rt in (1e-4, 1e-3, 3e-3, 1e-2, 1e-1):
            k = int(np.argmin(np.abs(rn - rt)))
            Q0 = np.mean(rho_n[k, band] / (rn[k] ** 2 * cs2[band]))
            kap['%g' % rt] = float(np.mean(rho_n[k, axis] / (rn[k] ** 2 * cs2[axis])) / Q0)
        out['kappa_axis'] = kap
        return out


# ---------------------------------------------------------------------------------------------------------------
def run(args):
    dev = 'cuda'
    p = args['p']
    table = None
    if args['kind'] == 'table':
        dd = np.load(args['Afile']); table = (dd['thA'], dd['A'])
    par = args['par']
    if args['kind'] in ('fourier', 'expf'):
        par = [float(v) for v in str(args['par']).split(':')]
    if args.get('restart'):
        dd = np.load(args['restart'])
        g0 = torch.tensor(dd['g'], device=dev); lr0 = dd['lr']
        Nr, Nth = g0.shape
        lo, hi = float(lr0[0]), float(lr0[-1])
        S = PFwd(Nr, Nth, lo, hi, p, dev=dev, limiter=bool(args['limiter']), thshift=args.get('thshift', 0.0), tail2=bool(args.get('tail2', 0)))
        g = g0
    else:
        Nr, Nth, lo, hi = args['Nr'], args['Nth'], args['lo'], args['hi']
        S = PFwd(Nr, Nth, lo, hi, p, dev=dev, limiter=bool(args['limiter']), thshift=args.get('thshift', 0.0), tail2=bool(args.get('tail2', 0)))
        A = datum(S.th, args['kind'], par, table)
        g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
    A = datum(S.th, args['kind'], par, table)
    Afun = lambda th: datum(th, args['kind'], par, table)
    ds = args['ds']; hist = []; t0 = time.time()
    for n in range(args['nsteps']):
        gn, (Wr, Wt) = S.step(g, ds, A, Afun)
        dg = float((gn - g).abs().max()) / ds
        g = gn
        if n % args['every'] == 0 or n == args['nsteps'] - 1:
            dgn = S.diagnostics(g)
            rec = dict(n=n, s=round((n + 1) * ds, 4), dgds=dg, wall=round(time.time() - t0, 1))
            rec.update(dgn)
            hist.append(rec)
            r20 = rec['ring20']
            print(json.dumps(dict(n=n, s=rec['s'], dgds='%.2e' % dg, m1=r20['m1'], m2=r20['m2'], e1=r20['e1_deg'],
                                  c_mom=round(rec['c_moment'], 5), c_tgt=round(rec['c_target'], 5), d_mom=round(rec['d_moment'], 5),
                                  Rrel=rec['R_rel_bands'], wall=rec['wall'])), flush=True)
            np.savez(args['out'], g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), hist=json.dumps(hist),
                     args=json.dumps(args))
    return g, S, hist


if __name__ == '__main__':
    args = dict(p=0.5, Nr=661, Nth=256, lo=-12.0, hi=10.0, kind='cos2', par=0.0, ds=0.02, nsteps=3000, every=250,
                out='runs/pfwd/test.npz', restart='', Afile='', limiter=1, thshift=0.0, tail2=0)
    for a in sys.argv[1:]:
        k, v = a.split('=', 1)
        if k in ('Nr', 'Nth', 'nsteps', 'every', 'limiter', 'tail2'):
            args[k] = int(v)
        elif k in ('kind', 'out', 'restart', 'Afile'):
            args[k] = v
        elif k == 'par' and ':' in v:
            args[k] = v
        else:
            args[k] = float(v)
    print(json.dumps(args), flush=True)
    run(args)
