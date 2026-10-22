"""N8 certificate (lead 00:06Z): rigorous upper bounds on B_{3 delta}(P), P = (x_*, 0), delta in DELTAS, of
  sup ||D^j V||_F (j = 1..4),  V = c_l X + grad^perp psi~  (d^alpha V_1 = -d^alpha psi_y, d^alpha V_2 = d^alpha psi_x for |alpha| >= 2),
  sup ||D^j rho~||_F (j = 0..5),  ||D^j f||_F^2 = sum_{a+b=j} C(j,a) (d_x^a d_y^b f)^2  (sum over i for V),
and C_V = 41.7 M_V + 3 M_rho (M_V = sup ||D^2 V||_F, M_rho = sup ||D^2 rho~||_F) against kappa/(2 delta) = 1.687/delta.

Method (all arithmetic rigorous: src/midrad.py mid-rad float64 with outward rounding; transcendental values in Arb (python-flint),
imported as mid/rad):
 1. Radial sub-cells [t_a, t_a + h] of data/cert_green.npz (certified A_n, B_n at the cell starts; exact spline polynomials of the
    a_m).  On each, Taylor models (degree Q in sigma = t - t_a, remainder) of psi_n^{(i)} (i <= 5) and R_j^{(i)} (i <= 5) exactly as in
    cert_resid._cell_core_deriv (A' = -2n A + g, B' = 2n B - g differentiated exactly; R_j^{(i)} exact exponential-polynomials).
 2. Each radial sub-cell is split into KSUB equal sub-intervals; on each, the two-sided range of every mode derivative by the
    re-centred Bernstein enclosure (+ remainder) -> an MR interval per (sub-interval, mode, i).
 3. Angular cells [theta_k, theta_{k+1}], theta_k = k theta_max/ntheta (exact reals, Arb balls).  The ranges of sin(f theta + l pi/2) over a cell
    (f = 2j+1 for rho, 2n for psi, f = 1 for the coordinate factors) are Arb enclosures of sin and cos evaluated on the ball covering the
    cell (sin_cos of a ball argument; rigorous, second-order tight at critical points).
 4. (t,theta)-jets on every (sub-interval x angular cell): d_t^i d_theta^l rho~ = sum_j R_j^{(i)} (2j+1)^l sin((2j+1) theta + l pi/2), same for
    psi~ with 2n: MR interval products and rigorous sums over the modes (midrad.MR.sum).
 5. Cartesian derivatives by the exact recursion d_x = e^{-t}(cos th d_t - sin th d_th), d_y = e^{-t}(sin th d_t + cos th d_th) applied to
    the (t,theta)-jets (TrialJets.polar_to_cart re-implemented on MR intervals; the coefficient fields e^{-t} cos(th + b pi/2) etc. are MR
    ranges over the cell).  Then the Frobenius norms (upper bounds: mag of the entries) per cell, and the maximum over the cells meeting
    B_{3 delta}(P) (a cell is included if a RIGOROUS lower bound (MR arithmetic, certified x_* bracket, Arb cos/sin at the cell edge) of its
    distance to P is <= 3 delta; over-inclusion is safe).  The radial sub-intervals used for the mode ranges and for the coordinate factors
    are the same exact intervals I_kk = [kk hk_f, (kk+1) hk_f], hk_f = succ(h/KSUB).  Entries for delta > delta_max are marked PARTIAL.
    The ball B_{3 delta}(P) also contains points with y < 0; by the parity of rho~ (odd in y) and psi~ (odd in y), every |d_x^a d_y^b f| is
    even in y, so the quadrant theta in [0, theta_max] suffices.  Coverage of r in [x_* - 3 delta_max, x_* + 3 delta_max] and
    theta in [0, asin(3 delta_max/x_*)] is checked explicitly.
Usage: python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz out.json [KSUB=4] [ntheta=350] [delta_max=0.2]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb, factorial
from flint import arb, ctx
from midrad import MR, mr_matmul, succ, U, ETA
from cert_resid import Certifier, TMArr, tm_exp, mag

XSTAR_LO, XSTAR_HI = 8.60006380515688, 8.600063805157474       # certified bracket of x_* (runs/axis_cell.json, S1)
XSTAR = 0.5 * (XSTAR_LO + XSTAR_HI)
XRAD = float(np.nextafter(max(XSTAR_HI - XSTAR, XSTAR - XSTAR_LO), np.inf))     # radius enclosing both bracket ends
DELTAS = [0.0165, 0.05, 0.1, 0.2]
if os.environ.get('N8_DELTAS'): DELTAS = [float(x) for x in os.environ['N8_DELTAS'].split(',')]   # optional override
NDER = 5


def pred(x): return -succ(-np.asarray(x, float))


def mode_derivative_tms(C, h_up, e_ta, a_terms, A0, B0, nder=NDER):
    """TMs psi[i] (i <= nder; TMArr over n) and Rd[i] (i <= nder + 1; TMArr over j) on [0, h]; copy of the first part of
    cert_resid._cell_core_deriv (same identities, same remainders)."""
    Q = C.Q; n = C.n
    hpow = np.array([1.0] + [succ(h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Q + 3)])
    f_terms, R_terms = C.f_terms_from_a(a_terms)
    e2 = e_ta * e_ta; e3 = e2 * e_ta; e4 = e2 * e2

    def bc(c, r, S):
        return TMArr(MR(np.broadcast_to(c.m, (S, Q + 1)).copy(), np.broadcast_to(c.r, (S, Q + 1)).copy()), np.full(S, r))

    def zero_tm(S):
        return TMArr(MR(np.zeros((S, Q + 1)), np.zeros((S, Q + 1))), np.zeros(S))

    def poly_deriv(P):
        dm = np.zeros_like(P.m); dr = np.zeros_like(P.r)
        if P.m.shape[0] > 1:
            dm[:-1] = P.m[1:] * np.arange(1, P.m.shape[0])[:, None]; dr[:-1] = succ(P.r[1:] * np.arange(1, P.m.shape[0])[:, None] + U * np.abs(dm[:-1]))
        return MR(dm, dr)

    g_list = [zero_tm(C.Nf) for _ in range(nder + 1)]; gsup = np.zeros((C.Nf, Q + 1))
    for alpha, F in f_terms:
        gam = alpha + MR.exact(4.0); gabs = float(gam.mag()); Ec, Er = tm_exp(gam, h_up, Q); E = bc(Ec, Er, C.Nf)
        Fi = MR(F.m.T, F.r.T)
        Fsup = C.poly_derivative_sups(F, hpow); degF = F.m.shape[1] - 1
        x = succ(gabs * h_up); assert x <= 1.0; egh = succ(1 + x + x * x)
        for i in range(Q + 1):
            s_ = np.zeros(C.Nf)
            for kk in range(min(i, degF) + 1):
                s_ = succ(s_ + succ(comb(i, kk) * succ(gabs ** (i - kk) * (1 + 2 * (i - kk) * U)) * Fsup[:, kk]))
            gsup[:, i] = succ(gsup[:, i] + succ(s_ * egh * (1 + 4 * (Q + 1) * U)))
        for i in range(nder + 1):
            g_list[i] = g_list[i] + E.mul_poly(MR(Fi.m.T, Fi.r.T), hpow)
            Fi = Fi * gam + poly_deriv(Fi)
    g_list = [gi.scale(e4) for gi in g_list]; gsup = succ(gsup * mag(e4) * (1 + 4 * U))
    A = [C.ode_tm(A0, g_list[0], gsup, -2.0 * n, h_up)]; B = [C.ode_tm(B0, g_list[0], gsup, 2.0 * n, h_up, gsign=-1.0)]
    m2n = MR(-2.0 * n, 0.0); p2n = MR(2.0 * n, 0.0)
    for i in range(nder):
        A.append(A[-1].scale(m2n) + g_list[i]); B.append(B[-1].scale(p2n) - g_list[i])
    inv4n = MR(1.0 / (4 * n), succ(U / (4 * n)))
    psi = [(A[i] + B[i]).scale(inv4n) for i in range(nder + 1)]
    Rd = [zero_tm(C.M + 1) for _ in range(nder + 2)]
    for alpha, Rc, dR in R_terms:
        a3 = alpha + MR.exact(3.0); Ec, Er = tm_exp(a3, h_up, Q); E = bc(Ec, Er, C.M + 1)
        Ri = Rc
        for i in range(nder + 2):
            Rd[i] = Rd[i] + E.mul_poly(MR(Ri.m.T, Ri.r.T), hpow)
            Ri = Ri * a3 + poly_deriv(Ri)
    Rd = [r_.scale(e3) for r_ in Rd]
    return psi, Rd, hpow, dict(remA=float(A[0].r.max()), remB=float(B[0].r.max()))


def poly_range_subs(C, tm, h_up, K):
    """Two-sided outward ranges of the TM 'tm' (coefficients (A, Q+1), remainders (A,)) on the K sub-intervals [kk hk, (kk+1) hk] of
    [0, h] (hk = h/K rounded up; Bernstein bound on a slightly longer interval is valid for the longer interval and hence for the exact one).
    Returns MR of shape (K, A)."""
    Q = C.Q; A = tm.c.m.shape[0]; hk = succ(h_up / K); hkP = C.mr_powers(hk, Q)
    lo_ = np.zeros((K, A)); hi_ = np.zeros((K, A))
    for kk in range(K):
        a = kk * hk; apow = [MR.exact(1.0)]
        for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
        cm = np.zeros_like(tm.c.m); cr = np.zeros_like(tm.c.r)
        for j in range(Q + 1):
            acc = MR(np.zeros(A), np.zeros(A))
            for i in range(j, Q + 1): acc = acc + tm.c[..., i] * MR.exact(float(comb(i, j))) * apow[i - j]
            cm[:, j] = acc.m; cr[:, j] = acc.r
        ah = MR(cm, cr) * MR(hkP.m[None, :], hkP.r[None, :])
        b = mr_matmul(ah, MR(C.Bern.m.T, C.Bern.r.T))
        lo_[kk] = pred(pred((b.m - b.r).min(-1)) - tm.r); hi_[kk] = succ(succ((b.m + b.r).max(-1)) + tm.r)
    mid = 0.5 * (lo_ + hi_); rad = succ(succ(np.maximum(hi_ - mid, mid - lo_)) * succ(1 + 4 * U))
    return MR(mid, rad)


class Angular:
    """Exact angular grid theta_k = k theta_max/ntheta (Arb balls of the exact reals) and rigorous ranges of sin(f theta + l pi/2), f in freqs,
    over each cell [theta_k, theta_{k+1}]: direct Arb evaluation of sin and cos on the ball covering the cell (the union of the two endpoint
    balls), f exact integers.  Arb's enclosure of sin/cos on a ball is rigorous (and second-order tight near critical points)."""
    def __init__(self, theta_max_arb, ntheta, freqs):
        ctx.prec = 128
        self.ntheta = ntheta; self.freqs = np.asarray(freqs, float)
        dth = theta_max_arb / ntheta
        self.theta_k = [dth * k for k in range(ntheta + 1)]
        self.dth_up = float(np.nextafter(float(dth.upper()), np.inf))
        F = len(freqs); S = np.zeros((ntheta, F)); Sr = np.zeros((ntheta, F)); Cm = np.zeros((ntheta, F)); Cr = np.zeros((ntheta, F))
        for k in range(ntheta):
            cell = self.theta_k[k].union(self.theta_k[k + 1])
            for q, f in enumerate(freqs):
                x = cell * int(f); s_, c_ = x.sin_cos()
                S[k, q] = float(s_.mid()); Sr[k, q] = float(s_.rad()); Cm[k, q] = float(c_.mid()); Cr[k, q] = float(c_.rad())
        # conversion of the Arb mid/rad to doubles: |float(mid) - mid| <= u |mid| + eta/2, radius rounded up
        self.S = MR(S, succ(succ(succ(Sr) + succ(U * np.abs(S))) + ETA)); self.Cc = MR(Cm, succ(succ(succ(Cr) + succ(U * np.abs(Cm))) + ETA))
        self.theta_lo = np.array([float(th.lower()) for th in self.theta_k]); self.theta_hi = np.array([float(th.upper()) for th in self.theta_k])

    def ranges(self, l):
        """MR (ntheta, F) range of sin(f theta + l pi/2) over the cells: l mod 4 = 0: sin, 1: cos, 2: -sin, 3: -cos."""
        l = l % 4
        base = self.S if l in (0, 2) else self.Cc
        return MR(-base.m, base.r) if l >= 2 else MR(base.m.copy(), base.r.copy())


def cart_from_polar_mr(J, order, emt, cos_b, sin_b):
    """J: dict (i,l) -> MR (S) jets d_t^i d_th^l f, i + l <= order; emt: MR range of e^{-t}; cos_b[b], sin_b[b]: MR ranges of
    cos(th + b pi/2), sin(th + b pi/2) (b <= order).  Returns dict (a,b) -> MR range of d_x^a d_y^b f, a + b <= order.
    Identical recursion to TrialJets.polar_to_cart (d_t^a d_th^b of e^{-t} cos th = (-1)^a e^{-t} cos(th + b pi/2), etc.)."""
    def coef(kind, a, b):
        ang = cos_b[b] if kind == "c" else sin_b[b]
        return (emt * ang) * MR.exact((-1.0) ** a)
    def apply(Fj, ordr, which):
        out = {}
        for i in range(ordr):
            for j in range(ordr - i):
                acc = None
                for a in range(i + 1):
                    for b in range(j + 1):
                        cc = MR.exact(float(comb(i, a) * comb(j, b)))
                        if which == "x":
                            term = coef("c", a, b) * Fj[(i - a + 1, j - b)] - coef("s", a, b) * Fj[(i - a, j - b + 1)]
                        else:
                            term = coef("s", a, b) * Fj[(i - a + 1, j - b)] + coef("c", a, b) * Fj[(i - a, j - b + 1)]
                        term = term * cc
                        acc = term if acc is None else acc + term
                out[(i, j)] = acc
        return out
    D = {(0, 0): J[(0, 0)]}
    cache = {(0, 0): (J, order)}
    for a in range(order + 1):
        for b in range(order + 1 - a):
            if a == 0 and b == 0: continue
            if b == 0:
                Fj, ordr = cache[(a - 1, 0)]; cur = apply(Fj, ordr, "x"); cache[(a, 0)] = (cur, ordr - 1)
            else:
                Fj, ordr = cache[(a, b - 1)]; cur = apply(Fj, ordr, "y"); cache[(a, b)] = (cur, ordr - 1)
            D[(a, b)] = cur[(0, 0)]
    return D


def main(green, trial, out, KSUB=4, ntheta=350, delta_max=0.2):
    t0 = time.time()
    C = Certifier(green, trial, Q=12)
    deltas = [d for d in DELTAS if d <= delta_max]                      # only balls covered by the cells are reported (no partial entries; strict, referee round 2)
    if len(deltas) < len(DELTAS): print('note: deltas > delta_max dropped (their balls would not be covered):', [d for d in DELTAS if d not in deltas], flush=True)
    ctx.prec = 128
    xs = arb(XSTAR, XRAD)
    R3 = 3 * delta_max
    # angular extent of B_{R3}(P) seen from the origin: asin(R3/x_*) (tangent lines); theta_max an exact double >= its upper bound x 1.000001
    theta_max_f = float(np.nextafter(float(((arb(R3) / xs).asin() * arb("1.000001")).upper()), np.inf)); theta_max = arb(theta_max_f)
    # radial cells meeting [x_* - R3, x_* + R3]: t_lo_need/t_hi_need are rigorous lower/upper bounds of log(x_* -/+ R3)
    t_lo_need = float(pred(float((xs - R3).log().lower()))); t_hi_need = float(succ(float((xs + R3).log().upper())))   # outward after the double conversion
    tb_lo = C.tb.lower(); tb_hi = C.tb.upper()
    cells = [ci for ci in range(C.nc) if tb_hi[ci + 1] > t_lo_need and tb_lo[ci] < t_hi_need]
    # coverage: the first selected cell starts at or before log(x_* - R3) (its start's UPPER bound <= the LOWER bound of the target) and the last
    # selected cell ends at or after log(x_* + R3); consecutive cells share the boundary array tb, so the union is the interval [tb[c0], tb[c1+1]]
    assert tb_hi[cells[0]] <= t_lo_need and tb_lo[cells[-1] + 1] >= t_hi_need, "radial coverage"
    assert cells == list(range(cells[0], cells[-1] + 1)), "cells contiguous"   # abutting by construction (shared boundary array tb)
    print("radial cells %d (ci %d..%d, r in [%.5f, %.5f]); theta_max %.6f; ntheta %d; KSUB %d" % (
        len(cells), cells[0], cells[-1], np.exp(tb_lo[cells[0]]), np.exp(tb_hi[cells[-1] + 1]), float(theta_max.mid()), ntheta, KSUB), flush=True)
    # angular structures
    f_rho = 2.0 * np.arange(C.M + 1) + 1.0; f_psi = 2.0 * C.n
    ang_rho = Angular(theta_max, ntheta, f_rho); ang_psi = Angular(theta_max, ntheta, f_psi); ang_one = Angular(theta_max, ntheta, [1.0])
    print("angular Arb tables done (%.0fs)" % (time.time() - t0), flush=True)
    # angular factor ranges per l: (2j+1)^l sin((2j+1) th + l pi/2) etc.; shapes (ntheta, F)
    FAC_rho = []; FAC_psi = []
    for l in range(NDER + 1):
        FAC_rho.append(ang_rho.ranges(l) * MR.exact(f_rho[None, :] ** l)); FAC_psi.append(ang_psi.ranges(l) * MR.exact(f_psi[None, :] ** l))
    cos_b = [ang_one.ranges(l + 1)[:, 0] for l in range(NDER + 2)]      # cos(th + b pi/2) = sin(th + (b+1) pi/2)
    sin_b = [ang_one.ranges(l)[:, 0] for l in range(NDER + 2)]
    # per-delta accumulators
    keys = ["V1", "V2", "V3", "V4", "rho0", "rho1", "rho2", "rho3", "rho4", "rho5"]
    best = {d: {k: 0.0 for k in keys} for d in deltas}; where = {d: {} for d in deltas}; ncell = {d: 0 for d in deltas}
    cell_rows = []
    th_lo_c = ang_one.theta_lo[:-1]; th_hi_c = ang_one.theta_hi[1:]
    XS_MR = MR(XSTAR, XRAD)                                               # certified bracket of x_* (ball containing both ends)
    COS1 = MR.from_arb([th.cos() for th in ang_one.theta_k[:-1]]); SIN1 = MR.from_arb([th.sin() for th in ang_one.theta_k[:-1]])   # at the lower edges
    for idx, ci in enumerate(cells):
        h = C.tb[ci + 1] - C.tb[ci]; h_up = h.mag()
        assert succ(2.0 * C.Nf * h_up) <= 1.0, 'ODE remainder hypothesis 2 Nf h <= 1'
        psi, Rd, hpow, rems = mode_derivative_tms(C, h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], NDER)
        # ranges per sub-interval: (KSUB, modes)
        PSI_R = [poly_range_subs(C, psi[i], h_up, KSUB) for i in range(NDER + 1)]
        RHO_R = [poly_range_subs(C, Rd[i], h_up, KSUB) for i in range(NDER + 1)]
        # e^{-t} ranges per sub-interval (Arb): t in [t_a + kk hk, t_a + (kk+1) hk] with t_a the ball tb[ci]
        # common sub-interval I_kk = [kk hk_f, (kk+1) hk_f] (exact reals from the double hk_f = succ(h_up/KSUB), the same as in poly_range_subs;
        # the union over kk is [0, KSUB hk_f] which contains [0, h]).  Validity domain: J_kk = I_kk n [0, h]: at every sigma in J_kk the polynomial
        # part lies in its Bernstein range over I_kk and the Taylor-model remainder (derived on [0, h_up] >= [0, h]) applies; the coordinate
        # factors are enclosed over t_a + I_kk; the union of the J_kk is [0, h].  (The remainder is never used beyond h; referee round 2.)
        ta = arb(float(C.d["tb"][ci]), float(C.d["tb_rad"][ci])); hk_f = succ(h_up / KSUB); hk = arb(hk_f)
        assert (hk * KSUB).lower() >= arb(h_up), "sub-intervals cover the cell"           # compared in Arb (referee round 2)
        emt_list = []; r_lo = np.zeros(KSUB); r_hi = np.zeros(KSUB)
        for kk in range(KSUB):
            tcell = (ta + hk * kk).union(ta + hk * (kk + 1))        # ball covering ta + I_kk (Arb union = hull of the two balls)
            e_ = (-tcell).exp(); emt_list.append(e_)
            r_lo[kk] = float(pred(float(tcell.exp().lower()))); r_hi[kk] = float(succ(float(tcell.exp().upper())))   # outward after the double conversion
        emt = MR.from_arb(emt_list)                                           # (KSUB,)
        emt2 = MR(np.broadcast_to(emt.m[:, None], (KSUB, ntheta)).copy(), np.broadcast_to(emt.r[:, None], (KSUB, ntheta)).copy())
        cos2 = [MR(np.broadcast_to(c.m[None, :], (KSUB, ntheta)).copy(), np.broadcast_to(c.r[None, :], (KSUB, ntheta)).copy()) for c in cos_b]
        sin2 = [MR(np.broadcast_to(c.m[None, :], (KSUB, ntheta)).copy(), np.broadcast_to(c.r[None, :], (KSUB, ntheta)).copy()) for c in sin_b]
        # (t,theta)-jets: (KSUB, ntheta)
        Jrho = {}; Jpsi = {}
        for i in range(NDER + 1):
            for l in range(NDER + 1 - i):
                pr = MR(RHO_R[i].m[:, None, :], RHO_R[i].r[:, None, :]) * MR(FAC_rho[l].m[None, :, :], FAC_rho[l].r[None, :, :])
                Jrho[(i, l)] = pr.sum(axis=-1)
                pp = MR(PSI_R[i].m[:, None, :], PSI_R[i].r[:, None, :]) * MR(FAC_psi[l].m[None, :, :], FAC_psi[l].r[None, :, :])
                Jpsi[(i, l)] = pp.sum(axis=-1)
        Drho = cart_from_polar_mr(Jrho, NDER, emt2, cos2, sin2)
        Dpsi = cart_from_polar_mr(Jpsi, NDER, emt2, cos2, sin2)
        # Frobenius norm upper bounds per (sub-interval, angular cell)
        fro = {}
        for j in range(NDER + 1):
            acc = np.zeros((KSUB, ntheta))
            for a in range(j + 1):
                b = j - a; v = Drho[(a, b)].mag(); acc = succ(acc + succ(comb(j, a) * succ(v * v)))
            fro["rho%d" % j] = succ(np.sqrt(acc) * (1 + 2 * U))
        for j in range(1, NDER):
            acc = np.zeros((KSUB, ntheta))
            for a in range(j + 1):
                b = j - a
                v1 = -Dpsi[(a, b + 1)]; v2 = Dpsi[(a + 1, b)]
                if j == 1:
                    if a == 1: v1 = v1 + C.c_l
                    if b == 1: v2 = v2 + C.c_l
                m1 = v1.mag(); m2 = v2.mag()
                acc = succ(acc + succ(comb(j, a) * succ(succ(m1 * m1) + succ(m2 * m2))))
            fro["V%d" % j] = succ(np.sqrt(acc) * (1 + 2 * U))
        # RIGOROUS lower bound of the distance from P = (x_*, 0) to the polar cell [r1, r2] x [th1, th2] (th1 >= 0): for fixed r the distance
        # increases with theta on [0, pi], so the minimum is on the edge theta = th1, where d^2 = (r - x_* cos th1)^2 + (x_* sin th1)^2 and
        # min over r in [r1, r2] gives d^2 = dist(x_* cos th1, [r1, r2])^2 + (x_* sin th1)^2.  MR arithmetic with x_* the certified bracket,
        # cos th1, sin th1 Arb enclosures at the exact cell edge, r1 = Arb lower bound of e^t and r2 = Arb upper bound over the sub-interval
        # (a larger r-interval only lowers the bound).  dmin_lo = lower bound of d (rounded down); a cell counts if dmin_lo <= 3 delta.
        R1 = MR(np.broadcast_to(r_lo[:, None], (KSUB, ntheta)).copy()); R2 = MR(np.broadcast_to(r_hi[:, None], (KSUB, ntheta)).copy())
        xc = MR(np.broadcast_to((XS_MR * COS1).m[None, :], (KSUB, ntheta)).copy(), np.broadcast_to((XS_MR * COS1).r[None, :], (KSUB, ntheta)).copy())
        xsn = XS_MR * SIN1
        g1 = (R1 - xc).lower(); g2 = (xc - R2).lower()                      # lower bounds of r1 - x_* cos th1 and x_* cos th1 - r2
        g = np.maximum(0.0, np.maximum(g1, g2))                              # lower bound of dist(x_* cos th1, [r1, r2]) (max of lower bounds)
        d2_lo = pred(pred(g * g * (1 - 4 * U)) + pred((xsn.mig() ** 2)[None, :] * (1 - 4 * U)))
        dmin = pred(np.sqrt(np.maximum(d2_lo, 0.0)) * (1 - 4 * U))
        row = dict(ci=ci, t_a=float(C.tb.m[ci]), h=float(h_up), r_lo=float(r_lo.min()), r_hi=float(r_hi.max()), remA=rems["remA"], remB=rems["remB"],
                   rem_psi5=float(psi[NDER].r.max()), rem_R5=float(Rd[NDER].r.max()), cellmax={k: float(fro[k].max()) for k in keys})
        for d in deltas:
            m = dmin <= 3 * d
            if not m.any(): continue
            ncell[d] += int(m.sum())
            for k in keys:
                v = np.where(m, fro[k], 0.0); kk, q = np.unravel_index(int(np.argmax(v)), v.shape)
                if v[kk, q] > best[d][k]:
                    best[d][k] = float(v[kk, q]); where[d][k] = dict(ci=ci, r=[float(r_lo[kk]), float(r_hi[kk])], theta=[float(th_lo_c[q]), float(th_hi_c[q])])
        cell_rows.append(row)
        print("cell %d/%d ci=%d r=[%.5f, %.5f] |D2V|<=%.4g |D3V|<=%.4g |D4V|<=%.4g |D2rho|<=%.4g |D5rho|<=%.4g remA %.1e rem_psi5 %.1e (%.0fs)" % (
            idx, len(cells), ci, r_lo.min(), r_hi.max(), fro["V2"].max(), fro["V3"].max(), fro["V4"].max(), fro["rho2"].max(), fro["rho5"].max(), rems["remA"], psi[NDER].r.max(), time.time() - t0), flush=True)
        json.dump(dict(done=False, cells=cell_rows), open(out, "w"))
    # angular coverage check: theta_max >= asin(3 delta_max / x_*) by construction (factor 1.000001); report
    res = dict(green=green, trial=trial, KSUB=KSUB, ntheta=ntheta, delta_max=delta_max, theta_max=theta_max_f, x_star_bracket=[XSTAR_LO, XSTAR_HI], code_version="cert_n8.py v3 (2026-10-21T02:0xZ: v2 + robustness items of referee round 2: strict delta filter, outward double conversions of the coverage bounds and of r_lo/r_hi, Arb-side coverage assertion, validity-domain comment; arithmetic unchanged)",
               radial_cells=[int(cells[0]), int(cells[-1])], r_cover=[float(np.exp(tb_lo[cells[0]])), float(np.exp(tb_hi[cells[-1] + 1]))],
               method="see module docstring; rigorous upper bounds (mid-rad float64 + Arb), Frobenius norms with multinomial weights", deltas={}, cells=cell_rows, done=True, time=time.time() - t0)
    print("\n%-8s %7s %11s %11s %11s %11s | %11s %11s %11s %11s | %9s %9s" % ("delta", "ncells", "M_V=|D2V|", "|D3V|", "|D4V|", "M_rho", "|D3rho|", "|D4rho|", "|D5rho|", "|D1V|", "C_V", "1.687/d"))
    for d in deltas:
        CV = succ(succ(41.7 * best[d]["V2"]) + succ(3 * best[d]["rho2"]))
        ok = bool(CV <= 1.687 / d * (1 - 1e-12))
        complete = bool(d <= delta_max)        # the cells cover B_{3 delta_max}(P); entries with delta > delta_max are PARTIAL (not certificates)
        res["deltas"][str(d)] = dict(radius_3delta=3 * d, ncells=ncell[d], sup_bounds=best[d], where=where[d], C_V=float(CV), kappa_over_2delta=1.687 / d, C_V_ok=ok,
                                     complete_ball=complete, status="CERTIFICATE (ball covered)" if complete else "PARTIAL: delta > delta_max, ball not covered, NOT a certificate")
        print("%-8g %7d %11.5g %11.5g %11.5g %11.5g | %11.5g %11.5g %11.5g %11.5g | %9.4g %9.4g %s %s" % (d, ncell[d], best[d]["V2"], best[d]["V3"], best[d]["V4"], best[d]["rho2"], best[d]["rho3"], best[d]["rho4"], best[d]["rho5"], best[d]["V1"], CV, 1.687 / d, "OK" if ok else "FAIL", "" if complete else "PARTIAL (ball not covered)"))
    json.dump(res, open(out, "w"), indent=1)
    print("done %.0fs -> %s" % (time.time() - t0, out))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], int(a[4]) if len(a) > 4 else 4, int(a[5]) if len(a) > 5 else 350, float(a[6]) if len(a) > 6 else 0.2)
