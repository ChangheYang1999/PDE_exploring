# Lead exploration: structure of a forward (P0) steady state: residual location, zeros of Y, level sets near the origin.
import sys, numpy as np
sys.path.insert(0, '.')
import p0_forward as P1, p0_forward2 as P2
d = np.load(sys.argv[1]); f, rho, th = d['f'], d['rho'], d['th']
r = np.exp(rho); Nr, Nth = f.shape; drho = rho[1] - rho[0]
wr, wt = P2.velocity(f, rho, th)
Yr = r[:, None] + wr; Yt = wt
fr = P1.d_rho(f, drho) / r[:, None]; ft = P1.d_th(f) / r[:, None]   # physical d_r f, (1/r) d_th f
res = Yr * fr + Yt * ft
i, j = np.unravel_index(np.argmax(np.abs(res)), res.shape)
print('max |Y.grad f| = %.3g at r=%.4g th=%.3f (f=%.3f, |grad f|=%.3g, |Y|=%.3g)' % (abs(res[i, j]), r[i], th[j], f[i, j], np.hypot(fr[i, j], ft[i, j]), np.hypot(Yr[i, j], Yt[i, j])))
# relative residual |Y.grad f|/(|Y||grad f|)
rel = np.abs(res) / (np.hypot(Yr, Yt) * np.hypot(fr, ft) + 1e-30)
print('fraction of points with rel residual > 0.1:', float((rel > 0.1).mean()))
# |Y| small region (stagnation set), excluding r<1e-2
Ym = np.hypot(Yr, Yt) / r[:, None]
for thr in [0.02, 0.05, 0.1]:
    msk = (Ym < thr) & (r[:, None] > 1e-2) & (r[:, None] < 50)
    if msk.any():
        ii, jj = np.nonzero(msk)
        print('|Y|/r < %g: %d pts, r in [%.3g, %.3g], th in [%.3f, %.3f], f in [%.3f, %.3f]' % (thr, msk.sum(), r[ii].min(), r[ii].max(), th[jj].min(), th[jj].max(), f[msk].min(), f[msk].max()))
    else:
        print('|Y|/r < %g: none' % thr)
# angular profile of f on a few circles
for rr in [0.05, 0.2, 0.5, 1, 2, 5, 20]:
    k = np.searchsorted(r, rr)
    row = f[k]
    print('r=%.3g: f(th) at th=0,30,60,90,120,150,180,270 deg:' % r[k], ' '.join('%.3f' % row[int(round(a / 360 * Nth)) % Nth] for a in [0, 30, 60, 90, 120, 150, 180, 270]))
# Y on the x axis and the y axis near 0
for rr in [0.01, 0.05, 0.2, 0.5, 1.0]:
    k = np.searchsorted(r, rr)
    print('r=%.3g Y/r at th=0: (%.3f, %.3f)  th=90: (%.3f, %.3f)  th=270: (%.3f, %.3f)' % (r[k], Yr[k, 0] / r[k], Yt[k, 0] / r[k], Yr[k, Nth // 4] / r[k], Yt[k, Nth // 4] / r[k], Yr[k, 3 * Nth // 4] / r[k], Yt[k, 3 * Nth // 4] / r[k]))
