"""
bq3core.py  --  core discretisation for the B2 Boussinesq self-similar profile problem.

Representation (half plane x >= 0, phi = theta + pi/2 in [0, pi], eta = cos(phi) = -y/r, x = r sin(phi)):
    Theta = x^2 F,   Omega = x G,   Psi = x H,
    F = sum_k f_k(r) cos(k phi),  G = sum_k g_k(r) cos(k phi),      k = 0..K-1
    f_k(r) = D(t) t^{m_k} sum_j c^F[k,j] B_j(t),   g_k likewise with c^G,
    t = 1 - (L/(r+L))^{1/beta}  (so r = L((1-t)^{-beta} - 1)),
    D_F(t) = (1-t)^{beta+2} ~ r^{-(1+2/beta)} (F tail),  D_G(t) = (1-t)^{beta+1} ~ r^{-(1+1/beta)} (G tail, SPEC sec. 5),
    m_k = min(k, m_reg) enforces f_k = O(r^{m_k}) at the centre.
Omega has sine modes: Omega = sum_{k>=1} Omega_k(r) sin(k phi), Omega_1 = r(g_0 - g_2/2), Omega_k = (r/2)(g_{k-1}-g_{k+1}).
Full-plane inverse (odd in x): Psi_k = (r/2k)(I^-_k + I^+_k), Psi_k' = (I^+_k - I^-_k)/2 with
    I^-_k(r) = int_0^r (rho/r)^{k+1} Omega_k(rho) drho,   I^+_k(r) = int_r^inf (r/rho)^{k-1} Omega_k(rho) drho,
and for k = 1 the once-subtracted form I^+_1 -> -int_0^r Omega_1 drho (removes the uniform vertical velocity,
so that U(0) = 0 exactly and W = beta X + U).
Reduced equations (desingularised):
    R_F = 2A(F + sF_s) + B F_y - (beta-2)F,     R_G = A(G + 2sG_s) + B G_y + G - 2(F + sF_s),
    A = beta - H_y,  B = beta y + U_2,  (U_2(0) = 0).
Cartesian residuals: R_Theta = x^2 R_F, R_Omega = x R_G; normalisers N_Theta = x^2 N_F, N_Omega = |x| N_G.
"""
import numpy as np
import torch
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import BSpline

DT = torch.float64


def gauss_on_intervals(edges, ng):
    """Gauss-Legendre nodes/weights on consecutive intervals given by edges (1D array)."""
    xg, wg = leggauss(ng)
    a = edges[:-1][:, None]
    b = edges[1:][:, None]
    nodes = (0.5 * (b - a) * xg[None, :] + 0.5 * (b + a)).ravel()
    weights = (0.5 * (b - a) * wg[None, :]).ravel()
    return nodes, weights


class Basis:
    """Radial B-spline basis on t in [0,1] (clamped, uniform knots) and angular cosine/sine modes."""

    def __init__(self, Nt, deg, K, Nphi, ng_coll=3, ng_quad=12, m_reg=2, device="cuda", knots=None, grade=1.0):
        self.Nt, self.deg, self.K, self.Nphi = Nt, deg, K, Nphi
        self.m_reg = m_reg
        self.grade = grade
        self.device = device
        if knots is None:
            inner = np.linspace(0.0, 1.0, Nt + 1) ** grade
        else:
            inner = np.asarray(knots, dtype=float)
            self.Nt = Nt = len(inner) - 1
        self.edges = inner
        self.knots = np.concatenate([np.zeros(deg), inner, np.ones(deg)])
        self.Nb = len(self.knots) - deg - 1
        # collocation nodes in t: Gauss points per knot interval
        self.t_coll, self.w_coll = gauss_on_intervals(inner, ng_coll)
        self.Nc = len(self.t_coll)
        # quadrature nodes for the radial integrals: full intervals (Gauss), last interval geometrically refined
        edges_q = list(inner[:-1])
        last_a = inner[-2]
        h = 1.0 - last_a
        sub = [last_a]
        while h > 1e-13:
            h *= 0.5
            sub.append(1.0 - h)
        sub.append(1.0)
        edges_q = np.array(edges_q + sub[1:])
        self.t_quad, self.w_quad = gauss_on_intervals(edges_q, ng_quad)
        self.edges_q = edges_q
        self.ng_quad = ng_quad
        # angular nodes
        j = np.arange(Nphi)
        self.phi = np.pi * (j + 0.5) / Nphi
        self.eta = np.cos(self.phi)
        self.sphi = np.sin(self.phi)
        kk = np.arange(K)
        self.C = np.cos(np.outer(self.phi, kk))          # Nphi x K  cos(k phi)
        self.S = np.sin(np.outer(self.phi, kk))          # Nphi x K  sin(k phi)
        ks = np.arange(1, K + 1)
        self.Ssin = np.sin(np.outer(self.phi, ks))       # Nphi x K  sin(k phi), k=1..K  (Omega modes)
        self.Csin = np.cos(np.outer(self.phi, ks))
        # Chebyshev U_{k-1}(eta) = sin(k phi)/sin(phi), k = 1..K, and its derivative
        U = np.zeros((Nphi, K))
        dU = np.zeros((Nphi, K))
        U[:, 0] = 1.0
        if K > 1:
            U[:, 1] = 2 * self.eta
            dU[:, 1] = 2.0
        for k in range(2, K):
            U[:, k] = 2 * self.eta * U[:, k - 1] - U[:, k - 2]
            dU[:, k] = 2 * U[:, k - 1] + 2 * self.eta * dU[:, k - 1] - dU[:, k - 2]
        self.U = U
        self.dU = dU
        self.mk = np.minimum(kk, m_reg)            # mask count for the r-map: j >= min(k, m_reg)
        self.mk2 = np.minimum(kk // 2, self.Nb - 2) if hasattr(self, 'Nb') else kk // 2   # r2-map: j >= floor(k/2) (no cap; astra review)
        self.kodd = (kk % 2).astype(float)
        # spline design matrices at collocation and quadrature nodes
        self.B_coll, self.dB_coll = self._design(self.t_coll)
        self.B_quad, self.dB_quad = self._design(self.t_quad)
        self.to_torch()

    def _design(self, t):
        spl = BSpline(self.knots, np.eye(self.Nb), self.deg, extrapolate=False)
        t = np.clip(t, 0.0, 1.0 - 1e-16)
        B = spl(t)
        dB = spl.derivative()(t)
        B = np.nan_to_num(B)
        dB = np.nan_to_num(dB)
        return B, dB

    def to_torch(self):
        d = self.device
        for name in ["t_coll", "w_coll", "t_quad", "w_quad", "phi", "eta", "sphi", "C", "S", "Ssin", "Csin",
                     "U", "dU", "B_coll", "dB_coll", "B_quad", "dB_quad"]:
            setattr(self, name + "_t", torch.tensor(getattr(self, name), dtype=DT, device=d))
        self.mk_t = torch.tensor(self.mk, dtype=torch.long, device=d)


class Geometry:
    """beta-dependent quantities: map, radial factors, modal inverse matrices, design operators.
    rmap = 'r' (t ~ r near 0) or 'r2' (t ~ r^2 near 0, odd modes times rho_odd)."""

    def __init__(self, basis, beta, L, rmap='r'):
        self.b = basis
        self.beta = float(beta)
        self.L = float(L)
        self.rmap = rmap
        b = basis
        dev = b.device
        self.dev = dev
        beta_t = torch.tensor(self.beta, dtype=DT, device=dev)
        L_t = torch.tensor(self.L, dtype=DT, device=dev)
        self.beta_t, self.L_t = beta_t, L_t
        self.pF = self.beta + 2          # D_F = (1-t)^{pF} ~ r^{-(1+2/beta)}
        self.pG = self.beta + 1          # D_G = (1-t)^{pG} ~ r^{-(1+1/beta)}
        t = b.t_coll_t
        self.r, self.drdt = self.r_of_t(t)
        tq = b.t_quad_t
        self.rq, self.drdtq = self.r_of_t(tq)
        K, Nb = b.K, b.Nb
        # masks per mode
        mcount = b.mk if rmap == 'r' else b.mk2
        mask = torch.ones(K, Nb, dtype=DT, device=dev)
        for k in range(K):
            mask[k, :int(mcount[k])] = 0.0
        self.mask_k = mask
        self.active = (mask > 0).reshape(-1)
        # design stacks per field and mode: R0k[k] = fac_k(t) B_j(t) mask, R1k = d/dr
        def design(pw):
            R0 = torch.zeros(K, b.Nc, Nb, dtype=DT, device=dev); R1 = torch.zeros_like(R0)
            for k in range(K):
                fac, dfac = self.radial_factor(k, t, pw)
                R0[k] = fac[:, None] * b.B_coll_t * mask[k][None, :]
                R1[k] = ((dfac[:, None] * b.B_coll_t + fac[:, None] * b.dB_coll_t) / self.drdt[:, None]) * mask[k][None, :]
            return R0, R1
        self.R0kF, self.R1kF = design(self.pF)
        self.R0kG, self.R1kG = design(self.pG)
        # elementary vorticity radial functions at quadrature nodes per g-mode k': omega_{k'j}(rho) = rho fac_{k'}(tq) B_j(tq) mask
        self.Wq_k = []
        for k in range(K):
            fac, _ = self.radial_factor(k, tq, self.pG)
            self.Wq_k.append((self.rq * fac)[:, None] * b.B_quad_t * mask[k][None, :])     # Nq x Nb
        self._build_inverse()
        self._build_design()

    # ------------------------------------------------------------------ map and factors
    def r_of_t(self, t):
        beta, L = self.beta_t, self.L_t
        if self.rmap == 'r':
            r = L * ((1 - t) ** (-beta) - 1)
            drdt = L * beta * (1 - t) ** (-beta - 1)
        else:
            u = L ** 2 * ((1 - t) ** (-2 * beta) - 1)
            r = torch.sqrt(u)
            drdt = beta * L ** 2 * (1 - t) ** (-2 * beta - 1) / r
        return r, drdt

    def t_of_r(self, r):
        beta, L = self.beta_t, self.L_t
        if self.rmap == 'r':
            return 1 - (L / (r + L)) ** (1.0 / beta)
        return 1 - (L ** 2 / (r ** 2 + L ** 2)) ** (1.0 / (2 * beta))

    def radial_factor(self, k, t, pw):
        """fac_k(t) = (1-t)^pw [ * rho_odd(t) if k odd and rmap == 'r2' ];  returns (fac, dfac/dt)."""
        beta = self.beta_t
        D = (1 - t) ** pw
        dD = -pw * (1 - t) ** (pw - 1)
        if self.rmap == 'r2' and (k % 2 == 1):
            w = (1 - t) ** (2 * beta)
            rho = torch.sqrt(1 - w)
            drho = beta * (1 - t) ** (2 * beta - 1) / rho
            return D * rho, dD * rho + D * drho
        return D, dD

    def g1prime0(self, cG):
        """g_1'(0) for the stored representation (cG: (..., K*Nb))."""
        b = self.b; Nb = b.Nb
        if self.rmap == 'r':
            _, dB0 = b._design(np.array([0.0]))
            return cG[..., Nb + 1] * float(dB0[0, 1]) / (self.beta * self.L)      # c_{11} B_1'(0) dt/dr(0)
        return cG[..., Nb] / self.L                                              # c_{10} * d(rho_odd)/dr(0) = c_{10}/L

    # ------------------------------------------------------------------ modal inverse
    def _cum_matrices(self):
        b = self.b
        tq = b.t_quad; wq = b.w_quad; tc = b.t_coll
        Nc, Nq = len(tc), len(tq)
        edges = b.edges_q
        idx = np.searchsorted(edges, tc, side="right") - 1
        ng = b.ng_quad
        Wlow = np.zeros((Nc, Nq)); Whigh = np.zeros((Nc, Nq))
        for i in range(Nc):
            Wlow[i, : idx[i] * ng] = wq[: idx[i] * ng]
            Whigh[i, (idx[i] + 1) * ng:] = wq[(idx[i] + 1) * ng:]
        xg, wg = leggauss(ng)
        a = edges[idx]; bb = edges[idx + 1]
        tpl = 0.5 * (tc - a)[:, None] * xg[None, :] + 0.5 * (tc + a)[:, None]
        wpl = 0.5 * (tc - a)[:, None] * wg[None, :]
        tph = 0.5 * (bb - tc)[:, None] * xg[None, :] + 0.5 * (bb + tc)[:, None]
        wph = 0.5 * (bb - tc)[:, None] * wg[None, :]
        return Wlow, Whigh, tpl, wpl, tph, wph

    def _build_inverse(self):
        """Im[(k,kg)], Ip[(k,kg)]: Nc x Nb matrices giving I^-_k, I^+_k (k = 1 subtracted) of the elementary vorticity
        functions of g-mode kg at the collocation radii."""
        b = self.b; dev = self.dev
        Wlow, Whigh, tpl, wpl, tph, wph = self._cum_matrices()
        Wlow = torch.tensor(Wlow, dtype=DT, device=dev); Whigh = torch.tensor(Whigh, dtype=DT, device=dev)
        Bpl, _ = b._design(tpl.ravel()); Bph, _ = b._design(tph.ravel())
        Bpl = torch.tensor(Bpl, dtype=DT, device=dev).reshape(b.Nc, -1, b.Nb)
        Bph = torch.tensor(Bph, dtype=DT, device=dev).reshape(b.Nc, -1, b.Nb)
        tpl = torch.tensor(tpl, dtype=DT, device=dev); wpl = torch.tensor(wpl, dtype=DT, device=dev)
        tph = torch.tensor(tph, dtype=DT, device=dev); wph = torch.tensor(wph, dtype=DT, device=dev)
        rpl, drpl = self.r_of_t(tpl); rph, drph = self.r_of_t(tph)
        r = self.r; rq = self.rq
        K = b.K
        with torch.no_grad():
            lr = torch.log(r)[:, None]; lrq = torch.log(rq)[None, :]
            lrpl = torch.log(rpl); lrph = torch.log(rph)
        self.Im = {}; self.Ip = {}
        for k in range(1, K + 1):
            Km = torch.exp((k + 1) * torch.clamp(lrq - lr, max=0.0)) * Wlow * self.drdtq[None, :]
            Kp = torch.exp((k - 1) * torch.clamp(lr - lrq, max=0.0)) * Whigh * self.drdtq[None, :] if k >= 2 else None
            Kpl = torch.exp((k + 1) * torch.clamp(lrpl - lr, max=0.0))
            Kph = torch.exp((k - 1) * torch.clamp(lr - lrph, max=0.0)) if k >= 2 else None
            for kg in (k - 1, k + 1):
                if kg < 0 or kg >= K:
                    continue
                Wq = self.Wq_k[kg]
                maskm = self.mask_k[kg]
                facpl, _ = self.radial_factor(kg, tpl, self.pG)
                facph, _ = self.radial_factor(kg, tph, self.pG)
                wpl_f = rpl * facpl * drpl * wpl
                Im = Km @ Wq + torch.einsum("ig,ig,igj->ij", Kpl, wpl_f, Bpl * maskm)
                if k >= 2:
                    wph_f = rph * facph * drph * wph
                    Ip = Kp @ Wq + torch.einsum("ig,ig,igj->ij", Kph, wph_f, Bph * maskm)
                else:
                    I0 = (Wlow * self.drdtq[None, :]) @ Wq + torch.einsum("ig,igj->ij", wpl_f, Bpl * maskm)
                    Ip = -I0
                self.Im[(k, kg)] = Im; self.Ip[(k, kg)] = Ip

    # ------------------------------------------------------------------ design operators
    def _build_design(self):
        b = self.b
        K, Nb, Nc, Nphi = b.K, b.Nb, b.Nc, b.Nphi
        C, S = b.C_t, b.S_t
        r = self.r
        sphi, eta = b.sphi_t, b.eta_t
        kk = torch.arange(K, dtype=DT, device=self.dev)
        def ops(R0k, R1k):
            Phi0 = torch.einsum("jk,kia->ijka", C, R0k)
            Phir = torch.einsum("jk,kia->ijka", C, R1k)
            Phiphi = -torch.einsum("jk,k,kia->ijka", S, kk, R0k)
            xdx = (r[:, None] * sphi[None, :] ** 2)[..., None, None] * Phir + (sphi * eta)[None, :, None, None] * Phiphi
            dy = -eta[None, :, None, None] * Phir + (sphi[None, :] / r[:, None])[..., None, None] * Phiphi
            return (Phi0.reshape(Nc * Nphi, K * Nb), (Phi0 + 0.5 * xdx).reshape(Nc * Nphi, K * Nb),
                    (Phi0 + xdx).reshape(Nc * Nphi, K * Nb), dy.reshape(Nc * Nphi, K * Nb))
        self.Phi0F, self.Phi1F, _, self.PhiyF = ops(self.R0kF, self.R1kF)
        self.Phi0G, _, self.Phi2G, self.PhiyG = ops(self.R0kG, self.R1kG)
        # Psi_k, Psi_k' at radii as (Nc x K*Nb) operators on cG, for sine modes k = 1..K
        Psi = torch.zeros(K, Nc, K * Nb, dtype=DT, device=self.dev); dPsi = torch.zeros_like(Psi)
        for k in range(1, K + 1):
            Im_terms = torch.zeros(Nc, K * Nb, dtype=DT, device=self.dev); Ip_terms = torch.zeros_like(Im_terms)
            for (kg, wgt) in [(k - 1, 1.0 if k == 1 else 0.5), (k + 1, -0.5)]:
                if kg < 0 or kg >= K:
                    continue
                Im_terms[:, kg * Nb:(kg + 1) * Nb] += wgt * self.Im[(k, kg)]
                Ip_terms[:, kg * Nb:(kg + 1) * Nb] += wgt * self.Ip[(k, kg)]
            Psi[k - 1] = (r / (2 * k))[:, None] * (Im_terms + Ip_terms)
            dPsi[k - 1] = 0.5 * (Ip_terms - Im_terms)
        self.Psi_op = Psi; self.dPsi_op = dPsi
        U, dU = b.U_t, b.dU_t
        hk = Psi / r[None, :, None]
        dhk = dPsi / r[None, :, None] - Psi / (r ** 2)[None, :, None]
        H = torch.einsum("jk,kia->ija", U, hk)
        Hr = torch.einsum("jk,kia->ija", U, dhk)
        Hphi_term = torch.einsum("jk,kia->ija", dU, hk)
        Hy = -eta[None, :, None] * Hr - ((1 - eta ** 2)[None, :] / r[:, None])[..., None] * Hphi_term
        ks = torch.arange(1, K + 1, dtype=DT, device=self.dev)
        Psir = torch.einsum("jk,kia->ija", b.Ssin_t, dPsi)
        Psiphi = torch.einsum("jk,k,kia->ija", b.Csin_t, ks, Psi)
        U2 = sphi[None, :, None] * Psir + (eta[None, :] / r[:, None])[..., None] * Psiphi
        U1 = eta[None, :, None] * Psir - (sphi[None, :] / r[:, None])[..., None] * Psiphi
        PsiV = torch.einsum("jk,kia->ija", b.Ssin_t, Psi)
        N = K * Nb
        self.M_H = H.reshape(Nc * Nphi, N); self.M_Hy = Hy.reshape(Nc * Nphi, N)
        self.M_U2 = U2.reshape(Nc * Nphi, N); self.M_U1 = U1.reshape(Nc * Nphi, N); self.M_Psi = PsiV.reshape(Nc * Nphi, N)
        self.x = (r[:, None] * sphi[None, :]).reshape(-1)
        self.y = (-r[:, None] * eta[None, :]).reshape(-1)
        self.rr = (r[:, None] * torch.ones_like(sphi)[None, :]).reshape(-1)
        self._build_centre_ops()

    def _build_centre_ops(self):
        """c = Psi_xy(0) = -(1/2) int_0^inf Omega_2/rho drho (Omega_2 = (r/2)(g_1 - g_3));
        v0 = (1/2) int_0^inf Omega_1 drho (Omega_1 = r(g_0 - g_2/2)), divergent for the generic tail."""
        b = self.b; K, Nb = b.K, b.Nb
        wq = b.w_quad_t * self.drdtq
        cvec = torch.zeros(K * Nb, dtype=DT, device=self.dev); v0vec = torch.zeros_like(cvec)
        for (kg, wgt) in [(1, 0.5), (3, -0.5)]:
            if kg < K:
                cvec[kg * Nb:(kg + 1) * Nb] += -0.5 * wgt * ((wq / self.rq) @ self.Wq_k[kg])
        for (kg, wgt) in [(0, 1.0), (2, -0.5)]:
            if kg < K:
                v0vec[kg * Nb:(kg + 1) * Nb] += 0.5 * wgt * (wq @ self.Wq_k[kg])
        self.c_op = cvec; self.v0_op = v0vec


def fields_at(basis, beta_b, L, rmap, cF, cG, x, y):
    """Evaluate F and G of a stored representation at arbitrary points (x > 0)."""
    g = Geometry.__new__(Geometry)
    g.b = basis; g.beta = float(beta_b); g.L = float(L); g.rmap = rmap
    g.beta_t = torch.tensor(g.beta, dtype=DT, device=x.device); g.L_t = torch.tensor(g.L, dtype=DT, device=x.device)
    g.pF = g.beta + 2; g.pG = g.beta + 1
    r = torch.sqrt(x ** 2 + y ** 2)
    t = g.t_of_r(r)
    phi = torch.atan2(x, -y)
    spl = BSpline(basis.knots, np.eye(basis.Nb), basis.deg, extrapolate=False)
    Bv = torch.tensor(np.nan_to_num(spl(np.clip(t.cpu().numpy(), 0, 1 - 1e-16))), dtype=DT, device=x.device)
    K, Nb = basis.K, basis.Nb
    mcount = basis.mk if rmap == 'r' else basis.mk2
    F = torch.zeros_like(x); G = torch.zeros_like(x)
    for k in range(K):
        ck = torch.cos(k * phi)
        facF, _ = g.radial_factor(k, t, g.pF); facG, _ = g.radial_factor(k, t, g.pG)
        m = int(mcount[k])
        cFk = cF[k * Nb:(k + 1) * Nb].clone(); cGk = cG[k * Nb:(k + 1) * Nb].clone()
        cFk[:m] = 0; cGk[:m] = 0
        F = F + facF * ck * (Bv @ cFk)
        G = G + facG * ck * (Bv @ cGk)
    return F, G


class Problem:
    """Residuals and Jacobian for given basis/geometry."""

    def __init__(self, geom, beta_dyn=None):
        self.g = geom
        self.b = geom.b
        self.beta = geom.beta if beta_dyn is None else float(beta_dyn)

    def fields(self, cF, cG):
        g = self.g
        F = g.Phi0F @ cF
        F1 = g.Phi1F @ cF         # F + s F_s
        Fy = g.PhiyF @ cF
        G = g.Phi0G @ cG
        G2 = g.Phi2G @ cG         # G + 2 s G_s
        Gy = g.PhiyG @ cG
        Hy = g.M_Hy @ cG
        U2 = g.M_U2 @ cG
        A = self.beta - Hy
        B = self.beta * g.y + U2
        return dict(F=F, F1=F1, Fy=Fy, G=G, G2=G2, Gy=Gy, Hy=Hy, U2=U2, A=A, B=B)

    def residuals(self, cF, cG, f=None):
        g = self.g
        if f is None:
            f = self.fields(cF, cG)
        beta = self.beta
        RF = 2 * f["A"] * f["F1"] + f["B"] * f["Fy"] - (beta - 2) * f["F"]
        RG = f["A"] * f["G2"] + f["B"] * f["Gy"] + f["G"] - 2 * f["F1"]
        NF = 2 * f["A"].abs() * f["F1"].abs() + f["B"].abs() * f["Fy"].abs() + abs(beta - 2) * f["F"].abs()
        NG = f["A"].abs() * f["G2"].abs() + f["B"].abs() * f["Gy"].abs() + f["G"].abs() + 2 * f["F1"].abs()
        return RF, RG, NF, NG

    def jacobian(self, cF, cG, f=None):
        """Jacobian of (RF, RG) w.r.t. (cF, cG) at fixed beta. Returns J of shape (2 Npts, 2 N)."""
        g = self.g
        if f is None:
            f = self.fields(cF, cG)
        beta = self.beta
        A, B = f["A"], f["B"]
        JFF = 2 * A[:, None] * g.Phi1F + B[:, None] * g.PhiyF - (beta - 2) * g.Phi0F
        JFG = -2 * f["F1"][:, None] * g.M_Hy + f["Fy"][:, None] * g.M_U2
        JGF = -2 * g.Phi1F
        JGG = A[:, None] * g.Phi2G + B[:, None] * g.PhiyG + g.Phi0G - f["G2"][:, None] * g.M_Hy + f["Gy"][:, None] * g.M_U2
        return torch.cat([torch.cat([JFF, JFG], 1), torch.cat([JGF, JGG], 1)], 0)
