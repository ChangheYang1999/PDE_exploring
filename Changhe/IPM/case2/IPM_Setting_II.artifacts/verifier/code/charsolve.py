"""Independent profile solver of the independent verifier: radial characteristic marching + Newton-Krylov.

Unknown: xi on a polar grid (composite Gauss-Legendre panels in r, uniform theta), rho = xi^2.
Map T(xi):
  1. rho = xi^2; c = psi_xy(0), b = psi_yy(0) from the exact moment functionals
     c = -2 int Im rho_3 r^-2 dr, psi_xx(0) = 2 int Re rho_3 r^-2 dr, b = -psi_xx(0) (+ power-law tail beyond L);
  2. grad V(0) = c_l I + [[-c,-b],[-b,c]]; the slow eigenvalue is set to 1/2: c_l = 1/2 + sqrt(c^2+b^2), and the
     jet direction l is the slow unit eigenvector (b = 0 gives c_l = 1/2 + c, l = e_1, i.e. the PROMPT jet);
  3. W = U - U(0) by the canonical once-subtracted law, per Fourier mode with the exact radial Green's function
     (same formulas as code/polar_inverse.py, assembled as dense per-mode matrices on the GPU), tail r^p A beyond L;
  4. solve V.grad xi_new = xi_new/2, V = c_l X + W, by marching outward in r from r1 (inflow value xi = l.X at r = r1),
     panel by panel: on each panel xi is a polynomial of degree q in r through the left-edge value and the q Gauss
     nodes, collocated at the Gauss nodes (Gauss collocation), Fourier collocation in theta. Requires V_r > 0.
Fixed point xi = T(xi) solves the profile system with a rank-one jet along l (rho = (l.X)^2 + O(r^3)).
No symmetry is imposed anywhere. Differentiation in the marching uses the (q+1)-point panel polynomial including the
left edge; the residual check uses PolarGrid.grad (q-point Gauss polynomial, no edge) and code/bs_cartesian.py.
"""
import numpy as np, torch, sys, math, time
sys.path.insert(0, 'code')
from polar_inverse import PolarGrid
# torch 2.8 'default' backend heuristic: the forward-AD (dual) batched torch.linalg.solve in march returns a wrong
# primal and tangent for n = q nt >= 768 (nt >= 96; correct for single matrices and with an explicit backend; found
# 2026-10-17T20:04Z, tests/adt3.py). Force cuSOLVER.
torch.backends.cuda.preferred_linalg_library('cusolver')

def lagrange_diff(xs):
    """differentiation matrix of the Lagrange interpolant on nodes xs (barycentric)."""
    n = len(xs)
    w = np.array([1.0/np.prod([xs[j]-xs[k] for k in range(n) if k != j]) for j in range(n)])
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i, j] = (w[j]/w[i])/(xs[i]-xs[j])
        D[i, i] = -D[i].sum()
    return D

def lagrange_eval(xs, t):
    n = len(xs)
    return np.array([np.prod([(t-xs[k])/(xs[j]-xs[k]) for k in range(n) if k != j]) for j in range(n)])

def fourier_diff(n):
    """physical-space Fourier differentiation matrix, n even (Trefethen)."""
    D = np.zeros((n, n))
    h = 2*np.pi/n
    for j in range(n):
        for l in range(n):
            if j != l:
                D[j, l] = 0.5*(-1)**(j-l)/np.tan((j-l)*h/2)
    return D

class CharSolver:
    def __init__(self, edges, q=8, nt=64, r1=1e-6, dev='cuda', mkeep=None):
        self.dev = dev; self.dt = torch.float64
        G = PolarGrid(edges, q, nt); self.G = G
        self.edges = np.asarray(edges, float); self.q = q; self.nt = nt; self.P = len(edges)-1
        self.Nr = self.P*q
        ip = np.where(np.isclose(self.edges, r1, rtol=1e-12, atol=0))[0]
        assert len(ip) == 1, 'r1 must be an edge'
        self.p0 = int(ip[0]); self.r1 = r1
        self.L = self.edges[-1]
        T = lambda a: torch.tensor(a, dtype=self.dt, device=dev)
        self.r = T(G.r); self.w = T(G.w); self.th = T(G.th)
        self.R = T(G.R); self.TH = T(G.T); self.X = T(G.X); self.Y = T(G.Y)
        self.cs = torch.cos(self.TH); self.sn = torch.sin(self.TH)
        self.ms = G.m.copy()
        self.mkeep = nt//2 - 3 if mkeep is None else mkeep
        self.keep = T((np.abs(self.ms) <= self.mkeep).astype(float))
        self._build_bs()
        self._build_march()

    # ---------------- Biot-Savart (canonical once-subtracted law) ----------------
    def _build_bs(self):
        """per-mode matrices W_{m-2} += M_m rho_m, built on the GPU from the panel quadrature (same formulas and
        sub-rules as PolarGrid._inner/_outer/cum0, vectorised; checked against them in code/test_charsolve.py)."""
        G, Nr, nt, q, P = self.G, self.Nr, self.nt, self.q, self.P
        dev, dt = self.dev, self.dt
        T = lambda a: torch.tensor(np.asarray(a), dtype=dt, device=dev)
        sigL, wL, LL, sigR, wR, LR = [T(a) for a in G._subrules()]
        r = self.r; w = self.w
        e = T(self.edges); hp = T(np.diff(self.edges)/2)
        pid = torch.arange(Nr, device=dev)//q
        ri = r[:, None]; sk = r[None, :]
        earlier = pid[None, :] < pid[:, None]; later = pid[None, :] > pid[:, None]
        ratio_in = torch.where(earlier, sk/ri, torch.zeros_like(ri*sk))     # s/r < 1 where used
        ratio_out = torch.where(later, ri/sk, torch.zeros_like(ri*sk))      # r/s < 1 where used
        rp = r.reshape(P, q)                                           # node radii per panel
        sigLp = e[:P, None, None] + hp[:, None, None]*(sigL[None] + 1)   # (P, q, q) sub-nodes in [e_p, r_i]
        sigRp = e[:P, None, None] + hp[:, None, None]*(sigR[None] + 1)   # (P, q, q) sub-nodes in [r_i, e_{p+1}]
        def blockdiag(Bm):   # Bm (P, q, q) -> (Nr, Nr)
            out = torch.zeros((Nr, Nr), dtype=dt, device=dev)
            for p in range(P):
                out[p*q:(p+1)*q, p*q:(p+1)*q] = Bm[p]
            return out
        def inner_mat(mu):
            M = w[None, :]*ratio_in**(mu+1)/ri
            ratio = (sigLp/rp[:, :, None])**(mu+1)
            Bm = torch.einsum('ik,pik,ikj->pij', wL, ratio, LL)*hp[:, None, None]/rp[:, :, None]
            return M + blockdiag(Bm)
        def outer_mat(nu):
            M = torch.where(later, w[None, :]*ratio_out**nu/sk, torch.zeros_like(ratio_out))
            ratio = (rp[:, :, None]/sigRp)**nu/sigRp
            Bm = torch.einsum('ik,pik,ikj->pij', wR, ratio, LR)*hp[:, None, None]
            return M + blockdiag(Bm)
        Cq = T(G.C)
        Cum = torch.where(earlier, w[None, :]/sk, torch.zeros_like(ratio_in)) + blockdiag(Cq[None]*hp[:, None, None]/rp[:, None, :])
        I = torch.eye(Nr, dtype=dt, device=dev)
        self.Mbs = torch.zeros((nt, Nr, Nr), dtype=dt, device=dev)    # real matrices (all formulas are real)
        tgt = np.zeros(nt, int)
        self.tail_modes = []
        for j, m in enumerate(self.ms):
            tgt[j] = (m-2) % nt
            if abs(m) > self.mkeep:
                continue
            if m <= 0:
                mu = float(abs(m))
                self.Mbs[j] = 0.25*(-I + 2*(1+mu)*inner_mat(mu))
            elif m == 1:
                self.Mbs[j] = -0.25*I
            elif m == 2:
                self.Mbs[j] = 0.25*(-I - 2*(m-1)*Cum)
            else:
                nu = float(m-2)
                self.Mbs[j] = 0.25*(-I + 2*(m-1)*outer_mat(nu))
                self.tail_modes.append(j)
        self.tgt = torch.tensor(tgt, device=dev)
        # extrapolation of nodal values on the last panel to r = L (Gauss nodes -> +1)
        xg = np.polynomial.legendre.leggauss(q)[0]
        self.ext_last = torch.tensor(lagrange_eval(xg, 1.0), dtype=dt, device=dev)

    def rho_modes(self, rho):
        return torch.fft.fft(rho.to(torch.complex128), dim=1)/self.nt*self.keep

    def velocity(self, rho, p):
        """W = U - U(0) (W1, W2) on the grid; p = far-field exponent used for the tail beyond L."""
        rm = self.rho_modes(rho)
        src = torch.complex(torch.einsum('jab,bj->aj', self.Mbs, rm.real), torch.einsum('jab,bj->aj', self.Mbs, rm.imag))
        Wm = torch.zeros_like(rm).index_add(1, self.tgt, src)
        # tail beyond L for modes m >= 3: b(r) += (r/L)^{m-2} rho_m(L)/(m-2-p)
        q = self.q
        rhoL = torch.einsum('k,km->m', self.ext_last.to(torch.complex128), rm[-q:])
        if len(self.tail_modes):
            tm = self.tail_modes
            mm = torch.tensor([float(self.ms[j]) for j in tm], dtype=self.dt, device=self.dev)
            add = 0.5*(mm - 1)*(self.r[:, None]/self.L)**(mm - 2)*rhoL[tm]/(mm - 2 - p)
            tg = torch.tensor([(int(self.ms[j]) - 2) % self.nt for j in tm], device=self.dev)
            Wm = Wm.index_add(1, tg, add.to(Wm.dtype))
        W = torch.fft.ifft(Wm, dim=1)*self.nt
        return 2*W.imag, 2*W.real - rho/2

    def moments(self, rho, p):
        """c = psi_xy(0), b = psi_yy(0) of the canonical law (tail r^p beyond L)."""
        rm = self.rho_modes(rho)
        r3 = rm[:, 3]
        I = torch.sum(self.w*r3/self.r**2)
        rhoL = torch.dot(self.ext_last.to(torch.complex128), r3[-self.q:])
        I = I + rhoL/(self.L*(1-p))
        c = -2*I.imag; psixx = 2*I.real
        return c, -psixx

    def solve_p(self, rho, h=1.0, mu=0.0, p_init=0.5, iters=60):
        """exact far-field self-consistency p = 1/c_l. c, b are affine in u = 1/(1-p) (tail rhoL/(L(1-p))):
        c = c0 + ca u, b = b0 + ba u; with C = h c + (1-h) mu, B = h b, c_l = 1/2 + sqrt(C^2 + B^2), solve
        f(u) = c_l(u)(u - 1) - u = 0 by safeguarded Newton from u = 1/(1-p_init) (root nearest the start, u in (1, 1e3]).
        Torch ops throughout, so forward AD gives the implicit derivative. Returns c, b, c_l, l, p, |f|."""
        rm3 = self.rho_modes(rho)[:, 3]
        I0 = torch.sum(self.w*rm3/self.r**2)
        A = torch.dot(self.ext_last.to(torch.complex128), rm3[-self.q:])/self.L
        c0, ca, b0, ba = -2*I0.imag, -2*A.imag, -2*I0.real, -2*A.real
        u = torch.as_tensor(1.0/(1.0 - float(p_init)), dtype=self.dt, device=self.dev)
        f = None
        for _ in range(iters):
            C = h*(c0 + ca*u) + (1 - h)*mu; B = h*(b0 + ba*u)
            s = torch.sqrt(C**2 + B**2); cl = 0.5 + s
            f = cl*(u - 1) - u
            df = h*(C*ca + B*ba)/s*(u - 1) + cl - 1
            un = u - f/df
            uf = float(un)
            if not math.isfinite(uf) or uf <= 1.0:
                un = 0.5*(u + 1.0)                 # stay in p > 0
            elif uf > 1e3:
                un = 0.5*(u + 1e3)
            if abs(float(un) - float(u)) < 1e-14*float(u) and abs(float(f)) < 1e-12:
                u = un; break
            u = un
        C = h*(c0 + ca*u) + (1 - h)*mu; B = h*(b0 + ba*u)
        cl, l = self.jet(C, B)
        f = cl*(u - 1) - u
        return c0 + ca*u, b0 + ba*u, cl, l, 1.0 - 1.0/u, float(abs(f))

    @staticmethod
    def jet(c, b):
        s = torch.sqrt(c**2 + b**2)
        v1 = torch.stack([s + c, b]); v2 = torch.stack([b, s - c])
        v = v1 if torch.linalg.norm(v1) >= torch.linalg.norm(v2) else v2
        v = v/torch.linalg.norm(v)
        if v[0] < 0: v = -v
        return 0.5 + s, v

    # ---------------- radial marching ----------------
    def _build_march(self):
        q, nt = self.q, self.nt
        xg = np.polynomial.legendre.leggauss(q)[0]
        xs = np.concatenate([[-1.0], xg])
        D = lagrange_diff(xs)
        self.Dt = torch.tensor(D[1:], dtype=self.dt, device=self.dev)      # (q, q+1), reference coords
        self.Eright = torch.tensor(lagrange_eval(xs, 1.0), dtype=self.dt, device=self.dev)  # (q+1,)
        self.Dth = torch.tensor(fourier_diff(nt), dtype=self.dt, device=self.dev)
        self.hp = torch.tensor(np.diff(self.edges)/2, dtype=self.dt, device=self.dev)

    def march(self, Vr, Vt_r, z0):
        """solve Vr d_r z + Vt_r d_th z = z/2 for panels p >= p0, inflow z0 (nt,) at r = r1.
        Vr, Vt_r: (Nr, nt) radial velocity and angular velocity / r. Returns z on all nodes of panels >= p0."""
        q, nt, P, p0 = self.q, self.nt, self.P, self.p0
        npn = P - p0
        Vr_p = Vr[p0*q:].reshape(npn, q, nt); Vt_p = Vt_r[p0*q:].reshape(npn, q, nt)
        Dt = self.Dt[None]/self.hp[p0:, None, None]                        # (npn, q, q+1)
        eye_q = torch.eye(q, dtype=self.dt, device=self.dev); eye_t = torch.eye(nt, dtype=self.dt, device=self.dev)
        A = (Vr_p[:, :, :, None, None]*Dt[:, :, None, 1:, None]*eye_t[None, None, :, None, :]
             + Vt_p[:, :, :, None, None]*eye_q[None, :, None, :, None]*self.Dth[None, None, :, None, :]
             - 0.5*eye_q[None, :, None, :, None]*eye_t[None, None, :, None, :])
        A = A.reshape(npn, q*nt, q*nt)
        B = -(Vr_p*Dt[:, :, 0:1])[:, :, :, None]*eye_t[None, None, :, :]    # (npn, q, nt, nt)
        B = B.reshape(npn, q*nt, nt)
        Gp = torch.linalg.solve(A, B).reshape(npn, q, nt, nt)               # z_panel = Gp z_left
        Pi = self.Eright[0]*eye_t[None] + torch.einsum('k,pkjl->pjl', self.Eright[1:], Gp)
        zl = z0
        out = []
        for k in range(npn):
            out.append(torch.einsum('kjl,l->kj', Gp[k], zl))
            zl = Pi[k] @ zl
        return torch.stack(out, 0).reshape(npn*q, nt)

    # ---------------- the map ----------------
    def T(self, xi, p_tail=None, info=False, cl_fixed=None):
        """the map xi -> xi_new. cl_fixed: use this c_l (and p = 1/c_l) instead of 1/2 + sqrt(c^2+b^2); the jet
        direction is always the slow eigenvector of [[-c,-b],[-b,c]]; info['g'] = c_l - 1/2 - sqrt(c^2+b^2)."""
        rho = xi**2
        if cl_fixed is not None:
            cl = torch.tensor(float(cl_fixed), dtype=self.dt, device=self.dev)
            p = 1.0/float(cl_fixed) if p_tail is None else p_tail
            c, b = self.moments(rho, p)
            clj, l = self.jet(c, b)
        elif getattr(self, 'exact_p', False) and p_tail is None:      # opt-in exact p = 1/c_l (solve_p, h = 1)
            c, b, cl, l, p, self.last_fp = self.solve_p(rho, 1.0, 0.0, getattr(self, 'p_start', 0.5))
            clj = cl
        else:
            p = 0.5 if p_tail is None else p_tail
            for _ in range(3):
                c, b = self.moments(rho, p)
                cl, l = self.jet(c, b)
                if p_tail is None:
                    p = torch.clamp(1.0/cl, max=0.999)     # tensor: differentiable (forward AD) far-field exponent
            clj = cl
        W1, W2 = self.velocity(rho, p)
        Vr = cl*self.R + W1*self.cs + W2*self.sn
        Vt_r = (-W1*self.sn + W2*self.cs)/self.R
        z0 = self.r1*(l[0]*torch.cos(self.th) + l[1]*torch.sin(self.th))
        q, p0 = self.q, self.p0
        new = torch.cat([l[0]*self.X[:p0*q] + l[1]*self.Y[:p0*q], self.march(Vr, Vt_r, z0)], 0)
        if info:
            d = dict(c=float(c), b=float(b), cl=float(cl), g=float(cl - clj), l=(float(l[0]), float(l[1])), p=float(p),
                     minVr_r=float((Vr[p0*q:]/self.R[p0*q:]).min()))
            if getattr(self, 'exact_p', False): d['fp'] = getattr(self, 'last_fp', 0.0)
            return new, d
        return new

    # ---------------- independent residual (different differentiation) ----------------
    def residual(self, xi, cl=None):
        """R = V.grad rho - rho with rho = xi^2, gradient by PolarGrid.grad (Gauss-node panel polynomials)."""
        rho = xi**2
        c, b = self.moments(rho, 0.5)
        clj, l = self.jet(c, b)
        p = float(min(1.0/clj, 0.999))
        c, b = self.moments(rho, p); clj, l = self.jet(c, b)
        cl = clj if cl is None else cl
        W1, W2 = self.velocity(rho, p)
        rn = rho.detach().cpu().numpy()
        gx, gy = self.G.grad(rn)
        gx = torch.tensor(gx, device=self.dev); gy = torch.tensor(gy, device=self.dev)
        V1 = cl*self.X + W1; V2 = cl*self.Y + W2
        R = V1*gx + V2*gy - rho
        return R, dict(c=float(c), b=float(b), cl=float(cl), p=p)
