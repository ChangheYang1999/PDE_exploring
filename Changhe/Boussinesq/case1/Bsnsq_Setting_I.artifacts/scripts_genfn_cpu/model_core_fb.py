"""Core patches added to the free-exponent basis of model_fb.ModelFB (beta fixed per instance, M = 3 by default):
  G = x eta E^(1/beta) [ sum c_nk T_n(2 tau - 1) T_k(2 w - 1) + sum_p chi_p sum d^p_ij T_i(2 xi_p - 1) T_j(2 zeta_p - 1) ],
  E = x^2 + (1 + (eta/se)^(2M))^(m/M), m = beta/(beta - 2), t = E^(-1/(2 beta)), w = (eta/se)^2 E^(-1/m),
  xi_p = x^2/(Rc_p^2 + x^2), zeta_p = eta^2/(Rc_p^2 + eta^2), chi_p = exp(-(x^2 + eta^2)/Lc_p^2).
For beta = 3, M = 3 this is exactly model_core.ModelCore (same E, prefactor and patch functions), so core states are reused."""
import numpy as np, torch
from jets import Jet, monos, DT
from model_fb import ModelFB
from model_core import as_patches

class ModelCoreFB(ModelFB):
    def __init__(self, J, Kw, *core, beta=3.0, M=3, alpha=3.0, se=1.0, gam=0.0):
        super().__init__(J, Kw, beta=beta, M=M, alpha=alpha, se=se, gam=gam)
        self.patches = as_patches(core[0] if len(core) == 1 else core)
        self.nbo = self.nb; self.nbc = sum((q[0] + 1) * (q[1] + 1) for q in self.patches); self.nb = self.nbo + self.nbc
    def core_jets(self, x0, e0, p=4):
        X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
        Hs = H * (1.0 / self.se)
        E = X * X + (Hs.ipow(2 * self.M) + 1).pow(self.mr / self.M)
        X2 = X * X; H2 = H * H
        pre0 = X * H * E.pow(1.0 / self.beta)
        def cheb(z, K):
            s = 2 * z - 1
            T = [Jet.const(1.0, p, z.c.shape[1]), s]
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
    def g_jet(self, cfull, x0, e0, p=4):
        """Taylor coefficients of G for the full coefficient vector (outer c, then the patch coefficients)"""
        cfull = np.asarray(cfull, dtype=float)
        out = super().g_jet(cfull[:self.nbo], x0, e0, p)
        Bc = torch.stack([B.c for B in self.core_jets(x0, e0, p)], -1)
        return out + Bc @ torch.tensor(cfull[self.nbo:], dtype=DT)
