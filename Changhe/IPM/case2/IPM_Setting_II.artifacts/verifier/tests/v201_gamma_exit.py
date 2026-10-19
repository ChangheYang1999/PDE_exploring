"""V201: independent check of the numerics exit-angle sensitivity test (numerics tests/pfwd_exit_sens.py, notes of the lead analyst 20:39Z (a)).
My velocity (code/charsolve.py via code/fwdstat.py) of an imported numerics-format state (g, lr, th, x with p last); exits of the two
branches of the strong unstable manifold Gamma traced by my own RK4 in t = log r from (t = lr_g, th = 90 / 270 deg) to t = 10 with my
tensor-cubic interpolation of alpha = l + W_r/r, beta = W_th/r. Perturbations as in the numerics test, but applied on my grid:
    bump at lr = c:  g -> g (1 + e cos th exp(-(lr - c)^2/2)),  e = eps |u| / |v|,  u = g/scale, v = u cos th exp(-(lr-c)^2/2),
norms over the numerics grid points (so e is the numerics' e exactly), scale = (r^2/(1+r^2))^(1-p/2).
    b1rhs: v = odd(g cos(TH_exit) / scale), TH_exit = forward-orbit exit angle of each numerics grid cell under MY velocity (g in
place of T(g): the difference is of the order of the base defect), e = eps |u| / |v| on the numerics grid; the perturbed state
g + e v scale is imported to my grid by the same splines.
Usage: python3 -B tests/v201_gamma_exit.py STATE.npz [nt] [ppu] [q] [nstep] [eps list] [dirs] [lr_g]"""
import sys, math, json, time, numpy as np, torch
sys.dont_write_bytecode = True
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g0, lr0, th0 = d['g'], d['lr'], d['th']; X = d['x']
p = float(X[-1])
nt = int(sys.argv[2]) if len(sys.argv) > 2 else len(th0)
ppu = int(sys.argv[3]) if len(sys.argv) > 3 else 3
q = int(sys.argv[4]) if len(sys.argv) > 4 else 8
nstep = int(sys.argv[5]) if len(sys.argv) > 5 else 2200
epss = [float(s) for s in (sys.argv[6] if len(sys.argv) > 6 else '1e-6,1e-5,1e-4').split(',')]
dirs = (sys.argv[7] if len(sys.argv) > 7 else 'bump_far,bump_inner').split(',')
lr_g = float(sys.argv[8]) if len(sys.argv) > 8 else -12.0
A = lambda t: np.cos(t)**2          # datum enters only the exit map, not the velocity or Gamma
F = FwdStat(p, A, tmin=float(lr0[0]), tmax=float(lr0[-1]), ppu=ppu, q=q, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
def imp(gs):
    G = CubicSpline(lr0, gs, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
    if len(th0) != len(thn) or not np.allclose(th0, thn):
        G = CubicSpline(np.concatenate([th0, [2*math.pi]]), np.concatenate([G, G[:, :1]], 1), axis=1, bc_type='periodic')(thn)
    G[lrr < lr0[0]] = 0.0
    return torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
rho0 = imp(g0)
au_cache = {}
def fields_u(rho):
    al, be, _, _ = F.fields(rho)
    return al, be, F.Imat @ al, F.Imat @ be
def trace(au, bu, t0, thi, n=nstep, t1=None):
    """RK4 in t for d th/dt = beta/alpha from t0 to t1 (no global V_r check; alpha checked along the orbits)."""
    t1 = F.tmax if t1 is None else t1
    h = (t1 - t0)/n; th = thi.clone(); t = torch.full_like(thi, t0); amin = float('inf')
    def f(t, th):
        a = F.interp(au, t, th); b = F.interp(bu, t, th)
        return b/a, float(a.min())
    for k in range(n):
        k1, a1 = f(t, th); k2, a2 = f(t + h/2, th + h/2*k1); k3, a3 = f(t + h/2, th + h/2*k2); k4, a4 = f(t + h, th + h*k3)
        th = th + h/6*(k1 + 2*k2 + 2*k3 + k4); t = t + h; amin = min(amin, a1, a2, a3, a4)
    return th, amin
def exits(rho, n=nstep):
    _, _, au, bu = fields_u(rho)
    th, amin = trace(au, bu, lr_g, torch.tensor([math.pi/2, 3*math.pi/2], dtype=DT, device='cuda'), n)
    e = np.degrees(np.remainder(th.cpu().numpy(), 2*math.pi))
    return e, amin
t0 = time.time()
nd = F.node(rho0)
e0, am0 = exits(rho0); e0b, _ = exits(rho0, 2*nstep)
base = dict(state=fn.split('/')[-1], p=p, nt=nt, ppu=ppu, q=q, nstep=nstep, lr_g=lr_g, m1=round(nd['m1'], 6), c=nd['c'], b=nd['b'],
            exits0=[float(x) for x in e0], exits0_2n_minus_n=[float(x) for x in (e0b - e0)], alpha_min_gamma=am0)
print(json.dumps(base), flush=True)
lrg = lr0[:, None]; thg = th0[None, :]
scale = (np.exp(2*lrg)/(1 + np.exp(2*lrg)))**(1 - p/2)
u = g0/scale; un = float(np.linalg.norm(u))
flip = (len(th0)//2 - np.arange(len(th0))) % len(th0)
def odd(v): return 0.5*(v - v[:, flip])
for name in dirs:
    if name.startswith('bump'):
        c = -2.0 if name == 'bump_far' else (-6.0 if name == 'bump_inner' else float(name.split('@')[1]))
        v = odd(u*np.cos(thg)*np.exp(-0.5*(lrg - c)**2)); vn = float(np.linalg.norm(v))
        fac = torch.cos(F.TH)*torch.exp(-0.5*(torch.log(F.R) - c)**2)
        mk = lambda e: rho0*(1 + e*fac)
    elif name == 'b1rhs':
        al0, be0, au, bu = fields_u(rho0)
        TT = torch.tensor(np.broadcast_to(lrg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
        TH0 = torch.tensor(np.broadcast_to(thg, g0.shape).copy(), dtype=DT, device='cuda').reshape(-1)
        # per-cell forward exit angle and exit time from each numerics grid point, arclength orbits (V_r <= 0 lobes allowed;
        # code/fwdstat.py trace_s), and my exit map on the numerics grid: Tg = e^{-s} L^p A(TH_exit) / r^p with the state's datum
        # A = cos^2 th exp(sum a_j phi_j) (x-even modes: sin(n th) for odd n, cos(n th) for even n; x-odd coefficients zero)
        THex, sx, nbad = F.trace_s(al0, be0, TT, TH0, 0.03, 12000)
        K = 16; par = np.array(X[:K], float); assert np.all(np.array(X[K:-1]) == 0)
        jj = np.arange(1, K + 1)
        def Ad(t):
            ph = np.where(jj[:, None] % 2 == 1, np.sin(jj[:, None]*t[None, :]), np.cos(jj[:, None]*t[None, :]))
            return np.cos(t)**2*np.exp(par @ ph)
        THn = THex.cpu().numpy(); Tg = (np.exp(-sx.cpu().numpy())*math.exp(p*F.tmax)*Ad(THn)).reshape(g0.shape)/np.exp(p*lrg)
        THex = THn.reshape(g0.shape)
        rel = np.abs(Tg - g0)/np.maximum(g0.max(1, keepdims=True), 1e-300)
        print(json.dumps(dict(b1rhs_cells=int(TT.numel()), not_exited=nbad, trace=F.last_trace, my_defect_max=float(rel.max()),
                              my_defect_rms=float(np.sqrt((rel**2).mean())))), flush=True)
        v = odd(Tg*np.cos(THex)/scale); vn = float(np.linalg.norm(v))
        mk = lambda e: imp(g0 + e*v*scale)
    else:
        raise SystemExit('unknown dir ' + name)
    print(json.dumps(dict(dir=name, v_norm=vn, u_norm=un)), flush=True)
    for eps in epss:
        e = eps*un/vn
        ep, am = exits(mk(e))
        dd = ((ep - e0 + 180) % 360) - 180
        print(json.dumps(dict(dir=name, eps=eps, e=e, exit1=float(ep[0]), exit2=float(ep[1]), dth1=float(dd[0]), dth2=float(dd[1]),
                              dth1_per_eps=float(dd[0]/eps), dth2_per_eps=float(dd[1]/eps), alpha_min=am, wall=round(time.time() - t0, 1))), flush=True)
