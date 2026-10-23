"""qdiag.py -- diagnostics for a saved state (Q/QL representation: keys beta, cl, N, M, L, Lf, gK; or ipm3 representation: keys b,
cl, gamma, N, M, L, p, mu) as requested by SPEC v9 Section 9 and the lead's notes of 17:11Z, 17:38Z, 18:01Z, 18:06Z, 18:21Z:
  * between-node residual tables by region with the maximizing coordinates: max|R| (absolute), max|R|/N_f, max|R|/N_v;
  * G6 energy margins: Rg = max|grad rho|, V = max|DU|_F (DU by central differences of the evaluated U, h = 1e-5 r), the margins
    m2 = 2V + Rg - (c_l - 1) and m3 = 3V + Rg + 3(2 + sqrt2) sqrt(V Rg) - (2 c_l - 1) (exact profiles have both >= 0);
  * G2: Theta0(th) = lim r^-gamma rho(r, th), min Theta0/sin th, min over [delta, pi/2] of |Theta0| + |Theta0'| (delta = 0.01) with
    location; convergence of r^-gamma rho to Theta0 at two finite outer radii; min over the grid of rho/(a0 y) = w b/a0;
  * strain moment int_0^inf rho_3 r^-2 dr computed from the EVALUATED rho (angular quadrature at 64 angles, Gauss-Legendre in t),
    compared with c + a0/4 (modal c) and with 1 - c_l + a0/4 (what an exact profile needs);
  * G1/G3: x-axis functions w(x) = W_1(x,0)/(c_l x) and g(x) = rho_y(x,0)/a0 on a dense radial set: minima, sign changes; off-axis
    min |W|/(c_l r) (search for other zeros of W);
  * a0, c, c_l + c - 1, a0/D, a0/4A, K, L_can, between-node tables.
Everything is evaluated from the spectral representation between nodes (midpoints in t and in theta plus near-axis angles, section 7
of NUM_REPORT).  usage: python3 src/qdiag.py state.pt [label]"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q, ipm3ql
from ipm3 import interp_matrix
torch.set_default_dtype(torch.float64); dev = 'cuda' if torch.cuda.is_available() else 'cpu'
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


class State:
    """uniform access to a saved state of either representation."""
    def __init__(self, path):
        st = torch.load(path, weights_only=False); self.st = st; self.path = path
        self.cl = float(st['cl']); self.N, self.M, self.L = int(st['N']), int(st['M']), float(st['L'])
        self.gamma = 1.0 / self.cl
        self.mu = st.get('mu', None)
        if 'beta' in st and hasattr(st['beta'], 'shape'):
            self.rep = 'Q'
            self.Lf = float(st.get('Lf', self.L)); self.gK = float(st.get('gK', float('nan')))
            p_saved = float(st['p']) if 'p' in st else None
            p_rebuilt = 1.0 / (1.0 - self.gamma)
            self.frozen = p_saved is not None and abs(p_saved - p_rebuilt) > 1e-8 * p_rebuilt
            if self.frozen:   # frozen-map state (4K(b)): evaluate the SAVED function (map power p_saved, far-field exponent 1 - 1/p_saved), residual with its c_l
                print(f"NOTE: frozen-map state: saved p = {p_saved:.6f} (exponent {1 - 1/p_saved:.6f}) vs 1/c_l = {self.gamma:.6f}; evaluating the saved function on its own map")
                self.mdl = ipm3ql.IPM3QL(N=self.N, M=self.M, L=self.L, gamma=1 - 1 / p_saved, p=p_saved, device=dev, Lf=self.Lf)
                self.gamma = 1 - 1 / p_saved
            else:
                self.mdl = ipm3ql.IPM3QL(N=self.N, M=self.M, L=self.L, gamma=self.gamma, device=dev, Lf=self.Lf)
            self.coef = st['beta'].to(dev)
            self.flds = self.mdl.fields(self.coef)
            self.a0 = self.coef[0, 0].item()
            bk1 = (self.mdl.rad.ext1_R @ self.coef).reshape(-1)                      # beta_k(1) = b_k(1) (sigma = 1)
            self.bk_inf = bk1.cpu().numpy()
            self.wfac_inf = 0.5 * self.L ** (1 - self.gamma)                             # r^-gamma rho -> wfac * b(1,th) sin th
            self.K = self.wfac_inf * (self.bk_inf * np.cos(np.pi * np.arange(self.M))).sum()
            b, _, _ = self.mdl.b_values(self.coef); self.b_nodes = b; self.w_nodes = self.mdl.rad.wR
            self.p = self.mdl.p
            self.g_of_t = lambda t: (1 - t ** 2) / ((1 - t) / 2 + self.p * (1 + t))
            self.phi = lambda r: (1 + r ** 2 / self.Lf ** 2) ** (-2)
        else:
            self.rep = 'ipm3'
            self.Lf = float(st.get('Lf', self.L)); self.gK = float('nan')          # eps-continuation states save Lf = eps (referee (e2) item 7)
            self.mdl = ipm3.IPM3(N=self.N, M=self.M, L=self.L, gamma=self.gamma, device=dev)
            self.mdl.rad.rmap_np = self.mdl.rad.rmap                                        # pure arithmetic, works on numpy arrays
            self.coef = st['b'].to(dev)
            self.flds = self.mdl.fields(self.coef)
            self.a0 = self.coef[0, 0].item()
            bhat = self.mdl.ang.to_coef(self.coef, 'EE')
            self.bk_inf = (self.mdl.rad.ext1_R @ bhat).reshape(-1).cpu().numpy()
            self.wfac_inf = self.L ** (1 - self.gamma)
            self.K = self.wfac_inf * (self.bk_inf * np.cos(np.pi * np.arange(len(self.bk_inf)))).sum()
            self.b_nodes = self.coef; self.w_nodes = self.mdl.wR
            self.p = self.mdl.p
            self.g_of_t = lambda t: (1 - t ** 2) / ((1 - t) + self.p * (1 + t))
            self.phi = lambda r: (1 + r ** 2 / self.Lf ** 2) ** (-2)
        self.c = self.mdl.psi_xy0(self.flds).item()
        self.rad = self.mdl.rad

    def ev(self, r, th):
        return self.mdl.evaluate(self.coef, self.cl, self.flds, r, th)

    def ev_xy(self, x, y):
        r = np.hypot(x, y); th = np.arctan2(y, x)
        return self.ev(r, th)

    def theta0(self, th):
        """Theta0(th) and Theta0'(th) from the far-field coefficients."""
        k = np.arange(len(self.bk_inf))
        bb = (self.bk_inf[None, :] * np.cos(2 * np.outer(th, k))).sum(1)
        bb_th = -(self.bk_inf[None, :] * 2 * k[None, :] * np.sin(2 * np.outer(th, k))).sum(1)
        T0 = self.wfac_inf * bb * np.sin(th); T0p = self.wfac_inf * (bb_th * np.sin(th) + bb * np.cos(th))
        return T0, T0p, self.wfac_inf * bb


RMAX = 1e120                                                                                   # radii beyond this are not evaluated (float range)

def eval_set(S):
    tR = S.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); tt = np.sort(np.concatenate([tR[1:], tm]))
    rr = S.rad.rmap_np(tt); keep = rr < RMAX; tt, rr = tt[keep], rr[keep]                      # overflow guard for maps with p >> 1 (c_l near 1)
    th = S.mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    extra = np.array([th[0] / 4, th[0] / 2, (th[-1] + np.pi / 2) / 2, np.pi / 2 - (np.pi / 2 - th[-1]) / 4, np.pi / 2])
    tha = np.sort(np.concatenate([thm, extra, th]))
    RR, TT = np.meshgrid(rr, tha, indexing='ij')
    return RR, TT


def region_table(S, RR, TT, out, mu):
    phi = S.phi(RR); Rf = out['R'] - (mu * out['y'] * phi if mu else 0.0)
    bins = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e8), (1e8, 1e300)]
    lines = []
    for lo, hi in bins:
        m = (RR >= lo) & (RR < hi)
        if not m.any(): continue
        A = np.abs(Rf); qf = A / out['Nf']; qv = A / out['Nv']
        def arg(Z):
            Zm = np.where(m, Z, -1.0); i = np.unravel_index(np.argmax(Zm), Z.shape); return Zm[i], RR[i], TT[i]
        a, ra, tha = arg(A); f, rf, thf = arg(qf); v, rv, thv = arg(qv)
        lines.append(f"    r in [{lo:g},{hi:g}): max|R| {a:.2e} at (r={ra:.3g}, th={tha:.3f}); max|R|/Nf {f:.2e} at (r={rf:.3g}, th={thf:.3f}); "
                     f"max|R|/Nv {v:.2e} at (r={rv:.3g}, th={thv:.3f})")
    return lines


def energy(S, RR, TT, out):
    x, y = out['x'], out['y']; h = 1e-5 * RR
    ep = S.ev_xy(x + h, y); em = S.ev_xy(x - h, y); fp = S.ev_xy(x, y + h); fm = S.ev_xy(x, y - h)
    U1x = (ep['U1'] - em['U1']) / (2 * h); U2x = (ep['U2'] - em['U2']) / (2 * h)
    U1y = (fp['U1'] - fm['U1']) / (2 * h); U2y = (fp['U2'] - fm['U2']) / (2 * h)
    DU = np.sqrt(U1x ** 2 + U1y ** 2 + U2x ** 2 + U2y ** 2)
    div = np.abs(U1x + U2y); curl_err = np.abs((U2x - U1y) + out['rho_x'])
    G = np.sqrt(out['rho_x'] ** 2 + out['rho_y'] ** 2)
    iG = np.unravel_index(np.argmax(G), G.shape); iV = np.unravel_index(np.argmax(DU), DU.shape)
    Rg, V = G[iG], DU[iV]
    m2 = 2 * V + Rg - (S.cl - 1); m3 = 3 * V + Rg + 3 * (2 + math.sqrt(2)) * math.sqrt(V * Rg) - (2 * S.cl - 1)
    # DU at the origin from the evaluated field: should be diag(-c, c)
    e0 = S.ev_xy(np.array([1e-6, -1e-6, 0.0, 0.0]), np.array([0.0, 0.0, 1e-6, -1e-6]))
    c_fd = -(e0['U1'][0] - e0['U1'][1]) / 2e-6
    return dict(Rg=Rg, locG=(RR[iG], TT[iG]), V=V, locV=(RR[iV], TT[iV]), m2=m2, m3=m3, divmax=div.max(), curlmax=curl_err.max(),
                curlrel=(curl_err / (np.abs(out['rho_x']) + 1e-300 + DU)).max(), c_fd=c_fd)


def strain_contrast_weighted(S, RR, TT, out):
    """lead 19:45Z (1): sigma = sup |sym DU|_op with location, M = sup(-X.U/r^2), sigma/D; lead 19:19Z: A(q) = int osc_th q dr/r, q = rho/(a0 y),
    over the sampled radii (log-spaced, trusted range r < RMAX); lead 19:45Z (2): weighted residual E_m = ||R - a0 delta y||_m / ||h||_m with
    h = rho - a0 y, ||g||_m^2 = int |g|^2 r^-2m dX, m = 2.5, 3, 3.5, and the three terms ((m-1) c_l - 1)||h||^2, m int (X.U/r^2) h^2 r^-2m,
    a0 int v_2 h r^-2m (v = U - (-c x, c y)).  All sampled / quadrature estimates on r < RMAX."""
    x, y = out['x'], out['y']; h = 1e-5 * RR
    ep = S.ev_xy(x + h, y); em = S.ev_xy(x - h, y); fp = S.ev_xy(x, y + h); fm = S.ev_xy(x, y - h)
    U1x = (ep['U1'] - em['U1']) / (2 * h); U2x = (ep['U2'] - em['U2']) / (2 * h); U1y = (fp['U1'] - fm['U1']) / (2 * h); U2y = (fp['U2'] - fm['U2']) / (2 * h)
    a, d, b = U1x, U2y, 0.5 * (U1y + U2x)
    Sop = np.abs((a + d) / 2) + np.sqrt(((a - d) / 2) ** 2 + b ** 2)                       # operator norm of the symmetric 2x2 matrix
    iS = np.unravel_index(np.argmax(Sop), Sop.shape)
    XU = -(x * out['U1'] + y * out['U2']) / RR ** 2; iM = np.unravel_index(np.argmax(XU), XU.shape)
    D = S.cl - 1
    res = dict(sigma=Sop[iS], sigma_loc=(RR[iS], TT[iS]), sigma_over_D=Sop[iS] / D, M=XU[iM], M_loc=(RR[iM], TT[iM]), sigma0=math.sqrt(2) * abs(S.c) / math.sqrt(2))
    # A(q): osc over the sampled angles at each sampled radius, trapezoid in log r
    q = out['rho'] / (S.a0 * out['y']); osc = q.max(axis=1) - q.min(axis=1); lr = np.log(RR[:, 0])
    A = np.trapz(osc, lr); res.update(Aq=A, Aq_range=(RR[0, 0], RR[-1, 0]), Aq_tail_osc=osc[-1], DA_test=(abs(D / S.a0 - 0.25), 0.4135 * A))
    # weighted residual: GL in t x 64 angles
    nq, Mq = 300, 64
    tq, wq = np.polynomial.legendre.leggauss(nq); tmax = S.rad.t_of_r(np.array([RMAX]))[0]; tmin = S.rad.t_of_r(np.array([1e-40]))[0]   # r^-2m overflows below ~1e-40
    wq = wq * (tmax - tmin) / 2; tq = tmin + (tq + 1) * (tmax - tmin) / 2
    rq = S.rad.rmap_np(tq); thq = (np.arange(Mq) + 0.5) * np.pi / (2 * Mq); Rq, Tq = np.meshgrid(rq, thq, indexing='ij'); o = S.ev(Rq, Tq)
    g = S.g_of_t(tq)                                                                         # r dt/dr ; dX = r dr dth = r^2 (dt/g) dth, quadrant x 4
    dX = (4 * (np.pi / (2 * Mq))) * (Rq ** 2 * (wq / g)[:, None])
    hq = o['rho'] - S.a0 * o['y']; delta = S.cl + S.c - 1; Rres = o['R'] - S.a0 * delta * o['y']
    XUq = (o['x'] * o['U1'] + o['y'] * o['U2']) / Rq ** 2; v2 = o['U2'] - S.c * o['y']
    out_m = {}
    for m in (2.5, 3.0, 3.5):
        wgt = Rq ** (-2 * m) * dX
        nh2 = (hq ** 2 * wgt).sum(); nR2 = (Rres ** 2 * wgt).sum()
        T1 = ((m - 1) * S.cl - 1) * nh2; T2 = m * (XUq * hq ** 2 * wgt).sum(); T3 = S.a0 * (v2 * hq * wgt).sum()
        # radius where the weighted mass of h sits: median of the cumulative distribution in log r
        mass = (hq ** 2 * wgt).sum(axis=1); cum = np.cumsum(mass) / mass.sum(); rmed = rq[np.searchsorted(cum, 0.5)]
        out_m[m] = dict(Em=math.sqrt(nR2 / nh2) if nh2 > 0 else float('nan'), nh=math.sqrt(nh2), T1_over_nh2=T1 / nh2, T2_over_nh2=T2 / nh2, T3_over_nh2=T3 / nh2, rmed=rmed,
                        bound=(m - 1) * S.cl - 1 - m * res['sigma'])
    res['weighted'] = out_m
    return res


def strain_moment(S, nq=400, Mq=64):
    tq, wq = np.polynomial.legendre.leggauss(nq)
    tmax = S.rad.t_of_r(np.array([RMAX]))[0]                                                     # integrate over r < RMAX only (tail of rho_3 r^-2 negligible)
    wq = wq * (tmax + 1) / 2; tq = -1 + (tq + 1) * (tmax + 1) / 2
    rq = S.rad.rmap_np(tq); thq = (np.arange(Mq) + 0.5) * np.pi / (2 * Mq)
    RR, TT = np.meshgrid(rq, thq, indexing='ij'); out = S.ev(RR, TT)
    rho3 = (2.0 / Mq) * (out['rho'] * np.sin(3 * TT)).sum(1)                   # sin 3th coefficient of rho (odd modes orthogonal on (0,pi/2))
    rho1 = (2.0 / Mq) * (out['rho'] * np.sin(TT)).sum(1)
    g = S.g_of_t(tq)                                                              # r dt/dr
    integrand = rho3 / rq / g                                                     # rho_3 r^-2 dr = (rho_3/r) dt/g
    mom = (wq * integrand).sum()
    neg = (wq * np.minimum(integrand, 0)).sum()
    return mom, neg, rho3, rho1, rq


def axis_scan(S, RR):
    rr = RR[:, 0]
    out = S.ev(rr, np.zeros_like(rr))
    wfun = out['W1'] / (S.cl * rr); gfun = out['rho_y'] / S.a0
    def signch(f):
        s = np.sign(f); idx = np.where(s[:-1] * s[1:] < 0)[0]; return [rr[i] for i in idx]
    return dict(wmin=(wfun.min(), rr[np.argmin(wfun)]), gmin=(gfun.min(), rr[np.argmin(gfun)]), wzeros=signch(wfun), gzeros=signch(gfun),
                w_dxU1_0=None)


def main(path, label=None):
    S = State(path); label = label or path
    t0 = time.time()
    RR, TT = eval_set(S); out = S.ev(RR, TT)
    mu = S.mu if (S.mu is not None) else 0.0
    D = S.cl - 1; A = 2 * S.cl - 1
    Lcan = (S.K / S.a0) ** (S.cl / D) if S.K / S.a0 > 0 else float('nan')
    lines = [f"QDIAG {now()} {label} [{S.rep}] N={S.N} M={S.M} L={S.L} Lf={S.Lf} gK={S.gK} mu={S.mu}",
             f"  c_l={S.cl:.10f} D={D:.6g} a0={S.a0:.10f} a0/D={S.a0/D:.4f} a0/4A={S.a0/(4*A):.4f} c(modal)={S.c:+.10f} c_l+c-1={S.cl+S.c-1:+.3e} "
             f"(forced Delta=mu/a0={mu/S.a0:+.3e}) K={S.K:.8g} L_can={Lcan:.6g}"]
    lines.append("  between-node residual tables (unforced R; for forced states R_f = R - mu y phi):")
    lines += region_table(S, RR, TT, out, mu)
    # also report the FORCING-free residual for forced states: max |R| itself
    E = energy(S, RR, TT, out)
    lines.append(f"  G6 energy: Rg=max|grad rho|={E['Rg']:.6g} at (r={E['locG'][0]:.3g}, th={E['locG'][1]:.3f}); V=max|DU|_F={E['V']:.6g} at "
                 f"(r={E['locV'][0]:.3g}, th={E['locV'][1]:.3f}); m2=2V+Rg-(c_l-1)={E['m2']:+.6g}; m3=3V+Rg+3(2+sqrt2)sqrt(V Rg)-(2c_l-1)={E['m3']:+.6g}; "
                 f"FD checks: max|div U|={E['divmax']:.1e}, max|curl U + rho_x|/(|rho_x|+|DU|)={E['curlrel']:.1e}, c from the secant of U1 at x = +-1e-6 (a Taylor-regime estimate only where r = 1e-6 is inside the origin scale): {E['c_fd']:+.8f}")
    # Theta0
    th = np.linspace(1e-4, np.pi / 2, 4001); T0, T0p, T0s = S.theta0(th)
    i_s = np.argmin(T0s); m_s = (th >= 0.01); comb = np.abs(T0) + np.abs(T0p); i_c = np.argmin(np.where(m_s, comb, np.inf))
    nz = []
    sgn = np.sign(T0); idx = np.where(sgn[:-1] * sgn[1:] < 0)[0]
    for i in idx: nz.append((th[i], T0p[i]))
    lines.append(f"  G2 Theta0 (from b(t=1,.)): min Theta0/sin th = {T0s[i_s]:.6g} at th={th[i_s]:.4f}; min_[0.01,pi/2] |Theta0|+|Theta0'| = {comb[i_c]:.6g} at th={th[i_c]:.4f}; "
                 f"Theta0(pi/2)=K={T0[-1]:.6g}; Theta0'(0)={T0p[0]:.6g}; zeros of Theta0 in (0,pi/2): {[(round(a,4), round(b,4)) for a,b in nz] if nz else 'none'}")
    # convergence of r^-gamma rho to Theta0 at finite radii
    for j in (S.N - 1, S.N - 3, S.N - 6):
        r_j = S.rad.rmap_np(S.rad.tR_np[j])
        if not (r_j < RMAX): lines.append(f"    node {j}: r = {r_j:.3g} beyond the evaluation range"); continue
        thj = np.linspace(0.02, np.pi / 2, 200); o = S.ev(np.full_like(thj, r_j), thj)
        T0j = o['rho'] / r_j ** S.gamma; T0e, _, _ = S.theta0(thj)
        lines.append(f"    r^-gamma rho at node r={r_j:.3g} vs Theta0: max rel dev {np.max(np.abs(T0j - T0e))/np.max(np.abs(T0e)):.2e}")
    # min rho/(a0 y) on nodes
    ratio = (S.w_nodes[:, None] * S.b_nodes / S.a0).cpu().numpy(); i_r = np.unravel_index(np.argmin(ratio), ratio.shape)
    qq = out['rho'] / (S.a0 * out['y']); iq = np.unravel_index(np.argmax(qq), qq.shape)
    lines.append(f"  CAP DIAGNOSTIC q = rho/(a0 y) on the between-node set: max q - 1 = {qq[iq] - 1:+.3e} at (r={RR[iq]:.3g}, th={TT[iq]:.3f}); min q = {qq.min():.6g} (sampled)")
    lines.append(f"  min over nodes of rho/(a0 y) = w b/a0 = {ratio[i_r]:.6g} at (r={S.rad.rR[i_r[0]].item():.3g}, th={S.mdl.ang.theta_np[i_r[1]]:.3f}); "
                 f"min over the between-node set of rho/(a0 y) = {np.min(out['rho']/(S.a0*out['y'])):.6g}")
    # strain moment
    mom, neg, rho3, rho1, rq = strain_moment(S)
    lines.append(f"  strain moment int rho_3 r^-2 dr (evaluated rho, GL 400 x 64 angles) = {mom:+.8f}; negative part = {neg:+.4e}; "
                 f"c(modal) + a0/4 = {S.c + S.a0/4:+.8f} (difference {mom - S.c - S.a0/4:+.1e}); exact profile needs 1 - c_l + a0/4 = {1 - S.cl + S.a0/4:+.8f} "
                 f"(defect {mom - (1 - S.cl + S.a0/4):+.3e}); max|rho_3|/max|rho_1| = {np.abs(rho3).max()/np.abs(rho1).max():.3e}")
    # axis
    ax = axis_scan(S, RR)
    lines.append(f"  G1/G3 x-axis: min W_1(x,0)/(c_l x) = {ax['wmin'][0]:.6g} at x={ax['wmin'][1]:.3g}; min rho_y(x,0)/a0 = {ax['gmin'][0]:.6g} at x={ax['gmin'][1]:.3g}; "
                 f"sign changes DETECTED between adjacent samples (tangential/flat zeros not detectable) of w: {[f'{v:.3g}' for v in ax['wzeros']] or 'none'}; of g: {[f'{v:.3g}' for v in ax['gzeros']] or 'none'}")
    Wn = np.hypot(out['W1'], out['W2']) / (S.cl * RR); iW = np.unravel_index(np.argmin(Wn), Wn.shape)
    lines.append(f"  off-axis min |W|/(c_l r) over the between-node set = {Wn[iW]:.6g} at (r={RR[iW]:.3g}, th={TT[iW]:.3f}) (1 means U negligible; a zero of W would show as ~0)")
    # sign pattern of rho_x on Q1
    rx = out['rho_x']; lines.append(f"  sign of rho_x on Q1 (between-node set): fraction negative {np.mean(rx < 0):.3f}, min rho_x = {rx.min():.4g} at "
                                      f"(r={RR[np.unravel_index(np.argmin(rx), rx.shape)]:.3g}, th={TT[np.unravel_index(np.argmin(rx), rx.shape)]:.3f}), max rho_x = {rx.max():.4g}")
    try:
        W = strain_contrast_weighted(S, RR, TT, out)
        lines.append(f"  STRAIN SUP: sigma = sup|sym DU|_op (sampled) = {W['sigma']:.6g} at (r={W['sigma_loc'][0]:.3g}, th={W['sigma_loc'][1]:.3f}); sigma/D = {W['sigma_over_D']:.4g}; |sym DU(0)|_op = |c| = {abs(S.c):.6g}; "
                     f"M = sup(-X.U/r^2) (sampled) = {W['M']:.6g} at (r={W['M_loc'][0]:.3g}, th={W['M_loc'][1]:.3f}); 3 sigma + (25/7)|a0| - (2 c_l - 1) = {3*W['sigma'] + 25/7*abs(S.a0) - (2*S.cl-1):+.4g} (sampled; a negative value does not exclude)")
        lines.append(f"  ANGULAR CONTRAST (sampled): A(q) = int osc_th(rho/(a0 y)) dr/r over r in [{W['Aq_range'][0]:.2g}, {W['Aq_range'][1]:.2g}] (log-spaced sample radii) = {W['Aq']:.5g}; osc at the last radius {W['Aq_tail_osc']:.2e}; "
                     f"|D/a0 - 1/4| = {W['DA_test'][0]:.4g} vs 0.4135 A(q) = {W['DA_test'][1]:.4g}")
        for m, d in W['weighted'].items():
            lines.append(f"  WEIGHTED m={m}: E_m = ||R - a0 delta y||_m/||h||_m = {d['Em']:.4g}; terms/||h||^2: ((m-1)c_l - 1) = {d['T1_over_nh2']:+.4g}, m int (X.U/r^2) h^2 r^-2m = {d['T2_over_nh2']:+.4g}, a0 int v_2 h r^-2m = {d['T3_over_nh2']:+.4g}; "
                         f"lower bound (m-1)c_l - 1 - m sigma = {d['bound']:+.4g}; ||h||_m = {d['nh']:.3g}; median radius of the weighted mass of h: {d['rmed']:.3g}  (quadrature on r < {RMAX:.0e})")
    except Exception as e:
        lines.append(f"  STRAIN/CONTRAST/WEIGHTED: failed ({type(e).__name__}: {e})")
    lines.append(f"  ({time.time()-t0:.0f} s)")
    txt = "\n".join(lines); print(txt, flush=True)
    import os; base = os.path.basename(path).replace('.pt', '')
    with open(f'runs/qdiag_{base}.txt', 'a') as f: f.write(txt + "\n")
    return S, out


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
