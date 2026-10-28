"""Phase 2b driver (s2-num): rigorous upper bounds D_j for the dropped output modes N > Nmax of every column image.
Phase A (parallel over cells): background tables (float64 UPPER bounds, rounded outward):
   SUP[ic, n-1, 0:4] = sup|Pe_n|, sup|Pe_n'|, sup|Qe_n|, sup|Qe_n'| on cell ic (all n = 1..Nf);
   NRM[ic, j, 0:4]   = ||dR_j||_{H1_W}, ||dR_j||_{L2_W}, ||Rhat_j||_{H1_W}, ||Rhat_j||_{L2_W} (Y weight of the cell).
Phase B (parallel over columns): D_j^2 >= sum_{N>Nmax} wY2(N) ||G_N||^2 via the l^1 majorant
   sqrt(sum_N wY2(N) ||G_N||^2) <= sum_N sqrt(wY2(N)) ||G_N|| <= sum_terms (f+1) * term_bound   (f = 2N+1 the sine frequency, wY2 = 1 + f^2 <= (f+1)^2),
with the term bounds of tailbound.py; computed in ball arithmetic from the float upper bounds (exact conversion).
Usage: python3 run_tailbound.py <tag> <trial> Mh stride Mout stride_test nworkers [prec]
"""
import sys, os, time, json
import multiprocessing as mp
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Operator
from basis import cutoff_chi
from section import Weights, Section, MomentCache, arb_dyadic
from tailbound import sup_bound, h1_norm2, l2_norm2
from run_section import FIX, HERE


def up(x):
    return float(x.upper())


def workerA(args):
    wid, cells_idx, outdir = args
    ctx.prec = PREC
    Nf = SEC.T.Nf; Mj = SEC.T.Mj
    SUP = np.zeros((len(cells_idx), Nf, 4)); NRM = np.zeros((len(cells_idx), Mj, 4)); t0 = time.time()
    for kk, ic in enumerate(cells_idx):
        d = SEC.bg.get(ic); cl = SEC.cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = SEC.W.cell_weight(cl, "Y")
        for ni in range(Nf):
            sP, sdP = sup_bound(d["Pe"][ni], cl); sQ, sdQ = sup_bound(d["Qe"][ni], cl)
            SUP[kk, ni] = [up(sP), up(sdP), up(sQ), up(sdQ)]
        for j in range(Mj):
            dR = d["dR"][j]; R = d["Rhat"][j]
            NRM[kk, j] = [up(h1_norm2(dR, mc, wY, W0Y).sqrt()), up(l2_norm2(dR, mc, wY, W0Y).sqrt()), up(h1_norm2(R, mc, wY, W0Y).sqrt()), up(l2_norm2(R, mc, wY, W0Y).sqrt())]
        if kk % 20 == 0: open(os.path.join(outdir, "tprogressA_%d.txt" % wid), "w").write("%d/%d cells %.0fs\n" % (kk + 1, len(cells_idx), time.time() - t0))
    np.savez(os.path.join(outdir, "tablesA_%d.npz" % wid), idx=np.array(cells_idx), SUP=SUP, NRM=NRM)
    return wid, time.time() - t0


def workerB(args):
    wid, col_list, outdir = args
    ctx.prec = PREC
    T = SEC.T; cells = SEC.cells; Nmax = SEC.Mout - 1; Mj = T.Mj; Nf = T.Nf
    res = {}
    t0 = time.time()
    for cidx, colobj in col_list:
        m = colobj.m
        Pj = {j: q2arb(T.P_q[j, m]) for j in range(Mj) if T.P_q[j, m] != 0}
        tot = arb(0)       # l^1 majorant sum_terms (f+1) bound_term over dropped frequencies
        # (b) on the support cells
        for ic, b in colobj.pieces.items():
            cl = cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = SEC.W.cell_weight(cl, "Y")
            bt = b.scale(arb(3)) + b.deriv()
            nb1 = h1_norm2(bt, mc, wY, W0Y).sqrt(); nb0 = l2_norm2(bt, mc, wY, W0Y).sqrt()
            nb1b = h1_norm2(b, mc, wY, W0Y).sqrt(); nb0b = l2_norm2(b, mc, wY, W0Y).sqrt()
            S_ = SUPT[ic]
            for n in range(1, Nf + 1):
                sPe, sdPe, sQe, sdQe = (arb(float(x)) for x in S_[n - 1])
                for j, pj in Pj.items():
                    v1 = abs(pj) / 2 * (sPe * nb1 + sdPe * nb0); v2 = abs(pj) * (2 * j + 1) / 2 * (sQe * nb1b + sdQe * nb0b)
                    for f in (2 * j + 1 + 2 * n, abs(2 * j + 1 - 2 * n)):
                        if f > 2 * Nmax + 1: tot += (f + 1) * v1
                    for f in (2 * n + 2 * j + 1, abs(2 * n - 2 * j - 1)):
                        if f > 2 * Nmax + 1: tot += (f + 1) * v2
        # (c) all cells, prefix sums over the background modes j: terms with f = 2j+1+2n > 2Nmax+1 (j >= Nmax - n + 1 ... always for j > Nmax)
        #     and f = |2j+1-2n| > 2Nmax+1 (j > Nmax + n or j < n - Nmax - 1). Bound every j in those ranges.
        for ic, cl in enumerate(cells.cells):
            Ah, Bh = colobj.green_on_cell(ic); em2a = (-2 * cl["ta"]).exp()
            for n in colobj.hmodes:
                Peh = (Ah[n] + Bh[n]).scale(em2a / 2).mul_exp(fmpq(-2)); Qeh = (Bh[n] - Ah[n]).scale(em2a / 2).mul_exp(fmpq(-2))
                if not Peh.terms and not Qeh.terms: continue
                sP, sdP = sup_bound(Peh, cl) if Peh.terms else (arb(0), arb(0))
                sQ, sdQ = sup_bound(Qeh, cl) if Qeh.terms else (arb(0), arb(0))
                # frequency 2j+1+2n: weight (2j+2n+2); dropped iff j + n > Nmax  -> j >= max(0, Nmax - n + 1)
                j0 = max(0, Nmax - n + 1)
                # sums over j >= j0 of (2j+2) x_j and x_j for x = ndR1, ndR0, (2j+1) nR1, (2j+1) nR0  (precomputed cumulative tables)
                c1 = CUM[ic]
                def tail_sum(j0, which):
                    # returns (sum_{j>=j0} (2j+2) x_j, sum_{j>=j0} x_j) as arb from float cumulative upper bounds
                    return arb(float(c1[which][0][j0])), arb(float(c1[which][1][j0]))
                for which, s1, s2 in (("dR1", sP, None), ("dR0", sdP, None)):
                    A2, A0 = tail_sum(j0, which)
                    tot += (A2 + 2 * n * A0) * s1 / 2
                for which, s1 in (("R1", sQ), ("R0", sdQ)):
                    A2, A0 = tail_sum(j0, which)
                    tot += (A2 + 2 * n * A0) * s1 / 2
                # frequency |2j+1-2n| > 2Nmax+1: j > Nmax + n (weight 2j+2-2n <= 2j+2) or j < n - Nmax - 1 (weight 2n - 2j)
                j1 = Nmax + n + 1
                for which, s1 in (("dR1", sP), ("dR0", sdP)):
                    A2, A0 = tail_sum(j1, which); tot += A2 * s1 / 2
                for which, s1 in (("R1", sQ), ("R0", sdQ)):
                    A2, A0 = tail_sum(j1, which); tot += A2 * s1 / 2
                for j in range(0, n - Nmax - 1):
                    f = 2 * n - 2 * j - 1
                    x = NRMT[ic][j]
                    tot += (f + 1) * (sP * arb(float(x[0])) + sdP * arb(float(x[1]))) / 2 + (f + 1) * (2 * j + 1) * (sQ * arb(float(x[2])) + sdQ * arb(float(x[3]))) / 2
        # (d) strain term: (c/3) dR_N for N > Nmax, all cells
        if colobj.c != 0:
            for ic in range(cells.n):
                c1 = CUM[ic]; A2, A0 = arb(float(c1["dR1"][0][Nmax + 1])), arb(float(c1["dR1"][1][Nmax + 1]))
                tot += abs(colobj.c) / 3 * A2       # sum_{N>Nmax} (2N+2) ||dR_N||  (f+1 = 2N+2)
        res[str(cidx)] = arb_dyadic(tot * tot)
        res[str(cidx) + "_float"] = up(tot * tot)
    json.dump(res, open(os.path.join(outdir, "tpartB_%d.json" % wid), "w"))
    return wid, time.time() - t0


if __name__ == "__main__":
    a = sys.argv
    tag, trial, Mh, stride, Mout, stride_test, nw = a[1], a[2], int(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7])
    PREC = int(a[8]) if len(a) > 8 else 256
    outdir = os.path.join(HERE, "runs", tag); os.makedirs(outdir, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial.from_npz(FIX, prec=PREC) if trial == "fixture" else ExactTrial(prec=PREC)
    T.build_green(verbose=False)
    cells = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, cells, nmax=None)        # all modes everywhere
    k = T.k_q
    W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    SEC = Section(T, cells, bg, W, Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test, verbose=False)
    print("tailbound: build %.0fs; cells %d, columns %d" % (time.time() - T0, cells.n, SEC.ncol), flush=True)
    mp.set_start_method("fork")
    idx = list(range(cells.n)); chunks = [idx[w::nw] for w in range(nw)]
    with mp.Pool(nw) as pool:
        for wid, dt in pool.imap_unordered(workerA, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  A worker %d done (%.0fs)" % (wid, dt), flush=True)
    Nf = T.Nf; Mj = T.Mj
    SUPT = np.zeros((cells.n, Nf, 4)); NRMT = np.zeros((cells.n, Mj, 4))
    for w in range(nw):
        z = np.load(os.path.join(outdir, "tablesA_%d.npz" % w)); SUPT[z["idx"]] = z["SUP"]; NRMT[z["idx"]] = z["NRM"]
    np.savez(os.path.join(outdir, "tablesA.npz"), SUP=SUPT, NRM=NRMT)
    # cumulative (reverse) sums over j of (2j+2) x_j and x_j, as float upper bounds (summation in float rounds; add a relative safety 1e-12 per term count)
    CUM = []
    for ic in range(cells.n):
        d = {}
        for which, col in (("dR1", 0), ("dR0", 1), ("R1", 2), ("R0", 3)):
            x = NRMT[ic, :, col].astype(float)
            w2 = (2 * np.arange(Mj) + 2) * x
            if which in ("R1", "R0"): x = (2 * np.arange(Mj) + 1) * x; w2 = (2 * np.arange(Mj) + 2) * x
            c2 = np.concatenate([np.cumsum(w2[::-1])[::-1], [0.0]]) * (1 + 1e-10); c0 = np.concatenate([np.cumsum(x[::-1])[::-1], [0.0]]) * (1 + 1e-10)
            d[which] = (c2, c0)
        CUM.append(d)
    cols = [(ci_, cd["col"]) for ci_, cd in enumerate(SEC.cols)] + [("TAU_m%d" % c.m, c) for c in SEC.TAU] + [("KP_m%d" % c.m, c) for c in SEC.KP]
    chunksB = [cols[w::nw] for w in range(nw)]
    with mp.Pool(nw) as pool:
        for wid, dt in pool.imap_unordered(workerB, [(w, chunksB[w], outdir) for w in range(nw)]):
            print("  B worker %d done (%.0fs)" % (wid, dt), flush=True)
    res = {}
    for w in range(nw): res.update(json.load(open(os.path.join(outdir, "tpartB_%d.json" % w))))
    json.dump(dict(Nmax=Mout - 1, D2_upper=res, note="D_j^2 >= sum_{N>Nmax} wY2(N) ||G_N||^2_{H1_W} (l^1 majorant, float tables are outward upper bounds; TAU_m*, KP_m* are the single-mode pieces: the bound for TAU (KP) is (sum_m sqrt(D2))^2)"), open(os.path.join(outdir, "tailbound.json"), "w"), indent=1)
    print("saved tailbound.json; total %.0fs" % (time.time() - T0))
