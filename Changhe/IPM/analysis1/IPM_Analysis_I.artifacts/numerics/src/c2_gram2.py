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
Usage: python3 src/c2_gram2.py save_raw.npz out.json [thresh=1e-10] [NJ=0] [MODE=H1m|H1|L2y] [SECTIONS=all|two] [ROWS=L2|H1|L2q|H1q]
  (L2q/H1q: the same rows with radial trapezoid quadrature weights, so that the functional approximates an integral in t and sections with different
  collocation densities are directly comparable without the per-row normalization; the spectrum route is the streaming QR for every ROWS.)
  (two = Fminus and free only; ROWS = H1: H1-type image norm, see weighted_rows; its spectrum is computed from the normal matrix, env C2_EIGH=1 forces
  that route for ROWS = L2 as a precision check against the SVD).
  WHY ROWS = H1: the version-2 functional pairs an H1-type column norm X with an L2-type image norm (collocation values of L h), so its smallest
  singular value measures an inverse that gains one derivative; a first-order transport operator has no such inverse (functions oscillating across
  the characteristics have ||L h||_{L2} = O(1) and ||h||_X = O(frequency)), and the finite section's smallest value is then expected to decrease
  with the resolution whatever the operator does at low frequency.  With ROWS = H1 both norms carry one derivative and the smallest value tests an
  inverse without derivative gain.
VERSION 3 (c2_gram2.py, shift 5, lead 12:07Z and verifier topics 127/128/130): (i) three CONTINUOUS reference functions are appended to the
extended basis, x^2 y f(t) with f a C^4 degree-9 polynomial step in t = log r (f = 1 - S(s), S(s) = 126 s^5 - 420 s^6 + 540 s^7 - 315 s^8 + 70 s^9,
s = (t - ta)/(tb - ta); f = 1 for t <= ta, 0 for t >= tb): ref_J (ta, tb) = (t0 - 1, t0), the continuous analogue of the section's J column
(x^2 y on r < R0, which jumps at R0); ref_Jin (tmin - 1, tmin), the continuous analogue of J_inner (x^2 y on r < rmin); ref_wide (tmin, t0),
x^2 y decaying smoothly across the whole fitted band.  Each is C^4 across its two joins (so in the H1m space exactly), lies in the m = 0 angular
mode, and its H1m norm is computed by the same quadrature (each join is a breakpoint).  cos^2 of the X-angle between the smallest singular
directions and each reference is reported (shares 'refs'), with the references' X-norms and their piecewise correlations with J_code/J_inner.
(ii) The five smallest right singular vectors of every section are SAVED in extended coordinates (out_vec.npz: <section>_h (next_ x 5),
<section>_sigma, <section>_hGh; the references' Gram columns G[ref, :]; the Gram diagonal; k, L, tmin, t0, Mh, nF, col_m/kind/label), so that
the cos^2 with any further reference can be computed afterwards from the _cols.pkl pieces alone (no raw matrix needed).
Everything else (rows, weights, Gram, constraints, eigen-cut, whitening, SVD) is unchanged from version 2 except as listed below; the section
values agree with the version-2 JSONs within the measured whitening error (on the fixture: to all printed digits; the quadrature nodes differ by
the breakpoints added at the reference joins).
ROW MEASURE CONVENTION (astra gram3, item 1): the rows carry the SPEC residual weight (1+u)^{1/2}/m at the collocation radii WITHOUT quadrature
weights (a discrete proxy of the weighted sup norm of L h); this is not the X measure e^{2t} m^{-2} (1+u^2)^{-3/2} dt, and sigma/sqrt(rows) is
comparable only between runs with the same row layout (same collocation scheme, Mout and ROWS). The collocation spacings vary (0.013 to 0.15 in t
in the production sections; up to 0.8 in the small fixture); the FD rows use the mean of the two endpoint weights (not an integration rule).
AFTER THE REFEREE ROUND astra/gram3 (13:01Z): the H1-row runs use NJ = 1 (with C^0 joins only, L h jumps at the external joins, [Lh] = (V.n)[d_n h],
and the FD rows there are mesh-dependent penalties); the H1-row spectrum is computed by a streaming Householder QR of B = Aw Q over row
chunks followed by the SVD of the nk x nk factor R (stable, no squaring of the condition number; about twice the cost of the normal matrix);
the normal-matrix route is kept as an option (C2_EIGH=1) with its smallest 40 candidates REFINED by direct evaluation (Rayleigh-Ritz: SVD of their
directly computed images A (Q v), exact residual quotients on that X-orthonormal subspace; raw eigh values kept as sigma_small5_raw_eigh);
C2_QR=1 forces the QR route for L2 rows; the references' cos^2 with the RETAINED constrained space is reported (refs_cos2_with_retained_space,
||Q^T G[sel, ref]||^2 / G[ref, ref]) besides the raw-F--span value; cos2_span equilibrates the sub-Gram before the pseudo-inverse; the constraint
rows are normalized before the rank decision and the join residual of the retained basis is reported; the vector archive carries ROWS, Mout,
t_eval, nrows, the spectrum method and the script's SHA-256; negative eigenvalues are counted and the smallest raw eigenvalue is saved; C2_EIGH=1
(exactly) forces the normal route, C2_SVD=1 forces the full SVD route for H1 rows (small cases only).
"""
STEP_COEF = [1.0, 0.0, 0.0, 0.0, 0.0, -126.0, 420.0, -540.0, 315.0, -70.0]      # 1 - S(s), S the C^4 smooth step (degree 9)


def step_pieces(ta, tb):
    """Exponential-polynomial pieces of f(t) = 1 (t < ta), 1 - S((t - ta)/(tb - ta)) on [ta, tb), 0 for t >= tb (C^4 at both joins)."""
    w = float(tb - ta)
    return [(-np.inf, float(ta), 0.0, [1.0]), (float(ta), float(tb), 0.0, [c / w ** j for j, c in enumerate(STEP_COEF)])]

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
    dK = np.sqrt(np.maximum(np.diag(K), 1e-300)); Ke = K / dK[:, None] / dK[None, :]; pe = p / dK      # equilibrated sub-Gram before the pseudo-inverse (astra gram3, item 6)
    Kp = np.linalg.pinv(Ke, rcond=1e-12, hermitian=True)
    return float(pe @ Kp @ pe / hGh)


def main(raw, out, thresh=1e-10, NJ=0, MODE="H1m", SECTIONS="all", ROWS="L2"):
    t0 = time.time()
    d = np.load(raw); meta = pickle.load(open(raw.replace(".npz", "_cols.pkl"), "rb"))
    Mat, KP, TAU, tails = d["Mat"], d["KP"], d["TAU"], d["tails"]
    t_eval = d["t_eval"]; k = float(d["k"]); L = float(d["L"]); Mout = int(d["Mout"]); Mh = int(d["Mh"]); tmin = float(d["tmin"]); t00 = float(d["t0"])
    uu = np.exp(t_eval) / L; mr = uu ** 3 * (1 + uu ** 2) ** ((k - 3) / 2); roww = np.repeat((1 + uu) ** 0.5 / mr, Mout)
    Ne = int(d["Ne"]); w_i = (1 + uu) ** 0.5 / mr                      # row weight per collocation radius
    def weighted_rows(Xu):
        """Xu: unweighted (Ne*Mout, nc) matrix, rows radius-major (i*Mout + N), (Lh)_N(t_i) the sine-(2N+1) image modes.  ROWS = 'L2': rows times w_i
        (the version-2 functional sum_i,N w_i^2 (Lh)_N(t_i)^2, an L2-type image norm).  ROWS = 'H1': an H1-type image norm of the same relative scale as
        the X norm, (Lh)^2 + r^2 |grad Lh|^2 = (Lh)^2 + (d_t Lh)^2 + (d_theta Lh)^2: value rows weighted w_i sqrt(1 + (2N+1)^2) (value and angular
        derivative) plus radial finite-difference rows ((Lh)_N(t_{i+1}) - (Lh)_N(t_i))/(t_{i+1} - t_i) weighted (w_i + w_{i+1})/2 for every pair of
        consecutive collocation radii (spacings 0.013-0.15 in t)."""
        quad = ROWS.endswith("q")                       # 'L2q' / 'H1q': radial trapezoid weights sqrt(omega_i) on the value rows and sqrt(Delta_i) on the FD rows,
        if quad:                                        # so that the functional approximates the integral  int sum_N [...] dt  (comparable across collocation densities)
            om = np.zeros(Ne); dtv = np.diff(t_eval); om[:-1] += 0.5 * dtv; om[1:] += 0.5 * dtv
            sq_om = np.sqrt(om); sq_dt = np.sqrt(dtv)
        else: sq_om = np.ones(Ne); sq_dt = np.ones(Ne - 1)
        if ROWS in ("L2", "L2q"): return Xu * (roww * np.repeat(sq_om, Mout))[:, None]
        X3 = Xu.reshape(Ne, Mout, -1); nc = X3.shape[2]
        ang = np.sqrt(1.0 + (2 * np.arange(Mout) + 1.0) ** 2)
        val = (X3 * ((w_i * sq_om)[:, None, None] * ang[None, :, None])).reshape(Ne * Mout, nc)
        dt = np.diff(t_eval); wm = 0.5 * (w_i[1:] + w_i[:-1])
        der = ((X3[1:] - X3[:-1]) * (wm * sq_dt / dt)[:, None, None]).reshape((Ne - 1) * Mout, nc)
        return np.vstack([val, der])
    col_m = d["col_m"]; col_kind = d["col_kind"]; col_label = d["col_label"]; A0 = d["A0"]; Bm = d["Bm"]
    cols = meta["cols"]; kp_pieces = meta["kp_pieces"]; tau_pieces = meta["tau_pieces"]
    nF = len(cols); Mt = len(A0); ntot = nF + 2 + Mh
    REFS = [("ref_J", t00 - 1.0, t00), ("ref_Jin", tmin - 1.0, tmin), ("ref_wide", tmin, t00), ("ref_wide16", t00 - 16.0, t00)]
    # ref_J, ref_Jin (width 1) and ref_wide16 (width 16) have EXACT binary64 step coefficients c_j / w^j, so S(1) = 1 holds exactly and the functions are
    # exactly C^4 and in X; ref_wide (width t0 - tmin = 13.008...) has rounded coefficients and an encoded end value of about 1.2e-13 at t0 (verifier
    # topic 134): its cos^2 values are broken-energy correlations, not X-angles. ref_wide16 (added 16:50Z) is its exact replacement (r from R0 e^-16 to R0).
    nref = len(REFS); next_ = ntot + 1 + nref                                   # extended basis: + J_inner reference + continuous references
    ref_idx = {name: ntot + 1 + i for i, (name, ta, tb) in enumerate(REFS)}
    assert Mh >= 4
    # ---- column functions: (radial pieces, angular coefficient vector over modes < Mang)
    Mang = Mt + 2; Aang = angular_matrix(Mang)
    def avec(pairs):
        a = np.zeros(Mang)
        for m, c in pairs: a[m] += c
        return a
    rad_pieces = [pieces for (m, pieces, lab) in cols] + [kp_pieces, tau_pieces, [(-np.inf, tmin, 0.0, [1.0])]] + [step_pieces(ta, tb) for (name, ta, tb) in REFS]   # J_inner radial, then the continuous references
    rad_of = list(range(nF)) + [nF, nF + 1] + [nF + 1] * Mh + [nF + 2] + [nF + 3 + i for i in range(nref)]
    acoef = [avec([(int(m), 1.0)]) for (m, pieces, lab) in cols] + [avec([(m, A0[m]) for m in range(Mt)]), avec([(m, Bm[m]) for m in range(min(Mt, len(Bm)))])] \
        + [avec([(m, 1.0)]) for m in range(Mh)] + [avec([(0, 1.0)])] + [avec([(0, 1.0)]) for _ in range(nref)]
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
    print("extended Gram %d x %d (%d function + KP + TAU + %d tails + J_inner ref + %d continuous refs); %d/%d radial nodes; 24-vs-48 relative difference %.2e; %.0fs" % (
        next_, next_, nF, Mh, nref, nq, nq2, gram_rel_diff, time.time() - t0), flush=True)
    for name, ta, tb in REFS:
        i = ref_idx[name]; print("   %s: x^2 y times the C^4 step in t on [%.6f, %.6f] (r in [%.6g, %.6g]); X-norm %.6e; piecewise cos^2 with J_code %s, with J_inner %.3e" % (
            name, ta, tb, np.exp(ta), np.exp(tb), np.sqrt(G[i, i]), ("%.3e" % cos2_span(G, np.eye(next_)[i], [jj for jj, (m, pieces, lab) in enumerate(cols) if lab == "J"])) if any(lab == "J" for (m, pieces, lab) in cols) else "-", cos2_span(G, np.eye(next_)[i], [ntot])), flush=True)
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
    Aw_all = weighted_rows(np.column_stack([Mat, KP, TAU, tails]))
    jidx = [i for i, (m, pieces, lab) in enumerate(cols) if lab == "J"]
    tail_idx = list(range(nF + 2, ntot)); kptau_idx = [nF, nF + 1]; jin_idx = [ntot]
    kinds = {kd: [i for i in range(nF) if col_kind[i] == kd] for kd in ("in", "sp", "out")}
    res = dict(raw=raw, Mh=Mh, stride=int(d["stride"]), Mout=Mout, ppc=int(d["ppc"]), Ne=int(d["Ne"]), nrows=int(Aw_all.shape[0]), n_collocation_rows=int(Ne * Mout), thresh=thresh, NJ=NJ,
               rows_mode=ROWS, rows_description={"L2": "sum_i,N w_i^2 (Lh)_N(t_i)^2, w_i = (1+u)^0.5/m (L2-type image norm)", "H1": "sum_i,N w_i^2 (1 + (2N+1)^2) (Lh)_N(t_i)^2 + sum_i,N ((w_i+w_i+1)/2)^2 [((Lh)_N(t_i+1) - (Lh)_N(t_i))/(t_i+1 - t_i)]^2 (H1-type image norm: value + angular derivative + radial finite difference)",
                                                 "L2q": "sum_i omega_i sum_N w_i^2 (Lh)_N(t_i)^2 with radial trapezoid weights omega_i (approximates int w^2 sum_N (Lh)_N^2 dt)", "H1q": "H1 rows with radial trapezoid weights omega_i on the value rows and Delta_i on the FD rows (approximates int w^2 [sum_N (1+(2N+1)^2)(Lh)_N^2 + (d_t (Lh)_N)^2] dt)"}[ROWS],
               spectrum_method=("svd" if os.environ.get("C2_SVD") == "1" else ("eigh of the normal matrix B^T B accumulated in row chunks, 40 smallest refined by direct evaluation (Rayleigh-Ritz)" if os.environ.get("C2_EIGH") == "1" else "streaming Householder QR of B over row chunks, SVD of the R factor")),
               inner_product=({"H1m": "int (h g + r^2 grad h . grad g) m(r)^-2 (1+r^2/L^2)^-1.5 dX  (m = u^3 (1+u^2)^((k-3)/2), the background scale)", "H1": "int (h g + r^2 grad h . grad g) (1+r^2/L^2)^-1.5 dX", "L2y": "int h g |y|^-2 (1+r^2/L^2)^-1.129 dX"}[MODE]), mode=MODE, row_weight="(1+u)^0.5/m(r)", gram_rel_diff_24_vs_48=gram_rel_diff, n_radial_nodes=nq,
               Xnorm2={"J_code": float(G[jidx[0], jidx[0]]) if jidx else None, "J_inner": float(G[ntot, ntot]), "KP": float(G[nF, nF]), "TAU": float(G[nF + 1, nF + 1]),
                       "inner_powers_min_max": [float(np.min(dg[kinds["in"]] ** 2)), float(np.max(dg[kinds["in"]] ** 2))] if kinds["in"] else None,
                       "cos2_Jcode_Jinner": cos2_span(G, np.eye(next_)[ntot], jidx) if jidx else None,
                       "refs": {name: dict(ta=ta, tb=tb, r_a=float(np.exp(ta)), r_b=float(np.exp(tb)), Xnorm=float(np.sqrt(G[ref_idx[name], ref_idx[name]])),
                                           cos2_with_Jcode_piecewise=cos2_span(G, np.eye(next_)[ref_idx[name]], jidx) if jidx else None,
                                           cos2_with_Jinner_piecewise=cos2_span(G, np.eye(next_)[ref_idx[name]], [ntot]),
                                           cos2_with_section_span=None) for (name, ta, tb) in REFS}},
               refs_definition="x^2 y f(t), f = 1 (t <= ta), 1 - S((t - ta)/(tb - ta)) on [ta, tb], 0 (t >= tb), S(s) = 126 s^5 - 420 s^6 + 540 s^7 - 315 s^8 + 70 s^9 (C^4 joins). Encoded as polynomials in t - ta with coefficients c_j/(tb - ta)^j: exact for the widths 1 (ref_J, ref_Jin) and 16 (ref_wide16), so these are exactly in X; ref_wide (width t0 - tmin) is rounded, end value about 1.2e-13 at t0 (ver topic 134): broken-energy correlation only",
               version="c2_gram2.py v3 (continuous references, saved singular vectors)", sections={})
    for name, ta, tb in REFS:         # how much of each reference lies in the span of the (unconstrained) F- columns: cos^2 with the whole section span
        res["Xnorm2"]["refs"][name]["cos2_with_section_span"] = cos2_span(G, np.eye(next_)[ref_idx[name]], list(range(nF + 2)))
    vec_out = {}
    section_list = [("Fminus", list(range(nF + 2))), ("Fminus_noJ", [i for i in range(nF + 2) if i not in jidx]), ("free", list(range(ntot))), ("free_noJ", [i for i in range(ntot) if i not in jidx])]
    if SECTIONS == "two": section_list = [section_list[0], section_list[2]]          # Fminus and free only (the noJ sections duplicate them to the printed digits)
    for name, sel in section_list:
        Gs = G[np.ix_(sel, sel)]; Ds = D[sel]; G1 = Gs * Ds[:, None] * Ds[None, :]          # equilibrated Gram (unit diagonal)
        C = constraints(NJ, sel)
        if C.shape[0]:
            Cn = C / np.linalg.norm(C, axis=1)[:, None]                                   # unit-norm constraint rows before the rank decision (astra gram3, item 6)
            Uc, Sc, Vct = np.linalg.svd(Cn, full_matrices=True); rank = int((Sc > 1e-10 * Sc[0]).sum()); N = Vct[rank:].T
        else: rank = 0; N = np.eye(len(sel))
        GN = N.T @ G1 @ N; lam, V = np.linalg.eigh(GN); lam = lam[::-1]; V = V[:, ::-1]
        keep = lam > thresh * lam[0]; keep12 = lam > 1e-12 * lam[0]
        QN = V[:, keep] / np.sqrt(lam[keep])[None, :]
        Q = (N @ QN) * Ds[:, None]                                        # original coefficients of the X-orthonormal basis (columns)
        join_residual = float(np.abs(Cn @ (N @ QN)).max()) if C.shape[0] else 0.0       # the retained basis satisfies the (unit-norm) join constraints to this accuracy
        Gs2 = G2[np.ix_(sel, sel)]; W = Q.T @ Gs2 @ Q; whit_err = float(np.abs(np.linalg.eigvalsh(W) - 1).max())
        Aw = Aw_all[:, sel]; nk = Q.shape[1]; nrow = Aw.shape[0]
        use_svd = os.environ.get("C2_SVD") == "1"                        # full SVD of B only on request (the streaming QR gives the same values; fixture: identical digits)
        use_eigh = (not use_svd) and os.environ.get("C2_EIGH") == "1"
        eig_info = {}; R_fac = None
        if use_svd:
            B = Aw @ Q; U_, S_, Vt = np.linalg.svd(B, full_matrices=False)
        elif not use_eigh:   # DEFAULT for H1 rows: streaming Householder QR of B = Aw Q over row chunks (stable, no squaring), then the SVD of the nk x nk factor R
            B = None; R = np.zeros((0, nk))
            for c0 in range(0, nrow, 4096):
                Bc = Aw[c0:c0 + 4096] @ Q; R = np.linalg.qr(np.vstack([R, Bc]), mode="r")[:nk]
            U_, S_, Vt = np.linalg.svd(R, full_matrices=False); R_fac = R
            eig_info = dict(spectrum_note="singular values of B from the SVD of its streaming-QR factor R (B = Q_B R)")
        else:            # memory-light route: normal matrix B^T B over row chunks; singular values = sqrt(eigenvalues), right singular vectors = eigenvectors
            B = None; Nm = np.zeros((nk, nk))
            for c0 in range(0, nrow, 4096):
                Bc = Aw[c0:c0 + 4096] @ Q; Nm += Bc.T @ Bc
            lamB, VB = np.linalg.eigh(Nm); del Nm
            eig_info = dict(eig_min_raw=float(lamB[0]), n_negative_eigenvalues=int((lamB < 0).sum()), eig_max=float(lamB[-1]))
            S_raw = np.sqrt(np.maximum(lamB[::-1], 0.0)); Vt = VB[:, ::-1].T.copy()
            # Rayleigh-Ritz refinement of the smallest candidates by DIRECT evaluation of their images (astra gram3, item 4)
            nref_rr = min(40, nk); Vc = VB[:, :nref_rr]                                   # ascending eigenvalues: the smallest candidates
            QV = Q @ Vc; Bc = np.vstack([Aw[c0:c0 + 4096] @ QV for c0 in range(0, nrow, 4096)])
            Uc, Sc, Wct = np.linalg.svd(Bc, full_matrices=False)                           # exact residual quotients on the X-orthonormal subspace span(Q Vc)
            eig_info["sigma_small5_raw_eigh"] = [float(x) for x in S_raw[-5:][::-1]]
            eig_info["rayleigh_ritz_subspace_dim"] = nref_rr
            S_ = S_raw.copy(); S_[-nref_rr:] = np.sort(Sc)[::-1]                          # positions nk-nref_rr .. nk-1 hold the refined values (descending, smallest last)
            Vt[-nref_rr:] = (Vc @ Wct.T)[:, np.argsort(Sc)[::-1]].T                          # refined right vectors in the same order
            del Bc, QV
        sec = dict(ncol=len(sel), n_constraints=int(C.shape[0]), constraint_rank=rank, nfree=int(N.shape[1]), n_kept=int(nk), n_kept_at_1em12=int(keep12.sum()),
                   gram_cond_after_equilibration=float(lam[0] / lam[keep][-1]), whitening_error_refined_quadrature=whit_err,
                   trivial_null_dimension=int(max(nk - nrow, 0)), sigma_max=float(S_[0]), sigma_small5=[float(x) for x in S_[-5:][::-1]],
                   join_residual_of_retained_basis=join_residual, spectrum_route=("svd" if use_svd else ("normal matrix + Rayleigh-Ritz refinement of the 40 smallest" if use_eigh else "streaming QR + SVD of R")), **eig_info,
                   refs_cos2_with_retained_space={rn: float(np.sum((Q.T @ G[sel, ref_idx[rn]]) ** 2) / G[ref_idx[rn], ref_idx[rn]]) for (rn, ta, tb) in REFS},
                   note_near_null="'near_null' below always means the five smallest singular directions (no threshold rule)",
                   n_below_1em3=int((S_ < 1e-3 * S_[0]).sum()), n_below_1em6=int((S_ < 1e-6 * S_[0]).sum()))
        # shares of the smallest right singular vectors (coefficients extended to the full basis incl. the J_inner reference)
        def extend(v):
            h = np.zeros(next_); h[sel] = Q @ v; return h
        shares = []
        for i in range(min(5, len(S_))):
            h = extend(Vt[-1 - i]); hGh = float(h @ G @ h)
            shares.append(dict(sigma=float(S_[-1 - i]), hGh=hGh, J_code=cos2_span(G, h, jidx, hGh) if jidx else None, J_inner=cos2_span(G, h, jin_idx, hGh),
                               tails=cos2_span(G, h, tail_idx, hGh), KP_TAU=cos2_span(G, h, kptau_idx, hGh),
                               refs={rn: cos2_span(G, h, [ref_idx[rn]], hGh) for (rn, ta, tb) in REFS},
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
        sec["principal_cosine_near_null_vs_refs"] = {}
        for rn, ta, tb in REFS:
            Er = np.zeros((next_, 1)); Er[ref_idx[rn], 0] = 1 / np.sqrt(G[ref_idx[rn], ref_idx[rn]]); sec["principal_cosine_near_null_vs_refs"][rn] = float(np.linalg.norm(Er.T @ G @ H))
        vec_out[name + "_h"] = H[:, ::-1].copy(); vec_out[name + "_sigma"] = S_[small][::-1].copy(); vec_out[name + "_hGh"] = np.array([sh["hGh"] for sh in shares])   # column 0 = smallest
        # unweighted collocation images (Lh)_N(t_i) of the five smallest directions (rows i*Mout + N), so that every row functional (L2, L2q, H1, H1q)
        # can be evaluated on the SAME vectors afterwards (astra gram4, item 2); the assembler's operator is the full linearization incl. the c[h]/3 X.grad rho~ term
        Hs = H[:, ::-1]; img = Mat @ Hs[:nF] + KP[:, None] * Hs[nF][None, :] + TAU[:, None] * Hs[nF + 1][None, :]
        if ntot > nF + 2 and max(sel) >= nF + 2: img = img + tails @ Hs[nF + 2:ntot]
        vec_out[name + "_img"] = img
        res["sections"][name] = sec
        print(name, json.dumps({kk: vv for kk, vv in sec.items() if kk != "smallest5_shares"}), flush=True)
        for sh in shares[:3]:
            print("   sigma %.3e: J_code %s J_inner %.3e tails %.3e KP/TAU %.3e refs %s kinds %s" % (sh["sigma"], ("%.3e" % sh["J_code"]) if sh["J_code"] is not None else "-", sh["J_inner"], sh["tails"], sh["KP_TAU"], {rn: "%.3e" % v for rn, v in sh["refs"].items()}, {kd: round(v, 3) for kd, v in sh["kinds"].items()}), flush=True)
        if name == "Fminus" and ROWS == "L2":
            # ell(Phi) in this conforming orthonormal F- basis: least squares of A_F h + A_tails p = 0 for tail increments p (Mh modes).
            # Solved through the QR factor (R^T R v = B^T rhs; B = Aw Q) when available: the version-2 lstsq (an SVD per right-hand side) took most of the run time.
            from scipy.linalg import solve_triangular
            ell = {}
            for lab, p in [("Theta0_truncated_to_Mh_modes", A0[:Mh]), ("cos0", np.eye(Mh)[0]), ("cos2", np.eye(Mh)[1]), ("cos4", np.eye(Mh)[2]), ("cos6", np.eye(Mh)[3])]:
                rhs = -(tails @ p) * roww
                if R_fac is not None:
                    bt = Q.T @ (Aw.T @ rhs); v = solve_triangular(R_fac, solve_triangular(R_fac, bt, trans="T")); rk = nk
                    res_vec = Aw @ (Q @ v) - rhs
                else:
                    B = Aw @ Q if B is None else B
                    v, resid, rk, sv = np.linalg.lstsq(B, rhs, rcond=None); res_vec = B @ v - rhs
                h = np.zeros(next_); h[sel] = Q @ v
                ell[lab] = dict(dk=float(h[nF]), dtau=float(h[nF + 1]), rel_residual=float(np.linalg.norm(res_vec) / max(np.linalg.norm(rhs), 1e-300)), rank=int(rk), h_X_norm=float(np.sqrt(h @ G @ h)))
                print("ell %s: dk %.4e dtau %.4e rel_res %.2e rank %d ||h||_X %.3e" % (lab, ell[lab]["dk"], ell[lab]["dtau"], ell[lab]["rel_residual"], rk, ell[lab]["h_X_norm"]), flush=True)
            res["ell"] = dict(convention="Phi = chi(t) r^k [R0^{3-k} cos^2 theta sin theta sum_m p_m cos 2m theta] with the tail amplitude e^{(k-3)(t-t0)} anchored at t0; KP = d/dk' of x^2 y chi t e^{(k-3)(t-t0)} Theta_0~ (factor t, not t - t0); TAU = x^2 y chi e^{(k-3)(t-t0)} Theta_1", values=ell)
    res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "(%.0fs)" % (time.time() - t0))
    vec_file = out[:-5] + "_vec.npz" if out.endswith(".json") else out + "_vec.npz"
    np.savez_compressed(vec_file, G_ref_cols=G[[ref_idx[rn] for (rn, ta, tb) in REFS], :], ref_names=np.array([rn for (rn, ta, tb) in REFS]),
                        ref_ta_tb=np.array([[ta, tb] for (rn, ta, tb) in REFS]), G_diag=np.diag(G), G_Jinner_col=G[ntot, :], G_KP_TAU_cols=G[[nF, nF + 1], :],
                        k=k, L=L, tmin=tmin, t0=t00, Mh=Mh, nF=nF, ntot=ntot, next=next_, A0=A0, Bm=Bm, col_m=col_m, col_kind=col_kind, col_label=col_label, mode=MODE, NJ=NJ, thresh=thresh,
                        ROWS=ROWS, Mout=Mout, Ne=Ne, t_eval=t_eval, w_i=w_i, nrows=int(Aw_all.shape[0]), raw=raw, spectrum_method=res["spectrum_method"],
                        operator="full linearization L h = V.grad h - h + (U[h] + c[h] X).grad rho~, c[h] = psi[h]_xy(0)/3 (lin_assembly.column: outT + outB + outC)",
                        script_sha256=__import__("hashlib").sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(), **vec_out)
    print("saved", vec_file)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], float(a[3]) if len(a) > 3 else 1e-10, int(a[4]) if len(a) > 4 else 0, a[5] if len(a) > 5 else "H1m", a[6] if len(a) > 6 else "all", a[7] if len(a) > 7 else "L2")
