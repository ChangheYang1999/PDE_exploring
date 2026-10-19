"""Angular enrichment of a c6 shape (lead, 2026-10-18 about 03:35Z; VERIFY_REPORT G42 (b), (c)): the same radial basis and
coefficients, angular modes m <= M_new (new coefficients zero), so the trial density is unchanged. Checks the unchanged
density and transport residual on a common grid and writes the new shape.
Usage: python3 make_angular.py IN_shape.npz OUT_shape.npz M_new [NR NT]"""
import sys
import json
import numpy as np
from centre_fit import load_shape

src, out, mnew = sys.argv[1], sys.argv[2], int(sys.argv[3])
nr = int(sys.argv[4]) if len(sys.argv) > 4 else 2048
nt = int(sys.argv[5]) if len(sys.argv) > 5 else 960
s0, z0 = load_shape(src, nr, nt)
s1, z1 = load_shape(src, nr, nt, angular=mnew)
_, f0, L20, res0, den0 = s0.evaluate(z0)
_, f1, L21, res1, den1 = s1.evaluate(z1)
rho0 = L20 ** 1.5 * f0["rho"]; rho1 = L21 ** 1.5 * f1["rho"]
info = dict(src=src, out=out, angular_old=int(s0.angular), angular_new=int(s1.angular), degree=int(s1.degree),
            ncol_old=len(z0), ncol_new=len(z1), cl_old=float(1 / z0[0]), cl_new=float(1 / z1[0]),
            L_old=float(np.sqrt(L20)), L_new=float(np.sqrt(L21)),
            rho_rel_diff=float(np.max(np.abs(rho1 - rho0)) / np.max(np.abs(rho0))),
            res_max_diff=float(np.max(np.abs(res1 / den1 - res0 / den0)[s0.rows])),
            f_norm_old=float(np.linalg.norm(s0.raw_fun(z0)[0])), f_norm_new=float(np.linalg.norm(s1.raw_fun(z1)[0])))
print(json.dumps(info, indent=1))
assert info["rho_rel_diff"] < 1e-12 and abs(info["cl_new"] - info["cl_old"]) < 1e-14, "enrichment changed the trial"
s1.run_configuration = dict(method="make_angular", **info)
s1.save(out, z1)
