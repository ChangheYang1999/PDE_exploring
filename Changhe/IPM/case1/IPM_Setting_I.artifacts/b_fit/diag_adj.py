"""Lead diagnostic 2 (2026-10-18 about 12:45Z): diag_lsqr.py found phibar 4.0697e-6 against the true linear residual
|f + J s| = 4.14215e-6 after 25 LSQR iterations at the s2g shape (and |f(z + s)| = 4.14215e-6, so the linear model itself is
consistent with the objective). In exact arithmetic phibar = |[f + J s; damp x]|, and the relation J V = U B holds by
construction, so the difference means that the Lanczos vectors u_k are not orthonormal; with x tiny (|x| ~ 1e-5) ordinary
rounding cannot do this, an inconsistency between the matvec and the rmatvec can.
This script repeats the same LSQR (same probes, scaling, damping) for NIT iterations and logs per iteration:
  adj_k = <u_k, A v_k> - <A^T u_k, v_k> (A = scaled operator), relative to alpha_k;
  <u_k, u_{k+1}>, <u_1, u_{k+1}>, <v_k, v_{k+1}>, <v_1, v_{k+1}>;
and every 5 iterations the true |b - A x| against phibar. Then the plain adjoint test on random and on structured vectors:
<A v, u> - <v, A^T u> relative to |A v||u| and to |<A v, u>|, for v = random, v = a unit column with the largest scale (the
least excited columns), u = random, u = f.
Usage: python3 diag_adj.py INPUT_shape.npz NR NT NIT OUT.jsonl"""
import sys, json, time
import numpy as np
from centre_fit import load_shape, CentreDerivative

src, nr, nt, nit, outp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
t0 = time.monotonic()
def emit(d):
    d['wall'] = round(time.monotonic() - t0, 1)
    with open(outp, 'a') as fh: fh.write(json.dumps(d) + '\n')
    print(json.dumps(d), flush=True)
s, z = load_shape(src, nr, nt)
s.output = None; s.seconds = float('inf'); s.start = time.monotonic()
f = s.fun(z)
op = CentreDerivative(s, z)
rng = np.random.default_rng(8128 + 1); diag = np.zeros(len(z))
for _ in range(24):
    diag += op.rmatvec(rng.choice(np.array([-1., 1.]), size=len(f))) ** 2 / 24
cut = max(float(diag.max()) * 1e-18, 1e-24)
scale = 1 / np.sqrt(np.maximum(diag, cut)); scale[diag < cut] = 0.; scale[0] = 0.
mv = lambda u: op @ (scale * u); rmv = lambda v: scale * op.rmatvec(v)
damp = np.sqrt(1e-8)
emit(dict(event='start', norm=float(np.linalg.norm(f)), ratio=float(scale[scale > 0].max() / scale[scale > 0].min())))
u = -f.copy(); beta = np.linalg.norm(u); u /= beta; b = u * beta
Atu = rmv(u); v = Atu.copy(); alpha = np.linalg.norm(v); v /= alpha
u1 = u.copy(); v1 = v.copy()
w = v.copy(); x = np.zeros(len(z)); phibar, rhobar = beta, alpha
for it in range(1, nit + 1):
    Av = mv(v); c1 = float(np.dot(u, Av)); c2 = float(np.dot(Atu, v))
    un = Av - alpha * u; beta = np.linalg.norm(un); un /= beta
    Atu = rmv(un); vn = Atu - beta * v; alpha_n = np.linalg.norm(vn); vn /= alpha_n
    d = dict(event='it', it=it, alpha=float(alpha), beta=float(beta), adj_rel=(c1 - c2) / float(alpha),
             uu=float(np.dot(u, un)), u1u=float(np.dot(u1, un)), vv=float(np.dot(v, vn)), v1v=float(np.dot(v1, vn)))
    u, v = un, vn
    rhobar1 = np.hypot(rhobar, damp); cs1 = rhobar / rhobar1; phibar = cs1 * phibar
    rho = np.hypot(rhobar1, beta); cs = rhobar1 / rho; sn = beta / rho
    theta = sn * alpha_n; rhobar = -cs * alpha_n
    phi = cs * phibar; phibar = sn * phibar
    x += (phi / rho) * w; w = v - (theta / rho) * w
    alpha = alpha_n
    if it % 5 == 0 or it <= 3:
        d['phibar'] = float(abs(phibar)); d['true'] = float(np.linalg.norm(b - mv(x))); d['xnorm'] = float(np.linalg.norm(x))
    emit(d)
# plain adjoint tests
rng = np.random.default_rng(5)
big = np.argsort(scale)[-5:]
tests = [('rand', 'rand'), ('rand', 'f')] + [('col%d' % j, 'rand') for j in big[-2:]] + [('col%d' % j, 'f') for j in big[-2:]]
for vt, ut in tests:
    if vt == 'rand': vv = rng.standard_normal(len(z)); vv[scale == 0] = 0
    else: vv = np.zeros(len(z)); vv[int(vt[3:])] = 1.
    uu = rng.standard_normal(len(f)) if ut == 'rand' else f.copy()
    Av = mv(vv); Atu_ = rmv(uu); p1 = float(np.dot(Av, uu)); p2 = float(np.dot(vv, Atu_))
    emit(dict(event='adjtest', v=vt, u=ut, Av_u=p1, v_Atu=p2, rel_norms=(p1 - p2) / float(np.linalg.norm(Av) * np.linalg.norm(uu)),
              rel_value=(p1 - p2) / max(abs(p1), 1e-300), scale_v=float(scale[int(vt[3:])]) if vt != 'rand' else None))
emit(dict(event='end'))
