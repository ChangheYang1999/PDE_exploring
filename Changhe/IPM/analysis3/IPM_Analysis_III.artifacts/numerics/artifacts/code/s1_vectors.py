"""Export the generalized eigenvectors of the pure-spline block of a floating fsec.py S1 section and print the per-spline mode coefficients
(a_b for m = 1, c_b for m = 2) of the weakest vector; the angular factor of the remainder column combination is
a (cos 2 theta + 1) + c (cos 4 theta - 1) = 2 cos^2 theta (a - 4 c sin^2 theta), so a nearly constant ratio a/c across the splines means a
fixed angular profile r^3 cos^4 theta sin theta (a - 4 c sin^2 theta) times a broad radial profile.   Usage: python3 s1_vectors.py runs/<tag> out.json"""
import sys, json, glob, os, re
import numpy as np, scipy.linalg as sla
rd, outp = sys.argv[1], sys.argv[2]; meta = json.load(open(os.path.join(rd, "meta.json"))); new = meta["new"]
GZ = None; BY = None
for f in sorted(glob.glob(os.path.join(rd, "base_*.npz")) + glob.glob(os.path.join(rd, "part_*.npz"))):
    z = np.load(f, allow_pickle=True); GZ = z["GZ"] if GZ is None else GZ + z["GZ"]; BY = z["BY"] if BY is None else BY + z["BY"]
GZ = (GZ + GZ.T) / 2; BY = (BY + BY.T) / 2
sel = [i for i, (k, l, m) in enumerate(new) if l.startswith("sp") and "+" not in l]
G = GZ[np.ix_(sel, sel)]; B = BY[np.ix_(sel, sel)]; ev, X = sla.eigh(B, G)
tm, tp = -4.8728634, 8.1353372; w = (tp - tm) / 26
out = dict(note="pure-spline block of %s: generalized eigenvectors of (B_Y, G_Z); coefficient vectors (scaled coordinates, see meta column_scales) normalized in l2; FLOATING" % rd,
           sigma=[float(np.sqrt(max(e, 0))) for e in ev[:6]], columns=[(new[i][1], new[i][2], round(tm + (int(re.match(r"sp(\d+)", new[i][1]).group(1)) - 3.5) * w, 3)) for i in sel],
           vectors=[[float(v) for v in (X[:, k] / np.linalg.norm(X[:, k]))] for k in range(3)])
json.dump(out, open(outp, "w"), indent=1); print("sigma", np.round(out["sigma"], 4))
x = X[:, 0] / np.linalg.norm(X[:, 0]); coef = {}
for j, i in enumerate(sel): coef.setdefault(new[i][1], {})[new[i][2]] = float(x[j])
rows = sorted(((lab, {m: round(v, 3) for m, v in d.items()}) for lab, d in coef.items()), key=lambda r: -sum(abs(v) for v in r[1].values()))
print("weakest vector, per spline mode coefficients (largest first):", rows[:12])
