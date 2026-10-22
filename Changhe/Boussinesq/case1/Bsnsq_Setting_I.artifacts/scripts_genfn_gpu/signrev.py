"""Sign structure along vertical lines: Omega(x, y) and Theta_x(x, y) along x = const for y log-spaced (physical points via the chart inversion of
gphys_local.phys_fields), with the sign-change locations (linear interpolation in log y). Usage: python3 signrev.py state.npz [x1,x2,...] [ymin ymax ny]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
sys.argv_backup = list(sys.argv)
state = sys.argv[1]
xs = [float(v) for v in sys.argv[2].split(',')] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else [1e-3, 1.0, 1e3, 1e6]
ymin = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4; ymax = float(sys.argv[4]) if len(sys.argv) > 4 else 1e7; ny = int(sys.argv[5]) if len(sys.argv) > 5 else 4000
sys.argv = [sys.argv[0], state, '/dev/null']      # gphys_local parses sys.argv at import
import gphys_local as G
y = np.logspace(np.log10(ymin), np.log10(ymax), ny)
print('state %s a0 %.4f: sign changes along vertical lines (y from %.0e to %.0e, %d points)' % (state, G.a0, ymin, ymax, ny))
for xv in xs:
    X = torch.full((ny,), xv, dtype=G.DT, device=G.DEV); Y = torch.tensor(y, dtype=G.DT, device=G.DEV)
    F = G.phys_fields(X, Y)
    for name, v in [('Omega', F['Om']), ('Theta_x', F['Thx'])]:
        v = v.cpu().numpy(); sgn = np.sign(v); ch = np.where(sgn[1:] * sgn[:-1] < 0)[0]
        locs = [float(np.exp(np.interp(0.0, [v[i], v[i + 1]], [np.log(y[i]), np.log(y[i + 1])]))) if v[i] != v[i + 1] else y[i] for i in ch]
        print('  x = %g: %s: %d sign change(s) at y = %s; sign at y = %.0e: %+d, at y = %.0e: %+d; max |value| %.3e' % (xv, name, len(ch), ', '.join('%.6g' % l for l in locs) if locs else '-', ymin, int(sgn[0]), ymax, int(sgn[-1]), float(np.abs(v).max())))
