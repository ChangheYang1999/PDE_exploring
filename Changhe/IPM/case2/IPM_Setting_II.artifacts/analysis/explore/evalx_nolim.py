# Lead: evalx.py with the clip of the semi-Lagrangian cubic interpolation removed (P2.interp_qm -> plain cubic spline),
# to test whether the quasi-monotone limiter causes the upper-axis failure of the axis law (specification M25(i)). Same arguments as evalx.py.
import sys, runpy
import numpy as np
from scipy.ndimage import map_coordinates
sys.path.insert(0, 'explore')
import p0_forward2 as P2


def interp_cubic(g, ci, cj, Nth):
    Pd = 24
    Nr = g.shape[0]
    gp = np.concatenate([g[:, -Pd:], g, g[:, :Pd]], axis=1)
    ci = np.clip(ci, 0, Nr - 1)
    cjp = np.mod(cj, Nth) + Pd
    return map_coordinates(gp, [ci, cjp], order=3, mode='nearest')


P2.interp_qm = interp_cubic
sys.argv = ['explore/evalx.py'] + sys.argv[1:]
runpy.run_path(sys.argv[0], run_name='__main__')
