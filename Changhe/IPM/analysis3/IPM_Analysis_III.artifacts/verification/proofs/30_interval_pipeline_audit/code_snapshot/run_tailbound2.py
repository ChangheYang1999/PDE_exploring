"""Phase 2b, version 2 (s2-num): rigorous upper bound E_j^> of the dropped-mode energy sum_{N > Nmax} wY2(N) ||G_N||^2_{H1_W} for every
COMPENSATED column u_j = phi_j + dk_j KP (and TAU + dk_TAU KP).
Bound structure: for each dropped mode N and each cell c, b[N, c] >= ||G_N||_{H1_W(cell c)} (sum of term bounds, triangle inequality);
then E^> <= sum_N wY2(N) sum_c b[N, c]^2 (l^2 over the orthogonal modes and the disjoint cells; astra round offbasis, Claim D).
Term bounds on a cell: ||f g|| <= sup|f| ||g||_{H1} + sup|f'| ||g||_{L2} (sup bounds of exponential polynomials by coefficient sums), except on
the outer half-line cell where the background density modes have infinite weighted norm: there every product is integrated exactly.
Terms: (a) transport self (only the TAU/KP pieces reach N > Nmax; on the outer cells TAU's is exactly 0 and KP's e^{(k-3)t} part cancels the
strain term's: joint treatment (d)); (b) background velocity modes acting on the column; (c) the column's velocity on the background;
(d) joint strain/KP-transport term: (C/3) dR_N^rem + dk T_N^cut(KP), dR_N^rem = dR_N without its e^{alpha_0 t} degree-0 part on t >= t_+.
Floats are upper bounds: every float addition/multiplication of nonnegative upper bounds is followed by the factor (1 + 2^-50) (round-up allowance).
Usage: python3 run_tailbound2.py <tag> <trial> Mh stride Mout stride_test nworkers [prec]
"""
import sys, os, time, json
import multiprocessing as mp
import numpy as np
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Operator, addsin
from basis import cutoff_chi
from section import Weights, Section, MomentCache, arb_dyadic
from tailbound import sup_bound, h1_norm2, l2_norm2
from run_section import FIX, HERE

FUDGE = 1 + 2.0 ** -50


def up(x): return float(x.upper())


def h1n(ep, mc, w, W0): return up(h1_norm2(ep, mc, w, W0).sqrt())
def l2n(ep, mc, w, W0): return up(l2_norm2(ep, mc, w, W0).sqrt())


def strip_alpha0(ep, al0):
    """copy of ep without the degree-0 coefficient of the exponent alpha_0 term"""
    r = ExpPoly()
    for e, cs in ep.terms.items():
        if e == al0:
            cs2 = list(cs); cs2[0] = arb(0)
            if any(x != 0 for x in cs2): r.add(e, cs2)
        else: r.add(e, cs)
    return r


def workerA(args):
    """per cell: SUP[n] (4 sup bounds of Pe_n, Qe_n and derivatives), NRM[j] (4 norms of dR_j, Rhat_j: H1, L2), NRMREM[j] (H1 norm of dR_j^rem),
    TK[N], TT[N] (H1 norms of the transport-self images of KP and TAU in mode N; KP's alpha_0 degree-0 part removed on outer cells)."""
    wid, cells_idx, outdir = args
    ctx.prec = PREC; T = SEC.T; Nf = T.Nf; Mj = T.Mj; al0 = T.alpha_q[0]
    SUP = np.zeros((len(cells_idx), Nf, 4)); NRM = np.full((len(cells_idx), Mj, 4), np.inf); NRMREM = np.zeros((len(cells_idx), Mj))
    TK = np.zeros((len(cells_idx), Mj)); TT = np.zeros((len(cells_idx), Mj)); t0 = time.time()
    for kk, ic in enumerate(cells_idx):
        d = SEC.bg.get(ic); cl = SEC.cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = SEC.W.cell_weight(cl, "Y")
        outer = cl["kind"] in ("outer", "pinf")
        for ni in range(Nf):
            sP, sdP = sup_bound(d["Pe"][ni], cl); sQ, sdQ = sup_bound(d["Qe"][ni], cl)
            SUP[kk, ni] = [up(sP), up(sdP), up(sQ), up(sdQ)]
        for j in range(Mj):
            dR = d["dR"][j]; R = d["Rhat"][j]
            if cl["kind"] not in ("minf", "pinf"):
                NRM[kk, j] = [h1n(dR, mc, wY, W0Y), l2n(dR, mc, wY, W0Y), h1n(R, mc, wY, W0Y), l2n(R, mc, wY, W0Y)]
            if j > SEC.Mout - 1:          # only the dropped modes need the strain-term norms; j <= 1 carries the x^2 y constant (infinite on the inner half-line)
                NRMREM[kk, j] = h1n(strip_alpha0(dR, al0) if outer else dR, mc, wY, W0Y)
        # transport-self images of the KP and TAU pieces living on this cell, summed into sine modes
        for lst, arr in ((SEC.KP, TK), (SEC.TAU, TT)):
            acc = {}
            for c in lst:
                if ic in c.pieces:
                    for N, ep in SEC.op.transport_self(c.pieces[ic], c.m, c.Pcol).items(): addsin(acc, 2 * N + 1, ep)
            for N, ep in acc.items():
                if N < Mj:
                    e2 = strip_alpha0(ep, al0) if outer else ep
                    if e2.terms:
                        if outer and lst is SEC.TAU:
                            assert all(x.contains(arb(0)) for cs in e2.terms.values() for x in cs), "TAU transport on outer cell must vanish"
                            continue
                        arr[kk, N] = h1n(e2, mc, wY, W0Y)
        if kk % 20 == 0: open(os.path.join(outdir, "t2progressA_%d.txt" % wid), "w").write("%d/%d cells %.0fs\n" % (kk + 1, len(cells_idx), time.time() - t0))
    np.savez(os.path.join(outdir, "t2tablesA_%d.npz" % wid), idx=np.array(cells_idx), SUP=SUP, NRM=NRM, NRMREM=NRMREM, TK=TK, TT=TT)
    return wid, time.time() - t0


def add_terms_sup(BND, ic, cl, n, sP, sdP, sQ, sdQ, j_list_vals, Nmax, Mj):
    """(c)-type terms with sup bounds on a finite cell: for every background mode j, bound (sP n1_j + sdP n0_j)/2 at frequencies 2j+1 +- 2n and
    (2j+1)(sQ r1_j + sdQ r0_j)/2 at 2n +- (2j+1). j_list_vals: NRM[ic] (Mj x 4)."""
    j = np.arange(Mj); x = j_list_vals
    v1 = (sP * x[:, 0] + sdP * x[:, 1]) / 2 * FUDGE; v2 = (2 * j + 1) * (sQ * x[:, 2] + sdQ * x[:, 3]) / 2 * FUDGE
    for f in (2 * j + 1 + 2 * n, np.abs(2 * j + 1 - 2 * n)):
        N = (f - 1) // 2; sel = (N > Nmax) & (f > 0)
        np.add.at(BND[:, ic], N[sel], v1[sel])
    for f in (2 * n + 2 * j + 1, np.abs(2 * n - 2 * j - 1)):
        N = (f - 1) // 2; sel = (N > Nmax) & (f > 0)
        np.add.at(BND[:, ic], N[sel], v2[sel])


def exact_terms_pinf(BND, ic, mc, wY, W0Y, Pe, Qe, g1, g0, Pj_or_coef, Nmax, modeflag):
    """exact (c)/(b)-type products on the outer half-line cell. modeflag='c': terms -(1/2) Pe dR_j, (1/2) Qe (2j+1) Rhat_j over background modes j
    (Pj_or_coef = (dR list, Rhat list)); modeflag='b': terms with the column radial functions g1 = (3b+b'), g0 = b and coefficients P_jm."""
    pass


def workerB(args):
    wid, items, outdir = args
    ctx.prec = PREC; T = SEC.T; cells = SEC.cells; Nmax = SEC.Mout - 1; Mj = T.Mj; Nf = T.Nf; al0 = T.alpha_q[0]
    half = {}
    for ih in (0, cells.n - 1):
        clh = cells.cells[ih]; half[ih] = (clh, MomentCache(clh), SEC.W.cell_weight(clh, "Y"), SEC.bg.get(ih))
    res = {}
    t0 = time.time()
    for key, colobjs in items:
        BND = np.zeros((Mj + 2 * Nf + 4, cells.n))
        for colobj in colobjs:
            m = colobj.m
            Pj = colobj.Pcol          # signed ball coefficients of the column's sine modes (aggregated columns included; verifier V027)
            # (b) on the support cells
            for ic, b in colobj.pieces.items():
                cl = cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = SEC.W.cell_weight(cl, "Y")
                bt = b.scale(arb(3)) + b.deriv()
                if cl["kind"] in ("minf", "pinf"):
                    dP = half[ic][3]
                    for ni in range(Nf):
                        n = ni + 1; Pe = dP["Pe"][ni]; Qe = dP["Qe"][ni]
                        for j, pj in Pj.items():
                            fs1 = [2 * j + 1 + 2 * n, abs(2 * j + 1 - 2 * n)]; fs2 = [2 * n + 2 * j + 1, abs(2 * n - 2 * j - 1)]
                            if all(((f - 1) // 2) <= Nmax for f in fs1 + fs2): continue
                            v1 = h1n((Pe * bt).scale(abs(pj) / 2), mc, wY, W0Y); v2 = h1n((Qe * b).scale(abs(pj) * (2 * j + 1) / 2), mc, wY, W0Y)
                            for f in fs1:
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v1) * FUDGE
                            for f in fs2:
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v2) * FUDGE
                else:
                    nb1 = h1n(bt, mc, wY, W0Y); nb0 = l2n(bt, mc, wY, W0Y); nb1b = h1n(b, mc, wY, W0Y); nb0b = l2n(b, mc, wY, W0Y)
                    S_ = SUPT[ic]
                    for n in range(1, Nf + 1):
                        sPe, sdPe, sQe, sdQe = S_[n - 1]
                        for j, pj in Pj.items():
                            apj = float(abs(pj).upper())
                            v1 = apj / 2 * (sPe * nb1 + sdPe * nb0) * FUDGE; v2 = apj * (2 * j + 1) / 2 * (sQe * nb1b + sdQe * nb0b) * FUDGE
                            for f in (2 * j + 1 + 2 * n, abs(2 * j + 1 - 2 * n)):
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v1) * FUDGE
                            for f in (2 * n + 2 * j + 1, abs(2 * n - 2 * j - 1)):
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v2) * FUDGE
            # (c) all cells
            for ic, cl in enumerate(cells.cells):
                Ah, Bh = colobj.green_on_cell(ic); em2a = (-2 * cl["ta"]).exp()
                for n in colobj.hmodes:
                    Peh = (Ah[n] + Bh[n]).scale(em2a / 2).mul_exp(fmpq(-2)); Qeh = (Bh[n] - Ah[n]).scale(em2a / 2).mul_exp(fmpq(-2))
                    if not Peh.terms and not Qeh.terms: continue
                    if cl["kind"] in ("minf", "pinf"):
                        clh, mcp, (W0p, wp), dP = half[ic]
                        for j in range(Mj):
                            fs1 = [2 * j + 1 + 2 * n, abs(2 * j + 1 - 2 * n)]; fs2 = [2 * n + 2 * j + 1, abs(2 * n - 2 * j - 1)]
                            if all(((f - 1) // 2) <= Nmax for f in fs1 + fs2): continue
                            v1 = h1n((Peh * dP["dR"][j]).scale(arb(1) / 2), mcp, wp, W0p) if Peh.terms else 0.0
                            v2 = h1n((Qeh * dP["Rhat"][j]).scale(arb(2 * j + 1) / 2), mcp, wp, W0p) if Qeh.terms else 0.0
                            for f in fs1:
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v1) * FUDGE
                            for f in fs2:
                                N = (f - 1) // 2
                                if N > Nmax and f > 0: BND[N, ic] = (BND[N, ic] + v2) * FUDGE
                    else:
                        sP, sdP = (up(x) for x in sup_bound(Peh, cl)) if Peh.terms else (0.0, 0.0)
                        sQ, sdQ = (up(x) for x in sup_bound(Qeh, cl)) if Qeh.terms else (0.0, 0.0)
                        add_terms_sup(BND, ic, cl, n, sP, sdP, sQ, sdQ, NRMT[ic], Nmax, Mj)
        res[key] = BND
    np.savez(os.path.join(outdir, "t2partB_%d.npz" % wid), keys=np.array([k for k, _ in items]), **{("B_%s" % k): v for k, v in res.items()})
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
    bg = Background(T, cells, nmax=None)
    k = T.k_q
    W = Weights(T, eps0X=1, gammaX=(3 * k - 1) / 2, sX=1, eps0Y=1, gammaY=(3 * k - 1) / 2, sY=1)
    SEC = Section(T, cells, bg, W, Mh=Mh, stride=stride, Mout=Mout, stride_test=stride_test, verbose=False)
    Nmax = Mout - 1; Mj = T.Mj; Nf = T.Nf
    print("tailbound2: build %.0fs; cells %d, columns %d" % (time.time() - T0, cells.n, SEC.ncol), flush=True)
    mp.set_start_method("fork")
    idx = list(range(cells.n)); chunks = [idx[w::nw] for w in range(nw)]
    with mp.Pool(nw) as pool:
        for wid, dt in pool.imap_unordered(workerA, [(w, chunks[w], outdir) for w in range(nw)]):
            print("  A worker %d done (%.0fs)" % (wid, dt), flush=True)
    SUPT = np.zeros((cells.n, Nf, 4)); NRMT = np.zeros((cells.n, Mj, 4)); NRMREM = np.zeros((cells.n, Mj)); TK = np.zeros((cells.n, Mj)); TT = np.zeros((cells.n, Mj))
    for w in range(nw):
        z = np.load(os.path.join(outdir, "t2tablesA_%d.npz" % w)); SUPT[z["idx"]] = z["SUP"]; NRMT[z["idx"]] = z["NRM"]; NRMREM[z["idx"]] = z["NRMREM"]; TK[z["idx"]] = z["TK"]; TT[z["idx"]] = z["TT"]
    np.savez(os.path.join(outdir, "t2tablesA.npz"), SUP=SUPT, NRM=NRMT, NRMREM=NRMREM, TK=TK, TT=TT)
    print("tables A done (%.0fs)" % (time.time() - T0), flush=True)
    # phase B: (b)+(c) arrays for every basis column, for KP (all pieces) and TAU (all pieces)
    items = [(str(ci_), [cd["col"]]) for ci_, cd in enumerate(SEC.cols)] + [("KP", list(SEC.KP)), ("TAU", list(SEC.TAU))]
    # KP/TAU are heavy: give them their own workers first
    order = items[-2:] + items[:-2]
    chunksB = [order[w::nw] for w in range(nw)]
    with mp.Pool(nw) as pool:
        for wid, dt in pool.imap_unordered(workerB, [(w, chunksB[w], outdir) for w in range(nw)]):
            print("  B worker %d done (%.0fs)" % (wid, dt), flush=True)
    BNDs = {}
    for w in range(nw):
        z = np.load(os.path.join(outdir, "t2partB_%d.npz" % w))
        for kk in z["keys"]: BNDs[str(kk)] = z["B_%s" % kk]
    # assemble per compensated column: BND_j + |dk_j| BND_KP + joint (d): |C_j|/3 NRMREM[:, N] + |dk_j| TK[:, N]  (N > Nmax), TAU adds TT
    kk_ = T.k; c_l = 1 / T.k; denom = 3 * c_l + kk_ * SEC.cKP
    wY2 = np.array([(1 + (2 * N + 1) ** 2) ** SEC.W.sY for N in range(BNDs["KP"].shape[0])])
    out = {}
    def total(B):
        B = B.copy(); B[:Nmax + 1, :] = 0.0
        return float((wY2[:, None] * B * B).sum() * (1 + 1e-8))      # covers the rounding of all float accumulations (< 1e5 ops per entry)
    for key, colobjs in items[:-2] + [("TAU", list(SEC.TAU))]:
        cval = colobjs[0].c if key != "TAU" else SEC.cTAU
        dk = -cval * kk_ / denom; C = cval + dk * SEC.cKP
        adk = abs(float(abs(dk).upper())); aC = float(abs(C).upper())
        B = BNDs[key] + adk * BNDs["KP"]
        for N in range(Nmax + 1, Mj):
            B[N, :] += aC / 3 * NRMREM[:, N] * FUDGE + adk * TK[:, N] * FUDGE + (TT[:, N] * FUDGE if key == "TAU" else 0.0)
        out[key] = dict(E2_upper=total(B), dk=float(dk.mid()), C=float(C.mid()))
    json.dump(dict(Nmax=Nmax, columns=out, note="E_j^> <= sum_{N>Nmax} wY2(N) sum_cells b[N,c]^2 for the COMPENSATED columns; floats are outward upper bounds"), open(os.path.join(outdir, "tailbound2.json"), "w"), indent=1)
    print("saved tailbound2.json; total %.0fs; max E2 %.3e" % (time.time() - T0, max(v["E2_upper"] for v in out.values())))
