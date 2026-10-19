"""V80: specification v4.1 M26(h) exact-T test with my exit map (code/fwdstat.py, my velocity of the imported state, arclength orbits;
t orbits too when min alpha > 0) on a lead/numerics-format state (g, lr, th, x with p last). Import: cubic spline in log r,
periodic cubic in th when the angle count differs; rho = 0 inside the state's lr range. Reported:
 (i) m1 (my moment) of T rho minus m1 of rho, and the same with T rho substituted only in one t band (band split of dm1);
 (ii) max |log(T rho / rho)| over my grid points with g > 1e-3 ring max, by t band, split into the weak-axis sectors
     |sin th| < sin 6 deg and the rest; with the angle and t of each maximum; and the 99th percentile.
Usage: python3 tests/v80_xT.py STATE.npz [nt (default: the state's)] [tmin (-14)] [hs (0.03)]"""
import sys, math, json, time, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g0, lr0, th0 = d['g'], d['lr'], d['th']; X = d['x'] if 'x' in d.files else d['X']
p = float(X[-1]); par = np.array(X[:-1], dtype=float)
nt = int(sys.argv[2]) if len(sys.argv) > 2 else len(th0); tmin = float(sys.argv[3]) if len(sys.argv) > 3 else -14.0
hs = float(sys.argv[4]) if len(sys.argv) > 4 else 0.03
jj = np.arange(1, len(par) + 1)
def A(t):
    ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*t[None, :]), np.cos(jj[:, None]*t[None, :]))
    return np.cos(t)**2*np.exp(par @ ph)
F = FwdStat(p, A, tmin=tmin, tmax=10, ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    G = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([G, G[:, :1]], 1), axis=1, bc_type='periodic')(thn)
G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
F.hs = hs; F.nmax = 8000
m1s = F.node(rho)['m1']
al, be, _, _ = F.fields(rho)
out = dict(state=fn.split('/')[-1], p=p, K=len(par), nt=nt, tmin=tmin, m1_state=round(m1s, 6), min_alpha=round(float(al.min()), 4))
t1 = time.time(); F.smode = True
Ts, _ = F.T(rho); out['time_s'] = round(time.time() - t1, 1); out['trace'] = F.last_trace
def report(Tr, tag):
    res = dict(dm1=float('%.3g' % (F.node(Tr)['m1'] - m1s)))
    split = {}
    for lo, hi in ((-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, 10)):
        msk = torch.tensor((lrr >= lo) & (lrr < hi), device='cuda')[:, None]
        split['%g..%g' % (lo, hi)] = float('%.2g' % (F.node(torch.where(msk, Tr, rho))['m1'] - m1s))
    res['dm1_band'] = split
    gg = rho.cpu().numpy(); tt = Tr.cpu().numpy()
    ok = gg > 1e-3*np.abs(gg).max(1, keepdims=True)
    with np.errstate(divide='ignore', invalid='ignore'):
        lq = np.where(ok, np.log(np.abs(tt/gg)), 0.0)
    lq = np.where(np.isfinite(lq), lq, 9.99)
    wk = np.abs(np.sin(thn)) < math.sin(math.radians(6.0))
    deg = np.degrees(thn); tab = {}
    for lo, hi in ((-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, 0), (0, 9)):
        mi = (lrr >= lo) & (lrr < hi)
        for nm, mj in (('weak', wk), ('rest', ~wk)):
            z = np.abs(lq[np.ix_(mi, mj)]); a_, b_ = np.unravel_index(np.argmax(z), z.shape)
            zo = z[ok[np.ix_(mi, mj)]]
            tab['%g..%g %s' % (lo, hi, nm)] = [float('%.3g' % z[a_, b_]), round(float(lrr[mi][a_]), 2), round(float(deg[mj][b_]), 2),
                                              float('%.2g' % (np.percentile(zo, 99) if zo.size else 0.0))]
    res['max|log(T/rho)| [max, t, deg, p99]'] = tab
    res['max|T-rho|/r^p'] = float('%.3g' % float(((Tr - rho)/F.R**p).abs().max()))
    out[tag] = res
report(Ts, 'arclength')
if float(al.min()) > 0:
    F.smode = False; Tt, _ = F.T(rho); report(Tt, 't_orbits')
    out['max|Ts-Tt|/r^p'] = float('%.3g' % float(((Ts - Tt)/F.R**p).abs().max()))
for k, v in out.items():
    if isinstance(v, dict) and 'dm1' in v:
        for k2, v2 in v.items(): print(k, k2, json.dumps(v2), flush=True)
    else: print(k, json.dumps(v), flush=True)
