"""Parallel exact assembly of the L_fix section in the lead's L^2(e^{mu~}) norm (section_l2.py).
Usage: python3 run_section_l2.py <tag> <trial: exact|fixture> Mh stride Mout stride_test nworkers [prec] [cells_limit]
"""
import sys, os, time, json, gzip
import multiprocessing as mp
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial
from section_l2 import CellsL2, BackgroundL2, SectionL2, MU_KNOTS
from section import arb_dyadic
from run_section import FIX, HERE, load_ball


def worker(args):
    wid, cells_idx, outdir = args
    ctx.prec = PREC
    acc = dict(GX={}, GY={}, rows={}); t0 = time.time(); last = t0
    for cnt, ic in enumerate(cells_idx):
        out = SEC.cell_contrib(ic)
        for key in acc:
            d = acc[key]
            for kk, v in out[key].items(): d[kk] = d[kk] + v if kk in d else v
        if time.time() - last > 120:
            last = time.time(); open(os.path.join(outdir, "progress_%d.txt" % wid), "w").write("%d/%d cells, %.0fs\n" % (cnt + 1, len(cells_idx), time.time() - t0))
    ser = {key: [[list(map(str, kk)), arb_dyadic(v)] for kk, v in d.items()] for key, d in acc.items()}
    json.dump(ser, open(os.path.join(outdir, "part_%d.json" % wid), "w"))
    return wid, len(cells_idx), time.time() - t0


if __name__ == "__main__":
    a = sys.argv
    tag, trial, Mh, stride, Mout, stride_test, nw = a[1], a[2], int(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7])
    PREC = int(a[8]) if len(a) > 8 else 256
    cells_limit = int(a[9]) if len(a) > 9 else None
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial.from_npz(FIX, prec=PREC) if trial == "fixture" else ExactTrial(prec=PREC)
    T.build_green(verbose=True)
    inner_extra = [fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)]
    outer_extra = sorted(set([fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)] + [k - T.t_hi_q for k in MU_KNOTS if k > T.t_hi_q]))
    split_at = [k for k in MU_KNOTS if T.t_lo_q < k < T.t_hi_q]
    cells = CellsL2(T, inner_extra, outer_extra, split_at)
    bg = BackgroundL2(T, cells, nmax=Mout + Mh + 3)
    SEC = SectionL2(T, cells, bg, Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test)
    meta = dict(tag=tag, trial=("npz fixture" if trial == "fixture" else "exact modal trial modal_v2.json + z"), sha=T.sha, prec=PREC, operator="L_fix (no strain term)",
                norm="L2(e^{8t + mu~(t)} dt dtheta) spatial, lead note 5 weight", Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test, q=SEC.q,
                ncells=cells.n, ncol=SEC.ncol, ntest=SEC.ntest, test_active=SEC.ts.active, columns=[dict(m=cd["m"], label=cd["label"]) for cd in SEC.cols],
                k=str(T.k_q), c_l=str(1 / T.k_q), mu_knots=[str(x) for x in MU_KNOTS], cell_bounds=[str(cl["tq"]) for cl in cells.cells], cell_kinds=[cl["kind"] for cl in cells.cells],
                test_knots=[str(x) for x in SEC.ts.bounds], build_seconds=time.time() - T0)
    json.dump(meta, open(os.path.join(outdir, "meta.json"), "w"), indent=1)
    idx = list(range(cells.n)) if cells_limit is None else list(range(0, cells.n, max(1, cells.n // cells_limit)))[:cells_limit]
    chunks = [idx[w::nw] for w in range(nw)]
    print("assembly: %d cells over %d workers (build %.0fs)" % (len(idx), nw, time.time() - T0), flush=True)
    mp.set_start_method("fork")
    with mp.Pool(nw) as pool:
        for wid, n, dt in pool.imap_unordered(worker, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  worker %d done: %d cells in %.0fs" % (wid, n, dt), flush=True)
    acc = dict(GX={}, GY={}, rows={})
    for w in range(nw):
        ser = json.load(open(os.path.join(outdir, "part_%d.json" % w)))
        for key, lst in ser.items():
            d = acc[key]
            for kk, q in lst:
                kk = tuple(int(x) for x in kk); v = load_ball(q); d[kk] = d[kk] + v if kk in d else v
    with gzip.open(os.path.join(outdir, "matrices_dyadic.json.gz"), "wt") as f:
        json.dump({key: {"|".join(map(str, kk)): arb_dyadic(v) for kk, v in d.items()} for key, d in acc.items()}, f)
    ncol = SEC.ncol; nt = SEC.ntest
    def tomat(d, shape, keyfun):
        mid = np.zeros(shape); rad = np.zeros(shape)
        for kk, v in d.items():
            i = keyfun(kk); mid[i] = float(v.mid()); rad[i] = float(v.rad())
        return mid, rad
    GXm, GXr = tomat(acc["GX"], (ncol, ncol), lambda kk: (kk[0], kk[1])); GYm, GYr = tomat(acc["GY"], (nt, nt), lambda kk: (kk[0], kk[1]))
    Bm, Br = tomat(acc["rows"], (Mout * nt, ncol), lambda kk: (kk[0] * nt + kk[1], kk[2]))
    np.savez(os.path.join(outdir, "matrices.npz"), GX_mid=GXm, GX_rad=GXr, GY_mid=GYm, GY_rad=GYr, B_mid=Bm, B_rad=Br, col_m=np.array([cd["m"] for cd in SEC.cols]), col_label=np.array([cd["label"] for cd in SEC.cols]))
    print("saved; max GX rad %.2e, max B rad %.2e, max |B| %.3e; total %.0fs" % (GXr.max(), Br.max(), np.abs(Bm).max(), time.time() - T0), flush=True)
