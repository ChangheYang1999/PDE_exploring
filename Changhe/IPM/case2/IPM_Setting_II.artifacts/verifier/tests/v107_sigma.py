"""V107 (specification v4.10 M28(k), lead 10:14Z, "NOT verifier-checked"): local radial exponent sigma = d log rho / d log r on fixed rays
of own-format panel states, by exact differentiation of the degree-7 Lagrange interpolant of log rho on each t-panel (8 Gauss
nodes per panel, panels of width 1/ppu from tmin to tmax; the core panel r < e^tmin is not used). Independent of the lead's
np.gradient on the nodes. Reports, on th = 0: sigma at lr -13.5 .. 9.5, every crossing of the levels 1.9 / 1.0 / 0.6, the lr ranges
with |sigma - 2| < 0.05 and |sigma - p| < 0.05, the minimum and its location, the smallest range of sigma over a window of width 1
in lr inside [-12, -2] (a plateau test), the largest jump of sigma across a panel edge; and min sigma over 30-85 deg at lr -3 .. -2.
CPU, numpy only. Usage: python3 tests/v107_sigma.py OWN.npz [OWN2.npz ...]"""
import sys, json, numpy as np
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); a = json.loads(str(d['args'])); p = float(d['p'])
    r = d['r']; th = d['th']; rho = d['rho']; nt = len(th)
    tmin = float(a.get('tmin', -14)); tmax = float(a.get('tmax', 10)); ppu = int(a.get('ppu', 3)); q = 8
    t = np.log(r); i0 = int(np.sum(t < tmin - 1e-12)); npan = int(round((tmax - tmin)*ppu))
    assert len(t) == i0 + q*npan, (len(t), i0, npan)
    nf = 41
    def sig_ray(j):
        T = []; S = []; jumps = []
        prev = None
        for k in range(npan):
            tk = t[i0 + q*k: i0 + q*(k + 1)]; v = np.log(rho[i0 + q*k: i0 + q*(k + 1), j])
            a0 = tmin + k/ppu; a1 = a0 + 1.0/ppu; c = (a0 + a1)/2; h = (a1 - a0)/2
            P = np.polynomial.polynomial.polyfit((tk - c)/h, v, q - 1)
            dP = np.polynomial.polynomial.polyder(P)
            u = np.linspace(-1, 1, nf); s = np.polynomial.polynomial.polyval(u, dP)/h
            if prev is not None: jumps.append((abs(s[0] - prev), a0))
            prev = s[-1]
            T.append(c + h*u); S.append(s)
        return np.concatenate(T), np.concatenate(S), max(jumps)
    out = dict(state=fn.split('/')[-1], par=a.get('par', a.get('source')), p=p, nt=nt, tmin=tmin, ppu=ppu)
    T, S, jmp = sig_ray(0)
    out['edge_jump_max_th0'] = [float('%.2g' % jmp[0]), round(jmp[1], 2)]
    grid = np.arange(-13.5, 9.6, 1.0)
    out['sigma_th0'] = {('%g' % L): round(float(np.interp(L, T, S)), 3) for L in grid if tmin < L < tmax}
    cr = {}
    for lev in (1.9, 1.0, 0.6):
        z = np.where(np.diff(np.sign(S - lev)) != 0)[0]
        cr['%g' % lev] = [round(float(T[k] + (lev - S[k])*(T[k+1] - T[k])/(S[k+1] - S[k])), 2) for k in z if S[k+1] != S[k]]
    out['crossings_th0'] = cr
    for nm, val in (('near2', 2.0), ('nearp', p)):
        m = np.abs(S - val) < 0.05
        out[nm] = [round(float(T[m].min()), 2), round(float(T[m].max()), 2)] if m.any() else None
    m = (T > tmin + 0.01) & (T < tmax - 0.01); k = int(np.argmin(S[m]))
    out['min_th0'] = [round(float(S[m][k]), 3), round(float(T[m][k]), 2)]
    best = (9, None)
    for L0 in np.arange(-12, -2.999, 0.05):
        w = (T >= L0) & (T <= L0 + 1)
        rg = float(S[w].max() - S[w].min())
        if rg < best[0]: best = (rg, L0)
    out['min_range_width1_in_-12_-2'] = [round(best[0], 3), round(float(best[1]), 2)]
    lo = float(np.interp(1.9, S[::-1], T[::-1])) if False else None
    k19 = np.where(S < 1.9)[0][0]; k06 = np.where(S < 0.6)[0][0]
    best = (9, None)
    for L0 in np.arange(T[k19], T[k06] - 1 + 1e-9, 0.05):
        w = (T >= L0) & (T <= L0 + 1); rg = float(S[w].max() - S[w].min())
        if rg < best[0]: best = (rg, L0)
    out['min_range_width1_between_1.9_and_0.6'] = [round(best[0], 3), round(float(best[1]), 2)] if best[1] is not None else None
    bad = np.where((np.abs(S - p) >= 0.05) & (T < tmax - 0.01))[0]
    out['lr_after_which_|sigma-p|<0.05'] = round(float(T[bad[-1]]), 2) if len(bad) else None
    bad = np.where((np.abs(S - p) >= 0.02) & (T < tmax - 0.01))[0]
    out['lr_after_which_|sigma-p|<0.02'] = round(float(T[bad[-1]]), 2) if len(bad) else None
    ang = {}
    for deg in (30, 45, 60, 75, 85):
        j = int(round(np.deg2rad(deg)/(th[1] - th[0]))); Tj, Sj, _ = sig_ray(j)
        w = (Tj >= -3) & (Tj <= -2); k = int(np.argmin(Sj[w]))
        ang['%d' % deg] = [round(float(np.interp(-2.5, Tj, Sj)), 3), round(float(Sj[w][k]), 3), round(float(Tj[w][k]), 2)]
    out['deg: sigma(-2.5), min on -3..-2 (lr)'] = ang
    w = (T >= -8) & (T <= -4); sl = np.polyfit(T[w], S[w], 1)[0]
    out['slope_dsigma_dlr_-8_-4'] = round(float(sl), 3)
    mn = (9, None, None)
    for deg in range(30, 86):
        j = int(round(np.deg2rad(deg)/(th[1] - th[0])))
        Tj, Sj, _ = sig_ray(j); w = (Tj >= -3) & (Tj <= -2); k = int(np.argmin(Sj[w]))
        if Sj[w][k] < mn[0]: mn = (float(Sj[w][k]), float(Tj[w][k]), deg)
    out['min_sigma_30-85deg_lr-3_-2'] = [round(mn[0], 3), round(mn[1], 2), mn[2]]
    print('SIGMA ' + json.dumps(out), flush=True)
