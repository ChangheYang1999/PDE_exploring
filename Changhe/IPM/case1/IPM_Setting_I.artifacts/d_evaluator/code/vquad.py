"""Verifier's method B: target-centered polar quadrature of the weakly singular Biot-Savart integrals (GPU, torch).

U_1(X) = (1/2pi) int (y - y2)/|X-Y|^2 F(Y) dY,   U_2(X) = -(1/2pi) int (x - y1)/|X-Y|^2 F(Y) dY,   F = d_x rho.
With Y = X + t e_phi the kernel singularity cancels against the area element:
  U_1 = -(1/2pi) int_0^{2pi} sin(phi) int_0^{L(phi)} F(X + t e_phi) dt dphi,
  U_2 = +(1/2pi) int_0^{2pi} cos(phi) int_0^{L(phi)} F(X + t e_phi) dt dphi,
over the centered disc |Y| < RB (L(phi) = distance from X to the circle |Y| = RB along e_phi).
Region |Y| > RB (for |X| < RB): exact multipole form psi_tail = sum_n (r^n/(2n)) T_n sin(n t),
T_n = int_RB^inf s^{1-n} F_n(s) ds (F_n = sin(n t) coefficient of F), computed by radial quadrature to RF and an analytic
power-law tail beyond RF (F_n ~ A s^{k-1}).  Phi: trapezoid (periodic); t: composite Gauss-Legendre panels.
This uses no Fourier modes of rho on the disc, no FFT and no Green-function recursion: independent of method A (vpolar).
"""
import math
import numpy as np
import torch

dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
DT = torch.float64


def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return torch.tensor(x, dtype=DT, device=dev), torch.tensor(w, dtype=DT, device=dev)


def disc_velocity(F, X, RB, nphi=512, npan=48, ngl=16, t0=0.05, chunk=64):
    """U on targets X (numpy (P,2)) from F (torch callable F(x, y)) on the disc |Y| < RB.
    Ray variable t = t0 (e^{a s} - 1), s in [0,1], a = log(L/t0 + 1); npan GL panels of ngl points in s."""
    xg, wg = gl(ngl)
    phi = torch.arange(nphi, dtype=DT, device=dev) * (2 * math.pi / nphi)
    cph, sph = torch.cos(phi), torch.sin(phi)
    out = np.zeros((len(X), 2))
    for i0 in range(0, len(X), chunk):
        Xc = torch.tensor(X[i0:i0 + chunk], dtype=DT, device=dev)  # (B,2)
        B = Xc.shape[0]
        xd = Xc[:, 0:1] * cph[None, :] + Xc[:, 1:2] * sph[None, :]  # X.e_phi (B,nphi)
        rr2 = (Xc ** 2).sum(1, keepdim=True)
        L = -xd + torch.sqrt(xd ** 2 + RB ** 2 - rr2)  # (B,nphi)
        a = torch.log(L / t0 + 1.0)
        acc = torch.zeros(B, nphi, dtype=DT, device=dev)
        for p in range(npan):
            s0, s1 = p / npan, (p + 1) / npan
            s = 0.5 * (s0 + s1) + 0.5 * (s1 - s0) * xg  # (ngl,)
            ws = 0.5 * (s1 - s0) * wg
            ea = torch.exp(a[..., None] * s[None, None, :])  # (B,nphi,ngl)
            t = t0 * (ea - 1.0)
            dtds = t0 * a[..., None] * ea
            Yx = Xc[:, 0, None, None] + t * cph[None, :, None]
            Yy = Xc[:, 1, None, None] + t * sph[None, :, None]
            acc += (F(Yx, Yy) * dtds * ws[None, None, :]).sum(-1)
        U1 = -(acc * sph[None, :]).sum(1) * (2 * math.pi / nphi) / (2 * math.pi)
        U2 = (acc * cph[None, :]).sum(1) * (2 * math.pi / nphi) / (2 * math.pi)
        out[i0:i0 + B, 0] = U1.cpu().numpy()
        out[i0:i0 + B, 1] = U2.cpu().numpy()
    return out


def tail_coeffs(F, RB, RF, nmax, k_far, nth=256, nu=4000):
    """T_n = int_RB^inf s^{1-n} F_n(s) ds for even n <= nmax, F_n = (1/pi) int F(s,t) sin(n t) dt.
    Quadrature in u = log s on [log RB, log RF] (trapezoid-free: GL panels), power-law tail beyond RF."""
    xg, wg = gl(16)
    npan = nu // 16
    u0, u1 = math.log(RB), math.log(RF)
    th = torch.arange(nth, dtype=DT, device=dev) * (2 * math.pi / nth)
    T = {}
    acc = {n: 0.0 for n in range(2, nmax + 1, 2)}
    Fn_end = {}
    for p in range(npan):
        a, b = u0 + (u1 - u0) * p / npan, u0 + (u1 - u0) * (p + 1) / npan
        u = 0.5 * (a + b) + 0.5 * (b - a) * xg
        wu = 0.5 * (b - a) * wg
        s = torch.exp(u)
        Fv = F(s[:, None] * torch.cos(th)[None, :], s[:, None] * torch.sin(th)[None, :])  # (16, nth)
        for n in acc:
            Fn = (Fv * torch.sin(n * th)[None, :]).sum(1) * (2 / nth)
            acc[n] += float((s ** (2 - n) * Fn * wu).sum())  # ds = s du
    for n in acc:
        Fv = F(RF * torch.cos(th), RF * torch.sin(th))
        FnR = float((Fv * torch.sin(n * th)).sum() * (2 / nth))
        A = FnR / RF ** (k_far - 1)
        acc[n] += A * RF ** (k_far + 1 - n) / (n - k_far - 1)
        T[n] = acc[n]
    return T


def tail_velocity(T, X):
    """U from psi_tail = sum_n (r^n/(2n)) T_n sin(n t): U = (-psi_y, psi_x).
    r^n sin(n t) = Im (x + i y)^n, d/dx Im z^n = Im(n z^{n-1}), d/dy = Im(i n z^{n-1}) = Re(n z^{n-1})."""
    z = X[:, 0] + 1j * X[:, 1]
    psx = np.zeros(len(X))
    psy = np.zeros(len(X))
    for n, Tn in T.items():
        dz = n * z ** (n - 1)
        psx += Tn / (2 * n) * dz.imag
        psy += Tn / (2 * n) * dz.real
    return np.stack([-psy, psx], 1)
