"""M2: physical-space Biot-Savart quadrature for the velocity, independent of the modal
method M1 in vbs.py.

  U(X) = (1/2pi) int_{R^2} (y - y2, -(x - y1)) / |X-Y|^2 Omega(Y) dY      (U = (-Psi_y, Psi_x)).

Omega is extended to R^2 by its odd-odd parity.  Partition of unity around each target:
  local  part: chi(|Y-X|/delta) Omega, polar coordinates centred at X (the 1/rho kernel singularity
               is cancelled by the Jacobian; Gauss-Legendre in rho, trapezoid in angle);
  global part: (1-chi) Omega on a full-plane log-polar grid centred at the origin (Gauss panels in
               xi = log r, periodic trapezoid in phi).  The integrand is C^infinity there.
Tail r > R = e^{xi_max} omitted unless tail_fn is given (tail_fn(X) returns the velocity due to
the exterior region, computed by the caller from an explicit far-field model).
Runs on the GPU with torch float64.
"""
import numpy as np
import torch
from numpy.polynomial.legendre import leggauss

DEV = 'cuda' if torch.cuda.is_available() else 'cpu'


def smooth_step(t):
    t = np.clip(t, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        a = np.where(t > 0, np.exp(-1.0 / np.where(t > 0, t, 1)), 0.0)
        b = np.where(t < 1, np.exp(-1.0 / np.where(t < 1, 1 - t, 1)), 0.0)
    return a / (a + b)


def chi(u, u0=0.2):
    return 1.0 - smooth_step((u - u0) / (1.0 - u0))


def chi_t(u, u0=0.2):
    t = torch.clamp((u - u0) / (1.0 - u0), 0.0, 1.0)
    tp = torch.where(t > 0, t, torch.ones_like(t)); tm = torch.where(t < 1, 1 - t, torch.ones_like(t))
    a = torch.where(t > 0, torch.exp(-1.0 / tp), torch.zeros_like(t))
    b = torch.where(t < 1, torch.exp(-1.0 / tm), torch.zeros_like(t))
    return 1.0 - a / (a + b)


def omega_full(Omega_q1, X, Y):
    """odd-odd extension of a Q1 function"""
    sx = np.sign(X); sy = np.sign(Y)
    return sx * sy * Omega_q1(np.abs(X), np.abs(Y))


def bs_direct(Omega_q1, xt, yt, nphi=2048, p=16, xi_min=-14.0, xi_max=14.0, dxi=0.05,
              delta_frac=0.3, delta_min=1e-3, nrho=48, nalpha=96, tail_fn=None, tbatch=8):
    xt = np.asarray(xt, float).ravel(); yt = np.asarray(yt, float).ravel()
    nt = xt.size
    # global log-polar grid
    br = np.arange(xi_min, xi_max + 1e-12, dxi)
    g, wg = leggauss(p)
    a = br[:-1][:, None]; b = br[1:][:, None]
    xi = (0.5 * (a + b) + 0.5 * (b - a) * g[None, :]).ravel()
    wxi = (0.5 * (b - a) * wg[None, :]).ravel()
    rr = np.exp(xi)
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    dph = 2 * np.pi / nphi
    R = rr[:, None]; P = ph[None, :]
    YX = R * np.cos(P); YY = R * np.sin(P)
    Om = omega_full(Omega_q1, YX, YY)
    Wq = (wxi * rr * rr)[:, None] * dph * np.ones_like(P)      # dY = r^2 dxi dphi
    yx = torch.tensor(YX.ravel(), device=DEV); yy = torch.tensor(YY.ravel(), device=DEV)
    wom = torch.tensor((Wq * Om).ravel(), device=DEV)
    del YX, YY, Om, Wq
    # local polar grids
    gr, wgr = leggauss(nrho)
    al = (np.arange(nalpha) + 0.5) * 2 * np.pi / nalpha
    U1 = np.zeros(nt); U2 = np.zeros(nt)
    rt = np.hypot(xt, yt)
    delta = np.maximum(delta_frac * rt, delta_min)
    for i0 in range(0, nt, tbatch):
        sl = slice(i0, min(nt, i0 + tbatch))
        X = torch.tensor(xt[sl], device=DEV)[:, None]; Y = torch.tensor(yt[sl], device=DEV)[:, None]
        dl = torch.tensor(delta[sl], device=DEV)[:, None]
        dx = X - yx[None, :]; dy = Y - yy[None, :]
        d2 = dx * dx + dy * dy
        w = wom[None, :] * (1.0 - chi_t(torch.sqrt(d2) / dl)) / d2
        U1[sl] += (torch.sum(w * dy, dim=1) / (2 * np.pi)).cpu().numpy()
        U2[sl] += (torch.sum(-w * dx, dim=1) / (2 * np.pi)).cpu().numpy()
        del dx, dy, d2, w
    # local parts
    for i in range(nt):
        d = delta[i]
        rho = 0.5 * d * (gr + 1); wrho = 0.5 * d * wgr
        PX = xt[i] + rho[:, None] * np.cos(al)[None, :]
        PY = yt[i] + rho[:, None] * np.sin(al)[None, :]
        val = omega_full(Omega_q1, PX, PY) * chi(rho / d)[:, None] * wrho[:, None] * (2 * np.pi / nalpha)
        U1[i] += np.sum(val * (-np.sin(al))[None, :]) / (2 * np.pi)
        U2[i] += np.sum(val * (np.cos(al))[None, :]) / (2 * np.pi)
    if tail_fn is not None:
        t1, t2 = tail_fn(xt, yt)
        U1 += t1; U2 += t2
    return U1, U2
