"""V20 (notes of the lead analyst 20:02Z item 2, 20:14Z item 1): independent evaluation of the lead's joint test density
    rho = x^2 exp(2F) (1+r^2)^{(p0-2)/2},  p0 = 1/2,  F = F7 + s (F15 - F7) + t (F32 - F7)
(F_i = random combinations of six features for two scales, numpy default_rng(1), same draw order as the lead's
explore/joint_scan.py; reconstructed here as analytic functions, checked against the lead's saved runs/joint_F_k32.npy).
Quantities (all scale invariant):
    kappa  = Q/(pi c^2),  Q = int rho W.grad phi,  phi = r^-3 sin 3th,     profile value 2(1-p0)/(2-p0) = 2/3
    3 kw/c, kw = int h w' dy / int h dy,  h = rho_xx(0,y),  w' = psi_xy(0,y)  profile value 2/3 as well.
Own methods (no lead code): c and w'(y0) = psi_xy(0,y0) = c-moment of the translated density rho(. + (0,y0)) (Prop 11.5
translation covariance; grad rho = 0 on the wall), by direct polar quadrature (composite Gauss-Legendre in r to L = 1e10
plus exact r^p tail, uniform trapezoid in theta); Q and min V_r/r from code/charsolve.py velocity (exact radial Green's
function per Fourier mode). eps > 0 replaces tanh(Y/L) by tanh(Y/sqrt(L^2 + eps^2 r^2)) (a smooth degree-0 version:
for eps = 0 the feature has gradient O(1/L) on the band |Y| < L at every radius, so rho violates S(b) and its angular
far-field profile jumps at th = 0, pi).
scan: the individual samples F_k (claim (ii)) and the lead's validation family F = log(1 + a Y/<r>).
env V20_FEAT = tanh | dec, V20_TRI = i,j,k (F = F_i + s (F_j - F_i) + t (F_k - F_i); default 7,15,32).
usage: python3 tests/v20_joint.py MODE [args]; MODE in {fcheck, eval, solve, scan}."""
import numpy as np, torch, sys, math, json, time, os
sys.path.insert(0, 'code')
dev = 'cuda'; DT = torch.float64
p0 = 0.5
FEAT = os.environ.get('V20_FEAT', 'tanh')   # 'dec': lead's smooth replacement L Y/(L^2 + r^2) of the tanh feature
TRI = tuple(int(v) for v in os.environ.get('V20_TRI', '7,15,32').split(','))   # base samples (i, j, k)
TGT = 2*(1 - p0)/(2 - p0)


def coef_sets(seed=1, n=40):
    rng = np.random.default_rng(seed)
    out = []
    for i in range(n):
        terms = []
        for L in [1.0, 4.0]:
            Lr = L*np.exp(rng.uniform(-1, 1.5))
            cs = [rng.uniform(-1.5, 1.5) for _ in range(6)]
            terms.append((Lr, cs))
        out.append(terms)
    return out


SETS = coef_sets()


def combine(s, t, k=None):
    i, j, k0 = TRI
    k = k0 if k is None else k
    out = []
    for wgt, idx in [(1 - s - t, i), (s, j), (t, k)]:
        for Lr, cs in SETS[idx]:
            out.append((Lr, [wgt*c for c in cs]))
    return out


def Ffun(X, Y, terms, eps):
    if callable(terms):
        return terms(X, Y)
    r2 = X*X + Y*Y
    F = torch.zeros_like(X)
    for Lr, cs in terms:
        R = torch.sqrt(Lr**2 + r2)
        T = torch.tanh(Y/torch.sqrt(Lr**2 + eps**2*r2)) if FEAT == 'tanh' else Lr*Y/(Lr**2 + r2)
        f = [Y/R, (X*X - Y*Y)/R**2, X*X*Y/R**3, Y**3/R**3, T, X*X*Y*Y/R**4]
        for c, fi in zip(cs, f):
            F = F + c*fi
    return F


def rho_fn(X, Y, terms, eps):
    return X*X*torch.exp(2*Ffun(X, Y, terms, eps))*(1 + X*X + Y*Y)**((p0 - 2)/2)


def radial(r1=1e-6, L=1e10, ratio=1.1, q=8):
    n = int(np.ceil(np.log(L/r1)/np.log(ratio)))
    edges = np.concatenate([[0.0], np.geomspace(r1, L, n + 1)])
    xg, wg = np.polynomial.legendre.leggauss(q)
    a, b = edges[:-1, None], edges[1:, None]
    r = ((a + b)/2 + (b - a)/2*xg[None]).ravel(); w = ((b - a)/2*wg[None]).ravel()
    return torch.tensor(r, dtype=DT, device=dev), torch.tensor(w, dtype=DT, device=dev)


class Quad:
    def __init__(self, nt=2048, ratio=1.1, L=1e10, chunk=None):
        self.r, self.w = radial(L=L, ratio=ratio)
        self.L = L; self.nt = nt
        th = 2*math.pi*torch.arange(nt, dtype=DT, device=dev)/nt
        self.c, self.s = torch.cos(th), torch.sin(th)
        self.e3 = torch.exp(-3j*th.to(torch.complex128))

    def cmom(self, f):
        """c = psi_xy(0), b = psi_yy(0) of density function f(X, Y) (canonical law, r^p0 tail beyond L)."""
        X = self.r[:, None]*self.c[None]; Y = self.r[:, None]*self.s[None]
        r3 = (f(X, Y).to(torch.complex128)*self.e3[None]).mean(1)
        I = torch.sum(self.w*r3/self.r**2)
        r3L = (f(self.L*self.c, self.L*self.s).to(torch.complex128)*self.e3).mean()
        I = I + r3L/(self.L*(1 - p0))
        return float(-2*I.imag), float(-2*I.real)


def wall(Qd, terms, eps, ymin=1e-5, ymax=1e7, nper=60):
    """int h dy, int h w' dy over R (u = log|y| trapezoid, power tails), w'(0) = c."""
    nu = int(round(np.log10(ymax/ymin)*nper)) + 1
    u = np.linspace(np.log(ymin), np.log(ymax), nu); yy = np.exp(u)
    res = {}
    Ih = Ihw = 0.0
    c0 = Qd.cmom(lambda X, Y: rho_fn(X, Y, terms, eps))[0]
    for sgn in (1, -1):
        wp = np.array([Qd.cmom(lambda X, Y: rho_fn(X, Y + sgn*y0, terms, eps))[0] for y0 in yy])
        Yt = torch.tensor(sgn*yy, dtype=DT, device=dev)
        h = (2*torch.exp(2*Ffun(torch.zeros_like(Yt), Yt, terms, eps))*(1 + Yt**2)**((p0 - 2)/2)).cpu().numpy()
        Ih_s = np.trapz(h*yy, u) + h[0]*ymin + h[-1]*ymax/(1 - p0)
        Ihw_s = np.trapz(h*wp*yy, u) + h[0]*c0*ymin + h[-1]*wp[-1]*ymax/(2 - 2*p0)
        Ih += Ih_s; Ihw += Ihw_s
        res[sgn] = dict(Ih=Ih_s, Ihw=Ihw_s, wp_first=wp[0], wp_last=wp[-1], slope_last=float(np.log(abs(wp[-1]/wp[-10]))/(u[-1] - u[-10])))
    return c0, Ih, Ihw, res


class VelEval:
    def __init__(self, nt=256, L=1e10, q=8):
        from charsolve import CharSolver
        r1 = 1e-6
        edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, 25)[1:],
                                np.geomspace(10, L, int(round(np.log10(L/10)*5)) + 1)[1:]])
        self.S = CharSolver(edges, q, nt, r1, dev)

    def Q(self, terms, eps):
        S = self.S
        rho = rho_fn(S.X, S.Y, terms, eps)
        c, b = S.moments(rho, p0)
        W1, W2 = S.velocity(rho, p0)
        g1 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.cs - torch.cos(3*S.TH)*S.sn)
        g2 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.sn + torch.cos(3*S.TH)*S.cs)
        wq = S.w[:, None]*S.r[:, None]*(2*math.pi/S.nt)
        Q = float(torch.sum(wq*rho*(W1*g1 + W2*g2)))
        lam = (1/p0 - 0.5)/float(c)
        Wr_r = (W1*S.cs + W2*S.sn)/S.R
        p0q = S.p0*S.q
        mvr = float((1/p0 + lam*Wr_r[p0q:]).min())
        # w' on the axis by differentiation of W_2 (second method, PolarGrid.grad Gauss-node polynomials)
        gx, gy = S.G.grad(W2.detach().cpu().numpy())
        ju, jd = S.nt//4, 3*S.nt//4
        return dict(c=float(c), b=float(b), Q=Q, minVr_r=mvr, r=S.r.cpu().numpy(), w=S.w.cpu().numpy(),
                    wp_up=gy[:, ju], wp_dn=gy[:, jd])


def evaluate(s, t, eps, Qd, VE, k=None):
    terms = combine(s, t, k)
    c0, Ih, Ihw, res = wall(Qd, terms, eps)
    vq = VE.Q(terms, eps)
    kap = vq['Q']/(math.pi*c0**2)
    kw3 = 3*(Ihw/Ih)/c0
    # second wall method: w' = d_y W_2(0, y) from the computed velocity (Gauss nodes of VelEval, both half-axes)
    r = vq['r']; w = vq['w']; Ihw_ax = 0.0
    for sgn, wp in ((1, vq['wp_up']), (-1, vq['wp_dn'])):
        Yt = torch.tensor(sgn*r, dtype=DT, device=dev)
        h = (2*torch.exp(2*Ffun(torch.zeros_like(Yt), Yt, terms, eps))*(1 + Yt**2)**((p0 - 2)/2)).cpu().numpy()
        Ihw_ax += float(np.sum(w*h*wp))
    kw3_ax = 3*(Ihw_ax/Ih)/c0
    return dict(s=s, t=t, eps=eps, k=k, c_quad=c0, c_vel=vq['c'], b=vq['b'], Q=vq['Q'], kappa=kap, kw3=kw3,
                kw3_axis=kw3_ax, Ih=Ih, Ihw=Ihw, minVr_r=vq['minVr_r'], wall=res)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'fcheck':
        F_lead = np.load('runs/joint_F_k32.npy')
        r = np.exp(np.linspace(-10, 12, 551))[:, None]; th = 2*np.pi*np.arange(256)/256
        X = torch.tensor(r*np.cos(th)[None], dtype=DT, device=dev); Y = torch.tensor(r*np.sin(th)[None], dtype=DT, device=dev)
        for (s, t) in [(0.577358696, -0.000555856), (5.77358696e-01, -5.55856380e-04)]:
            F = Ffun(X, Y, combine(s, t), 0.0).cpu().numpy()
            print('shape', F_lead.shape, 's,t', s, t, 'max |F_mine - F_lead| =', np.abs(F - F_lead).max(), 'max|F| =', np.abs(F_lead).max())
    elif mode == 'eval':
        s, t, eps = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
        nt = int(sys.argv[5]) if len(sys.argv) > 5 else 2048
        ratio = float(sys.argv[6]) if len(sys.argv) > 6 else 1.1
        ntv = int(sys.argv[7]) if len(sys.argv) > 7 else 256
        t0 = time.time()
        Qd = Quad(nt=nt, ratio=ratio); VE = VelEval(nt=ntv)
        d = evaluate(s, t, eps, Qd, VE)
        d.update(nt=nt, ratio=ratio, ntv=ntv, wall_s=time.time() - t0)
        print(json.dumps(d), flush=True)
    elif mode == 'scan':
        eps = float(sys.argv[2]); nt = int(sys.argv[3]); ratio = float(sys.argv[4]); ntv = int(sys.argv[5])
        Qd = Quad(nt=nt, ratio=ratio); VE = VelEval(nt=ntv)
        for a in [0.3, 0.6, 0.9]:
            Fv = lambda X, Y, a=a: torch.log(1 + a*Y/torch.sqrt(1 + X*X + Y*Y))
            c0, Ih, Ihw, res = wall(Qd, Fv, 0.0); vq = VE.Q(Fv, 0.0)
            print(json.dumps(dict(val=a, c=c0, c_vel=vq['c'], wp0_up=res[1]['wp_first'], wp0_dn=res[-1]['wp_first'],
                                  kappa=vq['Q']/(math.pi*c0**2), kw3=3*Ihw/Ih/c0)), flush=True)
        for k in range(len(SETS)):
            terms = [(Lr, cs) for Lr, cs in SETS[k]]
            c0 = Qd.cmom(lambda X, Y: rho_fn(X, Y, terms, eps))[0]
            if not c0 > 0:
                print(json.dumps(dict(k=k, eps=eps, c=c0)), flush=True); continue
            d = evaluate(0.0, 1.0, eps, Qd, VE, k=k)
            print(json.dumps({kk: v for kk, v in d.items() if kk != 'wall'}), flush=True)
    elif mode == 'solve':
        eps = float(sys.argv[2]); nt = int(sys.argv[3]); ratio = float(sys.argv[4]); ntv = int(sys.argv[5])
        st = np.array([float(sys.argv[6]), float(sys.argv[7])]) if len(sys.argv) > 7 else np.array([0.5729, -0.0009])
        Qd = Quad(nt=nt, ratio=ratio); VE = VelEval(nt=ntv)
        def G(st):
            d = evaluate(st[0], st[1], eps, Qd, VE)
            return np.array([d['kappa'] - TGT, d['kw3'] - TGT]), d
        for it in range(10):
            g, d = G(st)
            print(json.dumps(dict(it=it, s=st[0], t=st[1], G=list(g), c=d['c_quad'], c_vel=d['c_vel'], kappa=d['kappa'],
                                  kw3=d['kw3'], minVr_r=d['minVr_r'])), flush=True)
            if np.abs(g).max() < 1e-7: break
            J = np.zeros((2, 2)); e = 1e-4
            for j in range(2):
                dd = np.zeros(2); dd[j] = e
                J[:, j] = (G(st + dd)[0] - g)/e
            step = np.linalg.solve(J, -g)
            if np.abs(step).max() > 0.2: step *= 0.2/np.abs(step).max()
            st = st + step
        print(json.dumps(dict(final=True, s=st[0], t=st[1], d={k: v for k, v in d.items() if k != 'wall'})), flush=True)
