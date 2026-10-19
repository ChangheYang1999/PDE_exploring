"""Off-shell scan of the lead's wall identity (proofs/structure_v1.md Thm 5(c)): for a profile in S^+_even,
    kappa_w := int h w' dy / int h dy = (l - 1)/3,  h(y) = rho_xx(0,y), w'(y) = psi_xy(0,y), l = 1/2 + c = 1/p.
Is there a sign obstruction? Evaluate kappa_w on nonnegative x-even test densities rho = x^2 (1 + a y/<r>)^2 <r>^{p-2}
(rho = rho_x = 0 on the axis, far field r^p cos^2 th (1 + a sin th)^2, zeros of A only at +-pi/2 for |a| < 1).
w'(y0) = psi_xy at (0, y0) = c-moment of the translated density, computed with code/charsolve.py moments
(mode-3 radial integral + r^p tail beyond L = 1e10)."""
import numpy as np, torch, sys
sys.path.insert(0, 'code')
from charsolve import CharSolver
edges = np.concatenate([[0.0], np.geomspace(1e-6, 0.1, 12), np.geomspace(0.1, 10, 25)[1:], np.geomspace(10, 1e10, 46)[1:]])
S = CharSolver(edges, 8, 64, 1e-6, 'cuda')
X, Y = S.X, S.Y
def rho_fn(x, y, a, p):
    r2 = 1 + x*x + y*y
    return x*x*(1 + a*y/torch.sqrt(r2))**2*r2**((p - 2)/2)
yy = np.concatenate([-np.geomspace(1e6, 1e-3, 120), [0.0], np.geomspace(1e-3, 1e6, 120)])
print('a, p, c=psi_xy(0), l=1/2+c, kappa_w, (l-1)/3, (1/p-1)/3, int h')
for p in (0.3, 0.5, 0.7):
    for a in (0.0, 0.3, 0.6, 0.9, -0.6):
        wp = []
        for y0 in yy:
            rho = rho_fn(X, Y + y0, a, p)
            c, b = S.moments(rho, p)
            wp.append(float(c))
        wp = np.array(wp)
        h = 2*(1 + a*yy/np.sqrt(1 + yy**2))**2*(1 + yy**2)**((p - 2)/2)
        # trapezoid on the nonuniform grid + power tails beyond |y| = 1e6 (h ~ y^{p-2}, h w' ~ y^{2p-3})
        Ih = np.trapz(h, yy); Ihw = np.trapz(h*wp, yy)
        Y6 = 1e6
        for sgn, i in ((1, -1), (-1, 0)):
            Ih += h[i]*Y6/(1 - p); Ihw += h[i]*wp[i]*Y6/(2 - 2*p)
        c0 = wp[len(yy)//2]; l = 0.5 + c0
        print(f'{a:+.1f} {p:.1f}  c={c0:+.6f} l={l:.6f}  kappa_w={Ihw/Ih:+.6f}  (l-1)/3={(l-1)/3:+.6f}  (1/p-1)/3={(1/p-1)/3:+.6f}  int h={Ih:.5f}', flush=True)
