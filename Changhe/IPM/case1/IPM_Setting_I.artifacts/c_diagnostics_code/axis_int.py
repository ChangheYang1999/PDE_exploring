"""Lead axis residual tool (2026-10-18, after VERIFY_REPORT G69 (e)). Usage: python3 axis_int.py FIELDS.npz
From the axis arrays of an export (export_fit.py): w = W_1(x, 0), h = d_y W_2(x, 0), g = rho_y(x, 0), g' = d_x g, the
even limit of R/rho on the x-axis q0 = w g'/g + h - 1 (the y^1 coefficient T1 of SPEC D9 divided by g), the fit's
denominator on the axis den = 1 + |x g'/g + 1| + |(w - c_l x) g'/g + h - c_l|, and the label-free axis integral
I(eps) = int_{0.01}^{x* - eps} q0/|w| dx (the separatrix part of J; the verifier's code/vaxis.py computes the same
quantity with its own evaluator). Prints one JSON line."""
import sys
import json
import numpy as np
from scipy.integrate import simpson

d = np.load(sys.argv[1])
x = d["axis_x"]; w = d["axis_w"]; h = d["axis_h"]; g = d["axis_G1"]; gp = d["axis_G1_prime"]
cl = float(d["c_l_stored"])
q0 = w * gp / g + h - 1
den = 1 + np.abs(x * gp / g + 1) + np.abs((w - cl * x) * gp / g + h - cl)
i = np.flatnonzero((x > 5) & (x < 12) & (w[:] * np.roll(w, -1) < 0))[0]
xs = float(x[i] - w[i] * (x[i + 1] - x[i]) / (w[i + 1] - w[i]))
out = dict(file=sys.argv[1], c_l=cl, xstar=xs)
for eps in (0.03, 0.01):
    m = (x >= 0.01) & (x <= xs - eps)
    out["I(%g)" % eps] = float(simpson(q0[m] / np.abs(w[m]), x=x[m]))
m = (x > 0.01) & (x < xs)
k = np.argmax(np.abs(q0[m]))
out["max_abs_q0_on_(0,x*)"] = float(abs(q0[m][k])); out["at_x"] = float(x[m][k])
out["max_abs_q0_over_den_on_(0,x*)"] = float(np.max(np.abs(q0[m] / den[m])))
out["profile"] = {"%g" % v: [float(q0[np.argmin(abs(x - v))]), float(den[np.argmin(abs(x - v))])]
                  for v in (0.5, 1, 2, 3, 4, 5, 6, 7, 8)}
print(json.dumps(out))
