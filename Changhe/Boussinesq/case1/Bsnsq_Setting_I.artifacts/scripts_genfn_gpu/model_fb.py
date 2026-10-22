"""Generating-function basis with a continuous exponent beta (the verifier's free-exponent family, research 44, without
its core term): m = beta/(beta - 2), integer M,
  E = x^2 + (1 + (eta/se)^(2M))^(m/M),  G = x eta E^(1/beta) sum c_nk T_n(2 tau - 1) T_k(2 w - 1),
  t = E^(-1/(2 beta)) (the far-field expansion variable r^(-1/beta)), tau = log radial map of t, w = (eta/se)^2 E^(-1/m).
For beta = 3, M = 3 this is exactly model.Model(m = 3) (same E, t, w, prefactor), so m = 3 states are reused unchanged.
Note: model.Model with m != 3 uses t = E^(-1/(2m)), which is not r^(-1/beta) for m != 3."""
import math, numpy as np, torch
from jets import Jet, monos, DT

class ModelFB:
    def __init__(self, J, Kw, beta=3.0, M=3, alpha=3.0, se=1.0, gam=0.0):
        self.J, self.Kw, self.M, self.alpha, self.se, self.gam = J, Kw, int(M), float(alpha), float(se), float(gam)
        self.set_beta(beta)
        self.nb = (J + 1) * (Kw + 1)
    def set_beta(self, beta):
        self.beta = float(beta); self.mr = self.beta / (self.beta - 2); self.a = self.beta + 2; self.b = self.beta - 2
    def basis_jets(self, x0, e0, p=4):
        X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
        Hs = H * (1.0 / self.se)
        Jf = (Hs.ipow(2 * self.M) + 1).pow(self.mr / self.M)
        E = X * X + Jf
        pre = X * H * E.pow(1.0 / self.beta)
        t = E.pow(-1.0 / (2 * self.beta))
        if self.alpha > 0:
            ea = math.exp(self.alpha) - 1.0
            t = 1 - ((1 - t) * ea + 1).log() * (1.0 / self.alpha)
        w = Hs * Hs * E.pow(-1.0 / self.mr)
        if self.gam > 0:
            w = (w * (math.exp(self.gam) - 1.0) + 1).log() * (1.0 / self.gam)
        def cheb(z, K):
            s = 2 * z - 1
            T = [Jet.const(1.0, p, z.c.shape[1], dev=z.c.device), s]
            for k in range(2, K + 1): T.append(2 * s * T[-1] - T[-2])
            return T[:K + 1]
        Tt = cheb(t, self.J); Tw = cheb(w, self.Kw)
        out = []
        for n in range(self.J + 1):
            pn = pre * Tt[n]
            for k in range(self.Kw + 1):
                out.append(pn * Tw[k])
        return out
    def g_jet(self, cmat, x0, e0, p=4):
        """Taylor coefficients (n_p, N) of G = sum c_nk B_nk at (x0, e0) without forming the basis matrix: (J+1) jet products"""
        X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
        Hs = H * (1.0 / self.se)
        E = X * X + (Hs.ipow(2 * self.M) + 1).pow(self.mr / self.M)
        pre = X * H * E.pow(1.0 / self.beta)
        t = E.pow(-1.0 / (2 * self.beta))
        if self.alpha > 0:
            ea = math.exp(self.alpha) - 1.0
            t = 1 - ((1 - t) * ea + 1).log() * (1.0 / self.alpha)
        w = Hs * Hs * E.pow(-1.0 / self.mr)
        if self.gam > 0:
            w = (w * (math.exp(self.gam) - 1.0) + 1).log() * (1.0 / self.gam)
        def cheb(z, K):
            s = 2 * z - 1
            T = [Jet.const(1.0, p, z.c.shape[1], dev=z.c.device), s]
            for k in range(2, K + 1): T.append(2 * s * T[-1] - T[-2])
            return T[:K + 1]
        Tt = cheb(t, self.J); Tw = torch.stack([T.c for T in cheb(w, self.Kw)], 0)     # (K+1, n_p, N)
        Q = torch.einsum('nk,kpi->npi', torch.as_tensor(cmat, dtype=DT).reshape(self.J + 1, self.Kw + 1), Tw)
        S = None
        for n in range(self.J + 1):
            term = Tt[n] * Jet(Q[n], p)
            S = term if S is None else S + term
        return (pre * S).c
    def basis_matrix(self, x0, e0, p=4):
        Bj = self.basis_jets(x0, e0, p)
        return torch.stack([B.c for B in Bj], -1)
    def h00_row(self):
        return np.array([(-1.0) ** k for n in range(self.J + 1) for k in range(self.Kw + 1)])

def ts_to_xeta_fb(T, S, beta, M, se=1.0):
    """physical points from a compact (T, S) square: E = T^(-2 beta), eta_max(E) from x = 0, w = S wmax(E),
    eta = se w^(1/2) E^(1/(2m)), x^2 = E - (1 + (eta/se)^(2M))^(m/M)"""
    m = beta / (beta - 2)
    E = T ** (-2.0 * beta)
    emax = np.maximum(E ** (M / m) - 1, 0) ** (1.0 / (2 * M))
    wmax = emax ** 2 * E ** (-1.0 / m)
    w = S * wmax
    eta = se * np.sqrt(w) * E ** (1.0 / (2 * m))
    x2 = E - (1 + (eta / se) ** (2 * M)) ** (m / M)
    return np.sqrt(np.maximum(x2, 0)), eta
