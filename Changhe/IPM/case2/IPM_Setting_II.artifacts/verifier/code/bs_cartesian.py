"""Independent Cartesian real-space full-plane inverse for IPM profiles (independent verifier).

Velocity law (canonical sublinear class, |rho| <= C(1+|X|)^k, k < 1):
   U(X) - U(0) = p.v. int [K(X-Y) - K(-Y)] rho(Y) dY - (0, (rho(X) - rho(0))/2),
   K(W) = ( -w1 w2 / (pi |W|^4), (w1^2 - w2^2) / (2 pi |W|^4) ).
Discretisation (no polar modes, no periodic Poisson solve):
 * rho = f + g with f = rho chi(|Y|) (smooth radial cutoff chi = 1 for |Y| < L1, 0 for |Y| > L2), g = rho (1 - chi).
 * f-part on a uniform Cartesian grid (spacing h, box [-B,B]^2), as a free-space (zero padded, Hockney) discrete
   convolution: Ewald-type split K = K eta + K (1-eta), eta = (1 + r^2/sigma^2) exp(-r^2/sigma^2). K(1-eta) is real
   analytic and sampled (trapezoid rule); K eta is applied with its exact continuous Fourier transform
      FT[K1 eta](xi) = sin(2 phi) H(|xi|),  FT[K2 eta](xi) = -cos(2 phi) H(|xi|),  H(q) = (1 - exp(-q^2 sigma^2/4))/2.
 * g-part: direct quadrature of [K(X-Y) - K(-Y)] g(Y) on a polar grid in |Y| in [L1, inf) (no singularity for |X| < L1).
Derivatives: Fourier differentiation of f on the padded Cartesian grid (exact where chi = 1).
"""
import numpy as np, torch, scipy.special as ss

dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
DT = torch.float64

def smoothstep(t):
    """C^inf step: 0 for t<=0, 1 for t>=1."""
    t = np.clip(t, 0, 1)
    a = np.where(t > 0, np.exp(-1.0 / np.maximum(t, 1e-300)), 0.0)
    b = np.where(t < 1, np.exp(-1.0 / np.maximum(1 - t, 1e-300)), 0.0)
    return a / (a + b)

def smoothstep_t(t):
    t = torch.clamp(t, 0, 1)
    a = torch.where(t > 0, torch.exp(-1.0 / torch.clamp(t, min=1e-300)), torch.zeros_like(t))
    b = torch.where(t < 1, torch.exp(-1.0 / torch.clamp(1 - t, min=1e-300)), torch.zeros_like(t))
    return a / (a + b)

def eta_np(r, delta):          # 1 for r < delta/4, 0 for r > delta
    return 1.0 - smoothstep((r / delta - 0.25) / 0.75)

def chi_t(r, L1, L2):          # 1 for r < L1, 0 for r > L2
    return 1.0 - smoothstep_t((r - L1) / (L2 - L1))

class CartesianBS:
    def __init__(self, B, h, L1, L2, sigma=None):
        self.B, self.h, self.L1, self.L2 = B, h, L1, L2
        n = int(round(2 * B / h))
        if n % 2: n += 1
        self.n = n
        self.x1 = -B + h * torch.arange(n, dtype=DT, device=dev)       # grid includes 0 at index n/2
        self.i0 = n // 2
        self.X, self.Y = torch.meshgrid(self.x1, self.x1, indexing='ij')
        self.Rg = torch.sqrt(self.X ** 2 + self.Y ** 2)
        self.sigma = sigma if sigma is not None else 4 * h
        self.nmid = 8
        self._build_kernel()

    def _build_kernel(self):
        """Ewald-type split K = K eta + K (1 - eta), eta(r) = (1 + s) e^{-s}, s = r^2/sigma^2.
        1 - eta = O(r^4), so K (1-eta) is real analytic (K ~ r^{-2} x angular mode 2); it is sampled on the
        padded grid (free-space discrete convolution, spectrally accurate trapezoid rule).
        K eta is applied with its exact Fourier transform (closed form, checked by quadrature):
           FT[K1 eta] = sin(2 phi) H(q), FT[K2 eta] = -cos(2 phi) H(q), H(q) = (1 - exp(-q^2 sigma^2/4))/2."""
        n, h, sg = self.n, self.h, self.sigma
        M = 2 * n
        k = torch.arange(M, dtype=DT, device=dev)
        off = torch.where(k < M // 2, k, k - M) * h
        WX, WY = torch.meshgrid(off, off, indexing='ij')
        R2 = WX ** 2 + WY ** 2
        s = R2 / sg ** 2
        # (1 - eta)/r^4 = (1 - (1+s)e^{-s}) / (s^2 sigma^4), series for small s
        big = s > 1e-2
        sb = torch.where(big, s, torch.ones_like(s))
        g_big = (-torch.expm1(-sb) - sb * torch.exp(-sb)) / sb ** 2
        g_small = 0.5 - s / 3 + s ** 2 / 8 - s ** 3 / 30 + s ** 4 / 144 - s ** 5 / 840 + s ** 6 / 5760
        g = torch.where(big, g_big, g_small) / sg ** 4
        K1 = -WX * WY / np.pi * g
        K2 = (WX ** 2 - WY ** 2) / (2 * np.pi) * g
        F1 = torch.fft.fft2(K1) * h * h
        F2 = torch.fft.fft2(K2) * h * h
        fr = torch.fft.fftfreq(M, d=h, dtype=DT, device=dev) * 2 * np.pi
        QX, QY = torch.meshgrid(fr, fr, indexing='ij')
        Q2 = QX ** 2 + QY ** 2
        H = -0.5 * torch.expm1(-Q2 * sg ** 2 / 4)
        Q2s = torch.where(Q2 > 0, Q2, torch.ones_like(Q2))
        s2 = 2 * QX * QY / Q2s          # sin 2 phi
        c2 = (QX ** 2 - QY ** 2) / Q2s  # cos 2 phi
        self.F1 = F1 + s2 * H
        self.F2 = F2 - c2 * H
        self.QX, self.QY = QX, QY

    def pad(self, f):
        M = 2 * self.n
        out = torch.zeros((M, M), dtype=DT, device=dev)
        out[:self.n, :self.n] = f
        return out

    def near_far_f(self, f):
        """Free-space K * f on the grid (f compactly supported inside the box). Returns (V1, V2) = int K(X-Y) f(Y) dY."""
        fh = torch.fft.fft2(self.pad(f))
        V1 = torch.fft.ifft2(fh * self.F1).real[:self.n, :self.n]
        V2 = torch.fft.ifft2(fh * self.F2).real[:self.n, :self.n]
        return V1, V2

    def grad_f(self, f):
        fh = torch.fft.fft2(self.pad(f))
        fx = torch.fft.ifft2(1j * self.QX * fh).real[:self.n, :self.n]
        fy = torch.fft.ifft2(1j * self.QY * fh).real[:self.n, :self.n]
        return fx, fy

    def far_g(self, rho_fn, Xt, Yt, k=0.0, Lmax=1e9, P=60, q=16, nth=512):
        """int [K(X-Y) - K(-Y)] rho(Y)(1-chi(|Y|)) dY for targets (Xt,Yt) (torch 1-D) with |X| < L1,
        polar quadrature over |Y| in [L1, Lmax] (geometric panels) plus nothing beyond Lmax (tail ~ Lmax^(k-1))."""
        xg, wg = np.polynomial.legendre.leggauss(q)
        e = np.concatenate([np.linspace(self.L1, self.L2, self.nmid + 1), np.geomspace(self.L2, Lmax, P)[1:]])
        rr = np.concatenate([a + (b - a) * (xg + 1) / 2 for a, b in zip(e[:-1], e[1:])])
        ww = np.concatenate([wg * (b - a) / 2 for a, b in zip(e[:-1], e[1:])])
        th = 2 * np.pi * np.arange(nth) / nth
        rr = torch.tensor(rr, dtype=DT, device=dev); ww = torch.tensor(ww, dtype=DT, device=dev)
        th = torch.tensor(th, dtype=DT, device=dev)
        Rr, Tt = torch.meshgrid(rr, th, indexing='ij')
        YX = (Rr * torch.cos(Tt)).ravel(); YY = (Rr * torch.sin(Tt)).ravel()
        g = rho_fn(YX, YY) * (1 - chi_t(Rr.ravel(), self.L1, self.L2))
        wq = (ww[:, None] * Rr * (2 * np.pi / nth)).ravel() * g
        # cancellation-free difference: with complex w = w1 + i w2, K2 + i K1 = 1/(2 pi w^2), hence
        # [K2 + i K1](X-Y) - [K2 + i K1](-Y) = x (2y - x) / (2 pi (x-y)^2 y^2)   (x, y complex for X, Y)
        yc = torch.complex(YX, YY)
        out1 = torch.zeros_like(Xt); out2 = torch.zeros_like(Xt)
        bs = max(1, int(1e8 // YX.numel()))
        for i in range(0, Xt.numel(), bs):
            xc = torch.complex(Xt[i:i + bs], Yt[i:i + bs])[:, None]
            D = xc * (2 * yc[None, :] - xc) / (2 * np.pi * (xc - yc[None, :]) ** 2 * yc[None, :] ** 2)
            out2[i:i + bs] = (D.real * wq[None, :]).sum(1)
            out1[i:i + bs] = (D.imag * wq[None, :]).sum(1)
        return out1, out2

    def velocity(self, rho_fn, k=0.0, region=None, Lmax=1e9, **kw):
        """U(X)-U(0) on the grid points inside |X| < region (default L1/2). rho_fn: torch callable (X,Y)->rho."""
        region = region if region is not None else self.L1 / 2
        rho = rho_fn(self.X, self.Y)
        chi = chi_t(self.Rg, self.L1, self.L2)
        f = rho * chi
        V1, V2 = self.near_far_f(f)
        msk = self.Rg < region
        Xt = self.X[msk]; Yt = self.Y[msk]
        g1, g2 = self.far_g(rho_fn, Xt, Yt, k=k, Lmax=Lmax, **kw)
        i0 = self.i0
        U1 = V1[msk] - V1[i0, i0] + g1
        U2 = V2[msk] - V2[i0, i0] + g2 - (rho[msk] - rho[i0, i0]) / 2
        return msk, U1, U2, rho, f
