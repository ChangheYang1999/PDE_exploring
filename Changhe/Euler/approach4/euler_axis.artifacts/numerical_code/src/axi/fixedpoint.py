"""Method 2: transport/elliptic fixed point solved by Newton-Krylov (numerically independent of the collocation LM).

Unknowns y = (phi coefficients of all elements, q0) at fixed c_l (or (phi, c_l) at fixed q0).  Map:
  W_m from phi;  z0 = axis zero of W_z = c z + 2 phi(0, z) nearest the previous z0;
  qhat = least-squares Koopman eigenfunction: R_q(qhat; W_m) = 0 with qhat(0, z0) = 1 (linear LS in the q basis);
  etahat from (1+c) etahat + W_m . grad etahat = d_z(qhat^2) (linear LS in an eta basis: inner elements as phi, exterior
          exponents = phi exponents + 2);
  Phi = Delta_5^{-1}(-etahat) by the 5D mode Green's function (pressure.PressureSolver, dim 5), fitted to the phi basis.
Residual: F(y) = [phi - q0^2 Phi(phi);  phi_z(0, z0) - 1/2]  (square system).  Solved with scipy.optimize.newton_krylov
(LGMRES, finite-difference Jacobian action).  At a root, (phi, q = q0 qhat) satisfies the reduced system up to the LS
residuals of the two transport solves, which are reported (they vanish only if W_m admits exact smooth eigenfunctions).
"""
from __future__ import annotations

import math
import time

import numpy as np
import torch
from scipy.optimize import newton_krylov

from . import basis, ops, pressure
from .problem import Problem, PHI_KEYS


class FixedPoint:
    def __init__(self, prob: Problem, z0_init=0.0, w_int=100.0, w_pin=100.0, reg_ext=1e-3, lmax=None, log=print, unknown="q0", q0_fixed=1.0):
        """unknown = "q0": y = (phi, q0) at fixed c_l;  unknown = "cl": y = (phi, c_l) at fixed q0 = q0_fixed."""
        self.unknown = unknown; self.q0_fixed = q0_fixed
        self.prob = prob; self.cl = prob.cl; self.alpha = prob.alpha
        self.z0 = float(z0_init); self.log = log
        self.w_int = w_int; self.w_pin = w_pin; self.reg_ext = reg_ext
        ext = prob.elements[-1]
        self.eta_exps = [e + 2.0 for e in sorted(set(ex for (n, ex) in prob.ext_labels_phi))]
        self.Beta_ext, self.lab_eta = basis.build_B("exterior", ext.Rlo, ext.Rhi, ext.nmax, dict(ext.params, exponents=self.eta_exps), ext.R, ext.mu)
        self.n_eta = [prob.elements[i].nbasis if i < prob.nel - 1 else len(self.lab_eta) for i in range(prob.nel)]
        self.off_eta = np.concatenate([[0], np.cumsum(self.n_eta)]).astype(int)
        self.lmax = lmax if lmax is not None else prob.cfg.nmax + 2
        self.Jq_int = self._interface_rows(self._Bq_at, lambda i: prob.cols_q[i], prob.off_q - prob.nphi, prob.nq)
        self.Je_int = self._interface_rows(self._Beta_at, lambda i: np.arange(self.n_eta[i]), self.off_eta, int(self.off_eta[-1]))
        self.n_evals = 0
        self.last = {}

    # ---- bases at arbitrary points
    def _Bq_at(self, i, R, mu):
        return self.prob.elements[i].eval_at(R, mu)

    def _Beta_at(self, i, R, mu):
        if i < self.prob.nel - 1:
            return self.prob.elements[i].eval_at(R, mu)
        ext = self.prob.elements[-1]
        return basis.build_B("exterior", ext.Rlo, ext.Rhi, ext.nmax, dict(ext.params, exponents=self.eta_exps), R, mu)[0]

    def _interface_rows(self, Bfun, cols_fun, off, ncols, orders=((0, 0), (1, 0))):
        prob = self.prob
        rows = []
        mu_i, _ = basis.gauss_legendre(prob.nmu)
        for i in range(prob.nel - 1):
            Rint = prob.elements[i].Rhi; Rv = np.full_like(mu_i, Rint)
            BA = Bfun(i, Rv, mu_i); BB = Bfun(i + 1, Rv, mu_i)
            for k in orders:
                blk = np.zeros((len(mu_i), ncols))
                blk[:, off[i]:off[i + 1]] = self.w_int * Rint ** k[0] * BA[k][:, cols_fun(i)]
                blk[:, off[i + 1]:off[i + 2]] = -self.w_int * Rint ** k[0] * BB[k][:, cols_fun(i + 1)]
                rows.append(blk)
        return np.concatenate(rows, 0)

    @staticmethod
    def _rz(B, g):
        R, mu = g["R"].numpy(), g["mu"].numpy(); s = np.sqrt(np.clip(1 - mu ** 2, 0, None))
        fr = s[:, None] * B[(1, 0)] - (mu * s / R)[:, None] * B[(0, 1)]
        fz = mu[:, None] * B[(1, 0)] + ((1 - mu ** 2) / R)[:, None] * B[(0, 1)]
        return fr, fz

    @staticmethod
    def _lstsq(A, b):
        cs = np.max(np.abs(A), axis=0); cs[cs == 0] = 1.0
        c, *_ = np.linalg.lstsq(A / cs, b, rcond=None)
        return c / cs

    # ---- the map
    def phi_axis(self, cphi, z):
        R = max(abs(z), 1e-12); mu = 1.0 if z >= 0 else -1.0
        i = self.prob.element_index(R)
        B = self.prob.elements[i].eval_at(np.array([R]), np.array([mu]))
        v0 = float(B[(0, 0)][0, self.prob.cols_phi[i]] @ cphi[i]); v1 = float(B[(1, 0)][0, self.prob.cols_phi[i]] @ cphi[i])
        return v0, mu * v1          # phi, phi_z on the axis

    def locate_z0(self, cphi, z_guess):
        z = z_guess
        for _ in range(50):
            f = self.cl * z + 2 * self.phi_axis(cphi, z)[0]
            df = self.cl + 2 * self.phi_axis(cphi, z)[1]
            if abs(df) < 1e-14:
                break
            step = f / df; z -= step
            if abs(step) < 1e-14 * (1 + abs(z)):
                break
        return z

    def evaluate(self, cphi_all, q0):
        """cphi_all: list of numpy arrays (per element).  Returns dict with Phi fit (per element), qhat coeffs, residual norms."""
        prob = self.prob; cl = self.cl; alpha = self.alpha
        z0 = self.locate_z0(cphi_all, self.z0)
        rows_q, rows_e, nd = [], [], []
        for i in range(prob.nel):
            B = prob.elements[i].B
            phi = {k: torch.tensor(B[k][:, prob.cols_phi[i]] @ cphi_all[i]) for k in PHI_KEYS}
            g = prob.G[i] if prob.device.type == "cpu" else {k: v.cpu() for k, v in prob.G[i].items()}
            Ur, Uz, Uror = ops.velocities(phi, g)
            Wr = (cl * g["r"] + Ur).numpy(); Wz = (cl * g["z"] + Uz).numpy(); Uror = Uror.numpy()
            sq, se = prob.scales(g, alpha); wq = (prob.wnode[i].cpu() * sq).numpy(); we = (prob.wnode[i].cpu() * se).numpy()
            Bq0 = B[(0, 0)][:, prob.cols_q[i]]; fr, fz = self._rz({k: B[k][:, prob.cols_q[i]] for k in ((1, 0), (0, 1))}, g)
            rows_q.append(wq[:, None] * (Bq0 + Wr[:, None] * fr + Wz[:, None] * fz + 2 * Uror[:, None] * Bq0))
            Be = prob.elements[i].B if i < prob.nel - 1 else self.Beta_ext
            er, ez = self._rz({k: Be[k] for k in ((1, 0), (0, 1))}, g)
            rows_e.append(we[:, None] * ((1 + cl) * Be[(0, 0)] + Wr[:, None] * er + Wz[:, None] * ez))
            nd.append(dict(we=we, fz=fz, Bq0=Bq0, wq=wq))
        # qhat
        Aq = np.zeros((sum(r.shape[0] for r in rows_q), prob.nq)); r0 = 0
        for i, r_ in enumerate(rows_q):
            Aq[r0:r0 + r_.shape[0], prob.off_q[i] - prob.nphi:prob.off_q[i + 1] - prob.nphi] = r_; r0 += r_.shape[0]
        _, _, _, mu0, s0, s1 = prob.axis_phi_rows(z0, with_q=True)
        pin = self.w_pin * s0[prob.nphi:prob.nphi + prob.nq][None, :]
        regq = np.zeros((prob.nq, prob.nq)); i = prob.nel - 1
        for t, (n, e) in enumerate(prob.ext_labels_q):
            if abs(e - (alpha + 1)) > 1e-9:
                regq[prob.off_q[i] - prob.nphi + t, prob.off_q[i] - prob.nphi + t] = self.reg_ext
        A = np.concatenate([Aq, self.Jq_int, regq, pin], 0); b = np.zeros(A.shape[0]); b[-1] = self.w_pin
        cq = self._lstsq(A, b)
        q_res = np.linalg.norm(Aq @ cq); q_scale = np.linalg.norm(np.concatenate([nd[i]["wq"] * np.abs(nd[i]["Bq0"] @ cq[prob.off_q[i] - prob.nphi:prob.off_q[i + 1] - prob.nphi]) for i in range(prob.nel)]))
        # etahat
        rhs = []
        for i in range(prob.nel):
            c_i = cq[prob.off_q[i] - prob.nphi:prob.off_q[i + 1] - prob.nphi]
            rhs.append(nd[i]["we"] * 2 * (nd[i]["Bq0"] @ c_i) * (nd[i]["fz"] @ c_i))
        Ae = np.zeros((sum(r.shape[0] for r in rows_e), int(self.off_eta[-1]))); r0 = 0
        for i, r_ in enumerate(rows_e):
            Ae[r0:r0 + r_.shape[0], self.off_eta[i]:self.off_eta[i + 1]] = r_; r0 += r_.shape[0]
        rege = np.zeros((int(self.off_eta[-1]), int(self.off_eta[-1])))
        for t, (n, e) in enumerate(self.lab_eta):
            if abs(e - (alpha + 2)) > 1e-9:
                rege[self.off_eta[-2] + t, self.off_eta[-2] + t] = self.reg_ext
        A = np.concatenate([Ae, self.Je_int, rege], 0); b = np.concatenate([np.concatenate(rhs), np.zeros(self.Je_int.shape[0] + rege.shape[0])])
        ce = self._lstsq(A, b)
        e_res = np.linalg.norm(Ae @ ce - np.concatenate(rhs)); e_scale = max(np.linalg.norm(np.concatenate(rhs)), 1e-300)
        # Phi = Delta_5^{-1}(-etahat)
        def eta_func(R, mu):
            R = np.asarray(R, float); mu = np.asarray(mu, float); out = np.zeros_like(R)
            for i, e in enumerate(prob.elements):
                lo = e.Rlo if i > 0 else -1.0
                m = (R > lo) & (R <= e.Rhi) if i < prob.nel - 1 else (R > lo)
                if np.any(m):
                    out[m] = self._Beta_at(i, R[m], mu[m])[(0, 0)] @ ce[self.off_eta[i]:self.off_eta[i + 1]]
            return out
        edges = [0.0, 0.25 * prob.cfg.R1, prob.cfg.R1] + [e.Rhi for e in prob.elements[1:-1]]
        gs = pressure.PressureSolver(eta_func, edges, 1e6 * prob.Rm, self.lmax, 2 * prob.cfg.nmax + 12, dim=5)
        Phi = []; fit_err = 0.0
        for i, e in enumerate(prob.elements):
            vals = gs.evaluate(e.R, e.mu)["P"]
            A0 = e.B[(0, 0)][:, prob.cols_phi[i]]
            c = self._lstsq(A0, vals)
            fit_err = max(fit_err, float(np.max(np.abs(A0 @ c - vals))) / max(float(np.max(np.abs(vals))), 1e-300))
            Phi.append(c)
        Rz = max(abs(z0), 1e-12); muz = 1.0 if z0 >= 0 else -1.0
        Phi_z = float(gs.evaluate(np.array([Rz]), np.array([muz]))["P_z"][0])
        self.n_evals += 1
        self.last = dict(z0=z0, q_rel=q_res / max(q_scale, 1e-300), eta_rel=e_res / e_scale, fit_err=fit_err, Phi_z=Phi_z, cq=cq, ce=ce)
        return Phi, cq, z0

    def pack(self, cphi_all, q0):
        return np.concatenate(cphi_all + [np.array([q0])])

    def unpack(self, y):
        prob = self.prob
        cphi = [y[prob.off_phi[i]:prob.off_phi[i + 1]] for i in range(prob.nel)]
        return cphi, float(y[-1])

    def set_cl(self, cl):
        """Change c_l: rebuild the exterior exponents of the problem and the eta exterior basis."""
        prob = self.prob
        prob.set_cl(float(cl)); self.cl = prob.cl; self.alpha = prob.alpha
        ext = prob.elements[-1]
        self.eta_exps = [e + 2.0 for e in sorted(set(ex for (n, ex) in prob.ext_labels_phi))]
        self.Beta_ext, self.lab_eta = basis.build_B("exterior", ext.Rlo, ext.Rhi, ext.nmax, dict(ext.params, exponents=self.eta_exps), ext.R, ext.mu)
        self.Jq_int = self._interface_rows(self._Bq_at, lambda i: prob.cols_q[i], prob.off_q - prob.nphi, prob.nq)
        self.Je_int = self._interface_rows(self._Beta_at, lambda i: np.arange(self.n_eta[i]), self.off_eta, int(self.off_eta[-1]))

    def F(self, y):
        cphi, last = self.unpack(y)
        if self.unknown == "cl":
            self.set_cl(min(max(last, 0.501), 0.749)); q0 = self.q0_fixed
        else:
            q0 = last
        Phi, cq, z0 = self.evaluate(cphi, q0)
        res = [cphi[i] - q0 * q0 * Phi[i] for i in range(self.prob.nel)]
        phi0, phiz = self.phi_axis(cphi, z0)
        return np.concatenate(res + [np.array([phiz - 0.5])])

    def solve(self, cphi0, q0, maxiter=20, f_tol=1e-9, inner_maxiter=40, verbose=True):
        y0 = self.pack([np.asarray(c, float) for c in cphi0], q0)
        hist = []
        t0 = time.time()

        def cb(y, f):
            cphi, q0 = self.unpack(y)
            if self.unknown == "cl":
                q0 = self.q0_fixed
            self.z0 = self.last.get("z0", self.z0)
            rec = dict(it=len(hist), Fnorm=float(np.linalg.norm(f)), q0=q0, z0=self.last.get("z0"), q_rel=self.last.get("q_rel"), eta_rel=self.last.get("eta_rel"),
                       Phi_z=self.last.get("Phi_z"), fit_err=self.last.get("fit_err"), n_evals=self.n_evals, t=time.time() - t0)
            hist.append(rec)
            if verbose:
                self.log(f"NK it {rec['it']:3d} |F| {rec['Fnorm']:.3e} q0 {q0:.5f} cl {self.cl:.6f} z0 {rec['z0']:+.5f} q-eig rel {rec['q_rel']:.2e} eta rel {rec['eta_rel']:.2e} Phi_z {rec['Phi_z']:+.4f} fit {rec['fit_err']:.1e} evals {self.n_evals} {rec['t']:.0f}s")
        try:
            y = newton_krylov(self.F, y0, method="lgmres", maxiter=maxiter, f_tol=f_tol, inner_maxiter=inner_maxiter, callback=cb, verbose=False, line_search="armijo")
            status = "converged"
        except Exception as ex:          # NoConvergence carries the last iterate
            y = getattr(ex, "args", [y0])[0] if hasattr(ex, "args") and len(ex.args) and isinstance(ex.args[0], np.ndarray) else y0
            status = f"stopped: {type(ex).__name__}"
        return dict(y=y, hist=hist, status=status, Fnorm=float(np.linalg.norm(self.F(y))))
