"""V187: exit branch (upper Gamma near 90 deg / lower near 270 deg) of the core cells of the base state, the boundary
between the two branch regions (separatrix), the cells that switch branch at each eps, and the distance (in cells)
of the dominant cells of the odd product from the boundary (runs/v187_cells.npz)."""
import numpy as np
d = np.load('runs/v187_cells.npz'); ers = d['ers']; lr = d['lr']; sc = d['scale']; nu = float(d['nu']); fl = d['flip']
TH0 = d['TH0']; Tg0 = d['Tg0']; thd = np.arange(512) * 360 / 512
up0 = np.sin(TH0) > 0                                     # exits near the upper branch
# boundary cells: a cell whose angular neighbour exits on the other branch
bnd = (up0 != np.roll(up0, 1, axis=1)) | (up0 != np.roll(up0, -1, axis=1))
for i in range(0, 180, 30):
    js = np.nonzero(up0[i] != np.roll(up0[i], -1))[0]
    print('lr %.3f: branch changes between angles (deg) %s' % (lr[i], ' '.join('%.2f|%.2f' % (thd[j], thd[(j + 1) % 512]) for j in js)))
print('boundary cells: %d of %d' % (bnd.sum(), bnd.size))
ang = np.minimum.reduce([np.abs(((np.arange(512)[None, :] - np.nonzero(bnd[i])[0][:, None] + 256) % 512) - 256).min(0) if bnd[i].any() else np.full(512, 999) for i in range(1)])
def dist_to_bnd(i, j):
    jb = np.nonzero(bnd[i])[0]
    return int(np.min(np.abs((jb - j + 256) % 512 - 256))) if len(jb) else 999
for k, er in enumerate(ers):
    sw = (np.sin(d['TH'][k]) > 0) != up0
    e = er * nu; dT = (d['Tg'][k] - Tg0) / sc[:, None]; C = 0.5 * (dT - dT[:, fl]) / e
    w = (C ** 2).ravel(); idx = np.argsort(w)[::-1]; cum = np.cumsum(w[idx]) / w.sum(); n50 = int(np.searchsorted(cum, 0.5)) + 1
    top = [divmod(q, 512) for q in idx[:n50]]
    dists = [dist_to_bnd(i, j) for i, j in top]
    msw = np.zeros_like(sw); msw = sw | sw[:, fl]
    Cs = np.where(msw, 0.0, C)
    print('eps_rel %.2e: cells switching branch %d; |C|core %.3e, without switched cells (and mirrors) %.3e; 50%% of |C|^2 in %d cells, their distance to the boundary (cells) %s' % (
        er, sw.sum(), np.linalg.norm(C), np.linalg.norm(Cs), n50, dists[:8]))
