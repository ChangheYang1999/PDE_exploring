"""V208: my defect of the states returned by the numerics amplitude continuation 2(b) (numerics runs/pfwd/par/AC512_t*_s+1.npz,
notes to the lead analyst 21:51Z item 2), under the Gamma-slaved exit map as the numerics define it (code/pfwd_parity.py docstring):
    A(th) = 4 sin^2((th - th_1)/2) sin^2((th - th_2)/2) exp(sum a_j phi_j + sum b_j chi_j), phi: sin(n th) n odd, cos(n th) n even;
    chi: cos(n th) n odd, sin(n th) n even; th_1, th_2 = exits of the strong unstable manifold of the state's velocity.
Everything else is mine: velocity (code/fwdstat.py), Gamma exits (RK4 in t from lr = -12 at 90 / 270 deg, as tests/v201_gamma_exit.py),
per-cell forward exits and travel times (FwdStat.trace_s), image Tg = e^(-s) e^(p tmax) A(TH_exit) / r^p, defect |Tg - g| / max_th g.
Usage: python3 -B tests/v211_ac_defect.py STATE.npz [STATE.npz ...]"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
F = None
for fn in sys.argv[1:]:
    t0 = time.time()
    d = np.load(fn, allow_pickle=True); g0, lr0, th0 = d['g'], d['lr'], d['th']; X = np.array(d['x'], float); p = X[-1]
    K = Ko = 16; a = X[:K]; b = X[K:K + Ko]
    if F is None:
        F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=3, q=8, nt=len(th0), dti=0.01, nstep=800)
        rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy(); p0 = p
    assert p == p0 and np.allclose(th0, thn)
    G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
    al, be, _, _ = F.fields(rho); au = F.Imat @ al; bu = F.Imat @ be
    nd = F.node(rho)
    # Gamma exits
    nstep = 2200; t1 = F.tmax; tg = -12.0; h = (t1 - tg)/nstep
    th = torch.tensor([math.pi/2, 3*math.pi/2], dtype=DT, device='cuda'); t = torch.full_like(th, tg)
    fth = lambda t, th: F.interp(bu, t, th)/F.interp(au, t, th)
    for k in range(nstep):
        k1 = fth(t, th); k2 = fth(t + h/2, th + h/2*k1); k3 = fth(t + h/2, th + h/2*k2); k4 = fth(t + h, th + h*k3)
        th = th + h/6*(k1 + 2*k2 + 2*k3 + k4); t = t + h
    th1, th2 = [float(v) % (2*math.pi) for v in th.cpu().numpy()]
    lrg = lr0[:, None]; thg = th0[None, :]
    TT = torch.tensor(np.broadcast_to(lrg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
    TH0 = torch.tensor(np.broadcast_to(thg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
    THex, sx, nbad = F.trace_s(al, be, TT, TH0, 0.03, 12000)
    T = THex.cpu().numpy(); S = sx.cpu().numpy(); n = np.arange(1, K + 1)[:, None]
    phi = np.where(n % 2 == 1, np.sin(n*T[None, :]), np.cos(n*T[None, :])); chi = np.where(n % 2 == 1, np.cos(n*T[None, :]), np.sin(n*T[None, :]))
    A = 4*np.sin(0.5*(T - th1))**2*np.sin(0.5*(T - th2))**2*np.exp(a @ phi + b @ chi)
    Tg = (np.exp(-S)*math.exp(p*F.tmax)*A).reshape(g0.shape)/np.exp(p*lrg)
    rel = np.abs(Tg - g0)/np.maximum(g0.max(1, keepdims=True), 1e-300)
    rm = g0.max(1, keepdims=True); msk = (g0 > 1e-3*rm) | (Tg > 1e-3*rm)    # the numerics' rms convention: over cells where g or Tg > 1e-3 row max
    rms_msk = float(np.sqrt((np.where(msk, rel, 0.0)**2).sum()/msk.sum()))
    flip = (len(th0)//2 - np.arange(len(th0))) % len(th0)
    godd = 0.5*(g0 - g0[:, flip]); oddrms = float(np.linalg.norm(godd)/np.linalg.norm(g0))
    bands = {}
    for nm, lo, hi in (('core', -14.01, -8), ('inner', -8, -4), ('mid', -4, 0), ('outer', 0, 10.01)):
        m = (lr0 >= lo) & (lr0 < hi); bands[nm] = [float(rel[m].max()), float(np.sqrt((rel[m]**2).mean()))]
    print(json.dumps(dict(state=fn.split('/')[-1], b1=float(b[0]), b_other_max=float(np.abs(b[1:]).max()), m1=round(nd['m1'], 6),
                          th12_deg=[math.degrees(th1), math.degrees(th2)], not_exited=nbad, defect_max=float(rel.max()),
                          defect_rms=float(np.sqrt((rel**2).mean())), defect_rms_masked=rms_msk, bands_max_rms=bands, state_odd_rel=oddrms,
                          wall=round(time.time() - t0, 1))), flush=True)
