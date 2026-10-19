# Lead (2026-10-18): strain-moment m1 (numerics' identity I2: psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX,
# outer tail rho ~ r^p A(th)), compared with the ring fit m1(r) -> r = 0 (ringx.py). Usage: python3 mstrain.py state.npz p
import sys, json
import numpy as np
st = np.load(sys.argv[1]); p = float(sys.argv[2]); l = 1 / p
g, lr, th = st['g'], st['lr'], st['th']
r = np.exp(lr); d = lr[1] - lr[0]; dth = th[1] - th[0]
rho = (r ** p)[:, None] * g
w = (1 / r)[:, None] * d * dth / np.pi
c_grid = float((rho * np.sin(3 * th)[None, :] * w).sum()); d_grid = float((rho * np.cos(3 * th)[None, :] * w).sum())
a3s = float((g[-1] * np.sin(3 * th)).sum() * dth / np.pi); a3c = float((g[-1] * np.cos(3 * th)).sum() * dth / np.pi)
tail = r[-1] ** (p - 1) / (1 - p)
# inner part r < r_min with rho ~ r^2 c2(th): int_0^rmin r^-2 rho dr = rmin * c2 ; estimate c2 from the first ring
c2 = rho[0] / r[0] ** 2
inner = float((c2 * np.sin(3 * th)).sum() * dth / np.pi * r[0])
c = c_grid + a3s * tail
print(json.dumps(dict(c_grid=c_grid, tail=a3s * tail, inner_est=inner, m1_mom=l - c, m1_mom_inner=l - c - inner,
                      d_mom=d_grid + a3c * tail, lr0=float(lr[0]), lr1=float(lr[-1]))))
