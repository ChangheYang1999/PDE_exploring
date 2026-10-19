"""Independent evaluator for states saved by the numerical researcher (numerics, runs/*.pt, formulation 'zeta').

Only the published data format is used (no numerics code is imported or copied):
    zeta(r, th) = sum_{|m| <= M} r^{kappa_m} q_m(xi(r)) e^{i m th},   q_{-m} = conj(q_m),  M = Nth//2 - 1,
    (args prefactor 's', numerical record R15: (r/sqrt(1+r^2))^{kappa_m} in place of r^{kappa_m})
    xi = log(1 + r^2/L^2),  x = 2 xi/xi_max - 1,  xi_max = log(1 + R^2/L^2),
    q_m = polynomial of degree N = Nr - 1 in x given by its values at x_j = cos(2 pi j/(2N+1)), j = 0..N (x_0 = 1 <-> r = R),
    kappa_m = |m| for |m| <= K, else K or K+1 with the parity of |m| - K;   rho = zeta^2 inside r <= R;
    tail 'power2': beyond R, rho_m(r) = a_m r^p + b_m r^(2p-1), p = 1/c_l, (a_m, b_m) matched to rho_m at r = R and at the node
    nearest 0.6 R (modes |m| <= M of zeta^2).
    Forced continuation in c_l (args cl_path): the state solves Rz = V.grad zeta - zeta/2 = lam f0 on r <= R, f0 = Rz of the
    seed zeta0 = x (1 + ay y/<r>) <r>^(p0/2 - 1) at c_l0 (p0 = 1/c_l0); jet zeta = x + O(r^2); compat c_l = 1/2 + psi_xy(0).
Own methods: q_m by an exact Chebyshev fit at the nodes (chebvander solve) and Clenshaw evaluation; my composite
Gauss-Legendre panel grid (R is a panel edge), rho extended beyond R by the tail model up to Lmax and integrated numerically;
velocity W = U - U(0) and c = psi_xy(0), b = psi_yy(0) from code/charsolve.py (exact radial Green's function per Fourier
mode); grad zeta by PolarGrid.grad (panel polynomials in r, Fourier in th).
usage: python3 tests/cand_eval.py STATE.pt [nt] [ratio_in] [Lmax]"""
import numpy as np, torch, sys, math, json
sys.path.insert(0, 'code')
from charsolve import CharSolver, lagrange_eval
dev = 'cuda'; DT = torch.float64


def kappa_rule(m, K):
    m = abs(m)
    if m <= K:
        return m
    return K if (m - K) % 2 == 0 else K + 1


class ZetaRep:
    def __init__(self, st):
        a = st['args']
        self.Nr, self.Nth, self.R, self.L, self.K = int(a['Nr']), int(a['Nth']), float(a['R']), float(a['L']), int(a['K'])
        self.M = self.Nth//2 - 1
        q = st['q'].detach().cpu().numpy() if torch.is_tensor(st['q']) else np.asarray(st['q'])
        assert q.shape == (self.M + 1, self.Nr), q.shape
        self.kap = np.array([kappa_rule(m, self.K) for m in range(self.M + 1)], float)
        kf = np.asarray(st['kappa'].cpu() if torch.is_tensor(st['kappa']) else st['kappa'], float)
        assert np.allclose(kf, self.kap), (kf, self.kap)
        N = self.Nr - 1
        self.xn = np.cos(2*np.pi*np.arange(self.Nr)/(2*N + 1))
        self.xi_max = math.log(1 + self.R**2/self.L**2)
        self.rn = self.L*np.sqrt(np.exp(self.xi_max*(1 + self.xn)/2) - 1)
        rf = np.asarray(st['r'].cpu() if torch.is_tensor(st['r']) else st['r'], float)
        assert np.allclose(rf, self.rn, rtol=1e-12, atol=1e-13), np.abs(rf - self.rn).max()
        V = np.polynomial.chebyshev.chebvander(self.xn, N)
        self.cond = np.linalg.cond(V)
        self.b = np.linalg.solve(V, q.T).T           # Chebyshev coefficients per mode
        self.k_tail = int(np.argmin(np.abs(self.rn - 0.6*self.R)))
        self.pref = a.get('prefactor') or 'r'
        assert self.pref in ('r', 's'), self.pref

    def pw(self, r, k):
        """radial prefactor of mode with exponent k and its r-derivative: r^k ('r') or (r/sqrt(1+r^2))^k ('s', numerical record R15)."""
        r = np.asarray(r, float)
        if k == 0:
            return np.ones_like(r), np.zeros_like(r)
        if self.pref == 'r':
            return r**k, k*r**(k - 1)
        s = r/np.sqrt(1 + r*r)
        return s**k, k*s**(k - 1)*(1 + r*r)**-1.5

    def xof(self, r):
        return 2*np.log1p(r**2/self.L**2)/self.xi_max - 1

    def modes_at(self, r):
        """zeta_m(r) for m = 0..M at radii r (numpy), shape (len r, M+1)."""
        x = self.xof(np.asarray(r, float))
        out = np.empty((len(x), self.M + 1), complex)
        for m in range(self.M + 1):
            out[:, m] = self.pw(r, self.kap[m])[0]*np.polynomial.chebyshev.chebval(x, self.b[m])
        return out

    def field(self, r, th):
        zm = self.modes_at(r)
        E = np.exp(1j*np.outer(np.arange(self.M + 1), th))
        f = zm @ E
        return 2*f.real - zm[:, :1].real*np.ones((1, len(th)))   # m = 0 counted once

    def jet(self):
        """zeta(0), zeta_x(0), zeta_y(0): q_0(x=-1) (kappa_0 = 0) and zeta_1 = r q_1 -> 2 Re[q_1(0) e^{i th}] r."""
        z0 = np.polynomial.chebyshev.chebval(-1.0, self.b[0]).real
        q1 = np.polynomial.chebyshev.chebval(-1.0, self.b[1])
        return float(z0), float(2*q1.real), float(-2*q1.imag)


def rho_modes_on_circle(Z, r, nfine=512):
    """modes m = 0..M of zeta^2 at radius r (fine th grid), as numbers (complex)."""
    th = 2*np.pi*np.arange(nfine)/nfine
    z = Z.field(np.array([r]), th)[0]
    return np.fft.fft(z*z)[:Z.M + 1]/nfine


def tail_fit(Z, p, rho_fun=None):
    """(a_m, b_m), m = 0..M, of the power2 model; rho_fun(r) -> modes 0..M (default: zeta^2 of the state)."""
    f = rho_fun if rho_fun is not None else (lambda r: rho_modes_on_circle(Z, r))
    R, rk = Z.R, Z.rn[Z.k_tail]
    q1, q2 = p, 2*p - 1
    rR, rK = f(R), f(rk)
    det = R**q1*rk**q2 - R**q2*rk**q1
    a = (rR*rk**q2 - rK*R**q2)/det
    b = (-rR*rk**q1 + rK*R**q1)/det
    return a, b, q1, q2


def grid(R, ratio_in=1.25, Lmax=1e16, ratio_out=2.0):
    e_in = np.geomspace(1e-6, R, int(np.ceil(np.log(R/1e-6)/np.log(ratio_in))) + 1)
    e_out = np.geomspace(R, Lmax, int(np.ceil(np.log(Lmax/R)/np.log(ratio_out))) + 1)
    return np.concatenate([[0.0], e_in, e_out[1:]])


def tail_field(a, b, q1, q2, r, th):
    M = len(a) - 1
    E = np.exp(1j*np.outer(np.arange(M + 1), th))
    f = (np.outer(r**q1, np.ones(M + 1))*a[None] + np.outer(r**q2, np.ones(M + 1))*b[None]) @ E
    return 2*f.real - (r**q1*a[0].real + r**q2*b[0].real)[:, None]


def seed_zeta(X, Y, ay, p0):
    rr = np.sqrt(1 + X*X + Y*Y)
    return X*(1 + ay*Y/rr)*rr**(p0/2 - 1)


def panel_interp(Ev, F, rq):
    """values of nodal F (Nr_mine, nt) at radii rq: Gauss-node Lagrange polynomial of the panel containing r (a radius on
    an edge is taken from the inner panel)."""
    e = Ev.edges; q = Ev.G.q
    xg = np.polynomial.legendre.leggauss(q)[0]
    out = np.empty((len(rq), F.shape[1]), F.dtype)
    for i, rr in enumerate(rq):
        p = int(np.searchsorted(e, rr, side='left')) - 1
        t = 2*(rr - e[p])/(e[p + 1] - e[p]) - 1
        out[i] = lagrange_eval(xg, t) @ F[p*q:(p + 1)*q]
    return out


def zeta_grad_rep(Z, r, th):
    """zeta, zeta_x, zeta_y of the representation at (r, th) by term-wise differentiation of the Chebyshev series."""
    x = Z.xof(r)
    dxdr = (2/Z.xi_max)*2*r/(Z.L**2 + r**2)
    zr = np.empty((len(r), Z.M + 1), complex); zm = np.empty_like(zr)
    for m in range(Z.M + 1):
        qv = np.polynomial.chebyshev.chebval(x, Z.b[m]); qd = np.polynomial.chebyshev.chebval(x, np.polynomial.chebyshev.chebder(Z.b[m]))
        k = Z.kap[m]
        P, dP = Z.pw(r, k)
        zm[:, m] = P*qv
        zr[:, m] = dP*qv + P*qd*dxdr
    mm = np.arange(Z.M + 1)
    E = np.exp(1j*np.outer(mm, th))
    def syn(f):
        g = f @ E
        return 2*g.real - f[:, :1].real
    z = syn(zm); dr = syn(zr); dt = syn(zm*(1j*mm)[None])/r[:, None]
    c, s_ = np.cos(th)[None], np.sin(th)[None]
    return z, c*dr - s_*dt, s_*dr + c*dt


def seed_grad(X, Y, a, p0):
    s = np.sqrt(1 + X*X + Y*Y); k = p0/2 - 1
    g = 1 + a*Y/s
    z = X*g*s**k
    zx = g*s**k + X*(-a*Y*X/s**3)*s**k + X*g*k*s**(k - 2)*X
    zy = X*(a/s - a*Y*Y/s**3)*s**k + X*g*k*s**(k - 2)*Y
    return z, zx, zy


def split_modes(F, M):
    """max over r of the |m| <= M part and of the |m| > M part of F(r, th) (uniform th)."""
    Fm = np.fft.fft(F, axis=1)/F.shape[1]
    m = np.fft.fftfreq(F.shape[1], 1.0/F.shape[1])
    lo = np.fft.ifft(np.where(np.abs(m)[None] <= M, Fm, 0), axis=1).real*F.shape[1]
    return lo, F - lo


class Evaluator:
    def __init__(self, R, nt=128, ratio_in=1.25, Lmax=1e16, q=8):
        self.edges = grid(R, ratio_in, Lmax)
        self.S = CharSolver(self.edges, q, nt, 1e-6, dev)
        self.G = self.S.G
        self.inside = self.G.r <= R*(1 + 1e-14)
        self.R = R

    def transport(self, zeta, rho, cl, p):
        """Rz = (c_l X + W[rho]).grad zeta - zeta/2 on all nodes (meaningful where zeta is defined); c, b of rho."""
        S = self.S
        rt = torch.tensor(rho, dtype=DT, device=dev)
        c, b = S.moments(rt, p)
        W1, W2 = S.velocity(rt, p)
        W1 = W1.cpu().numpy(); W2 = W2.cpu().numpy()
        gx, gy = self.G.grad(zeta)
        Rz = (cl*self.G.X + W1)*gx + (cl*self.G.Y + W2)*gy - 0.5*zeta
        return Rz, float(c), float(b), W1, W2, gx, gy


def decades(Ev, F, ref, pw=None):
    """per radial band: max|F|/max|ref|, and (pw given) max|F|, max|ref| and max|F|/wz, wz = r/(1+r^2)^((1-pw/2)/2)
    (the expected size of zeta, the numerical researcher's residual weight)."""
    out = {}
    r = Ev.G.r
    for lo, hi in [(0, 1e-2), (1e-2, 1), (1, 10), (10, 100), (100, Ev.R*(1 + 1e-14))]:
        sel = (r > lo) & (r <= hi) & Ev.inside
        if sel.any():
            a, b = np.abs(F[sel]).max(), np.abs(ref[sel]).max()
            key = '%g-%g' % (lo, hi)
            if pw is None:
                out[key] = float(a/max(b, 1e-300))
            else:
                wz = r[sel]/(1 + r[sel]**2)**((1 - pw/2)/2)
                out[key] = dict(rel=float(a/max(b, 1e-300)), absF=float(a), absref=float(b),
                                wF=float((np.abs(F[sel])/wz[:, None]).max()), wref=float((np.abs(ref[sel])/wz[:, None]).max()))
    return out


def evaluate(path, nt=128, ratio_in=1.25, Lmax=1e16):
    st = torch.load(path, map_location='cpu', weights_only=False)
    assert st.get('formulation') == 'zeta'
    a = st['args']
    Z = ZetaRep(st)
    cl = float(st['cl']); lam = float(st['lam']) if st.get('lam') is not None else None
    p = 1/cl
    Ev = Evaluator(Z.R, nt, ratio_in, Lmax)
    G = Ev.G
    th = G.th; r = G.r
    ins = Ev.inside
    # state zeta and rho on my grid
    zeta = np.zeros_like(G.X); zeta[ins] = Z.field(r[ins], th)
    ta, tb, q1, q2 = tail_fit(Z, p)
    rho = zeta*zeta
    rho[~ins] = tail_field(ta, tb, q1, q2, r[~ins], th)
    Rz, c, bb, W1, W2, gx, gy = Ev.transport(zeta, rho, cl, p)
    # seed (analytic), at c_l0, with its own power2 tail fit (as a solver would), and exactly (no tail model)
    cl0 = float(a['cl0']); p0 = 1/cl0; ay = float(a.get('ay', 0.0))
    z0 = seed_zeta(G.X, G.Y, ay, p0)
    def seed_rho_modes(rr, nf=512):
        t = 2*np.pi*np.arange(nf)/nf
        zz = seed_zeta(rr*np.cos(t), rr*np.sin(t), ay, p0)
        return np.fft.fft(zz*zz)[:Z.M + 1]/nf
    sa, sb, s1, s2 = tail_fit(Z, p0, seed_rho_modes)
    rho0t = z0*z0; rho0t[~ins] = tail_field(sa, sb, s1, s2, r[~ins], th)
    f0t, c0t, b0t, W01, W02 = Ev.transport(z0, rho0t, cl0, p0)[:5]
    f0e, c0e, b0e = Ev.transport(z0, z0*z0, cl0, p0)[:3]
    out = dict(path=path, Nr=Z.Nr, Nth=Z.Nth, R=Z.R, L=Z.L, cl=cl, lam=lam, cheb_cond=Z.cond, nt=nt, ratio_in=ratio_in,
               Lmax=Lmax, Nr_mine=len(r))
    out['jet'] = Z.jet()
    out['c'] = c; out['b'] = bb; out['compat'] = cl - 0.5 - c
    out['seed'] = dict(c_tail=c0t, c_exact=c0e, b_exact=b0e)
    # state continuity check: my reconstruction at their nodes vs the stored q (exactness of the fit)
    zm_nodes = Z.modes_at(Z.rn)
    qst = st['q'].detach().cpu().numpy()
    PW = np.stack([Z.pw(Z.rn, k)[0] for k in Z.kap], 1)
    out['fit_err'] = float(np.abs(zm_nodes/np.where(PW > 0, PW, 1) - qst.T).max())
    out['prefactor'] = Z.pref
    sel = ins & (r > 0)
    for name, f0 in [('tailfit', f0t), ('exact', f0e)]:
        A = f0[sel].ravel(); B = Rz[sel].ravel()
        lam_ls = float(A @ B/(A @ A))
        d = dict(lam_ls=lam_ls)
        if lam is not None:
            d['rel_max_vs_lam'] = float(np.abs(B - lam*A).max()/np.abs(lam*A).max())
            d['by_decade'] = decades(Ev, Rz - lam*f0, lam*f0, p0)
        d['rel_max_ls'] = float(np.abs(B - lam_ls*A).max()/np.abs(lam_ls*A).max())
        d['rel_l2_ls'] = float(np.linalg.norm(B - lam_ls*A)/np.linalg.norm(lam_ls*A))
        out['f0_' + name] = d
    out['f0_tail_vs_exact'] = float(np.abs(f0t - f0e)[sel].max()/np.abs(f0e[sel]).max())
    out['Rz_max'] = float(np.abs(Rz[sel]).max())
    # f0-free scale (for lam -> 0, an unforced candidate): per band max|Rz| / max|zeta/2| and max|lam f0| / max|zeta/2|
    unf = {}
    for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1000), (1000, Ev.R*(1 + 1e-14))]:
        sb = sel & (r > lo) & (r <= hi)
        if sb.any():
            zs = 0.5*np.abs(zeta[sb]).max()
            unf['%g-%g' % (lo, hi)] = dict(Rz_over_zeta=float(np.abs(Rz[sb]).max()/zs),
                                           lamf0_over_zeta=float(abs(lam or 0.0)*np.abs(f0t[sb]).max()/zs))
    out['unforced_scale'] = unf
    # rho residual 2 zeta Rz and min V_r/r inside R
    Vr = (cl*G.X + W1)*np.cos(G.T) + (cl*G.Y + W2)*np.sin(G.T)
    out['minVr_r_inside'] = float((Vr[sel]/G.R[sel]).min())
    out['tail_a2'] = complex(ta[2]).__repr__(); out['tail_b2'] = complex(tb[2]).__repr__()
    out['rho_min_inside'] = float(rho[ins].min())
    # at the numerical researcher's own radial nodes (their collocation points), my velocity interpolated from my panels,
    # grad zeta from the Chebyshev series; theta on my uniform grid; split into |m| <= M (their equations) and |m| > M
    rq = Z.rn
    w1 = panel_interp(Ev, W1, rq); w2 = panel_interp(Ev, W2, rq)
    v1 = panel_interp(Ev, W01, rq); v2 = panel_interp(Ev, W02, rq)
    Xq = rq[:, None]*np.cos(th)[None]; Yq = rq[:, None]*np.sin(th)[None]
    z, zx, zy = zeta_grad_rep(Z, rq, th)
    Rzq = (cl*Xq + w1)*zx + (cl*Yq + w2)*zy - 0.5*z
    s0, s0x, s0y = seed_grad(Xq, Yq, ay, p0)
    f0q = (cl0*Xq + v1)*s0x + (cl0*Yq + v2)*s0y - 0.5*s0
    D = Rzq - (lam if lam is not None else 0.0)*f0q
    Dlo, Dhi = split_modes(D, Z.M); Flo, Fhi = split_modes(f0q, Z.M)
    wz = rq/(1 + rq**2)**((1 - p0/2)/2)
    rows = []
    for j in range(len(rq)):
        rows.append(dict(r=float(rq[j]), Dlo=float(np.abs(Dlo[j]).max()), Dhi=float(np.abs(Dhi[j]).max()),
                         f0=float(np.abs(f0q[j]).max()), f0hi=float(np.abs(Fhi[j]).max()), wz=float(wz[j])))
    out['nodes'] = rows
    # between their nodes (midpoints in x), same evaluation: tests the interpolant, not only the collocation equations
    xm = 0.5*(Z.xn[:-1] + Z.xn[1:])
    rm_ = Z.L*np.sqrt(np.exp(Z.xi_max*(1 + xm)/2) - 1)
    w1 = panel_interp(Ev, W1, rm_); w2 = panel_interp(Ev, W2, rm_)
    v1 = panel_interp(Ev, W01, rm_); v2 = panel_interp(Ev, W02, rm_)
    Xm = rm_[:, None]*np.cos(th)[None]; Ym = rm_[:, None]*np.sin(th)[None]
    z, zx, zy = zeta_grad_rep(Z, rm_, th)
    s0, s0x, s0y = seed_grad(Xm, Ym, ay, p0)
    Dm = (cl*Xm + w1)*zx + (cl*Ym + w2)*zy - 0.5*z - (lam if lam is not None else 0.0)*((cl0*Xm + v1)*s0x + (cl0*Ym + v2)*s0y - 0.5*s0)
    Dmlo, Dmhi = split_modes(Dm, Z.M)
    wzm = rm_/(1 + rm_**2)**((1 - p0/2)/2)
    out['mid'] = [dict(r=float(rm_[j]), Dlo=float(np.abs(Dmlo[j]).max()), Dhi=float(np.abs(Dmhi[j]).max())) for j in range(len(rm_))]
    out['mid_wmax_Dlo'] = float((np.abs(Dmlo)/wzm[:, None]).max())
    # Chebyshev coefficient tails of q_m (resolution in r): max_m |b_m,k| for the last 5 k, relative to max |b|
    bt = np.abs(Z.b)
    out['cheb_tail_rel'] = [float(v) for v in (bt[:, -5:].max(0)/bt.max())]
    out['cheb_by_mode_last'] = [float(v) for v in (bt[:, -3:].max(1)/np.maximum(bt.max(1), 1e-300))]
    A = Flo.ravel(); B = (Rzq - Dhi).ravel()
    out['lam_ls_nodes'] = float(A @ (split_modes(Rzq, Z.M)[0].ravel())/(A @ A))
    out['nodes_wmax_Dlo'] = float((np.abs(Dlo)/wz[:, None]).max()); out['nodes_wmax_Dhi'] = float((np.abs(Dhi)/wz[:, None]).max())
    out['nodes_wrms_Dlo'] = float(np.sqrt(np.mean((Dlo/wz[:, None])**2)))
    return out


if __name__ == '__main__':
    path = sys.argv[1]
    nt = int(sys.argv[2]) if len(sys.argv) > 2 else 128
    ratio_in = float(sys.argv[3]) if len(sys.argv) > 3 else 1.25
    Lmax = float(sys.argv[4]) if len(sys.argv) > 4 else 1e16
    print(json.dumps(evaluate(path, nt, ratio_in, Lmax)), flush=True)
