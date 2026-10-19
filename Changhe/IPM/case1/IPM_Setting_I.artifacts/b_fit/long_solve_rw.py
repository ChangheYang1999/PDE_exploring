"""REWEIGHTED VARIANT (long_solve_rw.py, lead 2026-10-18 about 06:50Z; reasons in WORKLOG, analysis 13.14 (e) and 13.15):
identical to long_solve_fixcl.py except that, at the start of every outer linearization (or only the first with --rw-once),
the node weights are reset to base x factor, where base is the weight of long_solve (with --pweight if given) and
factor = clip((m / tau)^gamma, 1, cap), m = a node value of the current best state after a maximum filter over +-kr radial
and +-kt angular fit nodes (--rw-dilate kr,kt), tau = --rw-frac times the largest node value. The node value is, with
--rw-norm flux (default, added 2026-10-18 about 07:20Z), the flux-normalized residual |R| / (|W1 rho_x| + |W2 rho_y| +
|rho|) of the residual standard (the quick_scan.py formula res / fdlog on the fit nodes); with --rw-norm fit it is the
fit's own row value |res/den| (den = 1 + |3 + ht| for the log objective). The two differ by a position-dependent factor
(about 0.1 next to the x-axis near 0, about 1 next to P), so only the flux choice upweights where the standard is largest.
This is one Lawson-type (iteratively reweighted least squares) step per relinearization toward a fit that controls the
largest node residuals rather than their sum of squares. The best state is tracked under the current weights; every
reweighting and every check also report the unweighted objective (base weights), comparable with long_solve objectives.
Original description:
Lead continuation with a long, checkpointed damped LSQR on one linearization (work/c6).
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
from scipy.ndimage import maximum_filter
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
ap.add_argument("--rw-frac", type=float, default=0.25)
ap.add_argument("--rw-gamma", type=float, default=1.0)
ap.add_argument("--rw-cap", type=float, default=8.0)
ap.add_argument("--rw-dilate", default="6,3")
ap.add_argument("--rw-once", action="store_true")
ap.add_argument("--rw-norm", choices=("flux", "fit"), default="flux")
args = ap.parse_args()
t0 = time.monotonic(); deadline = t0 + 3600 * args.hours
s, z = load_shape(args.input, args.nr, args.nt)
if args.pweight != 1.:
    Ls = float(np.load(args.input)["L"])
    rr = s.p.r[s.rows][:, None]; tt = s.p.theta[s.cols][None, :]
    dist = np.hypot(rr * np.cos(tt) - args.pcentre / Ls, rr * np.sin(tt)) * Ls
    s.weight = s.weight * (1 + (args.pweight - 1) * np.exp(-(dist / args.pwidth) ** 2))
s.output = args.output; s.seconds = float("inf"); s.start = time.monotonic()
s.run_configuration = dict(vars(args), method="long_solve LSQR" + (" fixed c_l" if args.fix_cl else "") + " reweighted")
log = Path(args.output + ".long.jsonl")
lower = np.r_[.05, np.full(len(z) - 1, -30.)]; upper = np.r_[.98, np.full(len(z) - 1, 30.)]


def emit(d):
    d["wall"] = time.monotonic() - t0
    with log.open("a") as fh:
        fh.write(json.dumps(d) + "\n")
    print(json.dumps(d), flush=True)


base_w = s.weight.copy()
kr, kt = (int(v) for v in args.rw_dilate.split(","))
rr_n = s.p.r[s.rows]; tt_n = s.p.theta[s.cols]
L_in = float(np.load(args.input)["L"])


def unweighted(zz):
    """Node values |res/den| (base weights divided out) and the objective with base weights."""
    w = s.weight; s.weight = base_w
    res, _, _ = s.raw_fun(zz)
    s.weight = w
    vals = np.abs(res[:base_w.size].reshape(base_w.shape) / base_w)
    return vals, float(np.linalg.norm(res))


def flux_vals(zz):
    """|res / fdlog| on the fit nodes: the flux-normalized residual of quick_scan.py."""
    _, f, L2, res, _ = s.evaluate(zz)
    k = zz[0]; ct, st = s.p.ct, s.p.st
    wa = 1 / k + L2 * f["ux"]; wb = 1 / k + L2 * f["uy"]
    fd = (np.abs(wa * (2 + f["ht"] * ct ** 2 - f["ha"] * ct * st)) +
          np.abs(wb * (1 + f["ht"] * st ** 2 + f["ha"] * ct * st)) + 1)
    return np.abs(res / fd)[s.rows][:, s.cols]


def reweight(zz, outer):
    vals, unw = unweighted(zz)
    fit_max = float(vals.max())
    if args.rw_norm == "flux":
        vals = flux_vals(zz)
    m = maximum_filter(vals, size=(2 * kr + 1, 2 * kt + 1), mode="nearest")
    tau = args.rw_frac * float(vals.max())
    fac = np.clip((m / tau) ** args.rw_gamma, 1., args.rw_cap)
    s.weight = base_w * fac; s.best = np.inf
    i, j = np.unravel_index(int(np.argmax(vals)), vals.shape)
    emit(dict(event="reweight", outer=outer, norm=args.rw_norm, unweighted=unw, node_max=float(vals.max()), fit_node_max=fit_max,
              node_max_at=[float(rr_n[i] * L_in), float(tt_n[j])], tau=tau,
              frac_up=float(np.mean(fac > 1)), fac_mean=float(fac.mean()), fac_max=float(fac.max())))


f = s.fun(z); best = float(np.linalg.norm(f)); zb = z.copy()
emit(dict(event="start", norm=best, cl=1 / z[0], nr=args.nr, nt=args.nt, ncol=len(z), nrow=len(f)))
outer = 0
while time.monotonic() < deadline - 120:
    outer += 1
    z = zb.copy()
    if outer == 1 or not args.rw_once:
        reweight(z, outer)
    f = s.fun(z); best = float(np.linalg.norm(f))
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
            vt, ut = unweighted(trial)
            fx = float(flux_vals(trial).max()) if args.rw_norm == "flux" else None
            emit(dict(event="check", outer=outer, it=it, predicted=float(abs(phibar)), actual=nt_, best=best,
                      cl=1 / trial[0], max_step=float(np.max(abs(step))), unweighted=ut, node_max=float(vt.max()),
                      flux_node_max=fx))
    # final save of the best (s.fun already saved improvements); store run json
    info = dict(input=args.input, output=args.output, configuration=s.run_configuration, final_norm=best,
                outer=outer, elapsed=time.monotonic() - t0)
    Path(args.output + ".long.json").write_text(json.dumps(info, indent=2))
emit(dict(event="end", best=best))
