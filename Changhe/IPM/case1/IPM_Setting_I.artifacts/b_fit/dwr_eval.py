"""Discrete dual-weighted c_l estimate on an evaluation grid (lead, 2026-10-18; astra softcl1 task 3, analysis 13.11).
Input: a fitted shape z0 and its soft tangent v (soft_tangent.py, computed on the fit grid; k = z[0] = 1/c_l).
On the evaluation grid G (rows of CentreShape.raw_fun at nr x nt):
  s_G = F_k + J_s v_G,  f_G = F(z0),  dk_G = -<f_G, s_G>/|s_G|^2,  dcl_G = 1/(k0 + dk_G) - c0,
where v_G = v + dv and dv is a warm-started LSQR correction min |s_G + J_s dv| on G (--inner iterations; 0 keeps v).
When J_s^T s_G = 0 (the normal equations of the tangent problem on G), the linearized residual f_G = J_s e + F_k d + f_perp
with f_perp orthogonal to the range gives <s_G, f_G> = d |s_G|^2 exactly: dk_G is then the Gauss-Newton exponent step of
the objective on G within the trial space (where its least-squares minimizer lies in k, to first order), whatever the
shape error e. It is a property of the trial space and the grid, not of the exact profile. The stationarity defect
max_i |<c_i, s_G>| / |s_G| over the scaled shape columns c_i (unit norm by the column scaling; rms version too) is reported at every check, together with the split of
<f_G, s_G> over physical radius bands and the extra rows (source row, two centre rows).
Usage: python3 dwr_eval.py SHAPE.npz TANGENT.npz OUT_PREFIX --nr 20480 --nt 480 [--inner 200 --check 50]"""
import json
import time
import argparse
from pathlib import Path
import numpy as np
from centre_fit import load_shape, CentreDerivative

ap = argparse.ArgumentParser()
ap.add_argument("input"); ap.add_argument("tangent"); ap.add_argument("prefix")
ap.add_argument("--nr", type=int, default=20480); ap.add_argument("--nt", type=int, default=480)
ap.add_argument("--inner", type=int, default=200)
ap.add_argument("--check", type=int, default=50)
ap.add_argument("--hours", type=float, default=1.5)
ap.add_argument("--damping", type=float, default=1e-14)
ap.add_argument("--probes", type=int, default=24)
args = ap.parse_args()
t0 = time.monotonic(); deadline = t0 + 3600 * args.hours
s, z0 = load_shape(args.input, args.nr, args.nt)
s.seconds = float("inf"); s.start = time.monotonic()
tan = np.load(args.tangent)
v0 = np.array(tan["v"], float)
assert v0.shape == z0.shape, "tangent and shape have different coefficient vectors"
assert abs(float(tan["k0"]) - float(z0[0])) < 1e-12, "tangent was computed at another k"
log = Path(args.prefix + "_dwr.jsonl")
k0 = float(z0[0]); c0 = 1 / k0


def emit(d):
    d["wall"] = time.monotonic() - t0
    with log.open("a") as fh:
        fh.write(json.dumps(d) + "\n")
    print(json.dumps(d), flush=True)


f0, cen, source = s.raw_fun(z0)
ntr = len(f0) - 3
r_phys = s.p.r[s.rows] * np.sqrt(cen["L2"])
band_edges = [0., 2., 10., 100., 1e3, np.inf]
row_r = np.repeat(r_phys, len(s.cols))
assert len(row_r) == ntr
bands = [(lo, hi, (row_r >= lo) & (row_r < hi)) for lo, hi in zip(band_edges[:-1], band_edges[1:])]
# shells by distance from the source point P = (x*, 0) (physical units), for the location of the tangent residual s
xstar = float(np.sqrt(cen["L2"]) * np.exp(source[0]))
row_t = np.tile(s.p.theta[s.cols], len(r_phys))
dP = np.hypot(row_r * np.cos(row_t) - xstar, row_r * np.sin(row_t))
shell_edges = [0., .5, 1., 2., 4., 8., np.inf]
shells = [(lo, hi, (dP >= lo) & (dP < hi)) for lo, hi in zip(shell_edges[:-1], shell_edges[1:])]
emit(dict(event="start", input=args.input, tangent=args.tangent, c0=c0, xstar=xstar, nr=args.nr, nt=args.nt, nrow=len(f0),
          norm_f=float(np.linalg.norm(f0)), hP1=float(source[1] - 1), E=float(cen["E"]), D2=float(cen["D2"]),
          tangent_it=int(tan["it"])))
op = CentreDerivative(s, z0)
e0 = np.zeros(len(z0)); e0[0] = 1.
Fk = op @ e0
rng = np.random.default_rng(4049); diag = np.zeros(len(z0))
for _ in range(args.probes):
    diag += op.rmatvec(rng.choice(np.array([-1., 1.]), size=len(f0))) ** 2 / args.probes
cut = max(float(diag.max()) * 1e-18, 1e-24)
scale = 1 / np.sqrt(np.maximum(diag, cut)); scale[diag < cut] = 0.; scale[0] = 0.
v0 = v0.copy(); v0[0] = 0.
s0 = Fk + op @ v0
mv = lambda u: op @ (scale * u)
rmv = lambda w: scale * op.rmatvec(w)
damp = np.sqrt(args.damping)
colnorm = np.sqrt(np.maximum(diag, 0.)) * scale          # about 1 on the active columns


def report(it, sv):
    ns = float(np.linalg.norm(sv)); dot = float(f0 @ sv)
    dk = -dot / ns ** 2
    g = rmv(sv)                                           # scaled J_s^T s
    stat = float(np.max(abs(g)) / ns)                     # largest cosine between s and a scaled shape column
    stat_rms = float(np.linalg.norm(g) / (np.sqrt(np.sum(colnorm ** 2)) * ns))
    split = {f"r[{lo:g},{hi:g})": float(f0[:ntr][m] @ sv[:ntr][m]) for lo, hi, m in bands}
    split["source_row"] = float(f0[ntr] * sv[ntr]); split["centre_rows"] = float(f0[ntr + 1:] @ sv[ntr + 1:])
    for lo, hi, m in shells:
        split[f"dP[{lo:g},{hi:g})"] = float(f0[:ntr][m] @ sv[:ntr][m])
    # where the tangent residual lives: fractions of |s|^2 by radius band, by shell around P, and in the extra rows
    s2 = {f"r[{lo:g},{hi:g})": float(sv[:ntr][m] @ sv[:ntr][m]) / ns ** 2 for lo, hi, m in bands}
    s2.update({f"dP[{lo:g},{hi:g})": float(sv[:ntr][m] @ sv[:ntr][m]) / ns ** 2 for lo, hi, m in shells})
    s2["source_row"] = float(sv[ntr] ** 2) / ns ** 2; s2["centre_rows"] = float(sv[ntr + 1:] @ sv[ntr + 1:]) / ns ** 2
    emit(dict(event="check", it=it, norm_s=ns, sigma_per_cl=ns * k0 ** 2, f_dot_s=dot, dk=dk,
              dcl=1 / (k0 + dk) - c0, stationarity=stat, stationarity_rms=stat_rms,
              m_min=float(np.sqrt(max(np.linalg.norm(f0) ** 2 - dot ** 2 / ns ** 2, 0.))), split=split, s2_fraction=s2))


report(0, s0)
# warm-started LSQR on the correction: min |s0 + J_s (scale x)|, x0 = 0
u = -s0.copy(); beta = np.linalg.norm(u); u /= beta
w_ = rmv(u); alpha = np.linalg.norm(w_); w_ /= alpha
w = w_.copy(); x = np.zeros(len(z0))
phibar, rhobar = beta, alpha
it = 0
for it in range(1, args.inner + 1):
    if time.monotonic() > deadline - 300:
        break
    u = mv(w_) - alpha * u; beta = np.linalg.norm(u)
    if beta > 0: u /= beta
    w_ = rmv(u) - beta * w_; alpha = np.linalg.norm(w_)
    if alpha > 0: w_ /= alpha
    rhobar1 = np.hypot(rhobar, damp); cs1 = rhobar / rhobar1
    phibar = cs1 * phibar
    rho = np.hypot(rhobar1, beta); cs = rhobar1 / rho; sn = beta / rho
    theta = sn * alpha; rhobar = -cs * alpha
    phi = cs * phibar; phibar = sn * phibar
    x += (phi / rho) * w; w = w_ - (theta / rho) * w
    if it % args.check == 0 and it < args.inner:
        report(it, s0 + op @ (scale * x))
if args.inner > 0:
    vG = v0 + scale * x
    report(it, Fk + op @ vG)
    np.savez(args.prefix + "_dwr_tangent.npz", v=vG, it=it, k0=k0, c0=c0, nr=args.nr, nt=args.nt)
emit(dict(event="end", it=it))
