"""Certification of the finite section (s2-num): verified lower bound of the smallest generalized singular value
   sigma_min = min_x sqrt( x^T B^T G_Y^{-1} B x / x^T G_X x )
of A = Q_M L P_N in the stated norms, from the exact-dyadic interval matrices of run_section.py.

Column space: compensated columns phi_j + dk_j KP (dk_j = -c_j k / (3 c_l + k c_KP), so the far-field tail of the image cancels exactly)
for all basis columns (J included) and TAU + dk_TAU KP.  Domain Gram: G = blockdiag(G_rem (exact integrals of the remainder columns),
w_J, w_tau) + w_k dk dk^T.  Forcing Gram: G_Y = blockdiag_N (wY2(N) G_test) (the rows already carry wY2(N)).
Lower bound: for SPD G_Y and any symmetric Z0, G_Y^{-1} >= 2 Z0 - Z0 G_Y Z0; hence B^T G_Y^{-1} B >= B^T (2 Z0 - Z0 G_Y Z0) B =: K.
If K - s^2 G is positive semidefinite then sigma_min >= s.  PSD check: with an approximate Cholesky factor Lf of M = K - s^2 G,
E = Lf^{-1} M Lf^{-T} - I computed in ball arithmetic; ||E||_inf < 1 implies M positive definite.
Usage: python3 certify.py runs/<tag> [w_J=1] [w_k=1] [w_tau=1] [safety=0.98]
"""
import sys, os, json, gzip, time
import numpy as np
from flint import arb, arb_mat, fmpz, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_section import load_ball


def arbmat_from_dict(dd, shape, keyfun):
    n, m = shape
    M = arb_mat(n, m)
    for kk, q in dd.items():
        parts = kk.split("|"); i = keyfun(parts)
        M[i[0], i[1]] = load_ball(q)
    return M


def arbmat_from_float(A):
    n, m = A.shape
    return arb_mat(n, m, [arb(float(x)) for x in A.ravel()])


def sym_fill(M):
    n = M.nrows()
    for i in range(n):
        for j in range(i + 1, n):
            if M[j, i] == 0: M[j, i] = M[i, j]
            elif M[i, j] == 0: M[i, j] = M[j, i]
    return M


def max_abs(M):
    n, m = M.nrows(), M.ncols()
    return max(float(abs(M[i, j]).upper()) for i in range(n) for j in range(m))


def inf_norm(M):
    """upper bound of the infinity norm, row sums in ball arithmetic"""
    n, m = M.nrows(), M.ncols(); best = arb(0)
    for i in range(n):
        s = arb(0)
        for j in range(m): s += abs(M[i, j])
        best = arb.max(best, s) if hasattr(arb, 'max') else (s if float(s.upper()) > float(best.upper()) else best)
    return float(best.upper())


def verified_pd(M, label=""):
    """returns (ok, ||E||_inf) for the ball matrix M (symmetric): approximate Cholesky, then E = Lf^{-1} M Lf^{-T} - I"""
    n = M.nrows()
    Mf = np.array([[float(M[i, j].mid()) for j in range(n)] for i in range(n)])
    try:
        Lf = np.linalg.cholesky(Mf)
    except np.linalg.LinAlgError:
        return False, float("inf")
    Lb = arbmat_from_float(Lf)
    Linv = Lb.inv()
    E = Linv * M * Linv.transpose()
    for i in range(n): E[i, i] = E[i, i] - 1
    nE = inf_norm(E)
    return nE < 1, nE


def main(rundir, w_J=1.0, w_k=1.0, w_tau=1.0, safety=0.98, prec=192):
    ctx.prec = prec
    meta = json.load(open(os.path.join(rundir, "meta.json")))
    D = json.load(gzip.open(os.path.join(rundir, "matrices_dyadic.json.gz"), "rt"))
    ncol = meta["ncol"]; nt = meta["ntest"]; Mout = meta["Mout"]
    labels = [c["label"] for c in meta["columns"]]
    kq = meta["k"]; k = arb(fmpz(int(kq.split("/")[0]))) / fmpz(int(kq.split("/")[1])) if "/" in kq else arb(kq)
    c_l = 1 / k
    cvec = [load_ball(c["c"]) for c in meta["columns"]]; cKP = load_ball(meta["cKP"]); cTAU = load_ball(meta["cTAU"])
    t0 = time.time()
    Grem = sym_fill(arbmat_from_dict(D["GX"], (ncol, ncol), lambda p: (int(p[0]), int(p[1]))))
    Gtest = sym_fill(arbmat_from_dict(D["GY"], (nt, nt), lambda p: (int(p[0]), int(p[1]))))
    B = arbmat_from_dict(D["rows"], (Mout * nt, ncol), lambda p: (int(p[0]) * nt + int(p[1]), int(p[2])))
    BT = arbmat_from_dict(D["rows_tau"], (Mout * nt, 1), lambda p: (int(p[0]) * nt + int(p[1]), 0))
    BK = arbmat_from_dict(D["rows_kp"], (Mout * nt, 1), lambda p: (int(p[0]) * nt + int(p[1]), 0))
    print("loaded matrices (%.0fs): ncol %d, rows %d x %d" % (time.time() - t0, ncol, Mout, nt), flush=True)
    # compensated columns: basis columns + TAU; dk_j = -c_j k / (3 c_l + k c_KP)
    denom = 3 * c_l + k * cKP
    assert not denom.contains(arb(0)), "compensation denominator must exclude zero"
    cols_all = list(range(ncol)) + ["TAU"]
    n_all = ncol + 1
    dk = [-(cvec[j] if j != "TAU" else cTAU) * k / denom for j in cols_all]
    Bc = arb_mat(Mout * nt, n_all)
    for jj, j in enumerate(cols_all):
        src = B if j != "TAU" else BT
        col = j if j != "TAU" else 0
        for i in range(Mout * nt):
            Bc[i, jj] = src[i, col] + dk[jj] * BK[i, 0]
    # domain Gram: remainder block (J has zero rows/cols there), scalar weights, rank-one dk dk^T
    G = arb_mat(n_all, n_all)
    sX = meta["weights"]["sX"]; col_m = [cc["m"] for cc in meta["columns"]]
    for i in range(ncol):
        for j in range(ncol):
            G[i, j] = Grem[i, j] * (arb(1 + (2 * col_m[i]) ** 2) ** sX) if Grem[i, j] != 0 else arb(0)
    jJ = labels.index("J") if "J" in labels else None
    if jJ is not None: G[jJ, jJ] = arb(w_J)
    G[ncol, ncol] = arb(w_tau)
    for i in range(n_all):
        for j in range(n_all): G[i, j] = G[i, j] + arb(w_k) * dk[i] * dk[j]
    # forcing Gram blocks: wY2(N) Gtest; Z0 approx inverse (float, block)
    sY = meta["weights"]["sY"]
    Gtest_f = np.array([[float(Gtest[i, j].mid()) for j in range(nt)] for i in range(nt)])
    Zt_f = np.linalg.inv(Gtest_f)
    print("test Gram: cond %.3e" % np.linalg.cond(Gtest_f), flush=True)
    # verify Gtest > 0
    okG, nEG = verified_pd(Gtest); print("G_test positive definite: %s (||E|| = %.3e)" % (okG, nEG), flush=True)
    okX, nEX = verified_pd(G); print("G_X positive definite: %s (||E|| = %.3e)" % (okX, nEX), flush=True)
    # K = B^T (2 Z0 - Z0 G_Y Z0) B, blockwise over N: Z0_N = Zt / wY2(N), G_Y,N = wY2(N) Gtest
    Zt = arbmat_from_float(Zt_f)           # any real matrix Z: G^{-1} >= Z + Z^T - Z^T G Z (exact in ball arithmetic)
    W2 = Zt + Zt.transpose() - Zt.transpose() * Gtest * Zt
    W2 = (W2 + W2.transpose()) * (arb(1) / 2)   # symmetric by construction; symmetrize the enclosure
    K = arb_mat(n_all, n_all)
    Bf = np.zeros((Mout * nt, n_all)); Gf = np.array([[float(G[i, j].mid()) for j in range(n_all)] for i in range(n_all)])
    for N in range(Mout):
        wY2 = (1 + (2 * N + 1) ** 2) ** sY
        blk = arb_mat(nt, n_all)
        for i in range(nt):
            for j in range(n_all): blk[i, j] = Bc[N * nt + i, j]; Bf[N * nt + i, j] = float(Bc[N * nt + i, j].mid())
        K = K + (blk.transpose() * W2 * blk) * (arb(1) / wY2)
    print("K assembled (%.0fs)" % (time.time() - t0), flush=True)
    # float estimate of the generalized singular values
    Ry = np.linalg.cholesky(Gtest_f)
    Cf = np.zeros_like(Bf)
    for N in range(Mout):
        wY2 = (1 + (2 * N + 1) ** 2) ** sY
        Cf[N * nt:(N + 1) * nt] = np.linalg.solve(Ry, Bf[N * nt:(N + 1) * nt]) / np.sqrt(wY2)
    Rx = np.linalg.cholesky(Gf)
    Cf = np.linalg.solve(Rx, Cf.T).T
    svals = np.linalg.svd(Cf, compute_uv=False)
    print("float generalized singular values: smallest 5 %s, largest %.4e, median %.4e" % (np.array2string(svals[-5:][::-1], precision=5), svals[0], np.median(svals)), flush=True)
    # weakest direction: dominant labels
    U, S, Vt = np.linalg.svd(Cf, full_matrices=False)
    vmin = np.linalg.solve(Rx.T, Vt[-1])     # coordinates x of the weakest direction (x = Rx^{-1} v)
    xn = vmin / np.linalg.norm(vmin)
    top = np.argsort(-np.abs(xn))[:8]
    print("weakest direction (coordinate mass): ", [(labels[i] + "_m%d" % meta["columns"][i]["m"] if i < ncol else "TAU", round(float(xn[i]), 4)) for i in top])
    # verified lower bound
    s = safety * svals[-1]
    ok = False
    for attempt in range(6):
        sb = arb(s); M = K - G * (sb * sb)
        ok, nE = verified_pd(M)
        print("  try s = %.6f: K - s^2 G positive definite: %s (||E|| = %.3e)" % (s, ok, nE), flush=True)
        if ok: break
        s *= 0.9
    res = dict(rundir=rundir, n_all=n_all, w_J=w_J, w_k=w_k, w_tau=w_tau, float_sigma_min=float(svals[-1]), float_sigma_max=float(svals[0]),
               float_sigma_small5=[float(x) for x in svals[-5:][::-1]], verified_lower_bound=(s if (ok and okG and okX) else None), Gtest_pd=okG, GX_pd=okX,
               weakest_direction_top=[(labels[i] if i < ncol else "TAU", int(meta["columns"][i]["m"]) if i < ncol else -1, float(xn[i])) for i in top],
               dk_TAU=str(dk[-1].str(8)), seconds=time.time() - t0)
    json.dump(res, open(os.path.join(rundir, "certificate.json"), "w"), indent=1)
    print("saved", os.path.join(rundir, "certificate.json"))
    return res


if __name__ == "__main__":
    a = sys.argv
    main(a[1], float(a[2]) if len(a) > 2 else 1.0, float(a[3]) if len(a) > 3 else 1.0, float(a[4]) if len(a) > 4 else 1.0, float(a[5]) if len(a) > 5 else 0.98)
