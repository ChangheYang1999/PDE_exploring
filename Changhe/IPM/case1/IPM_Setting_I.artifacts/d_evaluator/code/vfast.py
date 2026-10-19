"""Vectorized version of the verifier's polar inverse (same discretization as vpolar.py: exact exponential weights
against local Lagrange interpolants on a uniform log r grid), for repeated use inside the verifier's solver.
The recursions Q_{j+1} = e Q_j + b_j are done with scipy.signal.lfilter."""
import numpy as np
from scipy.signal import lfilter
from vpolar import LogGrid


class FastInverse:
    def __init__(self, g, nmax):
        self.g = g
        self.ns = np.arange(2, nmax + 1, 2)
        N = g.N
        self.st = np.array([g._stencil(j) for j in range(N - 1)])  # (N-1, q)
        # the weights depend on j only through the stencil offset lo - j (uniform grid): compute once per offset
        off = self.st[:, 0] - np.arange(N - 1)
        reps = {o: int(np.where(off == o)[0][0]) for o in np.unique(off)}
        def table(lam, bwd):
            W = np.empty((N - 1, g.q))
            for o, j in reps.items():
                W[off == o] = g._weights(lam, j, bwd)[1]
            return W
        self.Wf = np.array([table(float(n), False) for n in self.ns])
        self.Wb = np.array([table(float(n), True) for n in self.ns])
        self.W0 = table(0.0, False)
        self.e = np.exp(-self.ns * g.h)

    def solve(self, F, tail_hi=None, tail_lo=None):
        """F: (M, N) array, F[i] = f_{2i+1}(r) (odd sine modes of rho).  tail_hi: (A[M], k) with f_m ~ A_m r^k for r > R;
        tail_lo: (f0[M], beta[M]) with f_m(r) = f0_m (r/r0)^beta_m for r < r0 (f0_m = f_m(r0)).
        Returns p, dp: (nn, N) for n = 2, 4, ..., and c = int f_3 r^{-2} dr."""
        g = self.g
        r = g.r
        M, N = F.shape
        nn = len(self.ns)
        p = np.zeros((nn, N))
        dp = np.zeros((nn, N))
        for a, n in enumerate(self.ns):
            ilo = (n - 1 - 1) // 2   # index of f_{n-1}
            ihi = (n + 1 - 1) // 2   # index of f_{n+1}
            flo = F[ilo] if ilo < M else np.zeros(N)
            fhi = F[ihi] if ihi < M else np.zeros(N)
            glo = r * flo
            ghi = r * fhi
            blo = np.einsum('jk,jk->j', self.Wf[a], glo[self.st])
            bhi = np.einsum('jk,jk->j', self.Wb[a], ghi[self.st])
            Q0 = 0.0
            if tail_lo is not None and ilo < M:
                f0, be = tail_lo[0][ilo], tail_lo[1][ilo]
                Q0 = f0 * r[0] / (n + be + 1)
            QN = 0.0
            if tail_hi is not None and ihi < M:
                A, k = tail_hi[0][ihi], tail_hi[1]
                QN = A * r[-1] ** (k + 1) / (n - k - 1)
            e = self.e[a]
            Slo = np.empty(N)
            Slo[0] = Q0
            Slo[1:] = lfilter([1.0], [1.0, -e], blo, zi=[e * Q0])[0]
            Shi = np.empty(N)
            Shi[-1] = QN
            Shi[:-1] = lfilter([1.0], [1.0, -e], bhi[::-1], zi=[e * QN])[0][::-1]
            p[a] = 0.5 * (Shi - Slo)
            dp[a] = n / (2 * r) * (Shi + Slo) - 0.5 * (fhi + flo)
        # c = int f_3 / r du-measure: int f_3 r^{-2} dr = int f_3 r^{-1} du
        f3 = F[1]
        b0 = np.einsum('jk,jk->j', self.W0, (f3 / r)[self.st])
        c = b0.sum()
        if tail_hi is not None:
            A, k = tail_hi[0][1], tail_hi[1]
            c += A * r[-1] ** (k - 1) / (1 - k)
        if tail_lo is not None:
            f0, be = tail_lo[0][1], tail_lo[1][1]
            c += f0 / (r[0] * (be - 1))
        return p, dp, c
