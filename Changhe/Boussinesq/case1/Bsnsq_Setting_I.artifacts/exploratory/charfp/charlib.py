"""Characteristic (slaved-transport) reconstruction of Theta, grad Theta and Omega from a velocity given by
Omega coefficients in the polarlib basis. Prototype for the Psi-only fixed point.
For X: integrate backward dY/ds = -W(Y) together with dP/ds = P A(Y), P(0) = I (3x3), where
A = [[b - dxW1, -dxW2, 0], [-dyW1, b - dyW2, 0], [1, 0, -1]], until |Y| < r_stop; then
(Theta_x, Theta_y, Omega)(X) = P(S) z(Y_S), z = local jet values, and Theta(X) = e^(b S) Theta_jet(Y_S)."""
import math, numpy as np, torch
from polarlib import *
from evalfields import load_coefs, radial_profiles

class VelTable:
    """Tabulated psi_n, psi_n', g_n, g_n' on a uniform grid in s = ln r; cubic Hermite interpolation."""
    def __init__(self, P, cO, NO, K, rmin=1e-4, rmax=1e10, per_dec=100):
        self.P = P; self.NO = NO; self.beta = P.beta
        nd = math.log10(rmax / rmin)
        self.s = torch.linspace(math.log(rmin), math.log(rmax), int(round(nd * per_dec)) + 1, dtype=DT)
        self.hs = float(self.s[1] - self.s[0]); self.s0 = float(self.s[0])
        r = torch.exp(self.s)
        cT0 = torch.zeros(1, K, dtype=DT)
        prof = radial_profiles(P, cT0, cO, r, 1, NO, K)
        psi, dpsi, g, dg = prof['psi'], prof['dpsi'], prof['g'], prof['dg']
        m = torch.tensor([2.0 * n for n in range(1, NO + 1)], dtype=DT)[:, None]
        d2psi = -g - dpsi / r + m * m * psi / r ** 2
        # values and s-derivatives (d/ds = r d/dr)
        self.V = torch.stack([psi, dpsi, d2psi])            # (3, NO, Ns)
        # s-derivatives: psi -> r psi', psi' -> r psi''; psi'' -> r psi''' from differentiating the ODE
        d3psi = -dg - d2psi / r + dpsi / r ** 2 + m * m * (dpsi / r ** 2 - 2 * psi / r ** 3)
        self.D = torch.stack([r * dpsi, r * d2psi, r * d3psi])
        self.c = prof['c']; self.m = m[:, 0]

    def interp(self, rr):
        s = torch.log(rr)
        x = (s - self.s0) / self.hs
        i = torch.clamp(torch.floor(x).long(), 0, self.s.shape[0] - 2)
        t = x - i
        h00 = 2 * t ** 3 - 3 * t ** 2 + 1; h10 = t ** 3 - 2 * t ** 2 + t; h01 = -2 * t ** 3 + 3 * t ** 2; h11 = t ** 3 - t ** 2
        V0 = self.V[:, :, i]; V1 = self.V[:, :, i + 1]; D0 = self.D[:, :, i]; D1 = self.D[:, :, i + 1]
        out = h00 * V0 + h01 * V1 + self.hs * (h10 * D0 + h11 * D1)   # (3, NO, N)
        return out[0], out[1], out[2]

    def W_DW(self, Y, scale=1.0):
        """W (N,2) and DW (N,2,2) at points Y (N,2) in the closed first quadrant. U is multiplied by `scale`."""
        x, y = Y[:, 0], Y[:, 1]
        r = torch.sqrt(x * x + y * y); ph = torch.atan2(y, x)
        ps, dps, d2ps = self.interp(r)
        m = self.m[:, None]
        sm = torch.sin(m * ph[None, :]); cm = torch.cos(m * ph[None, :])
        Pr = (dps * sm).sum(0); Pf = (m * ps * cm).sum(0); Prr = (d2ps * sm).sum(0)
        Prf = (m * dps * cm).sum(0); Pff = -(m * m * ps * sm).sum(0)
        c = torch.cos(ph); s_ = torch.sin(ph)
        Px = c * Pr - s_ * Pf / r; Py = s_ * Pr + c * Pf / r
        A1 = Pr / r + Pff / r ** 2; A2 = Prf / r - Pf / r ** 2
        Pxx = c * c * Prr + s_ * s_ * A1 - 2 * s_ * c * A2
        Pyy = s_ * s_ * Prr + c * c * A1 + 2 * s_ * c * A2
        Pxy = s_ * c * (Prr - A1) + (c * c - s_ * s_) * A2
        b = self.beta
        W = torch.stack([b * x - scale * Py, b * y + scale * Px], 1)
        DW = torch.empty(Y.shape[0], 2, 2, dtype=DT)
        DW[:, 0, 0] = b - scale * Pxy; DW[:, 0, 1] = -scale * Pyy
        DW[:, 1, 0] = scale * Pxx;     DW[:, 1, 1] = b + scale * Pxy
        return W, DW

def local_jets(tab, rfit=(1e-3, 2e-3)):
    """h10, h01 from psi_1 ~ -r^2 + A r^4 (c normalized), psi_2 ~ C4 r^4."""
    rr = torch.tensor(rfit, dtype=DT)
    ps, _, _ = tab.interp(rr)
    c = tab.c
    p1 = ps[0] - (c / 2) * rr ** 2   # psi_1 = (c/2) r^2 + A r^4 + ...
    A = float((p1 / rr ** 4)[0]); A2 = float((p1 / rr ** 4)[1])
    C4 = float((ps[1] / rr ** 4)[0])
    return A, C4, A2

def reconstruct(tab, X, a0, h=0.02, r_stop=1e-3, S_max=60.0, scale=1.0, jets=True):
    """Returns dict Th, Thx, Thy, Om at X (N,2), plus S (backward time) and flags."""
    b = tab.beta - 2.0; beta = tab.beta
    N = X.shape[0]
    Y = X.clone(); Pm = torch.eye(3, dtype=DT).repeat(N, 1, 1)
    S = torch.zeros(N, dtype=DT); done = torch.zeros(N, dtype=torch.bool)
    def rhs(Y, Pm):
        W, DW = tab.W_DW(Y, scale)
        A = torch.zeros(Y.shape[0], 3, 3, dtype=DT)
        A[:, 0, 0] = b - DW[:, 0, 0]; A[:, 0, 1] = -DW[:, 1, 0]
        A[:, 1, 0] = -DW[:, 0, 1];    A[:, 1, 1] = b - DW[:, 1, 1]
        A[:, 2, 0] = 1.0; A[:, 2, 2] = -1.0
        return -W, torch.bmm(Pm, A)
    s = 0.0
    while s < S_max:
        act = ~done
        if not act.any(): break
        Ya, Pa = Y[act], Pm[act]
        k1y, k1p = rhs(Ya, Pa)
        k2y, k2p = rhs(Ya + 0.5 * h * k1y, Pa + 0.5 * h * k1p)
        k3y, k3p = rhs(Ya + 0.5 * h * k2y, Pa + 0.5 * h * k2p)
        k4y, k4p = rhs(Ya + h * k3y, Pa + h * k3p)
        Y[act] = Ya + h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        Pm[act] = Pa + h / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        S[act] += h; s += h
        rr = torch.sqrt((Y ** 2).sum(1))
        done = done | (rr < r_stop)
    # local jet at Y_S: Psi = (c/2)*r^2 sin2phi... -> xy coefficient c; quartic h10 x^3 y + h01 x y^3
    if jets:
        A, C4, _ = local_jets(tab)
        h10 = 2 * A + 4 * C4; h01 = 2 * A - 4 * C4     # h10 + h01 = 4A, h10 - h01 = 8 C4
    else:
        h10 = h01 = 0.0
    a10 = -3 * a0 * h10 / (2 * beta + 4); a01 = -a0 * h01 / (2 * beta - 4)
    g00 = 2 * a10 / (2 * beta + 1)
    x, y = Y[:, 0], Y[:, 1]
    Th_S = a0 * y + a10 * x * x * y + a01 * y ** 3
    z = torch.stack([2 * a10 * x * y, a0 + a10 * x * x + 3 * a01 * y * y, g00 * x * y], 1)
    out = torch.bmm(Pm, z[:, :, None])[:, :, 0]
    Th = torch.exp(b * S) * Th_S
    return dict(Th=Th, Thx=out[:, 0], Thy=out[:, 1], Om=out[:, 2], S=S, done=done, Y=Y, h10=h10, h01=h01)
