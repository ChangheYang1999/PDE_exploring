"""V208: independent count of the cells whose forward exit switches branch under a fixed x-odd perturbation (numerics
notes to the lead analyst 21:51Z item 1: dT/db_1 4 -> 14 at eps 1e-4 and 47 -> 115 at 1e-3, far bump 191 -> 383 at 1e-4, 512 -> 1024
angles), and the per-cell exit-angle changes at eps 1e-6. My velocity (code/fwdstat.py) of the imported numerics-format
state; per-cell forward exits by my arclength RK4 (FwdStat.trace_s) from every numerics grid point; the directions b1rhs,
bump_far, bump_inner exactly as in tests/v201_gamma_exit.py. A cell switches if its exit angle changes by more than 90 deg.
Bands of log r: core [-14,-8), inner [-8,-4), mid [-4,0), outer [0,10].
Usage: python3 -B tests/v211_switch.py STATE.npz nt eps_b1 eps_far eps_inner"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g0, lr0, th0 = d['g'], d['lr'], d['th']; X = d['x']; p = float(X[-1])
nt = int(sys.argv[2])
EPS = {'b1rhs': [float(s) for s in sys.argv[3].split(',')], 'bump_far': [float(s) for s in sys.argv[4].split(',')],
       'bump_inner': [float(s) for s in sys.argv[5].split(',')]}
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=3, q=8, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
def imp(gs):
    G = CubicSpline(lr0, gs, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn) or not np.allclose(th0, thn):
        G = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([G, G[:, :1]], 1), axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    return torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
lrg = lr0[:, None]; thg = th0[None, :]
TT = torch.tensor(np.broadcast_to(lrg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
TH0 = torch.tensor(np.broadcast_to(thg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
LR = np.broadcast_to(lrg, g0.shape).reshape(-1)
bands = [('core', -14.01, -8), ('inner', -8, -4), ('mid', -4, 0), ('outer', 0, 10.01)]
def cell_exits(rho):
    al, be, _, _ = F.fields(rho)
    the, s, nbad = F.trace_s(al, be, TT, TH0, 0.03, 12000)
    return the.cpu().numpy(), s.cpu().numpy(), nbad
t0 = time.time()
rho0 = imp(g0)
E0, S0, nb0 = cell_exits(rho0)
print(json.dumps(dict(state=fn.split('/')[-1], nt=nt, cells=int(E0.size), not_exited=nb0, wall=round(time.time() - t0, 1))), flush=True)
scale = (np.exp(2*lrg)/(1 + np.exp(2*lrg)))**(1 - p/2)
u = g0/scale; un = float(np.linalg.norm(u))
flip = (len(th0)//2 - np.arange(len(th0))) % len(th0)
def odd(v): return 0.5*(v - v[:, flip])
for name in ('b1rhs', 'bump_far', 'bump_inner'):
    if not EPS[name]:
        continue
    if name == 'b1rhs':
        K = 16; par = np.array(X[:K], float); assert np.all(np.array(X[K:-1]) == 0)
        jj = np.arange(1, K + 1)
        def Ad(t):
            ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*t[None, :]), np.cos(jj[:, None]*t[None, :]))
            return np.cos(t)**2*np.exp(par @ ph)
        Tg = (np.exp(-S0)*math.exp(p*F.tmax)*Ad(E0)).reshape(g0.shape)/np.exp(p*lrg)
        v = odd(Tg*np.cos(E0.reshape(g0.shape))/scale); vn = float(np.linalg.norm(v))
        mk = lambda e: imp(g0 + e*v*scale)
    else:
        c = -2.0 if name == 'bump_far' else -6.0
        v = odd(u*np.cos(thg)*np.exp(-0.5*(lrg - c)**2)); vn = float(np.linalg.norm(v))
        fac = torch.cos(F.TH)*torch.exp(-0.5*(torch.log(F.R) - c)**2)
        mk = lambda e: rho0*(1 + e*fac)
    for eps in EPS[name]:
        E1, S1, nb1 = cell_exits(mk(eps*un/vn))
        dd = np.degrees(((E1 - E0 + math.pi) % (2*math.pi)) - math.pi); ad = np.abs(dd)
        sw = ad > 90.0
        out = dict(dir=name, eps=eps, not_exited=nb1, switched=int(sw.sum()),
                   switched_bands={b: int((sw & (LR >= lo) & (LR < hi)).sum()) for b, lo, hi in bands})
        core = (LR < -8) & ~sw
        out['core_absdth_deg_q50_q90_q999'] = [float(np.quantile(ad[core], q)) for q in (0.5, 0.9, 0.999)]
        out['wall'] = round(time.time() - t0, 1)
        print(json.dumps(out), flush=True)
