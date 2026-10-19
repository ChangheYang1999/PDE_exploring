"""V94 (lead team notes 09:13Z item 5): where c = l - m1 comes from, on own-format exit-map states, with my moment
(code/charsolve.py moments: Gauss-Legendre panels including the core panel [0, e^tmin], closed-form tail beyond r_max).
dc/dt = (1/pi) int e^{(p-1)t} g sin 3th dth; band integrals of c over t = log r, the core panel and the tail reported apart,
each also split into the upper (sin th > 0) and lower half-planes. Half-disc model: if rho = G_+- x^2 in the upper / lower
half-plane then dc/dt = (14 / (15 pi)) (G_+ - G_-) r; G_+- = median of rho / x^2 over |cos th| > 1/2 in each half-plane on
each ring (as the lead's definition). Model band integrals use the same quadrature. Also log(G_- / G_+) at t = -13 .. -2.
Runs on the CPU (one thread). Usage: python3 tests/v94_cband.py OWN.npz [OWN2.npz ...]"""
import sys, math, json, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
                dti=0.01, nstep=800, dev='cpu')
    S = F.S; tmin = float(args['tmin'])
    rho = torch.tensor(d['rho'], dtype=torch.float64)
    nd = F.node(rho); c_tot = nd['c']
    r = S.r.numpy(); w = S.w.numpy(); th = S.th.numpy(); t = np.log(r); R = rho.numpy()
    up = np.sin(th) > 0
    def c_of(Rm):
        rm = S.rho_modes(torch.tensor(Rm))[:, 3]
        node = -2*(S.w*rm/S.r**2).imag.numpy()
        tail = float(-2*(torch.dot(S.ext_last.to(torch.complex128), rm[-S.q:])/(S.L*(1 - p))).imag)
        return node, tail
    nodeA, tailA = c_of(R); nodeU, tailU = c_of(np.where(up[None, :], R, 0.0)); nodeL, tailL = c_of(np.where(up[None, :], 0.0, R))
    x2 = (r[:, None]*np.cos(th)[None, :])**2; sel = np.abs(np.cos(th)) > 0.5
    Gp = np.array([np.median((R[i]/x2[i])[sel & up]) for i in range(len(r))])
    Gm = np.array([np.median((R[i]/x2[i])[sel & ~up]) for i in range(len(r))])
    model = w*(14/(15*math.pi))*(Gp - Gm)          # int (14/(15 pi)) (G_+ - G_-) r dt = int ... dr
    edges = [('core r<e^tmin', t < tmin - 1e-12)]
    bl = [tmin, -12, -10, -8, -6, -4, -2, 0, 4, float(args['tmax'])]
    bl = sorted(set([b for b in bl if b >= tmin]))
    for a, b in zip(bl[:-1], bl[1:]):
        edges.append(('%g..%g' % (a, b), (t >= a - 1e-12) & (t < b - 1e-12)))
    rows = []
    for nm, m in edges:
        rows.append(dict(band=nm, c=round(float(nodeA[m].sum()), 4), c_up=round(float(nodeU[m].sum()), 4),
                         c_lo=round(float(nodeL[m].sum()), 4), model=round(float(model[m].sum()), 4)))
    rows.append(dict(band='tail r>r_max', c=round(tailA, 4), c_up=round(tailU, 4), c_lo=round(tailL, 4)))
    lt = float(nodeA[t < -4].sum())
    G = {}
    for tt in (-13, -12, -11, -10, -9, -8, -6, -4, -2):
        if tt < tmin: continue
        i = int(np.argmin(np.abs(t - tt)))
        G['%g' % tt] = [round(float(t[i]), 2), float('%.4g' % Gp[i]), float('%.4g' % Gm[i]), round(math.log(Gm[i]/Gp[i]), 3)]
    out = dict(state=fn.split('/')[-1], par=args['par'], p=p, nt=nt, tmin=tmin, m1=round(nd['m1'], 6), c=round(c_tot, 5),
               c_sum_check=round(float(nodeA.sum()) + tailA, 5), c_logr_lt_m4=round(lt, 4), bands=rows,
               G_t_Gup_Glo_loglo_up=G)
    print('CBAND ' + json.dumps(out), flush=True)
