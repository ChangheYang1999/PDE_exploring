"""Sub-block analysis of a floating fsec.py S1 section (s2-num, 12:50Z; the inline script of logs/s1m3_bulk.log made reusable).
For the pure spline columns (labels sp<b> without '+') and for the full column set, by angular mode sets m <= 1, m <= 2, ..., and per mode:
smallest generalized singular values, the weakest vector's main coefficients with the radial centre of each coarse spline, and the
accumulation-rounding interval of the Rayleigh quotient (see s1_robust.py).   Usage: python3 s1_blocks.py runs/<tag>"""
import sys, json, glob, os, re
import numpy as np, scipy.linalg as sla
rd = sys.argv[1]; meta = json.load(open(os.path.join(rd, "meta.json"))); new = meta["new"]
GZ = None; BY = None
blocks = sorted(glob.glob(os.path.join(rd, "base_*.npz")) + glob.glob(os.path.join(rd, "part_*.npz")))
assert blocks, "no parts"
for f in blocks:
    z = np.load(f, allow_pickle=True); GZ = z["GZ"] if GZ is None else GZ + z["GZ"]; BY = z["BY"] if BY is None else BY + z["BY"]
GZ = (GZ + GZ.T) / 2; BY = (BY + BY.T) / 2
tm, tp = -4.8728634, 8.1353372; w = (tp - tm) / 26
def centre(lab):
    mt = re.match(r"sp(\d+)", lab); return None if not mt else round(tm + (int(mt.group(1)) - 3.5) * w, 2)
sb = np.sqrt(np.diag(BY)); sg = np.sqrt(np.diag(GZ)); modes = sorted(set(m for k, l, m in new))
def report(name, sel, nvec=2):
    if len(sel) < 2: return
    G = GZ[np.ix_(sel, sel)]; B = BY[np.ix_(sel, sel)]; d = np.sqrt(np.diag(G)); wn = np.linalg.eigvalsh(G / np.outer(d, d))
    ev, X = sla.eigh(B, G)
    print("%s (%d cols): normalized Gram eig min %.2e; smallest sv %s" % (name, len(sel), wn[0], np.round(np.sqrt(np.maximum(ev[:6], 0)), 4)))
    for i in range(nvec):
        x = X[:, i] / np.linalg.norm(X[:, i]); gq = x @ G @ x; bq = x @ B @ x
        eG = 1.3e-12 * (np.abs(x) @ sg[sel]) ** 2; eB = 1.3e-12 * (np.abs(x) @ sb[sel]) ** 2; top = np.argsort(-np.abs(x))[:8]
        flag = "quotient in [%.4f, %.4f]" % (np.sqrt((bq - eB) / (gq + eG)), np.sqrt((bq + eB) / (gq - eG))) if (gq > eG and bq > eB) else "UNDETERMINED"
        print("   sv %d = %.4f (g %.2e e_G %.1e, b %.2e e_B %.1e) %s" % (i, np.sqrt(max(ev[i], 0)), gq, eG, bq, eB, flag))
        print("      dir:", [(new[sel[j]][1], new[sel[j]][2], round(float(x[j]), 3), centre(new[sel[j]][1])) for j in top])
pure = lambda l: l.startswith("sp") and "+" not in l
for M in modes:
    report("pure splines m <= %d" % M, [i for i, (k, l, m) in enumerate(new) if pure(l) and m <= M])
for M in modes:
    report("pure splines m = %d only" % M, [i for i, (k, l, m) in enumerate(new) if pure(l) and m == M], nvec=1)
def spidx(l): return int(re.match(r"sp(\d+)", l).group(1))
for M in modes:      # verifier V210: of the pure columns only sp7..sp26 belong to the lead's actual high graph D_H(A0) (sp6, sp27 only to H_full)
    report("pure splines sp7..sp26 (D_H members, V210) m <= %d" % M, [i for i, (k, l, m) in enumerate(new) if pure(l) and 7 <= spidx(l) <= 26 and m <= M], nvec=1)
for M in modes:
    report("all columns m <= %d" % M, [i for i, (k, l, m) in enumerate(new) if m <= M], nvec=1)
