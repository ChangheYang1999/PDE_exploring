"""Spectral basis for axisymmetric scalar fields smooth in (r^2, z), in spherical (R, mu) coordinates.

Three element types on R in [0, inf):
  ball     : R in [0, R1].   psi_{n,k} = P_n(mu) rho^n T_k(2 rho^2 - 1), rho = R/R1, n + 2k <= D.
             This is exactly the space of axisymmetric Cartesian polynomials of degree <= D, so
             origin and axis regularity (functions of r^2 and z) is built in.
  shell    : R in [Ra, Rb].  psi_{n,k} = P_n(mu) T_k(x), x = 2 ln(R/Ra)/ln(Rb/Ra) - 1 (log map) or linear.
  exterior : R in [Rm, inf). psi_{n,j} = P_n(mu) (R/Rm)^(-e_j), e_j in an alpha-dependent exponent set.
             The fractional power-law decay is factored analytically; nothing is compactified.

Every element provides collocation nodes (R, mu), quadrature weights, and dense matrices
B[(i, j)] of shape (n_nodes, n_basis) holding d^i/dR^i d^j/dmu^j of every basis function,
for all i + j <= 3.  All arrays are float64 numpy; the solver moves them to torch.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import numpy as np
from numpy.polynomial import chebyshev as Cheb, legendre as Leg

DERIV_KEYS = [(i, j) for i in range(4) for j in range(4) if i + j <= 3]


# ----------------------------------------------------------------------------- 1D families

def legendre_derivs(mu: np.ndarray, nmax: int, maxder: int = 3) -> List[np.ndarray]:
    """Return [P^{(m)}_n(mu)] for m = 0..maxder as arrays (len(mu), nmax+1)."""
    out = []
    eye = np.eye(nmax + 1)
    for m in range(maxder + 1):
        cols = []
        for n in range(nmax + 1):
            c = Leg.legder(eye[:, n], m) if m > 0 else eye[:, n]
            cols.append(Leg.legval(mu, c))
        out.append(np.array(cols).T)
    return out


def cheb_derivs_x(x: np.ndarray, kmax: int, maxder: int = 3) -> List[np.ndarray]:
    """Return [T^{(m)}_k(x)] for m = 0..maxder as arrays (len(x), kmax+1)."""
    out = []
    eye = np.eye(kmax + 1)
    for m in range(maxder + 1):
        cols = []
        for k in range(kmax + 1):
            c = Cheb.chebder(eye[:, k], m) if m > 0 else eye[:, k]
            cols.append(Cheb.chebval(x, c))
        out.append(np.array(cols).T)
    return out


def jacobi_values(x: np.ndarray, kmax: int, a: float, b: float) -> np.ndarray:
    """P_k^{(a,b)}(x), k = 0..kmax, by the three-term recurrence; returns (len(x), kmax+1)."""
    x = np.asarray(x, dtype=np.float64)
    P = np.zeros((x.size, kmax + 1))
    P[:, 0] = 1.0
    if kmax >= 1:
        P[:, 1] = 0.5 * ((a + b + 2) * x + (a - b))
    for k in range(1, kmax):
        c = 2 * k + a + b
        A1 = 2 * (k + 1) * (k + a + b + 1) * c
        B1 = (c + 1) * ((c + 2) * c * x + a * a - b * b)
        C1 = 2 * (k + a) * (k + b) * (c + 2)
        P[:, k + 1] = (B1 * P[:, k] - C1 * P[:, k - 1]) / A1
    return P


def jacobi_derivs_x(x: np.ndarray, kmax: int, a: float, b: float, maxder: int = 3) -> List[np.ndarray]:
    """[d^m/dx^m P_k^{(a,b)}(x)] for m = 0..maxder as arrays (len(x), kmax+1), using
    d^m/dx^m P_k^{(a,b)} = Gamma(k+a+b+1+m)/(2^m Gamma(k+a+b+1)) P_{k-m}^{(a+m,b+m)}  (zero for k < m)."""
    x = np.asarray(x, dtype=np.float64)
    out = []
    for m in range(maxder + 1):
        D = np.zeros((x.size, kmax + 1))
        if kmax - m >= 0:
            Pm = jacobi_values(x, kmax - m, a + m, b + m)
            for k in range(m, kmax + 1):
                fac = 1.0
                for j in range(m):
                    fac *= (k + a + b + 1 + j) / 2.0
                D[:, k] = fac * Pm[:, k - m]
        out.append(D)
    return out


def _compose_derivs(T: List[np.ndarray], x1, x2, x3) -> List[np.ndarray]:
    """Given T^{(m)}(x) and x(R) derivatives x1, x2, x3, return d^m/dR^m T(x(R)) for m=0..3 (Faa di Bruno)."""
    T0, T1, T2, T3 = T
    x1 = x1[:, None]; x2 = x2[:, None]; x3 = x3[:, None]
    d0 = T0
    d1 = T1 * x1
    d2 = T2 * x1**2 + T1 * x2
    d3 = T3 * x1**3 + 3 * T2 * x1 * x2 + T1 * x3
    return [d0, d1, d2, d3]


def _product_derivs(f: List[np.ndarray], g: List[np.ndarray]) -> List[np.ndarray]:
    """Leibniz rule up to third order for products of two lists of derivative arrays."""
    f0, f1, f2, f3 = f
    g0, g1, g2, g3 = g
    return [f0 * g0,
            f1 * g0 + f0 * g1,
            f2 * g0 + 2 * f1 * g1 + f0 * g2,
            f3 * g0 + 3 * f2 * g1 + 3 * f1 * g2 + f0 * g3]


def power_derivs(R: np.ndarray, p: float) -> List[np.ndarray]:
    """d^m/dR^m R^p for m=0..3, with exact zeros when p is a non-negative integer < m."""
    R = np.asarray(R, dtype=np.float64)
    out = []
    coef = 1.0
    for m in range(4):
        e = p - m
        if coef == 0.0:
            out.append(np.zeros_like(R))
        else:
            out.append(coef * np.power(R, e))
        coef *= (p - m)
        if abs(coef) < 1e-300:
            coef = 0.0
    return out


# ----------------------------------------------------------------------------- nodes

def gauss_legendre(n: int, a: float = -1.0, b: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    x, w = np.polynomial.legendre.leggauss(n)
    xm = 0.5 * (b - a) * x + 0.5 * (b + a)
    return xm, 0.5 * (b - a) * w


# ----------------------------------------------------------------------------- elements

@dataclass
class Element:
    kind: str
    Rlo: float
    Rhi: float                      # inf for exterior
    nmax: int                       # max Legendre degree in mu
    params: dict
    R: np.ndarray = field(repr=False)        # nodes, shape (n_nodes,)
    mu: np.ndarray = field(repr=False)
    wR: np.ndarray = field(repr=False)       # radial quadrature weight (in R)
    wmu: np.ndarray = field(repr=False)      # angular quadrature weight (in mu)
    B: Dict[Tuple[int, int], np.ndarray] = field(repr=False)   # derivative matrices
    labels: List[Tuple] = field(repr=False)                     # (n, k) or (n, e) per basis column
    nbasis: int = 0

    def eval_at(self, R: np.ndarray, mu: np.ndarray) -> Dict[Tuple[int, int], np.ndarray]:
        """Evaluate the element's basis derivatives at arbitrary points (holdout grids)."""
        return build_B(self.kind, self.Rlo, self.Rhi, self.nmax, self.params, np.asarray(R, float), np.asarray(mu, float))[0]


def _ball_radial(R, R1, nmax, D, radial="cheb"):
    """Radial parts rho^n Q_k(2rho^2-1) with n+2k<=D; returns dict n -> (list of 4 arrays (len R, Kn+1)).
    radial = "cheb": Q_k = T_k (Chebyshev; the shift-1 choice, nearly dependent at high n: scaled Jacobian condition 2e10);
    radial = "jacobi": Q_k = P_k^{(0, n+1/2)} (3D Zernike radial polynomials, orthogonal on the unit ball with weight rho^2 drho;
    well conditioned).  Both span the same polynomial space; the Jacobian condition is the only difference."""
    rho = R / R1
    x = 2 * rho**2 - 1
    x1 = 4 * rho / R1
    x2 = np.full_like(R, 4 / R1**2)
    x3 = np.zeros_like(R)
    out = {}
    for n in range(nmax + 1):
        Kn = (D - n) // 2
        if Kn < 0:
            continue
        T = cheb_derivs_x(x, Kn) if radial == "cheb" else jacobi_derivs_x(x, Kn, 0.0, n + 0.5)
        Tc = _compose_derivs(T, x1, x2, x3)
        rp = [a[:, None] / R1**n for a in power_derivs(R, float(n))]
        rp = [np.broadcast_to(a, Tc[0].shape) for a in rp]
        out[n] = _product_derivs(rp, Tc)
    return out


_LEG_CACHE = {}


def legendre_derivs_cached(mu, nmax, maxder=3):
    """legendre_derivs with a small cache keyed by the node array content (free-c_l runs rebuild the exterior basis at the same
    nodes thousands of times; the Legendre part does not depend on c_l)."""
    key = (hash(np.asarray(mu, dtype=np.float64).tobytes()), int(nmax), int(maxder))
    v = _LEG_CACHE.get(key)
    if v is None:
        v = legendre_derivs(mu, nmax, maxder)
        if len(_LEG_CACHE) > 64:
            _LEG_CACHE.clear()
        _LEG_CACHE[key] = v
    return v


def build_B(kind, Rlo, Rhi, nmax, params, R, mu):
    """Return (B dict, labels) for arbitrary points R, mu (same length)."""
    Pm = legendre_derivs_cached(mu, nmax)      # list over mu-derivative order
    cols: Dict[Tuple[int, int], list] = {k: [] for k in DERIV_KEYS}
    labels = []
    if kind == "ball":
        D = params["D"]
        rad = _ball_radial(R, Rlo if Rlo > 0 else params.get("R1", Rhi), nmax, D, params.get("radial", "cheb"))
        for n in range(nmax + 1):
            if n not in rad:
                continue
            fr = rad[n]
            Kn = fr[0].shape[1]
            for k in range(Kn):
                for (i, j) in DERIV_KEYS:
                    cols[(i, j)].append(fr[i][:, k] * Pm[j][:, n])
                labels.append((n, k))
    elif kind == "shell":
        K = params["K"]
        mapping = params.get("map", "log")
        if mapping == "log":
            L = math.log(Rhi / Rlo)
            x = 2 * np.log(R / Rlo) / L - 1
            x1 = 2 / (R * L)
            x2 = -x1 / R
            x3 = 2 * x1 / R**2
        else:
            x = 2 * (R - Rlo) / (Rhi - Rlo) - 1
            x1 = np.full_like(R, 2 / (Rhi - Rlo))
            x2 = np.zeros_like(R)
            x3 = np.zeros_like(R)
        T = cheb_derivs_x(x, K)
        Tc = _compose_derivs(T, x1, x2, x3)
        for n in range(nmax + 1):
            for k in range(K + 1):
                for (i, j) in DERIV_KEYS:
                    cols[(i, j)].append(Tc[i][:, k] * Pm[j][:, n])
                labels.append((n, k))
    elif kind == "exterior":
        exps = params["exponents"]
        Rm = Rlo
        for n in range(nmax + 1):
            for e in exps:
                pw = power_derivs(R / Rm, -e)
                pw = [a / Rm**m for m, a in enumerate(pw)]
                for (i, j) in DERIV_KEYS:
                    cols[(i, j)].append(pw[i] * Pm[j][:, n])
                labels.append((n, float(e)))
    else:
        raise ValueError(kind)
    B = {k: np.array(v).T.copy() for k, v in cols.items()}
    return B, labels


def make_element(kind, Rlo, Rhi, nmax, params, nR, nmu=None, pole_pad=0) -> Element:
    """Create an element with tensor collocation nodes: nR radial Gauss nodes x nmu angular Gauss nodes."""
    nmu = nmu or (nmax + 1 + pole_pad)
    mu1, wmu1 = gauss_legendre(nmu)
    if kind == "ball":
        # Gauss nodes in x = 2 rho^2 - 1 (so rho^2 is sampled like a Jacobi weight), rho in (0,1)
        x, wx = gauss_legendre(nR)
        rho = np.sqrt(0.5 * (x + 1))
        R1 = Rhi
        R = R1 * rho
        wR = wx * R1 / (4 * rho)      # dR = R1 d rho, d rho = dx/(4 rho)
        params = dict(params, R1=R1)
    elif kind == "shell":
        mapping = params.get("map", "log")
        x, wx = gauss_legendre(nR)
        if mapping == "log":
            L = math.log(Rhi / Rlo)
            R = Rlo * np.exp(0.5 * (x + 1) * L)
            wR = wx * R * L / 2
        else:
            R = Rlo + 0.5 * (x + 1) * (Rhi - Rlo)
            wR = wx * (Rhi - Rlo) / 2
    elif kind == "exterior":
        # nodes log-spaced in t = ln(R/Rm) in (0, Tmax]: Gauss nodes in t; R = Rm e^t; dR = R dt.
        # Tmax = ln(1e6) by default so that every power R^-e dominates on some part of the node set
        # (a cancelling combination of powers cannot mimic a non-decaying function on all nodes).
        Tmax = params.get("Tmax", math.log(1e6))
        t, wt = gauss_legendre(nR, 0.0, Tmax)
        R = Rlo * np.exp(t)
        wR = wt * R
    else:
        raise ValueError(kind)
    RR, MM = np.meshgrid(R, mu1, indexing="ij")
    WR, WM = np.meshgrid(wR, wmu1, indexing="ij")
    Rf, Mf, WRf, WMf = RR.ravel(), MM.ravel(), WR.ravel(), WM.ravel()
    B, labels = build_B(kind, Rlo, Rhi, nmax, params, Rf, Mf)
    return Element(kind=kind, Rlo=Rlo, Rhi=Rhi, nmax=nmax, params=params, R=Rf, mu=Mf,
                   wR=WRf, wmu=WMf, B=B, labels=labels, nbasis=len(labels))


# ----------------------------------------------------------------------------- exponent set

def exterior_exponents(alpha: float, emax: float, field_kind: str, merge_tol: float = 0.03) -> List[float]:
    """Exponents e for the far-field ansatz f = sum_e R^{-e} F_e(mu), up to e <= emax.

    phi: generated by {alpha} U {3,4,5,...} (3D potential multipoles R^{-(l+2)}, l>=1) under
         (a, b) -> a + b + 1  (quadratic nonlinearity of the eta equation, phi gains one power of R
         relative to velocity x gradient).
    q:   leading alpha + 1; nonlinear corrections a_phi + b_q + 1.
    Exponents closer than merge_tol are merged (near-resonant pairs; see FAR_FIELD notes).
    """
    base_phi = {alpha} | {float(k) for k in range(3, int(math.floor(emax)) + 1)}
    phi_set = set(base_phi)
    changed = True
    while changed:
        changed = False
        for a in list(phi_set):
            for b in list(phi_set):
                c = a + b + 1
                if c <= emax + 1e-12 and all(abs(c - x) > 1e-12 for x in phi_set):
                    phi_set.add(c)
                    changed = True
    if field_kind == "phi":
        exps = phi_set
    elif field_kind == "q":
        q_set = {alpha + 1}
        changed = True
        while changed:
            changed = False
            for a in list(phi_set):
                for b in list(q_set):
                    c = a + b + 1
                    if c <= emax + 1e-12 and all(abs(c - x) > 1e-12 for x in q_set):
                        q_set.add(c)
                        changed = True
        exps = q_set
    else:
        raise ValueError(field_kind)
    exps = sorted(exps)
    merged = []
    for e in exps:
        if merged and abs(e - merged[-1]) < merge_tol:
            continue
        merged.append(e)
    return merged
