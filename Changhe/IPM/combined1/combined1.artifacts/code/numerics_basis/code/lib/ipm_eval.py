"""Polar separable evaluator for the S1/IPM potential family (lane c1-n1, own derivation; torch float64).

chi_i = G_i(r) cos(n theta), n = 2m, G = R^p Y(t), Y(t) = t^m T(t), T = t^h or t^w P_nleg(2t-1), R = 1+r^2, t = r^2/R.
All fields are finite sums  sum_N rad_N(r) * ang_N(theta)  with ang in {S_N = sin(N th)/sin th, sin(N th), cos(N th), sin th U_{N-1}(cos th), sin th cos th U'_{N-1}(cos th)}.

Polar derivations (own; cross-checked against the exact rules in ipm_exact.py):
  Lap chi = D cos(n th),  D = G'' + G'/r - n^2 G/r^2
  rho = -d_y Lap chi = A_+ sin((n+1)th) + A_- sin((n-1)th),  A_+ = -(D' - nD/r)/2,  A_- = (D' + nD/r)/2
  f = rho/y = sum_N (A_N/r) S_N(th)
  rho_x = sum_N [ (A_N' - N A_N/r)/2 sin((N+1)th) + (A_N' + N A_N/r)/2 sin((N-1)th) ],  f_x = rho_x / y
  f_y = sin th sum_N [ (A_N/r)' U_{N-1}(cos th) - (cos th/r)(A_N/r) U'_{N-1}(cos th) ]
  chi_y = B_+ sin((n+1)th) + B_- sin((n-1)th),  B_+ = (G' - nG/r)/2,  B_- = -(G' + nG/r)/2
  psi = chi_xy = sum_M [ (B_M' - M B_M/r)/2 sin((M+1)th) + (B_M' + M B_M/r)/2 sin((M-1)th) ] =: sum_K Psi_K sin(K th)
  psi_x = sum_K [ (Psi_K' - K Psi_K/r)/2 sin((K+1)th) + (Psi_K' + K Psi_K/r)/2 sin((K-1)th) ] =: sum_N X_N sin(N th);  psi_x/y = sum_N (X_N/r) S_N
  psi_y = sum_K [ (Psi_K' + K Psi_K/r)/2 cos((K-1)th) + (-Psi_K' + K Psi_K/r)/2 cos((K+1)th) ]
  transport (c r d_r - 1) rho = sum_N (kappa A_N - 2c Atilde_N) sin(N th), kappa = c(2p-3)-1, Atilde from Gtilde = R^(p-1)[pY - tY'] (stable form).
  R_f = [transport]/y - psi_y f_x + psi_x f_y + (psi_x/y) f ;  F = y R_f  (density residual).
"""
import math
import numpy as np
import torch

DT = torch.float64

# ------------------------------------------------------------------ mesh
def unit_gauss(order):
    z, w = np.polynomial.legendre.leggauss(order)
    return (z+1)/2, w/2

def whole_axis_radial(origin_radius=0.02, upper_log_radius=16., origin_order=48, middle_order=32, infinity_order=256, panel_width=1.):
    """radial nodes s=log r and weights for the measure ds (= dr/r), three blocks as in case4 whole_axis_mesh.py"""
    lo = math.log(origin_radius); S = upper_log_radius
    ou, ow = unit_gauss(origin_order); tu, tw = unit_gauss(infinity_order)
    os_ = lo+np.log(ou); osw = ow/ou
    ts = S-np.log(tu); tsw = tw/tu
    z, w = np.polynomial.legendre.leggauss(middle_order)
    edges = np.linspace(lo, S, max(1, int(math.ceil((S-lo)/panel_width)))+1)
    ms = np.concatenate([.5*(a+b+(b-a)*z) for a, b in zip(edges[:-1], edges[1:])])
    msw = np.concatenate([.5*(b-a)*w for a, b in zip(edges[:-1], edges[1:])])
    s = np.r_[os_, ms, ts]; ws = np.r_[osw, msw, tsw]
    blocks = np.r_[np.zeros(len(os_), int), np.ones(len(ms), int), np.full(len(ts), 2)]
    return s, ws, blocks

def angular_gauss(order):
    au, aw = unit_gauss(order)
    return au*np.pi/2, aw*np.pi/2

def angular_midpoint(N):
    """uniform midpoint rule on (0, pi/2): exact for cos(2 l theta), l < 2N (the alias l = N vanishes at midpoints), hence exact for
    the squared residual of a potential with angular maximum 2M when N >= 2M+2 (c1-n4 research/angular_resolution/PROOF.md)"""
    th = (np.arange(N)+0.5)*np.pi/(2*N)
    return th, np.full(N, np.pi/(2*N))

class Mesh:
    """product mesh: r (Nr), theta (Nt); weights w_s (ds = dr/r) and w_th; device tensors"""
    def __init__(self, s, ws, theta, wth, device):
        self.device = device
        self.s = torch.as_tensor(np.asarray(s), dtype=DT, device=device); self.ws = torch.as_tensor(np.asarray(ws), dtype=DT, device=device)
        self.theta = torch.as_tensor(np.asarray(theta), dtype=DT, device=device); self.wth = torch.as_tensor(np.asarray(wth), dtype=DT, device=device)
        self.r = torch.exp(self.s); self.Nr = len(s); self.Nt = len(theta)
        self.r2 = self.r*self.r; self.R = 1+self.r2; self.u = 1/self.R; self.t = self.r2*self.u
        self.logR = torch.log1p(self.r2)
        self.sin = torch.sin(self.theta); self.cos = torch.cos(self.theta)
        self.W = self.ws[:, None]*self.wth[None, :]            # weights for ds dtheta
        self._ang = {}
    def angular_tables(self, Nmax):
        """S[N] = sin(N th)/sin th (N>=1), U'[N] = U'_{N-1}(cos th) for N>=1, sin, cos tables up to Nmax"""
        if Nmax in self._ang: return self._ang[Nmax]
        c = self.cos; sn = self.sin; Nt = self.Nt
        U = torch.zeros(Nmax+2, Nt, dtype=DT, device=self.device); dU = torch.zeros(Nmax+2, Nt, dtype=DT, device=self.device)
        U[0] = 1; U[1] = 2*c; dU[1] = 2
        for k in range(2, Nmax+2):
            U[k] = 2*c*U[k-1]-U[k-2]; dU[k] = 2*U[k-1]+2*c*dU[k-1]-dU[k-2]
        # S_N = U_{N-1}; store index by N
        S = torch.zeros(Nmax+2, Nt, dtype=DT, device=self.device); S[1:] = U[:-1]
        dS = torch.zeros(Nmax+2, Nt, dtype=DT, device=self.device); dS[1:] = dU[:-1]          # U'_{N-1}
        N = torch.arange(Nmax+2, dtype=DT, device=self.device)[:, None]
        SIN = torch.sin(N*self.theta[None, :]); COS = torch.cos(N*self.theta[None, :])
        tab = {'S': S, 'sin': SIN, 'cos': COS, 'sU': sn[None, :]*S, 'scdU': (sn*c)[None, :]*dS}
        self._ang[Nmax] = tab
        return tab

def training_mesh(device, angular_order=96, **kw):
    s, ws, blocks = whole_axis_radial(**kw); th, wth = angular_gauss(angular_order)
    m = Mesh(s, ws, th, wth, device); m.blocks = blocks
    return m

# ------------------------------------------------------------------ generators
def legendre_t_jets(t, nmax, order):
    """d^h/dt^h P_n(2t-1), n<=nmax, h<=order (torch)"""
    z = 2*t-1
    P = [[None]*(order+1) for _ in range(nmax+1)]
    P[0][0] = torch.ones_like(t)
    for h in range(1, order+1): P[0][h] = torch.zeros_like(t)
    if nmax >= 1:
        P[1][0] = z; P[1][1] = torch.full_like(t, 2.)
        for h in range(2, order+1): P[1][h] = torch.zeros_like(t)
    for n in range(1, nmax):
        for h in range(order+1):
            term = z*P[n][h]+(2*h*P[n][h-1] if h else 0)
            P[n+1][h] = ((2*n+1)*term-n*P[n-1][h])/(n+1)
    return P

def falling(x, n):
    out = 1.0
    for i in range(n): out *= (x-i)
    return out

def legendre_torch(n, z):
    """P_n(z) by recurrence (differentiable)"""
    if n == 0: return torch.ones_like(z)
    P0 = torch.ones_like(z); P1 = z
    for k in range(1, n):
        P0, P1 = P1, ((2*k+1)*z*P1-k*P0)/(k+1)
    return P1

def autograd_radial(Gfun, r, order):
    """G^(a)(r), a = 0..order, by repeated autograd of a scalar-separable function Gfun(r) (each output depends on its own r_i)"""
    rr = r.clone().detach().requires_grad_(True)
    G = Gfun(rr); out = [G.detach()]
    cur = G
    for a in range(1, order+1):
        (g,) = torch.autograd.grad(cur.sum(), rr, create_graph=True)
        out.append(g.detach()); cur = g
    return out

class Generator:
    """one generator: m, p (float), spec ('mono',h) | ('leg',w,n) | ('legq',w,n,Q) | ('legqs',w,n,Q,R0).
    Y(t) = t^m T(t) for the first three (chi = R^p Y(t) cos(2m th) = H_m R^(p-m) T(t)).
    'legqs': G(r) = r^(2m) (1+r^2)^(p-m) ts^w us^Q P_n(2 ts - 1), ts = r^2/(R0^2+r^2), us = R0^2/(R0^2+r^2): multi-scale inner function with
    vanishing far-field moments q < Q (radial derivatives by autograd)."""
    def __init__(self, m, p, spec):
        self.m = int(m); self.p = float(p); self.spec = tuple(spec)
        self.n = 2*self.m
    def is_direct(self): return self.spec[0] == 'legqs'
    def G_direct(self, mesh, order):
        """G^(a)(r) for a <= order and the companion Gt^(a) = p G^(a) - (a G^(a) + r G^(a+1))/2 for a <= order-1 (r dG/dr = 2pG - 2Gt)"""
        w, n, Qd, R0 = int(self.spec[1]), int(self.spec[2]), int(self.spec[3]), float(self.spec[4]); m = self.m; p = self.p
        def Gfun(r):
            r2 = r*r; ts = r2/(R0*R0+r2); us = (R0*R0)/(R0*R0+r2)
            return r**(2*m)*torch.exp((p-m)*torch.log1p(r2))*ts**w*us**Qd*legendre_torch(n, 2*ts-1)
        G = autograd_radial(Gfun, mesh.r, order)
        Gt = [p*G[a]-(a*G[a]+mesh.r*G[a+1])/2 for a in range(order)]
        return G, Gt
    def kappa(self, c): return c*(2*self.p-3)-1
    def Y_jets(self, mesh, order, Pleg):
        """Y^{(l)}(t), l<=order, as torch arrays over the r grid; and companion Ytil = pY - tY' jets"""
        t = mesh.t
        if self.spec[0] == 'mono':
            e = self.m+int(self.spec[1])
            Yj = [falling(e, l)*t**(e-l) if l <= e else torch.zeros_like(t) for l in range(order+2)]
        else:
            # 'leg': Y = t^(m+w) P_n(2t-1);  'legq': Y = t^(m+w) (1-t)^Q P_n(2t-1) = sum_i (-1)^i C(Q,i) t^(m+w+i) P_n
            if self.spec[0] == 'leg': parts = [(int(self.spec[1]), 1)]
            else:
                Q = int(self.spec[3]); parts = [(int(self.spec[1])+i, (-1)**i*math.comb(Q, i)) for i in range(Q+1)]
            nl = int(self.spec[2])
            Yj = [torch.zeros_like(t) for l in range(order+2)]
            for w, fac in parts:
                e = self.m+w
                for l in range(order+2):
                    acc = torch.zeros_like(t)
                    for i in range(min(l, e)+1):
                        acc = acc+math.comb(l, i)*falling(e, i)*t**(e-i)*Pleg[nl][l-i]
                    Yj[l] = Yj[l]+fac*acc
        # companion: Ytil = p Y - t Y';  Ytil^{(l)} = p Y^{(l)} - (t Y^{(l+1)} + l Y^{(l)})
        Ytj = [self.p*Yj[l]-(t*Yj[l+1]+l*Yj[l]) for l in range(order+1)]
        return Yj[:order+1], Ytj

def radial_derivs(p, Yj, mesh, order):
    """G = R^p Y(t): u-derivatives G_u^{(a)} = R^(p-a) sum_l C(a,l) (p-l)_(a-l) (1-t)^l Y^{(l)}, then r-derivatives up to `order` (<=4)."""
    omt = mesh.u            # 1 - t = 1/R
    Rp = torch.exp(p*mesh.logR)
    Gu = []
    for a in range(order+1):
        acc = torch.zeros_like(mesh.t)
        for l in range(a+1):
            acc = acc+math.comb(a, l)*falling(p-l, a-l)*omt**l*Yj[l]
        Gu.append(Rp*omt**a*acc)
    r = mesh.r; u = mesh.r2
    G = [Gu[0]]
    if order >= 1: G.append(2*r*Gu[1])
    if order >= 2: G.append(2*Gu[1]+4*u*Gu[2])
    if order >= 3: G.append(12*r*Gu[2]+8*r*u*Gu[3])
    if order >= 4: G.append(12*Gu[2]+48*u*Gu[3]+16*u*u*Gu[4])
    return G

def rho_coeffs(G, n, mesh):
    """A_N (rho sine coefficients) and A_N' from radial derivatives G[0..4] of the potential radial function; dict N -> (A, A')"""
    r = mesh.r; n2 = n*n
    D = G[2]+G[1]/r-n2*G[0]/r**2
    D1 = G[3]+G[2]/r-G[1]/r**2-n2*G[1]/r**2+2*n2*G[0]/r**3
    D2 = G[4]+G[3]/r-2*G[2]/r**2+2*G[1]/r**3-n2*G[2]/r**2+4*n2*G[1]/r**3-6*n2*G[0]/r**4
    Ap = -(D1-n*D/r)/2; Apd = -(D2-n*D1/r+n*D/r**2)/2
    Am = (D1+n*D/r)/2; Amd = (D2+n*D1/r-n*D/r**2)/2
    out = {}
    def add(N, A, Ad):
        if N < 0: N, A, Ad = -N, -A, -Ad
        if N == 0: return
        if N in out: out[N] = (out[N][0]+A, out[N][1]+Ad)
        else: out[N] = (A, Ad)
    add(n+1, Ap, Apd); add(n-1, Am, Amd)
    return out

def psi_coeffs(G, n, mesh):
    """Psi_K, Psi_K' (psi = sum Psi_K sin K th) from G[0..3]"""
    r = mesh.r
    B = {}
    def addB(M, b, bd, bdd):
        if M < 0: M, b, bd, bdd = -M, -b, -bd, -bdd
        if M == 0: return
        B[M] = (b, bd, bdd) if M not in B else tuple(x+y for x, y in zip(B[M], (b, bd, bdd)))
    Bp = (G[1]-n*G[0]/r)/2; Bpd = (G[2]-n*G[1]/r+n*G[0]/r**2)/2; Bpdd = (G[3]-n*G[2]/r+2*n*G[1]/r**2-2*n*G[0]/r**3)/2
    Bm = -(G[1]+n*G[0]/r)/2; Bmd = -(G[2]+n*G[1]/r-n*G[0]/r**2)/2; Bmdd = -(G[3]+n*G[2]/r-2*n*G[1]/r**2+2*n*G[0]/r**3)/2
    addB(n+1, Bp, Bpd, Bpdd); addB(n-1, Bm, Bmd, Bmdd)
    Psi = {}
    def addP(K, P, Pd):
        if K < 0: K, P, Pd = -K, -P, -Pd
        if K == 0: return
        Psi[K] = (P, Pd) if K not in Psi else (Psi[K][0]+P, Psi[K][1]+Pd)
    for M, (b, bd, bdd) in B.items():
        # (b' - M b/r)/2 at K=M+1 ; derivative: (b'' - M b'/r + M b/r^2)/2
        addP(M+1, (bd-M*b/r)/2, (bdd-M*bd/r+M*b/r**2)/2)
        addP(M-1, (bd+M*b/r)/2, (bdd+M*bd/r-M*b/r**2)/2)
    return Psi

class FieldSlots:
    """per generator, the radial coefficient arrays per angular slot; slot key = (angtype, N)"""
    pass

def generator_slots(gen, mesh, c, Pleg):
    """returns dict fieldname -> list of (angtype, N, radial tensor) for fields f, fx, fy, psix (sin), psiy (cos), q (=psix/y), T (=transport/y)"""
    if gen.is_direct():
        G, Gt = gen.G_direct(mesh, 5); G = G[:5]
    else:
        Yj, Ytj = gen.Y_jets(mesh, 4, Pleg)
        G = radial_derivs(gen.p, Yj, mesh, 4)
        Gt = radial_derivs(gen.p-1, Ytj, mesh, 4)
    n = gen.n; r = mesh.r
    A = rho_coeffs(G, n, mesh); At = rho_coeffs(Gt, n, mesh)
    kappa = gen.kappa(c)
    out = {k: [] for k in ('f', 'fx', 'fy', 'psix', 'psiy', 'q', 'T')}
    def put(field, typ, N, rad):
        if N < 0:
            N = -N; rad = -rad if typ != 'cos' else rad
        if N == 0 and typ in ('S', 'sin', 'sU', 'scdU'): return
        out[field].append((typ, N, rad))
    for N, (a, ad) in A.items():
        put('f', 'S', N, a/r)
        put('T', 'S', N, (kappa*a-2*c*At[N][0])/r)
        # rho_x -> f_x
        put('fx', 'S', N+1, (ad-N*a/r)/2/r); put('fx', 'S', N-1, (ad+N*a/r)/2/r)
        # f_y = sin th [ (a/r)' U_{N-1} - (cos th / r)(a/r) U'_{N-1} ]
        put('fy', 'sU', N, ad/r-a/r**2); put('fy', 'scdU', N, -(a/r)/r)
    Psi = psi_coeffs(G, n, mesh)
    for K, (P, Pd) in Psi.items():
        put('psix', 'sin', K+1, (Pd-K*P/r)/2); put('psix', 'sin', K-1, (Pd+K*P/r)/2)
        put('q', 'S', K+1, (Pd-K*P/r)/2/r); put('q', 'S', K-1, (Pd+K*P/r)/2/r)
        put('psiy', 'cos', K-1, (Pd+K*P/r)/2); put('psiy', 'cos', K+1, (-Pd+K*P/r)/2)
    return out

FIELDS = ('f', 'fx', 'fy', 'psix', 'psiy', 'q', 'T')

class Basis:
    """a list of generators with precomputed radial slots on a mesh"""
    def __init__(self, gens, mesh, c):
        self.gens = gens; self.mesh = mesh; self.c = float(c); self.n = len(gens)
        nleg = max([int(g.spec[2]) for g in gens if g.spec[0] in ('leg', 'legq')], default=0)
        Pleg = legendre_t_jets(mesh.t, nleg, 6) if nleg >= 0 else None
        self.slots = [generator_slots(g, mesh, self.c, Pleg) for g in gens]
        self.Nmax = max(N for sl in self.slots for f in FIELDS for (_, N, _) in sl[f])+2
        self.tab = mesh.angular_tables(self.Nmax)
    def field_matrix(self, field, idx):
        """(Nr, Nt, len(idx)) tensor of field values of generators idx"""
        mesh = self.mesh
        out = torch.zeros(mesh.Nr, mesh.Nt, len(idx), dtype=DT, device=mesh.device)
        for j, i in enumerate(idx):
            for typ, N, rad in self.slots[i][field]:
                out[:, :, j] += rad[:, None]*self.tab[typ][N][None, :]
        return out
    def total_fields(self, a):
        """fields of the state with coefficient vector a (torch, n): dict field -> (Nr, Nt)"""
        mesh = self.mesh; a = torch.as_tensor(a, dtype=DT, device=mesh.device)
        out = {}
        for field in FIELDS:
            acc = {}
            for i in range(self.n):
                ai = a[i]
                for typ, N, rad in self.slots[i][field]:
                    key = (typ, N)
                    acc[key] = acc[key]+ai*rad if key in acc else ai*rad
            tot = torch.zeros(mesh.Nr, mesh.Nt, dtype=DT, device=mesh.device)
            for (typ, N), rad in acc.items(): tot += rad[:, None]*self.tab[typ][N][None, :]
            out[field] = tot
        return out
    def residual_Rf(self, a):
        """R_f on the mesh and the fields"""
        Fd = self.total_fields(a)
        # note: T/y = c x f_x + c y f_y + (c-1) f already contains the (c-1) f part of q f; Fd['q'] is psi_x/y only
        Rf = Fd['T']-Fd['psiy']*Fd['fx']+Fd['psix']*Fd['fy']+Fd['q']*Fd['f']
        return Rf, Fd
    def jacobian_Rf(self, Fd, block=64):
        """dR_f/da (Nr*Nt, n) given current fields Fd"""
        mesh = self.mesh; J = torch.zeros(mesh.Nr*mesh.Nt, self.n, dtype=DT, device=mesh.device)
        for b0 in range(0, self.n, block):
            idx = list(range(b0, min(self.n, b0+block)))
            M = self.field_matrix('T', idx)
            M -= Fd['psiy'][:, :, None]*self.field_matrix('fx', idx)
            M -= Fd['fx'][:, :, None]*self.field_matrix('psiy', idx)
            M += Fd['psix'][:, :, None]*self.field_matrix('fy', idx)
            M += Fd['fy'][:, :, None]*self.field_matrix('psix', idx)
            M += Fd['q'][:, :, None]*self.field_matrix('f', idx)
            M += Fd['f'][:, :, None]*self.field_matrix('q', idx)
            J[:, b0:b0+len(idx)] = M.reshape(-1, len(idx))
        return J

A_REF = 23.95065822465609

def J_abs(Rf, mesh):
    """(1/(pi a_ref^2)) int R_f^2 ds dtheta on the product mesh"""
    return float(torch.sum(mesh.W*Rf*Rf)/(math.pi*A_REF**2))

# ------------------------------------------------------------------ case4 state -> generators (T1 internal coordinates, well conditioned)
def case4_generators(J, c):
    """From a case4 checkpoint JSON: list of (Generator, coef) in internal T1 form: 60 low monomials + 800 Legendre. a_000 analytic (from exact)."""
    import sys
    from fractions import Fraction
    gamma = 1/c; lam = 1-gamma
    def p_of(j): return (3+gamma-j*lam)/2
    P = [float.fromhex(h) for h in J['P_hex']]; high = [float.fromhex(h) for h in J['high_hex']]
    NN = [float.fromhex(h) for h in J['frozen_Nn_hex']]
    LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]
    HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
    gens = []; coefs = []
    a000 = float(J['a000_analytic_decimal'])
    for v, (m, k, j) in zip(P, LOW):
        gens.append(Generator(m, p_of(j), ('mono', k-m))); coefs.append(a000 if (m, k, j) == (0, 0, 0) else v)
    for v, (m, n, j) in zip(high, HIGH):
        gens.append(Generator(m, p_of(j), ('leg', max(5-m, 0), n))); coefs.append(v*NN[n])
    return gens, np.array(coefs)


def panel_edge_radius(k, origin_radius=0.02, upper_log_radius=16., panel_width=1.):
    """radius of the k-th middle-panel edge of the whole-axis rule (edges equally spaced between log r0 and S)"""
    lo = math.log(origin_radius); S = upper_log_radius
    npan = max(1, int(math.ceil((S-lo)/panel_width)))
    return math.exp(lo+k*(S-lo)/npan)
