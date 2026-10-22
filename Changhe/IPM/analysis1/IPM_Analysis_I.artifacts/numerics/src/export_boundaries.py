"""Export the radial cell-boundary balls (midpoint, radius) of the three certificate regions from the Green files to a small file, so that
src/xnorm_cert.py (version 3) can run from the published artifacts without the 291 MB data/cert_green.npz:
  middle: tb, tb_rad (7810 boundaries, t = log r);  outer: t0, t0_rad, tau_out, tau_out_rad (8949; t = t0 + tau);  inner: tmin, tmin_rad, tau_in, tau_in_rad (2633).
Usage: python3 src/export_boundaries.py [data/cert_green.npz data/cert_outer_green.npz data/cert_inner_green.npz data/cell_boundaries.npz]"""
import sys, os, numpy as np
lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:]
G, Go, Gi, out = (a + ["data/cert_green.npz", "data/cert_outer_green.npz", "data/cert_inner_green.npz", "data/cell_boundaries.npz"][len(a):])[:4]
G = np.load(os.path.join(lane, G)); Go = np.load(os.path.join(lane, Go)); Gi = np.load(os.path.join(lane, Gi))
np.savez(os.path.join(lane, out), tb=G["tb"], tb_rad=G["tb_rad"], t0=Go["t0"], t0_rad=Go["t0_rad"], tau_out=Go["tau"], tau_out_rad=Go["tau_rad"],
         tmin=Gi["tmin"], tmin_rad=Gi["tmin_rad"], tau_in=Gi["tau"], tau_in_rad=Gi["tau_rad"],
         note="cell-boundary balls (mid, rad doubles) of the certificate regions, copied from the Green files; t = log r; outer t = t0 + tau_out, inner t = tmin + tau_in")
print("written", out, "middle", len(G["tb"]), "outer", len(Go["tau"]), "inner", len(Gi["tau"]))
