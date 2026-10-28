"""Real regular solid harmonics P_q(y) = r^l Y_q(theta, phi) as Cartesian polynomials.

Conventions (fixed for the whole campaign):
  complex table  R_l^m(y) = r^l P_l^m(cos theta) e^{i m phi} / (l+m)!,  m >= 0, no Condon-Shortley phase,
                 R_l^{-m} = (-1)^m conj(R_l^m).
  real orthonormal spherical harmonics on S^2:
                 Y_{l,0}   = N_{l0} P_l(cos theta)
                 Y_{l,m,c} = sqrt(2) N_{lm} P_l^m(cos theta) cos(m phi)
                 Y_{l,m,s} = sqrt(2) N_{lm} P_l^m(cos theta) sin(m phi)
                 N_{lm} = sqrt((2l+1)/(4 pi) (l-m)!/(l+m)!).
  So P_{l,0} = N_{l0} l! R_l^0, P_{l,m,c} = sqrt2 N_{lm} (l+m)! Re R_l^m, P_{l,m,s} = sqrt2 N_{lm} (l+m)! Im R_l^m.

Recurrences (polynomial, stable, regular on the axis and at the origin):
  R_0^0 = 1,  R_m^m = (x+iy) R_{m-1}^{m-1} / (2m),  R_{m+1}^m = z R_m^m,
  R_l^m = [(2l-1) z R_{l-1}^m - rho R_{l-2}^m] / ((l-m)(l+m)).
Derivative ladders (verified in tests/test_solid_harmonics.py against sympy and finite differences):
  d/dz R_l^m = R_{l-1}^m,   (d/dx + i d/dy) R_l^m = -R_{l-1}^{m+1},   (d/dx - i d/dy) R_l^m = R_{l-1}^{m-1}.
"""
from __future__ import annotations
import math
import numpy as np
import torch

DT = torch.float64


def mode_list(L, m_parity="even", l_min=1):
    """Ordered list of real modes (l, m, t) with t in {0: cos/m=0, 1: sin}; cos/sin pairs adjacent.
    m_parity: 'even' (two-fold equivariance), 'all', 'odd'."""
    modes = []
    for l in range(l_min, L + 1):
        for m in range(0, l + 1):
            if m_parity == "even" and m % 2 == 1:
                continue
            if m_parity == "odd" and m % 2 == 0:
                continue
            modes.append((l, m, 0))
            if m > 0:
                modes.append((l, m, 1))
    return modes


def complex_table(y, L):
    """Return (Re, Im) tensors of shape (..., L+1, 2L+1) holding R_l^m(y) for m in [-L, L] (index m+L)."""
    x, yy, z = y[..., 0], y[..., 1], y[..., 2]
    rho = x * x + yy * yy + z * z
    shape = y.shape[:-1]
    Re = torch.zeros(shape + (L + 1, 2 * L + 1), dtype=y.dtype, device=y.device)
    Im = torch.zeros_like(Re)
    Re[..., 0, L] = 1.0
    for m in range(1, L + 1):
        # R_m^m = (x + i y) R_{m-1}^{m-1} / (2m)
        pr, pi_ = Re[..., m - 1, L + m - 1], Im[..., m - 1, L + m - 1]
        Re[..., m, L + m] = (x * pr - yy * pi_) / (2 * m)
        Im[..., m, L + m] = (x * pi_ + yy * pr) / (2 * m)
    for m in range(0, L):
        Re[..., m + 1, L + m] = z * Re[..., m, L + m]
        Im[..., m + 1, L + m] = z * Im[..., m, L + m]
    for m in range(0, L + 1):
        for l in range(m + 2, L + 1):
            c = 1.0 / ((l - m) * (l + m))
            Re[..., l, L + m] = ((2 * l - 1) * z * Re[..., l - 1, L + m] - rho * Re[..., l - 2, L + m]) * c
            Im[..., l, L + m] = ((2 * l - 1) * z * Im[..., l - 1, L + m] - rho * Im[..., l - 2, L + m]) * c
    # negative m: R_l^{-m} = (-1)^m conj(R_l^m)
    for m in range(1, L + 1):
        sgn = (-1) ** m
        Re[..., :, L - m] = sgn * Re[..., :, L + m]
        Im[..., :, L - m] = -sgn * Im[..., :, L + m]
    return Re, Im


def ladder_tables(Re, Im, L):
    """Given the complex table up to degree L, return derivative tables (dx, dy, dz) each a pair (Re, Im)
    of shape (..., L+1, 2L+1) with entry [l, m] = partial R_l^m (degree l-1 harmonics)."""
    def shifted(dl, dm):
        # returns tables S with S[l, m] = R_{l+dl}^{m+dm}, zero when out of range
        Sr = torch.zeros_like(Re)
        Si = torch.zeros_like(Im)
        for l in range(0, L + 1):
            lp = l + dl
            if lp < 0 or lp > L:
                continue
            for m in range(-l, l + 1):
                mp = m + dm
                if abs(mp) > lp:
                    continue
                Sr[..., l, L + m] = Re[..., lp, L + mp]
                Si[..., l, L + m] = Im[..., lp, L + mp]
        return Sr, Si
    Az = shifted(-1, 0)                      # d/dz R_l^m = R_{l-1}^m
    Pr, Pi = shifted(-1, 1)                  # (dx + i dy) R = -R_{l-1}^{m+1}
    Mr, Mi = shifted(-1, -1)                 # (dx - i dy) R =  R_{l-1}^{m-1}
    # dx R = [(dx+idy) + (dx-idy)]/2 R = (-P + M)/2 ; dy R = [(dx+idy) - (dx-idy)]/(2i) R = (-P - M)/(2i) = i (P + M)/2
    dxr, dxi = (-Pr + Mr) / 2, (-Pi + Mi) / 2
    dyr, dyi = -(Pi + Mi) / 2, (Pr + Mr) / 2
    return (dxr, dxi), (dyr, dyi), Az


def real_from_complex(Re, Im, modes, L):
    """Convert complex table to real mode values; returns tensor (..., Nq)."""
    out = []
    for (l, m, t) in modes:
        if l > L:
            out.append(torch.zeros_like(Re[..., 0, 0]))
            continue
        N = math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - m) / math.factorial(l + m))
        if m == 0:
            out.append(N * math.factorial(l) * Re[..., l, L])
        else:
            f = math.sqrt(2.0) * N * math.factorial(l + m)
            out.append(f * (Re[..., l, L + m] if t == 0 else Im[..., l, L + m]))
    return torch.stack(out, dim=-1)


def eval_solid(y, modes, L, nderiv=2):
    """Evaluate real solid harmonics P_q(y) and Cartesian derivatives at points y (..., 3).
    Returns A0 (..., Nq), A1 (3, ..., Nq), A2 (3, 3, ..., Nq) (up to nderiv)."""
    Re, Im = complex_table(y, L)
    A0 = real_from_complex(Re, Im, modes, L)
    if nderiv == 0:
        return A0, None, None
    d = ladder_tables(Re, Im, L)
    A1 = torch.stack([real_from_complex(dr, di, modes, L) for (dr, di) in d], dim=0)
    if nderiv == 1:
        return A0, A1, None
    A2 = []
    for i in range(3):
        dd = ladder_tables(d[i][0], d[i][1], L)
        A2.append(torch.stack([real_from_complex(dr, di, modes, L) for (dr, di) in dd], dim=0))
    A2 = torch.stack(A2, dim=0)  # (i, j, ..., Nq): d_i d_j P
    return A0, A1, A2


class AngularGrid:
    """Gauss-Legendre in theta times uniform in phi; weights integrate exactly spherical polynomials of
    degree <= 2*ntheta-1 (theta) and azimuthal orders < nphi."""
    def __init__(self, ntheta, nphi, device="cpu", phi0=0.0):
        xg, wg = np.polynomial.legendre.leggauss(ntheta)
        self.ntheta, self.nphi = ntheta, nphi
        ct = xg[::-1]  # cos theta descending => theta ascending
        wt = wg[::-1]
        phi = 2 * np.pi * np.arange(nphi) / nphi + phi0
        CT, PH = np.meshgrid(ct, phi, indexing="ij")
        WT = np.repeat(wt[:, None], nphi, axis=1) * (2 * np.pi / nphi)
        ST = np.sqrt(1 - CT ** 2)
        n = np.stack([ST * np.cos(PH), ST * np.sin(PH), CT], axis=-1).reshape(-1, 3)
        self.n = torch.tensor(n, dtype=DT, device=device)          # (Na, 3) unit vectors
        self.w = torch.tensor(WT.reshape(-1), dtype=DT, device=device)  # (Na,) weights, sum 4 pi
        self.theta = torch.tensor(np.arccos(CT).reshape(-1), dtype=DT, device=device)
        self.phi = torch.tensor(PH.reshape(-1), dtype=DT, device=device)
        self.Na = self.n.shape[0]

    def sph_basis(self):
        """Local spherical unit vectors e_r, e_theta, e_phi at the nodes, (Na, 3) each."""
        th, ph = self.theta, self.phi
        er = self.n
        eth = torch.stack([torch.cos(th) * torch.cos(ph), torch.cos(th) * torch.sin(ph), -torch.sin(th)], -1)
        eph = torch.stack([-torch.sin(ph), torch.cos(ph), torch.zeros_like(ph)], -1)
        return er, eth, eph


def angular_matrices(grid, modes, L, nderiv=2):
    """A0 (Na,Nq), A1 (3,Na,Nq), A2 (3,3,Na,Nq) of P_q and derivatives evaluated on unit vectors."""
    return eval_solid(grid.n, modes, L, nderiv)
