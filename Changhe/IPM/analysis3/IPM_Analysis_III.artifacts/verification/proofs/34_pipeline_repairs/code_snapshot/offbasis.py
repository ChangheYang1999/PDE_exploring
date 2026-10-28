"""Assembly of the certified off-basis bound ||(I - Q_M) L P_N||_{X_N -> Y} (s2-num).
Inputs: runs/<tag>/{meta.json, matrices_dyadic.json.gz, norms.json (compensated S_j), tailbound2.json (compensated E_j^>)}.
Per column j (compensated phi_j + dk_j KP):  t_j >= ||(I - Q_M) L (phi_j + dk_j KP)||_Y with
   t(phi)^2 <= [S(phi) - r(phi)^T (Z + Z^T - Z^T G_Y Z) r(phi)] + D(phi)^2,   t_j <= t(phi_j) + |dk_j| t(KP),
   S from norms.json (exact), D^2 from tailbound.json (upper bound), r the rows of matrices_dyadic, Z a float approximate inverse of G_Y.
Operator bound: with R a floating Cholesky factor of G (domain Gram, exact dyadic), E := R^{-T} G R^{-1} - I (ball), ||E||_inf < 1:
   for h = sum_i y_i (phi R^{-1})_i: ||h||_X^2 = y^T (I + E) y >= (1 - ||E||) |y|^2 and ||T h||_Y <= sum_i |y_i| that_i, that_i := sum_j |R^{-1}_{ji}| t_j,
   so ||T||_{X_N -> Y} <= |that|_2 / sqrt(1 - ||E||_inf).
Usage: python3 offbasis.py runs/<tag> [w_J w_k w_tau]
"""
import sys, os, json, gzip, time
import numpy as np
from flint import arb, arb_mat, fmpz, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_section import load_ball
from certify import arbmat_from_dict, arbmat_from_float, sym_fill, inf_norm
from outward import fup, flo, max_upper


def main(rundir, w_J=1.0, w_k=1.0, w_tau=1.0, prec=192):
    ctx.prec = prec; t0 = time.time()
    meta = json.load(open(os.path.join(rundir, "meta.json")))
    D = json.load(gzip.open(os.path.join(rundir, "matrices_dyadic.json.gz"), "rt"))
    NR = json.load(open(os.path.join(rundir, "norms.json")))["exact"]
    ncol = meta["ncol"]; nt = meta["ntest"]; Mout = meta["Mout"]; sY = meta["weights"]["sY"]; sX = meta["weights"]["sX"]
    labels = [c["label"] for c in meta["columns"]]; col_m = [c["m"] for c in meta["columns"]]
    kq = meta["k"]; k = arb(fmpz(int(kq.split("/")[0]))) / fmpz(int(kq.split("/")[1])); c_l = 1 / k
    cvec = [load_ball(c["c"]) for c in meta["columns"]]; cKP = load_ball(meta["cKP"]); cTAU = load_ball(meta["cTAU"])
    Grem = sym_fill(arbmat_from_dict(D["GX"], (ncol, ncol), lambda p: (int(p[0]), int(p[1]))))
    Gtest = sym_fill(arbmat_from_dict(D["GY"], (nt, nt), lambda p: (int(p[0]), int(p[1]))))
    B = arbmat_from_dict(D["rows"], (Mout * nt, ncol), lambda p: (int(p[0]) * nt + int(p[1]), int(p[2])))
    BT = arbmat_from_dict(D["rows_tau"], (Mout * nt, 1), lambda p: (int(p[0]) * nt + int(p[1]), 0))
    BK = arbmat_from_dict(D["rows_kp"], (Mout * nt, 1), lambda p: (int(p[0]) * nt + int(p[1]), 0))
    # test splines 0 and nt-1 (clamped end splines) are not in the forcing space: drop their rows (set to 0) and decouple them in the test Gram
    inactive = [0, nt - 1]
    for it in inactive:
        for N in range(Mout):
            i = N * nt + it
            for j in range(B.ncols()): B[i, j] = arb(0)
            BT[i, 0] = arb(0); BK[i, 0] = arb(0)
        for j in range(nt):
            Gtest[it, j] = arb(0); Gtest[j, it] = arb(0)
        Gtest[it, it] = arb(1)
    # lower bound of r^T G_Y^{-1} r blockwise: G_Y,N = wY2(N) Gtest -> r_N^T Gtest^{-1} r_N / wY2(N)
    Gtest_f = np.array([[float(Gtest[i, j].mid()) for j in range(nt)] for i in range(nt)])
    Zt = arbmat_from_float(np.linalg.inv(Gtest_f)); W2 = Zt + Zt.transpose() - Zt.transpose() * Gtest * Zt
    def proj_norm2(rcol):
        """lower bound of ||Q_M g||_Y^2 from the row vector (Mout*nt x 1)"""
        tot = arb(0)
        for N in range(Mout):
            wY2 = arb(1 + (2 * N + 1) ** 2) ** sY
            rN = arb_mat(nt, 1, [rcol[N * nt + i, 0] for i in range(nt)])
            tot += (rN.transpose() * W2 * rN)[0, 0] / wY2
        return tot
    def S_of(key): return load_ball(NR[key])
    TB2 = json.load(open(os.path.join(rundir, "tailbound2.json")))["columns"]
    def t_of(S, lb, E2):
        # keep balls: the upper end of the enclosure of S - lb + E2, then its square root in ball arithmetic (verifier V027: no float rounding)
        v = S - lb + E2
        vu = arb(v.upper()) if float(v.upper()) > 0 else arb(0)
        return vu.sqrt()
    denom = 3 * c_l + k * cKP
    # compensated rows: r_j + dk_j r_KP ; compensated norms S ("col|j", "TAU" are already compensated in norms.json); tail energies from tailbound2
    tvec = []
    for j in range(ncol):
        dk = -cvec[j] * k / denom
        rj = arb_mat(Mout * nt, 1, [B[i, j] + dk * BK[i, 0] for i in range(Mout * nt)])
        tvec.append(t_of(S_of("col|%d" % j), proj_norm2(rj), arb(float(TB2[str(j)]["E2_upper"]))))
    dkT = -cTAU * k / denom
    rT = arb_mat(Mout * nt, 1, [BT[i, 0] + dkT * BK[i, 0] for i in range(Mout * nt)])
    tvec.append(t_of(S_of("TAU"), proj_norm2(rT), arb(float(TB2["TAU"]["E2_upper"]))))
    n_all = ncol + 1
    S_KP = arb(0); D2_KP = arb(0); t_KP = arb(0)
    print("per-column off-basis bounds (compensated): max %.4e, median %.4e, t_TAU %.4e (%.0fs)" % (fup(max_upper(tvec)), float(np.median([fup(x) for x in tvec])), fup(tvec[-1]), time.time() - t0), flush=True)
    # domain Gram with weights and the rank-one dk term (same as certify.py)
    dks = [-cvec[j] * k / denom for j in range(ncol)] + [dkT]
    G = arb_mat(n_all, n_all)
    for i in range(ncol):
        for j in range(ncol): G[i, j] = Grem[i, j] * (arb(1 + (2 * col_m[i]) ** 2) ** sX) if Grem[i, j] != 0 else arb(0)
    jJ = labels.index("J") if "J" in labels else None
    if jJ is not None: G[jJ, jJ] = arb(w_J)
    G[ncol, ncol] = arb(w_tau)
    for i in range(n_all):
        for j in range(n_all): G[i, j] = G[i, j] + arb(w_k) * dks[i] * dks[j]
    Gf = np.array([[float(G[i, j].mid()) for j in range(n_all)] for i in range(n_all)])
    R = np.linalg.cholesky(Gf).T                     # G ~ R^T R
    Rinv = np.linalg.inv(R)
    Rb = arbmat_from_float(R); Rinvb = Rb.inv()
    E = Rinvb.transpose() * G * Rinvb
    for i in range(n_all): E[i, i] = E[i, i] - 1
    # ||E||_inf as a ball (row sums in ball arithmetic), kept as a ball through the final inequality (verifier V027)
    rows_ = []
    for i in range(n_all):
        srow = arb(0)
        for j in range(n_all): srow += abs(E[i, j])
        rows_.append(srow)
    nEb = max_upper(rows_)                    # exact dyadic comparison (no float ties; verifier V033)
    nE = fup(nEb)
    that = [sum((abs(Rinvb[j, i]) * tvec[j] for j in range(n_all)), arb(0)) for i in range(n_all)]
    norm_that = sum((x * x for x in that), arb(0)).sqrt()
    bound = norm_that / (1 - arb(nEb.upper())).sqrt() if nE < 1 else None
    res = dict(rundir=rundir, offbasis_bound=(fup(bound) if bound is not None else None), offbasis_bound_ball=(bound.str(12, radius=True) if bound is not None else None), E_inf=nE, t_max=fup(max_upper(tvec)),
               t_TAU=fup(tvec[-1]),
               per_column=[(labels[j] if j < ncol else "TAU", fup(tvec[j])) for j in range(n_all)], seconds=time.time() - t0)
    json.dump(res, open(os.path.join(rundir, "offbasis.json"), "w"), indent=1)
    print("||(I - Q_M) L P_N||_{X_N -> Y} <= %s   (||E|| = %.3e)" % (res["offbasis_bound"], nE))
    return res


if __name__ == "__main__":
    a = sys.argv
    main(a[1], *(float(x) for x in a[2:5]))
