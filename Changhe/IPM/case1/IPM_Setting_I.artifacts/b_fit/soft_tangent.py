"""Soft c_l direction of a fitted shape (lead, 2026-10-18; VERIFY_REPORT G37, G38 (f), (g)).
Linearized fixed-c least squares at the fitted coefficients z0 (k = z[0] = 1/c_l):
  F_k = dF/dk (column 0 of the Jacobian used by long_solve.py),
  v   = argmin_v |F_k + J_s v| over the shape columns (LSQR, column scaling as long_solve.py, k column excluded),
  r   = F_k + J_s v, the part of F_k that no change of shape absorbs (to the accuracy of the Krylov solve).
To first order the best objective at k0 + dk is m_lin(dk) = |f0 + dk r| (f0 = F(z0)), with minimum at
  dk* = -<f0, r>/|r|^2 (the Gauss-Newton correction of k along the soft direction), and |r| k^2 is the cost per unit
  c_l. A truncated Krylov solve over-estimates |r|, so sigma_N = |r_N| k^2 is an upper bound for the cost.
At checkpoints: |r_N|, <f0, r_N>, dk*, and nonlinear objective norms (and h(P) - 1) along the tangent z0 + dk (e0 + v_N)
for the requested c_l offsets. At the end the tangent and shape files at the offsets are saved.
Usage: python3 soft_tangent.py SHAPE.npz OUT_PREFIX --nr 10240 --nt 480 --inner 2500 --check 250
       [--every 500] [--offsets -3e-3,-1e-3,-3e-4,-1e-4,1e-4,3e-4,1e-3,3e-3]"""
import json
import time
import argparse
from pathlib import Path
import numpy as np
from centre_fit import load_shape, CentreDerivative

ap = argparse.ArgumentParser()
ap.add_argument("input"); ap.add_argument("prefix")
ap.add_argument("--nr", type=int, default=10240); ap.add_argument("--nt", type=int, default=480)
ap.add_argument("--inner", type=int, default=2500)
ap.add_argument("--check", type=int, default=250)
ap.add_argument("--every", type=int, default=500)
ap.add_argument("--hours", type=float, default=3.0)
ap.add_argument("--damping", type=float, default=1e-14)
ap.add_argument("--probes", type=int, default=24)
ap.add_argument("--offsets", default="-3e-3,-1e-3,-3e-4,-1e-4,1e-4,3e-4,1e-3,3e-3")
args = ap.parse_args()
offsets = [float(v) for v in args.offsets.split(",")]
t0 = time.monotonic(); deadline = t0 + 3600 * args.hours
s, z0 = load_shape(args.input, args.nr, args.nt)
s.seconds = float("inf"); s.start = time.monotonic()
log = Path(args.prefix + "_tangent.jsonl")
k0 = float(z0[0]); c0 = 1 / k0


def emit(d):
    d["wall"] = time.monotonic() - t0
    with log.open("a") as fh:
        fh.write(json.dumps(d) + "\n")
    print(json.dumps(d), flush=True)


def evaluate(z):
    res, cen, source = s.raw_fun(z)
    return res, dict(norm=float(np.linalg.norm(res)), transport=float(np.linalg.norm(res[:-3])),
                     hP1=float(source[1] - 1), E=float(cen["E"]), D2=float(cen["D2"]))


f0, info0 = evaluate(z0)
emit(dict(event="start", c0=c0, nr=args.nr, nt=args.nt, ncol=len(z0), nrow=len(f0), **info0))
op = CentreDerivative(s, z0)
e0 = np.zeros(len(z0)); e0[0] = 1.
Fk = op @ e0
# check of the k column against a central difference of the nonlinear rows
eps = 1e-6
fp, _ = evaluate(z0 + eps * e0); fm, _ = evaluate(z0 - eps * e0)
fd = (fp - fm) / (2 * eps)
emit(dict(event="k_column", norm_Fk=float(np.linalg.norm(Fk)), norm_fd=float(np.linalg.norm(fd)),
          rel_diff=float(np.linalg.norm(Fk - fd) / np.linalg.norm(fd)),
          f0_dot_Fk=float(f0 @ Fk)))
rng = np.random.default_rng(4049); diag = np.zeros(len(z0))
for _ in range(args.probes):
    diag += op.rmatvec(rng.choice(np.array([-1., 1.]), size=len(f0))) ** 2 / args.probes
cut = max(float(diag.max()) * 1e-18, 1e-24)
scale = 1 / np.sqrt(np.maximum(diag, cut)); scale[diag < cut] = 0.; scale[0] = 0.
mv = lambda u: op @ (scale * u)
rmv = lambda v: scale * op.rmatvec(v)
damp = np.sqrt(args.damping)


def checkpoint(it, x, nonlinear):
    v = scale * x
    r = Fk + op @ v
    nr_ = float(np.linalg.norm(r)); dot = float(f0 @ r)
    dks = -dot / nr_ ** 2
    d = dict(event="check", it=it, norm_r=nr_, sigma_per_cl=nr_ * k0 ** 2, f0_dot_r=dot,
             dk_star=dks, dcl_star=1 / (k0 + dks) - c0,
             m_lin_min=float(np.sqrt(max(np.linalg.norm(f0) ** 2 - dot ** 2 / nr_ ** 2, 0.))),
             m0=float(np.linalg.norm(f0)), max_v=float(np.max(abs(v))))
    lin = {}
    for dc in offsets:
        dk = 1 / (c0 + dc) - k0
        lin[repr(dc)] = float(np.linalg.norm(f0 + dk * r))
    d["m_lin"] = lin
    if nonlinear:
        nl = {}
        for dc in offsets:
            dk = 1 / (c0 + dc) - k0
            _, inf = evaluate(z0 + dk * (e0 + v))
            nl[repr(dc)] = inf
        d["m_nonlinear"] = nl
    emit(d)
    return v


# LSQR (Paige and Saunders 1982), damped, x0 = 0, b = -F_k
u = -Fk.copy(); beta = np.linalg.norm(u); u /= beta
v = rmv(u); alpha = np.linalg.norm(v); v /= alpha
w = v.copy(); x = np.zeros(len(z0))
phibar, rhobar = beta, alpha
emit(dict(event="lsqr_start", beta=float(beta)))
it = 0
for it in range(1, args.inner + 1):
    if time.monotonic() > deadline - 600:
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
    if it % args.check == 0 and it < args.inner:
        checkpoint(it, x, it % args.every == 0)
        np.savez(args.prefix + "_tangent.npz", v=scale * x, it=it, k0=k0, c0=c0)
vt = checkpoint(it, x, True)
np.savez(args.prefix + "_tangent.npz", v=vt, it=it, k0=k0, c0=c0)
s.run_configuration = dict(vars(args), method="soft_tangent: z0 + dk (e0 + v)")
for dc in offsets:
    dk = 1 / (c0 + dc) - k0
    s.save(f"{args.prefix}_tan{dc:+.0e}_shape.npz", z0 + dk * (e0 + vt))
emit(dict(event="end", it=it))
