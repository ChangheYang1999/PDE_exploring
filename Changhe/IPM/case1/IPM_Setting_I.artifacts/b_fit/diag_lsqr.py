"""Lead diagnostic (2026-10-18 about 12:35Z): is the LSQR linear model consistent with the objective at a stagnating point?
One linearization at INPUT with the setup of long_solve_fixcl.py --fix-cl (outer-1 probe seed, same scaling, damping 1e-8),
CPU operator. At each check iterate x: phibar (LSQR recurrence), lin = |f + J s| (one CPU matvec, s = scale*x), the damped
version, actual = |f(z + s)|, and at t = 0.5 the same pair; gap(t) = f(z + t s) - f - t J s. If |gap| scales like t^2 the
mismatch is nonlinearity, like t it is a derivative inconsistency. gap(1) is split by rows: grid bands in physical radius,
the disc of radius 1.5 about P, the source row and the two centre rows.
Usage: python3 diag_lsqr.py INPUT_shape.npz NR NT NITER CHECKS(comma list) OUT.jsonl"""
import sys, json, time
import numpy as np
from centre_fit import load_shape, CentreDerivative

src, nr, nt, nit = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
checks = sorted(int(c) for c in sys.argv[5].split(','))
outp = sys.argv[6]
t0 = time.monotonic()
def emit(d):
    d['wall'] = round(time.monotonic() - t0, 1)
    with open(outp, 'a') as fh: fh.write(json.dumps(d) + '\n')
    print(json.dumps(d), flush=True)
s, z = load_shape(src, nr, nt)
s.output = None; s.seconds = float('inf'); s.start = time.monotonic()
Ls = float(np.load(src)['L'])
rr = s.p.r[s.rows][:, None] * Ls + 0 * s.p.theta[s.cols][None, :]; tt = 0 * rr + s.p.theta[s.cols][None, :]
dP = np.hypot(rr * np.cos(tt) - 8.60088, rr * np.sin(tt))
rr = rr.ravel(); dP = dP.ravel(); ng = rr.size
bands = [(0, 1e-2), (1e-2, 1e-1), (1e-1, 1.), (1., 3.), (3., 10.), (10., 30.), (30., 100.), (100., 1e9)]
def split(g):
    gg = g[:ng]; d = {}
    for a, b in bands:
        m = (rr >= a) & (rr < b); d['r%g-%g' % (a, b)] = float(np.linalg.norm(gg[m]))
    d['nearP1.5'] = float(np.linalg.norm(gg[dP < 1.5])); d['src'] = float(g[ng]); d['cen'] = [float(g[ng + 1]), float(g[ng + 2])]
    i = int(np.argmax(abs(gg))); d['argmax_r'] = float(rr[i]); d['argmax_dP'] = float(dP[i]); d['max'] = float(abs(gg[i]))
    return d
f = s.fun(z); f0 = float(np.linalg.norm(f))
emit(dict(event='start', src=src, norm=f0, cl=1 / z[0], nrow=len(f), ncol=len(z), ngrid=ng, f_split=split(f)))
op = CentreDerivative(s, z)
rng = np.random.default_rng(8128 + 1); diag = np.zeros(len(z))
for _ in range(24):
    diag += op.rmatvec(rng.choice(np.array([-1., 1.]), size=len(f))) ** 2 / 24
cut = max(float(diag.max()) * 1e-18, 1e-24)
scale = 1 / np.sqrt(np.maximum(diag, cut)); scale[diag < cut] = 0.; scale[0] = 0.
emit(dict(event='scale', n_cut=int(np.sum(diag < cut)), ratio=float(scale[scale > 0].max() / scale[scale > 0].min())))
mv = lambda u: op @ (scale * u); rmv = lambda v: scale * op.rmatvec(v)
damp = np.sqrt(1e-8)
u = -f.copy(); beta = np.linalg.norm(u); u /= beta
v = rmv(u); alpha = np.linalg.norm(v); v /= alpha
w = v.copy(); x = np.zeros(len(z)); phibar, rhobar = beta, alpha
lower = np.r_[.05, np.full(len(z) - 1, -30.)]; upper = np.r_[.98, np.full(len(z) - 1, 30.)]
for it in range(1, nit + 1):
    u = mv(v) - alpha * u; beta = np.linalg.norm(u)
    if beta > 0: u /= beta
    v = rmv(u) - beta * v; alpha = np.linalg.norm(v)
    if alpha > 0: v /= alpha
    rhobar1 = np.hypot(rhobar, damp); cs1 = rhobar / rhobar1
    phibar = cs1 * phibar
    rho = np.hypot(rhobar1, beta); cs = rhobar1 / rho; sn = beta / rho
    theta = sn * alpha; rhobar = -cs * alpha
    phi = cs * phibar; phibar = sn * phibar
    x += (phi / rho) * w; w = v - (theta / rho) * w
    if it in checks:
        st = scale * x; Js = op @ st
        lin = float(np.linalg.norm(f + Js))
        d = dict(event='check', it=it, phibar=float(abs(phibar)), lin=lin, lin_damped=float(np.hypot(lin, damp * np.linalg.norm(x))),
                 max_step=float(np.max(abs(st))), clipped=int(np.sum((z + st < lower) | (z + st > upper))))
        for t in (1., .5):
            ft = s.fun(z + t * st); g = ft - f - t * Js
            d['actual_t%g' % t] = float(np.linalg.norm(ft)); d['lin_t%g' % t] = float(np.linalg.norm(f + t * Js))
            d['gap_t%g' % t] = float(np.linalg.norm(g))
            if t == 1.: d['gap_split'] = split(g); d['res_split'] = split(ft)
        emit(d)
emit(dict(event='end'))
