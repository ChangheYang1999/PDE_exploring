"""verifier: manufactured axis data (w, g, G_3 as analytic x-jets) in the AxisData interface, for validating the B_j
estimators on data with known B_j."""
import math
import numpy as np
import torch
from numpy.polynomial import legendre as Lg
import jets as J
from vaxis import AxisData

DT = torch.float64


class ManualAxis(AxisData):
    """jetfun(x_torch, K) -> dict(w=..., g=..., G3=..., [G5=...]) of Taylor-coefficient jets (K+1, n)."""

    def __init__(self, jetfun, c_l, xstar, K=6, q=20, xmin=1e-3, hmax=0.25, extra_breaks=()):
        self.jetfun, self.c_l, self.xs, self.K, self.q = jetfun, c_l, xstar, K, q
        self.dev = 'cpu'
        t0, ts = math.log(xmin), math.log(xstar)
        m = int(math.ceil((ts - t0) / hmax))
        b = t0 + (ts - t0) * np.arange(m + 1) / m
        self.b = np.unique(np.concatenate([b, list(extra_breaks)]))
        self.P = len(self.b) - 1
        self.xg, self.wg = Lg.leggauss(q)
        self.t = np.concatenate([self.b[j] + (self.xg + 1) * (self.b[j + 1] - self.b[j]) / 2 for j in range(self.P)])
        self.x = np.exp(self.t)
        self.wj = self.jets_at(self.x)
        self.coef = {key: self._fit(arr) for key, arr in self.wj.items()}

    def jets_at(self, x):
        d = self.jetfun(torch.as_tensor(np.atleast_1d(x), dtype=DT), self.K)
        return {k: v.numpy() for k, v in d.items()}


def s2h_pair(A):
    """SPEC S2 (h): w = -(A/k) sin kx, g = A (1 - cos kx), k = sqrt(2/A); G_3 = 0 (exact)."""
    k = math.sqrt(2 / A)

    def f(x, K):
        X = J.var(x, K)
        kx = k * X
        # sin, cos jets from exp of i kx: use Taylor directly
        s = torch.zeros_like(X)
        c = torch.zeros_like(X)
        x0 = x * k
        for j in range(K + 1):
            # d^j sin(k x)/dx^j / j! = k^j sin(kx + j pi/2) / j!
            s[j] = k ** j * torch.sin(x0 + j * math.pi / 2) / math.factorial(j)
            c[j] = k ** j * torch.cos(x0 + j * math.pi / 2) / math.factorial(j)
        w = -(A / k) * s
        one = J.const(torch.ones_like(x), K)
        g = A * (one - c)
        return dict(w=w, g=g, G3=torch.zeros_like(X))
    return f, (A + 1) / 2, math.pi / k


def r12_family(A, L):
    """R12: w = -A x (1 - u^2)/(1 + u^2), u = x/L; T_1 = 0 gives g = x^2/(1 + u^2) (g ~ x^2); x* = L, w'(L) = A."""
    def f(x, K):
        X = J.var(x, K)
        U2 = J.mul(X, X) / L ** 2
        one = J.const(torch.ones_like(x), K)
        rr = J.recip(one + U2)
        w = -A * J.mul(X, J.mul(one - U2, rr))
        g = J.mul(J.mul(X, X), rr)
        return dict(w=w, g=g, G3=torch.zeros_like(X))
    return f, (A + 1) / 2, L
