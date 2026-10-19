"""V54(i): core contribution to the node strain on own states. My radial grid has a first panel [0, e^tmin] (code/fwdstat.py:
edges = [0, e^tmin, ..., e^tmax]), so the moment c = l - m1 (code/charsolve.py moments) already integrates the core. This script
splits c into the panel-0 part (r < r_min = e^tmin) and the rest, and compares the panel-0 part with the lead's core formula
(r_min/pi) int (rho/r^2)(r_min, th) sin 3th dth (notes of the lead analyst 03:31Z item 2) evaluated at the Gauss nodes next to r_min.
Usage: python3 tests/v54_core.py STATE.npz [STATE2.npz ...]"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True)
    args = json.loads(str(d['args']))
    p = float(d['p']); nt = len(d['th']); tmin = float(args.get('tmin', -12)); tmax = float(args.get('tmax', 10))
    F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=10)
    assert np.allclose(F.r.cpu().numpy(), d['r'])
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
    S = F.S; q = S.q
    r3 = S.rho_modes(rho)[:, 3]
    terms = S.w*r3/S.r**2
    c_all = float(F.node(rho)['c'])
    c_core = float(-2*torch.sum(terms[:q]).imag)
    r = S.r.cpu().numpy(); th = F.th.cpu().numpy(); rh = d['rho']
    rmin = math.exp(tmin)
    # lead's formula with rho/r^2 taken at the last panel-0 node and at the first panel-1 node
    est = [float(rmin/math.pi*np.sum(rh[k]/r[k]**2*np.sin(3*th))*(2*math.pi/nt)) for k in (q - 1, q)]
    # radial profile of the sin 3th moment of rho/r^2 inside the core (constant if rho ~ C(th) r^2 there)
    prof = [round(float(np.sum(rh[k]/r[k]**2*np.sin(3*th))*(2*math.pi/nt)), 2) for k in range(q + 2)]
    print(json.dumps(dict(state=fn.split('/')[-1], p=p, nt=nt, tmin=tmin, m1=round(F.l - c_all, 6), c=round(c_all, 6),
                          c_core_panel0=round(c_core, 6), m1_without_core=round(F.l - c_all + c_core, 6),
                          lead_formula_at_nodes_q_minus_1_and_q=[round(e, 6) for e in est],
                          lr_nodes=[round(float(math.log(x)), 3) for x in r[:q + 2]], sin3_moment_rho_over_r2=prof)), flush=True)
