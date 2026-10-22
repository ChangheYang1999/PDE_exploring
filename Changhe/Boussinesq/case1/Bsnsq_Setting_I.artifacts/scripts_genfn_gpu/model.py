# GPU port of scripts_genfn_cpu/model.py: the only change is the device of the constant jet in cheb().
"""Generating-function formulation of the A1 profile problem (beta = 2m/(m-1); default m = 3, beta = 3).
Mixed coordinates (x, eta), Theta = a0 eta, y = G_x, xi = G_eta, A = G_x eta > 0 (formulas of the verifier's
research note 'generating_coordinates'):
  B0 = G_xx, C = G_etaeta, M = a G_eta - b eta C, W1 = M/A, W2 = B0 M/A + b eta A,
  Psi = beta x G_x + b eta G_eta - 2 beta G, Dx = d_x - (B0/A) d_eta, Dy = (1/A) d_eta, Omega = -(Dx^2 + Dy^2) Psi,
  R = (M/A) Omega_x + b eta Omega_eta + Omega + a0 B0/A   (= W.grad Omega + Omega - Theta_x, physical).
Temperature transport W.grad Theta = b Theta holds identically.
Basis: G = x eta E^(1/beta) sum_{n<=J, k<=Kw} c_nk T_n(2t - 1) T_k(2w - 1), E = 1 + x^2 + eta^(2m), t = E^(-1/(2m))... 
  with t = E^(-(m-1)/(2m))^(1/(m-1))?  For m = 3: t = E^(-1/6) (= R^(-1/3) = r^(-delta) asymptotically), w = eta^2 E^(-1/m)."""
import math, numpy as np, torch
from jets import Jet, monos, DT

class Model:
    def __init__(self, J, Kw, m=3, alpha=0.0, se=1.0, gam=0.0):
        self.J, self.Kw, self.m, self.alpha, self.se, self.gam = J, Kw, m, float(alpha), float(se), float(gam)
        self.beta = 2.0 * m / (m - 1); self.a = self.beta + 2; self.b = self.beta - 2
        self.nb = (J + 1) * (Kw + 1)
    def tcoef(self):
        return 1.0 / (2 * self.m)   # t = E^(-1/(2m)); for m = 3, r^(-1/3)
    def basis_jets(self, x0, e0, p=4):
        """list of nb jets of the basis functions (order p) at points (x0, e0)"""
        X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
        Hs = H * (1.0 / self.se)          # anisotropy parameter se: E = 1 + x^2 + (eta/se)^(2m), w = (eta/se)^2 E^(-1/m)
        E = 1 + X * X + Hs.ipow(2 * self.m)
        pre = X * H * E.pow(1.0 / self.beta)
        t = E.pow(-self.tcoef())
        if self.alpha > 0:
            # radial map: z = 1 - t = (exp(alpha zeta) - 1)/(exp(alpha) - 1); Chebyshev variable zeta (analytic in t at both ends)
            ea = math.exp(self.alpha) - 1.0
            t = 1 - ((1 - t) * ea + 1).log() * (1.0 / self.alpha)     # t now holds 1 - zeta (so that t -> 0 at infinity)
        w = Hs * Hs * E.pow(-1.0 / self.m)
        if self.gam > 0:
            # angular map: Chebyshev variable log(1 + w (e^gam - 1))/gam (analytic in w on [0, 1]; resolves small w)
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
    def basis_matrix(self, x0, e0, p=4):
        """tensor (n_p, N, nb): Taylor coefficients of each basis function"""
        Bj = self.basis_jets(x0, e0, p)
        return torch.stack([B.c for B in Bj], -1)
    def h00_row(self):
        """H(0,0) = sum c_nk T_n(1) T_k(-1)  (must equal 1 for c = -2)"""
        return np.array([(-1.0) ** k for n in range(self.J + 1) for k in range(self.Kw + 1)])

def fields(Gc, x0, e0, a0, beta, b=None, p=4):
    """From the order-4 Taylor coefficients Gc (n_4, N) of G at (x0, e0): residual R, normalizer pieces and fields."""
    a = beta + 2; b = beta - 2
    G = Jet(Gc, p)
    X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
    Gx = G.dx(); Ge = G.de()
    A = Gx.de(); B0 = Gx.dx(); C = Ge.de()
    M = a * Ge - b * (H * C)
    Psi = beta * (X * Gx) + b * (H * Ge) - 2 * beta * G
    iA = A.pow(-1.0); BA = B0 * iA
    Dx = lambda f: f.dx() - BA * f.de()
    Dy = lambda f: iA * f.de()
    Om = -(Dx(Dx(Psi)) + Dy(Dy(Psi)))
    Omx = Om.dx().val(); Ome = Om.de().val()
    Av = A.val(); Bv = B0.val(); Mv = M.val()
    W1 = Mv / Av; W2 = Bv * Mv / Av + b * e0 * Av
    Omv = Om.val()
    R = W1 * Omx + b * e0 * Ome + Omv + a0 * Bv / Av
    Ox = Omx - Bv / Av * Ome; Oy = Ome / Av
    Thx = -a0 * Bv / Av
    N = (W1 * Ox).abs() + (W2 * Oy).abs() + Omv.abs() + Thx.abs()
    y = Gx.val()
    return dict(R=R, N=N, A=Av, Om=Omv, Ox=Ox, Oy=Oy, W1=W1, W2=W2, Thx=Thx, y=y, Psi=Psi.val(),
                U1=W1 - beta * x0, U2=W2 - beta * y, Thy=a0 / Av)

def ts_to_xeta(T, S, m=3, se=1.0):
    """physical-domain points of the compact (t, s) square: E = t^(-2m), w = s * wmax(t), wmax = (1 - t^(2m))^(1/m),
    x^2 = E (1 - t^(2m) - w^m), eta = se w^(1/2) E^(1/(2m)) (numpy arrays)"""
    E = T ** (-2.0 * m); wmax = np.maximum(1 - T ** (2 * m), 0) ** (1.0 / m); w = wmax * S
    u = np.maximum(1 - T ** (2 * m) - w ** m, 0)
    return np.sqrt(E * u), se * np.sqrt(w) * E ** (1.0 / (2 * m))
