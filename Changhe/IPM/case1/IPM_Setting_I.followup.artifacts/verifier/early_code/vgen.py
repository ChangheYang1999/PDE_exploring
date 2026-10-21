"""verifier: independent generator of the trial density of PUBLISHED_REPORT 4.2 (written for this run).

From the stored coefficients only:
  u = r/L, q = 1 - (1+u^2)^(-(1-k)/2), s = u^2/(1+u^2), chi = u^2/(u^2+r0^2),
  H = (k-3)/2 log(1+u^2) + sum_m chi^max(m-1,0) b_m(q) cos(2 m theta) + s^(p3/2) T(2q-1) |cos theta|^(p3-2) sin^2 theta,
  rho = r^3 cos^2 theta sin theta exp(H) = x^2 y exp(H),  p3 = 6 + 2k/(2-k),  k = z[0].
Radial dependence is carried as truncated Taylor jets in r (jets.py), so radial derivatives of any order up to K are
exact up to rounding; theta derivatives are taken analytically.
"""
import math
import numpy as np
import torch
from scipy.interpolate import BSpline
from numpy.polynomial import chebyshev as C
import jets as J

DT = torch.float64


class Trial:
    def __init__(self, path, device='cuda'):
        d = np.load(path, allow_pickle=True)
        self.path = path
        self.dev = device
        z = np.asarray(d['z'], float)
        self.k = float(z[0])
        self.L = float(d['L'])
        self.deg, self.M, self.sing = int(d['degree']), int(d['angular']), int(d['singular'])
        self.order = int(d['spline_order'])
        self.r0 = float(d['origin_radius'])
        assert str(d['radial_basis']) == 'spline'
        assert len(z) == 1 + (self.M + 1) * self.deg + self.sing, 'coefficient count'
        self.knots = np.asarray(d['spline_knots'], float)
        assert len(self.knots) == self.deg + 1 + self.order + 1
        cm = np.zeros((self.deg + 1, self.M + 1))
        for m in range(self.M + 1):
            cm[1:, m] = z[1 + m * self.deg: 1 + (m + 1) * self.deg]
        self.cmat = cm
        self.tcoef = z[1 + (self.M + 1) * self.deg:]
        self.p3 = 6 + 2 * self.k / (2 - self.k)
        self.c_l_file = float(d['c_l']) if 'c_l' in d.files else None
        self.c_l = 1.0 / self.k
        self.spl = [BSpline(self.knots, cm, self.order, extrapolate=False)]
        self.tch = [self.tcoef]

    def _spl(self, j):
        while len(self.spl) <= j:
            last = self.spl[-1]
            if getattr(last, 'k', 0) == 0:
                # derivatives beyond the spline degree vanish inside the knot intervals
                ncol = self.M + 1
                self.spl.append(lambda q, ncol=ncol: np.zeros((len(np.atleast_1d(q)), ncol)))
            else:
                self.spl.append(last.derivative())
        return self.spl[j]

    def _tch(self, j):
        while len(self.tch) <= j:
            self.tch.append(C.chebder(self.tch[-1]) if len(self.tch[-1]) > 1 else np.zeros(1))
        return self.tch[j]

    def interior_knots_r(self):
        qi = np.unique(self.knots)
        qi = qi[(qi > 0) & (qi < 1)]
        u = np.sqrt((1 - qi) ** (-2 / (1 - self.k)) - 1)
        return self.L * u

    def radial(self, r, K):
        """Radial jets at the points r (1D numpy or torch, r > 0): H0 (K+1,Nr), Rm (K+1,Nr,M+1), S (K+1,Nr)."""
        dev = self.dev
        r = torch.as_tensor(r, dtype=DT, device=dev)
        k, L = self.k, self.L
        rj = J.var(r, K)
        u2 = J.mul(rj, rj) / L ** 2
        one = J.const(torch.ones_like(r), K)
        lg = J.log(u2 + one)
        H0 = (k - 3) / 2 * lg
        e = J.exp(-(1 - k) / 2 * lg)
        q = -e
        q[0] = q[0] + 1.0
        q0 = q[0].cpu().numpy()
        fd = [torch.as_tensor(self._spl(j)(q0), dtype=DT, device=dev) for j in range(K + 1)]   # (Nr, M+1)
        b = J.compose(fd, q.unsqueeze(-1))                                                       # (K+1,Nr,M+1)
        lchi = J.log(u2) - J.log(u2 + self.r0 ** 2 * one)
        mm = torch.arange(self.M + 1, dtype=DT, device=dev)
        ex = torch.clamp(mm - 1, min=0)
        chip = J.exp(lchi.unsqueeze(-1) * ex)                                                    # (K+1,Nr,M+1)
        Rm = J.mul(chip, b)
        s = J.mul(u2, J.recip(u2 + one))
        sp = J.pw(s, self.p3 / 2)
        zz = 2 * q - one
        z0 = zz[0].cpu().numpy()
        td = [torch.as_tensor(C.chebval(z0, self._tch(j)) * 2.0 ** 0, dtype=DT, device=dev) for j in range(K + 1)]
        T = J.compose(td, zz)
        S = J.mul(sp, T)
        return dict(r=r, H0=H0, Rm=Rm, S=S)

    def angular(self, th):
        th = torch.as_tensor(th, dtype=DT, device=self.dev)
        mm = torch.arange(self.M + 1, dtype=DT, device=self.dev)
        ang = 2 * mm[:, None] * th[None, :]
        co, si = torch.cos(th), torch.sin(th)
        ac = torch.abs(co)
        p = self.p3
        A = ac ** (p - 2) * si ** 2
        dA = -(p - 2) * ac ** (p - 3) * torch.sign(co) * si ** 3 + 2 * si * co * ac ** (p - 2)
        return dict(th=th, cos=torch.cos(ang), msin=-2 * mm[:, None] * torch.sin(ang), A=A, dA=dA, co=co, si=si)

    def field(self, rad, an, K, theta=True):
        """Jets in r of rho and (optionally) rho_theta on the tensor grid (Nr x Nth): shape (K+1, Nr, Nth)."""
        H = rad['H0'].unsqueeze(-1) + torch.einsum('krm,mt->krt', rad['Rm'], an['cos']) \
            + rad['S'].unsqueeze(-1) * an['A'][None, None, :]
        r = rad['r']
        Kp = H.shape[0] - 1
        r3 = J.pw(J.var(r, Kp), 3.0)
        E = J.mul(r3.unsqueeze(-1), J.exp(H))
        co, si = an['co'], an['si']
        rho = E * (co ** 2 * si)[None, None, :]
        if not theta:
            return rho, None
        Ht = torch.einsum('krm,mt->krt', rad['Rm'], an['msin']) + rad['S'].unsqueeze(-1) * an['dA'][None, None, :]
        fac = co ** 2 * si * Ht
        fac[0] = fac[0] + (co ** 3 - 2 * co * si ** 2)[None, :]
        rhot = J.mul(E, fac)
        return rho, rhot

    def axis(self, x, K):
        """Jets in x along the x-axis (theta = 0, x > 0) of g = d_y rho(x,0) = x^2 e^{H(x,0)} and of the trial's own
        G_3 = d_y^3 rho(x,0)/6 = g * H_2, H_2 = (1/2) d_y^2 H(x,0) = (1/2)[H_r/r + H_thth/r^2] at theta = 0."""
        rad = self.radial(x, K + 1)
        mm = torch.arange(self.M + 1, dtype=DT, device=self.dev)
        H = rad['H0'] + rad['Rm'].sum(-1)            # theta = 0: cos = 1; A(0) = 0
        Hr = J.deriv(H)                                # order K
        # H_thth at theta=0: sum_m -(2m)^2 R_m + S * A''(0), A''(0) = 2
        Htt = -(rad['Rm'] * (2 * mm) ** 2).sum(-1) + 2 * rad['S']
        Kp = K
        x_ = J.var(rad['r'], Kp)
        H2 = 0.5 * (J.mul(Hr, J.recip(x_)) + J.mul(Htt[:Kp + 1], J.recip(J.mul(x_, x_))))
        g = J.mul(J.mul(x_, x_), J.exp(H[:Kp + 1]))
        G3 = J.mul(g, H2)
        return dict(g=g, G3=G3, H=H[:Kp + 1], H2=H2)
