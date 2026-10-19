"""V187: the same scan for the FIXED-DATUM map (datum zeros held at the base values th1 = 90, th2 = 270 deg; numerics
option slave=0): T_fixed(e) = exp(-Tt(e)) e^(p hi) A(TH(e); th1_0, th2_0) / r^p, formed from the stored exit angles and
travel times of runs/v187_cells.npz (A_fixed = A(e) times the ratio of the zero factors). Band norms of the odd product,
its concentration in cells, and the same without the cells that switch exit branch (and their mirrors)."""
import numpy as np
d = np.load('runs/v187_cells.npz'); ers = d['ers']; lr = d['lr']; sc = d['scale']; nu = float(d['nu']); fl = d['flip']
Tg0 = d['Tg0']; TH0 = d['TH0']; A0 = d['A0']; ok = A0 > 0
t10 = np.radians(float(d['th10'])); t20 = np.radians(float(d['th20']))
z = lambda TH, a, b: np.sin(0.5 * (TH - a)) ** 2 * np.sin(0.5 * (TH - b)) ** 2
bands = [(-14, -12), (-12, -10), (-10, -8)]
up0 = np.sin(TH0) > 0
for name, fixed in (('slaved', False), ('fixed', True)):
    print('%s datum:' % name)
    for k, er in enumerate(ers):
        e = er * nu; TH = d['TH'][k]; t1 = np.radians(d['th1'][k]); t2 = np.radians(d['th2'][k])
        if fixed:
            Tg = np.where(ok, d['Tg'][k] * z(TH, t10, t20) / np.maximum(z(TH, t1, t2), 1e-300), 0.0)
            # axis cells (A0 = 0): T_fixed = exp(-Tt) e^(p hi) A_fixed / r^p cannot be recovered from the stored product; they are self-mirror and drop out of the odd part
        else:
            Tg = d['Tg'][k]
        dT = (Tg - Tg0) / sc[:, None]; C = 0.5 * (dT - dT[:, fl]) / e
        sw = (np.sin(TH) > 0) != up0; msw = sw | sw[:, fl]
        w = (C ** 2).ravel(); idx = np.argsort(w)[::-1]; cum = np.cumsum(w[idx]) / w.sum(); n50 = int(np.searchsorted(cum, 0.5)) + 1
        bn = [np.linalg.norm(C[(lr >= a) & (lr < b)]) for a, b in bands]
        bs = [np.linalg.norm(np.where(msw, 0, C)[(lr >= a) & (lr < b)]) for a, b in bands]
        if fixed:
            m = np.broadcast_to(((lr >= -14) & (lr < -12))[:, None], C.shape); i, j = divmod(int(idx[0]), 512)
            extra = ' | top cell lr %.3f th %.2f deg: delta0 %.3e, TH - th1_0 %.3e, T/T0 %.3f' % (lr[i], j * 360 / 512, TH0[i, j] - t10 if np.sin(TH0[i, j]) > 0 else TH0[i, j] - t20, (TH[i, j] - t10) if np.sin(TH[i, j]) > 0 else (TH[i, j] - t20), Tg[i, j] / Tg0[i, j])
        else:
            extra = ''
        print('  eps_rel %.2e: band |C| %s | 50%% of |C|^2 in %d cells | switched %d | band |C| without switched %s' % (er, ' '.join('%.3e' % x for x in bn), n50, sw.sum(), ' '.join('%.3e' % x for x in bs)) + extra)
