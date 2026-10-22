"""C2 with a well-conditioned, conforming column basis (lead 02:04Z; floating point, evidence only).  Version 2 after the astra review
(notes/astra_c2gram1_answer.md): quadrature breakpoints at every finite piece endpoint (the cutoff's fine knots included) with a refined-rule
check; column equilibration to unit X-norm before any eigen-cut; join-matching constraints at tmin and t0 (C^0 by default, optionally C^1)
imposed before whitening, so that only conforming combinations enter (the piecewise assembler omits the delta contributions of jumps; a
continuous combination has none); stable projections (pseudo-inverse, explicit h^T G h) onto reference spans: the section's J column
(x^2 y on r < R0), the inner scaling direction J_inner = x^2 y 1_{t < tmin} (a reference function outside the section), the free tails, KP/TAU,
the column kinds and the modes; principal angles between the near-null subspace and the tail span; the ell(Phi) least squares with its
conventions stated.
Input: the raw section saved by src/c2_fminus.py (save_raw.npz + _cols.pkl).  Column functions h_c = x^2 y f_c(t) a_c(theta),
a_c = sum_m a_{c,m} cos 2m theta.  DEFAULT inner product (MODE H1m): <h, g>_X = int (h g + r^2 grad h . grad g) m(r)^{-2} (1 + r^2/L^2)^{-3/2} dX
with m(r) = u^3 (1+u^2)^{(k-3)/2} the background scale (so h/m is the centre factor near 0 and an angular profile at infinity; this is the
same relative normalization as the rows, whose weight is (1+u)^{1/2}/m); without the 1/m^2 the first splines near rmin have X-norm 1e-8 and
image norm 1e5 (ratio 1e13) and the spectrum only reflects the mismatch.  Separable: h = r^3 b_m(t) Phi_m(theta), Phi_m = cos^2 sin cos 2m theta,
r^2 |grad h|^2 = (d_t h)^2 + (d_theta h)^2 = e^{6t}[(3b + b')^2 Phi^2 + b^2 Phi'^2], dX = e^{2t} dt dtheta, with the exact angular matrices
A0 = int Phi_m Phi_m', A1 = int Phi_m' Phi_m''.  Option MODE L2y: <h, g>_X = int h g |y|^{-2} (1 + r^2/L^2)^{-gamma'} dX, gamma' = 1129/1000; since
h/y = r^2 cos^2 theta sum_m b_m cos 2m theta and dX = r dr dtheta: <h_c, h_d>_X = (a_c^T Aang a_d) int f_c f_d e^{6t} (1 + e^{2t}/L^2)^{-gamma'} dt,
Aang_{mm'} = int_0^{2pi} cos^4 theta cos 2m theta cos 2m' theta dtheta = (I(2m-2m') + I(2m+2m'))/2, I(0) = 3pi/4, I(+-2) = pi/2, I(+-4) = pi/8, else 0.
Rows: residual modes N < Mout at the collocation radii of the assembly, weight (1+u)^{1/2}/m(r); target norm sum_{i,N} |roww_i (Lh)_N(t_i)|^2.
Usage: python3 src/c2_gram.py save_raw.npz out.json [thresh=1e-10] [NJ=0] [MODE=H1m|H1|L2y]
"""
import os, sys, json, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from numpy.polynomial.legendre import leggauss
from lin_assembly import ExpPolyBasis
GAMMA_P = 1129.0 / 1000.0          # far exponent of the L2 face-weighted inner product ('L2y')
GAMMA_H1 = 1.5                     # far exponent of the H1-type inner product ('H1'); h ~ r^k needs gamma > k + 1 = 1.18 for convergence


def piece_jet(pieces, t, side, nu):
    """One-sided value of d^nu/dt^nu of the exponential-polynomial at the exact point t (side '-' : the piece ending at t; '+': the piece starting at t)."""
    for (a, b, alpha, c) in pieces:
        if side == "-" and b == t: sig = 0.0 if np.isinf(a) else (t - a)
        elif side == "+" and a == t: sig = 0.0
        else: continue
        cc = np.array(c, float)
        for _ in range(nu):
            dc = alpha * cc
            if len(cc) > 1: dc[:-1] += cc[1:] * np.arange(1, len(cc))
            cc = dc
        return float(np.exp(alpha * sig) * np.polyval(cc[::-1], sig))
    return 0.0


def radial_nodes(bps, ng):
    x, w = leggauss(ng); nodes = []; weights = []
    for a, b in zip(bps[:-1], bps[1:]):
        if b <= a: continue
        nodes.append(0.5 * (b - a) * x + 0.5 * (a + b)); weights.append(0.5 * (b - a) * w)
    return np.concatenate(nodes), np.concatenate(weights)


def angular_matrix(Mmax):
    """Aang_{mm'} = int_0^{2pi} cos^4 theta cos 2m theta cos 2m' theta dtheta (exact)."""
    I = {0: 3 * np.pi / 4, 2: np.pi / 2, -2: np.pi / 2, 4: np.pi / 8, -4: np.pi / 8}
    A = np.zeros((Mmax, Mmax))
    for m in range(Mmax):
        for mp in range(Mmax):
            A[m, mp] = 0.5 * (I.get(2 * m - 2 * mp, 0.0) + I.get(2 * m + 2 * mp, 0.0))
    return A


def angular_matrices_H1(Mmax, N=16384):
    """A0_{mm'} = int Phi_m Phi_m' dtheta, A1_{mm'} = int Phi_m' Phi_m'' dtheta (derivatives in theta), Phi_m = cos^2 sin cos 2m theta, over [0, 2pi);
    equispaced quadrature exact for trigonometric degree < N (max degree 6 + 4 Mmax)."""
    th = 2 * np.pi * np.arange(N) / N; w = 2 * np.pi / N
    base = np.cos(th) ** 2 * np.sin(th); dbase = -2 * np.cos(th) * np.sin(th) ** 2 + np.cos(th) ** 3
    mm = np.arange(Mmax)[:, None]
    Phi = base[None, :] * np.cos(2 * mm * th[None, :]); dPhi = dbase[None, :] * np.cos(2 * mm * th[None, :]) - 2 * mm * base[None, :] * np.sin(2 * mm * th[None, :])
    return (Phi * w) @ Phi.T, (dPhi * w) @ dPhi.T


def cos2_span(G, h, idxs, hGh=None):
    """cos^2 of the X-angle between h (coefficient vector in the extended basis) and span{basis vectors idxs}: p^T K^+ p / h^T G h."""
    if not idxs: return float("nan")
    idxs = list(idxs); K = G[np.ix_(idxs, idxs)]; p = G[idxs, :] @ h
    hGh = float(h @ G @ h) if hGh is None else hGh
    Kp = np.linalg.pinv(K, rcond=1e-12, hermitian=True)
    return float(p @ Kp @ p / hGh)


def main(raw, out, thresh=1e-10, NJ=0, MODE="H1m"):
    t0 = time.time()
    d = np.load(raw); meta = pickle.load(open(raw.replace(".npz", "_cols.pkl"), "rb"))
    Mat, KP, TAU, tails = d["Mat"], d["KP"], d["TAU"], d["tails"]
    t_eval = d["t_eval"]; k = float(d["k"]); L = float(d["L"]); Mout = int(d["Mout"]); Mh = int(d["Mh"]); tmin = float(d["tmin"]); t00 = float(d["t0"])
    uu = np.exp(t_eval) / L; mr = uu ** 3 * (1 + uu ** 2) ** ((k - 3) / 2); roww = np.repeat((1 + uu) ** 0.5 / mr, Mout)
    col_m = d["col_m"]; col_kind = d["col_kind"]; col_label = d["col_label"]; A0 = d["A0"]; Bm = d["Bm"]
    cols = meta["cols"]; kp_pieces = meta["kp_pieces"]; tau_pieces = meta["tau_pieces"]
    nF = len(cols); Mt = len(A0); ntot = nF + 2 + Mh; next_ = ntot + 1          # extended basis: + J_inner reference
    assert Mh >= 4
    # ---- column functions: (radial pieces, angular coefficient vector over modes < Mang)
    Mang = Mt + 2; Aang = angular_matrix(Mang)
    def avec(pairs):
        a = np.zeros(Mang)
        for m, c in pairs: a[m] += c
        return a
    rad_pieces = [pieces for (m, pieces, lab) in cols] + [kp_pieces, tau_pieces, [(-np.inf, tmin, 0.0, [1.0])]]      # last: J_inner radial
    rad_of = list(range(nF)) + [nF, nF + 1] + [nF + 1] * Mh + [nF + 2]
    acoef = [avec([(int(m), 1.0)]) for (m, pieces, lab) in cols] + [avec([(m, A0[m]) for m in range(Mt)]), avec([(m, Bm[m]) for m in range(min(Mt, len(Bm)))])] \
        + [avec([(m, 1.0)]) for m in range(Mh)] + [avec([(0, 1.0)])]
    Acoef = np.array(acoef); AA = Acoef @ Aang @ Acoef.T
    # ---- radial quadrature with every finite piece endpoint as a breakpoint; refined rule for a check
    ends = set(np.linspace(tmin - 25.0, tmin, 51).tolist() + np.linspace(t00, t00 + 45.0, 91).tolist())      # half-lines subdivided (decay scales)
    for pieces in rad_pieces:
        for (a, b, al, c) in pieces:
            if np.isfinite(a): ends.add(float(a))
            if np.isfinite(b): ends.add(float(b))
    bps = np.array(sorted(ends))
    A0h, A1h = angular_matrices_H1(Mang); AA0 = Acoef @ A0h @ Acoef.T; AA1 = Acoef @ A1h @ Acoef.T
    def gram(ng):
        tq, wq = radial_nodes(bps, ng)
        F = np.array([ExpPolyBasis(pc).eval(tq) for pc in rad_pieces]); Fd = np.array([ExpPolyBasis(pc).eval(tq, 1) for pc in rad_pieces])
        if MODE == "L2y":
            wX = wq * np.exp(6 * tq) * (1 + np.exp(2 * tq) / L ** 2) ** (-GAMMA_P)
            R = (F * wX[None, :]) @ F.T
            return AA * R[np.ix_(rad_of, rad_of)], len(tq)
        # H1: h = r^3 b Phi_m; dX = e^{2t} dt dtheta; h^2 -> e^{8t} b^2 Phi^2; r^2|grad h|^2 = (d_t h)^2 + (d_theta h)^2 = e^{6t}[(3b + b')^2 Phi^2 + b^2 Phi'^2]
        # H1m (default): the same divided by m(r)^2 = u^6 (1+u^2)^{k-3} (the background scale that also normalizes the rows): e^{8t}/m^2 = L^6 e^{2t} (1+u^2)^{3-k}
        uq = np.exp(tq) / L
        if MODE == "H1m": wX = wq * L ** 6 * np.exp(2 * tq) * (1 + uq ** 2) ** (3 - k - GAMMA_H1)
        else: wX = wq * np.exp(8 * tq) * (1 + uq ** 2) ** (-GAMMA_H1)
        Fs = 3 * F + Fd
        R0 = (F * wX[None, :]) @ F.T; R1 = (Fs * wX[None, :]) @ Fs.T
        return AA0 * (R0 + R1)[np.ix_(rad_of, rad_of)] + AA1 * R0[np.ix_(rad_of, rad_of)], len(tq)
    G, nq = gram(24); G2, nq2 = gram(48)
    gram_rel_diff = float(np.linalg.norm(G - G2) / np.linalg.norm(G))
    print("extended Gram %d x %d (%d function + KP + TAU + %d tails + J_inner ref); %d/%d radial nodes; 24-vs-48 relative difference %.2e; %.0fs" % (
        next_, next_, nF, Mh, nq, nq2, gram_rel_diff, time.time() - t0), flush=True)
    # ---- equilibration
    dg = np.sqrt(np.maximum(np.diag(G), 1e-300)); D = 1.0 / dg
    # ---- join-matching constraints (function columns only; KP/TAU/tails are C^6 across the joins) in equilibrated coordinates
    def constraints(NJ, sel):
        rows = []
        for m in range(Mh):
            for join in (tmin, t00):
                for nu in range(NJ + 1):
                    row = np.zeros(len(sel))
                    for li, gi in enumerate(sel):
                        if gi < nF and int(col_m[gi]) == m:
                            pcs = cols[gi][1]
                            row[li] = (piece_jet(pcs, join, "-", nu) - piece_jet(pcs, join, "+", nu)) * D[gi]
                    if np.any(row): rows.append(row)
        return np.array(rows) if rows else np.zeros((0, len(sel)))
    Aw_all = np.column_stack([Mat, KP, TAU, tails]) * roww[:, None]
    jidx = [i for i, (m, pieces, lab) in enumerate(cols) if lab == "J"]
    tail_idx = list(range(nF + 2, ntot)); kptau_idx = [nF, nF + 1]; jin_idx = [ntot]
    kinds = {kd: [i for i in range(nF) if col_kind[i] == kd] for kd in ("in", "sp", "out")}
    res = dict(raw=raw, Mh=Mh, stride=int(d["stride"]), Mout=Mout, ppc=int(d["ppc"]), Ne=int(d["Ne"]), nrows=int(Aw_all.shape[0]), thresh=thresh, NJ=NJ,
               inner_product=({"H1m": "int (h g + r^2 grad h . grad g) m(r)^-2 (1+r^2/L^2)^-1.5 dX  (m = u^3 (1+u^2)^((k-3)/2), the background scale)", "H1": "int (h g + r^2 grad h . grad g) (1+r^2/L^2)^-1.5 dX", "L2y": "int h g |y|^-2 (1+r^2/L^2)^-1.129 dX"}[MODE]), mode=MODE, row_weight="(1+u)^0.5/m(r)", gram_rel_diff_24_vs_48=gram_rel_diff, n_radial_nodes=nq,
               Xnorm2={"J_code": float(G[jidx[0], jidx[0]]) if jidx else None, "J_inner": float(G[ntot, ntot]), "KP": float(G[nF, nF]), "TAU": float(G[nF + 1, nF + 1]),
                       "inner_powers_min_max": [float(np.min(dg[kinds["in"]] ** 2)), float(np.max(dg[kinds["in"]] ** 2))] if kinds["in"] else None,
                       "cos2_Jcode_Jinner": cos2_span(G, np.eye(next_)[ntot], jidx) if jidx else None}, sections={})
    for name, sel in [("Fminus", list(range(nF + 2))), ("Fminus_noJ", [i for i in range(nF + 2) if i not in jidx]), ("free", list(range(ntot))), ("free_noJ", [i for i in range(ntot) if i not in jidx])]:
        Gs = G[np.ix_(sel, sel)]; Ds = D[sel]; G1 = Gs * Ds[:, None] * Ds[None, :]          # equilibrated Gram (unit diagonal)
        C = constraints(NJ, sel)
        if C.shape[0]:
            Uc, Sc, Vct = np.linalg.svd(C, full_matrices=True); rank = int((Sc > 1e-10 * Sc[0]).sum()); N = Vct[rank:].T
        else: rank = 0; N = np.eye(len(sel))
        GN = N.T @ G1 @ N; lam, V = np.linalg.eigh(GN); lam = lam[::-1]; V = V[:, ::-1]
        keep = lam > thresh * lam[0]; keep12 = lam > 1e-12 * lam[0]
        QN = V[:, keep] / np.sqrt(lam[keep])[None, :]
        Q = (N @ QN) * Ds[:, None]                                        # original coefficients of the X-orthonormal basis (columns)
        Gs2 = G2[np.ix_(sel, sel)]; W = Q.T @ Gs2 @ Q; whit_err = float(np.abs(np.linalg.eigvalsh(W) - 1).max())
        Aw = Aw_all[:, sel]; B = Aw @ Q
        U_, S_, Vt = np.linalg.svd(B, full_matrices=False)
        nk = Q.shape[1]; nrow = B.shape[0]
        sec = dict(ncol=len(sel), n_constraints=int(C.shape[0]), constraint_rank=rank, nfree=int(N.shape[1]), n_kept=int(nk), n_kept_at_1em12=int(keep12.sum()),
                   gram_cond_after_equilibration=float(lam[0] / lam[keep][-1]), whitening_error_refined_quadrature=whit_err,
                   trivial_null_dimension=int(max(nk - nrow, 0)), sigma_max=float(S_[0]), sigma_small5=[float(x) for x in S_[-5:][::-1]],
                   n_below_1em3=int((S_ < 1e-3 * S_[0]).sum()), n_below_1em6=int((S_ < 1e-6 * S_[0]).sum()))
        # shares of the smallest right singular vectors (coefficients extended to the full basis incl. the J_inner reference)
        def extend(v):
            h = np.zeros(next_); h[sel] = Q @ v; return h
        shares = []
        for i in range(min(5, len(S_))):
            h = extend(Vt[-1 - i]); hGh = float(h @ G @ h)
            shares.append(dict(sigma=float(S_[-1 - i]), hGh=hGh, J_code=cos2_span(G, h, jidx, hGh) if jidx else None, J_inner=cos2_span(G, h, jin_idx, hGh),
                               tails=cos2_span(G, h, tail_idx, hGh), KP_TAU=cos2_span(G, h, kptau_idx, hGh),
                               kinds={kd: cos2_span(G, h, kinds[kd], hGh) for kd in kinds},
                               modes=[cos2_span(G, h, [j for j in range(nF) if int(col_m[j]) == mm], hGh) for mm in range(min(Mh, 8))]))
        sec["smallest5_shares"] = shares
        # principal cosines between the near-null subspace (sigma < 1e-6 sigma_max, else the 5 smallest) and the tail span, in X
        small = np.arange(len(S_) - min(5, len(S_)), len(S_))          # the 5 smallest singular directions (absolute values reported)
        sec["sigma_quantiles"] = {q: float(np.quantile(S_, q)) for q in (0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 1.0)}
        H = np.column_stack([extend(Vt[i]) for i in small])                 # X-orthonormal columns (up to the whitening error)
        Kt = G[np.ix_(tail_idx, tail_idx)]; lt, Vt_ = np.linalg.eigh(Kt); keep_t = lt > 1e-12 * lt.max()
        Et = np.zeros((next_, int(keep_t.sum()))); Et[tail_idx, :] = Vt_[:, keep_t] / np.sqrt(lt[keep_t])[None, :]
        pc = np.linalg.svd(Et.T @ G @ H, compute_uv=False)
        sec["near_null_dim"] = int(len(small)); sec["principal_cosines_near_null_vs_tails"] = [float(x) for x in pc[:min(len(pc), 8)]]
        if jidx:
            Ej = np.zeros((next_, 1)); Ej[jidx[0], 0] = 1 / np.sqrt(G[jidx[0], jidx[0]]); sec["principal_cosine_near_null_vs_Jcode"] = float(np.linalg.norm(Ej.T @ G @ H))
        Ei = np.zeros((next_, 1)); Ei[ntot, 0] = 1 / np.sqrt(G[ntot, ntot]); sec["principal_cosine_near_null_vs_Jinner"] = float(np.linalg.norm(Ei.T @ G @ H))
        res["sections"][name] = sec
        print(name, json.dumps({kk: vv for kk, vv in sec.items() if kk != "smallest5_shares"}), flush=True)
        for sh in shares[:3]:
            print("   sigma %.3e: J_code %s J_inner %.3f tails %.3f KP/TAU %.3f kinds %s" % (sh["sigma"], ("%.3f" % sh["J_code"]) if sh["J_code"] is not None else "-", sh["J_inner"], sh["tails"], sh["KP_TAU"], {kd: round(v, 3) for kd, v in sh["kinds"].items()}), flush=True)
        if name == "Fminus":
            # ell(Phi) in this conforming orthonormal F- basis: least squares of A_F h + A_tails p = 0 for tail increments p (Mh modes)
            ell = {}
            for lab, p in [("Theta0_truncated_to_Mh_modes", A0[:Mh]), ("cos0", np.eye(Mh)[0]), ("cos2", np.eye(Mh)[1]), ("cos4", np.eye(Mh)[2]), ("cos6", np.eye(Mh)[3])]:
                rhs = -(tails @ p) * roww
                v, resid, rk, sv = np.linalg.lstsq(B, rhs, rcond=None)
                h = np.zeros(next_); h[sel] = Q @ v
                ell[lab] = dict(dk=float(h[nF]), dtau=float(h[nF + 1]), rel_residual=float(np.linalg.norm(B @ v - rhs) / max(np.linalg.norm(rhs), 1e-300)), rank=int(rk), h_X_norm=float(np.sqrt(h @ G @ h)))
                print("ell %s: dk %.4e dtau %.4e rel_res %.2e rank %d ||h||_X %.3e" % (lab, ell[lab]["dk"], ell[lab]["dtau"], ell[lab]["rel_residual"], rk, ell[lab]["h_X_norm"]), flush=True)
            res["ell"] = dict(convention="Phi = chi(t) r^k [R0^{3-k} cos^2 theta sin theta sum_m p_m cos 2m theta] with the tail amplitude e^{(k-3)(t-t0)} anchored at t0; KP = d/dk' of x^2 y chi t e^{(k-3)(t-t0)} Theta_0~ (factor t, not t - t0); TAU = x^2 y chi e^{(k-3)(t-t0)} Theta_1", values=ell)
    res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "(%.0fs)" % (time.time() - t0))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], float(a[3]) if len(a) > 3 else 1e-10, int(a[4]) if len(a) > 4 else 0, a[5] if len(a) > 5 else "H1m")
