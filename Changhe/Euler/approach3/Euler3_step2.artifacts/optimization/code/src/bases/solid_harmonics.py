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


# D6FP (2026-10-28): the tables are evaluated in double-double arithmetic (solid_harmonics_dd.eval_solid_dd) and rounded once, which reproduces
# the verifier's 70-digit reference tables exactly (validation/check_angular_dd.py: 4496388 of 4496388 entries at the nest6 training nodes),
# whereas the float64 ladder recurrences below lose up to 6e-10 of relative accuracy in small derivative entries (verifier V020, SPEC G5 (c)).
# The float64 path is kept for point sets larger than DD_MAX_POINTS (scattered diagnostic points of the ray-integral check) and as the
# reference implementation (eval_solid_fp64).
DD_TABLES = True
DD_MAX_POINTS = 40000
_TABLE_CACHE = {}          # (sha256 of the point coordinates, modes, L, nderiv, device) -> tables; the same grids recur in every holdout / pressure build
_TABLE_CACHE_MAX = 64
# D6FP: explicit path dispatch (lead note 2026-10-28T22:35Z item 1): production calls use path="dd" (double-double, no size limit, raises never);
# path="auto" uses double-double up to DD_MAX_POINTS points and float64 beyond (diagnostic scattered point sets); path="fp64" requests the frozen
# float64 tables by name. Every call is counted per path with its point count and caller (PATH_LOG; the worker records the summary).
PATH_LOG = []
PATH_COUNTS = {"dd": 0, "fp64": 0}


def _log_path(path, n, L, nderiv):
    import sys
    try:                                                         # sys._getframe: no source reading, no tensor access (inspect.stack() raised inside functorch transforms, gates_full_D6 23:4xZ)
        fr = sys._getframe(2)
        caller = f"{fr.f_code.co_name} ({fr.f_code.co_filename.split('/')[-1]}:{fr.f_lineno})"
    except Exception:
        caller = "?"
    PATH_COUNTS[path] = PATH_COUNTS.get(path, 0) + 1
    if len(PATH_LOG) < 2000:
        PATH_LOG.append(dict(path=path, points=int(n), L=int(L), nderiv=int(nderiv), caller=caller))


def eval_solid(y, modes, L, nderiv=2, path="auto"):
    """Evaluate real solid harmonics P_q(y) and Cartesian derivatives at points y (..., 3).
    Returns A0 (..., Nq), A1 (3, ..., Nq), A2 (3, 3, ..., Nq) (up to nderiv). path: "dd" (production: double-double for any size),
    "fp64" (frozen float64, diagnostics by name), "auto" (double-double up to DD_MAX_POINTS points, float64 beyond)."""
    n = y.shape[:-1].numel()
    use_dd = DD_TABLES and (path == "dd" or (path == "auto" and n <= DD_MAX_POINTS))
    if path == "fp64":
        use_dd = False
    _log_path("dd" if use_dd else "fp64", n, L, nderiv)
    if use_dd:
        import hashlib
        from .solid_harmonics_dd import eval_solid_dd
        key = None
        if not y.requires_grad:
            try:                                                                # functorch duals/batched tensors have no data pointer: no caching for them (gates_full_D6/C5 crashed here 23:4xZ, 00:2xZ)
                key = (hashlib.sha256(y.detach().cpu().numpy().tobytes()).hexdigest(), tuple(modes), int(L), int(nderiv), str(y.device))
            except Exception:
                key = None
            hit = _TABLE_CACHE.get(key) if key is not None else None
            if hit is not None:
                return tuple(None if t is None else t.clone() for t in hit)      # clones: cached tensors are never shared with callers (lead 22:49Z item 3)
        out = eval_solid_dd(y, modes, L, nderiv)
        if key is not None:
            if len(_TABLE_CACHE) >= _TABLE_CACHE_MAX:
                _TABLE_CACHE.pop(next(iter(_TABLE_CACHE)))
            _TABLE_CACHE[key] = out
        return out
    return eval_solid_fp64(y, modes, L, nderiv)


def path_summary():
    """counts per path and the distinct (caller, points, L, nderiv, path) combinations seen in this process."""
    seen = {}
    for e in PATH_LOG:
        k = (e["caller"], e["points"], e["L"], e["nderiv"], e["path"]); seen[k] = seen.get(k, 0) + 1
    return dict(counts=dict(PATH_COUNTS), sites=[dict(caller=k[0], points=k[1], L=k[2], nderiv=k[3], path=k[4], calls=v) for k, v in sorted(seen.items(), key=lambda kv: -kv[1])])


def eval_solid_fp64(y, modes, L, nderiv=2):
    """The frozen float64 evaluation (reference implementation; used for very large scattered point sets)."""
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
    """A0 (Na,Nq), A1 (3,Na,Nq), A2 (3,3,Na,Nq) of P_q and derivatives evaluated on unit vectors (production: double-double path)."""
    return eval_solid(grid.n, modes, L, nderiv, path="dd")
