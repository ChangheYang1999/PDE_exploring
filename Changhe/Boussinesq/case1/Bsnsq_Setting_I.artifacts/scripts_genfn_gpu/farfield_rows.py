"""Differentiable (torch) far-field coefficient C(v), N20(v) of the generating-function residual (external review, 3.21(b) of the numerical report; same
formulas as farfield_C.py) as a function of the OUTER coefficient vector c (length (J+1)(Kw+1)) and a0, for use as least-squares rows
C(v_i)/N20_lag(v_i) ('infinity rows'). m = 3 only. The core patch does not contribute (superexponentially small at infinity)."""
import math, torch
from jets import Jet, monos, DT
P = 4
def _cheb_sum(coefs, z):   # coefs: torch (K+1,) differentiable; z: Jet
    s = 2 * z - 1
    T = [Jet.const(1.0, P, z.c.shape[1], dev=z.c.device), s]
    for k in range(2, coefs.shape[0]): T.append(2 * s * T[-1] - T[-2])
    out = T[0] * coefs[0:1]
    for k in range(1, coefs.shape[0]): out = out + T[k] * coefs[k:k + 1]
    return out
class FarField:
    def __init__(self, J, Kw, alpha, se, nv, dev):
        self.J, self.Kw, self.se = J, Kw, se
        if alpha > 0:
            kap = 1 - math.exp(-alpha); self.dd = kap / alpha; self.ee = kap ** 2 / (2 * alpha)
        else:
            self.dd = 1.0; self.ee = 0.0
        n = torch.arange(J + 1, dtype=DT, device=dev)
        self.T0 = (-1.0) ** n; self.T1 = 2 * (-1.0) ** (n - 1) * n ** 2; self.T2 = 4 * (-1.0) ** n * n ** 2 * (n ** 2 - 1) / 3.0
        import numpy as np
        vs = torch.tensor(0.5 * (1 - np.cos(np.pi * (np.arange(nv) + 0.5) / nv)), dtype=DT, device=dev)
        self.vs = vs; self.x0 = torch.sqrt(1 - vs ** 3); self.e0 = se * torch.sqrt(vs)
    def CN(self, c_outer, a0):
        """returns C (nv,), N20 (nv,) as torch tensors (differentiable in c_outer and a0)"""
        cm = c_outer.reshape(self.J + 1, self.Kw + 1)
        Fv0 = self.T0 @ cm; Ftau = self.T1 @ cm; Ftautau = self.T2 @ cm
        h0c = Fv0; h1c = self.dd * Ftau; h2c = self.ee * Ftau + 0.5 * self.dd ** 2 * Ftautau
        X = Jet.var(self.x0, 0, P); H = Jet.var(self.e0, 1, P); Hs = H * (1.0 / self.se)
        rho = (X * X + Hs.ipow(6)).pow(0.5); v = Hs * Hs * rho.pow(-2.0 / 3.0); pre = X * H
        G0 = pre * rho.pow(2.0 / 3.0) * _cheb_sum(h0c, v); G1 = pre * rho.pow(1.0 / 3.0) * _cheb_sum(h1c, v); G2 = pre * _cheb_sum(h2c, v)
        Gx0 = G0.dx(); A = Gx0.de(); B = Gx0.dx(); iA = A.pow(-1.0); BA = B * iA
        Dx = lambda f: f.dx() - BA * f.de()
        Dy = lambda f: iA * f.de()
        P1 = -G1; P2 = -2.0 * G2 + (G1.de() * G1.dx()) * iA
        om0 = -(Dx(Dx(P1)) + Dy(Dy(P1))); om1 = -(Dx(Dx(P2)) + Dy(Dy(P2)))
        u1 = -Dy(P1); u2 = Dx(P1)
        t1 = -om1.val(); t2 = u1.val() * Dx(om0).val(); t3 = u2.val() * Dy(om0).val(); t4 = a0 * (B * iA).val()
        return t1 + t2 + t3 + t4, t1.abs() + t2.abs() + t3.abs() + t4.abs()
