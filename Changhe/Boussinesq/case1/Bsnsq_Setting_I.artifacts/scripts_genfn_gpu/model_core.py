# GPU port: verbatim copy of scripts_genfn_cpu/model_core.py (device-safe through jets.DEV).
"""Core patches added to the generating-function basis of model.Model (m = 3):
  G = x eta E^(1/3) [ sum c_nk T_n(tau) T_k(2w - 1) + sum_p chi_p sum d^p_ij T_i(2 xi_p - 1) T_j(2 zeta_p - 1) ],
  xi_p = x^2/(Rc_p^2 + x^2), zeta_p = eta^2/(Rc_p^2 + eta^2), chi_p = exp(-(x^2 + eta^2)/Lc_p^2), i <= Jc_p, j <= Kc_p.
The patch functions are analytic, odd in x and in eta, and their variables cover only the physical quadrant (the (t, w)
square of Model also covers points with x^2 < 0 near the centre). chi_p removes them from the far field (superexponentially),
so the far-field expansion class of Model is unchanged. At the centre each patch adds sum d_ij (-1)^(i+j) to h.
patches: a list of (Jc, Kc, Rc, Lc), or a single tuple."""
import numpy as np, torch
from jets import Jet, monos, DT
from model import Model

def as_patches(core):
    a = np.asarray(core, dtype=float)
    a = a.reshape(1, 4) if a.ndim == 1 else a
    return [(int(q[0]), int(q[1]), float(q[2]), float(q[3])) for q in a]

class ModelCore(Model):
    def __init__(self, J, Kw, *core, m=3, alpha=0.0, se=1.0, gam=0.0):
        super().__init__(J, Kw, m=m, alpha=alpha, se=se, gam=gam)
        self.patches = as_patches(core[0] if len(core) == 1 else core)
        self.nbo = self.nb; self.nbc = sum((q[0] + 1) * (q[1] + 1) for q in self.patches); self.nb = self.nbo + self.nbc
        self.Jc, self.Kc, self.Rc, self.Lc = self.patches[0]
    def core_jets(self, x0, e0, p=4):
        X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
        Hs = H * (1.0 / self.se)
        E = 1 + X * X + Hs.ipow(2 * self.m)
        X2 = X * X; H2 = H * H
        pre0 = X * H * E.pow(1.0 / self.beta)
        def cheb(z, K):
            s = 2 * z - 1
            T = [Jet.const(1.0, p, z.c.shape[1], dev=z.c.device), s]
            for k in range(2, K + 1): T.append(2 * s * T[-1] - T[-2])
            return T[:K + 1]
        out = []
        for (Jc, Kc, Rc, Lc) in self.patches:
            pre = pre0 * ((X2 + H2) * (-1.0 / Lc ** 2)).exp()
            xi = X2 * (X2 + Rc ** 2).pow(-1.0); ze = H2 * (H2 + Rc ** 2).pow(-1.0)
            Tx = cheb(xi, Jc); Te = cheb(ze, Kc)
            for i in range(Jc + 1):
                pi = pre * Tx[i]
                for j in range(Kc + 1):
                    out.append(pi * Te[j])
        return out
    def basis_jets(self, x0, e0, p=4):
        return super().basis_jets(x0, e0, p) + self.core_jets(x0, e0, p)
    def h00_row(self):
        return np.concatenate([super().h00_row()] + [[(-1.0) ** (i + j) for i in range(q[0] + 1) for j in range(q[1] + 1)] for q in self.patches])
