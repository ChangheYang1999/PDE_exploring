"""Independent full-plane inverse for IPM profiles (independent verifier).

Method (genuinely different from a periodic-box FFT): polar Fourier modes about the origin X=0 and the exact radial
Green's function of the Laplacian, evaluated with composite Gauss-Legendre panels and cumulative spectral integration.

Let phi solve -Lap phi = rho, psi = d_x phi, U = grad^perp psi = (-phi_xy, phi_xx). With W = d_z^2 phi (z = x+iy),
   U = (2 Im W, 2 Re W - rho/2).
For rho = sum_m rho_m(r) e^{i m theta}, mode m of phi contributes to W the term w_m(r) e^{i(m-2) theta}, with
   m <= 0 :  w_m = (1/4)[ -rho_m + 2(1+|m|) r^{-|m|-2} int_0^r s^{|m|+1} rho_m ds ]
   m = 1  :  w_1 = -(1/4) rho_1
   m >= 2 :  w_m = (1/4)[ -rho_m + 2(m-1) r^{m-2} B_m(r) ],   B_m(r) = int_r^inf s^{1-m} rho_m ds.
Renormalisation (the velocity law): for modes with divergent B_m (growth |rho| ~ r^k needs m > k+2) B_m is replaced by
B_m(r) - B_m(0) = -int_0^r s^{1-m} rho_m ds; this changes W by a polynomial c z^{m-2}, i.e. a harmonic gauge field in U
of degree m-2. For k < 1 only m = 2 is renormalised and only a constant is affected, which U(X) - U(0) removes: this is
the canonical sublinear law U(X)-U(0) = p.v.int [K(X-Y)-K(-Y)] rho(Y) dY - (0,(rho(X)-rho(0))/2).
The parameter `ren_modes` lists the |m| >= 2 that are renormalised (default {2}).
"""
import numpy as np

def gl_panels(edges, q):
    """Composite Gauss-Legendre nodes/weights on panels given by edges; returns r, w, panel index arrays and
    the per-panel cumulative integration matrix (q x q) mapping nodal values to int_{a}^{r_i}."""
    xg, wg = np.polynomial.legendre.leggauss(q)
    # cumulative integration matrix on [-1,1]: C[i,j] = int_{-1}^{x_i} l_j(t) dt (Lagrange basis on GL nodes)
    V = np.polynomial.legendre.legvander(xg, q - 1)          # V[i,n] = P_n(x_i)
    Vinv = np.linalg.inv(V)
    # int_{-1}^{x} P_n = (P_{n+1}-P_{n-1})/(2n+1) for n>=1, and x+1 for n=0
    Ic = np.zeros((q, q))
    for n in range(q):
        if n == 0:
            Ic[:, 0] = xg + 1
        else:
            cp = np.zeros(n + 2); cp[n + 1] = 1
            cm = np.zeros(n + 2); cm[n - 1] = 1
            Ic[:, n] = (np.polynomial.legendre.legval(xg, cp) - np.polynomial.legendre.legval(xg, cm)) / (2 * n + 1)
    C = Ic @ Vinv
    # differentiation matrix on GL nodes
    Dl = np.zeros((q, q))
    for n in range(q):
        c = np.zeros(q); c[n] = 1
        Dl[:, n] = np.polynomial.legendre.legval(xg, np.polynomial.legendre.legder(c))
    D = Dl @ Vinv
    r, w, h = [], [], []
    for a, b in zip(edges[:-1], edges[1:]):
        r.append(a + (b - a) * (xg + 1) / 2); w.append(wg * (b - a) / 2); h.append((b - a) / 2)
    return np.concatenate(r), np.concatenate(w), np.array(h), C, D

class PolarGrid:
    def __init__(self, edges, q=16, ntheta=256):
        self.edges = np.asarray(edges, float)
        self.q = q; self.P = len(edges) - 1
        self.r, self.w, self.h, self.C, self.D = gl_panels(self.edges, q)
        self.nt = ntheta
        self.th = 2 * np.pi * np.arange(ntheta) / ntheta
        self.R, self.T = np.meshgrid(self.r, self.th, indexing='ij')
        self.X = self.R * np.cos(self.T); self.Y = self.R * np.sin(self.T)
        self.m = np.fft.fftfreq(ntheta, 1.0 / ntheta).astype(int)

    def cum0(self, f):
        """int_0^{r_i} f(s) ds for nodal values f (shape Nr x ...), panelwise spectral."""
        P, q = self.P, self.q
        fs = f.reshape((P, q) + f.shape[1:])
        loc = np.einsum('ij,pj...->pi...', self.C, fs) * self.h.reshape((P, 1) + (1,) * (f.ndim - 1))
        wg = np.polynomial.legendre.leggauss(q)[1]
        ptot = np.einsum('j,pj...->p...', wg, fs) * self.h.reshape((P,) + (1,) * (f.ndim - 1))
        offs = np.concatenate([np.zeros((1,) + ptot.shape[1:], ptot.dtype), np.cumsum(ptot, axis=0)[:-1]], axis=0)
        out = loc + offs[:, None]
        return out.reshape(f.shape), np.sum(ptot, axis=0)

    def dr(self, f):
        P, q = self.P, self.q
        fs = f.reshape((P, q) + f.shape[1:])
        d = np.einsum('ij,pj...->pi...', self.D, fs) / self.h.reshape((P, 1) + (1,) * (f.ndim - 1))
        return d.reshape(f.shape)

    def modes(self, F):
        return np.fft.fft(F, axis=1) / self.nt   # F_m(r) with F = sum_m F_m e^{i m th}

    def synth(self, Fm):
        return np.fft.ifft(Fm, axis=1) * self.nt

    def _subrules(self):
        """For each reference node x_i: Gauss sub-rules on [-1,x_i] and [x_i,1] with interpolation matrices from the
        panel nodes (Lagrange basis on the q GL nodes). Returns (sigL, wL, LL, sigR, wR, LR), each indexed [i,k(,j)]."""
        if hasattr(self, '_sr'): return self._sr
        q = self.q
        xg, wg = np.polynomial.legendre.leggauss(q)
        bw = np.array([1.0 / np.prod([xg[j] - xg[l] for l in range(q) if l != j]) for j in range(q)])
        def lag(t):
            d = t[:, None] - xg[None, :]
            ex = np.isclose(d, 0, atol=1e-15)
            d[ex] = 1.0
            M = bw[None, :] / d
            M = M / M.sum(axis=1, keepdims=True)
            rows = ex.any(axis=1)
            M[rows] = ex[rows].astype(float)
            return M
        sigL = np.zeros((q, q)); wL = np.zeros((q, q)); LL = np.zeros((q, q, q))
        sigR = np.zeros((q, q)); wR = np.zeros((q, q)); LR = np.zeros((q, q, q))
        for i in range(q):
            a, b = -1.0, xg[i]
            sigL[i] = a + (b - a) * (xg + 1) / 2; wL[i] = wg * (b - a) / 2; LL[i] = lag(sigL[i])
            a, b = xg[i], 1.0
            sigR[i] = a + (b - a) * (xg + 1) / 2; wR[i] = wg * (b - a) / 2; LR[i] = lag(sigR[i])
        self._sr = (sigL, wL, LL, sigR, wR, LR)
        return self._sr

    def _inner(self, fm, mu):
        """a(r_i) = r_i^{-mu-2} int_0^{r_i} s^{mu+1} f(s) ds = r_i^{-1} int_0^{r_i} (s/r_i)^{mu+1} f ds, stable."""
        P, q = self.P, self.q
        sigL, wL, LL, _, _, _ = self._subrules()
        wg = np.polynomial.legendre.leggauss(q)[1]
        out = np.zeros_like(fm)
        S = np.zeros(fm.shape[1], dtype=fm.dtype)
        e = self.edges
        for p in range(P):
            sl = slice(p * q, (p + 1) * q)
            s = self.r[sl]; f = fm[sl]; hp = self.h[p]
            sig = e[p] + hp * (sigL + 1)                       # (i,k) physical sub-nodes in [e_p, r_i]
            fi = np.einsum('ikj,jm->ikm', LL, f)               # interpolated f at sub-nodes
            ratio = (sig[:, :, None] / s[:, None, None]) ** (mu[None, None, :] + 1)
            part = hp * np.einsum('ik,ikm,ikm->im', wL, ratio, fi)
            pre = (e[p] / s[:, None]) ** (mu[None, :] + 1) * S[None, :] if e[p] > 0 else 0.0
            out[sl] = (pre + part) / s[:, None]
            S = (e[p] / e[p + 1]) ** (mu + 1) * S + hp * np.einsum('j,jm,jm->m', wg, (s[:, None] / e[p + 1]) ** (mu[None, :] + 1), f)
        return out

    def _outer(self, fm, nu, tail=None):
        """b(r_i) = int_{r_i}^{L} (r_i/s)^{nu} f(s)/s ds + (r_i/L)^nu tail, stable (nu >= 0)."""
        P, q = self.P, self.q
        _, _, _, sigR, wR, LR = self._subrules()
        wg = np.polynomial.legendre.leggauss(q)[1]
        out = np.zeros_like(fm)
        e = self.edges
        T = np.zeros(fm.shape[1], dtype=fm.dtype) if tail is None else np.asarray(tail).astype(fm.dtype)
        for p in range(P - 1, -1, -1):
            sl = slice(p * q, (p + 1) * q)
            s = self.r[sl]; f = fm[sl]; hp = self.h[p]
            sig = e[p] + hp * (sigR + 1)                       # sub-nodes in [r_i, e_{p+1}]
            fi = np.einsum('ikj,jm->ikm', LR, f)
            ratio = (s[:, None, None] / sig[:, :, None]) ** nu[None, None, :]
            part = hp * np.einsum('ik,ikm,ikm->im', wR, ratio / sig[:, :, None], fi)
            post = (s[:, None] / e[p + 1]) ** nu[None, :] * T[None, :]
            out[sl] = part + post
            if e[p] > 0:
                T = (e[p] / e[p + 1]) ** nu * T + hp * np.einsum('j,jm,jm->m', wg, (e[p] / s[:, None]) ** nu[None, :] / s[:, None], f)
        return out

    def velocity(self, rho, tail=None, ren_modes=(2,), rho0=0.0, mmax=None):
        """U(X)-U(0) on the grid from nodal rho (Nr x Nt).
        tail: optional dict m -> int_L^inf (L/s)^{m-2} rho_m(s)/s ds (far field beyond the last edge L) for m>=3.
        ren_modes: modes m>=2 renormalised by B_m -> B_m - B_m(0) (default (2,): canonical sublinear law)."""
        rm = self.modes(rho.astype(complex))
        nt = self.nt
        ms = self.m
        if mmax is not None:
            keep = np.abs(ms) <= mmax
        else:
            keep = np.ones_like(ms, bool)
        Wfull = np.zeros_like(rm)
        neg = np.where((ms <= 0) & keep)[0]
        if len(neg):
            mu = np.abs(ms[neg]).astype(float)
            a = self._inner(rm[:, neg], mu)
            w = 0.25 * (-rm[:, neg] + 2 * (1 + mu)[None, :] * a)
            for jj, j in enumerate(neg):
                Wfull[:, (ms[j] - 2) % nt] += w[:, jj]
        j1 = np.where(ms == 1)[0]
        for j in j1:
            Wfull[:, (1 - 2) % nt] += -0.25 * rm[:, j]
        pos = [j for j in np.where((ms >= 2) & keep)[0] if ms[j] not in ren_modes]
        if len(pos):
            pos = np.array(pos)
            nu = (ms[pos] - 2).astype(float)
            tl = None
            if tail is not None:
                tl = np.array([tail.get(int(ms[j]), 0.0) for j in pos])
            b = self._outer(rm[:, pos], nu, tl)
            w = 0.25 * (-rm[:, pos] + 2 * (ms[pos] - 1)[None, :] * b)
            for jj, j in enumerate(pos):
                Wfull[:, (ms[j] - 2) % nt] += w[:, jj]
        for m in ren_modes:
            j = np.where(ms == m)[0]
            if not len(j): continue
            j = j[0]
            # B_m - B_m(0) = -int_0^r s^{1-m} rho_m ds ; contributes 2(m-1) r^{m-2} * that
            I, _ = self.cum0(self.r ** (1 - m) * rm[:, j])
            Wfull[:, (m - 2) % nt] += 0.25 * (-rm[:, j] - 2 * (m - 1) * self.r ** (m - 2) * I)
        W = self.synth(Wfull)
        U1 = 2 * W.imag
        U2 = 2 * W.real - (rho - rho0) / 2
        return U1, U2

    def grad(self, f):
        """Cartesian gradient of nodal f via spectral d/dtheta and panel-polynomial d/dr."""
        fr = self.dr(f)
        fm = self.modes(f.astype(complex))
        ft = self.synth(1j * self.m[None, :] * fm).real
        c, s = np.cos(self.T), np.sin(self.T)
        return c * fr - s * ft / self.R, s * fr + c * ft / self.R
