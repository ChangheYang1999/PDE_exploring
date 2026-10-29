"""Diverse initializations (PROMPT.md section 10): smooth cores of different shapes and scales, different swirl
distributions, mixed poloidal/swirl far-field angular coefficients, symmetric and asymmetric z-dependence,
random spectral coefficients with controlled decay, and the S1-structured seeds of the lead's note 7
(an axis stagnation point of W_m with phi_z = 1/2 and q = q0 there).  Every family is seeded and recorded
in the job config.

Generic families: inner elements are least-squares fits of an explicit smooth field; the exterior leading
coefficients (exponent alpha for phi, alpha+1 for q) are set to a chosen angular profile and the leading tail
is scaled so that the gauge integral is one (initial guess only, not a dilation).
S1 families: phi, q are given analytically on the whole half-plane with their exact R^-alpha tail (A(mu), B(mu)
of the lead's formulas); the whole seed is dilated (L) so that the gauge integral is one, then fitted to all
elements including the exterior leading coefficients.  The S1 condition and the source position z0 are
starting values only; nothing constrains the solve unless cfg.s1_constraint is set.
"""
from __future__ import annotations

import json
import math
import os

import numpy as np
import torch

from . import basis
from .problem import Problem

FAMILIES = ["gauss_core", "ring_core", "random_spectral", "swirl_dominant", "poloidal_dominant", "asym_dipole", "flat_core",
            "s1_sym_v2", "s1_shift_v2", "ring_t2", "pair_t3", "t1budget"]

_S1_PARAMS = None


def s1_params(c, q0):
    """Parameters of the lead's s1_sym_v2 seed (configs/s1_sym_v2_params_from_lead.json), nearest tabulated c_l."""
    global _S1_PARAMS
    if _S1_PARAMS is None:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, "..", "..", "configs", "s1_sym_v2_params_from_lead.json")
        _S1_PARAMS = json.load(open(path))
    d = min(_S1_PARAMS, key=lambda t: abs(t["c"] - c))
    al = (1 - c) / c
    k, n, d1, eps = (3 + al) / 2, (1 + al) / 2, 1 + c, 0.2
    Rr = -(1 - eps) * k - eps * n
    Z = -4 * (c - 0.5) * d1 * Rr / (d1 ** 2 + q0 ** 2)          # S1 curvature relation at the source
    beta = k + (Z + eps * n) / (1 - eps)
    return dict(alpha=al, k=k, n=n, nu=d["nu"], lam=d["lam"], gam=d["gam"], eps=eps, beta=beta, c_table=d["c"])


def s1_sym_v2(r, z, c, q0, L=1.0):
    """Source at the origin: phi odd in z, q even, phi_z(0,0) = 1/2, q(0,0) = q0 (lead's formulas, note 7)."""
    p = s1_params(c, q0)
    zeta, rho2 = z / L, (r ** 2 + z ** 2) / L ** 2
    f = (1 + p["nu"]) * (1 + p["gam"] * zeta ** 2) * (1 + rho2) ** (-p["k"]) - p["nu"] * (1 + rho2 / p["lam"] ** 2) ** (-p["n"])
    phi = 0.5 * z * f
    q = q0 * ((1 - p["eps"]) * (1 + p["beta"] * zeta ** 2) * (1 + rho2) ** (-p["k"]) + p["eps"] * (1 + rho2) ** (-p["n"]))
    return phi, q


def s1_shift_v2(r, z, c, q0, z0, L=1.0):
    """Same structure centred at (0, z0), plus -c z0/2 times an envelope so that W_z(0, z0) = 0."""
    p = s1_params(c, q0)
    phi, q = s1_sym_v2(r, z - z0, c, q0, L)
    phi = phi - 0.5 * c * z0 * (1 + (r ** 2 + (z - z0) ** 2) / L ** 2) ** (-p["n"])
    return phi, q


def s1_tail_AB(c, q0, z0, L, nmax):
    """Legendre coefficients of the leading tail A(mu), B(mu) of the S1 seeds (phi ~ R^-alpha A, q ~ R^-alpha-1 B).
    A = (L^(1+alpha)/2)[(1+nu) gam mu^3 - nu lam^(1+alpha) mu] - (c z0/2) L^(1+alpha) (shift term, a 5D-monopole-like
    R^-(1+alpha) contribution that is subleading: not part of A), B = q0 L^(1+alpha)[(1-eps) beta mu^2 + eps]."""
    p = s1_params(c, q0)
    al = p["alpha"]
    mu, w = basis.gauss_legendre(2 * nmax + 8)
    A = (L ** (1 + al) / 2) * ((1 + p["nu"]) * p["gam"] * mu ** 3 - p["nu"] * p["lam"] ** (1 + al) * mu)
    B = q0 * L ** (1 + al) * ((1 - p["eps"]) * p["beta"] * mu ** 2 + p["eps"])
    P = basis.legendre_derivs(mu, nmax, 0)[0]
    norm = 2.0 / (2 * np.arange(nmax + 1) + 1)
    a = (P * w[:, None]).T @ A / norm
    b = (P * w[:, None]).T @ B / norm
    return a, b


def _legendre_profile(rng, nmax, ncoef, amp, even_only=False, odd_only=False):
    c = np.zeros(nmax + 1)
    k = min(ncoef, nmax + 1)
    c[:k] = amp * rng.normal(size=k) * np.exp(-0.4 * np.arange(k))
    if even_only:
        c[1::2] = 0
    if odd_only:
        c[0::2] = 0
    return c


def _set_leading_tail(prob, x, A, Bc):
    i = prob.nel - 1
    Rm = prob.Rm
    alpha = prob.alpha
    for j, idx in enumerate(prob.ext_lead_idx_phi):
        x[prob.off_phi[i] + idx] = A[prob.ext_lead_n_phi[j]] * Rm ** (-alpha)
    for j, idx in enumerate(prob.ext_lead_idx_q):
        x[prob.off_q[i] + idx] = Bc[prob.ext_lead_n_q[j]] * Rm ** (-(alpha + 1))
    return x


def make_init(prob: Problem, family: str, seed: int, scale_core: float = 1.0, amp_core: float = 1.0,
              swirl_amp: float = 1.0, tail_ratio: float = 1.0, extra: dict | None = None) -> torch.Tensor:
    rng = np.random.default_rng(seed)
    alpha = prob.alpha
    nmax = prob.cfg.nmax
    extra = extra or {}
    cl = prob.cl
    if family in ("s1_sym_v2", "s1_shift_v2"):
        return make_s1_init(prob, family, seed, extra)
    if family == "ring_t2":
        return make_t2_init(prob, seed, extra)
    if family == "pair_t3":
        return make_t3_init(prob, seed, extra)
    if family == "t1budget":
        return make_t1budget_init(prob, seed, extra)
    L = scale_core
    a1, a2, a3 = rng.normal(size=3) * 0.5
    b1, b2 = rng.normal(size=2) * 0.5

    def core_env(R):
        return np.exp(-(R / L) ** 2)

    if family == "gauss_core":
        fphi = lambda R, mu: amp_core * core_env(R) * (1 + a1 * R * mu + a2 * (R * mu) ** 2 / L**2)
        fq = lambda R, mu: swirl_amp * core_env(R) * (1 + b1 * R * mu / L)
    elif family == "ring_core":
        fphi = lambda R, mu: amp_core * core_env(R) * (R**2 * (1 - mu**2) / L**2) * (1 + a1 * R * mu / L)
        fq = lambda R, mu: swirl_amp * core_env(R) * (1 + 0.5 * R**2 * (1 - mu**2) / L**2 + b1 * R * mu / L)
    elif family == "flat_core":
        fphi = lambda R, mu: amp_core / (1 + (R / L) ** 2) ** 2 * (1 + a1 * R * mu / L)
        fq = lambda R, mu: swirl_amp / (1 + (R / L) ** 2) ** 2 * (1 + b1 * R * mu / L + b2 * (R * mu / L) ** 2)
    elif family == "asym_dipole":
        fphi = lambda R, mu: amp_core * core_env(R) * (R * mu / L + 0.3 * a1)
        fq = lambda R, mu: swirl_amp * core_env(R) * (1 + b1 * R * mu / L) * (0.5 + 0.5 * np.tanh(R * mu / L))
    elif family == "swirl_dominant":
        fphi = lambda R, mu: 0.2 * amp_core * core_env(R) * (1 + a1 * R * mu / L)
        fq = lambda R, mu: swirl_amp * core_env(R) * (1 + b1 * R * mu / L)
    elif family == "poloidal_dominant":
        fphi = lambda R, mu: amp_core * core_env(R) * (1 + a1 * R * mu / L + a3 * (R / L) ** 2 * (1 - mu**2))
        fq = lambda R, mu: 0.2 * swirl_amp * core_env(R) * (1 + b1 * R * mu / L)
    elif family == "random_spectral":
        fphi = fq = None
    else:
        raise ValueError(family)

    if fphi is not None:
        x = prob.fit_function(fphi, fq)
    else:
        x = torch.zeros(prob.nx, dtype=torch.float64)
        for i, e in enumerate(prob.elements):
            if e.kind == "exterior":
                continue
            lab = np.array([l[0] for l in e.labels], float)
            kk = np.array([l[1] for l in e.labels], float)
            dec = np.exp(-0.25 * (lab + 2 * kk))
            x[prob.off_phi[i]:prob.off_phi[i + 1]] = torch.tensor(amp_core * rng.normal(size=e.nbasis) * dec)
            x[prob.off_q[i]:prob.off_q[i + 1]] = torch.tensor(swirl_amp * rng.normal(size=e.nbasis) * dec)
        x = x.to(prob.device)
    # exterior: zero everything, then set leading coefficients to a random angular profile
    x = x.detach().cpu().clone()
    i = prob.nel - 1
    x[prob.off_phi[i]:prob.off_phi[i + 1]] = 0.0
    x[prob.off_q[i]:prob.off_q[i + 1]] = 0.0
    kind = extra.get("tail", rng.choice(["mixed", "poloidal", "swirl", "even", "odd"]))
    ncoef = int(extra.get("tail_ncoef", 4))
    if kind == "poloidal":
        A = _legendre_profile(rng, nmax, ncoef, 1.0); Bc = _legendre_profile(rng, nmax, ncoef, 0.15)
    elif kind == "swirl":
        A = _legendre_profile(rng, nmax, ncoef, 0.15); Bc = _legendre_profile(rng, nmax, ncoef, 1.0)
    elif kind == "even":
        A = _legendre_profile(rng, nmax, ncoef, 1.0, even_only=True); Bc = _legendre_profile(rng, nmax, ncoef, 1.0, even_only=True)
    elif kind == "odd":
        A = _legendre_profile(rng, nmax, ncoef, 1.0, odd_only=True); Bc = _legendre_profile(rng, nmax, ncoef, 1.0, even_only=True)
    else:
        A = _legendre_profile(rng, nmax, ncoef, 1.0); Bc = _legendre_profile(rng, nmax, ncoef, 1.0)
    x = _set_leading_tail(prob, x, A, Bc)
    # scale the leading tail to unit gauge integral (initial guess only; not a dilation)
    xg = x.to(prob.device)
    cphi, cq, _ = prob.split(xg)
    gI = float(prob.gauge_integral(cphi[-1], cq[-1], alpha))
    if gI > 0:
        s = (tail_ratio / gI) ** 0.5
        for idx in prob.ext_lead_idx_phi:
            xg[prob.off_phi[i] + idx] *= s
        for idx in prob.ext_lead_idx_q:
            xg[prob.off_q[i] + idx] *= s
    if prob.ix_cl is not None:
        xg[prob.ix_cl] = prob.cl
    if prob.ix_z0 is not None:
        xg[prob.ix_z0] = float(extra.get("z0", prob.cfg.z0_init))
    return _amp_normalize(prob, xg)


def _amp_normalize(prob, x):
    """With amp_param: divide the q coefficients by q(0, z0) so that qhat(0, z0) = 1 and store A = |q(0, z0)| (sign into qhat)."""
    if prob.ix_a is None:
        return x
    z0 = prob.z0_of(x)
    qv = float(prob.eval_field(x, "q", np.array([max(abs(z0), 1e-12)]), np.array([1.0 if z0 >= 0 else -1.0]))[0])
    if abs(qv) < 1e-8:
        qv = 1.0
    x[prob.nphi:prob.nphi + prob.nq] = x[prob.nphi:prob.nphi + prob.nq] / qv
    x[prob.ix_a] = math.log(abs(qv))
    if qv < 0:
        x[prob.nphi:prob.nphi + prob.nq] = -x[prob.nphi:prob.nphi + prob.nq]   # qhat(0,z0) = 1 requires the sign in A... keep qhat positive at the source
    return x


def make_s1_init(prob: Problem, family: str, seed: int, extra: dict) -> torch.Tensor:
    """S1 seeds: q0 = extra['q0'] (default 1), z0 = extra['z0'] (default 0 for s1_sym_v2, 0.5 for s1_shift_v2),
    optional extra['perturb'] relative random perturbation of the inner coefficients (seeded).
    The seed is dilated so that the gauge integral of its exact tail is one."""
    cl = prob.cl
    alpha = prob.alpha
    nmax = prob.cfg.nmax
    q0 = float(extra.get("q0", 1.0))
    z0 = float(extra.get("z0", 0.0 if family == "s1_sym_v2" else 0.5))
    if family == "s1_sym_v2":
        z0 = 0.0
    # gauge integral of the L = 1 tail; dilation by L multiplies it by L^(2(1+alpha))
    a1, b1 = s1_tail_AB(cl, q0, z0, 1.0, nmax)
    dev = prob.device
    cphi_ext = torch.zeros(prob.nb_phi[-1], dtype=torch.float64, device=dev)
    cq_ext = torch.zeros(prob.nb_q[-1], dtype=torch.float64, device=dev)
    Rm = prob.Rm
    for j, idx in enumerate(prob.ext_lead_idx_phi):
        cphi_ext[idx] = a1[prob.ext_lead_n_phi[j]] * Rm ** (-alpha)
    for j, idx in enumerate(prob.ext_lead_idx_q):
        cq_ext[idx] = b1[prob.ext_lead_n_q[j]] * Rm ** (-(alpha + 1))
    gI = float(prob.gauge_integral(cphi_ext, cq_ext, alpha))
    if "L" in extra:                       # absolute core scale (working gauge set from the seed by the worker)
        L = float(extra["L"])
    else:
        L = gI ** (-1.0 / (2 * (1 + alpha))) if gI > 0 else 1.0
        L *= float(extra.get("L_factor", 1.0))
    z0L = z0 * L

    def fphi(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return (s1_sym_v2(r, z, cl, q0, L) if family == "s1_sym_v2" else s1_shift_v2(r, z, cl, q0, z0L, L))[0]

    def fq(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return (s1_sym_v2(r, z, cl, q0, L) if family == "s1_sym_v2" else s1_shift_v2(r, z, cl, q0, z0L, L))[1]

    x = prob.fit_function(fphi, fq).detach().cpu().clone()
    # exterior: least-squares fit of the full seed onto all exterior columns (leading + corrections), weighted so
    # that every node counts relative to the local size of the seed
    i = prob.nel - 1
    e = prob.elements[i]
    for (cols, off, f) in ((prob.cols_phi[i], prob.off_phi, fphi), (prob.cols_q[i], prob.off_q, fq)):
        A0 = e.B[(0, 0)][:, cols]
        y = f(e.R, e.mu)
        wts = 1.0 / (np.abs(y).max(initial=0) * 1e-3 + np.abs(y) + 1e-300)
        cs = np.max(np.abs(A0 * wts[:, None]), axis=0); cs[cs == 0] = 1.0
        c, *_ = np.linalg.lstsq((A0 * wts[:, None]) / cs, y * wts, rcond=None)
        x[off[i]:off[i + 1]] = torch.tensor(c / cs)
    pert = float(extra.get("perturb", 0.0))
    if pert > 0:
        rng = np.random.default_rng(seed)
        for i2, e2 in enumerate(prob.elements):
            if e2.kind == "exterior":
                continue
            for off in (prob.off_phi, prob.off_q):
                sl = slice(off[i2], off[i2 + 1])
                x[sl] *= torch.tensor(1 + pert * rng.normal(size=int(off[i2 + 1] - off[i2])))
    if prob.ix_cl is not None:
        x[prob.ix_cl] = cl
    if prob.ix_z0 is not None:
        x[prob.ix_z0] = z0L
    return _amp_normalize(prob, x.to(dev))


# ----------------------------------------------------------------------------- T2 seed (lead note 13, seeds/ring_t2.py)
_T2_PARAMS = None


def _t2_F_all(rho, c, Finf, b, rho1, n):
    beta, nu = 1 / (2 * c), (1 + c) / 2
    A = c + nu - Finf
    rho = np.asarray(rho, dtype=float)
    u = (rho / b) ** 3
    t = 1 + u
    T0 = t ** (-beta / 3)
    T1 = -beta * rho ** 2 / b ** 3 * t ** (-beta / 3 - 1)
    T2 = -beta * t ** (-beta / 3 - 2) * (2 * rho / b ** 3 * t - (beta + 3) * rho ** 4 / b ** 6)
    x = (rho / rho1) ** n
    S0 = 1 / (1 + x)
    S1 = -n * rho ** (n - 1) / rho1 ** n / (1 + x) ** 2
    S2 = n * rho ** (n - 2) / rho1 ** n * ((n + 1) * x - (n - 1)) / (1 + x) ** 3
    return Finf * T0 + A * S0, Finf * T1 + A * S1, Finf * T2 + A * S2


def _t2_fit(c, b, n):
    from scipy.optimize import fsolve
    nu = (1 + c) / 2

    def eqs(p):
        F, F1, _ = _t2_F_all(1.0, c, p[0], b, np.exp(p[1]), n)
        return [float(F - c), float(F1 + nu)]
    sol, _, ier, _ = fsolve(eqs, [0.3, 0.0], full_output=True)
    if ier != 1:
        raise RuntimeError("ring_t2 fit failed")
    return float(sol[0]), float(np.exp(sol[1]))


def t2_params(c, K):
    global _T2_PARAMS
    if _T2_PARAMS is None:
        here = os.path.dirname(os.path.abspath(__file__))
        _T2_PARAMS = [t for t in json.load(open(os.path.join(here, "..", "..", "configs", "ring_t2_params_from_lead.json"))) if not t.get("infeasible")]
    t = min(_T2_PARAMS, key=lambda t: (t["c"] - c) ** 2 + (math.log(t["K"] / K)) ** 2)
    return t["b"], t["n"]


def ring_t2(r, z, c, K, b=None, n=None):
    """Lead's T2 seed: phi = z F(rho), q = K s z ((1 + rho)/2)^(-(3 + 1/c)/2), rho = r^2 + z^2; odd in z; ring source at (1, 0)."""
    if b is None or n is None:
        b, n = t2_params(c, K)
    Finf, rho1 = _t2_fit(c, b, n)
    r = np.asarray(r, float); z = np.asarray(z, float)
    s_ = r ** 2; rho = s_ + z ** 2
    F, F1, F2 = _t2_F_all(rho, c, Finf, b, rho1, n)
    gam = (3 + 1 / c) / 2
    return z * F, K * s_ * z * ((1 + rho) / 2) ** (-gam)


def make_t2_init(prob: Problem, seed: int, extra: dict) -> torch.Tensor:
    """T2 seed fitted to all elements (L = 1: the ring at r = 1 is the dilation gauge)."""
    cl = prob.cl; K = float(extra.get("K", prob.cfg.K_param))

    def fphi(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return ring_t2(r, z, cl, K)[0]

    def fq(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return ring_t2(r, z, cl, K)[1]
    x = prob.fit_function(fphi, fq).detach().cpu().clone()
    i = prob.nel - 1
    e = prob.elements[i]
    for (cols, off, f) in ((prob.cols_phi[i], prob.off_phi, fphi), (prob.cols_q[i], prob.off_q, fq)):
        A0 = e.B[(0, 0)][:, cols]
        y = f(e.R, e.mu)
        wts = 1.0 / (np.abs(y).max(initial=0) * 1e-3 + np.abs(y) + 1e-300)
        cs = np.max(np.abs(A0 * wts[:, None]), axis=0); cs[cs == 0] = 1.0
        c, *_ = np.linalg.lstsq((A0 * wts[:, None]) / cs, y * wts, rcond=None)
        x[off[i]:off[i + 1]] = torch.tensor(c / cs)
    pert = float(extra.get("perturb", 0.0))
    if pert > 0:
        rng = np.random.default_rng(seed)
        for i2, e2 in enumerate(prob.elements):
            if e2.kind == "exterior":
                continue
            for off in (prob.off_phi, prob.off_q):
                sl = slice(off[i2], off[i2 + 1])
                x[sl] *= torch.tensor(1 + pert * rng.normal(size=int(off[i2 + 1] - off[i2])))
    if prob.ix_cl is not None:
        x[prob.ix_cl] = cl
    return x.to(prob.device)


# ----------------------------------------------------------------------------- T3 seed (lead note 14, seeds/pair_t3.py)
_T3_PARAMS = None
_T3_CACHE = {}


def _t3_F_all(rho, c, Finf, b, rho1, n, p=1.0):
    beta = 1 / (2 * c)
    A = -(1 + 2 * c) / 2 - Finf
    rho = np.asarray(rho, dtype=float)
    u = (rho / b) ** 3
    t = 1 + u
    T0 = t ** (-beta / 3)
    T1 = -beta * rho ** 2 / b ** 3 * t ** (-beta / 3 - 1)
    T2 = -beta * t ** (-beta / 3 - 2) * (2 * rho / b ** 3 * t - (beta + 3) * rho ** 4 / b ** 6)
    x = (rho / rho1) ** n
    S0 = (1 + x) ** (-p)
    S1 = -p * n * rho ** (n - 1) / rho1 ** n * (1 + x) ** (-p - 1)
    first = 0.0 if n == 1 else (n - 1) * rho ** (n - 2) * (1 + x)
    S2 = -p * n / rho1 ** n * (1 + x) ** (-p - 2) * (first - (p + 1) * n * rho ** (2 * n - 2) / rho1 ** n)
    return Finf * T0 + A * S0, Finf * T1 + A * S1, Finf * T2 + A * S2


def _t3_fit(c, b, n, pw=1.0):
    from scipy.optimize import fsolve

    def eqs(p):
        F, F1, _ = _t3_F_all(1.0, c, p[0], b, np.exp(p[1]), n, pw)
        return [float(F + c / 2), float(F + 2 * F1 - 0.5)]
    for g in [(0.2, 0.0), (0.5, -0.3), (1.0, 0.3), (0.05, -0.1)]:
        sol, _, ier, _ = fsolve(eqs, g, full_output=True)
        if ier == 1 and np.max(np.abs(eqs(sol))) < 1e-12:
            return float(sol[0]), float(np.exp(sol[1]))
    raise RuntimeError("pair_t3 fit failed")


def _t3_axis_q(c, Finf, b, rho1, n, pw=1.0, zmax=1e4):
    from scipy.integrate import solve_ivp
    from scipy.interpolate import CubicSpline

    def phiz_axis(z):
        F, F1, _ = _t3_F_all(z ** 2, c, Finf, b, rho1, n, pw)
        return F + 2 * z ** 2 * F1

    def w(z):
        F, _, _ = _t3_F_all(z ** 2, c, Finf, b, rho1, n, pw)
        return z * (c + 2 * F)

    def rhs(u, y):
        z = np.exp(u)
        if abs(z - 1) < 1e-7:
            z = 1 + 1e-7
        return [-(1 - 2 * phiz_axis(z)) / w(z) * z]
    uu_up = np.linspace(0, np.log(zmax), 4001); uu_dn = np.linspace(0, np.log(1e-4), 4001)
    s_up = solve_ivp(rhs, (0, uu_up[-1]), [0.0], t_eval=uu_up, rtol=1e-11, atol=1e-13, method="DOP853")
    s_dn = solve_ivp(rhs, (0, uu_dn[-1]), [0.0], t_eval=uu_dn, rtol=1e-11, atol=1e-13, method="DOP853")
    u = np.concatenate([s_dn.t[::-1], s_up.t[1:]]); y = np.concatenate([s_dn.y[0][::-1], s_up.y[0][1:]])
    return CubicSpline(u, y - 2 * u)


def t3_params(c):
    global _T3_PARAMS
    if _T3_PARAMS is None:
        here = os.path.dirname(os.path.abspath(__file__))
        _T3_PARAMS = [t for t in json.load(open(os.path.join(here, "..", "..", "configs", "pair_t3_params_from_lead.json"))) if not t.get("infeasible")]
    t = min(_T3_PARAMS, key=lambda t: (t["c"] - c) ** 2)
    return t["b"], t["n"], t.get("p", 1.0)


def pair_t3(r, z, c, K):
    """Lead's T3 seed: S1 sources at z = +-1 (q = K there), axial-inflow saddle at the origin; phi odd, q even in z, q = z^2 x smooth."""
    b, n, pw = t3_params(c)
    key = (round(c, 12), b, n, pw)
    if key not in _T3_CACHE:
        Finf, rho1 = _t3_fit(c, b, n, pw)
        _T3_CACHE[key] = (Finf, rho1, _t3_axis_q(c, Finf, b, rho1, n, pw))
    Finf, rho1, L = _T3_CACHE[key]
    r = np.asarray(r, float); z = np.asarray(z, float)
    s_ = r ** 2; rho = s_ + z ** 2
    F, F1, F2 = _t3_F_all(rho, c, Finf, b, rho1, n, pw)
    phi = z * F
    t = np.maximum(rho, 1e-300)
    u = 0.5 * np.log(t)
    lo, hi = np.log(1e-4), np.log(1e4)
    uc = np.clip(u, lo, hi)
    logQ2 = L(uc)
    logQ2 = np.where(u > hi, L(hi) + (-(1 / c) - 2) * (u - hi), logQ2)
    q = K * z ** 2 * np.exp(logQ2)
    return phi, q


def t3_saddle_repair(cl, K, cutoff=0.3):
    """Lead note 18: the separated seed phi = z F(rho) has the wrong sign of e = eta_z(0, 0) at the origin saddle; the axis first
    integral w eta = 2 q (q - K) forces e = 2 K Q/(1 + c) > 0 with Q = q_zz(0, 0)/2.  Returns p1 such that adding chi(R) p1 s z to phi
    (chi a smooth cutoff of radius `cutoff`, chi(1) < 1e-6 so the sources at z = +-1 are untouched) gives the right e; the saddle
    strain phi_z(0, 0) is unchanged.  e changes by -8 p1 (eta = -Delta_5 phi, Delta_5(s z) = 8 z)."""
    h = 1e-4
    q_h = pair_t3(np.array([0.0]), np.array([h]), cl, K)[1][0]
    Q = q_h / h ** 2
    b, n, pw = t3_params(cl)
    key = (round(cl, 12), b, n, pw)
    Finf, rho1, _ = _T3_CACHE[key]
    def eta_axis(z):
        F, F1, F2 = _t3_F_all(z * z, cl, Finf, b, rho1, n, pw)
        return -z * (4 * z * z * F2 + 14 * F1)
    e_seed = (eta_axis(h) - eta_axis(-h)) / (2 * h)
    e_target = 2 * K * Q / (1 + cl)
    p1 = -(e_target - e_seed) / 8.0
    return dict(p1=p1, Q=Q, e_seed=e_seed, e_target=e_target, cutoff=cutoff)


def make_t3_init(prob: Problem, seed: int, extra: dict) -> torch.Tensor:
    cl = prob.cl; K = float(extra.get("K", prob.cfg.K_param))
    rep = t3_saddle_repair(cl, K) if extra.get("saddle_repair", False) else None

    def fphi(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        phi = pair_t3(r, z, cl, K)[0]
        if rep is not None:
            chi = np.exp(-(R / rep["cutoff"]) ** 4)
            phi = phi + chi * rep["p1"] * r ** 2 * z
        return phi

    def fq(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return pair_t3(r, z, cl, K)[1]
    x = prob.fit_function(fphi, fq).detach().cpu().clone()
    i = prob.nel - 1
    e = prob.elements[i]
    for (cols, off, f) in ((prob.cols_phi[i], prob.off_phi, fphi), (prob.cols_q[i], prob.off_q, fq)):
        A0 = e.B[(0, 0)][:, cols]
        y = f(e.R, e.mu)
        wts = 1.0 / (np.abs(y).max(initial=0) * 1e-3 + np.abs(y) + 1e-300)
        cs = np.max(np.abs(A0 * wts[:, None]), axis=0); cs[cs == 0] = 1.0
        c, *_ = np.linalg.lstsq((A0 * wts[:, None]) / cs, y * wts, rcond=None)
        x[off[i]:off[i + 1]] = torch.tensor(c / cs)
    if prob.ix_cl is not None:
        x[prob.ix_cl] = cl
    return x.to(prob.device)


# ----------------------------------------------------------------------------- T1 positive-strain seeds (lead note 20, referee files)
_T1B = {}


def t1budget_seed(c):
    """Referee's positive induced-strain T1 seed at the tabulated c (0.60, 0.68, 0.74): phi closed form
    z (1 + 3 z^2)/(2 (1 + a s + z^2)^(1 + 1/(2c))), q = K h with h the unit-amplitude characteristic swirl on the grid (x = log R, mu in [0, 1];
    q even in z).  Returns (meta, phi_fn(r, z), h_fn(r, z)) with h extrapolated like R^-(alpha + 1) beyond the grid."""
    key = round(c, 2)
    if key not in _T1B:
        from scipy.interpolate import RegularGridInterpolator
        here = os.path.dirname(os.path.abspath(__file__))
        d = os.path.join(here, "..", "..", "configs", "t1budget_seeds")
        meta = json.load(open(os.path.join(d, f"c{key:.2f}.json")))
        with np.load(os.path.join(d, f"c{key:.2f}.npz"), allow_pickle=False) as a:
            x, m, h = a["x"].copy(), a["m"].copy(), a["h"].copy()
        interp = RegularGridInterpolator((x, m), h, method="cubic", bounds_error=False, fill_value=None)
        alpha = (1 - key) / key; a_asp = meta["radial_aspect_parameter"]; xmax = float(x.max()); xmin = float(x.min())

        def h_fn(r, z):
            r = np.asarray(r, float); z = np.asarray(z, float)
            R = np.sqrt(r * r + z * z); Rs = np.where(R > 0, R, 1e-300); mu = np.abs(np.where(R > 0, z / Rs, 1.0))
            lx = np.log(np.maximum(Rs, 1e-300))
            lxc = np.clip(lx, xmin, xmax)
            v = interp(np.stack([lxc.ravel(), np.clip(mu, 0, 1).ravel()], axis=1)).reshape(R.shape)
            v = np.where(lx > xmax, v * np.exp(-(alpha + 1) * (lx - xmax)), v)      # power-law tail beyond the grid
            return v

        def phi_fn(r, z):
            r = np.asarray(r, float); z = np.asarray(z, float)
            return 0.5 * z * (1 + 3 * z * z) / (1 + a_asp * r * r + z * z) ** (1 + 1 / (2 * key))
        _T1B[key] = (meta, phi_fn, h_fn)
    return _T1B[key]


def make_t1budget_init(prob: Problem, seed: int, extra: dict) -> torch.Tensor:
    """T1 seed with positive induced source strain (referee), swirl amplitude q0 = extra['q0'] (q = q0 h, h(source) = 1)."""
    cl = prob.cl
    meta, phi_fn, h_fn = t1budget_seed(min((0.60, 0.68, 0.74), key=lambda c: abs(c - cl)))
    q0 = float(extra.get("q0", meta["K"]))

    def fphi(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return phi_fn(r, z)

    def fq(R, mu):
        r = R * np.sqrt(np.clip(1 - mu ** 2, 0, None)); z = R * mu
        return q0 * h_fn(r, z)
    x = prob.fit_function(fphi, fq).detach().cpu().clone()
    i = prob.nel - 1
    e = prob.elements[i]
    for (cols, off, f) in ((prob.cols_phi[i], prob.off_phi, fphi), (prob.cols_q[i], prob.off_q, fq)):
        A0 = e.B[(0, 0)][:, cols]
        y = f(e.R, e.mu)
        wts = 1.0 / (np.abs(y).max(initial=0) * 1e-3 + np.abs(y) + 1e-300)
        cs = np.max(np.abs(A0 * wts[:, None]), axis=0); cs[cs == 0] = 1.0
        c, *_ = np.linalg.lstsq((A0 * wts[:, None]) / cs, y * wts, rcond=None)
        x[off[i]:off[i + 1]] = torch.tensor(c / cs)
    if prob.ix_cl is not None:
        x[prob.ix_cl] = cl
    if prob.ix_z0 is not None:
        x[prob.ix_z0] = 0.0
    return _amp_normalize(prob, x.to(prob.device))
