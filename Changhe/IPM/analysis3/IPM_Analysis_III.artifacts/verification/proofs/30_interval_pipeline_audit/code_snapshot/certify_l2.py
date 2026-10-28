"""Verified lower bound of sigma_min for the L_fix section in the lead's L^2(e^{mu~}) norm (no compensation, no scalar coordinates).
sigma_min^2 = lambda_min(B^T G_Y^{-1} B, G), G_Y = blockdiag_N G_test (the pi factor is already in the rows and Grams), same certificate as certify.py.
Usage: python3 certify_l2.py runs/<tag> [safety=0.98]
"""
import sys, os, json, gzip, time
import numpy as np
from flint import arb, arb_mat, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_section import load_ball
from certify import arbmat_from_dict, arbmat_from_float, sym_fill, verified_pd


def main(rundir, safety=0.98, prec=192):
    ctx.prec = prec; t0 = time.time()
    meta = json.load(open(os.path.join(rundir, "meta.json")))
    D = json.load(gzip.open(os.path.join(rundir, "matrices_dyadic.json.gz"), "rt"))
    ncol = meta["ncol"]; nt = meta["ntest"]; Mout = meta["Mout"]; active = meta["test_active"]; na = len(active); pos = {it: a_ for a_, it in enumerate(active)}
    labels = [c["label"] for c in meta["columns"]]
    G = sym_fill(arbmat_from_dict(D["GX"], (ncol, ncol), lambda p: (int(p[0]), int(p[1]))))
    Gt_full = sym_fill(arbmat_from_dict(D["GY"], (nt, nt), lambda p: (int(p[0]), int(p[1]))))
    Gtest = arb_mat(na, na)
    for i in active:
        for j in active: Gtest[pos[i], pos[j]] = Gt_full[i, j]
    Bfull = arbmat_from_dict(D["rows"], (Mout * nt, ncol), lambda p: (int(p[0]) * nt + int(p[1]), int(p[2])))
    B = arb_mat(Mout * na, ncol)
    for N in range(Mout):
        for it in active:
            for j in range(ncol): B[N * na + pos[it], j] = Bfull[N * nt + it, j]
    print("loaded (%.0fs): ncol %d, active test splines %d, rows %d" % (time.time() - t0, ncol, na, Mout * na), flush=True)
    okG, nEG = verified_pd(Gtest); okX, nEX = verified_pd(G)
    print("G_test PD: %s (%.2e); G PD: %s (%.2e)" % (okG, nEG, okX, nEX), flush=True)
    Gtest_f = np.array([[float(Gtest[i, j].mid()) for j in range(na)] for i in range(na)])
    Zt = arbmat_from_float(np.linalg.inv(Gtest_f)); W2 = Zt + Zt.transpose() - Zt.transpose() * Gtest * Zt; W2 = (W2 + W2.transpose()) * (arb(1) / 2)
    K = arb_mat(ncol, ncol); Bf = np.zeros((Mout * na, ncol))
    for N in range(Mout):
        blk = arb_mat(na, ncol)
        for i in range(na):
            for j in range(ncol): blk[i, j] = B[N * na + i, j]; Bf[N * na + i, j] = float(B[N * na + i, j].mid())
        K = K + blk.transpose() * W2 * blk
    Gf = np.array([[float(G[i, j].mid()) for j in range(ncol)] for i in range(ncol)])
    Ry = np.linalg.cholesky(Gtest_f); Cf = np.zeros_like(Bf)
    for N in range(Mout): Cf[N * na:(N + 1) * na] = np.linalg.solve(Ry, Bf[N * na:(N + 1) * na])
    Rx = np.linalg.cholesky(Gf); Cf = np.linalg.solve(Rx, Cf.T).T
    U, svals, Vt = np.linalg.svd(Cf, full_matrices=False)
    print("float generalized singular values: smallest 5 %s, largest %.4e, median %.4e" % (np.array2string(svals[-5:][::-1], precision=5), svals[0], np.median(svals)), flush=True)
    vmin = np.linalg.solve(Rx.T, Vt[-1]); xn = vmin / np.linalg.norm(vmin); top = np.argsort(-np.abs(xn))[:8]
    print("weakest direction:", [(labels[i] + "_m%d" % meta["columns"][i]["m"], round(float(xn[i]), 4)) for i in top])
    s = safety * svals[-1]; ok = False
    for attempt in range(6):
        sb = arb(s); M = K - G * (sb * sb); ok, nE = verified_pd(M)
        print("  try s = %.6f: PD %s (||E|| = %.3e)" % (s, ok, nE), flush=True)
        if ok: break
        s *= 0.9
    res = dict(rundir=rundir, operator=meta["operator"], norm=meta["norm"], ncol=ncol, rows=Mout * na, float_sigma_min=float(svals[-1]), float_sigma_max=float(svals[0]),
               float_sigma_small5=[float(x) for x in svals[-5:][::-1]], verified_lower_bound=(s if (ok and okG and okX) else None), Gtest_pd=okG, G_pd=okX,
               weakest_direction_top=[(labels[i], int(meta["columns"][i]["m"]), float(xn[i])) for i in top], seconds=time.time() - t0)
    json.dump(res, open(os.path.join(rundir, "certificate.json"), "w"), indent=1); print("saved certificate.json")


if __name__ == "__main__":
    a = sys.argv; main(a[1], float(a[2]) if len(a) > 2 else 0.98)
