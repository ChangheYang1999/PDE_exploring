"""Compare the assembled floating 78-column input Gram G_Z of an S1 pure-spline run with the verifier's exact scaled input Gram
(V202, proofs/198_pure_spline_input_gram/evidence/gram_512_640.json, runs/<tag>/exact_scaled_input_Gram, 640-bit balls).
Reports (1) the largest entrywise relative discrepancy |G_ij - mid_ij| / sqrt(mid_ii mid_jj) (computed in mpmath, 60 digits, against the
60-digit midpoints; the exact doubles of G are converted exactly) and the largest ball radius in the same normalization, (2) the congruent
(whitened) quadratic-form relative error ||T^T (G - C) T||_row / (1 - ||T^T C T - I||_row) with C the midpoint matrix and T a 60-digit
whitener of C (same form as the verifier's check.py, there in Arb), and (3) the same bound with the ball radii included:
(d + r) / (1 - e - r), r = || |T|^T R |T| ||_row, R the radius matrix, which bounds sup_x |x^T (G - A) x| / x^T A x for the exact A inside
the balls (valid when e + r < 1; mpmath rounding of the 60-digit arithmetic is not enclosed, so (2) and (3) remain FLOATING estimates).
Nothing here certifies anything about the output Gram B_Y. Referee: astra merge_gram_ref (16:05Z).   Usage: python3 gram_compare.py runs/<tag> [S1M4P|S1M3]"""
import sys, json, glob, os
from fractions import Fraction as F
import numpy as np, mpmath as mp
rd = sys.argv[1]; tag = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(rd.rstrip("/"))
cert = json.load(open("verification/proofs/198_pure_spline_input_gram/evidence/gram_512_640.json"))
rec = cert["runs"][tag]; meta = json.load(open(os.path.join(rd, "meta.json"))); new = meta["new"]
sel = rec["selected_new_indices"]; n = len(sel)
# verifier declaration [i, m, scale fraction] versus producer labels ['rem', 'sp<i>', m]; the scales are the meta column_scales (exact doubles)
assert [(int(new[i][1][2:]), new[i][2]) for i in sel] == [(b[0], b[1]) for b in rec["basis_declaration"]], "basis declaration mismatch"
orig = {(l, m): i for i, (l, m) in enumerate(zip(meta["labels"], meta["col_m"]))}   # original S0 column index of each (label, mode)
scales = [F(meta["column_scales"][orig[(new[i][1], new[i][2])]]) for i in sel]
assert all(F(b[2]) == sc for b, sc in zip(rec["basis_declaration"], scales)), "scale mismatch"
parts = sorted(glob.glob(os.path.join(rd, "part_*.npz"))); assert len(parts) == int(meta.get("nworkers", len(parts))), "unexpected number of part files: %s" % parts
GZ = None
for f in parts:
    z = np.load(f, allow_pickle=True); GZ = z["GZ"] if GZ is None else GZ + z["GZ"]
asym = float(np.max(np.abs(GZ - GZ.T))); G = (GZ + GZ.T) / 2; G = G[np.ix_(sel, sel)]
mp.mp.dps = 60; DPS = mp.mp.dps
def lohi(d):
    lo = F(int(d["lo_binary"][0])) * F(2) ** int(d["lo_binary"][1]); hi = F(int(d["hi_binary"][0])) * F(2) ** int(d["hi_binary"][1]); assert lo <= hi; return lo, hi
def q2mp(q): return mp.mpf(q.numerator) / mp.mpf(q.denominator)
mid = mp.matrix(n, n); rad = mp.matrix(n, n); Gm = mp.matrix(n, n)
for i in range(n):
    for j in range(n):
        lo, hi = lohi(rec["exact_scaled_input_Gram"][i][j]); mid[i, j] = q2mp((lo + hi) / 2); rad[i, j] = q2mp((hi - lo) / 2); Gm[i, j] = q2mp(F(float(G[i, j])))
msym = max(abs(mid[i, j] - mid[j, i]) for i in range(n) for j in range(n))
rel_max = mp.mpf(0); at = (0, 0); rels = []; rad_max = mp.mpf(0)
for i in range(n):
    for j in range(n):
        s = mp.sqrt(mid[i, i] * mid[j, j]); r = abs(Gm[i, j] - mid[i, j]) / s; rels.append(r); rad_max = max(rad_max, rad[i, j] / s)
        if r > rel_max: rel_max, at = r, (i, j)
rels.sort(); med = rels[len(rels) // 2]
print("%s: %d columns; part asymmetry %.2e; midpoint asymmetry %s" % (tag, n, asym, mp.nstr(msym, 3)))
print("  largest entrywise relative discrepancy %s at (%d,%d) = %s / %s; median %s; largest exact-ball radius (same normalization) %s" % (mp.nstr(rel_max, 4), at[0], at[1], new[sel[at[0]]][1:], new[sel[at[1]]][1:], mp.nstr(med, 3), mp.nstr(rad_max, 3)))
L = mp.cholesky(mid); T = mp.inverse(L).T  # mid = L L^T, T = L^{-T}: T^T mid T = I
I = mp.eye(n); Tabs = mp.matrix([[abs(T[i, j]) for j in range(n)] for i in range(n)])
def rowbound(M): return max(sum(abs(M[a, b]) for b in range(n)) for a in range(n))
e = rowbound(T.T * mid * T - I); d = rowbound(T.T * (Gm - mid) * T); r = rowbound(Tabs.T * rad * Tabs)
if not (e + r < 1): raise SystemExit("no bound: whitener defect e + r = %s >= 1" % mp.nstr(e + r, 5))
b_mid = d / (1 - e); b_ball = (d + r) / (1 - e - r)
print("  whitened identity defect e = %s; congruent input error d = %s; radius term r = %s; relative quadratic-form error bound (midpoint) %s, (any A in the balls) %s  [%d-digit mpmath; FLOATING estimates]" % (mp.nstr(e, 3), mp.nstr(d, 4), mp.nstr(r, 3), mp.nstr(b_mid, 4), mp.nstr(b_ball, 4), DPS))
json.dump(dict(tag=tag, n=n, part_asymmetry=asym, midpoint_asymmetry=float(msym), max_entrywise_relative=float(rel_max), at=[int(at[0]), int(at[1])], median_entrywise_relative=float(med),
               max_ball_radius_relative=float(rad_max), whitened_identity_defect=float(e), congruent_input_error=float(d), radius_term=float(r),
               relative_quadratic_form_error_bound_midpoint=float(b_mid), relative_quadratic_form_error_bound_balls=float(b_ball), mp_dps=DPS,
               note="floating comparison of the assembled G_Z (pinv input quotients, V187) with the exact V202 Gram (60-digit mpmath; mpmath rounding not enclosed); input side only"),
          open(os.path.join(rd, "gram_compare.json"), "w"), indent=1); print("saved", os.path.join(rd, "gram_compare.json"))
