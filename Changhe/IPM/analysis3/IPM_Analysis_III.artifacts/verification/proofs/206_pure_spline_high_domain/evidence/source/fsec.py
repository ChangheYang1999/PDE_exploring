"""Floating-point section of L_red in the lead's w_a jet realization (lead note 12 item 4; s2-num 05:10Z). NUMERICAL ESTIMATE, not a certificate.

Spaces (S2_L2_THEORY.md 5.2): Z = E B (+) D_R, Y = E G (+) R; a = 17/4; w_a = |cos theta|^{-2a} e^{mu_a(log r)}, mu_a' = -17/2 (t < 0), -5/4 (t > 0).
 E beta = x^2 y beta(log r).  R = L^2(w_a): for g = e^{3t} sum_N G_N(t) sin((2N+1) theta) vanishing like cos^4 at the y-axis,
 ||g||_R^2 = int e^{8t + mu_a(t)} [Q(t)^T A Q(t)] dt, Q = modes of g/(r^3 cos^4 theta), A_{NN'} = int sin((2N+1)th) sin((2N'+1)th) |cos th|^{-1/2} dth.
 G: ||gamma||_G^2 = int_{t<0} gamma^2 e^{-t/2} + int_{t>0} gamma^2 e^{27t/4};  B: beta = H z, ||beta||_B = ||z'||_{L^2(omega)},
 omega = e^{-t/2} (t<0), e^{(3/4 + 2k) t} (t>0), H = (d/D)^2 exp(-int_{-inf}^t (D - d)/d ds), d(t) = V_2(0, e^t)/e^t (V041).
Operator: L_red h_0 = L(h_0 + kappa KP), kappa = -k c[h_0]/(3 c_l + k c_KP) (S2_C_FUNCTIONAL.md 7.2): exactly the compensated images of
 the S0 machinery (opimage/section). Domain basis (same span as the S0 columns): jet columns x^2 y b_i(t) (the m = 0 columns incl. J) and
 remainder columns x^2 y b_i(t) (cos 2m theta - (-1)^m) = cos^4 theta r^3 b_i (...) for m >= 1.  Image split: gamma = axis second-order
 coefficient of the factor (= -(1/2) sum (-1)^N (2N+1)^2 G_N), remainder = g - E gamma, divided by cos^4 (least squares; residual reported).
Quadrature: Gauss-Legendre nodes per cell (3 on spline cells, 8 on sub-cells, 16 on a length-40 stretch of each half-line). Images truncated
 at N <= NMAX (default 19; the background is kept to 26 modes on non-full cells, which excludes the near-resonant inner mode 27).
Usage: python3 fsec.py <tag> Mh stride nworkers [prec] [NMAX | all] [cells_limit or cell list]   (env FSEC_MODE=S1 for the core section)
Outputs runs/<tag>/part_*.npz (per-worker Gram accumulators) and prep.npz; assemble with fsec_assemble.py.
"""
import sys, os, time, json, math
import numpy as np
import multiprocessing as mp
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Column, Operator
from basis import cutoff_chi
from section import Weights, Section
from run_section import HERE
import fsec_ang as ang

A_ANI = 17.0 / 4
MODE = os.environ.get("FSEC_MODE", "LRED")      # LRED: L_red on Z = E B (+) D_R -> Y = E G (+) R;  S1: S_1 = T_R + C_R on R = L^2(w_a) -> R (lead note 19 item 3)


def mu_a(t): return -8.5 * t if t < 0 else -1.25 * t
def gG(t): return np.exp(-0.5 * t) if t < 0 else np.exp(6.75 * t)
def omega(t, k): return np.exp(-0.5 * t) if t < 0 else np.exp((0.75 + 2 * k) * t)


def gauss_nodes(a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    return (a + b) / 2 + (b - a) / 2 * x, (b - a) / 2 * w


def ep_eval(ep, s):
    """float value of the ExpPoly at sigma = s (float)"""
    return float(ep(arb(s)).mid()) if ep.terms else 0.0


def prep_nodes(T, cells, bg_full, L=40.0, ng_mid=3, ng_sub=8, ng_half=16):
    """nodes per cell (sigma, t, weight) and the axis data d, d', H, (log H)' at the nodes"""
    c_l = float((1 / T.k).mid()); D = 4 * c_l - 1
    nodes = []
    for ic, cl in enumerate(cells.cells):
        ta = float(cl["ta"].mid())
        if cl["kind"] == "minf": s, w = gauss_nodes(-L, 0.0, ng_half)
        elif cl["kind"] == "pinf": s, w = gauss_nodes(0.0, L, ng_half)
        else:
            h = float(cl["h"].mid()); s, w = gauss_nodes(0.0, h, ng_sub if cl["kind"] in ("inner", "outer") else ng_mid)
        nodes.append((s, ta + s, w))
    # d, d' at the nodes (full background, 260 modes; non-mid cells at 512 bits)
    dvals = []; dpvals = []
    for ic, cl in enumerate(cells.cells):
        saved = ctx.prec; ctx.prec = 512 if cl["kind"] != "mid" else saved
        dd = bg_full.get(ic)
        dEP = ExpPoly()
        for n in range(1, T.Nf + 1): dEP = dEP + dd["Pe"][n - 1].scale(arb((-1) ** (n + 1)))
        dpEP = dEP.deriv()
        s = nodes[ic][0]
        dvals.append(np.array([c_l + ep_eval(dEP, x) for x in s])); dpvals.append(np.array([ep_eval(dpEP, x) for x in s]))
        ctx.prec = saved
    # F(t) = int_{-inf}^t (D - d)/d: cumulative over cells (Gauss on each cell; the minf cell: f ~ C e^{2t} so F ~ f/2 at its nodes)
    F_start = []; Fnodes = []
    F = 0.0
    for ic, cl in enumerate(cells.cells):
        s, t, w = nodes[ic]; f = (D - dvals[ic]) / dvals[ic]
        if cl["kind"] == "minf":
            Fn = f / 2.0                                    # asymptotic cumulative value at each node
            F = float(Fn[-1] + np.sum(w * f) - np.sum(w * f))  # F at the end of the half-line stretch ~ value at the last node + tail
            F = float(f[-1] / 2.0)                          # end of minf stretch (sigma = 0): f(t_a)/2
            Fnodes.append(Fn); F_start.append(None); continue
        F_start.append(F)
        # within the cell: F(node_j) ~ F_start + integral from the cell start, by cumulative trapezoid over (start, nodes)
        cum = np.zeros_like(s); prev_s = 0.0; prev_f = f[0]; acc = 0.0
        for j in range(len(s)):
            acc += 0.5 * (prev_f + f[j]) * (s[j] - prev_s); cum[j] = acc; prev_s = s[j]; prev_f = f[j]
        Fnodes.append(F + cum)
        F += float(np.sum(w * f))
    H = []; dlogH = []
    for ic in range(cells.n):
        d = dvals[ic]; dp = dpvals[ic]
        H.append((d / D) ** 2 * np.exp(-Fnodes[ic])); dlogH.append(-(D - d - 2 * dp) / d)
    return nodes, dvals, dpvals, H, dlogH


CKPT_SEC = float(os.environ.get("FSEC_CKPT_SEC", "600"))


def worker(args):
    wid, cell_idx, outdir = args
    ctx.prec = PREC
    n_new = len(NEW); nm = NMAX + 1
    GZ = np.zeros((n_new, n_new)); BY = np.zeros((n_new, n_new))
    done = []; lastck = time.time()
    TOP = []
    diag = dict(axis_res_max=0.0, div_res_max=0.0, trjet_max=0.0, topmode_frac_max=0.0, cells=0,
                E_axis_res=0.0, E_div_res=0.0, E_img=0.0, E_trjet=0.0, E_tr=0.0, E_top3=0.0, t_img=0.0, t_far=0.0, t_acc=0.0)
    t0 = time.time(); last = t0
    for cnt, ic in enumerate(cell_idx):
        cl = CELLS.cells[ic]; s_nodes, t_nodes, w_nodes = NODES[ic]
        ctx.prec = 512 if (ALLMODES and cl["kind"] != "mid") else PREC    # V054 near-resonance of the inner mode 27 in the re-expanded Green data
        tc0 = time.time()
        ncol = len(SEC.cols); ns = len(s_nodes)
        G = np.zeros((ns, nm, ncol)); TR = np.zeros((ns, nm, ncol)); Bv = np.zeros((ns, ncol)); dBv = np.zeros((ns, ncol))
        def ev(img):
            """float samples (ns, nm) of an image dict N -> ExpPoly"""
            out = np.zeros((ns, nm))
            for N, ep in img.items():
                if N < nm and ep.terms:
                    for a, s in enumerate(s_nodes): out[a, N] = ep_eval(ep, s)
            return out
        # Images combined EXACTLY in ball arithmetic AT THE NODE VALUES before the float conversion (06:30Z): the KP compensation cancels the
        # e^{(k-3)t} tail of each image; at far nodes the cancelling parts exceed the remainder by orders of magnitude, so a float combination is
        # noise, and combining the ExpPolys themselves made the evaluations 10x slower (hundreds of exponent terms).
        def evA(img):
            """arb samples [a][N] of an image dict N -> ExpPoly (None where absent)"""
            out = [[None] * nm for _ in range(ns)]
            for N, ep in img.items():
                if N < nm and ep.terms:
                    for a, s in enumerate(s_nodes): out[a][N] = ep(arb(s))
            return out
        def addv(dst, src_, scale=None):
            for a in range(ns):
                for N in range(nm):
                    v = src_[a][N]
                    if v is None: continue
                    if scale is not None: v = v * scale
                    dst[a][N] = v if dst[a][N] is None else dst[a][N] + v
        def tofloat(vals):
            out = np.zeros((ns, nm))
            for a in range(ns):
                for N in range(nm):
                    if vals[a][N] is not None: out[a, N] = float(vals[a][N].mid())
            return out
        far = {}; far_n = set(); insup = {}
        for j, cd in enumerate(SEC.cols):
            if j not in USED: continue                     # 12:45Z: columns not used by any new-basis column are skipped (their images are never read)
            col = cd["col"]
            if ic in col.pieces:
                insup[j] = OP.image(col, ic, parts=True)
                b = col.pieces[ic]; db = b.deriv()
                for a, s in enumerate(s_nodes): Bv[a, j] = ep_eval(b, s); dBv[a, j] = ep_eval(db, s)
            else:
                fc = OP.far_coefficients(col, ic); far[j] = fc; far_n |= set(fc)
        KP = SEC.KP[0]
        if MODE == "S1": KPv = [[None] * nm for _ in range(ns)]          # S_1 has no KP compensation
        elif ic in KP.pieces: KPv = evA(OP.image(KP, ic))
        else:
            fcK = OP.far_coefficients(KP, ic); far["KP"] = fcK; far_n |= set(fcK); KPv = None
        diag["t_img"] += time.time() - tc0; tc1 = time.time()
        unit = OP.far_unit_images(ic, sorted(far_n)) if far_n else {}
        UAv = {n: evA(unit[n][0]) for n in unit}; UBv = {n: evA(unit[n][1]) for n in unit}
        Mv = evA({N: ep for N, ep in OP.M_cached(ic).items() if N < nm})
        def far_vals(fc, c):
            out = [[None] * nm for _ in range(ns)]
            for n, (al, be) in fc.items():
                if al != 0: addv(out, UAv[n], al)
                if be != 0: addv(out, UBv[n], be)
            if c != 0: addv(out, Mv, c)
            return out
        if KPv is None: KPv = far_vals(far["KP"], KP.c)
        dkb = DKB                                                      # exact Arb compensation coefficients (not rounded through float)
        if MODE == "S1":
            # strain term with the cutoff chi_0 := chi_J (the exact C^6 cutoff of the J column, 1 near 0): C_chi u = C_full u - (c[u]/3)(1 - chi_J) X.grad rho~,
            # whose factor modes are (c/3)(1 - chi_J(sigma)) dR_N(sigma); no KP compensation (S_1 acts on R and its image is taken in R)
            Jcol = SEC.cols[JIDX]["col"]; chiJ = Jcol.pieces.get(ic)
            d_ = OP.bg.get(ic)
            one_minus_chi = [arb(1) - (chiJ(arb(s)) if chiJ is not None else arb(0)) for s in s_nodes]
            dRv = [[(d_["dR"][N](arb(s)) if N < len(d_["dR"]) else None) for N in range(nm)] for s in s_nodes]
        for j, cd in enumerate(SEC.cols):
            if j not in USED: continue
            if j in insup:
                imT, imC = insup[j]; Tv = evA(imT); TR[:, :, j] = tofloat(Tv)
                tot = [[None] * nm for _ in range(ns)]; addv(tot, Tv); addv(tot, evA(imC))
                if MODE != "S1": addv(tot, KPv, dkb[j])
            else:
                tot = far_vals(far[j], SEC.cols[j]["col"].c)
                if MODE != "S1": addv(tot, KPv, dkb[j])
            if MODE == "S1":
                cj = SEC.cols[j]["col"].c
                if cj != 0:
                    for a in range(ns):
                        fac = -(cj / 3) * one_minus_chi[a]
                        for N in range(nm):
                            if dRv[a][N] is not None: tot[a][N] = (tot[a][N] + fac * dRv[a][N]) if tot[a][N] is not None else fac * dRv[a][N]
            G[:, :, j] = tofloat(tot)
        diag["t_far"] += time.time() - tc1; tc2 = time.time()
        # new basis and accumulation per node
        for a in range(len(s_nodes)):
            t = t_nodes[a]; w = w_nodes[a]
            wR = np.exp(8 * t + mu_a(t)); wG = gG(t); wB = omega(t, KF)
            Hn = HH[ic][a]; dlH = DLOGH[ic][a]
            # Y side: full images of the new basis columns: jet cols = col(L,0); remainder = col(L,m) - (-1)^m col(L,0)
            Gnew = G[a] @ NEWMAT            # (nm, n_new)
            TRnew = TR[a] @ NEWMAT
            gam = np.zeros(n_new); Q = np.zeros((nm - 2, n_new)); ax = np.zeros(n_new); dres2 = 0.0
            for b_ in range(n_new):
                g_, R_, a0 = ang.jet_split(Gnew[:, b_]); gam[b_] = g_; ax[b_] = a0
                q_, res = DIV(R_); Q[:, b_] = q_
                diag["div_res_max"] = max(diag["div_res_max"], res / (np.linalg.norm(R_) + 1e-300)); dres2 += res * res
            diag["axis_res_max"] = max(diag["axis_res_max"], float(np.max(np.abs(ax)) / (np.max(np.abs(Gnew)) + 1e-300)))
            if MODE == "S1":
                BY += w * wR * (Q.T @ AH @ Q); diag["E_jetS1"] = diag.get("E_jetS1", 0.0) + w * wG * float(np.sum(gam ** 2))
            else:
                BY += w * (wG * np.outer(gam, gam) + wR * (Q.T @ AH @ Q))
            # top contributions (diagnostic of the far-node scaling): per column, w * (wG gamma^2 + wR Q^T A Q)
            contrib = w * (wG * gam ** 2 + wR * np.einsum("ij,ik,kj->j", Q, AH, Q))
            jb = int(np.argmax(contrib)); TOP.append((float(contrib[jb]), ic, float(t), NEW[jb][1], NEW[jb][2], float(gam[jb]), float(np.max(np.abs(Gnew[:, jb])))))
            if len(TOP) > 400: TOP.sort(reverse=True); del TOP[12:]
            top = np.sum(Gnew[-3:, :] ** 2); tot = np.sum(Gnew ** 2) + 1e-300
            diag["topmode_frac_max"] = max(diag["topmode_frac_max"], float(top / tot))
            # energy-weighted diagnostics (R-weight w_R; the mode vectors are compared in the plain l2 of modes)
            diag["E_img"] += w * wR * tot; diag["E_top3"] += w * wR * top; diag["E_axis_res"] += w * wR * float(np.sum(ax ** 2)); diag["E_div_res"] += w * wR * dres2
            # Z side
            # jet columns: z' = (beta' - beta dlogH)/H with beta = b_L
            zp = np.zeros(n_new); QR = np.zeros((nm - 2, n_new)); QT = np.zeros((nm - 2, n_new))
            for b_ in range(n_new):
                kind, L, m, j0, jm = NEW[b_]
                if kind == "jet":
                    beta = Bv[a, j0] / SCALE[j0]; dbeta = dBv[a, j0] / SCALE[j0]
                    zp[b_] = (dbeta - beta * dlH) / Hn
                else:
                    QR[:, b_] = Bv[a, j0] / SCALE[j0] * VM[m]          # modes of h_R/(r^3 cos^4) (scaled column)
                    gT, RT, a0T = ang.jet_split(TRnew[:, b_])
                    diag["trjet_max"] = max(diag["trjet_max"], abs(gT) / (np.max(np.abs(TRnew[:, b_])) + 1e-300))
                    diag["E_trjet"] += w * wR * (gT * gT / 16.0); diag["E_tr"] += w * wR * float(np.sum(TRnew[:, b_] ** 2))
                    qT, _ = DIV(RT); QT[:, b_] = qT
            if MODE == "S1": GZ += w * wR * (QR.T @ AH @ QR)          # R = L^2(w_a) norm of u only
            else: GZ += w * (wB * np.outer(zp, zp) + wR * (QR.T @ AH @ QR + QT.T @ AH @ QT))
        diag["t_acc"] += time.time() - tc2
        diag["cells"] += 1; done.append(int(ic))
        if time.time() - lastck > CKPT_SEC:
            lastck = time.time()
            np.savez(os.path.join(outdir, "ckpt_%d_%d.npz" % (wid, os.getpid())), GZ=GZ, BY=BY, diag=json.dumps({k: v for k, v in diag.items()}), done=np.array(done))
        if time.time() - last > 120:
            last = time.time()
            with open(os.path.join(outdir, "progress_%d.txt" % wid), "w") as f: f.write("%d/%d cells, %.0fs (img %.0f, far %.0f, acc %.0f)\n" % (cnt + 1, len(cell_idx), time.time() - t0, diag["t_img"], diag["t_far"], diag["t_acc"]))
    TOP.sort(reverse=True); diag["top_contributions"] = [dict(value=v, cell=c, t=t_, label=l, m=m_, gamma=g, max_mode=mx) for v, c, t_, l, m_, g, mx in TOP[:12]]
    np.savez(os.path.join(outdir, "part_%d.npz" % wid), GZ=GZ, BY=BY, diag=json.dumps(diag), done=np.array(done))      # done set stored (12:40Z, lead note 38)
    return wid, len(cell_idx), time.time() - t0, diag


if __name__ == "__main__":
    a = sys.argv
    tag, Mh, stride, nw = a[1], int(a[2]), int(a[3]), int(a[4])
    PREC = int(a[5]) if len(a) > 5 else 256       # 256 as in S0: at 192 bits the exact-zero check of the strain image M fails on inner cells (radius 4e-58)
    NMAX = (None if (len(a) > 6 and a[6] == "all") else (int(a[6]) if len(a) > 6 else 19))     # 'all': complete mode set (exact cos^4 division)
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial(prec=PREC); T.build_green(verbose=True)
    CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    full = set(cutoff_chi(T, CELLS).keys()) | set(ic for ic, cl in enumerate(CELLS.cells) if cl["kind"] in ("outer", "pinf"))
    if NMAX is None:
        NMAX = 2 * T.Mj + 2 * Mh + 4               # highest image mode (sin((2j+1+2n) theta) with j <= Mj - 1, n <= Mh + 1): complete set (522 for the trial)
        bg = Background(T, CELLS, nmax=None)      # all background modes (inner cells need 512 bits: see HI_PREC handling below)
        ALLMODES = True
    else:
        bg = Background(T, CELLS, nmax=NMAX + Mh + 3, full_cells=full)
        ALLMODES = (NMAX + Mh + 3 >= 27)          # the truncated background then contains the near-resonant inner mode 27 (V054): non-mid cells at 512 bits
    k = T.k_q; KF = float(q2arb(k).mid())
    W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    SEC = Section(T, CELLS, bg, W, Mh=Mh, stride=stride, Mout=NMAX + 1, stride_test=30)
    OP = SEC.op
    c_l = 1 / T.k; denom = 3 * c_l + T.k * SEC.cKP
    DKB = [-(cd["col"].c) * T.k / denom for cd in SEC.cols]          # exact ball quotients, used in the node-value compensation (verifier 07:03Z)
    DK = [float(x.mid()) for x in DKB]                                 # floats for the record only
    # new basis: (kind, label, m, j0 (index of the m=0 column with this label), jm (index of the (label, m) column))
    by_label = {}
    for j, cd in enumerate(SEC.cols): by_label.setdefault(cd["label"], {})[cd["m"]] = j
    NEW = []
    for lab, dm in sorted(by_label.items(), key=lambda kv: min(kv[1].values())):
        if 0 in dm: NEW.append(("jet", lab, 0, dm[0], dm[0]))
    for lab, dm in sorted(by_label.items(), key=lambda kv: min(kv[1].values())):
        for m in sorted(dm):
            if m >= 1:
                assert 0 in dm, "remainder column without its m = 0 partner: " + lab
                NEW.append(("rem", lab, m, dm[0], dm[m]))
    if MODE == "S1": NEW = [x for x in NEW if x[0] == "rem"]
    DROP = [x for x in os.environ.get("FSEC_DROP", "").split(",") if x]       # junction test (10:15Z): e.g. FSEC_DROP=+out removes the sp+out columns
    if DROP: NEW = [x for x in NEW if not any(d_ in x[1] for d_ in DROP)]; print("dropped columns matching %s -> %d new-basis columns" % (DROP, len(NEW)), flush=True)
    USED = set(j for x in NEW for j in (x[3], x[4]))        # S0 columns whose images are needed (j0 = the m = 0 partner, jm = the (label, m) column)
    print("S0 columns with images computed: %d of %d" % (len(USED), len(SEC.cols)), flush=True)
    JIDX = [j for j, cd in enumerate(SEC.cols) if cd["label"] == "J"][0]
    import pickle
    prep_file = os.path.join(HERE, "runs", "fsec_prep_L40_ng3_8_16.pkl")          # floating data; independent of the ball precision
    if os.path.exists(prep_file):
        NODES, DV, DPV, HH, DLOGH = pickle.load(open(prep_file, "rb")); print("prep: loaded", prep_file, flush=True)
    else:
        print("prep: nodes and axis data (full background)", flush=True)
        bg_full = Background(T, CELLS, nmax=None)
        NODES, DV, DPV, HH, DLOGH = prep_nodes(T, CELLS, bg_full)
        pickle.dump((NODES, DV, DPV, HH, DLOGH), open(prep_file, "wb"))
    ncol = len(SEC.cols); NEWMAT = np.zeros((ncol, len(NEW)))
    # column pre-scaling (07:15Z): the weight e^{8t + mu_a} spans e^{-25} .. e^{+108} over the support of the columns, so an unscaled float64
    # Gram has a dynamic range of 1e30+ and is numerically indefinite. Every column is divided by SCALE[j] = exp((8 + mu_a'(t_j)) t_j / 2)
    # at the centre t_j of its support (the generalized singular values are invariant under column scaling); the remainder combination
    # col(L, m) - (-1)^m col(L, 0) shares the radial factor, so both members get the same scale.
    def support_centre(col):
        ts = [float(CELLS.cells[ic]["ta"].mid()) for ic in col.pieces if CELLS.cells[ic]["kind"] == "mid"]
        if ts: return 0.5 * (min(ts) + max(ts))
        kinds = {CELLS.cells[ic]["kind"] for ic in col.pieces}
        return float(T.t_hi_q) if ("pinf" in kinds or "outer" in kinds) else float(T.t_lo_q)
    # (07:20Z) the scale is the column's own weighted radial norm, sqrt(sum_nodes w e^{8t + mu_a} b_j^2), computed in a cheap pre-pass: the '+out'
    # columns (coarse splines extended across t_+ by outer power laws) carry Vandermonde coefficients of size 1e4..1e8 and are 1e-4 at t = 13
    # where the weight is e^{88}; without this normalization the float Gram spans 1e34.
    SCALE = []
    t_pre = time.time()
    for cd in SEC.cols:
        col = cd["col"]; acc = 0.0
        for ic in col.pieces:
            s_nodes, t_nodes, w_nodes = NODES[ic]; ep = col.pieces[ic]
            for ai, s in enumerate(s_nodes):          # (not 'a': that is sys.argv here)
                v = ep_eval(ep, s); acc += w_nodes[ai] * math.exp(8 * t_nodes[ai] + mu_a(t_nodes[ai])) * v * v
        SCALE.append(math.sqrt(acc) if acc > 0 else 1.0)
    print("column scales (weighted radial norms): min %.2e max %.2e (%.0fs)" % (min(SCALE), max(SCALE), time.time() - t_pre), flush=True)
    for b_, (kind, lab, m, j0, jm) in enumerate(NEW):
        if kind == "jet": NEWMAT[j0, b_] = 1.0 / SCALE[j0]
        else: NEWMAT[jm, b_] = 1.0 / SCALE[jm]; NEWMAT[j0, b_] = -((-1.0) ** m) / SCALE[j0]
    CVEC = np.array([float(cd["col"].c.mid()) for cd in SEC.cols]) @ NEWMAT          # strain of the new basis columns (uncompensated h_0)
    nm = NMAX + 1
    from eta2 import A_half_fast
    AH = A_half_fast(nm - 2); M4, DIV = ang.div_cos4(nm)
    print("angular Gram: %d modes, eig min %.3e" % (nm - 2, np.linalg.eigvalsh(AH)[0]), flush=True)
    VM = {}
    for m in range(1, Mh):
        Gm = ang.factor_cos2m_modes(nm, m) - ((-1.0) ** m) * ang.x2y_modes(nm)
        q_, res = DIV(Gm)
        # exact quotient (verifier V189, 12:45Z): the cos^4 quotient of p (cos 2m theta - (-1)^m) has sine coefficients Q_j = 2 (-1)^(m-1-j) (2m-2j-1)
        # for 0 <= j < m and zero beyond (m = 1: [2]; m = 2: [-6, 2]; m = 3: [10, -6, 2]); the pinv value was padding dependent at the 1e-7 level (V187)
        qx = np.zeros(nm - 2); qx[:m] = [2.0 * ((-1) ** (m - 1 - j)) * (2 * m - 2 * j - 1) for j in range(m)]
        print("remainder angular factor m=%d: division residual %.2e; pinv quotient vs exact template: max diff %.2e (exact used)" % (m, res, float(np.max(np.abs(q_ - qx)))))
        VM[m] = qx
    np.savez(os.path.join(outdir, "prep.npz"), t=np.concatenate([n[1] for n in NODES]), d=np.concatenate(DV), dp=np.concatenate(DPV), H=np.concatenate(HH),
             cell_of_node=np.concatenate([np.full(len(n[0]), ic) for ic, n in enumerate(NODES)]))
    # the run's cell set, fixed here and recorded in meta.json (V188)
    cells_limit = (None if len(a) <= 7 else (a[7] if "," in a[7] else int(a[7])))
    if cells_limit is None: IDX_EXPECTED = list(range(CELLS.n))
    elif isinstance(cells_limit, str): IDX_EXPECTED = [int(x) for x in cells_limit.split(",")]
    else:
        step = max(1, CELLS.n // cells_limit)
        IDX_EXPECTED = sorted(set(list(range(0, CELLS.n, step))[:cells_limit]) | {0, 1, 4, CELLS.n - 2, CELLS.n - 1})
    # resume guard (verifier V196, 13:07Z): blocks accumulated across launches must come from the same producer settings
    SETTINGS = dict(mode=MODE, Mh=Mh, stride=stride, NMAX=NMAX, prec=PREC, drop=os.environ.get("FSEC_DROP", ""), out_shift=os.environ.get("BASIS_OUT_SHIFT", "0"), ncol=ncol, n_new=len(NEW))
    mpath = os.path.join(outdir, "meta.json")
    if os.path.exists(mpath):
        old = json.load(open(mpath)).get("settings")
        if old is not None and old != SETTINGS: raise SystemExit("resume with different settings: %s vs %s" % (old, SETTINGS))
    json.dump(dict(tag=tag, mode=MODE, Mh=Mh, stride=stride, NMAX=NMAX, nworkers=nw, prec=PREC, ncol=ncol, n_new=len(NEW), column_scales=SCALE, new=[(k_, l_, m_) for k_, l_, m_, _, _ in NEW], cvec=CVEC.tolist(),
                   cells_expected=[int(i) for i in IDX_EXPECTED], settings=SETTINGS,       # the run's cell set (V188): the assembler requires the union of the block done sets to equal it
                   dk=DK, k=str(k), c_l=str(c_l.str(20)), cKP=str(SEC.cKP.str(15)), build_seconds=time.time() - T0, labels=[cd["label"] for cd in SEC.cols], col_m=[cd["m"] for cd in SEC.cols]),
              open(os.path.join(outdir, "meta.json"), "w"), indent=1)
    idx = list(IDX_EXPECTED)
    # resume: merge every earlier checkpoint of this run into base accumulators and skip their cells (works with a different worker count)
    import glob
    base_GZ = np.zeros((len(NEW), len(NEW))); base_BY = np.zeros((len(NEW), len(NEW))); done_all = set(); base_diags = []
    # cells of earlier base blocks and of final parts of earlier launches are done as well (12:40Z, lead note 38 item 4): they are not merged
    # again (their blocks stay on disk as disjoint summands for fsec_assemble.py) but excluded from the new cell list
    prev_done = set()
    for f in sorted(glob.glob(os.path.join(outdir, "base_*.npz")) + glob.glob(os.path.join(outdir, "part_*.npz"))):
        zp = np.load(f, allow_pickle=True)
        if "done" in zp.files: prev_done |= set(int(x) for x in zp["done"])
        else: raise SystemExit("resume: %s has no done set (run older than 12:40Z): assemble it as it stands, do not resume" % f)
    for f in sorted(glob.glob(os.path.join(outdir, "ckpt_*.npz"))):
        zc = np.load(f, allow_pickle=True); dset = set(int(x) for x in zc["done"]) - prev_done
        if not dset: continue
        assert dset == set(int(x) for x in zc["done"]), "checkpoint overlaps earlier blocks: " + f
        base_GZ += zc["GZ"]; base_BY += zc["BY"]; done_all |= dset; base_diags.append(json.loads(str(zc["diag"])))
    for f in glob.glob(os.path.join(outdir, "part_*.npz")):      # parts of the earlier launch keep their name only if renamed: move them aside as blocks
        os.rename(f, f.replace("part_", "base_part%d_" % int(time.time())))
    if done_all:
        np.savez(os.path.join(outdir, "base_%d.npz" % int(time.time())), GZ=base_GZ, BY=base_BY, diag=json.dumps(base_diags), done=np.array(sorted(done_all)))
        for f in glob.glob(os.path.join(outdir, "ckpt_*.npz")): os.remove(f)
        print("resume: %d cells already done in earlier checkpoints (merged into base_*.npz)" % len(done_all), flush=True)
    idx = [ic for ic in idx if ic not in done_all and ic not in prev_done]
    chunks = [idx[w::nw] for w in range(nw)]
    print("sampling: %d cells over %d workers, %d columns -> %d new-basis columns, NMAX %d (build %.0fs)" % (len(idx), nw, ncol, len(NEW), NMAX, time.time() - T0), flush=True)
    mp.set_start_method("fork")
    with mp.Pool(nw) as pool:
        for wid, n, dt, diag in pool.imap_unordered(worker, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  worker %d done: %d cells in %.0fs; diag %s" % (wid, n, dt, diag), flush=True)
    print("DONE %.0fs" % (time.time() - T0), flush=True)
