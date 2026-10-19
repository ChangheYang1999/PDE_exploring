"""For saved states of the homotopy / Newton runs (charsolve.T with the fixed 3-step loop p <- 1/c_l from p = 0.5),
compare the (c, c_l, p) used by T with the exact self-consistent solution of CharSolver.solve_p (h = 1)."""
import sys, glob, numpy as np, torch
sys.path.insert(0, 'code')
from charsolve import CharSolver
cache = {}
for f in sys.argv[1:]:
    d = torch.load(f, weights_only=False)
    key = (tuple(np.round(np.log(np.asarray(d['edges'])[1:]), 12)), d['q'], d['nt'])
    if key not in cache: cache[key] = CharSolver(d['edges'], d['q'], d['nt'], d['r1'], 'cuda')
    S = cache[key]
    xi = d['xi'].cuda(); rho = xi**2
    _, dT = S.T(xi, info=True)
    p = 0.5
    for k in range(3):
        c, b = S.moments(rho, p); cl, l = S.jet(c, b); p_prev, p = p, float(min(1/float(cl), 0.999))
    ce, be, cle, le, pe, fe = S.solve_p(rho, 1.0, 0.0, dT['p'])
    print(f"{f.split('/')[-1]}: L={S.L:.0e} T-loop c={dT['c']:.6f} cl={dT['cl']:.6f} p={dT['p']:.6f} (p2={p_prev:.6f})"
          f" | exact c={float(ce):.6f} cl={float(cle):.6f} p={float(pe):.6f} |f|={fe:.1e}")
