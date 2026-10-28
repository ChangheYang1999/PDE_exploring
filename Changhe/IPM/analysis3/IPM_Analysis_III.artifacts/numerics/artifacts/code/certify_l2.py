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
    # Two-sided whitening (05:45Z): the L^2(e^{8t + mu~}) Grams span 60 orders of magnitude (inner power columns ~1e-23, far columns ~1e28;
    # test splines 1e-20 .. 1e48), so float Cholesky factors are meaningless. Change bases exactly: T_X = L_X^{-T}, T_Y = L_Y^{-T} from
    # 140-digit mpmath Choleskys of the exact dyadic midpoints (V056 recipe); G -> T_X^T G T_X ~ I, Gtest -> T_Y^T Gtest T_Y ~ I,
    # B_N -> T_Y^T B_N T_X in ball arithmetic. The generalized singular values of (B, G, G_Y) are invariant under both changes.
    import mpmath
    mpmath.mp.dps = 140
    def mp_mid(x):
        m, e = x.mid().man_exp(); return mpmath.mpf(int(m)) * mpmath.power(2, int(e))
    def whitener(M, n):
        Mmp = mpmath.matrix([[mp_mid(M[i, j]) for j in range(n)] for i in range(n)])
        L = mpmath.cholesky(Mmp); Tm = mpmath.inverse(L).T
        return arb_mat(n, n, [arb(mpmath.nstr(Tm[i, j], 45)) for i in range(n) for j in range(n)]), Mmp
    TX, Gmp = whitener(G, ncol); TY, Gtmp = whitener(Gtest, na)
    condX = float(mpmath.cond(Gmp)) if ncol <= 200 else None
    G = TX.transpose() * G * TX; G = (G + G.transpose()) * (arb(1) / 2)
    Gtest = TY.transpose() * Gtest * TY; Gtest = (Gtest + Gtest.transpose()) * (arb(1) / 2)
    Bw = arb_mat(Mout * na, ncol)
    for N in range(Mout):
        blk = arb_mat(na, ncol)
        for i in range(na):
            for j in range(ncol): blk[i, j] = B[N * na + i, j]
        blk = TY.transpose() * blk * TX
        for i in range(na):
            for j in range(ncol): Bw[N * na + i, j] = blk[i, j]
    B = Bw
    Gf = np.array([[float(G[i, j].mid()) for j in range(ncol)] for i in range(ncol)]); Gtest_f = np.array([[float(Gtest[i, j].mid()) for j in range(na)] for i in range(na)])
    print("whitened: max |G - I| %.2e, max |Gtest - I| %.2e, raw cond(G) %s (%.0fs)" % (np.abs(Gf - np.eye(ncol)).max(), np.abs(Gtest_f - np.eye(na)).max(), ("%.2e" % condX) if condX else "n/a", time.time() - t0), flush=True)
    okG, nEG = verified_pd(Gtest); okX, nEX = verified_pd(G)
    print("whitened G_test PD: %s (%.2e); whitened G PD: %s (%.2e)" % (okG, nEG, okX, nEX), flush=True)
    Zt = arbmat_from_float(np.linalg.inv(Gtest_f)); W2 = Zt + Zt.transpose() - Zt.transpose() * Gtest * Zt; W2 = (W2 + W2.transpose()) * (arb(1) / 2)
    K = arb_mat(ncol, ncol); Bf = np.zeros((Mout * na, ncol))
    for N in range(Mout):
        blk = arb_mat(na, ncol)
        for i in range(na):
            for j in range(ncol): blk[i, j] = B[N * na + i, j]; Bf[N * na + i, j] = float(B[N * na + i, j].mid())
        K = K + blk.transpose() * W2 * blk
    Ry = np.linalg.cholesky(Gtest_f); Cf = np.zeros_like(Bf)
    for N in range(Mout): Cf[N * na:(N + 1) * na] = np.linalg.solve(Ry, Bf[N * na:(N + 1) * na])
    Rx = np.linalg.cholesky(Gf); Cf = np.linalg.solve(Rx, Cf.T).T
    U, svals, Vt = np.linalg.svd(Cf, full_matrices=False)
    print("float generalized singular values: smallest 5 %s, largest %.4e, median %.4e" % (np.array2string(svals[-5:][::-1], precision=5), svals[0], np.median(svals)), flush=True)
    TXf = np.array([[float(TX[i, j].mid()) for j in range(ncol)] for i in range(ncol)])
    vmin = TXf @ np.linalg.solve(Rx.T, Vt[-1]); xn = vmin / np.linalg.norm(vmin); top = np.argsort(-np.abs(xn))[:8]       # original-basis coordinates
    print("weakest direction (original coordinates):", [(labels[i] + "_m%d" % meta["columns"][i]["m"], round(float(xn[i]), 4)) for i in top])
    s = safety * svals[-1]; ok = False
    for attempt in range(6):
        sb = arb(s); M = K - G * (sb * sb); ok, nE = verified_pd(M)
        print("  try s = %.6f: PD %s (||E|| = %.3e)" % (s, ok, nE), flush=True)
        if ok: break
        s *= 0.9
    res = dict(rundir=rundir, operator=meta["operator"], norm=meta["norm"], ncol=ncol, rows=Mout * na, whitening="two-sided, exact midpoints, mpmath 140 digits", raw_cond_G=condX, float_sigma_min=float(svals[-1]), float_sigma_max=float(svals[0]),
               float_sigma_small5=[float(x) for x in svals[-5:][::-1]], verified_lower_bound=(s if (ok and okG and okX) else None), Gtest_pd=okG, G_pd=okX,
               weakest_direction_top=[(labels[i], int(meta["columns"][i]["m"]), float(xn[i])) for i in top], seconds=time.time() - t0)
    json.dump(res, open(os.path.join(rundir, "certificate.json"), "w"), indent=1); print("saved certificate.json")


if __name__ == "__main__":
    a = sys.argv; main(a[1], float(a[2]) if len(a) > 2 else 0.98)
