"""V273 companion: the Newton iterates of numerical record R22 (c), (e) (numerics runs/pfwd/tan/M2d_256_it*.npz, M2f_256_it*.npz; keys g, lr,
th, z, p, b1, a_even, normF) evaluated with MY fixed-datum exit map (same map and norm as tests/v273_r22_lin.py: velocity
code/fwdstat.py, FwdStat.trace_s per cell, strong exits by RK4 from lr = -12).  Prints, per state, the 2-norm of the defect
(g - Tg)/rowmax(g_base) over all cells, its x-odd part and the band norms, against the unperturbed base at the same b_1.
Version 2 (tests/v273_iter2.py): also with the zeros set to MY strong exits of each iterate; near_share as in v273_r22_lin2.py.
Usage: python3 -B tests/v273_iter2.py BASE.npz ITER.npz [ITER.npz ...]"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64

base = np.load(sys.argv[1], allow_pickle=True); its = sys.argv[2:]
g0, lr0, th0 = base['g'], base['lr'], base['th']; X = np.array(base['x'], float); p = X[-1]; K = 16; a = X[:K]
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=3, q=8, nt=len(th0), dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr)
rowmax = np.maximum(g0.max(1, keepdims=True), 1e-300)
flip = (len(th0)//2 - np.arange(len(th0))) % len(th0)
n = np.arange(1, K + 1)[:, None]


def trace(g):
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


def defect(g, tr, z, b1, ac):
    T, S, the, nbad = tr
    phi = np.where(n % 2 == 1, np.sin(n*T[None, :]), np.cos(n*T[None, :]))
    A = 4*np.sin(0.5*(T - z[0]))**2*np.sin(0.5*(T - z[1]))**2*np.exp(ac @ phi + b1*np.cos(T))
    Tg = (np.exp(-S)*math.exp(p*F.tmax)*A).reshape(g.shape)/np.exp(p*lr0[:, None])
    D = (g - Tg)/rowmax; Do = 0.5*(D - D[:, flip])
    bands = {}
    for lo, hi in ((-14.01, -8), (-8, -4), (-4, -2), (-2, 2), (2, 10.01)):
        m = (lr0 >= lo) & (lr0 < hi); bands['[%g,%g)' % (lo, hi)] = [float(np.linalg.norm(D[m])), float(np.linalg.norm(Do[m]))]
    Te = T.reshape(g.shape); dist = np.minimum(np.abs(np.angle(np.exp(1j*(Te - z[0])))), np.abs(np.angle(np.exp(1j*(Te - z[1])))))
    core = np.broadcast_to((lr0 < -8)[:, None], Te.shape); near = core & (dist < math.radians(0.5))
    sh = float((Do[near]**2).sum()/max((Do[core]**2).sum(), 1e-300))
    return dict(near_share=sh, near_cells=int(near.sum()), norm=float(np.linalg.norm(D)), norm_odd=float(np.linalg.norm(Do)), dmax=float(np.abs(D).max()), bands_norm_odd=bands,
                th_e_deg=the, not_exited=nbad)


t0 = time.time(); z0 = [math.pi/2, 3*math.pi/2]
tr0 = trace(g0); done = set()
for fn in its:
    R = np.load(fn, allow_pickle=True); b1 = float(R['b1']); ac = np.array(R['a_even'], float)
    assert np.allclose(R['lr'], lr0) and np.allclose(R['th'], th0) and abs(float(R['p']) - p) < 1e-12
    if b1 not in done:
        done.add(b1)
        print(json.dumps(dict(kind='unperturbed', eps=b1, a_diff=float(np.abs(ac - a).max()), **defect(g0, tr0, z0, b1, a))), flush=True)
    t1 = time.time(); g = np.array(R['g'], float); z = [float(v) for v in R['z']]; tr = trace(g); d = defect(g, tr, z, b1, ac)
    d['z_deg'] = [math.degrees(v) for v in z]
    print(json.dumps(dict(kind='iterate', resp=fn.split('/')[-1], eps=b1, normF_num=float(R['normF']),
                          g_change_rel_max=float(np.abs((g - g0)/rowmax).max()), **d, wall=round(time.time() - t1, 1))), flush=True)
    zo = [math.radians(tr[2][0]), math.radians(tr[2][1])]; d2 = defect(g, tr, zo, b1, ac)
    print(json.dumps(dict(kind='iterate_ownz', resp=fn.split('/')[-1], eps=b1, **d2)), flush=True)
print(json.dumps(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=round(time.time() - t0, 1))), flush=True)
