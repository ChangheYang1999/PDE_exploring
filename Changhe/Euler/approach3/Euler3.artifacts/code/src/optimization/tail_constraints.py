"""Exact cancellation of the forbidden tail rates alpha+1 and alpha+2 (SPEC 4.4 rate bookkeeping; lead notes 2026-10-24T20:39Z
and 20:44Z, derivations d17). For a column with Chebyshev coefficients a_k (cos) and b_k (sin) of a twisted (l, m) pair, with
x = (s-R0)/(s+R0): T_k(2x-1) = 1 - 4 R0 k^2/r + R0^2 (4k^2 + (8/3) k^2(k^2-1))/r^2 + O(r^-3); the envelope (s/R0)^-(a+l) and the
regularized twist add r^-2 terms. Constraints (p = (a+l)/2 with a = alpha (T) or alpha-1 (S), q = m kappa/2, kappa = omega/c_l):
    sum_k k^2 a_k = 0,  sum_k k^2 b_k = 0                                                    (rate alpha+1)
    (8/3) sum_k k^2(k^2-1) a_k = p sum_k a_k - q sum_k b_k,
    (8/3) sum_k k^2(k^2-1) b_k = q sum_k a_k + p sum_k b_k                                   (rate alpha+2)
Four real equations per pair with m >= 1 (two for m = 0); the top two Chebyshev coefficients of each column are eliminated
(linear reparametrization). B and D channels: sum_k k^2 = 0 only (their k^2 moment carries rate 2alpha+2), eliminating the top
coefficient. The reduced vector z_red holds the free coefficients; expand(z_red) returns the full z."""
from __future__ import annotations
import math
import torch
from ..equations.fields import alpha_of

DT = torch.float64


class TailConstraints:
    def __init__(self, model, nu=0.0):
        """nu > 0 (S8): the rate alpha+2 moment of every leading column becomes inhomogeneous, C_2 = -(nu/(2 c_l R0^2)) B t with t the
        leading amplitude (complex over a cos/sin pair, t = sum a + i sum b) and B = (-P - i m kappa)(1 + 2 l - P - i m kappa), P the
        envelope power (alpha + l for T, alpha + l - 1 for S), kappa = omega/c_l (lead d63 Q3: t_2 = -(nu/(2 c_l)) B_alpha t). The rate
        alpha+1 moment stays zero. In the code's normalization (k4 - p).a + q 1.b is the coefficient of (R0/r)^(P+2) when sum a is the
        coefficient of (R0/r)^P."""
        self.model = model; self.nu = float(nu)
        self.Nk = model.Nk
        self.k = torch.arange(model.Nk, dtype=DT, device=model.r.device)
        self.k2 = self.k ** 2
        self.k4 = (8.0 / 3.0) * self.k2 * (self.k2 - 1)
        # pairs: for each cos mode (m > 0) its partner; m = 0 singles
        self.pairs = [(q, q + 1, int(model.m_arr[q]), int(model.l_arr[q])) for q, (l, m, t) in enumerate(model.modes) if m > 0 and t == 0]
        self.singles = [(q, int(model.l_arr[q])) for q, (l, m, t) in enumerate(model.modes) if m == 0]
        nf = model.Nk - 2
        self.n_free_per_col = nf
        # reduced layout: A and C columns keep Nk-2 coefficients each; B, D keep Nk_B - 1 / Nk_D - 1; E unchanged
        lay = dict(model.layout)
        self.red_sizes = {"A": nf, "C": nf, "B": (lay["B"] if lay["B"] <= 1 else lay["B"] - 1), "D": (lay["D"] if lay["D"] <= 1 else lay["D"] - 1), "E": lay["E"]}
        self.ncols = getattr(model, "ncols", {k: model.Nq for k in ("A", "C", "B", "D", "E")})
        self.cols = getattr(model, "chan_cols", None)
        self.n_red = sum(self.red_sizes[k] * self.ncols[k] for k in ("A", "C", "B", "D", "E")) + (2 if model.free_params else 0)

    def _solve_pair(self, free_a, free_b, p, q, visc=None):
        """free_a, free_b: (Nk-2,) free coefficients of the two columns. Returns full columns (Nk,) with the top two
        coefficients chosen so that all four constraints hold (p, q tensors). visc: optional (Br, Bi) real and imaginary parts of
        -(nu/(2 c_l R0^2)) B for the inhomogeneous rate alpha+2 rows: (k4 - p).a + q 1.b = Br 1.a - Bi 1.b, -q 1.a + (k4 - p).b = Bi 1.a + Br 1.b."""
        Nk = self.Nk; k2, k4 = self.k2, self.k4
        # unknowns u = (a_{N-2}, a_{N-1}, b_{N-2}, b_{N-1}); constraints:
        #  k2 . a = 0 ;  k2 . b = 0 ;  (k4 - p) . a + q 1.b = 0 ;  -q 1.a + (k4 - p) . b = 0   (the sums over all k)
        ones = torch.ones_like(k2)
        ra = torch.stack([k2, torch.zeros_like(k2), k4 - p * ones, -q * ones], 0)     # coefficients multiplying a_k in the 4 equations
        rb = torch.stack([torch.zeros_like(k2), k2, q * ones, k4 - p * ones], 0)     # multiplying b_k
        if visc is not None:                                                             # move the viscous targets to the left-hand side
            Br, Bi = visc
            ra = ra - torch.stack([0 * ones, 0 * ones, Br * ones, Bi * ones], 0)
            rb = rb - torch.stack([0 * ones, 0 * ones, -Bi * ones, Br * ones], 0)
        M = torch.stack([ra[:, Nk - 2], ra[:, Nk - 1], rb[:, Nk - 2], rb[:, Nk - 1]], 1)   # (4, 4)
        rhs = -(ra[:, : Nk - 2] @ free_a + rb[:, : Nk - 2] @ free_b)                        # (4,)
        u = torch.linalg.solve(M, rhs)
        a = torch.cat([free_a, u[:2]]); b = torch.cat([free_b, u[2:]])
        return a, b

    def _solve_single(self, free_a, p, visc=None):
        Nk = self.Nk; k2, k4 = self.k2, self.k4
        ra = torch.stack([k2, k4 - p * torch.ones_like(k2)], 0)
        if visc is not None:
            ra = ra - torch.stack([0 * k2, visc[0] * torch.ones_like(k2)], 0)
        M = ra[:, Nk - 2:]                                                                    # (2, 2)
        rhs = -(ra[:, : Nk - 2] @ free_a)
        u = torch.linalg.solve(M, rhs)
        return torch.cat([free_a, u])

    def _solve_k2(self, free, n):
        """B/D columns: sum k^2 a_k = 0 by the top coefficient. For n = 1 the k^2 moment vanishes identically (vacuous): unchanged."""
        if n == 1:
            return free if free.numel() == 1 else torch.zeros(1, dtype=DT, device=free.device)
        k2 = torch.arange(n, dtype=DT, device=free.device) ** 2
        top = -(k2[: n - 1] @ free) / k2[n - 1]
        return torch.cat([free, top[None]])

    def expand(self, z_red):
        model = self.model
        Nq = model.Nq
        off = 0
        red = {}
        for name in ("A", "C", "B", "D", "E"):
            n = self.red_sizes[name]; nc = self.ncols[name]
            a = z_red[off: off + n * nc].reshape(n, nc) if n > 0 else torch.zeros(0, nc, dtype=DT, device=z_red.device); off += n * nc
            if nc != Nq:
                a = torch.zeros(n, Nq, dtype=DT, device=z_red.device).index_copy(1, self.cols[name], a)
            red[name] = a
        if model.free_params:
            c_l, omega = z_red[-2], z_red[-1]
        else:
            c_l = torch.tensor(model.c_l0, dtype=DT, device=z_red.device); omega = torch.tensor(model.omega0, dtype=DT, device=z_red.device)
        alpha = alpha_of(c_l); kappa = omega / c_l
        R0 = torch.as_tensor(model.R0, dtype=DT, device=z_red.device)
        def visc_factor(P, l, m):
            """(Re, Im) of -(nu/(2 c_l R0^2)) (-P - i m kappa)(1 + 2 l - P - i m kappa)."""
            if self.nu <= 0:
                return None
            w1 = torch.complex(-P, -m * kappa); w2 = torch.complex(1 + 2 * l - P, -m * kappa)
            B = -(self.nu / (2 * c_l * R0 ** 2)) * (w1 * w2)
            return (B.real, B.imag)
        full = {}
        for name, a_env in (("A", alpha), ("C", alpha - 1.0)):
            cols = [None] * Nq
            for (qc, qs, m, l) in self.pairs:
                p = (a_env + l) / 2.0; q = m * kappa / 2.0
                a, b = self._solve_pair(red[name][:, qc], red[name][:, qs], p, q, visc=visc_factor(a_env + l, l, m))
                cols[qc] = a; cols[qs] = b
            for (q0, l) in self.singles:
                p = (a_env + l) / 2.0
                cols[q0] = self._solve_single(red[name][:, q0], p, visc=visc_factor(a_env + l, l, 0))
            full[name] = torch.stack(cols, 1)
        for name in ("B", "D"):
            n = dict(model.layout)[name]
            if n > 0:
                full[name] = torch.stack([self._solve_k2(red[name][:, q], n) for q in range(Nq)], 1)
        extra = {k: full[k] for k in ("B", "D") if k in full}
        if self.red_sizes["E"] > 0:
            extra["E"] = red["E"]
        return model.pack(full["A"], full["C"], c_l, omega, extra=extra)

    def reduce(self, z_full):
        """Drop the eliminated coefficients (top two of A/C columns, top one of B/D); the expanded state then satisfies the
        constraints exactly (it differs from z_full in those coefficients only)."""
        d = self.model.unpack_all(z_full)
        def g(name, a):
            return a if self.ncols[name] == self.model.Nq else a[:, self.cols[name]]
        parts = [g("A", d["A"][: self.Nk - 2]).reshape(-1), g("C", d["C"][: self.Nk - 2]).reshape(-1)]
        for name in ("B", "D"):
            if self.red_sizes[name] > 0:
                parts.append(g(name, d[name][: self.red_sizes[name]]).reshape(-1))
        if self.red_sizes["E"] > 0:
            parts.append(g("E", d["E"]).reshape(-1))
        if self.model.free_params:
            parts.append(torch.stack([d["c_l"], d["omega"]]))
        return torch.cat(parts)
