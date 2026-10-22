"""Verifier's independent full-plane Biot-Savart evaluators for odd-odd vorticity.

Convention (PROMPT.md):  -Lap Psi = Omega on R^2,  U = (-Psi_y, Psi_x).
Canonical inverse: the unique odd-odd solution with grad Psi = o(|X|), i.e. no added harmonic
Im(z^{2n}) terms (n=1 is the excluded strain 2xy).

M1  modal Green formula.  Omega(r,phi) = sum_{n>=1} om_n(r) sin(2 n phi),
    psi_m(r) = (1/2m) [ int_0^r (rho/r)^m rho om_m drho + int_r^inf (r/rho)^m rho om_m drho ],  m=2n.
    Angular transform: midpoint rule on [0,pi/2] (= periodic trapezoid for the even, pi-periodic
    integrand), i.e. a DST-II.  Radial: Gauss-Legendre panels in xi = log rho, with every target
    radius a panel breakpoint, and the two weighted cumulative sums done recursively (stable).
M2  physical-space quadrature (see vbs_direct.py).
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.fft import dst


def _panels(breaks, p):
    """Gauss-Legendre nodes/weights in xi on consecutive intervals [breaks[k], breaks[k+1]]."""
    g, wg = leggauss(p)
    a = breaks[:-1][:, None]; b = breaks[1:][:, None]
    xi = 0.5 * (a + b) + 0.5 * (b - a) * g[None, :]
    wx = 0.5 * (b - a) * wg[None, :]
    return xi, wx  # shape (npan, p)


def modal_coeffs(Omega_fn, rho, nphi):
    """om_n(rho), n=1..nphi, from midpoint samples on [0,pi/2]. rho: 1D array.
    Omega_fn(x, y) vectorized on Q1 points."""
    phij = (np.arange(nphi) + 0.5) * (np.pi / 2) / nphi
    X = rho[:, None] * np.cos(phij)[None, :]
    Y = rho[:, None] * np.sin(phij)[None, :]
    vals = Omega_fn(X, Y)
    c = dst(vals, type=2, axis=1) / nphi   # c[:, n-1] = om_n
    return c


def bs_modal(Omega_fn, xt, yt, nphi=256, p=16, xi_min=-25.0, xi_max=80.0, dxi=0.25,
             nmodes=None, second=False, chunk=4000, tail_alpha=None):
    """Velocity (and Psi, optionally DU) at targets (xt, yt) in the closed first quadrant
    (other quadrants by parity) from the odd-odd vorticity Omega_fn.
    Returns dict with Psi, U1, U2 and (if second) U1x, U1y, U2x, U2y.
    tail_alpha: if given (list of decay exponents a_j > 0), om_m(rho) for rho > R=e^{xi_max} is
    modelled as sum_j C_mj rho^{-a_j}, C fitted at len(a) radii in [R/e, R], and the tail
    int_R^inf (R/rho)^m rho om drho = sum_j C_mj R^{2-a_j}/(m+a_j-2) is added to S2(R)."""
    xt = np.asarray(xt, float).ravel(); yt = np.asarray(yt, float).ravel()
    rt = np.hypot(xt, yt); pht = np.arctan2(yt, xt)
    if nmodes is None:
        nmodes = nphi
    m = 2.0 * np.arange(1, nmodes + 1)
    # breakpoints: uniform grid in xi plus all target radii
    base = np.arange(xi_min, xi_max + 1e-12, dxi)
    with np.errstate(divide='ignore'):
        lt = np.log(rt[rt > 0])
    br = np.unique(np.concatenate([base, lt]))
    br = br[(br >= xi_min) & (br <= xi_max)]
    # drop near-duplicate breakpoints
    keep = np.concatenate([[True], np.diff(br) > 1e-13])
    br = br[keep]
    xi, wx = _panels(br, p)
    npan = xi.shape[0]
    rho = np.exp(xi)                      # (npan, p)
    wr = wx * rho                         # d rho = rho d xi
    Rb = np.exp(br)                       # breakpoints in rho
    # angular coefficients at all nodes (chunked)
    rf = rho.ravel()
    om = np.empty((rf.size, nmodes))
    for i0 in range(0, rf.size, chunk):
        c = modal_coeffs(Omega_fn, rf[i0:i0 + chunk], nphi)
        om[i0:i0 + chunk] = c[:, :nmodes]
    om = om.reshape(npan, p, nmodes)
    # inner sums S1(R_k) = int_0^{R_k} (rho/R_k)^m rho om drho, recursion over panels
    S1 = np.zeros((npan + 1, nmodes))
    for k in range(npan):
        fac = (Rb[k] / Rb[k + 1]) ** m
        J = np.einsum('q,qm->m', wr[k] * rho[k], om[k] * (rho[k][:, None] / Rb[k + 1]) ** m[None, :])
        S1[k + 1] = fac * S1[k] + J
    # outer sums S2(R_k) = int_{R_k}^inf (R_k/rho)^m rho om drho
    S2 = np.zeros((npan + 1, nmodes))
    if tail_alpha is not None:
        a = np.atleast_1d(np.asarray(tail_alpha, float))
        Rmax = Rb[-1]
        rfit = Rmax * np.exp(-np.linspace(0, 1, len(a)))
        Mf = rfit[:, None] ** (-a[None, :])                    # (nfit, na)
        omf = modal_coeffs(Omega_fn, rfit, nphi)[:, :nmodes]   # (nfit, nmodes)
        C = np.linalg.solve(Mf, omf) if len(a) > 1 else omf / Mf
        S2[npan] = np.sum(C * (Rmax ** (2 - a))[:, None] / (m[None, :] + a[:, None] - 2), axis=0)
    for k in range(npan - 1, -1, -1):
        fac = (Rb[k] / Rb[k + 1]) ** m
        J = np.einsum('q,qm->m', wr[k] * rho[k], om[k] * (Rb[k] / rho[k][:, None]) ** m[None, :])
        S2[k] = fac * S2[k + 1] + J
    # targets: each target radius is (up to 1 ulp) a breakpoint; use the breakpoint value
    lr = np.log(np.where(rt > 0, rt, 1.0))
    idx = np.searchsorted(br, lr)
    idx = np.clip(idx, 1, npan)
    left = np.abs(br[idx - 1] - lr) < np.abs(br[np.clip(idx, 0, npan)] - lr)
    idx = np.where(left, idx - 1, idx)
    if np.any(np.abs(br[idx] - lr)[rt > 0] > 1e-12):
        raise RuntimeError('target radius not a breakpoint (outside [xi_min, xi_max]?)')
    rt = np.where(rt > 0, Rb[idx], 0.0)
    out = {}
    s1 = S1[idx]; s2 = S2[idx]                       # (nt, nmodes)
    r = rt[:, None]
    with np.errstate(divide='ignore', invalid='ignore'):
        psi = (s1 + s2) / (2 * m[None, :])
        dpsi = 0.5 * (-s1 + s2) / r                   # psi_m'(r)
    sinm = np.sin(m[None, :] * pht[:, None]); cosm = np.cos(m[None, :] * pht[:, None])
    Psi = np.sum(psi * sinm, axis=1)
    Pr = np.sum(dpsi * sinm, axis=1)
    Pphi_over_r = np.sum(m[None, :] * psi / r * cosm, axis=1)
    c, s = np.cos(pht), np.sin(pht)
    Px = c * Pr - s * Pphi_over_r
    Py = s * Pr + c * Pphi_over_r
    out['Psi'] = Psi; out['U1'] = -Py; out['U2'] = Px
    if second:
        # om_m at target radii needed for psi'' = -psi'/r + m^2 psi/r^2 - om_m
        omt = modal_coeffs(Omega_fn, rt, nphi)[:, :nmodes]
        d2psi = -dpsi / r + (m[None, :] ** 2) * psi / r ** 2 - omt
        Prr = np.sum(d2psi * sinm, axis=1)
        Prp = np.sum(m[None, :] * dpsi * cosm, axis=1)          # d_r d_phi Psi
        Ppp = np.sum(-(m[None, :] ** 2) * psi * sinm, axis=1)   # d_phi^2 Psi
        Pp = np.sum(m[None, :] * psi * cosm, axis=1)            # d_phi Psi
        rr = rt
        # Cartesian second derivatives
        Pxx = c * c * Prr + s * s * (Pr / rr + Ppp / rr ** 2) - 2 * s * c * (Prp / rr - Pp / rr ** 2)
        Pyy = s * s * Prr + c * c * (Pr / rr + Ppp / rr ** 2) + 2 * s * c * (Prp / rr - Pp / rr ** 2)
        Pxy = s * c * (Prr - Pr / rr - Ppp / rr ** 2) + (c * c - s * s) * (Prp / rr - Pp / rr ** 2)
        out['Pxx'] = Pxx; out['Pyy'] = Pyy; out['Pxy'] = Pxy
        out['U1x'] = -Pxy; out['U1y'] = -Pyy; out['U2x'] = Pxx; out['U2y'] = Pxy
    return out


def strain_origin(Omega_fn, nphi=256, p=16, xi_min=-25.0, xi_max=80.0, dxi=0.25):
    """Psi_xy(0) = (1/2) int_0^inf om_1(rho)/rho drho (only the m=2 mode contributes)."""
    br = np.arange(xi_min, xi_max + 1e-12, dxi)
    xi, wx = _panels(br, p)
    rho = np.exp(xi).ravel()
    om1 = modal_coeffs(Omega_fn, rho, nphi)[:, 0]
    return 0.5 * np.sum(wx.ravel() * om1)        # d rho/rho = d xi
