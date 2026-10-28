"""Compare the assembled floating 38-column input Gram G_Z of the junction-test run S1J1 with the verifier's exact scaled input Gram
(V267, proofs/239_s1j1_full_input/evidence/check.json, runs[1]: 640-bit balls, antiderivative moments; column order = meta.json 'new', whose
SHA256 the export records). Same quantities as gram_compare.py (entrywise relative discrepancy against the midpoints, whitened quadratic-form
relative error bounds with and without the ball radii; 60-digit mpmath; FLOATING estimates, input side only).   Usage: python3 gram_compare_s1j1.py runs/S1J1"""
import sys, json, glob, os, hashlib
from fractions import Fraction as F
import numpy as np, mpmath as mp
rd = sys.argv[1]
cert = json.load(open("verification/proofs/239_s1j1_full_input/evidence/check.json"))
meta_path = os.path.join(rd, "meta.json"); meta = json.load(open(meta_path)); new = meta["new"]; n = len(new)
assert hashlib.sha256(open(meta_path, "rb").read()).hexdigest() == cert["metadata_sha256"], "meta.json differs from the export's metadata hash"
rec = cert["runs"][1]; A = rec["scaled_input_Gram"]; assert len(A) == n == cert["n"] and all(len(row) == n for row in A)
parts = sorted(glob.glob(os.path.join(rd, "part_*.npz"))); assert len(parts) == int(meta["nworkers"]), parts
GZ = None
for f in parts:
    z = np.load(f, allow_pickle=True); GZ = z["GZ"] if GZ is None else GZ + z["GZ"]
asym = float(np.max(np.abs(GZ - GZ.T))); G = (GZ + GZ.T) / 2
mp.mp.dps = 60; DPS = mp.mp.dps
def lohi(d):
    lo = F(int(d["lo_binary"][0])) * F(2) ** int(d["lo_binary"][1]); hi = F(int(d["hi_binary"][0])) * F(2) ** int(d["hi_binary"][1]); assert lo <= hi; return lo, hi
def q2mp(q): return mp.mpf(q.numerator) / mp.mpf(q.denominator)
mid = mp.matrix(n, n); rad = mp.matrix(n, n); Gm = mp.matrix(n, n)
for i in range(n):
    for j in range(n):
        lo, hi = lohi(A[i][j]); mid[i, j] = q2mp((lo + hi) / 2); rad[i, j] = q2mp((hi - lo) / 2); Gm[i, j] = q2mp(F(float(G[i, j])))
msym = max(abs(mid[i, j] - mid[j, i]) for i in range(n) for j in range(n))
rel_max = mp.mpf(0); at = (0, 0); rels = []; rad_max = mp.mpf(0)
for i in range(n):
    for j in range(n):
        s = mp.sqrt(mid[i, i] * mid[j, j]); r = abs(Gm[i, j] - mid[i, j]) / s; rels.append(r); rad_max = max(rad_max, rad[i, j] / s)
        if r > rel_max: rel_max, at = r, (i, j)
rels.sort(); med = rels[len(rels) // 2]
print("S1J1: %d columns (blocks %s); part asymmetry %.2e; midpoint asymmetry %s" % (n, cert["block_sizes"], asym, mp.nstr(msym, 3)))
print("  largest entrywise relative discrepancy %s at (%d,%d) = %s / %s; median %s; largest exact-ball radius (same normalization) %s" % (mp.nstr(rel_max, 4), at[0], at[1], new[at[0]][1:], new[at[1]][1:], mp.nstr(med, 3), mp.nstr(rad_max, 3)))
# per-block worst entries (33 non-outer, 5 outer power columns)
blk = [i for i, v in enumerate(new) if not v[1].startswith("out")]; blo = [i for i, v in enumerate(new) if v[1].startswith("out")]
def worst(I, J):
    w = mp.mpf(0); a = None
    for i in I:
        for j in J:
            r = abs(Gm[i, j] - mid[i, j]) / mp.sqrt(mid[i, i] * mid[j, j])
            if r > w: w, a = r, (new[i][1], new[j][1])
    return mp.nstr(w, 3), a
print("  worst entrywise relative: non-outer block %s, outer block %s, cross block %s" % (worst(blk, blk), worst(blo, blo), worst(blk, blo)))
L = mp.cholesky(mid); T = mp.inverse(L).T; I = mp.eye(n); Tabs = mp.matrix([[abs(T[i, j]) for j in range(n)] for i in range(n)])
def rowbound(M): return max(sum(abs(M[a, b]) for b in range(n)) for a in range(n))
e = rowbound(T.T * mid * T - I); d = rowbound(T.T * (Gm - mid) * T); r = rowbound(Tabs.T * rad * Tabs)
if not (e + r < 1): print("  no quadratic-form bound: e + r = %s >= 1" % mp.nstr(e + r, 5)); b_mid = b_ball = None
else:
    b_mid = d / (1 - e); b_ball = (d + r) / (1 - e - r)
    print("  whitened identity defect e = %s; congruent input error d = %s; radius term r = %s; relative quadratic-form error bound (midpoint) %s, (any A in the balls) %s  [%d-digit mpmath; FLOATING estimates]" % (mp.nstr(e, 3), mp.nstr(d, 4), mp.nstr(r, 3), mp.nstr(b_mid, 4), mp.nstr(b_ball, 4), DPS))
# the same quadratic-form comparison restricted to the 33 non-outer columns (well conditioned)
midk = mp.matrix([[mid[i, j] for j in blk] for i in blk]); Gk = mp.matrix([[Gm[i, j] for j in blk] for i in blk]); Lk = mp.cholesky(midk); Tk = mp.inverse(Lk).T; Ik = mp.eye(len(blk))
nk = len(blk)
def rowbound_k(M): return max(sum(abs(M[a, b]) for b in range(nk)) for a in range(nk))
ek = rowbound_k(Tk.T * midk * Tk - Ik); dk = rowbound_k(Tk.T * (Gk - midk) * Tk)
print("  non-outer 33-column block: e = %s, d = %s, relative quadratic-form error bound (midpoint) %s" % (mp.nstr(ek, 3), mp.nstr(dk, 4), mp.nstr(dk / (1 - ek), 4)))
json.dump(dict(tag="S1J1", n=n, part_asymmetry=asym, max_entrywise_relative=float(rel_max), at=[int(at[0]), int(at[1])], median_entrywise_relative=float(med), max_ball_radius_relative=float(rad_max),
               whitened_identity_defect=float(e), congruent_input_error=float(d), radius_term=float(r), relative_quadratic_form_error_bound_midpoint=(float(b_mid) if b_mid is not None else None),
               relative_quadratic_form_error_bound_balls=(float(b_ball) if b_ball is not None else None), non_outer_block=dict(n=nk, e=float(ek), d=float(dk), bound=float(dk / (1 - ek))), mp_dps=DPS,
               export="proofs/239_s1j1_full_input/evidence/check.json runs[1] (V267)", note="floating comparison of the assembled S1J1 G_Z with the exact V267 Gram; input side only"),
          open(os.path.join(rd, "gram_compare.json"), "w"), indent=1); print("saved", os.path.join(rd, "gram_compare.json"))
