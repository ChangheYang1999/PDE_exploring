"""GPU-accelerated version of the lead's long_solve / long_solve_fixcl / long_solve_fixcl_ax (lead work/c6, work/c7),
numerics lane 2026-10-18. Same algorithm (one linearisation at a time, damped LSQR of Paige-Saunders with the lead's
stochastic column scaling, bounds, acceptance by the lead's own CPU objective s.fun at every --check iterations, shapes
saved by the lead's CentreShape.save), same shape files and the same .long.jsonl log format; only J v and J^T u inside LSQR
run on the GPU (gpu_op.GPUDerivative, validated against the CPU operator). The linearisation itself (CentreDerivative:
fields, k column by finite differences, centre rows) is the lead's CPU code.
Usage: python3 gpu_long_solve.py INPUT_shape.npz OUTPUT_shape.npz --nr 20480 --nt 720 --hours H [--inner 500] [--check 250]
       [--fix-cl] [--fit-radius FR] [--aweight A --ax0 0.3 --ax1 7.2 --ayw 0.3] [--pweight W --pwidth 3 --pcentre 8.60088]
       [--max-outer N] [--max-its K] [--reorth] [--damping 1e-8] [--probes 24]"""
import os, sys, json, time, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "b_fit_domain"))
import numpy as np
import torch
from centre_fit import load_shape, CentreDerivative
from gpu_op import GPUDerivative

ap = argparse.ArgumentParser()
ap.add_argument("input"); ap.add_argument("output")
ap.add_argument("--nr", type=int, default=4096); ap.add_argument("--nt", type=int, default=480)
ap.add_argument("--hours", type=float, default=1.0)
ap.add_argument("--inner", type=int, default=3000)
ap.add_argument("--check", type=int, default=150)
ap.add_argument("--damping", type=float, default=1e-8)
ap.add_argument("--probes", type=int, default=24)
ap.add_argument("--pweight", type=float, default=1.)
ap.add_argument("--pwidth", type=float, default=3.)
ap.add_argument("--pcentre", type=float, default=8.60088)
ap.add_argument("--fit-radius", type=float, default=None)
ap.add_argument("--inverse-radius", type=float, default=None, help="inverse domain R_shape (shape units) set independently of the fit radius (default: fit radius / 0.9, the lead's load_shape rule); with it the fit rows are r < --fit-radius (default 900)")
ap.add_argument("--fix-cl", action="store_true")
ap.add_argument("--aweight", type=float, default=1.)
ap.add_argument("--ax0", type=float, default=0.3)
ap.add_argument("--ax1", type=float, default=7.2)
ap.add_argument("--ayw", type=float, default=0.3)
ap.add_argument("--max-outer", type=int, default=10 ** 6)
ap.add_argument("--reorth", action="store_true", help="one-sided full reorthogonalisation (CGS2) of the right Lanczos vectors v against all previous v of the current linearisation (Simon and Zha 2000); memory ncol x inner doubles")
ap.add_argument("--max-its", type=int, default=0, help="stop after this many LSQR iterations in total (0: no limit); a check is forced there")
args = ap.parse_args()
t0 = time.monotonic(); deadline = t0 + 3600 * args.hours
if args.inverse_radius is not None:
    # control runs: inverse domain and fit radius chosen independently (load_shape ties R = fit_radius / 0.9)
    from centre_fit import CentreShape
    _old = np.load(args.input)
    s = CentreShape(args.nr, args.nt, args.inverse_radius, int(_old["degree"]), int(_old["angular"]), "matched", int(_old["singular"]), rmin=1e-4)
    s.fit_radius = args.fit_radius if args.fit_radius is not None else 900.
    z = s.configure(_old, None, ())
    print(json.dumps({"inverse_radius": args.inverse_radius, "fit_radius": s.fit_radius, "rows": int(np.sum(s.rows)), "R_shape": float(s.p.R)}), flush=True)
else:
    s, z = load_shape(args.input, args.nr, args.nt, fit_radius=args.fit_radius)
Ls = float(np.load(args.input)["L"])
if args.pweight != 1.:
    rr = s.p.r[s.rows][:, None]; tt = s.p.theta[s.cols][None, :]
    dist = np.hypot(rr * np.cos(tt) - args.pcentre / Ls, rr * np.sin(tt)) * Ls
    s.weight = s.weight * (1 + (args.pweight - 1) * np.exp(-(dist / args.pwidth) ** 2))
afac = np.ones_like(s.weight)
if args.aweight != 1.:
    rr = s.p.r[s.rows][:, None]; tt = s.p.theta[s.cols][None, :]
    xx = rr * np.cos(tt) * Ls; yy = rr * np.sin(tt) * Ls
    am = (1 + np.tanh((xx - args.ax0) / .1)) * (1 - np.tanh((xx - args.ax1) / .25)) / 4 * np.exp(-(yy / args.ayw) ** 2)
    afac = 1 + (args.aweight - 1) * am
    s.weight = s.weight * afac
nval = s.weight.size


def l2u(fv):
    return float(np.linalg.norm(np.r_[fv[:nval] / afac.ravel(), fv[nval:]]))


s.output = args.output; s.seconds = float("inf"); s.start = time.monotonic()
s.run_configuration = dict(vars(args), method="gpu_long_solve LSQR (GPU operator)" + (" fixed c_l" if args.fix_cl else "") + (" reorth" if args.reorth else ""))
log = Path(args.output + ".long.jsonl")
lower = np.r_[.05, np.full(len(z) - 1, -30.)]; upper = np.r_[.98, np.full(len(z) - 1, 30.)]
dev = "cuda"


def emit(d):
    d["wall"] = time.monotonic() - t0
    with log.open("a") as fh:
        fh.write(json.dumps(d) + "\n")
    print(json.dumps(d), flush=True)


f = s.fun(z); best = float(np.linalg.norm(f)); zb = z.copy()
emit(dict(event="start", norm=best, l2_unweighted=l2u(f), cl=1 / z[0], nr=args.nr, nt=args.nt, ncol=len(z), nrow=len(f),
          aweight=args.aweight, fix_cl=args.fix_cl, fit_radius=args.fit_radius, inverse_radius=args.inverse_radius, reorth=args.reorth, gpu=torch.cuda.get_device_name(0)))
outer = 0; total_its = 0
while time.monotonic() < deadline - 120 and outer < args.max_outer and (args.max_its <= 0 or total_its < args.max_its):
    outer += 1
    z = zb.copy(); f = s.fun(z) if outer > 1 else f
    tl = time.monotonic()
    op = CentreDerivative(s, z)
    g = GPUDerivative(op, dev)
    rng = np.random.default_rng(8128 + outer); diag = torch.zeros(len(z), dtype=torch.float64, device=dev)
    for _ in range(args.probes):
        probe = torch.as_tensor(rng.choice(np.array([-1., 1.]), size=len(f)), device=dev)
        diag += g.rmatvec(probe) ** 2 / args.probes
    cut = max(float(diag.max()) * 1e-18, 1e-24)
    scale = 1 / torch.sqrt(torch.clamp(diag, min=cut)); scale[diag < cut] = 0.
    if args.fix_cl:
        scale[0] = 0.
    damp = float(np.sqrt(args.damping))
    # LSQR (Paige and Saunders 1982), damped, x0 = 0, b = -f (the lead's loop verbatim, on GPU tensors)
    fdev = torch.as_tensor(f, device=dev)
    u = -fdev.clone(); beta = float(torch.linalg.norm(u)); u /= beta
    v = scale * g.rmatvec(u); alpha = float(torch.linalg.norm(v)); v /= alpha
    w = v.clone(); x = torch.zeros(len(z), dtype=torch.float64, device=dev)
    phibar, rhobar = beta, alpha
    res2 = 0.   # accumulated psi_k^2 of the damping rotations (scipy lsqr's res2): the damped residual is sqrt(phibar^2 + res2)
    if args.reorth:
        V = torch.empty((len(z), args.inner + 1), dtype=torch.float64, device=dev); V[:, 0] = v; nv = 1
    torch.cuda.synchronize()
    emit(dict(event="linearize", outer=outer, norm=float(np.linalg.norm(f)), cl=1 / z[0], seconds_linearize=time.monotonic() - tl,
              gpu_mem_gb=torch.cuda.max_memory_allocated() / 1e9))
    ti = time.monotonic()
    for it in range(1, args.inner + 1):
        if time.monotonic() > deadline - 60:
            break
        total_its += 1
        u = g.matvec(scale * v) - alpha * u; beta = float(torch.linalg.norm(u))
        if beta > 0: u /= beta
        v = scale * g.rmatvec(u) - beta * v
        if args.reorth:
            Vk = V[:, :nv]
            v = v - Vk @ (Vk.T @ v)
            v = v - Vk @ (Vk.T @ v)
        alpha = float(torch.linalg.norm(v))
        if alpha > 0: v /= alpha
        if args.reorth:
            V[:, nv] = v; nv += 1
        rhobar1 = float(np.hypot(rhobar, damp)); cs1 = rhobar / rhobar1; sn1 = damp / rhobar1
        psi = sn1 * phibar
        phibar = cs1 * phibar
        res2 += psi * psi
        rho = float(np.hypot(rhobar1, beta)); cs = rhobar1 / rho; sn = beta / rho
        theta = sn * alpha; rhobar = -cs * alpha
        phi = cs * phibar; phibar = sn * phibar
        x += (phi / rho) * w; w = v - (theta / rho) * w
        last = args.max_its > 0 and total_its >= args.max_its
        if it % args.check == 0 or it == args.inner or last:
            sx = scale * x
            linres = float(torch.linalg.norm(fdev + g.matvec(sx)))   # true linear residual |f + J S x| (one extra matvec; diagnostic only)
            step = sx.cpu().numpy()
            trial = np.clip(z + step, lower, upper)
            ft = s.fun(trial); nt_ = float(np.linalg.norm(ft))
            if nt_ < best:
                best = nt_; zb = trial.copy()
            dampx = damp * float(torch.linalg.norm(x))
            pred = float(np.sqrt(phibar * phibar + res2))          # LSQR estimate of the DAMPED residual sqrt(|f + J S x|^2 + damp^2 |x|^2)
            emit(dict(event="check", outer=outer, it=it, predicted=pred, phibar=float(abs(phibar)), damp_x=dampx,
                      predicted_undamped=float(np.sqrt(max(pred * pred - dampx * dampx, 0.))), linres=linres, actual=nt_, best=best, l2_unweighted=l2u(ft),
                      cl=1 / trial[0], max_step=float(np.max(abs(step))), seconds_per_it=(time.monotonic() - ti) / it, total_its=total_its))
        if last:
            break
    del g, op
    if args.reorth:
        del V, Vk
    torch.cuda.empty_cache()
    info = dict(input=args.input, output=args.output, configuration=s.run_configuration, final_norm=best,
                outer=outer, elapsed=time.monotonic() - t0)
    Path(args.output + ".long.json").write_text(json.dumps(info, indent=2))
emit(dict(event="end", best=best, total_its=total_its))
