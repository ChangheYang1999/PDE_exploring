"""V108 (lead team notes 10:45Z, revised V102b request (2)): where the x-odd Ritz vector u of tests/v108_xodd_mode.py
sits, in the Arnoldi norm sum (u / r^p)^2 over the nodes and in the dt-weighted norm int int (u / r^p)^2 dt dth (Gauss
weights in r divided by r; the core panel [0, e^tmin] reported with its own weight). Regions (disjoint): node core
log r < -10; slow windows 75-100 deg and 260-285 deg (= -100..-75 deg) with log r >= -10; bulk = the rest. Also the
fractions by t band within each region. CPU, one thread.
Usage: python3 tests/v108c_sectors.py MODE.npz [MODE2.npz ...]"""
import sys, json, numpy as np
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); u = d['u']; r = d['r']; th = d['th']; p = float(d['p'])
    args = json.loads(str(d['args'])); src = np.load(args['source'], allow_pickle=True); sa = json.loads(str(src['args']))
    tmin = float(sa.get('tmin', -12)); tmax = float(sa.get('tmax', 10)); ppu = int(sa.get('ppu', 3))
    npan = int(round((tmax - tmin)*ppu)); edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, npan + 1))])
    xg, wg = np.polynomial.legendre.leggauss(8)
    rr = np.concatenate([(a + b)/2 + (b - a)/2*xg for a, b in zip(edges[:-1], edges[1:])])
    ww = np.concatenate([(b - a)/2*wg for a, b in zip(edges[:-1], edges[1:])])
    assert rr.shape == r.shape and np.allclose(rr, r)
    t = np.log(r); deg = np.degrees(th) % 360
    U = (u/r[:, None]**p)**2; Uw = U*(ww/r)[:, None]
    core = t < -10
    win = ((deg >= 75) & (deg < 100)) | ((deg >= 260) & (deg < 285))
    regs = dict(core_lr_lt_m10=core[:, None] & np.ones_like(win)[None, :], windows=(~core)[:, None] & win[None, :])
    regs['bulk'] = ~(regs['core_lr_lt_m10'] | regs['windows'])
    out = dict(mode=fn.split('/')[-1], lam=float(d['lam']), nt=len(th), tmin=tmin)
    for nm, Z in (('node_norm', U), ('dt_norm', Uw)):
        tot = Z.sum(); out[nm] = {k: round(float(Z[m].sum()/tot), 4) for k, m in regs.items()}
        bands = [(-99, tmin), (tmin, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 99)]
        out[nm + '_band'] = {'%g..%g' % (a, b): [round(float(Z[(t >= a) & (t < b)].sum()/tot), 4),
                                                 round(float(Z[((t >= a) & (t < b))[:, None] & win[None, :]].sum()/tot), 4)]
                             for a, b in bands}
    i, j = np.unravel_index(np.argmax(np.abs(u)/r[:, None]**p), u.shape)
    out['argmax_u_over_rp'] = [round(float(t[i]), 2), round(float(deg[j]), 1)]
    print('SECTORS ' + json.dumps(out), flush=True)
