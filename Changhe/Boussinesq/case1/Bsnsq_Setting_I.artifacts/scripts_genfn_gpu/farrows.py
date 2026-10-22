"""Exact far-field limit of the grouped vorticity ratio, as differentiable rows for the solver.
For the model.py basis with beta = 3 (m = 3), alpha > 0, gam = 0: G = x eta E^(1/3) P(t, w) (+ core patches, which do not
contribute). With F = x^2 + (e/se)^6, w0 = (e/se)^2 F^(-1/3), c1 = d/alpha, c2 = d^2/(2 alpha), d = 1 - exp(-alpha):
  G0 = x e F^(1/3) P(0, w0),  G1 = c1 x e F^(1/6) P_t(0, w0),  G2 = x e [c2 P_t(0, w0) + (c1^2/2) P_tt(0, w0)],
  A = G0_xe, b = G0_xx / A, D_x = d_x - b d_e, D_y = A^(-1) d_e (physical derivatives of the limiting chart),
  S0 = -G1, S1 = -2 G2 + G1_x G1_e / A, u01 = -D_y S0, u02 = D_x S0, omega_j = -(D_x^2 + D_y^2) S_j,
  Z1 = -omega1, Z2 = u01 D_x omega0, Z3 = u02 D_y omega0, Z4 = a b,  C = Z1 + .. + Z4,  N20 = |Z1| + .. + |Z4|
(the verifier's analytic far-residual identity). Along every ray R_Omega/N2 -> C/N20 at physical infinity. Points are taken
on the compact section F = 1: x = sqrt(1 - w^3), e = se sqrt(w), 0 < w < 1 (w -> 0 horizontal axis, w -> 1 vertical axis).
P_t, P_tt are derivatives in the Chebyshev variable t of model.py (t -> 0 at infinity): T_n(2t - 1) at t = 0 has value
(-1)^n, first derivative 2 (-1)^(n+1) n^2, second derivative 4 (-1)^n n^2 (n^2 - 1)/3."""
import math, numpy as np, torch
from jets import Jet, DT


class FarRows:
    def __init__(self, J, Kw, alpha, se, wnodes, p=4, beta=3.0):
        """beta != 3: the same limit for the free-exponent basis (model_fb, model_core_fb): F = x^2 + (e/se)^(2m),
        m = beta/(beta - 2), F^(1/3) -> F^(1/beta), F^(1/6) -> F^(1/(2 beta)), section x = sqrt(1 - w^m). The derivation is
        unchanged: G_k has degree 2 - k/beta under (x, e) -> (l x, l^(1/m) e), so Psi(G_k) = -k G_k for every beta, and the
        difference E - F is of relative order t^(2M(beta - 2)) (t^6 at beta 3), beyond the second order used here."""
        self.J, self.Kw, self.alpha, self.se, self.p = J, Kw, float(alpha), float(se), p
        self.beta = float(beta); mr = self.beta / (self.beta - 2)
        d = 1.0 - math.exp(-self.alpha)
        self.c1 = d / self.alpha; self.c2 = d * d / (2 * self.alpha)
        w = np.asarray(wnodes, dtype=float); self.w = w
        self.x0 = torch.tensor(np.sqrt(1.0 - w ** mr), dtype=DT); self.e0 = torch.tensor(self.se * np.sqrt(w), dtype=DT)
        n = np.arange(J + 1, dtype=float)
        self.r0 = torch.tensor((-1.0) ** n, dtype=DT)
        self.r1 = torch.tensor(2.0 * (-1.0) ** (n + 1) * n ** 2, dtype=DT)
        self.r2 = torch.tensor(4.0 * (-1.0) ** n * n ** 2 * (n ** 2 - 1) / 3.0, dtype=DT)
        X = Jet.var(self.x0, 0, p); H = Jet.var(self.e0, 1, p)
        Hs = H * (1.0 / self.se)
        F = X * X + (Hs.ipow(6) if self.beta == 3.0 else (Hs * Hs).pow(mr))
        w0 = Hs * Hs * F.pow(-1.0 / mr)
        s = 2 * w0 - 1
        T = [Jet.const(1.0, p, len(w)), s]
        for k in range(2, Kw + 1): T.append(2 * s * T[-1] - T[-2])
        self.Tw = torch.stack([T[k].c for k in range(Kw + 1)], 0)          # (K+1, n_p, N)
        self.pre0 = X * H * F.pow(1.0 / self.beta)
        self.pre1 = X * H * F.pow(0.5 / self.beta) * self.c1
        self.pre2 = X * H

    def terms(self, c, a):
        """c: torch vector whose first (J+1)(Kw+1) entries are the outer coefficients (row-major (n, k)); a: amplitude
        (stored a0, Theta = a eta). Returns the signed terms Z (4, N) as torch tensors (differentiable in c and a)."""
        p = self.p
        cm = c[:(self.J + 1) * (self.Kw + 1)].reshape(self.J + 1, self.Kw + 1)
        P0 = Jet(torch.einsum('k,kpi->pi', self.r0 @ cm, self.Tw), p)
        P1 = Jet(torch.einsum('k,kpi->pi', self.r1 @ cm, self.Tw), p)
        P2 = Jet(torch.einsum('k,kpi->pi', self.r2 @ cm, self.Tw), p)
        G0 = self.pre0 * P0; G1 = self.pre1 * P1; G2 = self.pre2 * (P1 * self.c2 + P2 * (0.5 * self.c1 ** 2))
        G0x = G0.dx()
        A = G0x.de(); B = G0x.dx(); iA = A.pow(-1.0); bb = B * iA
        Dx = lambda f: f.dx() - bb * f.de()
        Dy = lambda f: iA * f.de()
        S0 = -G1
        S1 = G2 * (-2.0) + G1.dx() * G1.de() * iA
        u01 = -(Dy(S0).val()); u02 = Dx(S0).val()
        om0 = -(Dx(Dx(S0)) + Dy(Dy(S0)))
        om1 = -(Dx(Dx(S1)) + Dy(Dy(S1))).val()
        Dxom0 = om0.dx().val() - bb.val() * om0.de().val()
        Dyom0 = iA.val() * om0.de().val()
        Z1 = -om1; Z2 = u01 * Dxom0; Z3 = u02 * Dyom0; Z4 = a * bb.val()
        return torch.stack([Z1, Z2, Z3, Z4], 0)

    def ratio(self, c, a):
        Z = self.terms(c, a)
        return Z.sum(0) / Z.abs().sum(0)


def cheb_w(K):
    return 0.5 * (1 - np.cos(np.pi * (np.arange(K) + 0.5) / K))


if __name__ == '__main__':
    import sys
    st = np.load(sys.argv[1])
    J, Kw = int(st['J']), int(st['Kw'])
    ws = [float(v) for v in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(cheb_w(25))
    fr = FarRows(J, Kw, float(st['alpha']), float(st['se']), ws, beta=float(st['beta']) if 'beta' in st.files else 3.0)
    q = fr.ratio(torch.tensor(st['c'][:(J + 1) * (Kw + 1)], dtype=DT), float(st['a0'])).numpy()
    print('state %s a0 %.6f  signed C/N20 on the section F = 1:' % (sys.argv[1], float(st['a0'])))
    for wv, qv in zip(ws, q): print('  w %.6f  %+.9e' % (wv, qv))
    print('  max |C|/N20 over these w: %.4e' % np.abs(q).max())
