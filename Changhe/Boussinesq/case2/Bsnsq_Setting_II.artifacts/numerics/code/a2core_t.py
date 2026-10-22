"""
A2 model with the beta-adapted radial map (single domain, far-field adapted).

  t = (1 + r^2/L^2)^(-1/(2 beta)) in (0,1],  eta = 2t - 1 in (-1,1]   (r=0 -> eta=1, r=inf -> eta=-1)
  t is analytic in r^2 at the origin, and t = (L/r)^{1/beta} (1 + O(r^-2)) at infinity, so polynomials in eta are smooth
  even functions of r at 0 and expand the far field in integer powers of eps = r^{-1/beta} (the natural far-field
  expansion variable for beta X . grad Theta = (beta-2) Theta + U . grad Theta with U ~ r^{1-1/beta}).

Even-even fields, angular mode j = 2l:
  a_l(r) = (1 - t^{2 beta})^l  t^{e_a}  q_l(eta),   G_l(r) = (1 - t^{2 beta})^l  t^{e_G}  p_l(eta),
  with rho^2 = r^2/(r^2+L^2) = 1 - t^{2 beta}, and far-field exponents e_a = 2 beta sigma_a (default sigma_a = 1 + 1/beta,
  i.e. a ~ r^{-2-2/beta}, Theta ~ r^{1-2/beta}) and e_G = 2 beta sigma_G (default sigma_G = 1 + 1/(2 beta), i.e.
  Omega ~ r^{-1/beta}).
Omega sine modes k = 2(l'+1):  b_k = L^2 (1-t^{2b})^{k/2} t^{mu} [p_l' - (1-t^{2b})^2 p_{l'+2}]/4  (k>=4),
  b_2 = L^2 (1-t^{2b}) t^{mu} [p_0 - (1-t^{2b})^2 p_2 / 2]/2,   mu = e_G - 2 beta  (= 1 by default)
  (from Omega = (r^2/4) sum_l gamma_l [sin((2l+2)th) - sin((2l-2)th)] and r^2 = L^2 (1-t^{2b}) t^{-2b}).
Green formula per mode (canonical inverse, see a2core.py):
  r^k I_out  = L^4 beta t_e^{-2b} (1-t_e^{2b})^{k/2} int_0^{t_e} (t/t_e)^{b(k-2)} t^{mu-1} Q(t) dt
  r^-k I_in  = L^4 beta t_e^{-2b} int_{t_e}^1 (t_e/t)^{b(k+2)} ((1-t^{2b})/(1-t_e^{2b}))^{k/2} (1-t^{2b})^{k/2} t^{mu-1} Q(t) dt
  with Q = q-part (p_l' or (1-t^{2b})^2 p_{l'+2}), h_k = (r^k I_out + r^-k I_in)/(2k), h_k' = (r^k I_out - r^-k I_in)/(2 r).
"""
import math
import numpy as np
import torch
from scipy.special import roots_jacobi, roots_legendre
from a2core import cheb_T, cheb_T_deriv, cheb_gauss_nodes, DT


class QuadratureT:
    def __init__(self, k, beta, mu, t_e, Nq, n_gj=None, n_gl=24):
        self.k, self.beta, self.mu = k, float(beta), float(mu)
        t_e = np.asarray(t_e, dtype=np.float64)
        E = len(t_e)
        b = self.beta
        alpha = b * (k - 2) + mu - 1.0
        assert alpha > -1.0
        n_gj = n_gj or (Nq // 2 + 6)
        tau, wq = roots_jacobi(n_gj, 0.0, alpha)   # weight (1+tau)^alpha on [-1,1]
        gl_t, gl_w = roots_legendre(n_gl)
        Hout1 = np.zeros((E, Nq)); Hout2 = np.zeros((E, Nq)); Hin1 = np.zeros((E, Nq)); Hin2 = np.zeros((E, Nq))
        for e, te in enumerate(t_e):
            if te <= 0.0 or te >= 1.0:
                continue
            # outer: int_0^{te} (t/te)^alpha_b ... with t = te (1+tau)/2:  (t/te)^{b(k-2)} t^{mu-1} = ((1+tau)/2)^{b(k-2)} te^{mu-1} ((1+tau)/2)^{mu-1}
            t = te * (1 + tau) / 2
            pref = b * te ** (-2 * b) * (1 - te ** (2 * b)) ** (k / 2.0) * te ** (mu - 1.0) * (te / 2) * 2.0 ** (-alpha)
            # int_0^{te} f dt = (te/2) int_{-1}^{1} f(t(tau)) dtau ; (t/te)^{b(k-2)} t^{mu-1} = te^{mu-1} ((1+tau)/2)^{alpha}
            Tn = cheb_T(2 * t - 1, Nq)
            w2 = (1 - t ** (2 * b)) ** 2
            Hout1[e] = pref * (wq @ Tn)
            Hout2[e] = pref * ((wq * w2) @ Tn)
            # inner: u = log(t/te) in [0, U], integrand e^{-b(k+2)u} ((1-t^2b)/(1-te^2b))^{k/2} (1-t^2b)^{k/2} t^{mu-1} Q dt, dt = t du
            U = math.log(1.0 / te)
            umax = min(U, 40.0 / (b * (k + 2)))
            delta = min(0.5, 2.0 / (b * (k + 2)))
            npan = max(1, int(math.ceil(umax / delta)))
            edges = np.linspace(0.0, umax, npan + 1)
            acc1 = np.zeros(Nq); acc2 = np.zeros(Nq)
            for p in range(npan):
                u0, u1 = edges[p], edges[p + 1]
                u = u0 + (u1 - u0) * (gl_t + 1) / 2; w = gl_w * (u1 - u0) / 2
                t = te * np.exp(u)
                f = np.exp(-b * (k + 2) * u) * ((1 - t ** (2 * b)) / (1 - te ** (2 * b))) ** (k / 2.0) \
                    * (1 - t ** (2 * b)) ** (k / 2.0) * t ** (mu - 1.0) * t
                Tn = cheb_T(2 * t - 1, Nq)
                acc1 += (w * f) @ Tn
                acc2 += (w * f * (1 - t ** (2 * b)) ** 2) @ Tn
            pin = b * te ** (-2 * b)
            Hin1[e] = pin * acc1; Hin2[e] = pin * acc2
        self.Hout1, self.Hout2, self.Hin1, self.Hin2 = Hout1, Hout2, Hin1, Hin2


class A2ModelT:
    def __init__(self, N, M, L, beta, sigma_a=None, sigma_G=None, device=None, eta_eval=None, th_eval=None):
        self.N, self.M, self.L, self.beta = N, M, float(L), float(beta)
        b = self.beta
        self.sigma_a = (1.0 + 1.0 / b) if sigma_a is None else float(sigma_a)
        self.sigma_G = (1.0 + 1.0 / (2 * b)) if sigma_G is None else float(sigma_G)
        self.e_a, self.e_G = 2 * b * self.sigma_a, 2 * b * self.sigma_G
        self.mu = self.e_G - 2 * b
        assert self.mu > 0, "Omega must decay (sigma_G > 1)"
        self.dev = device or (torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
        self.eta = cheb_gauss_nodes(N) if eta_eval is None else np.asarray(eta_eval, dtype=np.float64)
        self.th = ((np.arange(M) + 0.5) * np.pi / (2 * M)) if th_eval is None else np.asarray(th_eval, dtype=np.float64)
        self._build()

    def r_of_eta(self, eta):
        t = (1 + eta) / 2
        return self.L * np.sqrt(t ** (-2 * self.beta) - 1.0)

    def eta_of_r(self, r):
        return 2 * (1 + (np.asarray(r) / self.L) ** 2) ** (-1 / (2 * self.beta)) - 1

    def _build(self):
        N, M, L, b = self.N, self.M, self.L, self.beta
        eta, th = self.eta, self.th
        dev = self.dev
        t = (1 + eta) / 2
        self.t = t
        self.r = L * np.sqrt(t ** (-2 * b) - 1.0)
        # d eta / dr = 2 dt/dr,  dt/dr = - r t^{2b+1} / (b L^2)
        self.detadr = -2 * self.r * t ** (2 * b + 1) / (b * L ** 2)
        T = cheb_T(eta, N); dT, _ = cheb_T_deriv(eta, N)
        self.T = torch.tensor(T, dtype=DT, device=dev); self.dT = torch.tensor(dT, dtype=DT, device=dev)
        l = np.arange(M)
        rho2 = 1 - t ** (2 * b)                       # = r^2/(r^2+L^2)
        Pa = rho2[None, :] ** l[:, None] * t[None, :] ** self.e_a
        PG = rho2[None, :] ** l[:, None] * t[None, :] ** self.e_G
        # d/d eta log P = (1/2) d/dt log P = (1/2) [ -2b l t^{2b-1}/(1-t^{2b}) + e/t ]
        dlogPa = 0.5 * (-2 * b * l[:, None] * t[None, :] ** (2 * b - 1) / rho2[None, :] + self.e_a / t[None, :])
        dlogPG = 0.5 * (-2 * b * l[:, None] * t[None, :] ** (2 * b - 1) / rho2[None, :] + self.e_G / t[None, :])
        self.Pa = torch.tensor(Pa, dtype=DT, device=dev); self.PG = torch.tensor(PG, dtype=DT, device=dev)
        self.dPa = self.Pa * torch.tensor(dlogPa, dtype=DT, device=dev)
        self.dPG = self.PG * torch.tensor(dlogPG, dtype=DT, device=dev)
        self.C = torch.tensor(np.cos(np.outer(th, 2 * l)), dtype=DT, device=dev)
        self.dC = torch.tensor(-2 * l[None, :] * np.sin(np.outer(th, 2 * l)), dtype=DT, device=dev)
        kk = 2 * (l + 1)
        self.S = torch.tensor(np.sin(np.outer(th, kk)), dtype=DT, device=dev)
        self.dS = torch.tensor(kk[None, :] * np.cos(np.outer(th, kk)), dtype=DT, device=dev)
        self.kk = torch.tensor(kk, dtype=DT, device=dev)
        self.rt = torch.tensor(self.r, dtype=DT, device=dev)
        self.detadr_t = torch.tensor(self.detadr, dtype=DT, device=dev)
        self.cth = torch.tensor(np.cos(th), dtype=DT, device=dev); self.sth = torch.tensor(np.sin(th), dtype=DT, device=dev)
        self.xit = torch.tensor(eta, dtype=DT, device=dev)     # name kept for lm_solve row weights
        self.tt = torch.tensor(t, dtype=DT, device=dev)
        # Green matrices acting on Chebyshev coefficients (degree < N) of p_l' (G1) and p_{l'+2} (G2)
        Nq = N
        E = len(eta)
        H = {nm: np.zeros((M, E, Nq)) for nm in ('o1', 'o2', 'i1', 'i2')}
        for li in range(M):
            Q = QuadratureT(int(kk[li]), b, self.mu, t, Nq)
            H['o1'][li], H['o2'][li], H['i1'][li], H['i2'][li] = Q.Hout1, Q.Hout2, Q.Hin1, Q.Hin2
        Ht = {nm: torch.tensor(v, dtype=DT, device=dev) for nm, v in H.items()}
        L4 = L ** 4
        inv2k = (1.0 / (2 * self.kk))[:, None, None]
        self.Gh1 = L4 * (Ht['o1'] + Ht['i1']) * inv2k; self.Gh2 = L4 * (Ht['o2'] + Ht['i2']) * inv2k
        inv2r = (0.5 / self.rt)[None, :, None]
        self.Gd1 = L4 * (Ht['o1'] - Ht['i1']) * inv2r; self.Gd2 = L4 * (Ht['o2'] - Ht['i2']) * inv2r
        # strain at origin: c = (1/2) int_0^inf b_2/s ds = (1/2) L^2 b int_0^1 t^{mu-1} Q_2 dt, Q_2 = p_0 - (1-t^{2b})^2 p_2/2
        tau, wq = roots_jacobi(Nq // 2 + 6, 0.0, self.mu - 1.0)
        tq = (1 + tau) / 2
        Tn = cheb_T(2 * tq - 1, Nq)
        base = 0.5 * L ** 2 * b * 0.5 * 2.0 ** (-(self.mu - 1.0))   # (1/2) * L^2 b * [dt = dtau/2 ; t^{mu-1} = ((1+tau)/2)^{mu-1}]
        self.c_row1 = torch.tensor(base * (wq @ Tn), dtype=DT, device=dev)
        self.c_row2 = torch.tensor(base * ((wq * (1 - tq ** (2 * b)) ** 2) @ Tn), dtype=DT, device=dev)
        self.origin_T = torch.tensor(cheb_T(np.array([1.0]), N)[0], dtype=DT, device=dev)   # T_n(eta=1)

    def fields(self, ca, cG, beta):
        """ca, cG: [M, N] Chebyshev coefficients (in eta). beta: the transport parameter (may differ slightly from the
        map's beta during free-beta iterations)."""
        T, dT = self.T, self.dT
        Qa = ca @ T.T; dQa = ca @ dT.T; QG = cG @ T.T; dQG = cG @ dT.T
        al = self.Pa * Qa; al_eta = self.dPa * Qa + self.Pa * dQa
        gl = self.PG * QG; gl_eta = self.dPG * QG + self.PG * dQG
        a = al.T @ self.C.T; a_eta = al_eta.T @ self.C.T; a_th = al.T @ self.dC.T
        G = gl.T @ self.C.T; G_eta = gl_eta.T @ self.C.T; G_th = gl.T @ self.dC.T
        a_r = a_eta * self.detadr_t[:, None]; G_r = G_eta * self.detadr_t[:, None]
        r = self.rt[:, None]; c = self.cth[None, :]; s = self.sth[None, :]
        a_x = c * a_r - s * a_th / r; a_y = s * a_r + c * a_th / r
        G_x = c * G_r - s * G_th / r; G_y = s * G_r + c * G_th / r
        M = self.M
        # h_k = Gh1 . p_l' - Gh2 . p_{l'+2}  (/2 for k>=4; k=2: p_0 - p_2-term/2)
        h1 = torch.einsum('len,ln->le', self.Gh1, cG); hd1 = torch.einsum('len,ln->le', self.Gd1, cG)
        h = torch.zeros_like(h1); hd = torch.zeros_like(hd1)
        if M > 2:
            h2 = torch.einsum('len,ln->le', self.Gh2[:M - 2], cG[2:]); hd2 = torch.einsum('len,ln->le', self.Gd2[:M - 2], cG[2:])
            h[1:M - 2] = (h1[1:M - 2] - h2[1:]) / 4; hd[1:M - 2] = (hd1[1:M - 2] - hd2[1:]) / 4
            h[0] = (h1[0] - h2[0] / 2) / 2; hd[0] = (hd1[0] - hd2[0] / 2) / 2
            h[M - 2:] = h1[M - 2:] / 4; hd[M - 2:] = hd1[M - 2:] / 4
            cstrain = (self.c_row1 @ cG[0] - (self.c_row2 @ cG[2]) / 2) / 2
        else:
            h[0] = h1[0] / 2; hd[0] = hd1[0] / 2
            if M == 2:
                h[1] = h1[1] / 4; hd[1] = hd1[1] / 4
            cstrain = (self.c_row1 @ cG[0]) / 2
        Psi = h.T @ self.S.T; Psi_r = hd.T @ self.S.T; Psi_th = h.T @ self.dS.T
        U1 = -(s * Psi_r + c * Psi_th / r); U2 = c * Psi_r - s * Psi_th / r
        x = r * c; y = r * s
        W1 = beta * x + U1; W2 = beta * y + U2
        w1 = beta + U1 / x; w2 = beta + U2 / y
        Ra = W1 * a_x + W2 * a_y + (2 * w1 + w2 - beta + 2) * a
        RG = W1 * G_x + W2 * G_y + (w1 + w2 + 1) * G - 2 * a - x * a_x
        a0 = ca[0] @ self.origin_T; G0 = cG[0] @ self.origin_T     # t=1 at the origin: prefactors = 1
        return dict(a=a, G=G, a_x=a_x, a_y=a_y, G_x=G_x, G_y=G_y, Psi=Psi, U1=U1, U2=U2, W1=W1, W2=W2, w1=w1, w2=w2,
                    Ra=Ra, RG=RG, x=x, y=y, c=cstrain, a0=a0, G0=G0, h=h, hd=hd)
