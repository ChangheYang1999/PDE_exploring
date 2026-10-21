"""verifier: reader and generator for the numerics lane's Psi-map / collocation states (written for this run).

Only the representation is taken from the numerics lane (the docstring of their ipm_newton.py and the npz keys); the
evaluation below is this lane's own code.  Representation:
    rho = r^3 w(r) Pi(theta) b(q, theta) = x^2 y w(r) b(q, theta),  Pi = cos^2 theta sin theta,
    w = (1 + u^2)^((k-3)/2),  u = r/L,  k = 1/c_l,  q = 1 - (1 + u^2)^(-(1-k)/2),
    b(q, theta) = sum_{m=0}^{M-1} C_m(q) cos(2 m s(theta)),  theta(s) = s + (beta/2) sin(2 s),
with b given by its values at the Chebyshev-Lobatto nodes q_i = (1 - cos(pi i/N))/2 (i = 0..N, degree-N polynomial in q)
and at the mapped angles theta_j = theta(s_j), s_j = (j + 1/2) pi/(2M) (exact trigonometric interpolation in s).
Interface as vgen.Trial (radial, angular, field, axis, interior_knots_r), so that vres.Evaluation, vaxis.AxisData and
vgaxis.GreenAxis run unchanged.  Radial jets are exact Taylor jets (Chebyshev derivatives composed with the jets of q).
"""
import math
import numpy as np
import torch
from numpy.polynomial import chebyshev as Ch
import jets as J

DT = torch.float64


def s_of_theta(th, beta):
    """Inverse of theta = s + (beta/2) sin 2s (monotone for 0 <= beta < 1), by Newton, for any real theta."""
    th = np.asarray(th, float)
    s = th.copy()
    if beta == 0.0:
        return s
    for _ in range(100):
        f = s + 0.5 * beta * np.sin(2 * s) - th
        s = s - f / (1.0 + beta * np.cos(2 * s))
        if np.abs(f).max() < 1e-15:
            break
    return s


def dct1_cheb(vals):
    """Chebyshev coefficients (in z = 2q - 1) of the degree-N interpolant through values at z_i = -cos(pi i/N),
    i = 0..N, along axis 0 (DCT-I with halved end terms)."""
    v = np.asarray(vals, float)
    N = v.shape[0] - 1
    # reorder to z_j = cos(pi j/N): j = N - i
    f = v[::-1]
    j = np.arange(N + 1)
    wt = np.ones(N + 1); wt[0] = wt[-1] = 0.5
    Cm = np.cos(np.pi * np.outer(j, j) / N)              # (k, j)
    c = (2.0 / N) * (Cm * wt[None, :]) @ f.reshape(N + 1, -1)
    c[0] *= 0.5; c[-1] *= 0.5
    return c.reshape((N + 1,) + v.shape[1:])


class NumTrial:
    def __init__(self, path, device='cuda', c_l=None):
        d = np.load(path, allow_pickle=True)
        self.path, self.dev = path, device
        self.N, self.M, self.L = int(d['N']), int(d['M']), float(d['L'])
        self.beta = float(d['beta']) if 'beta' in d.files else 0.0
        self.c_l_file = float(d['c_l'])
        self.c_l = self.c_l_file if c_l is None else float(c_l)
        self.k = 1.0 / self.c_l
        self.A = 2 * self.c_l - 1
        self.p3 = 6 + 2.0 / self.A
        self.Cfile = float(d['C']) if 'C' in d.files else None
        b = np.asarray(d['b'], float)
        assert b.shape == (self.N + 1, self.M)
        self.bnodes = b
        # own node sets, compared with the stored ones
        qn = 0.5 * (1.0 - np.cos(np.pi * np.arange(self.N + 1) / self.N))
        sj = (np.arange(self.M) + 0.5) * np.pi / (2 * self.M)
        thn = sj + 0.5 * self.beta * np.sin(2 * sj)
        self.node_check = dict(q=float(np.abs(qn - np.asarray(d['q'])).max()),
                               theta=float(np.abs(thn - np.asarray(d['theta'])).max()))
        self.qn, self.sj, self.thn = qn, sj, thn
        m = np.arange(self.M)
        V = np.cos(np.outer(sj, 2 * m))                      # (j, m)
        Cs = np.linalg.solve(V, b.T).T                        # (i, m): C_m(q_i)
        self.Cs = Cs
        self.cheb = dct1_cheb(Cs)                             # (N+1 Chebyshev coefficients in z, M)
        self.cder = [self.cheb]

    def _cd(self, j):
        while len(self.cder) <= j:
            last = self.cder[-1]
            self.cder.append(Ch.chebder(last, axis=0) if last.shape[0] > 1 else np.zeros((1, self.M)))
        return self.cder[j]

    def Cm_at(self, q, j=0):
        """d^j C_m / dq^j at q (numpy), shape (len(q), M)."""
        z = 2 * np.asarray(q, float) - 1
        return Ch.chebval(z, self._cd(j)).T * 2.0 ** j if self._cd(j).shape[0] > 0 else np.zeros((len(z), self.M))

    def interior_knots_r(self):
        return np.array([])

    def radial(self, r, K):
        """Jets in r: W0 = r^3 w(r) (K+1, Nr), Rm = C_m(q(r)) (K+1, Nr, M)."""
        dev = self.dev
        r = torch.as_tensor(r, dtype=DT, device=dev)
        k, L = self.k, self.L
        rj = J.var(r, K)
        u2 = J.mul(rj, rj) / L ** 2
        one = J.const(torch.ones_like(r), K)
        lg = J.log(u2 + one)
        W0 = J.mul(J.pw(rj, 3.0), J.exp((k - 3) / 2 * lg))
        q = -J.exp(-(1 - k) / 2 * lg)
        q[0] = q[0] + 1.0
        q0 = q[0].cpu().numpy()
        fd = [torch.as_tensor(self.Cm_at(q0, j), dtype=DT, device=dev) for j in range(K + 1)]
        Rm = J.compose(fd, q.unsqueeze(-1))
        return dict(r=r, W0=W0, Rm=Rm, q0=q0)

    def angular(self, th):
        thn = np.asarray(th.detach().cpu().numpy() if torch.is_tensor(th) else th, float)
        s = s_of_theta(thn, self.beta)
        sp = 1.0 / (1.0 + self.beta * np.cos(2 * s))         # ds/dtheta
        m = np.arange(self.M)
        T = lambda a: torch.as_tensor(a, dtype=DT, device=self.dev)
        th_t = T(thn)
        co, si = torch.cos(th_t), torch.sin(th_t)
        return dict(th=th_t, cs=T(np.cos(np.outer(2 * m, s))), dcs=T(-2 * m[:, None] * np.sin(np.outer(2 * m, s)) * sp[None, :]),
                    co=co, si=si, Pi=co ** 2 * si, dPi=co ** 3 - 2 * co * si ** 2)

    def field(self, rad, an, K, theta=True):
        """Jets in r of rho and rho_theta on the tensor grid (K+1, Nr, Nth)."""
        Kp = min(K, rad['W0'].shape[0] - 1)
        W0 = rad['W0'][:Kp + 1]
        Rm = rad['Rm'][:Kp + 1]
        bb = torch.einsum('krm,mt->krt', Rm, an['cs'])
        Wb = J.mul(W0.unsqueeze(-1), bb)
        rho = Wb * an['Pi'][None, None, :]
        if not theta:
            return rho, None
        bt = torch.einsum('krm,mt->krt', Rm, an['dcs'])
        rhot = Wb * an['dPi'][None, None, :] + J.mul(W0.unsqueeze(-1), bt) * an['Pi'][None, None, :]
        return rho, rhot

    def axis(self, x, K):
        """x-jets on the x-axis of g = d_y rho(x, 0) = x^2 a(x, 0) and G_3 = d_y^3 rho(x, 0)/6 = x^2 a_2(x),
        a = w b, a_2 = (1/2) d_y^2 a(x, 0) = (1/2) [a_r/r + a_thth/r^2] at theta = 0 (a even in theta);
        b_thth(q, 0) = -sum_m (2m)^2 C_m(q) s'(0)^2, s'(0) = 1/(1 + beta)."""
        rad = self.radial(x, K + 1)
        r = rad['r']
        Kq = K + 1
        rj = J.var(r, Kq)
        w = J.mul(rad['W0'], J.recip(J.pw(rj, 3.0)))
        m = torch.arange(self.M, dtype=DT, device=self.dev)
        b0 = rad['Rm'].sum(-1)
        btt = -(rad['Rm'] * (2 * m) ** 2).sum(-1) / (1.0 + self.beta) ** 2
        a = J.mul(w, b0)
        att = J.mul(w, btt)
        ar = J.deriv(a)
        x_ = J.var(r, K)
        a2 = 0.5 * (J.mul(ar, J.recip(x_)) + J.mul(att[:K + 1], J.recip(J.mul(x_, x_))))
        x2 = J.mul(x_, x_)
        return dict(g=J.mul(x2, a[:K + 1]), G3=J.mul(x2, a2), a=a[:K + 1], a2=a2)
