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
