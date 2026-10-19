"""Start shape for a fixed-c_l fit (lead, 2026-10-18 about 03:55Z; VERIFY_REPORT G45 (e)): z = z0 + dk (e0 + v), with v the
soft tangent of soft_tangent.py (PREFIX_tangent.npz, same basis as the shape) and dk = 1/c_target - 1/c0: the linear
fixed-c correction of the fitted shape, extrapolated to the target c_l. Without a tangent file (argument "none") only k
is changed. Reports the objective of the start and of the naive start on the given grid.
Usage: python3 make_fixc_start.py SHAPE.npz TANGENT.npz|none C_TARGET OUT_shape.npz [NR NT]"""
import sys
import json
import numpy as np
from centre_fit import load_shape

src, tan, ct, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
nr = int(sys.argv[5]) if len(sys.argv) > 5 else 4096
nt = int(sys.argv[6]) if len(sys.argv) > 6 else 480
s, z0 = load_shape(src, nr, nt)
c0 = 1 / z0[0]; dk = 1 / ct - z0[0]
e0 = np.zeros(len(z0)); e0[0] = 1.
info = dict(src=src, tangent=tan, c0=float(c0), c_target=ct, dk=float(dk), nr=nr, nt=nt)
if tan != "none":
    d = np.load(tan); v = d["v"]
    assert len(v) == len(z0) and abs(float(d["c0"]) - c0) < 1e-12, "tangent does not belong to this shape"
    info["tangent_it"] = int(d["it"])
else:
    v = np.zeros(len(z0))
z = z0 + dk * (e0 + v)
for name, zz in (("fitted", z0), ("naive", z0 + dk * e0), ("start", z)):
    res, cen, source = s.raw_fun(zz)
    info[name] = dict(norm=float(np.linalg.norm(res)), hP1=float(source[1] - 1), cl=float(1 / zz[0]))
print(json.dumps(info, indent=1))
s.run_configuration = dict(method="make_fixc_start", **{k: info[k] for k in ("src", "tangent", "c0", "c_target", "dk")})
s.save(out, z)
