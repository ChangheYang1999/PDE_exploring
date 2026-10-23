"""region_maxima.py -- lead 02:52Z item 6: for each saved Q state, the regional maxima (radial bins [0,0.1), [0.1,1), [1,100), [100,1e4), [1e4,1e8), [1e8,..))
of the absolute residual |R|, of |R|/N_f and of |R|/N_v with the location (r, th) of each maximum, on the standard between-node set of qdiag.eval_set
(midpoints of the Radau nodes in t and of the quadrant angles, plus the near-axis angles th_0/4, th_0/2, (th_{M-1}+pi/2)/2, pi/2 - (pi/2-th_{M-1})/4 and
pi/2; radii below RMAX = 1e120).  Excluded neighbourhoods of normalization zeros: the x-axis th = 0 itself (where R, N_f and N_v vanish identically by
parity) is not in the set; no other point is excluded (N_f, N_v > 0 at every sampled point: the minimum of N_f and N_v over the set is printed).
All values are sampled maxima, not bounds.  usage: python3 src/region_maxima.py states..."""
import sys, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); RR, TT = qdiag.eval_set(S); out = S.ev(RR, TT)
    print(f"{f} [N={S.N} M={S.M} c_l={S.cl:.6f} a0={S.a0:.6f} K={S.K:.4f}]  sample set {RR.size} points, r in [{RR.min():.3g}, {RR.max():.3g}], th in [{TT.min():.4f}, {TT.max():.4f}]; "
          f"min N_f = {out['Nf'].min():.3e}, min N_v = {out['Nv'].min():.3e} (no zero denominators in the set)")
    for l in qdiag.region_table(S, RR, TT, out, 0.0): print(l)
