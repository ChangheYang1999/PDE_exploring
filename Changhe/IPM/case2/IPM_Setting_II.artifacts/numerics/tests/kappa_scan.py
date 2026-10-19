"""Scan of the lead's moment-law pair over nonnegative data rho = zeta^2 (random smooth zeta with the jet):
kappa = Q/(pi c^2) vs the profile value 1 - 1/(2c), together with min_X V_r/r (V = (1/2+c)X + W[rho]; a single
stagnation point iff V_r > 0 everywhere on the grid) and the x-odd fraction.  No solves: one velocity evaluation per
sample.  Usage: python3 tests/kappa_scan.py Nr Nth R nsamp seed [xodd]"""
import sys, math, time; sys.path.insert(0, 'code')
import torch, numpy as np
from ipm2polar import Disc
from zetasolve import quad_weights, wq_r
torch.set_default_dtype(torch.float64)
dev = 'cuda'
Nr, Nth, R, nsamp, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
xodd = len(sys.argv) > 6 and sys.argv[6] == 'xodd'
d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev)
th = d.theta_p[:, None]; r = d.r[None, :]
X, Y = r * torch.cos(th), r * torch.sin(th)
rng = np.random.default_rng(seed)
wq = quad_weights(d); wr = wq_r(d)
thp = d.theta_p[:, None]; rr = d.r[None, :]
phi_r = -3 * rr ** -4 * torch.sin(3 * thp); phi_t_over_r = 3 * rr ** -4 * torch.cos(3 * thp)
mm = torch.arange(d.M + 1, device=dev); sgn = (-1.0) ** mm
print("# Nr %d Nth %d R %g nsamp %d seed %d xodd %s %s" % (Nr, Nth, R, nsamp, seed, xodd, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
print("# columns: sample p_in c b kappa=Q/(pi c^2) target=1-1/(2c) Qint Qext minVr/r minV/r asym_x rho_max_R desc")
for isamp in range(nsamp):
    p_in = rng.uniform(0.25, 0.8)
    g = torch.ones_like(X); desc = []
    for k in range(rng.integers(1, 4)):
        A = rng.normal() * rng.choice([0.5, 1.0, 2.0, 4.0]); sc = rng.choice([0.3, 1.0, 3.0, 10.0, 30.0])
        kind = rng.choice(['y', 'y3', 'x2y', 'bump', 'yr'])
        rr2 = 1 + r ** 2 / sc ** 2
        if kind == 'y':     h = A * Y / rr2 ** 0.5 / sc
        elif kind == 'y3':  h = A * Y ** 3 / rr2 ** 1.5 / sc ** 3
        elif kind == 'x2y': h = A * X ** 2 * Y / rr2 ** 1.5 / sc ** 3
        elif kind == 'yr':  h = A * Y / rr2 / sc
        else:
            x0, y0 = rng.normal() * sc, rng.normal() * sc
            h = A * torch.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / (0.3 * sc) ** 2)
        g = g + h; desc.append("%s(%.2f,%.1f)" % (kind, A, sc))
    if xodd:
        A = rng.normal() * 0.5; sc = rng.choice([0.3, 1.0, 3.0]); g = g + A * X * Y / (1 + r ** 2 / sc ** 2) / sc ** 2; desc.append("xodd(%.2f,%.1f)" % (A, sc))
    z0 = X * g * (1 + r ** 2) ** ((p_in / 2 - 1) / 2)
    qz = d.to_modes(z0) / d.rk
    d.tail_exps = (p_in, p_in - 1.0)
    out = d.zeta_residual_modes(qz, torch.tensor(1.0 / p_in, device=dev), return_all=True)
    U0, pxx, pxy, pyy = d.taylor_psi(out['p'])
    c, b = float(pxy), float(pyy)
    rho, Ur, Ut = out['rho'], out['Ur'], out['Ut']
    integ = (rho * (Ur * phi_r + Ut * phi_t_over_r)).mean(dim=0) * 2 * math.pi
    Qin = float(torch.sum(integ * wr))
    r0, r2 = float(d.r[0]), float(d.r[2]); i0, i2 = float(integ[0] * r0), float(integ[2] * r2)
    Qext = float('nan')
    if i0 * i2 > 0:
        slope = math.log(abs(i0) / abs(i2)) / math.log(r0 / r2)
        if slope < -1.0: Qext = -i0 * r0 / (slope + 1.0)
    Q = Qin + (Qext if np.isfinite(Qext) else 0.0)
    kap = Q / (math.pi * c * c) if c != 0 else float('nan')
    cl = 0.5 + c
    Vr = cl * rr + Ur; Vmag = torch.sqrt(Vr ** 2 + Ut ** 2) / rr
    rho_m = out['rho_m']; odd_x = 0.5 * (rho_m - sgn[:, None] * rho_m.conj()); nrm = torch.sqrt((rho_m.abs() ** 2 * wq[None, :]).sum())
    ax = float(torch.sqrt((odd_x.abs() ** 2 * wq[None, :]).sum()) / nrm)
    print("%3d %.3f %9.4f %9.2e %9.4f %9.4f %9.4f %9.2e %7.3f %7.3f %8.1e %8.1e %s" % (isamp, p_in, c, b, kap, 1 - 1 / (2 * c) if c != 0 else float('nan'), Qin, Qext, float((Vr / rr).min()), float(Vmag.min()), ax, float(rho[:, 0].abs().max()), " ".join(desc)), flush=True)
