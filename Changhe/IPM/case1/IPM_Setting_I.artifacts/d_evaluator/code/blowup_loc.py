"""Localize the DR blowup in r and theta from dense snapshots (verifier diagnostic)."""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vpolar import LogGrid

d = np.load(sys.argv[1], allow_pickle=True)
r, ms, Fs, taus = d['r'], d['ms'], d['F'], d['tau']
g = LogGrid(len(r), r[0], r[-1])
u = np.log(r)
f3 = Fs[:, 1]
# cumulative c by band: int f_3 r^{-2} dr = int f_3/r du
edges = [r[0], 1e-2, 1.0, 10.0, 100.0, 1e4, r[-1]]
th = np.linspace(0, np.pi / 2, 91)
S = np.sin(np.outer(ms, th))
iref = 0
for i, tau in enumerate(taus):
    band = []
    for a, b in zip(edges[:-1], edges[1:]):
        sel = (r >= a) & (r <= b)
        band.append(float(np.trapezoid(f3[i, sel] / r[sel], u[sel])))
    rho = Fs[i].T @ S                    # (N, nth)
    drho = (Fs[i] - Fs[iref]).T @ S
    sc = r[:, None] ** 3 / (1 + r[:, None] ** 2) ** ((3 - 0.67) / 2)   # initial-envelope scale
    rel = np.abs(drho) / sc
    j, t = np.unravel_index(np.argmax(rel), rel.shape)
    jr, tr = np.unravel_index(np.argmax(np.abs(rho) / sc), rho.shape)
    # high-m share by radius: sum_{m>=M/2} |f_m| / sum |f_m|
    hm = np.abs(Fs[i][len(ms) // 2:]).sum(0) / (np.abs(Fs[i]).sum(0) + 1e-300)
    jh = np.argmax(hm)
    print(json.dumps(dict(tau=round(float(tau), 3), cl=round(float(d['cl'][i]), 4),
                          c_bands=[round(x, 4) for x in band],
                          dmax_r=float('%.3g' % r[j]), dmax_th_deg=float(np.degrees(th[t])), dmax=float('%.3g' % rel[j, t]),
                          rhomax_r=float('%.3g' % r[jr]), rhomax_th=float(np.degrees(th[tr])), rhomax=float('%.3g' % (np.abs(rho)/sc)[jr, tr]),
                          hm_max=float('%.3g' % hm[jh]), hm_r=float('%.3g' % r[jh]))), flush=True)
