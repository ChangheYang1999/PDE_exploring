"""
hs_export_points.py -- export g, g_x, g_y of saved hydrostatic states at the 19649 common points of hs_cauchy.py (401 log radii 1e-3 .. 1e7 x 49 quadrant angles
incl. both axes) as NPZ, for the verifier's independent recomputation of the function-space differences of 4P(b)(xvi) (lead 18:33Z item 1).
usage: python3 src/hs_export_points.py outdir state.pt ...   -> outdir/<tag>_points.npz with arrays X, Y, g, gx, gy and scalars N, M, c
"""
import sys, os, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve, hs_cauchy
torch.set_default_dtype(torch.float64)
out = sys.argv[1]; os.makedirs(out, exist_ok=True); X, Y, R = hs_cauchy.points()
for f in sys.argv[2:]:
    s = hs_cauchy.load(f); g, gx, gy = s['ge'](X, Y)
    np.savez_compressed(os.path.join(out, s['tag'] + '_points.npz'), X=X, Y=Y, g=g, gx=gx, gy=gy, N=s['N'], M=s['M'], c=s['c'])
    print(s['tag'], 'exported:', len(X), 'points; max|g|', float(np.abs(g).max()))
