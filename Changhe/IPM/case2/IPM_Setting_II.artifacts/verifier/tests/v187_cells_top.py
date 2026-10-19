"""V187: the cells that dominate the odd core product at eps_rel 1e-5 and 1.78e-5 (runs/v187_cells.npz)."""
import numpy as np
d = np.load('runs/v187_cells.npz'); ers = d['ers']; lr = d['lr']; sc = d['scale']; nu = float(d['nu']); fl = d['flip']
Tg0 = d['Tg0']; TH0 = d['TH0']; A0 = d['A0']; ok = A0 > 0; Tt0 = np.where(ok, d['Tt0'], 0.0)
th = np.arange(512) * 2 * np.pi / 512
for k in (6, 8, 9, 12, 16):
    er = ers[k]; e = er * nu
    dT = (d['Tg'][k] - Tg0) / sc[:, None]; C = 0.5 * (dT - dT[:, fl]) / e
    dTt = np.where(ok, d['Tt'][k] - Tt0, 0.0); dTH = d['TH'][k] - TH0; dlA = np.where(ok, np.log(np.maximum(d['A'][k], 1e-300) / np.maximum(A0, 1e-300)), 0)
    w = C ** 2; idx = np.argsort(w.ravel())[::-1]
    tot = w.sum(); cum = np.cumsum(w.ravel()[idx]) / tot
    n50 = int(np.searchsorted(cum, 0.5)) + 1; n90 = int(np.searchsorted(cum, 0.9)) + 1
    print('eps_rel %.2e: |C|core %.3e; cells holding 50 / 90 %% of |C|^2: %d / %d of %d; dth1 %.3e' % (er, np.sqrt(tot), n50, n90, C.size, np.radians(d['th1'][k]) - np.radians(float(d['th10']))))
    for q in idx[:6]:
        i, j = divmod(q, 512)
        print('   lr %.3f th %.2f deg | C %.3e | Tt0 %.3f dTt %.3e | TH0 %.4f deg dTH %.3e | dlogA %.3e | T0/sc %.3e | mirror j %d: dTt %.3e dlogA %.3e' % (
            lr[i], np.degrees(th[j]), C[i, j], Tt0[i, j], dTt[i, j], np.degrees(TH0[i, j]), dTH[i, j], dlA[i, j], Tg0[i, j] / sc[i], fl[j], dTt[i, fl[j]], dlA[i, fl[j]]))
