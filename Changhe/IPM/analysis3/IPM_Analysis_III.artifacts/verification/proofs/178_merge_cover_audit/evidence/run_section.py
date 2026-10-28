"""Parallel exact assembly of a finite section (s2-num).
Usage: python3 run_section.py <tag> <trial: exact|fixture> Mh stride Mout stride_test nworkers [prec] [cells_limit]
Writes work/runs/<tag>/{meta.json, part_*.json, matrices.npz, matrices_dyadic.json.gz}.
"""
import sys, os, time, json, gzip, math
import multiprocessing as mp
from flint import arb, arb_mat, fmpq, fmpz, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Column, Operator
from basis import cutoff_chi
from section import Weights, Section, arb_dyadic

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT_SEC = float(os.environ.get("CKPT_SEC", "300"))
FIX = os.path.join(HERE, "..", "research_copy", "analysis1", "IPM_Analysis_I.artifacts", "numerics", "data", "trial_small_M20.npz")


def load_ball(q):
    man, ex, rman, rex = q
    with_prec = ctx.prec; ctx.prec = max(with_prec, 1500)
    mid = arb(fmpz(int(man))) * (arb(2) ** int(ex))
    rad = (arb(fmpz(int(rman))) * (arb(2) ** int(rex))) if int(rman) != 0 else arb(0)
    ctx.prec = with_prec
    return mid + (arb(0, float(rad.upper()) * (1 + 2.0 ** -40) + 2.0 ** -1000) if int(rman) != 0 else arb(0))


def ser_acc(acc):
    return {key: [[list(map(str, kk)), arb_dyadic(v)] for kk, v in d.items()] for key, d in acc.items()}


def deser_acc(ser, acc):
    for key, lst in ser.items():
        d = acc[key]
        for kk, q in lst:
            kk = tuple(int(x) if x.lstrip("-").isdigit() else x for x in kk)
            v = load_ball(q); d[kk] = d[kk] + v if kk in d else v


def worker(args):
    """One worker: accumulates its cells; checkpoints (acc + done cells) to ckpt_<wid>.json every CKPT_SEC seconds and
    resumes from an existing checkpoint (cells listed there are skipped; their contributions are loaded as balls)."""
    wid, cells_idx, outdir = args
    ctx.prec = PREC
    acc = dict(GX={}, GY={}, rows={}, rows_tau={}, rows_kp={})
    done = set()
    ck = os.path.join(outdir, "ckpt_%d.json" % wid)
    if os.path.exists(ck):
        try:
            c = json.load(open(ck)); deser_acc(c["acc"], acc); done = set(c["done"])
            print("  worker %d resumed from checkpoint: %d cells done" % (wid, len(done)), flush=True)
        except Exception as e:
            print("  worker %d: checkpoint unreadable (%s), starting from scratch" % (wid, e), flush=True)
            acc = dict(GX={}, GY={}, rows={}, rows_tau={}, rows_kp={}); done = set()
    t0 = time.time(); last = t0; lastck = t0
    for cnt, ic in enumerate(cells_idx):
        if ic in done: continue
        out = SEC.cell_contrib(ic, want_norms=False)
        for key in acc:
            d = acc[key]
            for kk, v in out[key].items(): d[kk] = d[kk] + v if kk in d else v
        done.add(ic)
        if time.time() - last > 120:
            last = time.time()
            with open(os.path.join(outdir, "progress_%d.txt" % wid), "w") as f: f.write("%d/%d cells, %.0fs\n" % (len(done), len(cells_idx), time.time() - t0))
        if time.time() - lastck > CKPT_SEC:
            lastck = time.time()
            tmp = ck + ".tmp"
            with open(tmp, "w") as f: json.dump(dict(acc=ser_acc(acc), done=sorted(done)), f)
            os.replace(tmp, ck)
    ser = ser_acc(acc)
    with open(os.path.join(outdir, "part_%d.json" % wid), "w") as f: json.dump(ser, f)
    return wid, len(cells_idx), time.time() - t0


if __name__ == "__main__":
    a = sys.argv
    tag, trial, Mh, stride, Mout, stride_test, nw = a[1], a[2], int(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7])
    PREC = int(a[8]) if len(a) > 8 else 256
    cells_limit = int(a[9]) if len(a) > 9 else None
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    ctx.prec = PREC
    T0 = time.time()
    T = ExactTrial.from_npz(FIX, prec=PREC) if trial == "fixture" else ExactTrial(prec=PREC)
    T.build_green(verbose=True)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    full = set(cutoff_chi(T, cells).keys()) | set(ic for ic, cl in enumerate(cells.cells) if cl["kind"] in ("outer", "pinf"))
    bg = Background(T, cells, nmax=Mout + Mh + 3, full_cells=full)
    k = T.k_q
    W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    SEC = Section(T, cells, bg, W, Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test)
    meta = dict(tag=tag, trial=("npz fixture trial_small_M20" if trial == "fixture" else "exact modal trial modal_v2.json + z"), sha=T.sha, prec=PREC,
                Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test, q=SEC.q, ncells=cells.n, ncol=SEC.ncol, ntest=SEC.ntest,
                weights=dict(eps0X=str(W.eps0X), gammaX=str(W.gammaX), sX=W.sX, eps0Y=str(W.eps0Y), gammaY=str(W.gammaY), sY=W.sY),
                columns=[dict(m=cd["m"], label=cd["label"], c=arb_dyadic(cd["col"].c)) for cd in SEC.cols],
                cTAU=arb_dyadic(SEC.cTAU), cKP=arb_dyadic(SEC.cKP), k=str(T.k_q), c_l=str(1 / T.k_q),
                test_knots=[str(x) for x in SEC.ts.bounds], cell_bounds=[str(cl["tq"]) for cl in cells.cells], cell_kinds=[cl["kind"] for cl in cells.cells],
                inner_extra="1/2,1,2,4", outer_extra="1/2,1,2,4,8", build_seconds=time.time() - T0)
    json.dump(meta, open(os.path.join(outdir, "meta.json"), "w"), indent=1)
    idx = list(range(cells.n)) if cells_limit is None else list(range(0, cells.n, max(1, cells.n // cells_limit)))[:cells_limit]
    chunks = [idx[w::nw] for w in range(nw)]
    print("assembly: %d cells over %d workers (build %.0fs)" % (len(idx), nw, time.time() - T0), flush=True)
    mp.set_start_method("fork")
    with mp.Pool(nw) as pool:
        for wid, n, dt in pool.imap_unordered(worker, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  worker %d done: %d cells in %.0fs" % (wid, n, dt), flush=True)
    # reduce
    t0 = time.time()
    acc = dict(GX={}, GY={}, rows={}, rows_tau={}, rows_kp={})
    for w in range(nw):
        deser_acc(json.load(open(os.path.join(outdir, "part_%d.json" % w))), acc)
    ncol = SEC.ncol; nt = SEC.ntest; Mout = SEC.Mout
    def dump(name, d):
        return {"|".join(map(str, kk)): arb_dyadic(v) for kk, v in d.items()}
    with gzip.open(os.path.join(outdir, "matrices_dyadic.json.gz"), "wt") as f:
        json.dump({key: dump(key, d) for key, d in acc.items()}, f)
    import numpy as np
    def tomat(d, shape, keyfun):
        mid = np.zeros(shape); rad = np.zeros(shape)
        for kk, v in d.items():
            i = keyfun(kk); mid[i] = float(v.mid()); rad[i] = float(v.rad())
        return mid, rad
    GXm, GXr = tomat(acc["GX"], (ncol, ncol), lambda kk: (kk[0], kk[1]))
    GYm, GYr = tomat(acc["GY"], (nt, nt), lambda kk: (kk[0], kk[1]))
    Bm, Br = tomat(acc["rows"], (Mout * nt, ncol), lambda kk: (kk[0] * nt + kk[1], kk[2]))
    BTm, BTr = tomat(acc["rows_tau"], (Mout * nt, 1), lambda kk: (kk[0] * nt + kk[1], 0))
    BKm, BKr = tomat(acc["rows_kp"], (Mout * nt, 1), lambda kk: (kk[0] * nt + kk[1], 0))
    np.savez(os.path.join(outdir, "matrices.npz"), GX_mid=GXm, GX_rad=GXr, GY_mid=GYm, GY_rad=GYr, B_mid=Bm, B_rad=Br, BTAU_mid=BTm, BTAU_rad=BTr, BKP_mid=BKm, BKP_rad=BKr,
             c_mid=np.array([float(cd["col"].c.mid()) for cd in SEC.cols]), c_rad=np.array([float(cd["col"].c.rad()) for cd in SEC.cols]),
             cTAU=float(SEC.cTAU.mid()), cKP=float(SEC.cKP.mid()), col_m=np.array([cd["m"] for cd in SEC.cols]), col_label=np.array([cd["label"] for cd in SEC.cols]))
    print("reduced and saved (%.0fs); max GX rad %.2e, max B rad %.2e, max |B| %.3e; total %.0fs" % (time.time() - t0, GXr.max(), Br.max(), np.abs(Bm).max(), time.time() - T0), flush=True)
