"""Optimizers: Levenberg-Marquardt (dense Gauss-Newton with Marquardt scaling) and torch L-BFGS.

Both minimize 0.5 ||r(x)||^2 for the weighted residual of problem.Problem.  The LM step solves
    (J^T J + lam * diag(J^T J) + eps I) dx = -J^T r
by Cholesky on the GPU; lam adapts with the gain ratio (0.3 / 0.7 / x4 schedule).  Progress is reported
through a callback; checkpointing is the caller's responsibility (worker.py) but the callback may raise
StopIteration to stop cleanly (used for SIGTERM and time limits).
"""
from __future__ import annotations

import math
import time
from typing import Callable, Optional

import torch

DT = torch.float64


class Stop(Exception):
    pass


def lm_solve(prob, x0, max_iter=200, lam0=1e-2, ftol=1e-10, xtol=1e-13, time_limit=None, callback=None,
             state=None, log=print, lam_max=1e12, cl_bounds=None, solver="chol"):
    """Return dict(x, cost, lam, it, history, status). `state` may hold {it, lam, history} to resume."""
    x = x0.detach().clone()
    it0 = 0
    lam = lam0
    history = []
    if state:
        it0 = state.get("it", 0)
        lam = state.get("lam", lam0)
        history = list(state.get("history", []))
    t_start = time.time()
    r = prob.residual(x)
    cost = 0.5 * float(r @ r)
    status = "max_iter"
    n = x.shape[0]
    eye = torch.eye(n, dtype=DT, device=x.device)
    it = it0
    while it < max_iter:
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"
            break
        t0 = time.time()
        J = prob.jacobian(x)
        g = J.T @ r
        H = J.T @ J
        d = torch.diagonal(H).clone()
        d = torch.clamp(d, min=1e-30)
        gnorm = float(torch.max(torch.abs(g)))
        accepted = False
        tries = 0
        while not accepted and tries < 12:
            tries += 1
            if solver == "qr":
                # least-squares step on the augmented system [J; sqrt(lam) diag(sqrt d)] dx = [-r; 0] by QR (no squaring of the
                # condition number, unlike the normal equations); column scaling by sqrt(d) first
                sd = torch.sqrt(d)
                Js = J / sd[None, :]
                Aug = torch.cat([Js, math.sqrt(lam) * torch.eye(n, dtype=DT, device=x.device)], 0)
                rhs = torch.cat([-r, torch.zeros(n, dtype=DT, device=x.device)])
                try:
                    Q, Rm_ = torch.linalg.qr(Aug, mode="reduced")
                    y = torch.linalg.solve_triangular(Rm_, (Q.T @ rhs)[:, None], upper=True)[:, 0]
                    dx = y / sd
                except Exception:
                    lam = min(lam * 10, lam_max)
                    continue
            else:
                A = H + lam * torch.diag(d) + 1e-14 * eye
                try:
                    L = torch.linalg.cholesky(A)
                    dx = torch.cholesky_solve(-g[:, None], L)[:, 0]
                except Exception:
                    lam = min(lam * 10, lam_max)
                    continue
            xn = x + dx
            if cl_bounds is not None and prob.cfg.free_cl:
                xn[prob.ix_cl] = torch.clamp(xn[prob.ix_cl], cl_bounds[0], cl_bounds[1])
            rn = prob.residual(xn)
            cn = 0.5 * float(rn @ rn)
            pred = -float(g @ dx) - 0.5 * float(dx @ (H @ dx))
            rho = (cost - cn) / pred if pred > 0 else -1.0
            if cn < cost and rho > 1e-4:
                accepted = True
                step = float(torch.norm(dx)) / max(1e-300, float(torch.norm(x)))
                x = xn
                rel_dec = (cost - cn) / max(cost, 1e-300)
                r = rn
                cost = cn
                if rho > 0.75:
                    lam = max(lam * 0.3, 1e-15)
                elif rho < 0.25:
                    lam = min(lam * 2.0, lam_max)
                else:
                    lam = max(lam * 0.7, 1e-15)
            else:
                lam = min(lam * 4.0, lam_max)
                if lam >= lam_max:
                    break
        it += 1
        dt = time.time() - t0
        rec = dict(it=it, cost=cost, rms=math.sqrt(2 * cost / r.shape[0]), lam=lam, gnorm=gnorm, accepted=accepted,
                   tries=tries, dt=dt, cl=prob.cl_of(x))
        history.append(rec)
        if log:
            log(f"LM it {it:4d} cost {cost:.6e} rms {rec['rms']:.3e} lam {lam:.2e} |g| {gnorm:.2e} tries {tries} dt {dt:.2f}s"
                + (f" cl {rec['cl']:.8f}" if prob.cfg.free_cl else ""))
        if callback is not None:
            try:
                callback(x, rec, history)
            except Stop:
                status = "stopped"
                break
        if not accepted:
            status = "lam_max"
            break
        if rel_dec < ftol and it - it0 > 3:
            status = "ftol"
            break
        if step < xtol:
            status = "xtol"
            break
        if not math.isfinite(cost):
            status = "nan"
            break
    return dict(x=x, cost=cost, lam=lam, it=it, history=history, status=status)


def lbfgs_solve(prob, x0, max_iter=500, history_size=50, time_limit=None, callback=None, log=print, tol_grad=1e-12):
    """torch L-BFGS with strong-Wolfe line search on 0.5||r||^2; gradient via reverse-mode autograd."""
    x = x0.detach().clone().requires_grad_(True)
    opt = torch.optim.LBFGS([x], lr=1.0, max_iter=20, history_size=history_size, line_search_fn="strong_wolfe",
                            tolerance_grad=tol_grad, tolerance_change=0.0)
    t_start = time.time()
    history = []
    status = "max_iter"
    it = 0

    def closure():
        opt.zero_grad()
        r = prob.residual(x)
        c = 0.5 * (r @ r)
        c.backward()
        return c

    while it < max_iter:
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"
            break
        t0 = time.time()
        c = opt.step(closure)
        it += 1
        with torch.no_grad():
            r = prob.residual(x)
            cost = 0.5 * float(r @ r)
        rec = dict(it=it, cost=cost, rms=math.sqrt(2 * cost / r.shape[0]), dt=time.time() - t0,
                   cl=prob.cl_of(x))
        history.append(rec)
        if log:
            log(f"LBFGS outer {it:4d} cost {cost:.6e} rms {rec['rms']:.3e} dt {rec['dt']:.2f}s")
        if callback is not None:
            try:
                callback(x.detach(), rec, history)
            except Stop:
                status = "stopped"
                break
        if len(history) > 5 and abs(history[-5]["cost"] - cost) < 1e-12 * max(cost, 1e-300):
            status = "stalled"
            break
        if not math.isfinite(cost):
            status = "nan"
            break
    return dict(x=x.detach(), cost=cost, it=it, history=history, status=status)


def homotopy_solve(prob, x0, r_seed, dt0=0.1, dt_min=1e-3, max_iter_step=300, tol_rel=1e-10, time_limit=None, callback=None,
                   state=None, log=print, cl_bounds=None, lam0=1e-2):
    """Natural-parameter continuation in the forcing: solve r(x) - (1 - t) r_seed = 0 from t = 0 (x0 is an exact solution)
    to t = 1 (the unforced problem).  Each step: LM from the previous solution; a step is accepted when the cost falls below
    tol_rel^2 * 0.5 ||r_seed||^2 (round-off level relative to the seed residual); otherwise dt is halved.  If dt < dt_min
    the path is declared folded (or lost) at the current t.  Returns dict(x, t, cost, history, status, path).
    `state` may hold {t, dt, path} to resume; r_seed must be the seed residual (recomputed by the caller)."""
    x = x0.detach().clone()
    t = 0.0; dt = dt0; path = []
    if state:
        t = state.get("t", 0.0); dt = state.get("dt", dt0); path = list(state.get("path", []))
    t_start = time.time()
    cost_tol = 0.5 * (tol_rel * float(torch.norm(r_seed))) ** 2
    history = []
    status = "running"
    while t < 1.0 - 1e-15:
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"; break
        t_try = min(1.0, t + dt)
        prob.r_offset = (1.0 - t_try) * r_seed
        res = lm_solve(prob, x, max_iter=max_iter_step, lam0=lam0, ftol=1e-15, xtol=1e-15, log=None, cl_bounds=cl_bounds)
        ok = res["cost"] <= max(cost_tol, 1e-300) or (res["status"] in ("ftol", "xtol", "lam_max") and res["cost"] <= 1e4 * cost_tol)
        rec = dict(t=t_try, dt=dt, cost=res["cost"], it=res["it"], status=res["status"], accepted=bool(ok), cl=prob.cl_of(res["x"]),
                   z0=prob.z0_of(res["x"]), A=prob.amp_of(res["x"]))
        path.append(rec); history.extend(res["history"])
        if log:
            log(f"homotopy t={t_try:.5f} dt={dt:.2e} cost {res['cost']:.3e} (tol {cost_tol:.1e}) it {res['it']} {res['status']} -> {'ACCEPT' if ok else 'reject'}"
                + (f" cl {rec['cl']:.6f}" if prob.cfg.free_cl else "") + (f" A {rec['A']:.4f}" if prob.ix_a is not None else "") + f" z0 {rec['z0']}")
        if ok:
            x = res["x"]; t = t_try
            dt = min(2 * dt, 0.25)
            if callback is not None:
                try:
                    callback(x, dict(it=len(path), cost=res["cost"], lam=res["lam"], t=t, dt=dt), path)
                except Stop:
                    status = "stopped"; break
        else:
            dt *= 0.5
            if dt < dt_min:
                status = "fold"; break
    else:
        status = "reached_t1"
    prob.r_offset = None
    return dict(x=x, t=t, cost=(path[-1]["cost"] if path else float("nan")), history=history, status=status, path=path, dt=dt)


class VarProProblem:
    """Variable projection (lead note 25 item 5 (b)): the q coefficients are slaved to (phi, scalars) by the linear least-squares solve
    of all rows that are linear homogeneous in q at fixed phi (the PDE q rows, the q interface-continuity rows, the q Tikhonov rows and
    the q-correction slave rows), with the pin q(0, z0) = q0 as a hard row (null-space elimination), using the job's row weights.  The
    outer optimizer sees only the phi coefficients and the scalar unknowns (c_l, z0).
    residual(y) = full weighted residual at (phi, q*(phi)).
    jacobian(y) = J_outer + J_q dq*/dy with the reduced Jacobian of Golub and Pereyra in the form valid when the inner residual is at its
    floor: dq*/dphi = -N (A N)^+ G, G = d(inner rows)/dphi at (phi, q*); the term with the inner residual itself (A q*, at the floor
    1e-6 of the states tested) is dropped.  Scalar columns (c_l, z0) of dq*/dy by central differences of the inner solve.
    full=False gives Kaufman's cruder approximation used in the first test (dq*/dy dropped entirely; FAILURE_ANALYSIS 16).
    Exposes the attributes lm_solve uses (cfg, ix_cl, cl_of)."""
    def __init__(self, prob, full=True, fd_h=1e-6, trunc_rel=1e-4):
        import numpy as np
        self.p = prob; self.cfg = prob.cfg; self.full = full; self.fd_h = fd_h
        self.trunc_rel = trunc_rel      # truncated-SVD inner solve: singular directions of the column-scaled reduced operator below
                                        # trunc_rel * median(sigma) are dropped from q* AND from dq*/dphi.  Those directions (relative singular
                                        # values 1e-7 to 1e-4, scripts/q_eigen_nullspace.py) carry no part of q* (TSVD test, FAILURE_ANALYSIS
                                        # 17) but make q* hypersensitive to phi (gain 1/sigma), giving the reduced problem a curvature of
                                        # order 1e20 along the gradient and breaking the LM step (Cholesky and QR; Tikhonov on the scaled
                                        # coordinates destroys the pinned solution instead).  trunc_rel = 0 gives the plain least squares.
        self.last_n_dropped = 0
        self.outer = [i for i in range(prob.nx) if not (prob.nphi <= i < prob.nphi + prob.nq)]
        self.ix_cl = (self.outer.index(prob.ix_cl) if prob.ix_cl is not None else None)
        self.ix_z0 = (self.outer.index(prob.ix_z0) if prob.ix_z0 is not None else None)
        self.ix_a = None
        self.qcols = list(range(prob.nphi, prob.nphi + prob.nq))
        self.phi_outer = [k for k, i in enumerate(self.outer) if i < prob.nphi]          # positions (in y) of phi coefficients
        self.scalar_outer = [k for k, i in enumerate(self.outer) if i >= prob.nphi + prob.nq]
        # inner rows: PDE q rows, then q-only linear rows of Jint and Jreg, then the q-correction slave rows
        n0 = 0; rows = []
        for i in range(prob.nel):
            n = prob.n_nodes_per_el[i]; rows += list(range(n0, n0 + n)); n0 += 2 * n
        n_pde = n0
        Jint = prob.Jint.detach().cpu().numpy(); Jreg = prob.Jreg.detach().cpu().numpy()
        qmask = np.zeros(prob.nx, bool); qmask[self.qcols] = True
        for k in range(Jint.shape[0]):
            if np.any(Jint[k, qmask] != 0) and not np.any(Jint[k, ~qmask] != 0):
                rows.append(n_pde + k)
        for k in range(Jreg.shape[0]):
            if np.any(Jreg[k, qmask] != 0) and not np.any(Jreg[k, ~qmask] != 0):
                rows.append(n_pde + Jint.shape[0] + k)
        if prob.cfg.slave_correction:
            k0 = prob.n_rows - prob.n_slave_rows + len(prob.slave_corr_phi)
            rows += list(range(k0, prob.n_rows))
        self.inner = rows
        self.x_full = None; self.last_q_floor = None; self.n_inner_solves = 0
        assert prob.cfg.s1_constraint and prob.cfg.q0_pin is not None, "varpro needs the S1 rows and the q0 pin"

    def cl_of(self, y):
        return float(y[self.ix_cl]) if self.ix_cl is not None else self.p.cl

    def z0_of(self, y):
        return float(y[self.ix_z0]) if self.ix_z0 is not None else self.p.z0_of(self.embed(y))

    def amp_of(self, y):
        return 1.0

    def embed(self, y, q=None):
        x = torch.zeros(self.p.nx, dtype=DT, device=y.device)
        x[self.outer] = y
        if q is not None:
            x[self.qcols] = q
        elif self.x_full is not None:
            x[self.qcols] = self.x_full[self.qcols]
        return x

    def _pin(self, x):
        import numpy as np
        z0 = self.p.z0_of(x) or 0.0; q0 = self.p.cfg.q0_pin
        _, _, _, _, s_full, _ = self.p.axis_phi_rows(z0, with_q=True)
        s = s_full[self.p.nphi:self.p.nphi + self.p.nq]
        c_p = s * (q0 / float(s @ s))
        Q, _ = np.linalg.qr(s[:, None], mode="complete"); N = Q[:, 1:]
        return torch.tensor(c_p, dtype=DT, device=x.device), torch.tensor(N, dtype=DT, device=x.device)

    def solve_q(self, y, want_factors=False):
        """q*(phi, scalars): hard-pinned linear least squares of the inner rows (QR of the column-scaled reduced operator)."""
        x = self.embed(y)
        if self.p.cfg.free_cl:
            self.p.set_cl(float(x[self.p.ix_cl]))
        J = self.p.jacobian(x)
        A = J[self.inner][:, self.qcols]
        c_p, N = self._pin(x)
        AN = A @ N; b = -(A @ c_p)
        cs = torch.max(torch.abs(AN), dim=0).values; cs = torch.where(cs == 0, torch.ones_like(cs), cs)
        M = AN / cs[None, :]
        U, S, Vh = torch.linalg.svd(M, full_matrices=False)
        # threshold relative to the MEDIAN singular value: with max-abs column scaling the largest singular values belong to the heavily
        # weighted interface and slave rows (weights 1e3 to 1e5) and sigma_max is not representative of the transport operator
        s_ref = float(S[len(S) // 2])
        keep = S > self.trunc_rel * s_ref
        self.last_n_dropped = int((~keep).sum())
        Uk, Sk, Vk = U[:, keep], S[keep], Vh[keep].T
        yy = Vk @ ((Uk.T @ b) / Sk)
        q = c_p + N @ (yy / cs)
        r = A @ q; self.last_q_floor = float(torch.sqrt(torch.mean(r * r))); self.n_inner_solves += 1
        if want_factors:
            return q, dict(N=N, cs=cs, Uk=Uk, Sk=Sk, Vk=Vk)
        return q

    def residual(self, y):
        q = self.solve_q(y)
        self.x_full = self.embed(y, q)
        return self.p.residual(self.x_full)

    def jacobian(self, y):
        q, F = self.solve_q(y, want_factors=True)
        self.x_full = self.embed(y, q)
        J = self.p.jacobian(self.x_full)                         # at (phi, q*): G = d(inner rows)/d phi is exact here
        Jy = J[:, self.outer].clone()
        if not self.full:
            return Jy
        Jq = J[:, self.qcols]
        Dq = torch.zeros((self.p.nq, len(self.outer)), dtype=DT, device=y.device)
        G = J[self.inner][:, [self.outer[k] for k in self.phi_outer]]
        # dq*/dphi = -N diag(1/cs) V_k S_k^-1 U_k^T G  (truncated pseudo-inverse, consistent with the inner solve)
        T = F["Vk"] @ ((F["Uk"].T @ G) / F["Sk"][:, None])
        Dq[:, self.phi_outer] = -(F["N"] @ (T / F["cs"][:, None]))
        # scalar columns by central differences of the inner solve
        for k in self.scalar_outer:
            h = self.fd_h if k != self.ix_z0 else 1e-5
            yp = y.clone(); yp[k] += h; ym = y.clone(); ym[k] -= h
            qp = self.solve_q(yp); qm = self.solve_q(ym)
            Dq[:, k] = (qp - qm) / (2 * h)
        if self.p.cfg.free_cl:
            self.p.set_cl(self.cl_of(y))
        return Jy + Jq @ Dq
