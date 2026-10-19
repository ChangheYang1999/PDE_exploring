# Lead: local radial exponent sigma = d log rho / d log r along fixed rays of a verifier panel state
# (rho on Gauss nodes per log-panel, as written by the verifier's fwdstat code). Prints sigma at integer-ish lr for rays th = 0, 30, 60, 85 deg
# and the plateau summary on th = 0. Usage: python3 sigma.py state.npz [state2.npz ...]
import sys, json, numpy as np
for f in sys.argv[1:]:
    d = np.load(f, allow_pickle=True); a = json.loads(str(d['args'])); p = float(a['p'])
    rho, r, th = d['rho'], d['r'], d['th']
    lr = np.log(r)
    print('==', f.split('/')[-1], 'p', p, 'par', a['par'])
    rows = []
    for deg in (0, 30, 60, 85):
        j = int(round(np.deg2rad(deg) / (th[1] - th[0])))
        # average the x-even pair th and pi - th to remove nothing (x-even states): use th itself
        v = np.log(np.maximum(rho[:, j], 1e-300))
        s = np.gradient(v, lr)
        rows.append((deg, s))
    grid = np.arange(-13.5, 9.6, 1.0)
    print('   lr   ' + ' '.join('%7s' % ('%d deg' % dg) for dg, _ in rows))
    for L in grid:
        k = np.argmin(abs(lr - L))
        print('%6.2f ' % lr[k] + ' '.join('%7.3f' % s[k] for _, s in rows))
    s0 = rows[0][1]
    near2 = lr[np.abs(s0 - 2) < 0.05]; nearp = lr[np.abs(s0 - p) < 0.05]
    print('   th=0: |sigma-2|<0.05 on lr in [%.2f, %.2f] (count %d); |sigma-p|<0.05 on lr in [%.2f, %.2f] (count %d)' % (
        near2.min() if len(near2) else np.nan, near2.max() if len(near2) else np.nan, len(near2),
        nearp.min() if len(nearp) else np.nan, nearp.max() if len(nearp) else np.nan, len(nearp)))
    # minimum of sigma between core and far field
    m = (lr > -14) & (lr < 9)
    k = np.argmin(s0[m]); print('   th=0: min sigma %.3f at lr %.2f; max %.3f at lr %.2f' % (s0[m][k], lr[m][k], s0[m].max(), lr[m][np.argmax(s0[m])]))
