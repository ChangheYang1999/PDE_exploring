"""Robustness analysis of a floating fsec.py section (s2-num, 10:00Z): generalized singular values of the stored double pair (B_Y, G_Z)
solved at 50 digits (mpmath), near-dependence of the columns (normalized Gram eigenvectors), Rayleigh-quotient intervals of the computed singular vectors
under an accumulation-rounding estimate 1.3e-12 (sum_i |x_i| sqrt(diag))^2 (eps times about 6000 accumulated node terms), values after removing
near-dependent directions, and sub-blocks (pure spline columns, per angular mode m).   Usage: python3 s1_robust.py runs/<tag>"""
import sys, json, glob
import numpy as np, scipy.linalg as sla, mpmath as mp
rd = sys.argv[1]; meta = json.load(open(rd + "/meta.json")); new = meta["new"]
GZ = None; BY = None
files = sorted(glob.glob(rd + "/part_*.npz")) or sorted(glob.glob(rd + "/base_*.npz") + glob.glob(rd + "/ckpt_*.npz"))
for f in files:
    z = np.load(f, allow_pickle=True); GZ = z["GZ"] if GZ is None else GZ + z["GZ"]; BY = z["BY"] if BY is None else BY + z["BY"]
GZ = (GZ + GZ.T) / 2; BY = (BY + BY.T) / 2; n = GZ.shape[0]
print("columns (%d):" % n, [(l, m) for k, l, m in new])
d = np.sqrt(np.diag(GZ)); Gn = GZ / np.outer(d, d); w, V = np.linalg.eigh(Gn)
print("normalized G_Z eigenvalues (smallest 8):", np.array2string(w[:8], precision=2))
for i in range(4):
    idx = np.argsort(-np.abs(V[:, i]))[:5]; print("  near-dependence %d (eig %.2e):" % (i, w[i]), [(new[j][1], new[j][2], round(float(V[j, i]), 3)) for j in idx])
ev, X = sla.eigh(BY, GZ); print("scipy generalized sv (smallest 8):", np.array2string(np.sqrt(np.maximum(ev[:8], 0)), precision=4))
mp.mp.dps = 50
G = mp.matrix(GZ.tolist()); B = mp.matrix(BY.tolist()); L = mp.cholesky(G); Li = mp.inverse(L); Bw = Li * B * Li.T; Bw = (Bw + Bw.T) / 2
Bwf = np.array([[float(Bw[i, j]) for j in range(n)] for i in range(n)]); Bwf = (Bwf + Bwf.T) / 2
E = sorted(np.linalg.eigvalsh(Bwf).tolist()); print("generalized sv (50-digit whitening, double eigen-solve; smallest 8):", [round(float(np.sqrt(max(x, 0))), 5) for x in E[:8]])
sb = np.sqrt(np.diag(BY)); sg = d
for i in range(6):
    x = X[:, i] / np.linalg.norm(X[:, i]); gq = x @ GZ @ x; bq = x @ BY @ x
    errB = 1.3e-12 * (np.abs(x) @ sb) ** 2; errG = 1.3e-12 * (np.abs(x) @ sg) ** 2; top = np.argsort(-np.abs(x))[:4]
    # accumulation-rounding model (astra referee junction_ref, item 3): for the FIXED computed vector x the true Rayleigh quotient lies in
    # [(b - e_B)/(g + e_G), (b + e_B)/(g - e_G)] (an upper bound of the infimum over the subspace); the ORDERED smallest value is not bounded below by this.
    if gq > errG and bq > errB: lo_, hi_ = np.sqrt((bq - errB) / (gq + errG)), np.sqrt((bq + errB) / (gq - errG)); flag = "quotient in [%.4f, %.4f]" % (lo_, hi_)
    else: flag = "UNDETERMINED (quotient below the rounding estimate)"
    print("sv %d = %.4f: x^T G_Z x = %.3e (rounding est %.1e), x^T B_Y x = %.3e (est %.1e) %s; dir %s" % (i, np.sqrt(max(ev[i], 0)), gq, errG, bq, errB, flag, [(new[j][1], new[j][2], round(float(x[j]), 2)) for j in top]))
for thr in (1e-10, 1e-8, 1e-6, 1e-4):
    keep = w > thr; W = V[:, keep] / d[:, None]; Gs = W.T @ GZ @ W; Bs = W.T @ BY @ W
    evs = sla.eigh((Bs + Bs.T) / 2, (Gs + Gs.T) / 2, eigvals_only=True)
    print("drop normalized-Gram directions below %.0e: keep %d, smallest 5 sv %s" % (thr, keep.sum(), np.array2string(np.sqrt(np.maximum(evs[:5], 0)), precision=4)))
blocks = [("pure spline columns", [i for i, (k, l, m) in enumerate(new) if "out" not in l and "in" not in l]), ("no outer power columns", [i for i, (k, l, m) in enumerate(new) if "out" not in l])]
blocks += [("m = %d only" % mm, [i for i, (k, l, m) in enumerate(new) if m == mm]) for mm in sorted(set(m for k, l, m in new))]
for name, sel in blocks:
    if len(sel) < 2: continue
    evs = sla.eigh(BY[np.ix_(sel, sel)], GZ[np.ix_(sel, sel)], eigvals_only=True)
    print("%s (%d cols): smallest 4 sv %s" % (name, len(sel), np.array2string(np.sqrt(np.maximum(evs[:4], 0)), precision=4)))
