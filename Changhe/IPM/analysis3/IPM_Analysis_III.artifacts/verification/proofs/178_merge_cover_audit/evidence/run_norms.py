"""Phase 2a (s2-num): exact squared Y-norms of the column images within the retained modes N <= Mout-1, over ALL cells
(for the within-mode part of (I - Q_M) L P_N).  Per column j: S_j = sum_{N<=Nmax} wY2(N) int (G_N^2 + G_N'^2) W_Y dt (exact, ball).
Far columns use the unit far images aggregated per velocity mode (TAU, KP aggregated over their 260 modes).
Usage: python3 run_norms.py <tag> <trial> Mh stride Mout stride_test nworkers [prec]   (same parameters as run_section.py)
Writes runs/<tag>/norms.json (per column: S_j as exact dyadic ball; TAU; KP).
"""
import sys, os, time, json
import multiprocessing as mp
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Operator
from basis import cutoff_chi
from section import Weights, Section, MomentCache, arb_dyadic
from run_section import FIX, HERE, load_ball


def norm2_of_img(mc, img, W, wY, W0Y):
    tot = arb(0)
    for N, ep in img.items():
        dep = ep.deriv()
        tot += W.wY2(N) * mc.integ(ep * ep + dep * dep, wY, W0Y)
    return tot


def cell_norms(S, ic):
    cl = S.cells.cells[ic]; mc = MomentCache(cl)
    W0Y, wY = S.W.cell_weight(cl, "Y"); Nmax = S.Mout - 1
    out = {}
    groups = [("col", [(ci_, cd["col"]) for ci_, cd in enumerate(S.cols)]), ("TAU", [("TAU", c) for c in S.TAU]), ("KP", [("KP", c) for c in S.KP])]
    far_coef = {}      # (store, cidx) -> {(n, which): coef}
    need_M = {}
    for store, lst in groups:
        for cidx, c in lst:
            key = (store, cidx)
            if ic in c.pieces:
                img = S.op.image(c, ic)
                if key in far_coef or key in need_M:
                    pass
                out[key] = out.get(key, arb(0)) + norm2_of_img(mc, img, S.W, wY, W0Y)
                # NOTE: for TAU/KP a mode piece may be in support while others are far; the far pieces are aggregated below
                # and their image must be added to this one before squaring: handle by collecting images instead
            else:
                fc = S.op.far_coefficients(c, ic)
                d = far_coef.setdefault(key if store == "col" else (store, store), {})
                for n, (al, be) in fc.items():
                    if al != 0: d[(n, "A")] = d.get((n, "A"), arb(0)) + al
                    if be != 0: d[(n, "B")] = d.get((n, "B"), arb(0)) + be
                if c.c != 0:
                    k2 = key if store == "col" else (store, store); need_M[k2] = need_M.get(k2, arb(0)) + c.c
    return out, far_coef, need_M


def strip_far_tail(img, S, cl):
    """on outer cells (t >= t_+) remove the degree-0 e^{alpha_0 sigma} term of every mode of a COMPENSATED image (identically zero by the
    definition of dk; checked to contain 0)."""
    if cl["kind"] not in ("outer", "pinf"): return img
    al0 = S.T.alpha_q[0]
    for N, ep in img.items():
        if al0 in ep.terms:
            cs = ep.terms[al0]
            assert cs[0].contains(arb(0)), ("far tail term not cancelled", N, cs[0].str(5))
            if len(cs) == 1: del ep.terms[al0]
            else: cs[0] = arb(0)
    return img


def cell_norms_full(S, ic):
    """exact squared Y-norms (modes N <= Nmax) on this cell of the COMPENSATED images: phi_j + dk_j KP for every basis column and TAU + dk_TAU KP."""
    cl = S.cells.cells[ic]; mc = MomentCache(cl)
    W0Y, wY = S.W.cell_weight(cl, "Y"); Nmax = S.Mout - 1
    imgs = {}
    def add_img(key, img, scale=None):
        cur = imgs.setdefault(key, {})
        for N, ep in img.items():
            e2 = ep if scale is None else ep.scale(scale)
            cur[N] = cur[N] + e2 if N in cur else e2
    far_coef = {}; need_M = {}
    for store, lst in [("col", [(ci_, cd["col"]) for ci_, cd in enumerate(S.cols)]), ("TAU", [("TAU", c) for c in S.TAU]), ("KP", [("KP", c) for c in S.KP])]:
        for cidx, c in lst:
            key = (store, cidx) if store == "col" else store
            if ic in c.pieces:
                add_img(key, S.op.image(c, ic))
            else:
                fc = S.op.far_coefficients(c, ic); d = far_coef.setdefault(key, {})
                for n, (al, be) in fc.items():
                    if al != 0: d[(n, "A")] = d.get((n, "A"), arb(0)) + al
                    if be != 0: d[(n, "B")] = d.get((n, "B"), arb(0)) + be
                if c.c != 0: need_M[key] = need_M.get(key, arb(0)) + c.c
    nset = sorted(set(n for d in far_coef.values() for (n, w_) in d))
    unit = S.op.far_unit_images(ic, nset) if nset else {}
    Mimg = {N: ep for N, ep in S.op.M_cached(ic).items() if N <= Nmax} if need_M else {}
    for key, d in far_coef.items():
        for (n, which), co in d.items():
            add_img(key, unit[n][0 if which == "A" else 1], co)
    for key, co in need_M.items(): add_img(key, Mimg, co)
    # compensation: dk_j = -c_j k / (3 c_l + k c_KP)
    k = S.T.k; c_l = S.op.c_l; denom = 3 * c_l + k * S.cKP
    imgKP = imgs.get("KP", {})
    out = {}
    for key, img in imgs.items():
        if key == "KP": continue
        cval = S.cols[key[1]]["col"].c if key[0] == "col" else S.cTAU
        dk = -cval * k / denom
        comp = {}
        for N, ep in img.items(): comp[N] = ep
        for N, ep in imgKP.items(): comp[N] = comp[N] + ep.scale(dk) if N in comp else ep.scale(dk)
        comp = strip_far_tail(comp, S, cl)
        out[key] = norm2_of_img(mc, comp, S.W, wY, W0Y)
    return out


def worker(args):
    wid, cells_idx, outdir = args
    ctx.prec = PREC; acc = {}; t0 = time.time(); last = t0
    for cnt, ic in enumerate(cells_idx):
        out = cell_norms_full(SEC, ic)
        for kk, v in out.items(): acc[kk] = acc[kk] + v if kk in acc else v
        if time.time() - last > 120:
            last = time.time()
            open(os.path.join(outdir, "nprogress_%d.txt" % wid), "w").write("%d/%d cells, %.0fs\n" % (cnt + 1, len(cells_idx), time.time() - t0))
    ser = [[list(map(str, kk)) if isinstance(kk, tuple) else [kk], arb_dyadic(v)] for kk, v in acc.items()]
    json.dump(ser, open(os.path.join(outdir, "npart_%d.json" % wid), "w"))
    return wid, len(cells_idx), time.time() - t0


if __name__ == "__main__":
    a = sys.argv
    tag, trial, Mh, stride, Mout, stride_test, nw = a[1], a[2], int(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7])
    PREC = int(a[8]) if len(a) > 8 else 256
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial.from_npz(FIX, prec=PREC) if trial == "fixture" else ExactTrial(prec=PREC)
    T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    full = set(cutoff_chi(T, cells).keys()) | set(ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf"))
    bg = Background(T, cells, nmax=Mout + Mh + 3, full_cells=full)
    k = T.k_q
    W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    SEC = Section(T, cells, bg, W, Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test, verbose=False)
    idx = list(range(cells.n)); chunks = [idx[w::nw] for w in range(nw)]
    print("norms: %d cells over %d workers (build %.0fs)" % (len(idx), nw, time.time() - T0), flush=True)
    mp.set_start_method("fork")
    with mp.Pool(nw) as pool:
        for wid, n, dt in pool.imap_unordered(worker, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  worker %d done: %d cells in %.0fs" % (wid, n, dt), flush=True)
    acc = {}
    for w in range(nw):
        for kk, q in json.load(open(os.path.join(outdir, "npart_%d.json" % w))):
            kk = tuple(kk); v = load_ball(q); acc[kk] = acc[kk] + v if kk in acc else v
    res = {"|".join(kk): arb_dyadic(v) for kk, v in acc.items()}
    res_f = {"|".join(kk): [float(v.mid()), float(v.rad())] for kk, v in acc.items()}
    json.dump(dict(exact=res, float=res_f, Nmax=Mout - 1, note="COMPENSATED columns phi_j + dk_j KP (and TAU + dk KP): sum_{N<=Nmax} wY2 int (G_N^2 + G_N'^2) W_Y dt over all cells; the cancelled far term is stripped with a containment check"), open(os.path.join(outdir, "norms.json"), "w"), indent=1)
    print("saved norms.json; total %.0fs" % (time.time() - T0))
