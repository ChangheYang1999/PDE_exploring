"""Does the finite section of 7.4b see the scaling tangent K = rho~ - X.grad rho~?  (NUM_REPORT section 9 item 0; FLOATING, evidence only)
Stage A (`A`): rebuild the H1m Gram of the section's F- columns (the pickled function columns plus KP and TAU with their angular vectors A0, Bm
from the section's _vec.npz; checked against the saved diagonal G_diag and against a 48-node rule), evaluate K = x^2 y sum_m a~_m(t) cos 2m theta
with a~_m = -2 a_m - a_m' for ALL modes m < M = 260 (vectorized spline / exp-poly evaluation; the angular coupling of the Phi_m = cos^2 sin cos 2m
theta basis reaches |m - m'| <= 3, astra/kproj1) on a fine node set (the trial's own knot cells added to the breakpoints), and compute the
X-orthogonal projection P K of K onto the retained constrained span exactly as c2_gram2 builds it (join constraints: NJ = 0 -> C^0, NJ = 1 -> C^1
at tmin and t0; eigen-cut thresh on the equilibrated constrained Gram). ||K||_X^2 is computed in the same Gram (same quadrature, same range), so
cos^2 = ||P K||_X^2 / ||K||_X^2 <= 1 and ||K - P K||_X^2 = ||K||_X^2 - ||P K||_X^2 are consistent. Version 2 after the referee round astra/kproj1
(version 1 used m < Mh + 2 and omitted KP/TAU: its cos^2 values were those of the m < 18 part and could exceed 1).
Usage: python3 src/c2_Kproj.py A trial.npz section_cols.pkl section_vec.npz NJ thresh out.npz [free]     (KPROJ_K2_JSON=... prints the modal norm too)
       python3 src/c2_Kproj.py KT trial.npz section_cols.pkl section_vec.npz out_piece.npz m_lo m_hi    (row images of KP, TAU over the modes m_lo <= m < m_hi; pieces, then)
       python3 src/c2_Kproj.py KTmerge runs/kproj/KT_images.npz piece1.npz piece2.npz ...                  (merged KP/TAU images; needed by stage B)
       python3 src/c2_Kproj.py B trial.npz section_cols.pkl section_vec.npz Kproj_out.npz out.json          (stage B: L(P K) at the section's rows, four row functionals)
       python3 src/c2_Kproj.py C trial.npz section_vec.npz m_lo m_hi out_piece.npz                           (stage C: assembler on K's own pieces, modes m_lo <= m < m_hi)
       python3 src/c2_Kproj.py Cmerge KprojB_img.npz piece1.npz ... out.json                                 (sum of the stage-C pieces against the direct image)
"""
import sys, os, json, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
from lin_assembly import ExpPolyBasis
from c2_gram2 import piece_jet, radial_nodes, angular_matrices_H1, GAMMA_H1
from xnorm_BKK import TrialK


def _popen(path):
    """Open a pickled column-piece file for reading; falls back to path + '.gz' (the artifacts folder stores the _cols.pkl pieces gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rb")
    return open(path, "rb")


def K_pieces(T, Mparts):
    """Radial pieces (ExpPolyBasis format) of a~_m for m < Mparts: inner exp-poly terms (sigma = t - tmin), knot-cell Taylor polynomials (sigma = t - ta),
    outer exp-poly terms (sigma = t - t0)."""
    TK = TrialK(T); G0 = TrialGreen(TK)                       # init only (no Green build): pc from the spline of a_m
    pc = G0.pc; pcK = -2.0 * pc; pcK[:, :-1, :] -= pc[:, 1:, :] * np.arange(1, pc.shape[1])[None, :, None]
    tb = G0.tb; out = []
    inner = TK.inner_terms(); outer = TK.outer_terms()
    for m in range(Mparts):
        pcs = [(-np.inf, float(T.tmin), float(al), np.array(c[:, m], float)) for (al, c) in inner]
        pcs += [(float(tb[ci]), float(tb[ci + 1]), 0.0, pcK[ci, :, m].copy()) for ci in range(len(tb) - 1)]
        pcs += [(float(T.t0), np.inf, float(al), np.array(c[:, m], float)) for (al, c) in outer]
        out.append(pcs)
    return out, tb


def extended_cols(meta, Mh, free, v=None):
    """Columns of the section: the F- function columns, then KP and TAU (multi-mode columns with angular coefficient vectors A0, Bm from the saved
    _vec.npz), then (free) the Mh pure tails x^2 y chi e^{(k-3)(t-t0)} cos 2m theta (radial pieces = the TAU pieces). Each entry: (m or None, pieces,
    label, angular coefficient vector or None)."""
    cols = [(int(m), p, lab, None) for (m, p, lab) in meta["cols"]]
    if v is not None:
        cols += [(None, meta["kp_pieces"], "KP", np.asarray(v["A0"], float)), (None, meta["tau_pieces"], "TAU", np.asarray(v["Bm"], float))]
    if free: cols += [(m, meta["tau_pieces"], "tail%d" % m, None) for m in range(Mh)]
    return cols


def main_A(trial, pkl, vecnpz, NJ, thresh, out, free=False, K2_modal_json=None):
    t0 = time.time()
    T = Trial(np.load(trial)); meta = pickle.load(_popen(pkl)); v = np.load(vecnpz, allow_pickle=True)
    Mh = int(v["Mh"]); k = float(v["k"]); L = float(v["L"]); tmin = float(v["tmin"]); t00 = float(v["t0"])
    assert abs(tmin - T.tmin) < 1e-12 and abs(t00 - T.t0) < 1e-12 and abs(k - T.k) < 1e-15 and abs(L - T.L) < 1e-12, "trial does not match the section archive"
    nfun = len(meta["cols"]); cols = extended_cols(meta, Mh, free, v); nF = len(cols); nfix = nfun + 2        # function columns + KP + TAU = the F- set of c2_gram2
    G_diag_saved = v["G_diag"][:nfix]
    Mt = T.M; Mang = Mt + 3                                                      # K has modes m < Mt; Phi_m couples to |m - m'| <= 3 (astra/kproj1)
    A0h, A1h = angular_matrices_H1(Mang)
    def acoef_of(col):
        m, pieces, lab, avec = col; a = np.zeros(Mang)
        if avec is None: a[m] = 1.0
        else: a[:len(avec)] = avec
        return a
    for c in cols:
        if c[3] is not None: assert len(c[3]) <= Mang and not np.any(np.asarray(c[3])[Mt:]), "%s has angular coefficients beyond the trial's modes" % c[2]
    AcC = np.array([acoef_of(c) for c in cols]); AcK = np.eye(Mang)[:Mt]          # K parts: one unit vector per mode m < Mt
    # ---- coarse Gram of the columns (c2_gram2's breakpoints and rule: every finite piece endpoint, exterior half-lines subdivided; ng = 24)
    ends = set(np.linspace(tmin - 25.0, tmin, 51).tolist() + np.linspace(t00, t00 + 45.0, 91).tolist())
    for (m, pieces, lab, av) in cols:
        for (a, b, al, c) in pieces:
            if np.isfinite(a): ends.add(float(a))
            if np.isfinite(b): ends.add(float(b))
    bps = np.array(sorted(ends))
    def wX_of(tq, wq):
        uq = np.exp(tq) / L; return wq * L ** 6 * np.exp(2 * tq) * (1 + uq ** 2) ** (3 - k - GAMMA_H1)
    def gram_FF(FA, FdA, AcA, FB, FdB, AcB, tq, wq):
        """H1m inner products between function lists given by radial values/derivatives (n, nt) and angular coefficient matrices (n, Mang)."""
        wX = wX_of(tq, wq); FsA = 3 * FA + FdA; FsB = 3 * FB + FdB
        R0 = (FA * wX[None, :]) @ FB.T; R1 = (FsA * wX[None, :]) @ FsB.T
        return (AcA @ A0h @ AcB.T) * (R0 + R1) + (AcA @ A1h @ AcB.T) * R0
    def col_vals(tq):
        F = np.array([ExpPolyBasis(p).eval(tq) for (m, p, lab, av) in cols]); Fd = np.array([ExpPolyBasis(p).eval(tq, 1) for (m, p, lab, av) in cols]); return F, Fd
    TK = TrialK(T)
    def K_vals(tq):
        return TK.eval(tq, 0).T, TK.eval(tq, 1).T                                  # (Mt, nt): a~_m and a~_m' for ALL modes (vectorized spline / exp-poly evaluation)
    tq, wq = radial_nodes(bps, 24); Fc, Fdc = col_vals(tq)
    Gcc = gram_FF(Fc, Fdc, AcC, Fc, Fdc, AcC, tq, wq)
    diag_err = float(np.abs(np.diag(Gcc)[:nfix] - G_diag_saved).max() / np.abs(G_diag_saved).max())
    diag_err_cw = float(np.max(np.abs(np.diag(Gcc)[:nfix] - G_diag_saved) / np.abs(G_diag_saved)))
    tq48, wq48 = radial_nodes(bps, 48); Fc48, Fdc48 = col_vals(tq48); Gcc48 = gram_FF(Fc48, Fdc48, AcC, Fc48, Fdc48, AcC, tq48, wq48)
    print("column Gram %d x %d rebuilt at %d nodes (%d function columns + KP + TAU%s): deviation of the diagonal from the saved G_diag %.2e (relative to the max), %.2e (componentwise max); 24 vs 48 nodes %.2e (%.0fs)" % (
        nF, nF, len(tq), nfun, " + %d tails" % Mh if free else "", diag_err, diag_err_cw, float(np.linalg.norm(Gcc - Gcc48) / np.linalg.norm(Gcc)), time.time() - t0), flush=True)
    # ---- K: cross block and self norm on the fine nodes (the trial's knots added to the breakpoints), ng = 8 and 16
    ends2 = set(bps.tolist()) | set(float(x) for x in TrialGreen(TK).tb); bps2 = np.array(sorted(ends2))
    def cross(ng):
        tq2, wq2 = radial_nodes(bps2, ng); FK, FdK = K_vals(tq2); Fc2, Fdc2 = col_vals(tq2)
        return gram_FF(FK, FdK, AcK, Fc2, Fdc2, AcC, tq2, wq2).sum(0), float(gram_FF(FK, FdK, AcK, FK, FdK, AcK, tq2, wq2).sum()), len(tq2)
    g, K2_gram, nq2 = cross(8); g16, K2_gram16, _ = cross(16)
    cross_err = float(np.abs(g - g16).max() / np.abs(g).max()); cross_err_cw = float(np.max(np.abs(g - g16) / np.maximum(np.abs(g16), 1e-300)))
    K2_modal = json.load(open(K2_modal_json))["norm2"]["K = rho~ - X.grad rho~"]["all"] if K2_modal_json else None
    print("cross block <K, col_i> at %d fine nodes, all %d modes of K (8 vs 16 Gauss nodes per cell: %.2e relative to the max, %.2e componentwise); ||K||_X^2 on the Gram range = %.8e (16 nodes %.8e)%s (%.0fs)" % (
        nq2, Mt, cross_err, cross_err_cw, K2_gram, K2_gram16, "; modal value on 1e-4 <= r <= 1e7: %.8e" % K2_modal if K2_modal else "", time.time() - t0), flush=True)
    # ---- projection onto the constrained span (c2_gram2 recipe; constraints on the function columns only)
    dg = np.sqrt(np.maximum(np.diag(Gcc), 1e-300)); D = 1.0 / dg; G1 = Gcc * D[:, None] * D[None, :]
    rows = []
    for m in range(Mh):
        for join in (tmin, t00):
            for nu in range(NJ + 1):
                row = np.zeros(nF)
                for gi in range(nfun):
                    if cols[gi][0] == m:
                        row[gi] = (piece_jet(cols[gi][1], join, "-", nu) - piece_jet(cols[gi][1], join, "+", nu)) * D[gi]
                if np.any(row): rows.append(row)
    C = np.array(rows) if rows else np.zeros((0, nF))
    if C.shape[0]:
        Cn = C / np.linalg.norm(C, axis=1)[:, None]; Uc, Sc, Vct = np.linalg.svd(Cn, full_matrices=True); rank = int((Sc > 1e-10 * Sc[0]).sum()); N = Vct[rank:].T
    else: rank = 0; N = np.eye(nF)
    GN = N.T @ G1 @ N; lam, V = np.linalg.eigh(GN); lam = lam[::-1]; V = V[:, ::-1]
    results = {}
    for th_name, th in (("thresh", thresh), ("1e-12", 1e-12), ("1e-15", 1e-15)):
        keep = lam > th * lam[0]
        QN = V[:, keep] / np.sqrt(lam[keep])[None, :]; Q = (N @ QN) * D[:, None]            # X-orthonormal basis of the retained constrained span, original coordinates
        y = Q.T @ g; x = Q @ y; PK2 = float(y @ y)
        whit = float(np.abs(np.linalg.eigvalsh(Q.T @ Gcc48 @ Q) - 1).max()) if th_name == "thresh" else None       # whitening error against the refined Gram
        join_res = float(np.abs(Cn @ (N @ QN)).max()) if C.shape[0] else 0.0
        resid2 = K2_gram - PK2                                                                 # ||K - P K||_X^2 if the projection were exact in one inner product
        resid2_direct = float(K2_gram16 - 2 * x @ g16 + x @ Gcc48 @ x)                          # direct ||K - sum x_i col_i||^2 on the refined rules (astra/kproj2): consistency check, not clipping
        assert resid2 > 0, "negative residual: inconsistent quadratures"
        results[th_name] = dict(n_kept=int(keep.sum()), PK_norm2=PK2, cos2=PK2 / K2_gram, dist_rel=float(np.sqrt(resid2 / K2_gram)), dist_rel_direct=float(np.sqrt(max(resid2_direct, 0.0) / K2_gram16)),
                                x=x, y=y, whitening_error=whit, join_residual=join_res)
        print("  eigen-cut %s: kept %d of %d constrained directions (join residual %.1e%s); ||P K||_X^2 = %.8e; cos^2(K, retained span) = %.6f; ||K - P K||_X / ||K||_X = %.6f (direct evaluation on the refined rules %.6f)" % (
            th_name, keep.sum(), N.shape[1], join_res, (", whitening error vs the 48-node Gram %.1e" % whit) if whit is not None else "", PK2, PK2 / K2_gram, results[th_name]["dist_rel"], results[th_name]["dist_rel_direct"]), flush=True)
    r = results["thresh"]
    np.savez(out, x=r["x"], y=r["y"], g=g, lam=lam, nF=nF, nfun=nfun, free=free, Mh=Mh, NJ=NJ, thresh=thresh, n_kept=r["n_kept"], PK_norm2=r["PK_norm2"], K2_gram=K2_gram,
             K2_full=K2_gram, K2_modal=(K2_modal if K2_modal else np.nan), cos2_full=r["cos2"], dist_rel=r["dist_rel"], whitening_error=r["whitening_error"], join_residual=r["join_residual"],
             diag_err=diag_err, diag_err_cw=diag_err_cw, cross_err=cross_err, cross_err_cw=cross_err_cw, col_m=np.array([(-1 if c[0] is None else c[0]) for c in cols]),
             col_label=np.array([c[2] for c in cols]), summary=json.dumps({k2: {kk: vv for kk, vv in v2.items() if not isinstance(vv, np.ndarray)} for k2, v2 in results.items()}))
    print("saved", out, "(%.0fs)" % (time.time() - t0))


def combined_bases(cols, x, Mh):
    """P K = sum_i x_i col_i as one ExpPolyBasis per mode m < Mh: pieces with identical (a, b, alpha) are summed (coefficient arrays padded)."""
    out = []
    for m in range(Mh):
        acc = {}
        for (cm, pieces, lab, av), xi in zip(cols, x):
            if cm is None or int(cm) != m or xi == 0.0: continue
            for (a, b, al, c) in pieces:
                key = (float(a), float(b), float(al)); c = np.asarray(c, float) * xi
                if key in acc:
                    old = acc[key]; n = max(len(old), len(c)); new = np.zeros(n); new[:len(old)] += old; new[:len(c)] += c; acc[key] = new
                else: acc[key] = c
        out.append(ExpPolyBasis([(a, b, al, c) for (a, b, al), c in acc.items()]))
    return out


def row_functionals(img, t_eval, w_i, Mout):
    """img: (Ne, Mout) unweighted image modes (Lh)_N(t_i). Returns the four functionals of c2_gram2.weighted_rows (L2, L2q, H1, H1q) as norms."""
    Ne = len(t_eval); out = {}
    dtv = np.diff(t_eval); om = np.zeros(Ne); om[:-1] += 0.5 * dtv; om[1:] += 0.5 * dtv
    ang = np.sqrt(1.0 + (2 * np.arange(Mout) + 1.0) ** 2); wm = 0.5 * (w_i[1:] + w_i[:-1])
    for name in ("L2", "L2q", "H1", "H1q"):
        quad = name.endswith("q"); sq_om = np.sqrt(om) if quad else np.ones(Ne); sq_dt = np.sqrt(dtv) if quad else np.ones(Ne - 1)
        val = img * (w_i * sq_om)[:, None]
        if name.startswith("L2"): out[name] = float(np.sqrt((val ** 2).sum())); continue
        val = val * ang[None, :]
        der = (img[1:] - img[:-1]) * (wm * sq_dt / dtv)[:, None]
        out[name] = float(np.sqrt((val ** 2).sum() + (der ** 2).sum()))
    return out


def main_B(trial, pkl, vecnpz, projnpz, out):
    """Stage B: image of P K under L by the fast assembler (one combined column per mode), the direct image of K (L K = eps~ - X.grad eps~ by the
    analytic jets; floating identity for the exactly normalized trial), the four row functionals of both, and the quotients against ||P K||_X, ||K||_X."""
    from lin_fast import FastAssembler
    from trial_jets import TrialJets
    from xnorm_jets import eps_mode_jets
    t0 = time.time()
    T = Trial(np.load(trial)); meta = pickle.load(_popen(pkl)); v = np.load(vecnpz, allow_pickle=True); P = np.load(projnpz, allow_pickle=True)
    Mh = int(v["Mh"]); Mout = int(v["Mout"]); t_eval = v["t_eval"]; w_i = v["w_i"]; Ne = len(t_eval)
    free = bool(P["free"]) if "free" in P.files else False; cols = extended_cols(meta, Mh, free, v)
    x = P["x"]; PK2 = float(P["PK_norm2"]); K2 = float(P["K2_full"]); assert len(x) == len(cols), (len(x), len(cols))
    KT = np.load(os.environ.get("KPROJ_KT", "runs/kproj/KT_images.npz"))                  # row images of KP and TAU (stage KT, same grid)
    assert np.array_equal(KT["t_eval"], t_eval) and int(KT["Mout"]) == Mout, "KP/TAU images are on a different grid"
    assert "M" in KT.files and "m_lo" not in KT.files and int(KT["M"]) == T.M, "KT images must be the merged complete archive (all modes 0..M) of this trial"      # astra/kproj2
    for lab in ("KP", "TAU"):
        av = [c[3] for c in cols if c[2] == lab][0]; assert not np.any(av[T.M:]), "%s has angular coefficients beyond the trial's modes" % lab
    G = TrialGreen(T); G.build(); print("Green build %.0fs" % (time.time() - t0), flush=True)
    asm = FastAssembler(G, t_eval, Mout)
    bases = combined_bases(cols, x, Mh)
    img = np.zeros((Ne, Mout)); csum = 0.0
    for m, basis in enumerate(bases):
        o, ch = asm.column(m, basis); img += o; csum += ch
    labels = [c[2] for c in cols]; iKP = labels.index("KP"); iTAU = labels.index("TAU")
    img += x[iKP] * KT["img_KP"] + x[iTAU] * KT["img_TAU"]; csum += x[iKP] * float(KT["c_KP"]) + x[iTAU] * float(KT["c_TAU"])
    print("assembled L(P K) on %d combined columns + KP, TAU (coefficients %.3e, %.3e) (%d rows x %d modes): c[P K] = %.3e (%.0fs)" % (Mh, x[iKP], x[iTAU], Ne, Mout, csum, time.time() - t0), flush=True)
    # direct image of K: (eps~ - d_t eps~)_N at the collocation radii, N < Mout
    mj = TrialJets(G, K=1).modal_jets(t_eval); E = eps_mode_jets(G, mj, 1); imgK = (E[0] - E[1])[:, :Mout]
    fK = row_functionals(imgK, t_eval, w_i, Mout); fP = row_functionals(img, t_eval, w_i, Mout); fD = row_functionals(img - imgK, t_eval, w_i, Mout)
    res = dict(trial=trial, section=pkl, vec=vecnpz, proj=projnpz, span=("free (F- + %d pure tails)" % Mh if free else "F-"), Mh=Mh, Mout=Mout, Ne=Ne, NJ=int(P["NJ"]), thresh=float(P["thresh"]), n_kept=int(P["n_kept"]),
               PK_norm=float(np.sqrt(PK2)), K_norm=float(np.sqrt(K2)), cos2=float(P["cos2_full"]), dist_rel=(float(P["dist_rel"]) if "dist_rel" in P.files else None), c_PK=csum,
               functionals_LPK=fP, functionals_LK_direct=fK, functionals_difference=fD,
               quotients_PK={k2: v2 / np.sqrt(PK2) for k2, v2 in fP.items()}, quotients_K={k2: v2 / np.sqrt(K2) for k2, v2 in fK.items()},
               note="quotients = row functional of the image / X norm of the vector; compare with the sections' smallest singular values (same rows, same X norm); the direct image of K uses the floating identity L K = eps~ - X.grad eps~ (exactly normalized trial, ver topic 138) evaluated by the analytic jets; the difference row measures the image of K - P K (unrepresented part) plus the identity's defect")
    print("row functionals of L(P K): %s" % {k2: "%.4e" % v2 for k2, v2 in fP.items()})
    print("row functionals of L K (direct, eps~ - X.grad eps~): %s" % {k2: "%.4e" % v2 for k2, v2 in fK.items()})
    print("row functionals of the difference L(P K) - L K: %s" % {k2: "%.4e" % v2 for k2, v2 in fD.items()})
    print("quotients of P K (functional / ||P K||_X = %.4e): %s" % (np.sqrt(PK2), {k2: "%.4e" % v2 for k2, v2 in res["quotients_PK"].items()}))
    print("quotients of K   (functional / ||K||_X   = %.4e): %s" % (np.sqrt(K2), {k2: "%.4e" % v2 for k2, v2 in res["quotients_K"].items()}))
    # where along r is the image concentrated: H1q value-row density per collocation radius (quadrature weights omega_i included)
    dtv = np.diff(t_eval); om = np.zeros(Ne); om[:-1] += 0.5 * dtv; om[1:] += 0.5 * dtv; ang2 = (1.0 + (2 * np.arange(Mout) + 1.0) ** 2)[None, :]; r_eval = np.exp(t_eval)
    def quant(im):
        val2 = ((im * w_i[:, None]) ** 2 * ang2).sum(1) * om; cum = np.cumsum(val2) / val2.sum()
        return {q: float(r_eval[np.searchsorted(cum, q)]) for q in (0.1, 0.5, 0.9)}
    res["H1q_value_part_radius_quantiles_of_LPK"] = quant(img); res["H1q_value_part_radius_quantiles_of_LK"] = quant(imgK)
    print("radius quantiles (10/50/90 percent) of the H1q value-row energy: L(P K) %s ; L K %s" % (res["H1q_value_part_radius_quantiles_of_LPK"], res["H1q_value_part_radius_quantiles_of_LK"]))
    res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1); np.savez(out.replace(".json", "_img.npz"), img_PK=img, img_K=imgK, t_eval=t_eval, w_i=w_i)
    print("saved", out, "(%.0fs)" % res["time"])


if __name__ == "__main__" and sys.argv[1] == "B":
    a = sys.argv[1:]; main_B(a[1], a[2], a[3], a[4], a[5])


def main_C(trial, vecnpz, m_lo, m_hi, out):
    """Stage C: L applied to K itself through the fast assembler (K's own fine-knot pieces, one single-mode column per mode m in [m_lo, m_hi)); saves the
    partial row image (Ne, Mout) so that pieces over m can be summed and compared with the direct image eps~ - X.grad eps~ (identity of ver topic 138)."""
    from lin_fast import FastAssembler
    t0 = time.time()
    T = Trial(np.load(trial)); v = np.load(vecnpz, allow_pickle=True); Mout = int(v["Mout"]); t_eval = v["t_eval"]; Ne = len(t_eval)
    assert 0 <= m_lo < m_hi <= T.M, "mode range must satisfy 0 <= m_lo < m_hi <= M = %d" % T.M
    G = TrialGreen(T); G.build(); asm = FastAssembler(G, t_eval, Mout); print("build %.0fs" % (time.time() - t0), flush=True)
    Kp, tb = K_pieces(T, m_hi)
    img = np.zeros((Ne, Mout)); csum = 0.0
    for m in range(m_lo, m_hi):
        o, ch = asm.column(m, ExpPolyBasis(Kp[m])); img += o; csum += ch
        if (m - m_lo + 1) % 8 == 0: print("  mode %d (%.0fs)" % (m, time.time() - t0), flush=True)
    import hashlib
    np.savez(out, img=img, c=csum, m_lo=m_lo, m_hi=m_hi, t_eval=t_eval, w_i=v["w_i"], Mout=Mout, trial=trial, trial_sha256=hashlib.sha256(open(trial, "rb").read()).hexdigest(), M=T.M)
    print("saved", out, "modes [%d, %d) c = %.3e (%.0fs)" % (m_lo, m_hi, csum, time.time() - t0))


def main_Cmerge(projB_img, pieces, out, M_total=260):
    """Sum the stage C pieces. Checks: identical collocation grid (t_eval, w_i) and Mout in every piece and in the stage B file; mode ranges disjoint,
    contiguous and covering [0, M_total) (duplicates or gaps are rejected)."""
    d0 = np.load(projB_img); imgK_direct = d0["img_K"]; t_eval = d0["t_eval"]; w_i = d0["w_i"]
    img = 0.0; c = 0.0; ms = []
    shas = set()
    for p in pieces:
        d = np.load(p)
        assert d["img"].shape == imgK_direct.shape and int(d["Mout"]) == imgK_direct.shape[1], "piece %s has a different image shape / Mout" % p
        assert np.array_equal(d["t_eval"], t_eval) and np.array_equal(d["w_i"], w_i), "piece %s has a different collocation grid" % p
        if "trial_sha256" in d.files: shas.add(str(d["trial_sha256"]))
        lo_, hi_ = int(d["m_lo"]), int(d["m_hi"]); assert 0 <= lo_ < hi_, "piece %s has an empty or inverted mode range" % p
        img = img + d["img"]; c += float(d["c"]); ms.append((lo_, hi_))
    assert len(shas) <= 1, "pieces come from different trials: %s" % shas                   # pieces written before 21:2xZ carry no identity (same trial by construction)
    ms.sort(); assert ms[0][0] == 0 and ms[-1][1] == M_total and all(ms[i][1] == ms[i + 1][0] for i in range(len(ms) - 1)), "mode ranges must tile [0, %d): %s" % (M_total, ms)
    Mout = img.shape[1]
    fA = row_functionals(img, t_eval, w_i, Mout); fD = row_functionals(imgK_direct, t_eval, w_i, Mout); fdiff = row_functionals(img - imgK_direct, t_eval, w_i, Mout)
    res = dict(modes=ms, c_K_assembled=c, functionals_LK_assembled=fA, functionals_LK_direct=fD, functionals_difference=fdiff,
               rel_difference={k2: fdiff[k2] / fD[k2] for k2 in fD}, max_abs_img_diff=float(np.abs(img - imgK_direct).max()), max_abs_img=float(np.abs(imgK_direct).max()))
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)


def main_KT(trial, pkl, vecnpz, out, m_lo=0, m_hi=None):
    """Row images of the KP and TAU columns (multi-mode: angular vectors A0, Bm over all modes) through the section's assembler, for stage B;
    modes m in [m_lo, m_hi) (pieces are summed by `KTmerge out piece1 piece2 ...`)."""
    from lin_fast import FastAssembler
    t0 = time.time()
    T = Trial(np.load(trial)); meta = pickle.load(_popen(pkl)); v = np.load(vecnpz, allow_pickle=True); Mout = int(v["Mout"]); t_eval = v["t_eval"]; Ne = len(t_eval)
    m_hi = T.M if m_hi is None else m_hi; assert 0 <= m_lo < m_hi <= T.M
    G = TrialGreen(T); G.build(); asm = FastAssembler(G, t_eval, Mout)
    A0 = np.asarray(v["A0"], float); Bm = np.asarray(v["Bm"], float)
    imgKP = np.zeros((Ne, Mout)); imgTAU = np.zeros((Ne, Mout)); cKP = 0.0; cTAU = 0.0
    bKP = ExpPolyBasis(meta["kp_pieces"]); bTAU = ExpPolyBasis(meta["tau_pieces"])
    for m in range(m_lo, m_hi):
        if A0[m] != 0.0:
            o, ch = asm.column(m, bKP); imgKP += A0[m] * o; cKP += A0[m] * ch
        if m < len(Bm) and Bm[m] != 0.0:
            o, ch = asm.column(m, bTAU); imgTAU += Bm[m] * o; cTAU += Bm[m] * ch
        if (m + 1) % 50 == 0: print("  mode %d (%.0fs)" % (m, time.time() - t0), flush=True)
    np.savez(out, img_KP=imgKP, img_TAU=imgTAU, c_KP=cKP, c_TAU=cTAU, t_eval=t_eval, Mout=Mout, m_lo=m_lo, m_hi=m_hi, M=T.M)
    print("saved", out, "modes [%d, %d) c_KP = %.6e c_TAU = %.6e (%.0fs)" % (m_lo, m_hi, cKP, cTAU, time.time() - t0))


def main_KTmerge(out, pieces):
    ds = [np.load(p) for p in pieces]; ms = sorted((int(d["m_lo"]), int(d["m_hi"])) for d in ds); M = int(ds[0]["M"])
    assert ms[0][0] == 0 and ms[-1][1] == M and all(ms[i][1] == ms[i + 1][0] for i in range(len(ms) - 1)), "KT pieces must tile [0, M): %s" % ms
    for d in ds[1:]: assert np.array_equal(d["t_eval"], ds[0]["t_eval"]) and int(d["Mout"]) == int(ds[0]["Mout"]) and int(d["M"]) == M, "KT pieces disagree in grid / Mout / M"
    np.savez(out, img_KP=sum(d["img_KP"] for d in ds), img_TAU=sum(d["img_TAU"] for d in ds), c_KP=sum(float(d["c_KP"]) for d in ds), c_TAU=sum(float(d["c_TAU"]) for d in ds),
             t_eval=ds[0]["t_eval"], Mout=int(ds[0]["Mout"]), M=M)
    print("saved", out, "from", ms)


if __name__ == "__main__" and sys.argv[1] == "KT":
    a = sys.argv[1:]; main_KT(a[1], a[2], a[3], a[4], int(a[5]) if len(a) > 5 else 0, int(a[6]) if len(a) > 6 else None)
if __name__ == "__main__" and sys.argv[1] == "KTmerge":
    a = sys.argv[1:]; main_KTmerge(a[1], a[2:])
if __name__ == "__main__" and sys.argv[1] == "C":
    a = sys.argv[1:]; main_C(a[1], a[2], int(a[3]), int(a[4]), a[5])
if __name__ == "__main__" and sys.argv[1] == "Cmerge":
    a = sys.argv[1:]; main_Cmerge(a[1], a[2:-1], a[-1], M_total=int(os.environ.get("KPROJ_MTOTAL", "260")))
if __name__ == "__main__" and sys.argv[1] == "A":
    a = sys.argv[1:]; main_A(a[1], a[2], a[3], int(a[4]), float(a[5]), a[6], free=(len(a) > 7 and a[7] == "free"), K2_modal_json=os.environ.get("KPROJ_K2_JSON"))
