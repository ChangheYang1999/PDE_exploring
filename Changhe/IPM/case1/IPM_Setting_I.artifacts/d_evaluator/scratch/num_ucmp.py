# Compare the verifier's velocity (own inverse, vcand/vresid on the imported rho) with the exporter's U1, U2 at the
# exporter's node radii and midpoint angles, and split the verifier's transport residual into the part due to the
# velocity difference. Usage (from code/): python3 ../scratch/num_ucmp.py imported.npz export.npz Mmax
import sys, json
import numpy as np
from scipy.interpolate import CubicSpline
from vcand import main as vcand_main
imp, exp_, Mmax = sys.argv[1], sys.argv[2], int(sys.argv[3])
out, ev, ax = vcand_main(imp, {'Mmax': Mmax, 'b3': False})
z = np.load(exp_, allow_pickle=True)
r, th = ev.g.r if hasattr(ev, 'g') else None, None
d = np.load(imp)
rg = d['r']; Nt = 4 * (Mmax + 1); thg = 2 * np.pi * np.arange(Nt) / Nt
re_, te = z['r'], z['theta']
jt = np.rint(te / (2 * np.pi / Nt)).astype(int)
assert np.allclose(thg[jt], te)
sel = (re_ > rg[8]) & (re_ < rg[-9])
lr = np.log(rg)
def at(F):
    return CubicSpline(lr, F[:, jt], axis=0)(np.log(re_[sel]))
Ur, Ut, rr, rt, Rv, Nv = at(ev.Ur), at(ev.Ut), at(ev.rho_r), at(ev.rho_t), at(ev.R), at(ev.Rnorm)
ct, st = np.cos(te)[None, :], np.sin(te)[None, :]
U1, U2 = Ur * ct - Ut * st, Ur * st + Ut * ct
E1, E2 = z['U1'][sel], z['U2'][sel]
R2 = re_[sel][:, None]
rx = ct * rr - st * rt / R2; ry = st * rr + ct * rt / R2
dU = np.hypot(U1 - E1, U2 - E2) / (np.hypot(E1, E2).max(axis=1)[:, None] + 1e-300)
dterm = ((E1 - U1) * rx + (E2 - U2) * ry) / Nv            # residual change if the exporter's U replaced mine
Rth = Rv / Nv + dterm
xs = 8.6
dP = np.hypot(R2 * ct - out.get('x_star', xs), R2 * st)
bands = [(0.1, 2), (2, 10), (10, 100), (100, 1000), (1000, 1e9)]
res = dict(file=exp_, c_l=out['c_l'], cl_exporter=float(z['c_l']))
rows = []
for a, b in bands:
    m = (R2 >= a) & (R2 < b) & np.ones_like(dU, bool)
    if m.sum() == 0: continue
    rows.append(dict(band=[a, b], dU_rel_max=float(dU[m].max()), mine_Nv_max=float(np.abs(Rv / Nv)[m].max()),
                     mine_Nv_rms=float(np.sqrt(np.mean((Rv / Nv)[m] ** 2))), dterm_max=float(np.abs(dterm)[m].max()),
                     with_exporterU_max=float(np.abs(Rth)[m].max()), with_exporterU_rms=float(np.sqrt(np.mean(Rth[m] ** 2)))))
for a, b in [(0, 0.5), (0, 2), (2, 4)]:
    m = (dP >= a) & (dP < b)
    rows.append(dict(shell=[a, b], dU_rel_max=float(dU[m].max()), mine_Nv_max=float(np.abs(Rv / Nv)[m].max()),
                     dterm_max=float(np.abs(dterm)[m].max()), with_exporterU_max=float(np.abs(Rth)[m].max())))
res['rows'] = rows
for q in rows: print({k: (round(v, 9) if isinstance(v, float) else v) for k, v in q.items()})
