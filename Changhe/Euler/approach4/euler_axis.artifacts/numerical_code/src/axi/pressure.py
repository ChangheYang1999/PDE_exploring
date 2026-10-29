"""Full-space pressure by Legendre-mode Green's functions (PROMPT.md section 7, SPEC 4).

    -Delta P = f,   P -> 0 at infinity,
    f(R, mu) = sum_l f_l(R) P_l(mu),   f_l(R) = (2l+1)/2 int_{-1}^{1} f(R, mu) P_l(mu) dmu,
    P_l(R) = 1/(2l+1) [ R^{-l-1} I_in_l(R) + R^l I_out_l(R) ],
    I_in_l(R) = int_0^R s^{l+2} f_l(s) ds,   I_out_l(R) = int_R^inf s^{1-l} f_l(s) ds,
    P_l'(R) = 1/(2l+1) [ -(l+1) R^{-l-2} I_in_l(R) + l R^{l-1} I_out_l(R) ]   (the boundary terms cancel).

Radial quadrature: the half-line is cut into panels (inner panels follow the representation's element boundaries,
exterior panels are geometric with ratio <= 10 out to R_far); on each panel f_l(s) is sampled at Chebyshev points
and integrated exactly through its Chebyshev interpolant, so I_in and I_out are available at any R in closed form.
Beyond R_far the exterior integral is completed analytically with the power law fitted on the last panel
(f_l(s) ~ f_l(R_far) (s/R_far)^(-p_l)); the remainder is reported.  Angular quadrature: Gauss-Legendre with
n_mu >= 2 nmax + 2 nodes (f is quadratic in a degree-nmax field).  Everything is float64 numpy.
The source f for the Euler profile is sum_ij d_i U_j d_j U_i = (U^r_r)^2 + (U^z_z)^2 + (U^r/r)^2 + 2 U^r_z U^z_r - 2 (U^theta/r) U^theta_r
(ops.primitive_terms, checked against the Cartesian expression in tests/test_ops.py).
"""
from __future__ import annotations

import math
from typing import Callable, List, Tuple

import numpy as np
from numpy.polynomial import chebyshev as Cheb, legendre as Leg


def cheb_nodes(a, b, n):
    k = np.arange(n)
    x = np.cos(np.pi * (2 * k + 1) / (2 * n))             # Chebyshev points of the first kind in (-1, 1)
    return 0.5 * (b - a) * x + 0.5 * (b + a), x


def gegenbauer32(mu, lmax):
    """C_l^{3/2}(mu), l = 0..lmax, by the recurrence (l+1) C_{l+1} = 2(l + 3/2) mu C_l - (l + 2) C_{l-1}; returns (lmax+1, len(mu))."""
    mu = np.asarray(mu, float)
    C = np.zeros((lmax + 1, mu.size))
    C[0] = 1.0
    if lmax >= 1:
        C[1] = 3.0 * mu
    for l in range(1, lmax):
        C[l + 1] = (2 * (l + 1.5) * mu * C[l] - (l + 2) * C[l - 1]) / (l + 1)
    return C


class PressureSolver:
    """Mode Green's-function inverse of -Delta in dimension dim for zonal (axisymmetric) sources.
    dim = 3: -Delta P = f with Legendre modes P_l (the pressure).
    dim = 5: -Delta_5 phi = eta with Gegenbauer C_l^{3/2} modes (zonal measure (1 - mu^2) dmu):
             phi_l(R) = 1/(2l+3) [ R^{-l-3} int_0^R s^{l+4} eta_l ds + R^l int_R^inf s^{1-l} eta_l ds ],
             phi_l'(R) = 1/(2l+3) [ -(l+3) R^{-l-4} I_in + l R^{l-1} I_out ]."""
    def __init__(self, f_func: Callable[[np.ndarray, np.ndarray], np.ndarray], panel_edges: List[float], R_far: float,
                 lmax: int, n_mu: int, order: int = 32, ext_ratio: float = 4.0, dim: int = 3):
        """f_func(R, mu) -> f values (vectorized).  panel_edges: increasing radii starting at 0 and ending at the exterior
        start R_m; exterior panels [R_m, ext_ratio R_m], ... up to >= R_far are appended."""
        self.f_func = f_func
        self.dim = dim
        edges = list(panel_edges)
        Rm = edges[-1]
        while edges[-1] < R_far * (1 - 1e-12):
            edges.append(min(edges[-1] * ext_ratio, R_far) if edges[-1] * ext_ratio < R_far * 1.0001 else R_far)
        self.edges = np.array(edges, float)
        self.lmax = lmax
        self.order = order
        mu, wmu = Leg.leggauss(n_mu)
        self.mu, self.wmu = mu, wmu
        if dim == 3:
            Pl = np.array([Leg.legval(mu, np.eye(lmax + 1)[l]) for l in range(lmax + 1)])        # (lmax+1, n_mu)
            self.proj = Pl * wmu[None, :] * ((2 * np.arange(lmax + 1) + 1) / 2.0)[:, None]        # f_l = proj @ f(mu)
            self.p_in = np.arange(lmax + 1) + 2; self.p_out = 1 - np.arange(lmax + 1)
            self.norm = 2 * np.arange(lmax + 1) + 1; self.pow_in = -np.arange(lmax + 1) - 1
        elif dim == 5:
            Pl = gegenbauer32(mu, lmax)
            wz = wmu * (1 - mu * mu)
            h = (Pl * Pl * wz[None, :]).sum(axis=1)                                                 # int C_l^2 (1-mu^2) dmu (exact by quadrature)
            self.proj = Pl * wz[None, :] / h[:, None]
            self.p_in = np.arange(lmax + 1) + 4; self.p_out = 1 - np.arange(lmax + 1)
            self.norm = 2 * np.arange(lmax + 1) + 3; self.pow_in = -np.arange(lmax + 1) - 3
        else:
            raise ValueError(dim)
        self.Pl = Pl
        self._build()

    def _fl_at(self, R):
        """f_l(R) for an array of radii: returns (len(R), lmax+1)."""
        RR, MM = np.meshgrid(R, self.mu, indexing="ij")
        F = self.f_func(RR.ravel(), MM.ravel()).reshape(len(R), len(self.mu))
        return F @ self.proj.T

    def _build(self):
        n = self.order
        L = self.lmax
        ls = np.arange(L + 1)
        self.xg, self.wg = np.polynomial.legendre.leggauss(48)
        self.panels = []
        for a, b in zip(self.edges[:-1], self.edges[1:]):
            s, x = cheb_nodes(a, b, n)
            fl = self._fl_at(s)                                     # (n, L+1)
            V = np.array([Cheb.chebval(x, np.eye(n)[k]) for k in range(n)]).T   # (n, n) Chebyshev Vandermonde
            cf = np.linalg.solve(V, fl)                                # Chebyshev coefficients of f_l(s(x)) per l
            p = dict(a=a, b=b, cf=cf, fl_nodes=fl, s_nodes=s)
            p["tot_in"] = self._quad(p, np.array([a]), np.array([b]), self.p_in)[0]
            p["tot_out"] = self._quad(p, np.array([a]), np.array([b]), self.p_out)[0] if a > 0 else None
            self.panels.append(p)
        # Why per-point Gauss quadrature instead of Chebyshev antiderivatives: I_in(R) = int_0^R s^{l+2} f_l ds is multiplied
        # by R^{-l-1}; an antiderivative stored on a panel [a, b] carries an absolute round-off of eps * b^{l+3} max|f_l|,
        # which R^{-l-1} amplifies by (b/R)^{l+1} (1e17 for b/R = 10, l = 16).  Integrating only over [a, R] from the
        # interpolant of f_l keeps the error at eps * R^{l+3}, i.e. eps * R^2 after the prefactor; likewise for I_out.
        nP = len(self.panels)
        self.Iin_start = np.zeros((nP, L + 1)); self.Iout_end = np.zeros((nP, L + 1))
        acc = np.zeros(L + 1)
        for i, p in enumerate(self.panels):
            self.Iin_start[i] = acc; acc = acc + p["tot_in"]
        last = self.panels[-1]
        s = last["s_nodes"]; fl = last["fl_nodes"]
        R_far = last["b"]
        fl_far = self._fl_at(np.array([R_far]))[0]
        self._fl_far = fl_far
        self.tail_p = np.zeros(L + 1); self.tail_rem = np.zeros(L + 1)
        i0, i1 = np.argmin(s), np.argmax(s)
        for l in range(L + 1):
            f0, f1 = fl[i0, l], fl[i1, l]
            if abs(f0) > 0 and abs(f1) > 0 and np.sign(f0) == np.sign(f1):
                p_l = -math.log(abs(f1) / abs(f0)) / math.log(s[i1] / s[i0])
            else:
                p_l = 2 * l + 4.0
            self.tail_p[l] = p_l
            expo = p_l + l - 2                 # int_Rfar^inf s^{1-l} f_far (s/Rfar)^-p ds = f_far Rfar^{2-l} / (p + l - 2)   (same for dim 3 and 5)
            self.tail_rem[l] = fl_far[l] * R_far ** (2 - l) / expo if expo > 0.05 else 0.0
        acc = self.tail_rem.copy()
        for i in range(nP - 1, -1, -1):
            self.Iout_end[i] = acc
            if self.panels[i]["tot_out"] is not None:
                acc = acc + self.panels[i]["tot_out"]
        self.Iout_total = acc

    def _quad(self, p, lo, hi, powers):
        """int_lo^hi s^{powers[l]} f_l(s) ds for arrays lo, hi (same length) inside panel p; returns (len(lo), L+1)."""
        a, b, cf = p["a"], p["b"], p["cf"]
        L = self.lmax
        lo = np.asarray(lo, float); hi = np.asarray(hi, float)
        half = 0.5 * (hi - lo)
        sg = half[:, None] * self.xg[None, :] + 0.5 * (hi + lo)[:, None]          # (m, 48)
        x = 2 * (sg - a) / (b - a) - 1
        xf = x.ravel()
        fl = np.array([Cheb.chebval(xf, cf[:, l]) for l in range(L + 1)]).T.reshape(len(lo), len(self.xg), L + 1)
        w = half[:, None] * self.wg[None, :]                                        # (m, 48)
        with np.errstate(divide="ignore", invalid="ignore"):
            sp = sg[:, :, None] ** np.asarray(powers, float)[None, None, :]        # (m, 48, L+1)
        return np.einsum("mg,mgl,mgl->ml", w, sp, fl)

    def integrals(self, R):
        """I_in_l(R), I_out_l(R) for an array of radii (len(R), lmax+1)."""
        R = np.asarray(R, float)
        L = self.lmax
        ls = np.arange(L + 1)
        Iin = np.zeros((len(R), L + 1)); Iout = np.zeros((len(R), L + 1))
        idx = np.clip(np.searchsorted(self.edges, R, side="right") - 1, 0, len(self.panels) - 1)
        for i, p in enumerate(self.panels):
            m = idx == i
            if not np.any(m):
                continue
            Rm_ = np.clip(R[m], p["a"], p["b"])
            Iin[m] = self.Iin_start[i][None, :] + self._quad(p, np.full_like(Rm_, p["a"]), Rm_, self.p_in)
            Iout[m] = self.Iout_end[i][None, :] + self._quad(p, Rm_, np.full_like(Rm_, p["b"]), self.p_out)
        beyond = R > self.edges[-1]
        if np.any(beyond):      # outside the resolved range: power-law tail f_l(s) = f_l(R_far) (s/R_far)^-p_l for both integrals
            Rb = R[beyond]; Rf = self.edges[-1]
            fl_far = self._fl_far
            for l in range(L + 1):
                p_l = self.tail_p[l]; pin = self.p_in[l]
                e_in = pin + 1 - p_l           # int_Rf^R s^pin f_far (s/Rf)^-p ds = f_far Rf^(pin+1) [(R/Rf)^e_in - 1]/e_in
                add = fl_far[l] * Rf ** (pin + 1) * (((Rb / Rf) ** e_in - 1.0) / e_in if abs(e_in) > 1e-12 else np.log(Rb / Rf))
                Iin[beyond, l] = self.Iin_start[-1][l] + self.panels[-1]["tot_in"][l] + add
                Iout[beyond, l] = self.tail_rem[l] * (Rb / Rf) ** (2 - l - p_l) if self.tail_rem[l] != 0 else 0.0
        return Iin, Iout

    def modes(self, R):
        """P_l(R) and P_l'(R) arrays (len(R), lmax+1)."""
        R = np.asarray(R, float)
        Iin, Iout = self.integrals(R)
        ls = np.arange(self.lmax + 1)
        Rl = R[:, None] ** ls[None, :]
        Rml1 = R[:, None] ** self.pow_in[None, :]                     # R^{-l-1} (dim 3) or R^{-l-3} (dim 5)
        Pl = (Rml1 * Iin + Rl * Iout) / self.norm[None, :]
        dPl = (self.pow_in[None, :] * Rml1 / R[:, None] * Iin + ls[None, :] * Rl / R[:, None] * Iout) / self.norm[None, :]
        return Pl, dPl

    def evaluate(self, R, mu):
        """P, P_R, P_mu at points (R, mu); plus P_r, P_z."""
        R = np.asarray(R, float); mu = np.asarray(mu, float)
        Pl, dPl = self.modes(R)
        L = self.lmax
        if self.dim == 3:
            Pm = np.array([Leg.legval(mu, np.eye(L + 1)[l]) for l in range(L + 1)]).T          # (n, L+1)
            dPm = np.array([Leg.legval(mu, Leg.legder(np.eye(L + 1)[l])) if l > 0 else np.zeros_like(mu) for l in range(L + 1)]).T
        else:
            Pm = gegenbauer32(mu, L).T
            # d/dmu C_l^{3/2} = 3 C_{l-1}^{5/2}; use the identity d/dmu C_l^{lam} = 2 lam C_{l-1}^{lam+1}; C^{5/2} by recurrence
            C52 = np.zeros((L + 1, mu.size)); C52[0] = 1.0
            if L >= 1: C52[1] = 5.0 * mu
            for l in range(1, L):
                C52[l + 1] = (2 * (l + 2.5) * mu * C52[l] - (l + 4) * C52[l - 1]) / (l + 1)
            dPm = np.zeros((mu.size, L + 1))
            for l in range(1, L + 1):
                dPm[:, l] = 3.0 * C52[l - 1]
        P = np.sum(Pl * Pm, axis=1)
        PR = np.sum(dPl * Pm, axis=1)
        Pmu = np.sum(Pl * dPm, axis=1)
        s2 = 1 - mu * mu; s = np.sqrt(np.clip(s2, 0, None))
        Pr = s * PR - (mu * s / R) * Pmu
        Pz = mu * PR + (s2 / R) * Pmu
        return dict(P=P, P_R=PR, P_mu=Pmu, P_r=Pr, P_z=Pz)

    def mode_coefficients_at(self, R):
        """Low multipole diagnostics: the coefficients of R^{-l-1} in P_l for large R, i.e. I_in_l(R) (+ the I_out part) at R."""
        Iin, Iout = self.integrals(np.array([R]))
        return dict(I_in=Iin[0], I_out=Iout[0], tail_p=self.tail_p, tail_rem=self.tail_rem, Iout_total=self.Iout_total)


def source_from_candidate(prob, x):
    """Return f_func(R, mu) = pressure Poisson source of the candidate (CPU numpy), using ops.primitive_terms."""
    import torch
    from . import ops
    xs = x.detach().cpu()

    def f_func(R, mu):
        phi, q = prob.eval_all(xs, R, mu)
        g = ops.geom(torch.tensor(np.asarray(R, float)), torch.tensor(np.asarray(mu, float)))
        P = ops.primitive_terms(phi, q, g, prob.cl)
        return P["S"].numpy()
    return f_func


def solver_for_candidate(prob, x, lmax=None, order=32, R_far_factor=1e6, n_mu=None):
    edges = [0.0, 0.25 * prob.cfg.R1, prob.cfg.R1] + [e.Rhi for e in prob.elements[1:-1]]
    lmax = lmax if lmax is not None else 2 * prob.cfg.nmax + 2      # the quadratic source of a degree-nmax field has Legendre degree <= 2 nmax (+2 margin)
    n_mu = n_mu or (2 * prob.cfg.nmax + 14)
    return PressureSolver(source_from_candidate(prob, x), edges, R_far_factor * prob.Rm, lmax, n_mu, order=order)


def eta_from_candidate(prob, x):
    """f_func(R, mu) = eta = -Delta_5 phi of the candidate (analytic from the basis)."""
    import torch
    from . import ops
    xs = x.detach().cpu()

    def f_func(R, mu):
        phi, q = prob.eval_all(xs, R, mu)
        g = ops.geom(torch.tensor(np.asarray(R, float)), torch.tensor(np.asarray(mu, float)))
        return ops.eta_and_grad(phi, g)[(0, 0)].numpy()
    return f_func


def stream_solver_for_candidate(prob, x, lmax=None, order=32, R_far_factor=1e6, n_mu=None):
    """5D Green inverse: phi_G = Delta_5^{-1}(-eta) for the candidate's eta; compare with the candidate's phi (SPEC 6.6 moment checks)."""
    edges = [0.0, 0.25 * prob.cfg.R1, prob.cfg.R1] + [e.Rhi for e in prob.elements[1:-1]]
    lmax = lmax if lmax is not None else prob.cfg.nmax + 2
    n_mu = n_mu or (2 * prob.cfg.nmax + 12)
    return PressureSolver(eta_from_candidate(prob, x), edges, R_far_factor * prob.Rm, lmax, n_mu, order=order, dim=5)
