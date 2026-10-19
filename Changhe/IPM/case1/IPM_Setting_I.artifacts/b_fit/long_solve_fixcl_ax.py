"""Lead continuation with a long, checkpointed damped LSQR on one linearization (work/c6).
AXIS-WEIGHTED VARIANT (long_solve_fixcl_ax.py, lead 2026-10-18 about 11:05Z; copy of long_solve_fixcl.py with --aweight):
the rows next to the x-axis between the origin and P get the extra weight 1 + (aweight - 1) m(x, y), with
m = (1 + tanh((x - ax0)/0.1))(1 - tanh((x - ax1)/0.25))/4 * exp(-(y/ayw)^2) in physical coordinates (x = r cos(theta) L,
y = r sin(theta) L). Reason: the residual rows are R/rho divided by den = 1 + |3 + ht| + |L^2 Uadv|, about 20 on that
axis segment, and the characteristic defect J integrates R/rho there with weight 1/|W_1| (VERIFY_REPORT G69 (e)). The
window ends before the strip next to P (x about 8.5). Every check also logs the unweighted L2 objective (l2_unweighted).
FIXED-C_L VARIANT (long_solve_fixcl.py, 2026-10-18 about 03:55Z; VERIFY_REPORT G45 (e)): identical to long_solve.py except
that with --fix-cl the k column (k = z[0] = 1/c_l) is excluded from every step (column scale 0, as in soft_tangent.py), so
c_l stays at the value of the input shape; the fixed-c objective m(c) of G38 (g) is approached from that start.
The construct4 chunks show predicted linear norm = actual norm to 8 digits: the fit is linear at this level and
only the 300-iteration Krylov solve limits progress. Here one linearization is solved by LSQR (Paige-Saunders, with
damping, written out so that the iterate can be checkpointed) for up to --inner iterations; every --check iterations
the actual objective at z + scale*x is evaluated and the shape is saved when it improves; then relinearize.
Column scaling: stochastic diagonal of J^T J (Rademacher probes), as in stationary.krylov_solve.
Usage: python3 long_solve.py INPUT_shape.npz OUTPUT_shape.npz --nr 4096 --nt 480 --hours H [--inner 3000] [--check 150]
       [--damping 1e-8] [--pweight W --pwidth 3 --pcentre 8.60088]"""
import json
import time
import argparse
from pathlib import Path
import numpy as np
from centre_fit import load_shape, CentreDerivative

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
ap.add_argument("--fix-cl", action="store_true")
ap.add_argument("--aweight", type=float, default=1.)
ap.add_argument("--ax0", type=float, default=0.3)
ap.add_argument("--ax1", type=float, default=7.2)
ap.add_argument("--ayw", type=float, default=0.3)
args = ap.parse_args()
t0 = time.monotonic(); deadline = t0 + 3600 * args.hours
s, z = load_shape(args.input, args.nr, args.nt)
if args.pweight != 1.:
    Ls = float(np.load(args.input)["L"])
    rr = s.p.r[s.rows][:, None]; tt = s.p.theta[s.cols][None, :]
    dist = np.hypot(rr * np.cos(tt) - args.pcentre / Ls, rr * np.sin(tt)) * Ls
    s.weight = s.weight * (1 + (args.pweight - 1) * np.exp(-(dist / args.pwidth) ** 2))
afac = np.ones_like(s.weight)
if args.aweight != 1.:
    Ls = float(np.load(args.input)["L"])
    rr = s.p.r[s.rows][:, None]; tt = s.p.theta[s.cols][None, :]
    xx = rr * np.cos(tt) * Ls; yy = rr * np.sin(tt) * Ls
    am = (1 + np.tanh((xx - args.ax0) / .1)) * (1 - np.tanh((xx - args.ax1) / .25)) / 4 * np.exp(-(yy / args.ayw) ** 2)
    afac = 1 + (args.aweight - 1) * am
    s.weight = s.weight * afac
nval = s.weight.size


def l2u(fv):
    return float(np.linalg.norm(np.r_[fv[:nval] / afac.ravel(), fv[nval:]]))


s.output = args.output; s.seconds = float("inf"); s.start = time.monotonic()
s.run_configuration = dict(vars(args), method="long_solve LSQR" + (" fixed c_l" if args.fix_cl else ""))
log = Path(args.output + ".long.jsonl")
lower = np.r_[.05, np.full(len(z) - 1, -30.)]; upper = np.r_[.98, np.full(len(z) - 1, 30.)]


def emit(d):
    d["wall"] = time.monotonic() - t0
    with log.open("a") as fh:
        fh.write(json.dumps(d) + "\n")
    print(json.dumps(d), flush=True)


f = s.fun(z); best = float(np.linalg.norm(f)); zb = z.copy()
emit(dict(event="start", norm=best, l2_unweighted=l2u(f), cl=1 / z[0], nr=args.nr, nt=args.nt, ncol=len(z), nrow=len(f),
          weighted_rows=int(np.sum(afac > 1.01)), afac_max=float(afac.max())))
outer = 0
while time.monotonic() < deadline - 120:
    outer += 1
    z = zb.copy(); f = s.fun(z) if outer > 1 else f
    op = CentreDerivative(s, z)
    rng = np.random.default_rng(8128 + outer); diag = np.zeros(len(z))
    for _ in range(args.probes):
        diag += op.rmatvec(rng.choice(np.array([-1., 1.]), size=len(f))) ** 2 / args.probes
    cut = max(float(diag.max()) * 1e-18, 1e-24)
    scale = 1 / np.sqrt(np.maximum(diag, cut)); scale[diag < cut] = 0.
    if args.fix_cl:
        scale[0] = 0.
    mv = lambda u: op @ (scale * u)
    rmv = lambda v: scale * op.rmatvec(v)
    damp = np.sqrt(args.damping)
    # LSQR (Paige and Saunders 1982), damped, x0 = 0, b = -f
    u = -f.copy(); beta = np.linalg.norm(u); u /= beta
    v = rmv(u); alpha = np.linalg.norm(v); v /= alpha
    w = v.copy(); x = np.zeros(len(z))
    phibar, rhobar = beta, alpha
    emit(dict(event="linearize", outer=outer, norm=float(np.linalg.norm(f)), cl=1 / z[0]))
    for it in range(1, args.inner + 1):
        if time.monotonic() > deadline - 60:
            break
        u = mv(v) - alpha * u; beta = np.linalg.norm(u)
        if beta > 0: u /= beta
        v = rmv(u) - beta * v; alpha = np.linalg.norm(v)
        if alpha > 0: v /= alpha
        rhobar1 = np.hypot(rhobar, damp); cs1 = rhobar / rhobar1; sn1 = damp / rhobar1
        phibar = cs1 * phibar
        rho = np.hypot(rhobar1, beta); cs = rhobar1 / rho; sn = beta / rho
        theta = sn * alpha; rhobar = -cs * alpha
        phi = cs * phibar; phibar = sn * phibar
        x += (phi / rho) * w; w = v - (theta / rho) * w
        if it % args.check == 0 or it == args.inner:
            step = scale * x
            trial = np.clip(z + step, lower, upper)
            ft = s.fun(trial); nt_ = float(np.linalg.norm(ft))
            if nt_ < best:
                best = nt_; zb = trial.copy()
            emit(dict(event="check", outer=outer, it=it, predicted=float(abs(phibar)), actual=nt_, best=best, l2_unweighted=l2u(ft),
                      cl=1 / trial[0], max_step=float(np.max(abs(step)))))
    # final save of the best (s.fun already saved improvements); store run json
    info = dict(input=args.input, output=args.output, configuration=s.run_configuration, final_norm=best,
                outer=outer, elapsed=time.monotonic() - t0)
    Path(args.output + ".long.json").write_text(json.dumps(info, indent=2))
emit(dict(event="end", best=best))
