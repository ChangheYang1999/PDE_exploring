import time, numpy as np, sys
from flint import arb, ctx; ctx.prec = 80
import zcurve, certify_lb as C
G = zcurve.CurveGeom(); print("segments", G.N, "last height", G.ys[-1], flush=True)
px = arb('1.3245528042787547'); py = arb('1.1500535909926854', '1.042620402567301')
t0 = time.time(); print("wide-ball branch dist", G.branch_dist(px, py).str(10, radius=True), f"{time.time()-t0:.2f}s", flush=True)
py2 = arb(G.AY[-1], arb("1e-6")); xb = G.x_at(py2); print("x_at straddling last height:", xb.str(10, radius=True), flush=True)
cx, cy, rQ, area, _, _, M2 = C.cell_geom_ang((arb(1), arb(0)), arb(1), arb(1) + arb('1e-10'), arb(0), arb('1e-10')); print("tiny cell rQ", rQ, "M2", M2, flush=True)
rng = np.random.default_rng(3); t0 = time.time(); nu = nt = 0
for _ in range(100):
    p = rng.normal(size=2)*rng.choice([0.1, 0.5, 2.0, 20.0]); rQ = 0.005*max(1, np.hypot(*p))
    d = G.dist(arb(p[0]), arb(p[1]))
    if d > rQ: nt += 1; nu += G.unique_nearest(arb(p[0]), arb(p[1]), arb(rQ), d)
print(f"unique {nu}/{nt}; {(time.time()-t0)/100*1e3:.2f} ms per point (dist+unique)", flush=True)
