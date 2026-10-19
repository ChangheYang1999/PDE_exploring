"""V273: independent check of numerical record R22 (d), (e) (numerics runs/pfwd/tan/LC*_resp_b1.npz, LCK*.log): is the consistent linear
response of the numerics' tangent realised by MY exit map?  Fixed-datum map as R22 defines it (code/pfwd_tangent.py docstring):
    T(g; z)(X) = e^(-tau) e^(p hi) A(theta_exit; z) / r^p,  A = 4 sin^2((th - z1)/2) sin^2((th - z2)/2) exp(F),
    F = the 16 x-even coefficients of the base (sin n th for n odd, cos n th for n even) + b_1 cos th.
Everything else is mine (as tests/v211_ac_defect.py): velocity code/fwdstat.py, per-cell forward exits and travel times (FwdStat.trace_s,
arclength steps), strong-exit angles by RK4 in t from lr = -12 at 90 / 270 deg.  Defect F = (g - Tg) / rowmax(g_base), all cells, 2-norm
(the numerics' norm without their two matching rows); x-odd part 0.5 (F - F(pi - th)).
For each eps: unperturbed (g, z0; b_1 = eps) and corrected (max(g + eps v, 0), z0 + eps dz; b_1 = eps) for each response file.
Usage: python3 -B tests/v273_r22_lin.py BASE.npz EPS_LIST RESP.npz [RESP.npz ...]"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64

base = np.load(sys.argv[1], allow_pickle=True); epss = [float(e) for e in sys.argv[2].split(',')]; resps = sys.argv[3:]
g0, lr0, th0 = base['g'], base['lr'], base['th']; X = np.array(base['x'], float); p = X[-1]; K = 16; a = X[:K]
assert np.abs(X[K:2*K]).max() == 0.0
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=3, q=8, nt=len(th0), dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
assert np.allclose(th0, thn)
rowmax = np.maximum(g0.max(1, keepdims=True), 1e-300)
flip = (len(th0)//2 - np.arange(len(th0))) % len(th0)
n = np.arange(1, K + 1)[:, None]


def trace(g):
    """exits and travel times of every cell of the numerics' grid under MY velocity of rho = r^p g; strong-exit angles."""
    G = CubicSpline(lr0, g, axis=0)(np.clip(lrr, lr0[0], lr0[-1])); G[lrr < lr0[0]] = 0.0
    rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
    al, be, _, _ = F.fields(rho); au = F.Imat @ al; bu = F.Imat @ be
    nstep = 2200; t1 = F.tmax; tg = -12.0; h = (t1 - tg)/nstep
    th = torch.tensor([math.pi/2, 3*math.pi/2], dtype=DT, device='cuda'); t = torch.full_like(th, tg)
    fth = lambda t, th: F.interp(bu, t, th)/F.interp(au, t, th)
    for k in range(nstep):
        k1 = fth(t, th); k2 = fth(t + h/2, th + h/2*k1); k3 = fth(t + h/2, th + h/2*k2); k4 = fth(t + h, th + h*k3)
        th = th + h/6*(k1 + 2*k2 + 2*k3 + k4); t = t + h
    the = [math.degrees(float(v) % (2*math.pi)) for v in th.cpu().numpy()]
    TT = torch.tensor(np.broadcast_to(lr0[:, None], g.shape).copy(), dtype=DT, device='cuda').reshape(-1)
    TH0 = torch.tensor(np.broadcast_to(th0[None, :], g.shape).copy(), dtype=DT, device='cuda').reshape(-1)
    THex, sx, nbad = F.trace_s(al, be, TT, TH0, 0.03, 12000)
    return THex.cpu().numpy(), sx.cpu().numpy(), the, int(nbad)


def defect(g, tr, z, b1):
    T, S, the, nbad = tr
    phi = np.where(n % 2 == 1, np.sin(n*T[None, :]), np.cos(n*T[None, :]))
    A = 4*np.sin(0.5*(T - z[0]))**2*np.sin(0.5*(T - z[1]))**2*np.exp(a @ phi + b1*np.cos(T))
    Tg = (np.exp(-S)*math.exp(p*F.tmax)*A).reshape(g.shape)/np.exp(p*lr0[:, None])
    D = (g - Tg)/rowmax; Do = 0.5*(D - D[:, flip])
    bands = {}
    for lo, hi in ((-14.01, -8), (-8, -4), (-4, -2), (-2, 2), (2, 10.01)):
        m = (lr0 >= lo) & (lr0 < hi); bands['[%g,%g)' % (lo, hi)] = [float(np.linalg.norm(D[m])), float(np.linalg.norm(Do[m]))]
    return dict(norm=float(np.linalg.norm(D)), norm_odd=float(np.linalg.norm(Do)), dmax=float(np.abs(D).max()), bands_norm_odd=bands,
                th_e_deg=the, not_exited=nbad)


t0 = time.time()
z0 = [math.pi/2, 3*math.pi/2]
tr0 = trace(g0)
print(json.dumps(dict(base=sys.argv[1].split('/')[-1], eps=0.0, **defect(g0, tr0, z0, 0.0), wall=round(time.time() - t0, 1))), flush=True)
for eps in epss:
    print(json.dumps(dict(kind='unperturbed', eps=eps, **defect(g0, tr0, z0, eps))), flush=True)
for fn in resps:
    R = np.load(fn, allow_pickle=True); v = R['v']; dz = R['x_tail']
    assert v.shape == g0.shape and np.allclose(R['lr'], lr0) and abs(float(R['p']) - p) < 1e-12
    vo = 0.5*(v - v[:, flip])
    print(json.dumps(dict(resp=fn.split('/')[-1], dz_deg_per_unit=[math.degrees(float(x)) for x in dz], v_odd_frac=float(np.linalg.norm(vo)/np.linalg.norm(v)),
                          v_rel_rms=float(np.sqrt(((v/rowmax)**2).mean())), v_rel_max=float(np.abs(v/rowmax).max()))), flush=True)
    for eps in epss:
        t1 = time.time(); g1 = np.maximum(g0 + eps*v, 0.0); z1 = [z0[0] + eps*float(dz[0]), z0[1] + eps*float(dz[1])]
        tr1 = trace(g1); d1 = defect(g1, tr1, z1, eps)
        d1['th_e_shift_deg'] = [d1['th_e_deg'][0] - tr0[2][0], d1['th_e_deg'][1] - tr0[2][1]]
        d1['z_shift_deg'] = [eps*math.degrees(float(dz[0])), eps*math.degrees(float(dz[1]))]
        print(json.dumps(dict(kind='corrected', resp=fn.split('/')[-1], eps=eps, **d1, wall=round(time.time() - t1, 1))), flush=True)
print(json.dumps(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=round(time.time() - t0, 1))), flush=True)
