"""Seed families for the multi-start search. Every seed is normalized to the dilation gauge int_S2 |F|^2 = 1
(coefficients scaled by one common factor); the core/tail amplitude ratio is a free seed parameter.

Families:
  'tail'   : explicit tail family (T modes (1,0) and (2,2,c): T ~ r^-alpha [cos theta - eps sin^2 theta cos 2 chi])
             plus random core content;
  'random' : random toroidal/poloidal coefficients with spectral decay in l and k, random helicity mix,
             random non-axisymmetric fraction (order-one allowed);
  'poloidal', 'toroidal': one potential dominant;
  'nonaxi' : m > 0 content dominant (genuinely non-axisymmetric start)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import alpha_of

DT = torch.float64


def _norm_to_gauge(prob, aT, aS, c_l, omega):
    n2 = prob.tail_norm2(aT, aS, c_l, omega).item()
    if n2 <= 0:
        raise ValueError("seed has zero tail")
    f = 1.0 / math.sqrt(n2)
    return aT * f, aS * f


def make_seed(prob, family, rng, c_l, omega, params=None):
    if family == "affine_core":
        from .transfer import affine_core_seed
        return affine_core_seed(prob, rng, c_l, omega, **(params or {}))
    model = prob.model
    params = params or {}
    Nk, Nq = model.Nk, model.Nq
    l = model.l_arr.cpu().numpy(); m = model.m_arr.cpu().numpy()
    t = np.array([tt for (_, _, tt) in model.modes])
    dev = model.r.device
    alpha = alpha_of(c_l)
    R0 = model.R0
    # radial spectral decay (core structure) and angular decay
    dk = params.get("decay_k", rng.uniform(0.15, 0.6))
    dl = params.get("decay_l", rng.uniform(0.2, 0.8))
    core_ratio = params.get("core_ratio", float(np.exp(rng.uniform(np.log(0.3), np.log(3.0)))))
    nonaxi = params.get("nonaxi", rng.uniform(0.2, 1.0))      # relative amplitude of m > 0 modes
    tor_frac = params.get("tor_frac", rng.uniform(0.2, 0.8))  # toroidal fraction of the amplitude
    if family == "toroidal":
        tor_frac = rng.uniform(0.85, 1.0)
    if family == "poloidal":
        tor_frac = rng.uniform(0.0, 0.15)
    if family == "nonaxi":
        nonaxi = rng.uniform(1.0, 3.0)
    wl = np.exp(-dl * (l - 1)); wm = np.where(m > 0, nonaxi, 1.0)
    wk = np.exp(-dk * np.arange(Nk))
    aT = rng.normal(size=(Nk, Nq)) * wk[:, None] * (wl * wm)[None, :] * tor_frac
    aS = rng.normal(size=(Nk, Nq)) * wk[:, None] * (wl * wm)[None, :] * (1 - tor_frac)
    # tail amplitude (Phi_k sum) vs core: scale the k>=1 part by core_ratio relative to k=0
    aT[1:] *= core_ratio; aS[1:] *= core_ratio
    if family == "tail":
        eps = params.get("eps", float(rng.choice([0.05, 0.2, 0.5, 1.0])))
        # T tail: r^-alpha [cos theta - eps sin^2 theta cos 2 chi]; Y_10 = sqrt(3/4pi) cos theta,
        # Y_22c = sqrt(2) N_22 * 3 sin^2 theta cos 2 phi with N_22 = sqrt(5/(4 pi) /24)
        q10 = model.modes.index((1, 0, 0))
        amp10 = 1.0 / math.sqrt(3 / (4 * math.pi))
        aT[:, :] *= params.get("tail_core_noise", 0.3) * core_ratio   # keep random content as core perturbation only
        aS[:, :] *= params.get("tail_core_noise", 0.3) * core_ratio
        aT[0, :] = 0.0; aS[0, :] = 0.0
        aT[0, q10] = amp10 / R0 ** (alpha + 1)
        if (2, 2, 0) in model.modes:
            q22 = model.modes.index((2, 2, 0))
            N22 = math.sqrt(5 / (4 * math.pi) / 24)
            aT[0, q22] = -eps / (3 * math.sqrt(2) * N22) / R0 ** (alpha + 2)
    aT = torch.tensor(aT, dtype=DT, device=dev); aS = torch.tensor(aS, dtype=DT, device=dev)
    aT, aS = _norm_to_gauge(prob, aT, aS, torch.tensor(c_l, dtype=DT, device=dev), torch.tensor(omega, dtype=DT, device=dev))
    meta = dict(family=family, decay_k=dk, decay_l=dl, core_ratio=core_ratio, nonaxi=nonaxi, tor_frac=tor_frac)
    if family == "tail":
        meta["eps"] = eps
    z = model.pack(aT, aS, c_l, omega) if model.free_params else model.pack(aT, aS)
    return z, meta
