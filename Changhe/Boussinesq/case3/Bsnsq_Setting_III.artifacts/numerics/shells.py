import sys, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, DT
import json
b = Basis(32, 5, 12, 12, ng_coll=7, m_reg=2, device='cuda', grade=1.5)   # residual grid of the scan
g = Geometry(b, 3.0, 1.5)
r = g.rr.cpu().numpy(); x = g.x.cpu().numpy(); y = g.y.cpu().numpy()
wr = (b.w_coll_t * g.drdt).cpu().numpy(); wphi = np.pi / b.Nphi
W = (wr[:, None] * np.ones((1, b.Nphi)) * wphi).reshape(-1)       # area element r dr dphi needs factor r
W = W * r
for f in sys.argv[1:]:
    d = np.load(f)
    Om = x * d['G']; Th = x ** 2 * d['F']
    integrand = 2 * x * y * Om / r ** 4 / np.pi   # factor 2: half plane -> full plane (integrand even in x)
    tot = (integrand * W).sum()
    print(f"{f}: c_in={float(d['c_in']):.3f} c_out(fit)={float(d['c_out']):+.4f} c_out(quad)={tot:+.4f}")
    edges = [0, 0.3, 1, 3, 10, 30, 100, 1e3, 1e4, 1e99]
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (r >= lo) & (r < hi)
        if m.any():
            om_pos = (Om[m & (y > 0)] * W[m & (y > 0)]).sum(); om_neg = (Om[m & (y < 0)] * W[m & (y < 0)]).sum()
            print(f"   r in [{lo:6g},{hi:6g}): c-contrib {(integrand[m]*W[m]).sum():+.4f}   int Omega (y>0) {om_pos:+.4f}  (y<0) {om_neg:+.4f}   max Omega {Om[m].max():.3f}  max Theta {Th[m].max():.3g}")
