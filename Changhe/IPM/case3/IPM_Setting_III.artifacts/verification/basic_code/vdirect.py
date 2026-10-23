# Independent direct real-space velocity quadrature (verification).
#   U(X) = -rho(X)/2 e_2 + PV int K(X-Y) rho(Y) dY   (symmetric truncation, i.e. circles about 0),
#   K1(Z) = -(1/pi) z1 z2/|Z|^4,  K2(Z) = (1/(2 pi)) (z1^2 - z2^2)/|Z|^4.
# Split with a smooth bump chi_X(Y) = chi(|Y-X|/delta):
#   near part: PV over local polar coords about X (trapezoid in angle, Gauss in radius),
#   far part:  global polar grid about 0 (Gauss panels in log r, trapezoid in angle), kernel K(X-Y) - K(-Y) 1_{|Y|>Rs}
#              (the subtracted term integrates to zero over every circle about 0 by the parities of rho).
# Tail beyond r_max: estimated by a power-law fit of the angular-integrated far integrand (reported, not hidden).
import numpy as np
from numpy.polynomial.legendre import leggauss


def bump(s):
    """C-infinity cutoff: 1 for s<=1/2, 0 for s>=1, smooth transition."""
    s = np.asarray(s, dtype=float)
    out = np.zeros_like(s)
    out[s <= 0.5] = 1.0
    m = (s > 0.5) & (s < 1.0)
    u = (s[m] - 0.5) * 2.0  # in (0,1)
    f = lambda z: np.exp(-1.0 / z)
    out[m] = f(1 - u) / (f(1 - u) + f(u))
    return out


def Kern(z1, z2):
    q = z1 * z1 + z2 * z2
    q2 = q * q
    return -(1.0 / np.pi) * z1 * z2 / q2, (1.0 / (2 * np.pi)) * (z1 * z1 - z2 * z2) / q2


class DirectVelocity:
    def __init__(self, rho_fun, tmin=np.log(1e-8), tmax=np.log(1e12), H=0.05, q=16, Nth=1024,
                 nloc_r=48, nloc_th=256):
        self.rho_fun = rho_fun
        npan = int(np.ceil((tmax - tmin) / H))
        edges = np.linspace(tmin, tmax, npan + 1)
        Hh = (tmax - tmin) / npan
        xg, wg = leggauss(q)
        t = (0.5 * (edges[:-1, None] + edges[1:, None]) + 0.5 * Hh * xg[None, :]).reshape(-1)
        wt = (0.5 * Hh * wg[None, :] * np.ones((npan, 1))).reshape(-1)
        r = np.exp(t)
        # angles: symmetric under th->-th and th->pi-th
        th = (np.arange(Nth) + 0.5) * 2 * np.pi / Nth
        self.r, self.th = r, th
        self.wr = wt * r * r            # dY = r dr dth = r^2 dt dth
        self.wth = 2 * np.pi / Nth
        Rg, Tg = np.meshgrid(r, th, indexing='ij')
        self.Y1 = Rg * np.cos(Tg); self.Y2 = Rg * np.sin(Tg)
        self.rhoY = rho_fun(self.Y1, self.Y2)
        self.rmax = r[-1]
        xs, ws = leggauss(nloc_r)
        self.loc_s = 0.5 * (xs + 1); self.loc_ws = 0.5 * ws
        self.loc_phi = (np.arange(nloc_th) + 0.5) * 2 * np.pi / nloc_th
        self.loc_wphi = 2 * np.pi / nloc_th

    def U(self, X1, X2, delta_frac=0.4, Rs_fac=3.0, return_parts=False):
        """Velocity at a single point X (not the origin)."""
        rX = np.hypot(X1, X2)
        delta = delta_frac * rX
        # near part: int_0^delta ds/s int dphi k(phi) rho(X + s e_phi) chi(s/delta)
        s = self.loc_s * delta
        ws = self.loc_ws * delta
        S, PH = np.meshgrid(s, self.loc_phi, indexing='ij')
        Z1 = S * np.cos(PH); Z2 = S * np.sin(PH)
        rv = self.rho_fun(X1 + Z1, X2 + Z2)
        # K(X-Y) with Y = X+Z -> K(-Z) = K(Z) (even)
        k1 = -(1 / np.pi) * np.cos(PH) * np.sin(PH)
        k2 = (1 / (2 * np.pi)) * (np.cos(PH) ** 2 - np.sin(PH) ** 2)
        chi = bump(S / delta)
        # dY = s ds dphi, K = k/s^2 -> ds/s
        ang1 = (k1 * rv * chi).sum(axis=1) * self.loc_wphi
        ang2 = (k2 * rv * chi).sum(axis=1) * self.loc_wphi
        near1 = np.sum(ws * ang1 / s); near2 = np.sum(ws * ang2 / s)
        # far part
        D1 = X1 - self.Y1; D2 = X2 - self.Y2
        dist = np.hypot(D1, D2)
        K1, K2 = Kern(D1, D2)
        R = np.hypot(self.Y1, self.Y2)
        sub = R > Rs_fac * rX
        K01, K02 = Kern(-self.Y1, -self.Y2)
        K1 = K1 - np.where(sub, K01, 0.0); K2 = K2 - np.where(sub, K02, 0.0)
        w = (1.0 - bump(dist / delta)) * self.rhoY
        integ1 = (K1 * w).sum(axis=1) * self.wth  # per radius
        integ2 = (K2 * w).sum(axis=1) * self.wth
        far1 = np.sum(self.wr * integ1); far2 = np.sum(self.wr * integ2)
        # tail estimate: fit last few radii of r^2 * integ ~ A e^{-a t}
        tail = []
        for g in (integ1, integ2):
            gg = self.r ** 2 * g
            a, b = gg[-40], gg[-1]
            ta, tb = np.log(self.r[-40]), np.log(self.r[-1])
            if a != 0 and b != 0 and np.sign(a) == np.sign(b) and abs(b) < abs(a):
                lam = np.log(abs(a / b)) / (tb - ta)
                tail.append(b / lam)
            else:
                tail.append(0.0)
        rhoX = self.rho_fun(np.array([X1]), np.array([X2]))[0]
        U1 = near1 + far1 + tail[0]
        U2 = near2 + far2 + tail[1] - 0.5 * rhoX
        if return_parts:
            return U1, U2, dict(near=(near1, near2), far=(far1, far2), tail=tail)
        return U1, U2
