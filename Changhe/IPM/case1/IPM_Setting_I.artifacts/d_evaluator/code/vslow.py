"""Verifier's check of the slow-manifold coefficient at P (lead analysis 13.5a; numerics NOTES 00:03Z item 4): with
W_1 = A xi + a2 y^2 + ... and W_2 = h y + ... near P = (x*, 0), the slow invariant curve is xi = kappa y^2 + ...,
kappa = a2/(2h - A). Own inverse via vcand.main. a2 = (1/2) d_y^2 U_1 at P, from polar data on the grid:
d_y^2 f(r, 0) = f_r/r + f_tt/r^2 for f even in theta (the c_l x part contributes 0); f_tt by 4th-order differences in
theta using evenness, f_r by 4th-order differences on the radial grid (log-uniform), then interpolated to r = x*.
Usage: python3 vslow.py field.npz Mmax
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main
from vcand import load_modes

path, Mmax = sys.argv[1], int(sys.argv[2])
out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
d, g, ms, F = load_modes(path, Mmax)
r = g.r
Nt = out['Nt']
dt = 2 * np.pi / Nt
U1 = ev.Ur * np.cos(2 * np.pi * np.arange(Nt) / Nt)[None, :] - ev.Ut * np.sin(2 * np.pi * np.arange(Nt) / Nt)[None, :]
f0, f1, f2 = U1[:, 0], U1[:, 1], U1[:, 2]
ftt = (-2 * f2 + 32 * f1 - 30 * f0) / (12 * dt ** 2)
s = np.log(r)
fs = np.gradient(f0, s, edge_order=2)
fr = fs / r
uyy = fr / r + ftt / r ** 2
cl = ev.c_l
w = cl * r + f0
i = np.nonzero((w[:-1] * w[1:] < 0) & (r[:-1] > 0.5))[0]
res = dict(file=path, c_l=cl)
for k in i[:3]:
    xs = r[k] - w[k] * (r[k + 1] - r[k]) / (w[k + 1] - w[k])
    j = slice(k - 6, k + 8)
    a2 = 0.5 * float(np.interp(xs, r[j], uyy[j]))
    wx = np.gradient(w, r, edge_order=2)
    A = float(np.interp(xs, r[j], wx[j]))
    W2y = cl + float(np.interp(xs, r[j], (ev.Ur[:, 1] * np.sin(dt) + ev.Ut[:, 1] * np.cos(dt))[j])) / (xs * np.sin(dt))
    res.setdefault('P', []).append(dict(x_star=float(xs), A=A, h=W2y, a2=a2, kappa=a2 / (2 * W2y - A),
                                        kappa_h1=a2 / (2 - A), divW=A + W2y, two_cl=2 * cl))
print(json.dumps(res, indent=1))
