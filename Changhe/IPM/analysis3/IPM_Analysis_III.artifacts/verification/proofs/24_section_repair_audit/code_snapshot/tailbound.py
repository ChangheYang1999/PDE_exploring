"""Phase 2b (s2-num): rigorous upper bound for the dropped output modes N > Nmax of every column image (part of (I - Q_M) L P_N).

For h = x^2 y b(t) cos 2m theta the modes N > Nmax of G = e^{-3t} L h come from
  (b) background velocity modes n with 2j+1 +- 2n = 2N+1 (j in the <= 4 modes of h):  -(1/2) Pe_n P_jm (3b + b'),  +(1/2) Qe_n (2j+1) P_jm b;
  (c) the column's velocity modes n (|n - m| <= 2) against background modes j with 2j+1 +- 2n = 2N+1:  -(1/2) Pe^h_n dR_j,  +(1/2) Qe^h_n (2j+1) Rhat_j;
  (d) the strain term (c[h]/3) dR_N.
Bound used (triangle inequality in the weighted H^1 norm of each mode, then the Cauchy-Schwarz over the terms feeding one N):
  ||f g||_{H1_W} <= sup|f| ||g||_{H1_W} + sup|f'| ||g||_{L2_W}   on each cell, with sup bounds of exponential polynomials by coefficient sums.
Output per column: an upper bound D_j^2 >= sum_{N > Nmax} wY2(N) ||G_N||^2_{H1_W}.
"""
import sys, os, time, json, math
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExpPoly, q2arb
from section import MomentCache


def sup_bound(ep, cl):
    """rigorous upper bounds (arb) of sup|ep| and sup|ep'| on the cell (finite: sigma in [0, h]; minf: sigma <= 0; pinf: sigma >= 0),
    by |sum_e e^{e sigma} p_e(sigma)| <= sum_e max_{sigma} e^{e sigma} sum_a |c_a| |sigma|^a (finite cells); for half-infinite cells each term
    e^{e sigma} sigma^a is bounded by its maximum (a/|e|)^a e^{-a} (requires e sigma -> -oo in the cell direction, i.e. e > 0 on minf, e < 0 on pinf)."""
    def one(f):
        tot = arb(0)
        for e, cs in f.terms.items():
            ea = q2arb(e)
            if cl["kind"] == "minf":
                assert ea > 0 or all(c == 0 for c in cs), "unbounded term on the inner half-line"
                for a, c in enumerate(cs):
                    if c == 0: continue
                    tot += abs(c) * (arb(1) if a == 0 else (arb(a) / ea) ** a * arb(-a).exp())
            elif cl["kind"] == "pinf":
                assert ea < 0 or all(c == 0 for c in cs), "unbounded term on the outer half-line"
                for a, c in enumerate(cs):
                    if c == 0: continue
                    tot += abs(c) * (arb(1) if a == 0 else (arb(a) / (-ea)) ** a * arb(-a).exp())
            else:
                h = cl["h"]; emax = arb(1) if ea <= 0 else (ea * h).exp()
                s = arb(0)
                for a, c in enumerate(cs):
                    if c != 0: s += abs(c) * h ** a
                tot += emax * s
        return tot
    return one(ep), one(ep.deriv())


def h1_norm2(ep, mc, w, W0):
    """exact int (ep^2 + ep'^2) e^{w sigma} W0 on the cell"""
    dep = ep.deriv()
    return mc.integ(ep * ep + dep * dep, w, W0)


def l2_norm2(ep, mc, w, W0):
    return mc.integ(ep * ep, w, W0)


def column_tail_bound(S, cidx, colobj, bgsup, bgnorm, Nmax):
    """Upper bound (arb) of sum_{N > Nmax} wY2(N) ||G_N||^2_{H1_W} for one column.
    bgsup[ic][n] = (supPe, supPe', supQe, supQe') for n = 1..Nf on cell ic;  bgnorm[ic][j] = (||dR_j||_{H1_W}, ||dR_j||_{L2_W}, ||Rhat_j||_{H1}, ||Rhat_j||_{L2}) on cell ic
    (all with the Y weight of the cell).  Terms are collected per output N as upper bounds of ||G_N||_{H1_W} (sum of the term bounds), then squared."""
    T = S.T; m = colobj.m; cells = S.cells
    Pj = {j: q2arb(T.P_q[j, m]) for j in range(T.Mj) if T.P_q[j, m] != 0}
    bound_N = {}        # N -> arb upper bound of ||G_N||_{H1_W}
    def addN(f, val):
        if f < 0: f = -f
        if f == 0: return
        N = (f - 1) // 2
        if N > Nmax: bound_N[N] = bound_N.get(N, arb(0)) + val
    # (b): on the support cells; need ||3b + b'||_{H1}, ||3b+b'||_{L2}, ||b||_{H1}, ||b||_{L2} per cell (exact), times sup bounds of Pe_n, Qe_n
    for ic, b in colobj.pieces.items():
        cl = cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = S.W.cell_weight(cl, "Y")
        bt = b.scale(arb(3)) + b.deriv()
        nb1 = h1_norm2(bt, mc, wY, W0Y).sqrt(); nb0 = l2_norm2(bt, mc, wY, W0Y).sqrt()
        nb1b = h1_norm2(b, mc, wY, W0Y).sqrt(); nb0b = l2_norm2(b, mc, wY, W0Y).sqrt()
        sup = bgsup[ic]
        for n in range(1, len(sup) + 1):
            sPe, sdPe, sQe, sdQe = sup[n - 1]
            for j, pj in Pj.items():
                v1 = abs(pj) / 2 * (sPe * nb1 + sdPe * nb0)
                v2 = abs(pj) * (2 * j + 1) / 2 * (sQe * nb1b + sdQe * nb0b)
                for f in (2 * j + 1 + 2 * n, 2 * j + 1 - 2 * n): addN(f, v1)
                for f in (2 * n + 2 * j + 1, 2 * n - 2 * j - 1): addN(f, v2)
    # (c): the column's velocity on the background, all cells: sup bounds of Pe^h_n, Qe^h_n (and derivatives) on each cell
    for ic, cl in enumerate(cells.cells):
        Ah, Bh = colobj.green_on_cell(ic)
        em2a = (-2 * cl["ta"]).exp()
        for n in colobj.hmodes:
            Peh = (Ah[n] + Bh[n]).scale(em2a / 2).mul_exp(fmpq(-2)); Qeh = (Bh[n] - Ah[n]).scale(em2a / 2).mul_exp(fmpq(-2))
            if not Peh.terms and not Qeh.terms: continue
            sP, sdP = sup_bound(Peh, cl) if Peh.terms else (arb(0), arb(0))
            sQ, sdQ = sup_bound(Qeh, cl) if Qeh.terms else (arb(0), arb(0))
            for j in range(T.Mj):
                if min(abs(2 * j + 1 - 2 * n), 2 * j + 1 + 2 * n) <= 2 * Nmax + 1 and (2 * n + 2 * j + 1 > 2 * Nmax + 1 or True):
                    pass
                ndR1, ndR0, nR1, nR0 = bgnorm[ic][j]
                v1 = (sP * ndR1 + sdP * ndR0) / 2
                v2 = (2 * j + 1) * (sQ * nR1 + sdQ * nR0) / 2
                for f in (2 * j + 1 + 2 * n, 2 * j + 1 - 2 * n): addN(f, v1)
                for f in (2 * n + 2 * j + 1, 2 * n - 2 * j - 1): addN(f, v2)
    # (d): strain term
    if colobj.c != 0:
        for ic, cl in enumerate(cells.cells):
            for N in range(Nmax + 1, T.Mj):
                bound_N[N] = bound_N.get(N, arb(0)) + abs(colobj.c) / 3 * bgnorm[ic][N][0]
    tot = arb(0)
    for N, v in bound_N.items(): tot += S.W.wY2(N) * v * v
    return tot, bound_N


def background_tables(S, ic):
    """per cell: sup bounds (Pe_n, Pe_n', Qe_n, Qe_n') for all n (requires bg.get with all modes on this cell) and the Y-weighted norms of dR_j, Rhat_j"""
    d = S.bg.get(ic); cl = S.cells.cells[ic]; mc = MomentCache(cl); W0Y, wY = S.W.cell_weight(cl, "Y")
    sup = []
    for ni in range(len(d["Pe"])):
        sP, sdP = sup_bound(d["Pe"][ni], cl); sQ, sdQ = sup_bound(d["Qe"][ni], cl)
        sup.append((sP, sdP, sQ, sdQ))
    norms = []
    for j in range(S.T.Mj):
        dR = d["dR"][j]; R = d["Rhat"][j]
        norms.append((h1_norm2(dR, mc, wY, W0Y).sqrt(), l2_norm2(dR, mc, wY, W0Y).sqrt(), h1_norm2(R, mc, wY, W0Y).sqrt(), l2_norm2(R, mc, wY, W0Y).sqrt()))
    return sup, norms
