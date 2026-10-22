"""
Core library: Boussinesq Setting A2 (fourfold parity, x^2 y leading temperature).

Representation (polar, first quadrant = exact parity reduction):
  Theta = x^2 y a(r,th),  Omega = x y G(r,th),  Psi = x y H(r,th),
  a, G even in x and in y (so smooth even-even functions):
     a(r,th) = sum_{l=0}^{M-1} alpha_l(r) cos(2 l th),  alpha_l(r) = P_{2l}(xi) q_l(xi),
     P_j(xi) = ((1+xi)/2)^{j/2} (1-xi)^{sigma},  q_l = sum_n c[l,n] T_n(xi),
  with the radial map xi = (r^2-L^2)/(r^2+L^2)  (r=0 -> xi=-1, r=inf -> xi=+1),
  so that any polynomial q(xi) is a smooth even function of r, rho^j = ((1+xi)/2)^{j/2} = (r/sqrt(r^2+L^2))^j
  gives the r^j behaviour of the j-th angular mode at the origin, and (1-xi)^sigma ~ (2L^2/r^2)^sigma the far field.

Canonical full-plane Biot-Savart inverse (parity class: Psi odd-odd, sine modes k = 2,4,...):
  -Delta Psi = Omega, Omega = sum_k b_k(r) sin(k th),  Psi = sum_k h_k(r) sin(k th),
  h_k(r) = (1/2k) [ r^{-k} int_0^r s^{k+1} b_k ds + r^k int_r^inf s^{1-k} b_k ds ].
  This is the unique solution with U = o(|X|) and regular at the origin (the homogeneous solutions r^k sin k th
  give |U| ~ r^{k-1} >= r, r^{-k} is singular). It converges iff the k=2 mode b_2 decays (b_2 = O(r^{-eps})).
  The integrals are computed by Gauss-Jacobi (outer) and composite Gauss-Legendre in u = log(2/(1-t)) (inner),
  acting on Chebyshev coefficients of the smooth part q_k of b_k = L^2 (1-xi)^sigma_Om rho^k q_k(xi).

Everything in float64 torch (GPU if available).
"""
import math
import numpy as np
import torch
from scipy.special import roots_jacobi, roots_legendre

DT = torch.float64


def cheb_gauss_nodes(N):
    """Chebyshev-Gauss nodes (interior), ascending."""
    i = np.arange(N)
    return np.sort(np.cos((2 * i + 1) * np.pi / (2 * N)))


def cheb_T(xi, Nq):
    """T_n(xi), n=0..Nq-1, for xi in [-1,1] (numpy). Returns [len(xi), Nq]."""
    xi = np.asarray(xi, dtype=np.float64)
    phi = np.arccos(np.clip(xi, -1.0, 1.0))
    n = np.arange(Nq)
    return np.cos(np.outer(phi, n))


def cheb_T_deriv(xi, Nq):
    """dT_n/dxi and d2T_n/dxi2 at xi (handles endpoints by limits). Returns (dT, d2T) each [len(xi), Nq]."""
    xi = np.asarray(xi, dtype=np.float64)
    n = np.arange(Nq, dtype=np.float64)
    dT = np.empty((len(xi), Nq)); d2T = np.empty((len(xi), Nq))
    inner = np.abs(xi) < 1 - 1e-13
    phi = np.arccos(np.clip(xi[inner], -1.0, 1.0))
    s = np.sin(phi)
    sn = np.sin(np.outer(phi, n)); cn = np.cos(np.outer(phi, n))
    dT[inner] = n * sn / s[:, None]
    d2T[inner] = -n * (n * cn * s[:, None] - sn * np.cos(phi)[:, None]) / (s ** 3)[:, None]
    for idx in np.where(~inner)[0]:
        sg = 1.0 if xi[idx] > 0 else -1.0
        dT[idx] = (sg ** (n + 1)) * n ** 2
        d2T[idx] = (sg ** n) * n ** 2 * (n ** 2 - 1) / 3.0
    return dT, d2T


def cheb_mult_1pxi_half(c):
    """Chebyshev coefficients of ((1+xi)/2) * q for q with coefficients c (torch, last axis = n). Degree +1."""
    # xi T_n = (T_{n+1} + T_{n-1})/2, with T_{-1} := T_1 (xi T_0 = T_1).
    Nn = c.shape[-1]
    out = torch.zeros(c.shape[:-1] + (Nn + 1,), dtype=c.dtype, device=c.device)
    out[..., :Nn] += c / 2.0
    out[..., 1:Nn + 1] += c / 4.0            # T_{n+1} part
    out[..., 0:Nn - 1] += c[..., 1:] / 4.0   # T_{n-1} part for n>=1 ... n-1 index
    out[..., 1] += c[..., 0] / 4.0           # n=0: xi T_0 = T_1  (full weight 1/2 * 1/2)
    # careful: for n=0, xi*T_0 = T_1 (not (T_1+T_{-1})/2 with T_{-1}=T_1 gives T_1 as well). We added c0/4 to T_1
    # via the T_{n+1} part and c0/4 again here, total c0/2 * T_1 = (1/2) xi T_0 contribution. Correct.
    return out


class Quadrature:
    """Green-operator matrices for mode k with far-field exponent sigma on target points xi_e.
    Hin[e,n], Hout[e,n] act on Chebyshev coefficients (degree < Nq) of q_k, where b_k = L^2 (1-xi)^sigma rho^k q_k:
      r^{-k} I_in  = L^4 Hin qhat,   r^k I_out = L^4 Hout qhat,
      h_k(xi_e)   = (L^4 / (2k)) * sum_n (Hin+Hout)[e,n] qhat_n
      h_k'(r_e)   = (L^4 / (2 r_e)) * sum_n (Hout-Hin)[e,n] qhat_n
    """

    def __init__(self, k, sigma, xi_e, Nq, n_gj=None, panel=0.25, n_gl=40):
        self.k, self.sigma, self.Nq = k, float(sigma), Nq
        xi_e = np.asarray(xi_e, dtype=np.float64)
        self.xi_e = xi_e
        E = len(xi_e)
        alpha = k / 2.0 + sigma - 2.0
        assert alpha > -1.0, f"mode k={k}, sigma={sigma}: outer integral diverges (need sigma > 1-k/2)"
        n_gj = n_gj or (Nq // 2 + 4)
        tq, wq = roots_jacobi(n_gj, alpha, 0.0)
        Hout = np.zeros((E, Nq)); Hin = np.zeros((E, Nq))
        for e, xe in enumerate(xi_e):
            if xe >= 1.0 - 1e-15:
                continue  # at infinity: h -> 0 contribution handled as zero (fields decay)
            # outer: int_{xe}^1 (1-t)^alpha T_n(t) dt = ((1-xe)/2)^{alpha+1} sum wq T_n(t(tau))
            t = xe + (1 - xe) * (1 + tq) / 2
            Tn = cheb_T(t, Nq)
            pref = ((1 + xe) / 2) ** (k / 2.0) * (1 - xe) ** (-k / 2.0) * ((1 - xe) / 2) ** (alpha + 1)
            Hout[e] = pref * (wq @ Tn)
            # inner: int_{-1}^{xe} (1+t)^k (1-t)^{sigma-k/2-2} T_n dt, normalised by (1-xe)^{k/2} (1+xe)^{-k/2}
            if xe <= -1.0 + 1e-15:
                continue
            ue = math.log(2.0 / (1 - xe))
            npan = max(1, int(math.ceil(ue / panel)))
            gl_t, gl_w = roots_legendre(n_gl)
            edges = np.linspace(0.0, ue, npan + 1)
            acc = np.zeros(Nq)
            for p in range(npan):
                u0, u1 = edges[p], edges[p + 1]
                u = u0 + (u1 - u0) * (gl_t + 1) / 2
                w = gl_w * (u1 - u0) / 2
                t = 1 - 2 * np.exp(-u)
                dtdu = 2 * np.exp(-u)
                # normalised integrand factors (all <= O(1)):
                f = 2.0 ** (-k / 2.0) * ((1 + t) / (1 + xe)) ** k * (1 + xe) ** (k / 2.0) \
                    * ((1 - xe) / (1 - t)) ** (k / 2.0) * (1 - t) ** (sigma - 2.0) * dtdu
                Tn = cheb_T(t, Nq)
                acc += (w * f) @ Tn
            Hin[e] = acc
        self.Hin, self.Hout = Hin, Hout


def dctII_matrices(M):
    """Angular nodes th_m=(m+1/2) pi/(2M) on (0,pi/2); cosine modes cos(2 l th), l=0..M-1; sine modes sin(2 l th), l=1..M."""
    th = (np.arange(M) + 0.5) * np.pi / (2 * M)
    l = np.arange(M)
    C = np.cos(np.outer(th, 2 * l))           # [m, l]
    S = np.sin(np.outer(th, 2 * (l + 1)))     # [m, l] modes k=2(l+1)
    return th, C, S


class A2Model:
    """Holds grids, basis matrices and Green matrices; evaluates fields and residuals from coefficient vectors."""

    def __init__(self, N, M, L, sigma_a, sigma_G, device=None, xi_eval=None, th_eval=None, origin_rows=True):
        self.N, self.M, self.L = N, M, float(L)
        self.sigma_a, self.sigma_G = float(sigma_a), float(sigma_G)
        self.sigma_Om = self.sigma_G - 1.0
        self.dev = device or (torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
        self.origin_rows = origin_rows
        # evaluation points (default: collocation nodes)
        self.xi = cheb_gauss_nodes(N) if xi_eval is None else np.asarray(xi_eval, dtype=np.float64)
        if th_eval is None:
            self.th, _, _ = dctII_matrices(M)
        else:
            self.th = np.asarray(th_eval, dtype=np.float64)
        self._build()

    def _build(self):
        N, M, L = self.N, self.M, self.L
        xi, th = self.xi, self.th
        dev = self.dev
        self.r = L * np.sqrt((1 + xi) / (1 - xi))
        self.dxidr = self.r * (1 - xi) ** 2 / L ** 2
        # Chebyshev basis at eval points, degree N-1
        T = cheb_T(xi, N); dT, d2T = cheb_T_deriv(xi, N)
        self.T = torch.tensor(T, dtype=DT, device=dev)
        self.dT = torch.tensor(dT, dtype=DT, device=dev)
        # prefactors for even-even fields: mode j=2l: P = ((1+xi)/2)^l (1-xi)^sigma; log-derivative
        l = np.arange(M)
        X = xi[None, :]
        self.Pa = torch.tensor(((1 + X) / 2) ** l[:, None] * (1 - X) ** self.sigma_a, dtype=DT, device=dev)
        self.PG = torch.tensor(((1 + X) / 2) ** l[:, None] * (1 - X) ** self.sigma_G, dtype=DT, device=dev)
        dlogPa = l[:, None] / (1 + X) - self.sigma_a / (1 - X)
        dlogPG = l[:, None] / (1 + X) - self.sigma_G / (1 - X)
        self.dPa = self.Pa * torch.tensor(dlogPa, dtype=DT, device=dev)
        self.dPG = self.PG * torch.tensor(dlogPG, dtype=DT, device=dev)
        # angular matrices at eval angles
        self.C = torch.tensor(np.cos(np.outer(th, 2 * l)), dtype=DT, device=dev)              # [m,l]
        self.dC = torch.tensor(-2 * l[None, :] * np.sin(np.outer(th, 2 * l)), dtype=DT, device=dev)
        kk = 2 * (l + 1)
        self.S = torch.tensor(np.sin(np.outer(th, kk)), dtype=DT, device=dev)                  # [m,l] k=2(l+1)
        self.dS = torch.tensor(kk[None, :] * np.cos(np.outer(th, kk)), dtype=DT, device=dev)
        self.kk = torch.tensor(kk, dtype=DT, device=dev)
        # geometry tensors
        self.rt = torch.tensor(self.r, dtype=DT, device=dev)
        self.xit = torch.tensor(xi, dtype=DT, device=dev)
        self.dxidr_t = torch.tensor(self.dxidr, dtype=DT, device=dev)
        self.cth = torch.tensor(np.cos(th), dtype=DT, device=dev)
        self.sth = torch.tensor(np.sin(th), dtype=DT, device=dev)
        # Green matrices for Omega modes k = 2(l+1), l=0..M-1, acting on q_k coefficients of degree < N+2
        Nq = N + 2
        self.Nq = Nq
        Hin = np.zeros((M, len(xi), Nq)); Hout = np.zeros((M, len(xi), Nq))
        for li in range(M):
            k = int(kk[li])
            Q = Quadrature(k, self.sigma_Om, xi, Nq)
            Hin[li] = Q.Hin; Hout[li] = Q.Hout
        self.Hin = torch.tensor(Hin, dtype=DT, device=dev)
        self.Hout = torch.tensor(Hout, dtype=DT, device=dev)
        self.Gh = (self.Hin + self.Hout) * (L ** 4 / (2 * self.kk))[:, None, None]     # h_k at eval radii
        self.Gd = (self.Hout - self.Hin) * (L ** 4 / 2) / self.rt[None, :, None]        # h_k'
        # strain at origin: H(0) = c = lim 2 h_2/r^2 = (1/2) int_0^inf b_2(s)/s ds
        # = (1/2) L^4 2^{-1} int_{-1}^{1} (1-t)^{sigma-1} q_2(t) dt   (from the outer integral with xi=-1, k=2):
        # = (L^2/4) int_{-1}^{1} (1-t)^{sigma_Om-1} q_2(t) dt
        alpha = self.sigma_Om - 1.0
        tq, wq = roots_jacobi(Nq // 2 + 4, alpha, 0.0)
        raw = wq @ cheb_T(tq, Nq)   # int_{-1}^1 (1-t)^{alpha} T_n dt
        self.c0_row = torch.tensor(0.25 * L ** 2 * raw, dtype=DT, device=dev)  # c = c0_row . qhat_2
        # Lagrange/Chebyshev transform matrices for q_k: p_{l} coefficients -> q_k coefficients (built in forward)
        self.origin_T = torch.tensor(cheb_T(np.array([-1.0]), N)[0], dtype=DT, device=dev)  # T_n(-1)

    # ---------- field evaluation ----------
    def fields(self, ca, cG, beta):
        """ca, cG: [M, N] Chebyshev coefficient tensors. Returns dict of grid fields [E, Mth] and scalars."""
        T, dT = self.T, self.dT
        # radial functions of each angular mode at eval radii: Q[l,e] = sum_n c[l,n] T_n(xi_e)
        Qa = ca @ T.T; dQa = ca @ dT.T
        QG = cG @ T.T; dQG = cG @ dT.T
        al = self.Pa * Qa; al_xi = self.dPa * Qa + self.Pa * dQa      # [l,e]
        gl = self.PG * QG; gl_xi = self.dPG * QG + self.PG * dQG
        # fields on grid [e,m]
        a = al.T @ self.C.T; a_xi = al_xi.T @ self.C.T; a_th = al.T @ self.dC.T
        G = gl.T @ self.C.T; G_xi = gl_xi.T @ self.C.T; G_th = gl.T @ self.dC.T
        a_r = a_xi * self.dxidr_t[:, None]; G_r = G_xi * self.dxidr_t[:, None]
        r = self.rt[:, None]; c = self.cth[None, :]; s = self.sth[None, :]
        a_x = c * a_r - s * a_th / r; a_y = s * a_r + c * a_th / r
        G_x = c * G_r - s * G_th / r; G_y = s * G_r + c * G_th / r
        # Omega sine modes: b_k = L^2 (1-xi)^{sigma_Om} rho^k q_k,  q_2 = p_0 - rho^4 p_4 / 2,  q_k = (p_{k-2} - rho^4 p_{k+2})/2
        M, N = self.M, self.N
        # Omega = (r^2/4) sum_l gamma_l [sin((2l+2)th) - sin((2l-2)th)]  =>  with k = 2(l'+1):
        #   b_2 = (r^2/2)(gamma_0 - gamma_2/2),   b_k = (r^2/4)(gamma_l' - gamma_{l'+2})  (l' >= 1)
        #   => q_2 = p_0 - rho^4 p_2 / 2,  q_k = (p_l' - rho^4 p_{l'+2}) / 2,  rho^4 = ((1+xi)/2)^2 (degree +2)
        rho4p = cheb_mult_1pxi_half(cheb_mult_1pxi_half(cG))   # [M, N+2]: coefficients of rho^4 p_l
        q = torch.zeros((M, N + 2), dtype=cG.dtype, device=cG.device)
        q[:, :N] += cG
        if M > 2:
            q[1:M - 2] -= rho4p[3:]
            q = q / 2.0
            q[0] = q[0] * 2.0 - rho4p[2] / 2.0
        else:
            q = q / 2.0
            q[0] = q[0] * 2.0
        # h_k and h_k' at eval radii: [l,e]
        h = torch.einsum('len,ln->le', self.Gh, q)
        hd = torch.einsum('len,ln->le', self.Gd, q)
        Psi = h.T @ self.S.T; Psi_r = hd.T @ self.S.T; Psi_th = h.T @ self.dS.T
        U1 = -(s * Psi_r + c * Psi_th / r)
        U2 = c * Psi_r - s * Psi_th / r
        x = r * c; y = r * s
        W1 = beta * x + U1; W2 = beta * y + U2
        w1 = beta + U1 / x; w2 = beta + U2 / y
        # desingularized residuals
        Ra = W1 * a_x + W2 * a_y + (2 * w1 + w2 - beta + 2) * a
        RG = W1 * G_x + W2 * G_y + (w1 + w2 + 1) * G - 2 * a - x * a_x
        # origin quantities
        cstrain = self.c0_row @ q[0]                   # H(0) = Psi_xy(0)
        a0 = (2.0 ** self.sigma_a) * (ca[0] @ self.origin_T)   # a(0)
        G0 = (2.0 ** self.sigma_G) * (cG[0] @ self.origin_T)
        return dict(a=a, G=G, a_x=a_x, a_y=a_y, G_x=G_x, G_y=G_y, Psi=Psi, U1=U1, U2=U2, W1=W1, W2=W2,
                    w1=w1, w2=w2, Ra=Ra, RG=RG, x=x, y=y, c=cstrain, a0=a0, G0=G0, q=q, h=h, hd=hd)

    def residual_vector(self, ca, cG, beta, a0_target=1.0, w_origin=1.0, fixed_beta=None):
        f = self.fields(ca, cG, beta)
        rows = [f['Ra'].reshape(-1), f['RG'].reshape(-1)]
        if self.origin_rows:
            # exact origin equations: R_a(0) = (2 beta - c + 2) a0 ; R_G(0) = (2 beta + 1) G0 - 2 a0
            rows.append(w_origin * ((2 * beta - f['c'] + 2) * f['a0']).reshape(1))
            rows.append(w_origin * ((2 * beta + 1) * f['G0'] - 2 * f['a0']).reshape(1))
        rows.append(w_origin * (f['a0'] - a0_target).reshape(1))
        return torch.cat(rows), f


def orthonormal_basis(model, which='a', tol=1e-9, row_weight=None):
    """Per angular mode l, return R_l (N x n_l) so that the (row-weighted) node values of the radial basis P_l (T R_l)
    are orthonormal columns; directions with relative singular value < tol (invisible on the weighted grid) are
    dropped. row_weight: [N_eval] weights applied to the rows (default: 1/P_0, the weights used in the least squares)."""
    P = model.Pa if which == 'a' else model.PG            # [M, N_eval] prefactor at nodes (eval = nodes here)
    T = model.T                                            # [N_eval, N]
    w = (1.0 / P[0]) if row_weight is None else row_weight
    Rs = []
    for l in range(model.M):
        B = (w * P[l])[:, None] * T                        # weighted node values of basis functions
        U, S, Vh = torch.linalg.svd(B, full_matrices=False)
        keep = S > tol * S[0]
        R = (Vh[keep].T) / S[keep][None, :]
        Rs.append(R)
    return Rs
