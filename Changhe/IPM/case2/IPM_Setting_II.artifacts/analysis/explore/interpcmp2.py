# Lead: driver for interpcmp.py; one-step drift of the numerics' local cubic Lagrange interpolant on a lead
# (B-spline-stationary) state, relative to the half-disc scale G cos^2 th (G = max of g / cos^2 on |cos| > 0.2 per ring).
# Usage: python3 interpcmp2.py state.npz
import sys, runpy, io, contextlib
st = sys.argv[1]; sys.argv = ['interpcmp.py', st]
sys.path.insert(0, 'explore')
import pforward as PF, pforward2 as PF2
PF.velocity_p = PF2.velocity_p
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    G = runpy.run_path('interpcmp.py', run_name='__main__')
import numpy as np
g = G['g']; lr = G['lr']; th = G['th']; deg = np.degrees(th); ds = 0.02; inside = G['inside']; fac = G['fac']
gn = np.where(inside, G['res']['lagrange'] * fac, g); gb = np.where(inside, G['res']['bspline+lim'] * fac, g)
c2 = np.cos(th) ** 2; ok = np.abs(np.cos(th)) > 1e-6
print('state', st, 'Nth', len(th))
for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, 0), (0, 4)]:
    i = np.where((lr >= a) & (lr < b))[0]
    sc = np.array([np.max((g[k] / c2)[np.abs(np.cos(th)) > 0.2]) for k in i])[:, None] * c2
    rl = ((gn[i] - g[i]) / (ds * sc))[:, ok]; rb = ((gb[i] - g[i]) / (ds * sc))[:, ok]; dk = deg[ok]
    k = np.unravel_index(np.argmax(np.abs(rl)), rl.shape)
    up = (dk > 30) & (dk < 150); lo = (dk > 210) & (dk < 330); nz = np.abs(dk - 90) < 2
    print('[%g,%g] lagrange max %.3e at lr %.2f th %.1f; bspline max %.1e; lagrange mean |.| upper 30-150 %.2e, lower 210-330 %.2e, |th-90|<2 %.2e' % (a, b, abs(rl[k]), lr[i[k[0]]], dk[k[1]], np.abs(rb).max(), np.abs(rl[:, up]).mean(), np.abs(rl[:, lo]).mean(), np.abs(rl[:, nz]).mean()))
