"""Levenberg-Marquardt with dense Jacobian built by chunked forward-mode AD (torch.func.jvp under vmap).
Normal equations (J^T J + lam * diag(J^T J)) dz = -J^T r solved by Cholesky (float64).  Suitable for up to ~1e4
unknowns; the residual count may be ~1e5-1e6."""
from __future__ import annotations
import math, time
import torch


def jacobian_fwd(fun, z, chunk=128):
    """Dense Jacobian (Nres, N) by chunked forward-mode AD (torch.func.jvp under vmap over `chunk` directions). Since 2026-10-25T15:57Z the result
    is preallocated and filled chunk by chunk (no torch.cat of the chunk list): the former cat doubled the peak memory of the stored J, which
    OOMed the L10 smoke (43.5 GB requested with 44.8 GB already held). Same values, same order."""
    N = z.numel()
    J = None
    for s in range(0, N, chunk):
        n = min(chunk, N - s)
        E = torch.zeros(n, N, dtype=z.dtype, device=z.device)
        E[torch.arange(n), torch.arange(s, s + n)] = 1.0
        def jv(e):
            return torch.func.jvp(fun, (z,), (e,))[1]
        Jc = torch.func.vmap(jv)(E)            # (n, Nres)
        if J is None:
            J = torch.empty(Jc.shape[1], N, dtype=Jc.dtype, device=Jc.device)
        J[:, s:s + n] = Jc.T
        del Jc, E
    return J


def jtj_split(fun, z, r_main, chunk=128, n_blocks=2, scalar_rows=None, r_scalar=None, scale_rows=None):
    """A = J^T J and g = J^T r for the dense Jacobian J of fun at z, accumulated in n_blocks COLUMN blocks so that at most
    ceil(N/n_blocks) columns of J are stored at once (memory J/n_blocks instead of J; cost (n_blocks+1)/2 Jacobian builds:
    block i is built and kept while the blocks j > i are rebuilt chunk by chunk for the off-diagonal blocks A[j, i]).
    The same A and g as the dense path up to the summation order of the matmuls (roundoff); the LM step is unchanged.
    Added 2026-10-25T16:10Z for L10 with SPEC-degree channels (J about 46 GB at L10 Nk24, which does not fit beside the
    model on an 80 GB GPU; n_blocks = 2 stores 23 GB). scalar_rows: appended scalar residual rows (reverse-mode gradients, as
    in the dense path) with their residual values r_scalar; fd_cols are not supported here (free parameters: use n_blocks = 1)."""
    N = z.numel()
    nb = max(1, min(int(n_blocks), N))
    bounds = [(N * b) // nb for b in range(nb + 1)]
    A = torch.zeros(N, N, dtype=z.dtype, device=z.device)
    g = torch.zeros(N, dtype=z.dtype, device=z.device)
    Dp = torch.zeros(N, dtype=z.dtype, device=z.device) if scale_rows is not None else None   # column norms over the first scale_rows rows (PDE-row Marquardt scaling)

    def jv(e):
        return torch.func.jvp(fun, (z,), (e,))[1]

    def col_chunks(s0, s1):
        for s in range(s0, s1, chunk):
            n = min(chunk, s1 - s)
            E = torch.zeros(n, N, dtype=z.dtype, device=z.device)
            E[torch.arange(n), torch.arange(s, s + n)] = 1.0
            Jc = torch.func.vmap(jv)(E)            # (n, Nres)
            del E
            yield s, s + n, Jc
            del Jc

    for i in range(nb):
        a0, a1 = bounds[i], bounds[i + 1]
        if a1 <= a0:
            continue
        Ji = None
        for cs, ce, Jc in col_chunks(a0, a1):
            if Ji is None:
                Ji = torch.empty(Jc.shape[1], a1 - a0, dtype=Jc.dtype, device=Jc.device)
            Ji[:, cs - a0:ce - a0] = Jc.T
            if Dp is not None:
                Dp[cs:ce] = (Jc[:, :scale_rows] ** 2).sum(1)
        A[a0:a1, a0:a1] = Ji.T @ Ji
        g[a0:a1] = Ji.T @ r_main
        for j in range(i + 1, nb):
            b0, b1 = bounds[j], bounds[j + 1]
            for cs, ce, Jc in col_chunks(b0, b1):
                blk = Jc @ Ji                      # (n, a1 - a0) = J[:, cs:ce]^T J[:, a0:a1]
                A[cs:ce, a0:a1] = blk
                A[a0:a1, cs:ce] = blk.T
                del blk
        del Ji
    if scalar_rows:
        for f, rs in zip(scalar_rows, r_scalar):
            zz = z.detach().clone().requires_grad_(True)
            val = f(zz); gr, = torch.autograd.grad(val, zz); gr = gr.detach()
            A += gr[:, None] * gr[None, :]
            g += gr * rs
    return (A, g) if Dp is None else (A, g, Dp)


def jacobian_fd(fun, z, h=1e-6):
    """Reference central-difference Jacobian (for tests only)."""
    N = z.numel(); r0 = fun(z)
    J = torch.zeros(r0.numel(), N, dtype=z.dtype, device=z.device)
    for k in range(N):
        e = torch.zeros_like(z); e[k] = h
        J[:, k] = (fun(z + e) - fun(z - e)) / (2 * h)
    return J


def lm_solve(fun, z0, max_iter=100, lam0=1e-2, lam_min=1e-12, lam_max=1e10, ftol=1e-14, xtol=1e-14,
             gtol=0.0, chunk=128, callback=None, log=None, bounds=None, time_limit=None, verbose=True, scale_rows=None, project=None,
             fd_cols=None, fd_fun=None, fd_h=1e-5, scalar_rows=None, eval_fun=None, jtj_blocks=1):
    """scalar_rows: optional list of functions z -> scalar residual (e.g. the Sigma_Z row evaluated on a fine grid); they are
    appended to fun(z) and their Jacobian rows come from reverse-mode gradients (one backward pass each) instead of the
    forward-mode vmap, which would multiply the memory of their field evaluation by the chunk size."""
    """Minimize 0.5 |fun(z)|^2.  bounds: optional (lo, hi) tensors (projected after each accepted step).
    scale_rows: if given, the Marquardt scaling D = diag(J^T J) uses only the first scale_rows residual rows (optional).
    project: optional exact symmetry projection z -> z applied after every accepted step (e.g. azimuthal phase alignment).
    fd_cols/fd_fun: replace the Jacobian columns fd_cols by central differences of fd_fun (a residual function that rebuilds
    every parameter-dependent discretization, e.g. the pressure kernels, at the perturbed parameters; SPEC 4.5).
    eval_fun: complete residual (main + scalar rows, same length as the Jacobian rows) used for the base and every trial cost; for
    free parameters this is the rebuilt-discretization residual, so base, trials and the fd columns share one discretization path.
    jtj_blocks: > 1 accumulates J^T J and J^T r in column blocks without storing the whole Jacobian (jtj_split; same step up to
    roundoff; memory J/jtj_blocks, time (jtj_blocks+1)/2 Jacobian builds). Not combinable with fd_cols.
    Returns dict(z, cost, history, status)."""
    base_fun = fun
    if scalar_rows:
        def fun(zz, _b=base_fun):
            return torch.cat([_b(zz), torch.stack([f(zz) for f in scalar_rows])])
    # eval_fun, when given, is ALWAYS the complete residual (same rows as the Jacobian: main rows + scalar rows); nothing is appended
    ev_fun = eval_fun if eval_fun is not None else fun
    z = z0.clone()
    if project is not None:
        z = project(z)
    r = ev_fun(z); cost = 0.5 * (r @ r).item()
    lam = lam0
    hist = []
    status = "max_iter"
    t_start = time.time()
    for it in range(max_iter):
        t0 = time.time()
        if jtj_blocks > 1:
            if fd_cols:
                raise ValueError("jtj_blocks > 1 (split J^T J accumulation) does not support fd_cols (free parameters): use jtj_blocks = 1")
            n_sc = len(scalar_rows) if scalar_rows else 0
            n_main = r.numel() - n_sc
            Dp = None
            if scale_rows is not None and scale_rows < r.numel():
                A, g, Dp = jtj_split(base_fun, z, r[:n_main], chunk=chunk, n_blocks=jtj_blocks, scalar_rows=scalar_rows, r_scalar=(r[n_main:] if n_sc else None), scale_rows=min(scale_rows, n_main))
            else:
                A, g = jtj_split(base_fun, z, r[:n_main], chunk=chunk, n_blocks=jtj_blocks, scalar_rows=scalar_rows, r_scalar=(r[n_main:] if n_sc else None))
            J = None
        else:
            if scalar_rows:
                Jm = jacobian_fwd(base_fun, z, chunk=chunk)
                grads = []
                for f in scalar_rows:
                    zz = z.detach().clone().requires_grad_(True)
                    val = f(zz); gr, = torch.autograd.grad(val, zz)
                    grads.append(gr.detach())
                J = torch.cat([Jm, torch.stack(grads, 0)], 0)
                del Jm, grads                                  # the stacked copy must not coexist with its parts beyond this point
            else:
                J = jacobian_fwd(fun, z, chunk=chunk)
            if fd_cols:
                for k in fd_cols:
                    e = torch.zeros_like(z); h = fd_h * max(1.0, abs(z[k].item())); e[k] = h
                    J[:, k] = (fd_fun(z + e) - fd_fun(z - e)) / (2 * h)
            A = J.T @ J
            g = J.T @ r
        gnorm = g.abs().max().item()
        if J is None and jtj_blocks > 1 and Dp is not None:
            D = Dp.clamp_min(1e-30); D = torch.maximum(D, 1e-12 * D.max())
        elif J is not None and scale_rows is not None and scale_rows < J.shape[0]:
            Js = J[:scale_rows]
            D = (Js * Js).sum(0).clamp_min(1e-30)
            D = torch.maximum(D, 1e-12 * D.max())
        else:
            D = torch.diagonal(A).clamp_min(1e-30)
        J = None                                               # 2026-10-25T16:20Z: free the stored Jacobian before the trial evaluations and the next build (the L10 OOM of 16:13Z was the SECOND J allocated while the first was still bound)
        accepted = False
        tj = time.time() - t0
        while True:
            M = A + lam * torch.diag(D)
            try:
                Lc = torch.linalg.cholesky(M)
                dz = -torch.cholesky_solve(g[:, None], Lc)[:, 0]
            except RuntimeError:
                lam = lam * 10
                if lam > lam_max:
                    break
                continue
            z_new = z + dz
            if bounds is not None:
                z_new = torch.maximum(torch.minimum(z_new, bounds[1]), bounds[0])
            r_new = ev_fun(z_new); cost_new = 0.5 * (r_new @ r_new).item()
            if math.isfinite(cost_new) and cost_new < cost and project is not None:
                # exact symmetry projection: the cost is invariant but the residual vector (on the fixed grid) is not;
                # re-evaluate so that the cached residual belongs to the projected state
                z_new = project(z_new); r_new = ev_fun(z_new); cost_new = 0.5 * (r_new @ r_new).item()
            if math.isfinite(cost_new) and cost_new < cost:
                # gain ratio
                pred = -(g @ dz).item() - 0.5 * (dz @ (A @ dz)).item()
                rho = (cost - cost_new) / max(pred, 1e-300)
                accepted = True
                step = dz.norm().item() / max(z.norm().item(), 1e-300)
                rel_dec = (cost - cost_new) / max(cost, 1e-300)
                z, r, cost_old, cost = z_new, r_new, cost, cost_new
                lam = max(lam * (0.3 if rho > 0.75 else 0.7), lam_min)
                break
            else:
                lam = lam * 4
                if lam > lam_max:
                    break
        rec = dict(it=it, cost=cost, rms=math.sqrt(2 * cost / max(r.numel(), 1)), lam=lam, gnorm=gnorm, accepted=accepted,
                   t_jac=tj, t_iter=time.time() - t0, elapsed=time.time() - t_start)
        hist.append(rec)
        if verbose and (it % 5 == 0 or not accepted):
            msg = f"  LM it {it:4d} cost {cost:.6e} rms {rec['rms']:.3e} lam {lam:.1e} |g| {gnorm:.2e} tjac {tj:.2f}s"
            print(msg, flush=True)
            if log is not None:
                log(msg)
        if callback is not None:
            changed = callback(it, z, cost, rec)
            if isinstance(changed, dict):                      # 2026-10-26 (safeguarded refresh, lead d128 CV 4): the callback may restart the damping
                if changed.get("lam") is not None:
                    lam = float(changed["lam"]); rec["lam"] = lam
                changed = bool(changed.get("changed", True))
            if changed:
                # the objective (weights, pressure kernels) changed: refresh the cached residual and cost before the next
                # Jacobian so that J^T r, the trust-region comparison and the reported cost are consistent
                r = ev_fun(z); cost = 0.5 * (r @ r).item()
                rec["cost_after_reweight"] = cost
        if not accepted:
            status = "stalled"
            break
        if rel_dec < ftol and it > 2:
            status = "ftol"
            break
        if step < xtol:
            status = "xtol"
            break
        if gnorm < gtol:
            status = "gtol"
            break
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"
            break
    return dict(z=z, cost=cost, rms=math.sqrt(2 * cost / max(r.numel(), 1)), history=hist, status=status, lam=lam)


def lbfgs_solve(fun, z0, max_iter=500, history_size=50, lr=1.0, callback=None, log=None, time_limit=None, verbose=True, tol=1e-30):
    """Second optimizer for comparison: torch L-BFGS (strong Wolfe) on 0.5 |fun(z)|^2 with exact gradients."""
    z = z0.clone().requires_grad_(True)
    opt = torch.optim.LBFGS([z], lr=lr, max_iter=20, history_size=history_size, line_search_fn="strong_wolfe", tolerance_grad=1e-14, tolerance_change=1e-16)
    hist = []; t_start = time.time(); status = "max_iter"
    cost = 0.5 * (fun(z.detach()) ** 2).sum().item()
    for it in range(max_iter // 20):
        t0 = time.time()
        def closure():
            opt.zero_grad()
            r = fun(z)
            c = 0.5 * (r @ r)
            c.backward()
            return c
        opt.step(closure)
        with torch.no_grad():
            r = fun(z.detach()); cost_new = 0.5 * (r @ r).item()
        rec = dict(it=(it + 1) * 20, cost=cost_new, rms=math.sqrt(2 * cost_new / r.numel()), t_iter=time.time() - t0, elapsed=time.time() - t_start, lam=0.0, gnorm=float(z.grad.abs().max()) if z.grad is not None else 0.0, accepted=cost_new <= cost)
        hist.append(rec)
        if verbose:
            msg = f"  LBFGS it {rec['it']:4d} cost {cost_new:.6e} rms {rec['rms']:.3e} |g| {rec['gnorm']:.2e}"
            print(msg, flush=True)
            if log is not None: log(msg)
        if callback is not None:
            callback(rec['it'], z.detach(), cost_new, rec)
        rel = (cost - cost_new) / max(cost, 1e-300)
        cost = cost_new
        if rel < 1e-7 and it > 2:
            status = "ftol"; break
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"; break
    return dict(z=z.detach(), cost=cost, rms=math.sqrt(2 * cost / max(fun(z.detach()).numel(), 1)), history=hist, status=status, lam=0.0)


# ======================================================================================================================
# D6FP (degree-6 free-parameter campaign, 2026-10-28): Levenberg-Marquardt with exact AD parameter columns and a
# self-consistent acceptance test (SPEC 2.3, 4.3, 5.5). The frozen lm_solve above is kept unchanged for regression tests.
# ======================================================================================================================
def param_columns(param_fun, z, param_idx):
    """Exact forward-mode columns d(param_fun)/dz[k] for k in param_idx (plain jvp, one direction at a time; the function may build
    the parameter-dependent pressure tables inside the differentiated graph)."""
    cols = []
    for k in param_idx:
        e = torch.zeros_like(z); e[k] = 1.0
        cols.append(torch.func.jvp(param_fun, (z,), (e,))[1])
    return torch.stack(cols, 1)


def lm_solve_free(fun, z0, param_fun=None, param_idx=(), objective=None, commit=None, project=None, phys=None, relayout=None,
                  max_iter=100, lam0=1e-2, lam_min=1e-12, lam_max=1e10, ftol=1e-14, xtol=1e-14, gtol=0.0, chunk=128,
                  callback=None, log=None, time_limit=None, verbose=True, param_step_max=None, grad_fun=None, jac_hook=None,
                  lam_up=4.0, lam_down=(0.3, 0.7), min_gain_ratio=0.0, saturation=None, saturation_patience=50, log_every=1, param_scale_rows=None, lag_jacobian=None, grad_every=1, counters=None, project_start=True):
    """Minimize O1(z) = 0.5 |objective(z)|^2.
    counters (gpu_v1, SPEC v1.13 3.6 (d), V161): dict(n_acc, n_rej, sat_count) of a resumed run; the cumulative counters continue from it (they drive the
    complete-gradient schedule and the saturation patience) and are returned in the result and in every iteration record (rec['counters']).
    project_start (gpu_v1, V162): apply the entry projection to the start vector (fresh starts); False on resume, so that the first resumed objective
    and Jacobian use the checkpointed vector byte for byte. Trial projections are unchanged.
    grad_every (D6FP 2026-10-29, lead rule R5): the complete gradient grad_fun is evaluated at every accepted step taken with a FRESH Jacobian and
    at least at every grad_every-th accepted step (counted over the run); at the other accepted steps the record states that it was skipped.
    grad_every = 1 (default) evaluates it at every accepted step.
    fun(z): residual with the committed base discretization (pressure tables, lagged nonlinear weights, lagged closure target):
            vmap-able; gives the coefficient columns of the frozen-weight Jacobian J_f.
    param_fun(z): the same residual with the pressure tables built from z's own parameters inside the graph (jvp-able); the
            columns param_idx of J_f are taken from it (exact parameter derivative including the kernel tables, SPEC 2.3).
    objective(z) -> (r, aux): the SELF-CONSISTENT residual at z (fresh tables on the current layout, weights and closure target at z);
            the only function used for base and trial costs (SPEC 4.3).  commit(aux): installs aux as the base discretization.
    project(z): exact symmetry projection applied to every trial point before its evaluation (cost invariant).
    phys(z) -> dict with the physical parameters (c_l, omega, chain-rule factors) for the records.
    relayout(z) -> (changed: bool, info): after an accepted step, rebuild the quadrature layout if the parameters left its margins;
            when changed, the base objective is re-evaluated on the new layout and the relative jump is recorded (SPEC 2.5).
    param_step_max: dict {index: max |step|} in optimizer coordinates (SPEC 5.5); a violating trial is rejected ('param_trust').
    grad_fun(z) -> complete gradient of O1 (weights and closure target differentiated), recorded at accepted iterates (SPEC 7.1).
    jac_hook(it, z, J, r, D, aux): called with the assembled Jacobian before it is released (linearization records).
    saturation(z) -> bool (SPEC 5.3); after saturation_patience consecutive flagged accepted iterations the run stops ('saturation').
    param_scale_rows: if given, the Marquardt scaling D of the PARAMETER columns uses only the first param_scale_rows residual rows (the PDE
            rows), not the gauge rows: the gauge row's parameter derivative is orders of magnitude larger than the PDE rows' (||F|| depends on
            alpha through R0^alpha), and full-column scaling damps the valley direction (coordinated coefficient-parameter motion) to nothing.
            A solver change only (SPEC 4.4); the objective is unchanged. Reported scaled gradients use the full column norms (SPEC 7.1).
    lag_jacobian (D6FP, lead 2026-10-29T01:11Z R2, solver option "lagJ"): None, or dict(max_reuse=8, rho_min=0.25). J_cw, its column scaling
            and its normal matrix are reused while steps are accepted with rho >= rho_min, for at most max_reuse consecutive reuses; rho is
            the actual decrease of the fresh self-consistent O1 divided by the decrease the (stale) linear model predicts at the FRESH residual
            (g = J^T r at the current point). A rejection or rho < rho_min with a stale J refreshes J at the current point before any damping
            increase. Acceptance and the parameter trust region are unchanged. Every record carries J_age (0 for a fresh J) and rho.
    Returns dict(z, cost, rms, history, status, lam, n_accepted, n_rejected)."""
    z = z0.clone()
    if project is not None and project_start:
        z = project(z)
    r, aux = objective(z); commit(aux)
    cost = 0.5 * float(r @ r); cost_start = cost
    if log:
        log(f"  LM initial cost {cost:.17e} at the start iterate (self-consistent O1; G7 compares it with the checkpointed record on resume)")   # D6FP 2026-10-29 (lead 02:48Z item 5)
    lam = float(lam0); hist = []; status = "max_iter"; t_start = time.time()
    n_acc = 0; n_rej = 0; sat_count = 0
    if counters:
        n_acc = int(counters.get("n_acc", 0)); n_rej = int(counters.get("n_rej", 0)); sat_count = int(counters.get("sat_count", 0))
        if log:
            log(f"  LM counters restored from the checkpoint: n_accepted {n_acc}, n_rejected {n_rej}, saturation streak {sat_count} (gpu_v1 resume path)")
    dev = z.device
    lag = lag_jacobian if lag_jacobian else None
    lag_max = int(lag.get("max_reuse", 8)) if lag else 0; lag_rho = float(lag.get("rho_min", 0.25)) if lag else 0.0
    J_keep = None; J_age = 0; force_fresh = True; last_rho = None
    for it in range(max_iter):
        t0 = time.time()
        fresh = (lag is None) or (J_keep is None) or force_fresh or (J_age >= lag_max) or (last_rho is None) or (last_rho < lag_rho)
        if fresh:
            # ---- Jacobian of the frozen-weight model J_f: coefficient columns by chunked vmap-jvp, parameter columns by exact jvp
            if dev.type == "cuda":
                torch.cuda.synchronize()
            J = jacobian_fwd(fun, z, chunk=chunk)
            if dev.type == "cuda":
                torch.cuda.synchronize()
            t_jac = time.time() - t0
            t1 = time.time()
            if param_fun is not None and len(param_idx) > 0:
                Jp = param_columns(param_fun, z, param_idx)
                for j, k in enumerate(param_idx):
                    J[:, k] = Jp[:, j]
                del Jp
            if dev.type == "cuda":
                torch.cuda.synchronize()
            t_pcols = time.time() - t1
            t2 = time.time()
            A = J.T @ J
            g = J.T @ r
            Dfull = torch.diagonal(A).clamp_min(1e-30)
            Dfull = torch.maximum(Dfull, 1e-12 * Dfull.max())
            colnorm = Dfull.sqrt()
            D = Dfull.clone()
            if param_scale_rows is not None and len(param_idx) > 0:
                for k in param_idx:
                    D[k] = max(float((J[:param_scale_rows, k] ** 2).sum()), 1e-30)
                D = torch.maximum(D, 1e-12 * D.max())
            D_param_full = {int(k): float(Dfull[k]) for k in param_idx}; D_param_damp = {int(k): float(D[k]) for k in param_idx}
            if jac_hook is not None:
                try:
                    jac_hook(it, z, J, r, colnorm, aux)
                except Exception as e:                       # a record failure never stops the optimization
                    if log is not None:
                        log(f"  jac_hook failed at it {it}: {e!r}")
            if lag is not None:
                J_keep = J; J_age = 0                         # lagJ: keep J for the stale-model gradient g = J^T r at later points
            J = None                                          # release the (local) Jacobian before the trial evaluations
            if dev.type == "cuda":
                torch.cuda.synchronize()
            t_normal = time.time() - t2
        else:
            # ---- lagJ: stale Jacobian (age J_age + 1); fresh residual gradient g = J^T r; A, scaling and damping diagonal reused
            J_age += 1; t_jac = 0.0; t_pcols = 0.0; t2 = time.time()
            g = J_keep.T @ r
            t_normal = time.time() - t2
        force_fresh = False; refresh_needed = False
        gnorm = float(g.abs().max()); rnorm = math.sqrt(2.0 * cost)
        gD = g / colnorm                                  # scaled gradient (Marquardt scaling), SPEC 7.1
        gD_inf = float(gD.abs().max()); gD_2 = float(gD.norm())
        gparam = {int(k): float(g[k]) for k in param_idx}
        gparam_scaled = {int(k): float(g[k] / (colnorm[k] * max(rnorm, 1e-300))) for k in param_idx}   # |J_p^T r| / (||J_p|| ||r||)
        # ---- trial loop
        accepted = False; rejections = []; t_solve = 0.0; t_trial = 0.0; n_trials = 0; rho = None; dz_acc = None; aux_new = None
        while True:
            ts = time.time()
            M = A + lam * torch.diag(D)
            try:
                Lc = torch.linalg.cholesky(M)
                dz = -torch.cholesky_solve(g[:, None], Lc)[:, 0]
                t_solve += time.time() - ts
            except RuntimeError as e:
                t_solve += time.time() - ts
                rejections.append(dict(reason="cholesky_failure", lam=lam))
                if lag is not None and not fresh:
                    rejections[-1]["stale_J_refresh"] = True; refresh_needed = True; break
                lam = lam * 10.0
                if lam > lam_max:
                    break
                continue
            if param_step_max:
                viol = {int(k): float(dz[k]) for k, mx in param_step_max.items() if abs(float(dz[k])) > mx}
                if viol:
                    rejections.append(dict(reason="param_trust", lam=lam, steps=viol))
                    if lag is not None and not fresh:
                        rejections[-1]["stale_J_refresh"] = True; refresh_needed = True; break
                    lam = lam * lam_up
                    if lam > lam_max:
                        break
                    continue
            tt = time.time(); n_trials += 1
            z_new = z + dz
            if project is not None:
                z_new = project(z_new)
            try:
                r_new, aux_new = objective(z_new)
                cost_new = 0.5 * float(r_new @ r_new)
            except RuntimeError as e:                     # e.g. pressure quadrature overflow at an extreme trial point
                cost_new = float("nan"); r_new = None; aux_new = None
                rejections.append(dict(reason="evaluation_error", lam=lam, error=repr(e)[:200]))
            t_trial += time.time() - tt
            if r_new is None:
                if lag is not None and not fresh:
                    rejections[-1]["stale_J_refresh"] = True; refresh_needed = True; break
                lam = lam * lam_up
                if lam > lam_max:
                    break
                continue
            pred = -float(g @ dz) - 0.5 * float(dz @ (A @ dz))
            if not math.isfinite(cost_new):
                rejections.append(dict(reason="non_finite", lam=lam, cost_new=cost_new))
            elif cost_new >= cost:
                rejections.append(dict(reason="increase", lam=lam, cost_new=cost_new, pred_decrease=pred))
            elif pred > 0 and (cost - cost_new) / pred < min_gain_ratio:
                rejections.append(dict(reason="gain_ratio", lam=lam, cost_new=cost_new, gain_ratio=(cost - cost_new) / pred))
            else:
                rho = (cost - cost_new) / max(pred, 1e-300)
                accepted = True
                dz_acc = (z_new - z)
                step = float(dz_acc.norm() / max(float(z.norm()), 1e-300))
                rel_dec = (cost - cost_new) / max(cost, 1e-300)
                z, r, cost_old, cost = z_new, r_new, cost, cost_new
                commit(aux_new); aux = aux_new
                lam = max(lam * (lam_down[0] if rho > 0.75 else lam_down[1]), lam_min)
                break
            if lag is not None and not fresh:                 # lagJ: a rejection with a stale J refreshes J before any damping increase
                rejections[-1]["stale_J_refresh"] = True; refresh_needed = True; break
            lam = lam * lam_up
            if lam > lam_max:
                break
        n_acc += int(accepted); n_rej += len(rejections)
        if lag is not None:
            if refresh_needed:
                force_fresh = True
            if accepted:
                last_rho = rho
                if rho < lag_rho:
                    force_fresh = True
        rec = dict(it=it, cost=cost, rms=math.sqrt(2 * cost / max(r.numel(), 1)), lam=lam, gnorm=gnorm, D_param_full=D_param_full, D_param_damping=D_param_damp, gD_inf_over_r=gD_inf / max(rnorm, 1e-300),
                   gD_scaling=("J_cw column norms at the pre-step point (lagged-closure model scaling, jacobian_kind J_cw; not a section 7.1 quantity)" if fresh else "REUSED J (lagJ): gD values are from a stale J, not reported"),
                   gD_2_over_r=gD_2 / max(rnorm, 1e-300), g_param_opt=gparam, g_param_scaled=gparam_scaled, accepted=accepted, n_trials=n_trials,
                   rejections=rejections, t_jac=t_jac, t_param_cols=t_pcols, t_normal=t_normal, t_solve=t_solve, t_trial=t_trial,
                   t_iter=time.time() - t0, elapsed=time.time() - t_start, J_age=int(J_age if (lag is not None and not fresh) else 0), J_fresh=bool(fresh), lag_jacobian=bool(lag is not None), rho=rho)
        if accepted:
            rec.update(gain_ratio=rho, step_rel=step, rel_decrease=rel_dec, cost_prev=cost_old,
                       dparam_opt={int(k): float(dz_acc[k]) for k in param_idx})
        if phys is not None:
            rec["params"] = phys(z)                                   # the NEW point (after an accepted step)
            if accepted and dz_acc is not None:
                rec["params_prestep"] = phys(z - dz_acc)             # the pre-step point: the frozen-model gradient g = J^T r of this record belongs to it (verifier V130)
            else:
                rec["params_prestep"] = rec["params"]
        if accepted:
            # layout check (SPEC 2.5): rebuild the quadrature layout when the parameters left its margins; record the objective jump
            if relayout is not None:
                try:
                    changed, info = relayout(z)
                except Exception as e:
                    changed, info = False, dict(error=repr(e))
                if changed:
                    r2, aux2 = objective(z); commit(aux2); aux = aux2
                    cost2 = 0.5 * float(r2 @ r2)
                    rec["layout_change"] = dict(info=info, cost_before=cost, cost_after=cost2, rel_jump=abs(cost2 - cost) / max(cost, 1e-300))
                    if log is not None:
                        log(f"  LAYOUT CHANGE at it {it}: {info}; objective jump {rec['layout_change']['rel_jump']:.3e} relative")
                    r, cost = r2, cost2; rec["cost"] = cost
                    if lag is not None:
                        force_fresh = True; J_keep = None             # lagJ: the layout changed, the cached J, A and scaling are invalid (verifier V116)
            grad_due = (grad_fun is not None) and (fresh or int(grad_every or 1) <= 1 or (n_acc % int(grad_every) == 0))
            if grad_fun is not None and not grad_due:
                rec["complete_gradient"] = dict(skipped=True, policy=f"R5 spacing: evaluated at fresh-J steps and every {int(grad_every)} accepted steps; this step used a reused J (age {int(J_age)}) and n_accepted {int(n_acc)} is not a multiple of {int(grad_every)}", J_age_at_step=int(0 if fresh else J_age))
            if grad_due:
                try:
                    tg = time.time(); gc = grad_fun(z)
                    # SPEC 7.1 as ruled by the lead (2026-10-29T01:27Z, V122): the record states its point (the NEW iterate); the raw complete gradient,
                    # its parameter components and ||g|| are the 7.1 quantities. Scaled forms count only with D from J_c at the SAME point (the J_c
                    # records); a scaling whose column norms come from another point (the pre-step J_cw, or a reused J) is NOT recorded.
                    rec["complete_gradient"] = dict(point="new iterate (after the accepted step of this iteration)", g_param_opt={int(k): float(gc[k]) for k in param_idx},
                                                    g_inf=float(gc.abs().max()), g_2=float(gc.norm()), g_inf_over_r=float(gc.abs().max()) / max(math.sqrt(2 * cost), 1e-300), g_2_over_r=float(gc.norm()) / max(math.sqrt(2 * cost), 1e-300),
                                                    seconds=time.time() - tg, scaled_forms="not recorded: the column norms available here come from the pre-step J_cw (another point); see the J_c records (SPEC 7.0) for D^-1 g",
                                                    J_age_at_step=int(0 if fresh else J_age))
                    rec["complete_gradient"]["note"] = "complete gradient of O1 at the NEW iterate (fresh evaluation, exact closure route); the frozen-model gradient g = J_cw^T r of this record refers to the pre-step point"
                except Exception as e:
                    rec["complete_gradient"] = dict(error=repr(e)[:300])
            if saturation is not None:
                sat_count = sat_count + 1 if saturation(z) else 0
                rec["saturation_flag"] = sat_count > 0
        rec["counters"] = dict(n_acc=int(n_acc), n_rej=int(n_rej), sat_count=int(sat_count))      # cumulative over resumes (gpu_v1)
        hist.append(rec)
        if verbose and (it % log_every == 0 or not accepted):
            pp = rec.get("params") or {}
            msg = (f"  LM it {it:4d} cost {cost:.6e} rms {rec['rms']:.3e} lam {lam:.1e} |gD|/|r| {rec['gD_inf_over_r']:.2e} "
                   f"{'acc' if accepted else 'REJ'}({n_trials} trials) tjac {t_jac:.1f}s tpar {t_pcols:.1f}s ttrial {t_trial:.1f}s")
            if pp:
                msg += f" c_l {pp.get('c_l', float('nan')):.9f} omega {pp.get('omega', float('nan')):.9f}"
                if accepted and rec.get("dparam_opt"):
                    dp = list(rec["dparam_opt"].values()); msg += f" dz_c {dp[0]:+.2e} dz_w {dp[1]:+.2e}"
            if rec.get("complete_gradient") and "gD_inf_over_r" in rec["complete_gradient"]:
                _v = rec['complete_gradient'].get('g_inf_over_r'); msg += (f" |gc|/|r| {_v:.2e}" if _v is not None else "")
            print(msg, flush=True)
            if log is not None:
                log(msg)
        if callback is not None:
            changed = callback(it, z, cost, rec)
            if changed:
                r, aux = objective(z); commit(aux); cost = 0.5 * float(r @ r); rec["cost_after_callback"] = cost
                if lag is not None:
                    force_fresh = True; J_keep = None                 # lagJ: the objective changed under the callback, the cached J is invalid (verifier V116)
        if not accepted:
            if lag is not None and refresh_needed:                    # lagJ: a rejection with a stale J: retry at the same point with a fresh J before any damping change
                if time_limit is not None and time.time() - t_start > time_limit:
                    status = "time_limit"; break
                continue
            status = "stalled"; break
        if sat_count >= saturation_patience:
            status = "saturation"; break
        if rel_dec < ftol and it > 2:
            status = "ftol"; break
        if step < xtol:
            status = "xtol"; break
        if gnorm < gtol:
            status = "gtol"; break
        if time_limit is not None and time.time() - t_start > time_limit:
            status = "time_limit"; break
    return dict(z=z, cost=cost, cost_start=cost_start, rms=math.sqrt(2 * cost / max(r.numel(), 1)), history=hist, status=status, lam=lam, n_accepted=n_acc, n_rejected=n_rej,
                counters=dict(n_acc=int(n_acc), n_rej=int(n_rej), sat_count=int(sat_count)))
