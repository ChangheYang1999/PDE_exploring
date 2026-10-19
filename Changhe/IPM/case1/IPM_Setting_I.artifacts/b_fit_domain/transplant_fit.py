"""FIT-CONVENTION VARIANT (work/c7/transplant_fit.py, lead 2026-10-18 08:14Z): identical to work/c6/transplant.py except
that it uses work/c7/centre_fit.py and loads the TARGET with fit_radius = 0.9 R_shape (R_shape read from the target
file, default 1000), so the reported norms are in the fit convention and the written shapes carry the target's R_shape.
Transplant of a soft c_l direction onto a finer c6 basis (lead, 2026-10-18; analysis 13.13 (d)(i)).
The c6c, c6d and c6f bases contain the 244 basis exactly (knot insertion, angular extension with zero coefficients), so the
two tangent shapes PLUS and MINUS (c6b segment 1 plus dk (e0 + v) at c_l offsets +-delta) are put on the TARGET basis
exactly, their difference quotient t = (z+ - z-) / (c+ - c-) is the soft direction per unit c_l in the target's
coefficients, and the shapes z_T + d t (d = OFFSETS) are written as OUT_PREFIX<d>_shape.npz. These are trials of the target
basis (rho = x^2 y exp(H) with H linear in the coefficients), not refitted.
Usage: python3 transplant.py TARGET_shape.npz PLUS_shape.npz MINUS_shape.npz OUT_PREFIX d1,d2,... [NR NT]"""
import sys
import json
from collections import Counter
import numpy as np
from centre_fit import load_shape

target, plus, minus, pre, offs = sys.argv[1:6]
nr = int(sys.argv[6]) if len(sys.argv) > 6 else 2048
nt = int(sys.argv[7]) if len(sys.argv) > 7 else 480
offsets = [float(x) for x in offs.split(",")]
T = np.load(target)
kt = Counter(T["spline_knots"].tolist())


def onto(src):
    S = np.load(src)
    ks = Counter(S["spline_knots"].tolist())
    assert all(kt[k] >= v for k, v in ks.items()), "source knots are not contained in the target knots"
    assert int(S["singular"]) == int(T["singular"]) and int(S["spline_order"]) == int(T["spline_order"])
    s, z = load_shape(src, nr, nt, angular=int(T["angular"]), insert=sorted((kt - ks).elements()))
    assert np.array_equal(np.asarray(s.spline_knots), T["spline_knots"]), "knot vectors differ after insertion"
    assert len(z) == len(T["z"])
    return s, z


fr = 0.9 * float(T["R_shape"]) if "R_shape" in T.files else None
sT, zT = load_shape(target, nr, nt, fit_radius=fr)
sp, zp = onto(plus)
sm, zm = onto(minus)
cp, cm, cT = 1 / zp[0], 1 / zm[0], 1 / zT[0]
t = (zp - zm) / (cp - cm)
info = dict(target=target, plus=plus, minus=minus, c_target=float(cT), c_plus=float(cp), c_minus=float(cm),
            nr=nr, nt=nt, t_k=float(t[0]), t_norm=float(np.linalg.norm(t[1:])), shapes={})
# exactness check of the transfer: the plus shape on the target basis has the same residual as on its own basis
s0, z0 = load_shape(plus, nr, nt)
info["transfer_check"] = dict(own=float(np.linalg.norm(s0.raw_fun(z0)[0])), target_basis=float(np.linalg.norm(sp.raw_fun(zp)[0])))
for name, zz in (("target", zT),) + tuple(("%+.1e" % d, zT + d * t) for d in offsets):
    res, cen, source = sT.raw_fun(zz)
    info["shapes"][name] = dict(norm=float(np.linalg.norm(res)), hP1=float(source[1] - 1), cl=float(1 / zz[0]))
for d in offsets:
    sT.run_configuration = dict(method="transplant", target=target, plus=plus, minus=minus, offset=d)
    sT.save("%s%+.1e_shape.npz" % (pre, d), zT + d * t)
print(json.dumps(info, indent=1))
