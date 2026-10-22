"""cert_forcing v2: the same certified bound as src/cert_forcing.py (read its docstring first), but on the transition annulus the cutoff tau
and ALL its Cartesian derivatives are themselves bivariate Taylor models (BiTM), so that the Leibniz products are formed exactly as BiTMs and
the sup of each full quantity (f, grad f, Lap f, grad Lap f, Lap^2 f, f = tau eps~) is taken per fine sub-cell: no products of suprema, no
absolute values of individual terms.  Construction per block (a sub-rectangle of a (spline sub-cell x angular cell)), in the block's local
variables (sigma', phi'):
  u = x - x_* = e^t cos th - x_*,  v = y = e^t sin th,  q = u^2 + v^2 = |X - P|^2            (BiTMs; x_* the certified bracket)
  W = q^{-1/2} = c0^{-1/2} sum_{k<=K} C(-1/2, k) ((q - c0)/c0)^k + tail,  c0 = constant term of q on the block (float > 0),
      |tail| <= c0^{-1/2} x^{K+1}/(1 - x), x = sup|q - c0|/c0 < 1   (|C(-1/2,k)| <= 1)
  rho = q W,  sigma = (rho - 7 delta/4) (2/delta),  S^{(j)}(sigma) by the exact integer polynomials (powers of the BiTM sigma)
  sigma_q-derivatives: s1 = W/delta, s2 = -W^3/(2 delta), s3 = 3 W^5/(4 delta), s4 = -15 W^7/(8 delta)       (d/dq of q^{-1/2} etc.)
  Faa di Bruno: S^_1 = S' s1, S^_2 = S'' s1^2 + S' s2, S^_3 = S''' s1^3 + 3 S'' s1 s2 + S' s3,
                S^_4 = S'''' s1^4 + 6 S''' s1^2 s2 + 3 S'' s2^2 + 4 S'' s1 s3 + S' s4        (tau = S^(q), S^_k = d^k S^/dq^k)
  Cartesian derivatives of tau = S^(q(u, v)) with q_u = 2u, q_v = 2v, q_uu = q_vv = 2: D^alpha tau = sum_k S^_k P_{alpha,k}(u, v) with the
  integer polynomials P generated symbolically by d_u[S^_k P] = S^_{k+1} 2u P + S^_k P_u (same for v).
  Then f = tau g, grad f, Lap f = tau Lap g + 2 grad tau.grad g + g Lap tau, grad Lap f (6 terms), Lap^2 f (6 terms, with D^2 tau : D^2 g exact),
  each a BiTM; suprema by tensor Bernstein on the fine sub-cells of the block.
Domain convention: a bivariate Taylor model consists of a polynomial and a remainder bound valid on the model's validity domain (the cell
[0, h] x [-w, w] for the cell models; a block is a sub-rectangle, re-centring does not extend the validity domain); the fine sub-cells used for the
sups and the geometry have outward (one-ulp larger) widths, so a sub-cell may overhang its parent domain by about 1e-19; the polynomial and
truncation bounds are taken over the (slightly larger) sub-cell, the remainder bound is used only on the intersection with the validity domain,
and the geometry over the larger sub-cell is conservative (larger area and distance ranges).  (Referee forcing2, item 4.)
Regimes per fine sub-cell (from its certified distance range to P): inside (sigma <= 0, tau = 1: f = g, bounds from the sups of D^alpha g),
transition (0 <= sigma <= 1 on the whole sub-cell: the BiTM bounds above), straddling (the v1 bounds of cert_forcing.py: products of suprema),
outside (zero).  Everything else (cells, jets, recursion, Hoelder, merge) as in v1.
Usage: python3 src/cert_forcing2.py green.npz trial.npz out.json [delta=33/2000] [cutoff=p9] [KSUB=64] [ntheta=16] [KP=8] [Qp=8] [nbs=2] [nbp=2] [Kser=16] [ci_lo ci_hi [q_lo q_hi]]
       python3 src/cert_forcing2.py merge out.json part1.json ...
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb, factorial
from fractions import Fraction
from flint import arb, ctx
from midrad import MR, mr_matmul, succ, U, ETA
from cert_resid import Certifier, TMArr, tm_exp, mag
from cert_forcing import (Cell, BiTM, BernSup, cart_from_polar, Cutoff, STEP_POLY, XSTAR, XRAD, XSTAR_LO, XSTAR_HI, NDER, S_ORDER, pred, finish, merge, f_up, f_lo)


# ---------------------------------------------------------------------------------------------------------------------------------
def shift_coeffs(c, a, combM, axis):
    """MR coefficient array c (Qs+1, Qp+1), scalar MR shift a along axis: new_j = sum_{i >= j} c_i C(i, j) a^{i-j}  (variable x = x' + a)."""
    n = c.m.shape[axis]
    apow = [MR.exact(1.0)]
    for i in range(1, n): apow.append(apow[-1] * a)
    outm = np.zeros_like(c.m); outr = np.zeros_like(c.r)
    for j in range(n):
        acc = None
        for i in range(j, n):
            ci = c[i, :] if axis == 0 else c[:, i]
            term = ci * MR.exact(float(combM[i, j])) * apow[i - j]
            acc = term if acc is None else acc + term
        if axis == 0: outm[j, :] = acc.m; outr[j, :] = acc.r
        else: outm[:, j] = acc.m; outr[:, j] = acc.r
    return MR(outm, outr)


class Recentre:
    def __init__(self, Qs, Qp):
        self.cs = np.array([[comb(i, j) if i >= j else 0 for j in range(Qs + 1)] for i in range(Qs + 1)], float)
        self.cp = np.array([[comb(i, j) if i >= j else 0 for j in range(Qp + 1)] for i in range(Qp + 1)], float)

    def __call__(self, f, a_s, a_p, newcell):
        """BiTM f on its cell -> the same function on the block with local variables sigma' = sigma - a_s, phi' = phi - a_p (MR scalars)."""
        c = shift_coeffs(f.c, a_s, self.cs, 0)
        c = shift_coeffs(c, a_p, self.cp, 1)
        return BiTM(c, f.r, newcell)

    def many(self, fs, a_s, a_p, newcell):
        """Batched version for a list of BiTMs on the same cell (stacked along a leading axis)."""
        n = len(fs); Qs1, Qp1 = fs[0].c.m.shape
        cm = np.stack([f.c.m for f in fs]); cr = np.stack([f.c.r for f in fs]); c = MR(cm, cr)
        aps = [MR.exact(1.0)]
        for i in range(1, Qs1): aps.append(aps[-1] * a_s)
        om = np.zeros_like(cm); orr = np.zeros_like(cr)
        for j in range(Qs1):
            acc = None
            for i in range(j, Qs1):
                term = c[:, i, :] * MR.exact(float(self.cs[i, j])) * aps[i - j]
                acc = term if acc is None else acc + term
            om[:, j, :] = acc.m; orr[:, j, :] = acc.r
        c = MR(om, orr)
        app = [MR.exact(1.0)]
        for i in range(1, Qp1): app.append(app[-1] * a_p)
        om = np.zeros_like(cm); orr = np.zeros_like(cr)
        for j in range(Qp1):
            acc = None
            for i in range(j, Qp1):
                term = c[:, :, i] * MR.exact(float(self.cp[i, j])) * app[i - j]
                acc = term if acc is None else acc + term
            om[:, :, j] = acc.m; orr[:, :, j] = acc.r
        return [BiTM(MR(om[k], orr[k]), fs[k].r, newcell) for k in range(n)]


def add_const(f, cst):
    """BiTM + MR scalar constant."""
    c = MR(f.c.m.copy(), f.c.r.copy()); z = c[0, 0] + cst; c.m[0, 0] = z.m; c.r[0, 0] = z.r
    return BiTM(c, f.r, f.cell)


def faa_di_bruno_tables(order):
    """For F(q(u, v)), q = u^2 + v^2: D^alpha F = sum_k F^{(k)}(q) P_{alpha,k}(u, v).  Returns dict alpha=(a,b) -> dict k -> poly (dict (i,j) -> int)."""
    def d_var(terms, var):
        out = {}
        def addp(k, poly, factor=1):
            tgt = out.setdefault(k, {})
            for mono, c in poly.items():
                tgt[mono] = tgt.get(mono, 0) + factor * c
        for k, P in terms.items():
            # chain term: F^{(k+1)} * dq/dvar * P, dq/du = 2u, dq/dv = 2v
            shifted = {}
            for (i, j), c in P.items():
                m = (i + 1, j) if var == "u" else (i, j + 1)
                shifted[m] = shifted.get(m, 0) + 2 * c
            addp(k + 1, shifted)
            # derivative of P
            dP = {}
            for (i, j), c in P.items():
                if var == "u" and i > 0: dP[(i - 1, j)] = dP.get((i - 1, j), 0) + i * c
                if var == "v" and j > 0: dP[(i, j - 1)] = dP.get((i, j - 1), 0) + j * c
            if dP: addp(k, dP)
        return {k: {m: c for m, c in P.items() if c != 0} for k, P in out.items() if any(c != 0 for c in P.values())}
    T = {(0, 0): {0: {(0, 0): 1}}}
    for a in range(order + 1):
        for b in range(order + 1 - a):
            if (a, b) == (0, 0): continue
            if b == 0: T[(a, b)] = d_var(T[(a - 1, 0)], "u")
            else: T[(a, b)] = d_var(T[(a, b - 1)], "v")
    return T


def _test_fdb():
    T = faa_di_bruno_tables(4)
    # checks: Lap tau = 4 q F'' + 4 F' ; D_x tau = F' 2u ; D_xxx = F''' 8u^3 + F'' 12 u
    assert T[(1, 0)] == {1: {(1, 0): 2}}
    assert T[(3, 0)] == {3: {(3, 0): 8}, 2: {(1, 0): 12}}, T[(3, 0)]
    lap = {}
    for k in set(T[(2, 0)]) | set(T[(0, 2)]):
        for src in (T[(2, 0)], T[(0, 2)]):
            for m, c in src.get(k, {}).items(): lap.setdefault(k, {}); lap[k][m] = lap[k].get(m, 0) + c
    assert lap == {2: {(2, 0): 4, (0, 2): 4}, 1: {(0, 0): 4}}, lap
    return True


# ---------------------------------------------------------------------------------------------------------------------------------
def main(green, trial, out, delta_str="33/2000", cutoff="p9", KSUB=64, ntheta=16, KP=8, Qp=8, nbs=2, nbp=2, Kser=16, chunk=None, qchunk=None):
    t0 = time.time()
    assert KSUB % nbs == 0 and KP % nbp == 0
    Ks_b, Kp_b = KSUB // nbs, KP // nbp
    assert _test_fdb()
    FDB = faa_di_bruno_tables(NDER)
    C = Certifier(green, trial, Q=12); Qs = C.Q
    ctx.prec = 128
    dfrac = Fraction(delta_str); cut = Cutoff(cutoff, dfrac)
    delta = cut.delta; xs = arb(XSTAR, XRAD)
    R3 = 3 * delta; R94 = cut.r_out
    Sj_coeffs = cut.S                                   # exact integer coefficients of S, S', ..., S''''
    r_in_MR = MR.from_arb([cut.r_in])[0]; two_over_delta = MR.from_arb([2 / delta])[0]
    inv_delta = MR.from_arb([1 / delta])[0]
    sder_scale = [None, inv_delta, MR.from_arb([-1 / (2 * delta)])[0], MR.from_arb([3 / (4 * delta)])[0], MR.from_arb([-15 / (8 * delta)])[0]]
    t_lo_need = float(pred(float((xs - R3).log().lower()))); t_hi_need = float(succ(float((xs + R3).log().upper())))
    tb_lo = C.tb.lower(); tb_hi = C.tb.upper()
    cells = [ci for ci in range(C.nc) if tb_hi[ci + 1] > t_lo_need and tb_lo[ci] < t_hi_need]
    assert tb_hi[cells[0]] <= t_lo_need and tb_lo[cells[-1] + 1] >= t_hi_need, "radial coverage"
    assert cells == list(range(cells[0], cells[-1] + 1)), "cells contiguous"
    cover = [int(cells[0]), int(cells[-1])]
    if chunk is not None:
        cells = [ci for ci in cells if chunk[0] <= ci <= chunk[1]]
        print("chunk: cells %d..%d of the cover %d..%d" % (cells[0], cells[-1], cover[0], cover[1]), flush=True)
    theta_max_f = float(np.nextafter(float(((R3 / xs).asin() * arb("1.000001")).upper()), np.inf)); theta_max = arb(theta_max_f)
    assert (theta_max - (R3 / xs).asin()).lower() > 0, "angular coverage"
    dth = theta_max / ntheta
    w_up = float(np.nextafter(float((dth / 2).upper()), np.inf))
    print("v2: delta = %s, cutoff %s (C^%d), radial cells %d (ci %d..%d), theta_max %.6g, ntheta %d, w %.3e, KSUB %d, KP %d, blocks %dx%d, Kser %d, Qs %d, Qp %d" % (
        dfrac, cutoff, cut.smooth, len(cells), cells[0], cells[-1], theta_max_f, ntheta, w_up, KSUB, KP, nbs, nbp, Kser, Qs, Qp), flush=True)
    Nmax = C.Nmax; twoN1 = 2.0 * np.arange(Nmax + 1) + 1.0
    XS_MR = MR(XSTAR, XRAD)
    lams = [1.0, 500.0]
    acc = {lam: dict(I3=0.0, I4=0.0) for lam in lams}
    keys = [(a, b) for a in range(NDER + 1) for b in range(NDER + 1 - a)]
    supD = {"B94": {k: 0.0 for k in keys}, "B3": {k: 0.0 for k in keys}}; where = {"B94": {}, "B3": {}}
    area_tot = {"B94": 0.0, "B3": 0.0}; regime_count = dict(inside=0, transition=0, straddle=0, outside=0, fallback_block=0)
    rows = []; worst = dict(x_series=0.0, tail=0.0)
    inv_fact = [MR(1.0 / factorial(p), succ(U / factorial(p))) for p in range(Qp + 1)]
    ang_tables = []
    for q in range(ntheta):
        theta_c = dth * (q + arb(1) / 2)
        sN = []; cN = []
        for N in range(Nmax + 1):
            s_, c_ = (theta_c * int(2 * N + 1)).sin_cos(); sN.append(s_); cN.append(c_)
        SN = MR.from_arb(sN); CN = MR.from_arb(cN); trig = [SN, CN, -SN, -CN]
        s1, c1 = theta_c.sin_cos(); S1 = MR.from_arb([s1]); C1 = MR.from_arb([c1]); trig1 = [S1, C1, -S1, -C1]
        fpow = [MR.exact(np.ones(Nmax + 1))]
        for m in range(1, NDER + Qp + 2): fpow.append(fpow[-1] * MR.exact(twoN1))
        wq = succ(w_up ** (Qp + 1) * (1 + 2 * (Qp + 1) * U) / factorial(Qp + 1))
        Tj = []; remfac = []
        for j in range(NDER + 1):
            cols = [fpow[j + p] * trig[(j + p) % 4] * inv_fact[p] for p in range(Qp + 1)]
            Tj.append(MR(np.stack([c.m for c in cols], 1), np.stack([c.r for c in cols], 1)))
            remfac.append(succ(mag(fpow[j + Qp + 1]) * wq * (1 + 2 * U)))
        cosb = []; sinb = []
        for b in range(NDER + 2):
            cc = [trig1[(b + p + 1) % 4] * inv_fact[p] for p in range(Qp + 1)]; ss = [trig1[(b + p) % 4] * inv_fact[p] for p in range(Qp + 1)]
            cosb.append(MR(np.array([x.m[0] for x in cc]), np.array([x.r[0] for x in cc]))); sinb.append(MR(np.array([x.m[0] for x in ss]), np.array([x.r[0] for x in ss])))
        ang_tables.append(dict(q=q, theta_c=theta_c, Tj=Tj, remfac=remfac, cosb=cosb, sinb=sinb, trig_rem=wq))
    print("angular tables done (%.0fs)" % (time.time() - t0), flush=True)
    REC = Recentre(Qs, Qp)
    tim = dict(rec=0.0, tau=0.0, bern=0.0, geo=0.0)
    for idx, ci in enumerate(cells):
        h = C.tb[ci + 1] - C.tb[ci]; h_up = h.mag()
        assert succ(2.0 * C.Nf * h_up) <= 1.0, 'ODE remainder hypothesis 2 Nf h <= 1'
        res = C.cell_core_deriv(h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], C.m_ta[ci], C.wfar_ta[ci], NDER)
        eps = C._last_eps
        cell = Cell(h_up, w_up, Qs, Qp)
        epsT = [MR(eps[i].c.m.T.copy(), eps[i].c.r.T.copy()) for i in range(NDER + 1)]
        epsSup = [eps[i].sup(cell.hpow) for i in range(NDER + 1)]
        ta = arb(float(C.d["tb"][ci]), float(C.d["tb_rad"][ci]))
        Ec, Er = tm_exp(-1.0, h_up, Qs); inv_e = MR.from_arb([(-ta).exp()])
        EMT = BiTM.from_sigma(Ec * MR(inv_e.m[0], inv_e.r[0]), succ(Er * float(inv_e.mag()[0]) * (1 + 2 * U)), cell)
        E1c, E1r = tm_exp(1.0, h_up, Qs); e_ta = MR.from_arb([ta.exp()])
        E1 = BiTM.from_sigma(E1c * MR(e_ta.m[0], e_ta.r[0]), succ(E1r * float(e_ta.mag()[0]) * (1 + 2 * U)), cell)
        # fine sub-cells of the cell: sigma in [ks hk, (ks+1) hk] (ks < KSUB), phi in [-w + kp wk, -w + (kp+1) wk] (kp < KP), hk >= h/KSUB, wk >= 2w/KP;
        # blocks = unions of Ks_b x Kp_b fine sub-cells: block (bs, bp) has sigma in [bs hb, (bs+1) hb], hb = Ks_b hk (exact double: Ks_b a power of two),
        # phi in [-w + bp wb, -w + (bp+1) wb], wb = Kp_b wk (exact).  The block-level BernSup uses the SAME hk, wk, so that the fine sub-cells of a
        # block are exactly the fine sub-cells of the cell (as exact reals), and the cell-level sups of D^alpha g can be indexed by (ks, kp).
        bern_c = BernSup(cell, KSUB, KP); hk = bern_c.hk; wk = bern_c.wk
        hb = Ks_b * hk; wb = Kp_b * wk
        assert (arb(hk) * Ks_b - arb(hb)).is_zero() and (arb(wk) * Kp_b - arb(wb)).is_zero(), "block sizes must be exact doubles (Ks_b, Kp_b powers of two)"
        assert (arb(hk) * KSUB).lower() >= h_up and (arb(wk) * KP).lower() >= 2.0 * w_up         # coverage of the cell by the fine sub-intervals, exact-real test
        blockcell = Cell(hb, 0.5 * wb, Qs, Qp)
        bern_b = BernSup(blockcell, Ks_b, Kp_b, hk=hk, wk=wk)
        for A in ang_tables:
            if qchunk is not None and not (qchunk[0] <= A["q"] <= qchunk[1]): continue
            t1 = time.time()
            J = {}
            for i in range(NDER + 1):
                for j in range(NDER + 1 - i):
                    cf = mr_matmul(epsT[i], A["Tj"][j])
                    r1 = succ(succ((eps[i].r * (twoN1 ** j)).sum() * succ(1 + (Nmax + 2) * U)) + (Nmax + 2) * ETA); r2 = succ(succ((epsSup[i] * A["remfac"][j]).sum() * succ(1 + (Nmax + 2) * U)) + (Nmax + 2) * ETA)      # additive eta allowance: the relative rule alone is not outward for subnormal terms (ver 08:07Z)
                    J[(i, j)] = BiTM(cf, succ(r1 + r2), cell)
            cos_b = [BiTM.from_phi(A["cosb"][b], A["trig_rem"], cell) for b in range(NDER + 2)]
            sin_b = [BiTM.from_phi(A["sinb"][b], A["trig_rem"], cell) for b in range(NDER + 2)]
            D = cart_from_polar(J, NDER, EMT, cos_b, sin_b)
            Ucell = E1 * cos_b[0] + BiTM.zero(cell); Ucell = add_const(Ucell, -XS_MR)          # u = x - x_*
            Vcell = E1 * sin_b[0]                                                                # v = y
            # cell-level sups of the g-quantities on the fine sub-cells (indexed by the global (ks, kp))
            lapg_c = D[(2, 0)] + D[(0, 2)]; lapgx_c = D[(3, 0)] + D[(1, 2)]; lapgy_c = D[(2, 1)] + D[(0, 3)]
            lap2g_c = D[(4, 0)] + D[(2, 2)].scale(MR.exact(2.0)) + D[(0, 4)]
            SgC = {k: bern_c.sups(D[k]) for k in keys}
            SgLC = bern_c.sups(lapg_c); SgLxC = bern_c.sups(lapgx_c); SgLyC = bern_c.sups(lapgy_c); SgL2C = bern_c.sups(lap2g_c)
            t2 = time.time(); tim["rec"] += t2 - t1
            theta_c = A["theta_c"]
            for bs in range(nbs):
                for bp in range(nbp):
                    tb1 = time.time()
                    a_s = MR(bs * hb, succ(U * bs * hb)); a_p = MR.exact(-w_up) + MR(bp * wb, succ(U * bp * wb)) + MR.exact(0.5 * wb)   # balls containing the exact shifts bs hb, -w + bp wb + wb/2 (the products are exact for nbs, nbp <= 2 but may round otherwise; referee forcing2)
                    sl_ks = slice(bs * Ks_b, (bs + 1) * Ks_b); sl_kp = slice(bp * Kp_b, (bp + 1) * Kp_b)
                    Sg = {k: SgC[k][sl_ks, sl_kp] for k in keys}
                    SgL = SgLC[sl_ks, sl_kp]; SgLx = SgLxC[sl_ks, sl_kp]; SgLy = SgLyC[sl_ks, sl_kp]; SgL2 = SgL2C[sl_ks, sl_kp]
                    rec_list = REC.many([D[k] for k in keys] + [Ucell, Vcell], a_s, a_p, blockcell)
                    Db = {k: rec_list[i] for i, k in enumerate(keys)}; ub = rec_list[-2]; vb = rec_list[-1]
                    g = Db[(0, 0)]; gx = Db[(1, 0)]; gy = Db[(0, 1)]
                    lapg = Db[(2, 0)] + Db[(0, 2)]; lapgx = Db[(3, 0)] + Db[(1, 2)]; lapgy = Db[(2, 1)] + Db[(0, 3)]
                    lap2g = Db[(4, 0)] + Db[(2, 2)].scale(MR.exact(2.0)) + Db[(0, 4)]
                    # tau as BiTM on the block (composition), if the series converges on the block
                    qb = ub * ub + vb * vb
                    c0 = float(qb.c.m[0, 0]); have_tau = False
                    if c0 > 0:
                        uq = add_const(qb, MR.exact(-c0)); Umax = float(uq.sup_crude()); xr = succ(Umax / c0 * (1 + 2 * U))
                        if xr < 0.6:
                            have_tau = True; worst["x_series"] = max(worst["x_series"], xr)
                            # W = q^{-1/2} = c0^{-1/2} sum_k C(-1/2,k) (uq/c0)^k + tail
                            c0a = arb(c0); pw = [BiTM.zero(blockcell)]; pw[0] = add_const(pw[0], MR.exact(1.0))
                            Wb = pw[0].scale(MR.from_arb([c0a ** arb(-0.5)])[0])
                            cur = pw[0]
                            for k in range(1, Kser + 1):
                                cur = cur * uq
                                coef = MR.from_arb([arb(comb(2 * k, k)) / arb(4) ** k * (-1) ** k * c0a ** (-arb(k) - arb(0.5))])[0]   # C(-1/2,k) = (-1)^k C(2k,k)/4^k
                                Wb = Wb + cur.scale(coef)
                            tail = f_up(((c0a ** arb(-0.5)) * (arb(xr) ** (Kser + 1)) / (1 - arb(xr))).upper()); worst["tail"] = max(worst["tail"], tail)   # Arb, outward (referee forcing2)
                            Wb = BiTM(Wb.c, succ(Wb.r + tail), blockcell)
                            rho_b = qb * Wb
                            sig = add_const(rho_b.scale(two_over_delta), -(r_in_MR * two_over_delta))
                            spow = [add_const(BiTM.zero(blockcell), MR.exact(1.0)), sig]
                            for k in range(2, len(Sj_coeffs[0])): spow.append(spow[-1] * sig)          # powers up to the degree of S (9 for p9, 11 for p11)
                            Sv = []
                            for j in range(5):
                                accS = None
                                for k, ck in enumerate(Sj_coeffs[j]):
                                    if ck == 0: continue
                                    term = spow[k].scale(MR.exact(float(ck)))
                                    accS = term if accS is None else accS + term
                                Sv.append(accS)
                            W2 = Wb * Wb; W3 = W2 * Wb; W5 = W3 * W2; W7 = W5 * W2
                            s1 = Wb.scale(sder_scale[1]); s2 = W3.scale(sder_scale[2]); s3 = W5.scale(sder_scale[3]); s4 = W7.scale(sder_scale[4])
                            s1_2 = s1 * s1; s1_3 = s1_2 * s1; s1_4 = s1_2 * s1_2; s1s2 = s1 * s2; s1_2s2 = s1_2 * s2; s2_2 = s2 * s2; s1s3 = s1 * s3
                            Shat = {0: Sv[0], 1: Sv[1] * s1,
                                    2: Sv[2] * s1_2 + Sv[1] * s2,
                                    3: Sv[3] * s1_3 + (Sv[2] * s1s2).scale(MR.exact(3.0)) + Sv[1] * s3,
                                    4: Sv[4] * s1_4 + (Sv[3] * s1_2s2).scale(MR.exact(6.0)) + (Sv[2] * s2_2).scale(MR.exact(3.0)) + (Sv[2] * s1s3).scale(MR.exact(4.0)) + Sv[1] * s4}
                            # monomials u^i v^j
                            upow = [add_const(BiTM.zero(blockcell), MR.exact(1.0)), ub]; vpow = [upow[0], vb]
                            for k in range(2, 5): upow.append(upow[-1] * ub); vpow.append(vpow[-1] * vb)
                            mono = {}
                            for i in range(5):
                                for j in range(5 - i):
                                    mono[(i, j)] = upow[i] if j == 0 else (vpow[j] if i == 0 else upow[i] * vpow[j])
                            Dtau = {}
                            for k_ in keys:
                                accT = None
                                for kk, P in FDB[k_].items():
                                    poly = None
                                    for m, cc in P.items():
                                        term = mono[m].scale(MR.exact(float(cc))); poly = term if poly is None else poly + term
                                    term = Shat[kk] * poly
                                    accT = term if accT is None else accT + term
                                Dtau[k_] = accT
                            tau = Dtau[(0, 0)]; tx = Dtau[(1, 0)]; ty = Dtau[(0, 1)]
                            lapt = Dtau[(2, 0)] + Dtau[(0, 2)]; laptx = Dtau[(3, 0)] + Dtau[(1, 2)]; lapty = Dtau[(2, 1)] + Dtau[(0, 3)]
                            lap2t = Dtau[(4, 0)] + Dtau[(2, 2)].scale(MR.exact(2.0)) + Dtau[(0, 4)]
                            f = tau * g
                            fx = tau * gx + tx * g; fy = tau * gy + ty * g
                            lapf = tau * lapg + (tx * gx + ty * gy).scale(MR.exact(2.0)) + g * lapt
                            lapfx = tx * lapg + tau * lapgx + (Dtau[(2, 0)] * gx + Dtau[(1, 1)] * gy).scale(MR.exact(2.0)) + (Db[(2, 0)] * tx + Db[(1, 1)] * ty).scale(MR.exact(2.0)) + gx * lapt + g * laptx
                            lapfy = ty * lapg + tau * lapgy + (Dtau[(1, 1)] * gx + Dtau[(0, 2)] * gy).scale(MR.exact(2.0)) + (Db[(1, 1)] * tx + Db[(0, 2)] * ty).scale(MR.exact(2.0)) + gy * lapt + g * lapty
                            lap2f = (tau * lap2g + g * lap2t + (lapt * lapg).scale(MR.exact(2.0)) + (tx * lapgx + ty * lapgy).scale(MR.exact(4.0))
                                     + (gx * laptx + gy * lapty).scale(MR.exact(4.0))
                                     + (Dtau[(2, 0)] * Db[(2, 0)] + (Dtau[(1, 1)] * Db[(1, 1)]).scale(MR.exact(2.0)) + Dtau[(0, 2)] * Db[(0, 2)]).scale(MR.exact(4.0)))
                            Sf = dict(f=bern_b.sups(f), fx=bern_b.sups(fx), fy=bern_b.sups(fy), L=bern_b.sups(lapf), Lx=bern_b.sups(lapfx), Ly=bern_b.sups(lapfy), L2=bern_b.sups(lap2f),
                                      tau=bern_b.sups(tau))
                    if not have_tau: regime_count["fallback_block"] += 1
                    tb2 = time.time(); tim["tau"] += tb2 - tb1
                    # fine sub-cells of the block: geometry and assembly
                    for kp in range(Kp_b):
                        kpg = bp * Kp_b + kp                                                                 # global fine index
                        thA = theta_c + arb(-w_up) + arb(kpg) * arb(wk); thB = thA + arb(wk)                # exact reals: the fine sub-cell [-w + kpg wk, -w + (kpg+1) wk]
                        thA0 = thA if thA.lower() >= 0 else arb(0)               # dmin: minimum over theta at the smallest |theta| (0 if the sub-cell straddles the axis)
                        cA = MR.from_arb([thA0.cos()]); sA = MR.from_arb([thA0.sin()]); cB = MR.from_arb([thB.cos()])
                        dth_up = f_up((thB - thA).upper())
                        for ks in range(Ks_b):
                            ksg = bs * Ks_b + ks
                            sA_ = arb(ksg) * arb(hk); tA = ta + sA_; tB = tA + arb(hk)                           # exact reals: fine sub-cell [ksg hk, (ksg+1) hk]
                            tcell = tA.union(tB)
                            r_lo = float(pred(float(tcell.exp().lower()))); r_hi = float(succ(float(tcell.exp().upper())))
                            R1 = MR.exact(r_lo); R2 = MR.exact(r_hi)
                            xc = XS_MR * cA; g1 = float((R1 - xc).lower()[0]); g2 = float((xc - R2).lower()[0]); gg = max(0.0, g1, g2)
                            xsn = XS_MR * sA
                            d2_lo = pred(pred(gg * gg * (1 - 4 * U)) + pred(float(xsn.mig()[0]) ** 2 * (1 - 4 * U)))
                            dmin = float(pred(np.sqrt(max(d2_lo, 0.0)) * (1 - 4 * U)))
                            xcB = XS_MR * cB
                            d2a = (R1 * R1 - MR.exact(2.0) * R1 * xcB + XS_MR * XS_MR).upper()[0]; d2b = (R2 * R2 - MR.exact(2.0) * R2 * xcB + XS_MR * XS_MR).upper()[0]
                            dmax = float(succ(np.sqrt(max(d2a, d2b, 0.0)) * (1 + 4 * U)))
                            area = succ(succ(0.5 * succ(succ(r_hi * r_hi) - r_lo * r_lo * (1 - 2 * U)) * dth_up) * 2.0 * (1 + 4 * U))
                            for ball, rad in (("B94", f_up(R94.upper())), ("B3", f_up(R3.upper()))):
                                if dmin <= rad:
                                    area_tot[ball] = succ(area_tot[ball] + area)
                                    for k_ in keys:
                                        v = Sg[k_][ks, kp]
                                        if v > supD[ball][k_]:
                                            supD[ball][k_] = float(v); where[ball][k_] = dict(ci=ci, q=A["q"], bs=bs, bp=bp, ks=ks, kp=kp, r=[r_lo, r_hi], dmin=dmin, dmax=dmax)
                            TQ = cut.quantities(dmin, dmax)
                            if TQ is None: regime_count["outside"] += 1; continue
                            slo, shi = TQ["sigma"]
                            G0 = Sg[(0, 0)][ks, kp]
                            G1 = succ(np.sqrt(succ(succ(Sg[(1, 0)][ks, kp] ** 2) + succ(Sg[(0, 1)][ks, kp] ** 2))) * (1 + 2 * U))
                            GL = SgL[ks, kp]; GL1 = succ(np.sqrt(succ(succ(SgLx[ks, kp] ** 2) + succ(SgLy[ks, kp] ** 2))) * (1 + 2 * U)); GL2 = SgL2[ks, kp]
                            if shi <= 0.0:                                                   # inside: tau = 1
                                regime = "inside"; F0, F1, FL, FL1, FL2 = G0, G1, GL, GL1, GL2
                            elif have_tau and slo >= 0.0 and shi <= 1.0:                     # transition: exact BiTM products
                                regime = "transition"
                                F0 = Sf["f"][ks, kp]; F1 = succ(np.sqrt(succ(succ(Sf["fx"][ks, kp] ** 2) + succ(Sf["fy"][ks, kp] ** 2))) * (1 + 2 * U))
                                FL = Sf["L"][ks, kp]; FL1 = succ(np.sqrt(succ(succ(Sf["Lx"][ks, kp] ** 2) + succ(Sf["Ly"][ks, kp] ** 2))) * (1 + 2 * U)); FL2 = Sf["L2"][ks, kp]
                            else:                                                            # straddling (or no tau model): v1 bounds
                                regime = "straddle"
                                G2F = succ(np.sqrt(succ(succ(succ(Sg[(2, 0)][ks, kp] ** 2) + succ(2 * succ(Sg[(1, 1)][ks, kp] ** 2))) + succ(Sg[(0, 2)][ks, kp] ** 2))) * (1 + 2 * U))
                                T0, T1, TL, T2F, TL1, TL2 = TQ["T0"], TQ["T1"], TQ["TL"], TQ["T2F"], TQ["TL1"], TQ["TL2"]
                                F0 = succ(T0 * G0); F1 = succ(succ(T0 * G1) + succ(T1 * G0))
                                FL = succ(succ(succ(T0 * GL) + succ(2 * succ(T1 * G1))) + succ(G0 * TL))
                                FL1 = succ(succ(succ(succ(succ(T1 * GL) + succ(T0 * GL1)) + succ(2 * succ(T2F * G1))) + succ(2 * succ(G2F * T1))) + succ(succ(G1 * TL) + succ(G0 * TL1)))
                                FL2 = succ(succ(succ(succ(succ(T0 * GL2) + succ(G0 * TL2)) + succ(2 * succ(TL * GL))) + succ(4 * succ(T1 * GL1))) + succ(succ(4 * succ(G1 * TL1)) + succ(4 * succ(T2F * G2F))))
                            regime_count[regime] += 1
                            for lam in lams:
                                l2 = lam * lam; l4 = l2 * l2
                                a3 = succ(succ(l2 * succ(succ(l2 * F0) + FL) ** 2) + succ(succ(succ(l2 * F1) + FL1) ** 2))
                                a4 = succ(succ(succ(succ(l4 * F0) + succ(2 * succ(l2 * FL))) + FL2) ** 2)
                                acc[lam]["I3"] = succ(acc[lam]["I3"] + succ(area * a3)); acc[lam]["I4"] = succ(acc[lam]["I4"] + succ(area * a4))
                            G2F_row = succ(np.sqrt(succ(succ(succ(Sg[(2, 0)][ks, kp] ** 2) + succ(2 * succ(Sg[(1, 1)][ks, kp] ** 2))) + succ(Sg[(0, 2)][ks, kp] ** 2))) * (1 + 2 * U))
                            rows.append(dict(ci=ci, q=A["q"], bs=bs, bp=bp, ks=ks, kp=kp, regime=regime, dmin=dmin, dmax=dmax, area=float(area), sigma=[slo, shi],
                                             F0=float(F0), F1=float(F1), FL=float(FL), FL1=float(FL1), FL2=float(FL2), G0=float(G0), G1=float(G1), G2F=float(G2F_row), GL=float(GL), GL1=float(GL1), GL2=float(GL2),
                                             T0=TQ["T0"], T1=TQ["T1"], T2F=TQ["T2F"], TL=TQ["TL"], TL1=TQ["TL1"], TL2=TQ["TL2"],
                                             tau_sup=float(Sf["tau"][ks, kp]) if have_tau else None,
                                             rem_D={"%d_%d" % k: float(D[k].r) for k in keys}, rem_lap=[float(lapg_c.r), float(lapgx_c.r), float(lapgy_c.r), float(lap2g_c.r)],
                                             rem_f=([float(f.r), float(fx.r), float(fy.r), float(lapf.r), float(lapfx.r), float(lapfy.r), float(lap2f.r)] if have_tau else None),
                                             rem_tau=([float(tau.r), float(tx.r), float(ty.r), float(lapt.r), float(laptx.r), float(lapty.r), float(lap2t.r)] if have_tau else None),
                                             series=([c0, float(xr), float(tail)] if have_tau else None)))
                    tim["geo"] += time.time() - tb2
        print("radial cell %d/%d ci=%d remA %.1e rem_eps4 %.1e | I3 %.4g I4 %.4g (lam=1) | regimes %s | worst series x %.3f tail %.1e | timers rec %.0f tau %.0f geo %.0f (%.0fs)" % (
            idx + 1, len(cells), ci, res["remA"], res["rem_eps_4"], acc[1.0]["I3"], acc[1.0]["I4"], regime_count, worst["x_series"], worst["tail"], tim["rec"], tim["tau"], tim["geo"], time.time() - t0), flush=True)
    results = {str(lam): finish(lam, acc[lam]["I3"], acc[lam]["I4"]) for lam in lams}
    out_d = dict(green=green, trial=trial, delta=str(dfrac), cutoff=cutoff, cutoff_smoothness="C^%d" % cut.smooth, cutoff_poly_step=STEP_POLY[cutoff],
                 s=S_ORDER, KSUB=KSUB, ntheta=ntheta, KP=KP, Qs=Qs, Qp=Qp, nbs=nbs, nbp=nbp, Kser=Kser, theta_max=theta_max_f, radial_cells=[int(cells[0]), int(cells[-1])],
                 radial_cells_cover=cover, chunk=[int(c) for c in cells], qchunk=list(qchunk) if qchunk is not None else [0, ntheta - 1], partial=(chunk is not None or qchunk is not None), x_star_bracket=[XSTAR_LO, XSTAR_HI],
                 n_angular_cells=ntheta, n_radial_cells=len(cells), n_subcells_in_support=sum(regime_count[k] for k in ("inside", "transition", "straddle")),
                 regime_count=regime_count, worst_series=worst, area_sum={k: float(v) for k, v in area_tot.items()}, results=results,
                 sup_D_eps={ball: {"%d_%d" % k: supD[ball][k] for k in keys} for ball in supD}, where={ball: {"%d_%d" % k: v for k, v in where[ball].items()} for ball in where},
                 cells=rows, code_version="cert_forcing2.py v2.2 (2026-10-21 shift 4; v2.1 + additive eta allowance in the jet remainder sums, full row fields)", time=time.time() - t0, done=True)
    json.dump(out_d, open(out, "w"), indent=1)
    print("\nRESULTS v2 (rigorous upper bounds), delta = %s, cutoff %s:" % (dfrac, cutoff))
    for lam in lams:
        r = results[str(lam)]
        print("  lam = %g: I3 <= %.6g, I4 <= %.6g;  order-3 <= %.5g, order-4 <= %.5g,  ORDER-3.1 BOUND <= %.5g" % (lam, r["I3"], r["I4"], r["bound_order3"], r["bound_order4"], r["bound_order_3_1"]))
    print("  regimes:", regime_count, " worst series ratio %.3f, worst tail %.2e" % (worst["x_series"], worst["tail"]))
    for ball in ("B94", "B3"):
        print("  sup |D^alpha eps~| on %s: " % ball + ", ".join("%d%d: %.3e" % (k[0], k[1], supD[ball][k]) for k in keys))
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    if a[1] == "merge":
        merge(a[3:], a[2])
    else:
        args = a[4:]
        delta_str = args[0] if len(args) > 0 else "33/2000"; cutoff = args[1] if len(args) > 1 else "p9"
        ints = [int(x) for x in args[2:]]
        KSUB, ntheta, KP, Qp, nbs, nbp, Kser = (ints + [64, 16, 8, 8, 2, 2, 16][len(ints):])[:7]
        chunk = (ints[7], ints[8]) if len(ints) > 8 else None
        qchunk = (ints[9], ints[10]) if len(ints) > 10 else None          # optional angular chunk q_lo q_hi (the parts are merged by merge())
        main(a[1], a[2], a[3], delta_str, cutoff, KSUB, ntheta, KP, Qp, nbs, nbp, Kser, chunk, qchunk)
