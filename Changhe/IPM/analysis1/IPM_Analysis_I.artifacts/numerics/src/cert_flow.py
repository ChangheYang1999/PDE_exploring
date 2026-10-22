"""Rigorous 2D bounds for the trial velocity field (lead request N1', notes/global_flow.md section 10), by Taylor models in t = log r
on the certificate's radial sub-cells and second-order angular Taylor models on angular cells.  REVISION 2 (after the astra referee
flow1, astra/flow1/answer.md): angular factors computed in Arb (no float trig allowances), outward rounding of every remainder and
magnitude sum, correct signed rounding of the V_1 bound, interval-valued mu by Arb hull, exact rational constants, Arb cell edges
covering [0, pi/2] exactly, the ODE step hypothesis 2 Nf h <= 1 asserted, coverage bookkeeping, s and axis-sign targets.

Quantities (polar; psi_n = stream modes (sin 2n theta), psi_r,n their r-derivatives):
  s     = X.V/r^2 = c_l - r^-2 sum_n 2n psi_n cos(2n theta)
  V_2/y = s + r^-1 sum_n psi_r,n C_n(theta),   C_n = cos theta sin(2n theta)/sin theta = 2 cos theta sum_{j<n} cos((2j+1) theta)
  V_1/x = s - r^-1 sum_n psi_r,n S_n(theta),   S_n = sin theta sin(2n theta)/cos theta = 2 sin theta sum_{j<n} (-1)^{n-1-j} sin((2j+1) theta)
  T_0   = -(1 + c_l) + a (V_1/x - s) + b (V_2/y - s) + mu(r) s,   mu(r) = gamma' + (a + b - gamma')/(1 + (r/R_m)^p)
with c_l := 1/k (the trial's exponent, as in the whole certificate), a = 129/20, b = 307/100, gamma' = 1129/1000, R_m = 6, p = 4 (exact
rationals, enclosed in Arb). Derivative bounds |D_n^{(k)}|, |E_n^{(k)}| <= 2 sum_{j<n} (2j+1)^k, hence |f'''| <= 2n + 6n^2 + 8n^3 + 4n^4 for
C_n and S_n, (2n)^3 for cos(2n theta); second-order Taylor models about the exact cell centre with |eta| <= d = (b - a)/2 (outward).
Per radial sub-cell: TMs of P_n = 2n psi_n e^{-2t} and R_n = psi_r,n e^{-t} in sigma = t - t_a (Certifier machinery of cert_resid.py;
hypothesis 2 Nf h <= 1 asserted); mode sums -> polynomials in (sigma, eta) with mid-rad coefficients; tensor Bernstein ranges (eta-Bernstein
coefficients q0 -+ q1 d + q2 d^2, q0 - q2 d^2; sigma on K sub-intervals). Box classification against B_1 = [x1, x2] x [0, y2] by the
Cartesian hull of the polar cell (Arb cos/sin bounds), adaptive angular bisection where a target fails.
Usage: python3 cert_flow.py green.npz trial.npz region(middle|outer|inner) out.json [ntheta] [ci_start ci_end|-] [region_green.npz]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb
from midrad import MR, mr_matmul, succ, U, ETA
from cert_resid import Certifier, TMArr, tm_exp, mag
from flint import arb, ctx

ctx.prec = 128
PAR = dict(a=(129, 20), b=(307, 100), gp=(1129, 1000), Rm=6.0, p=4, box=(4.80, 6.82, 2.85), kappa=0.2)
TARGETS = dict(m0=0.9, T_out=-0.22, T_in=1.30, V1_in=-13.0, kappa0=3.0, R0=20.0)
XSTAR = (8.600063805157177, 2.94e-13)          # S1 root enclosure (runs/scalars_full.json)


def pred(x): return -succ(-np.asarray(x, float))
def up(x): return float(np.nextafter(float(x.upper()), np.inf))
def lo(x): return float(np.nextafter(float(x.lower()), -np.inf))
def rat(p, q): return arb(p) / arb(q)
A_ARB, B_ARB, GP_ARB = rat(*PAR["a"]), rat(*PAR["b"]), rat(*PAR["gp"])
A_MR, B_MR, GP_MR = (MR.from_arb([x])[0] for x in (A_ARB, B_ARB, GP_ARB))
S_ARB = A_ARB + B_ARB


def bern_range(coef, hpow_mr, Bern):
    """coef: MR (A, Q+1) polynomial coefficients in sigma on [0, h]; returns outward (lo, hi) arrays (A,) of the range."""
    ah = coef * MR(hpow_mr.m[None, :], hpow_mr.r[None, :])
    b = mr_matmul(ah, MR(Bern.m.T, Bern.r.T))
    return pred((b.m - b.r).min(-1)), succ((b.m + b.r).max(-1))


class AngCache:
    """Second-order angular Taylor data of cos(2n th), C_n, S_n about the exact centre of a cell [a, b] (arb balls), computed in Arb."""
    def __init__(self, n):
        self.n = np.asarray(n); self.Nmax = int(self.n.max()); self.cache = {}
        self.jw = [arb(2 * j + 1) for j in range(self.Nmax)]

    def key(self, a, b): return (float(a.mid()), float(a.rad()), float(b.mid()), float(b.rad()))

    def factors(self, a, b):
        k = self.key(a, b)
        if k in self.cache: return self.cache[k]
        thc = (a + b) / 2; d_arb = (b - a) / 2; d = up(d_arb)
        c, s_ = thc.cos(), thc.sin()
        cj = [(w * thc).cos() for w in self.jw]; sj = [(w * thc).sin() for w in self.jw]
        D0 = [arb(0)]; D1 = [arb(0)]; D2 = [arb(0)]; E0 = [arb(0)]; E1 = [arb(0)]; E2 = [arb(0)]
        for j in range(self.Nmax):
            w = self.jw[j]; sg = arb(1) if j % 2 == 0 else arb(-1)
            D0.append(D0[-1] + 2 * cj[j]); D1.append(D1[-1] - 2 * w * sj[j]); D2.append(D2[-1] - 2 * w * w * cj[j])
            E0.append(E0[-1] + sg * sj[j]); E1.append(E1[-1] + sg * w * cj[j]); E2.append(E2[-1] + sg * w * w * sj[j])
        out = {}
        for fam in ("cos", "C", "S"):
            F0 = []; F1 = []; F2 = []
            for nn in self.n:
                nn = int(nn)
                if fam == "cos":
                    x = 2 * nn * thc; F0.append(x.cos()); F1.append(-2 * nn * x.sin()); F2.append(-2 * nn * nn * x.cos())
                elif fam == "C":
                    F0.append(c * D0[nn]); F1.append(-s_ * D0[nn] + c * D1[nn]); F2.append((-c * D0[nn] - 2 * s_ * D1[nn] + c * D2[nn]) / 2)
                else:
                    pre = arb(2) * (arb(1) if (nn - 1) % 2 == 0 else arb(-1))
                    e0 = pre * E0[nn]; e1 = pre * E1[nn]; e2 = -pre * E2[nn]
                    F0.append(s_ * e0); F1.append(c * e0 + s_ * e1); F2.append((-s_ * e0 + 2 * c * e1 + s_ * e2) / 2)
            nn = self.n.astype(float)
            rem = succ(((2 * nn) ** 3 if fam == "cos" else (2 * nn + 6 * nn ** 2 + 8 * nn ** 3 + 4 * nn ** 4)) * succ(d ** 3) / 6 * (1 + 16 * U))
            out[fam] = (MR.from_arb(F0), MR.from_arb(F1), MR.from_arb(F2), rem)
        out["d"] = d; out["cos_a"] = (lo(a.cos()), up(a.cos())); out["cos_b"] = (lo(b.cos()), up(b.cos()))
        out["sin_a"] = (lo(a.sin()), up(a.sin())); out["sin_b"] = (lo(b.sin()), up(b.sin())); out["a_lo"] = lo(a); out["b_hi"] = up(b)
        self.cache[k] = out
        return out


class FlowCertifier(Certifier):
    def psi_tms(self, h_up, e_ta, a_terms, A0, B0):
        """TMs (over modes n) of P_n = 2n psi_n e^{-2t} and R_n = psi_r,n e^{-t} on the sub-cell [0, h]; returns (P, R, hpow).
        Hypothesis of the inherited ODE remainder: 2 Nf h <= 1 (asserted)."""
        Q = self.Q; n = self.n
        assert succ(2.0 * self.Nf * h_up) <= 1.0, "ODE remainder hypothesis 2 Nf h <= 1 violated"
        hpow = np.array([1.0] + [succ(h_up ** i * (1 + 2 * i * U)) for i in range(1, 2 * Q + 3)])
        f_terms, R_terms = self.f_terms_from_a(a_terms)
        e2 = e_ta * e_ta; e4 = e2 * e2
        inv_e = MR(1.0 / e_ta.m, succ(e_ta.r / (e_ta.mig() ** 2) + U * abs(1.0 / e_ta.m))); inv_e2 = inv_e * inv_e
        def bc(c, r, S):
            return TMArr(MR(np.broadcast_to(c.m, (S, Q + 1)).copy(), np.broadcast_to(c.r, (S, Q + 1)).copy()), np.full(S, r))
        def zero_tm(S):
            return TMArr(MR(np.zeros((S, Q + 1)), np.zeros((S, Q + 1))), np.zeros(S))
        g = zero_tm(self.Nf); gsup = np.zeros((self.Nf, Q + 1))
        for alpha, F in f_terms:
            gam = alpha + MR.exact(4.0); gabs = float(gam.mag())
            Ec, Er = tm_exp(gam, h_up, Q)
            g = g + bc(Ec, Er, self.Nf).mul_poly(F, hpow)
            Fsup = self.poly_derivative_sups(F, hpow)
            x = succ(gabs * h_up); assert x <= 1.0; egh = succ(1 + x + x * x); degF = F.m.shape[1] - 1
            for i in range(Q + 1):
                s_ = np.zeros(self.Nf)
                for kk in range(min(i, degF) + 1):
                    s_ = succ(s_ + succ(comb(i, kk) * succ(gabs ** (i - kk) * (1 + 2 * (i - kk) * U)) * Fsup[:, kk]))
                gsup[:, i] = succ(gsup[:, i] + succ(s_ * egh * (1 + 4 * (Q + 1) * U)))
        g = g.scale(e4); gsup = succ(gsup * mag(e4) * (1 + 4 * U))
        A = self.ode_tm(A0, g, gsup, -2.0 * n, h_up)
        B = self.ode_tm(B0, g, gsup, 2.0 * n, h_up, gsign=-1.0)
        inv4n = MR(1.0 / (4 * n), succ(U / (4 * n)))
        psi = (A + B).scale(inv4n)
        Em1c, Em1r = tm_exp(-1.0, h_up, Q); Em2c, Em2r = tm_exp(-2.0, h_up, Q)
        Em1 = bc(Em1c, Em1r, self.Nf); Em2 = bc(Em2c, Em2r, self.Nf)
        def tm_mul(X, Y):
            Z = X.mul_poly(Y.c, hpow); return TMArr(Z.c, succ(Z.r + succ(X.sup(hpow) * Y.r)))
        dpsi_r = tm_mul((B - A).scale(inv_e * MR.exact(0.5)), Em1)                 # psi_r,n = (B-A) e^{-t} / 2
        P = tm_mul(psi.scale(MR(2.0 * n, 0.0) * inv_e2), Em2)                         # 2n psi_n e^{-2t}
        R = tm_mul(dpsi_r.scale(inv_e), Em1)                                          # psi_r,n e^{-t}
        return P, R, hpow

    def poly_range_sub(self, coef, h_up, K):
        """Outward two-sided range over [0, h] of MR polynomials (A, Q+1) by Bernstein on K sub-intervals (re-centred)."""
        from math import comb as _comb
        Q = self.Q; A = coef.m.shape[0]; hk = succ(h_up / K); hkP = self.mr_powers(hk, Q)
        lo_ = np.full(A, np.inf); hi_ = np.full(A, -np.inf)
        for kk in range(K):
            a = kk * hk; apow = [MR.exact(1.0)]
            for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
            cm = np.zeros_like(coef.m); cr = np.zeros_like(coef.r)
            for j in range(Q + 1):
                acc = MR(np.zeros(A), np.zeros(A))
                for i in range(j, Q + 1): acc = acc + coef[..., i] * MR.exact(float(_comb(i, j))) * apow[i - j]
                cm[:, j] = acc.m; cr[:, j] = acc.r
            l_, h_ = bern_range(MR(cm, cr), hkP, self.Bern)
            lo_ = np.minimum(lo_, l_); hi_ = np.maximum(hi_, h_)
        return lo_, hi_

    def cell_bounds(self, P, R, hpow, h_up, cells, ang, muM, K=2):
        """cells: list of (a, b) arb edges. Outward ranges over [0,h] x [a,b] of s, V2/y, V1/x, T0 (dict of arrays (A,))."""
        Q = self.Q; A = len(cells); Nf = self.Nf
        fac = [ang.factors(a, b) for (a, b) in cells]
        def stackF(fam, k):
            return MR(np.stack([f[fam][k].m for f in fac]), np.stack([f[fam][k].r for f in fac]))
        dvec = np.array([f["d"] for f in fac])
        remF = {fam: np.stack([f[fam][3] for f in fac]) for fam in ("cos", "C", "S")}
        cl = self.c_l
        def sums(fam, TM):
            out = [mr_matmul(stackF(fam, k), TM.c) for k in range(3)]
            supTM = TM.sup(hpow)
            facmag = succ(succ(succ(mag(stackF(fam, 0)) + succ(mag(stackF(fam, 1)) * dvec[:, None])) + succ(mag(stackF(fam, 2)) * succ(dvec[:, None] ** 2))) + remF[fam])
            rem = succ(succ(succ(remF[fam] @ supTM) + succ(facmag @ TM.r)) * (1 + 2 * (Nf + 4) * U))
            return out, rem
        SP, remP = sums("cos", P); SC, remC = sums("C", R); SS, remS = sums("S", R)
        def tensor_range(q0, q1, q2, rem):
            dM = MR(dvec[:, None], succ(U * dvec)[:, None])
            b0 = q0 - q1 * dM + q2 * dM * dM; b1 = q0 - q2 * dM * dM; b2 = q0 + q1 * dM + q2 * dM * dM
            lo_ = np.full(A, np.inf); hi_ = np.full(A, -np.inf)
            for bk in (b0, b1, b2):
                l_, h_ = self.poly_range_sub(bk, h_up, K); lo_ = np.minimum(lo_, l_); hi_ = np.maximum(hi_, h_)
            return pred(lo_ - rem), succ(hi_ + rem)
        def const(cval):
            z = MR(np.zeros((A, Q + 1)), np.zeros((A, Q + 1))); z.m[:, 0] = cval.m; z.r[:, 0] = succ(cval.r + U * abs(cval.m)); return z
        s_q = [const(cl) - SP[0], MR(-SP[1].m, SP[1].r), MR(-SP[2].m, SP[2].r)]
        s_lo, s_hi = tensor_range(*s_q, remP)
        v2_q = [s_q[k] + SC[k] for k in range(3)]; v2_lo, v2_hi = tensor_range(*v2_q, succ(remP + remC))
        v1_q = [s_q[k] - SS[k] for k in range(3)]; v1_lo, v1_hi = tensor_range(*v1_q, succ(remP + remS))
        T_q = [(SS[k] * MR.exact(-1.0)) * A_MR + SC[k] * B_MR + s_q[k] * muM for k in range(3)]
        one_cl = MR(1.0 + cl.m, succ(cl.r + 2 * U * (1 + abs(cl.m))))
        T_q[0] = T_q[0] - const(one_cl)
        remT = succ(succ(succ(float(A_MR.mag()) * remS) + succ(float(B_MR.mag()) * remC)) + succ(float(muM.mag()) * remP))
        T_lo, T_hi = tensor_range(*T_q, remT)
        return dict(s_lo=s_lo, s_hi=s_hi, v2y_lo=v2_lo, v2y_hi=v2_hi, v1x_lo=v1_lo, v1x_hi=v1_hi, T0_lo=T_lo, T0_hi=T_hi)


def mu_interval_mr(r_lo_arb, r_hi_arb):
    """MR enclosure of mu(r) over r in [r_lo, r_hi] (mu decreasing): Arb hull of mu(r_hi) and mu(r_lo)."""
    p = PAR["p"]; Rm = arb(PAR["Rm"])
    f = lambda r: GP_ARB + (S_ARB - GP_ARB) / (1 + (r / Rm) ** p)
    return MR.from_arb([f(r_hi_arb).union(f(r_lo_arb))])[0]


def box_class(r_lo, r_hi, f):
    """'in', 'out' or 'straddle' of the polar cell [r_lo, r_hi] x [a, b] against B_1 = [x1, x2] x [0, y2]; f = angular factor record
    (certified cos/sin bounds of the edges). Also returns outward x bounds (x_min_lo, x_max_hi)."""
    x1, x2, y2 = PAR["box"]
    x_min_lo = pred(r_lo * f["cos_b"][0]) if f["cos_b"][0] > 0 else pred(r_hi * f["cos_b"][0])
    x_max_hi = succ(r_hi * f["cos_a"][1])
    y_min_lo = pred(r_lo * f["sin_a"][0]); y_max_hi = succ(r_hi * f["sin_b"][1])
    if x_min_lo >= x1 and x_max_hi <= x2 and y_max_hi <= y2: cls = "in"
    elif x_max_hi < x1 or x_min_lo > x2 or y_min_lo > y2: cls = "out"
    else: cls = "straddle"
    return cls, float(x_min_lo), float(x_max_hi)


def cell_iter(C, region, path):
    """Yield (ci, h_up, e_ta (MR), a_terms, A0, B0, r_lo, r_hi, t_a, nc_total) for the region's sub-cells."""
    if region == "middle":
        for ci in range(C.nc):
            h = C.tb[ci + 1] - C.tb[ci]; h_up = h.mag()
            r_lo = float(pred(C.e_ta.m[ci] - C.e_ta.r[ci])); r_hi = float(succ((C.e_ta.m[ci] + C.e_ta.r[ci]) * succ(1 + h_up + h_up * h_up)))
            yield ci, h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], r_lo, r_hi, float(C.tb.m[ci]), C.nc
    else:
        from cert_resid_regions import recentre_terms
        d = np.load(path); tau = MR(d["tau"], d["tau_rad"]); A = MR(d["A_mid"], d["A_rad"]); B = MR(d["B_mid"], d["B_rad"])
        assert "alphas_rad" in d.files, "region file without exponent radii: regenerate with the current cert_green_outer.py"
        alphas = d["alphas"]; base_m = d["base_mid"]; base_r = d["base_rad"]; nc = len(d["tau"]) - 1
        base_t = float(d["t0"]) if region == "outer" else float(d["tmin"]); base_r_ = float(d["t0_rad"]) if region == "outer" else float(d["tmin_rad"])
        for ci in range(nc):
            h = tau[ci + 1] - tau[ci]; h_up = h.mag()
            tau_a = arb(float(d["tau"][ci]), float(d["tau_rad"][ci])); ta = arb(base_t, base_r_) + tau_a
            e = ta.exp(); e_ta = MR.from_arb([e])[0]
            a_terms = recentre_terms(alphas, base_m, base_r, tau_a, d["alphas_rad"])
            r_lo = float(pred(e_ta.m - e_ta.r)); r_hi = float(succ((e_ta.m + e_ta.r) * succ(1 + h_up + h_up * h_up)))
            yield ci, h_up, e_ta, a_terms, A[ci], B[ci], r_lo, r_hi, float(ta.mid()), nc


def run(green, trial, region, out, ntheta=200, c0=0, c1=None, region_path=None, maxdepth=7):
    C = FlowCertifier(green, trial, Q=12); ang = AngCache(C.n)
    half_pi = arb.pi() / 2
    base = [(half_pi * i / ntheta, half_pi * (i + 1) / ntheta) for i in range(ntheta)]      # exact cover of [0, pi/2] (arb balls)
    rows = []; t0 = time.time()
    glob = dict(s_min=np.inf, s_min_far=np.inf, v2y_min=np.inf, T0_max_out=-np.inf, T0_max_in=-np.inf, V1_max_in=-np.inf, n_unresolved=0,
                axis_sign_fail=0, v1x_axis_below_max=-np.inf, v1x_axis_above_min=np.inf)
    xs_lo, xs_hi = XSTAR[0] - XSTAR[1], XSTAR[0] + XSTAR[1]
    allcells = list(cell_iter(C, region, region_path)); nc_total = allcells[0][9]
    cells = [c for c in allcells if c[0] >= c0 and (c1 is None or c[0] < c1)]
    assert cells, "empty selection"
    for (ci, h_up, e_ta, a_terms, A0, B0, r_lo, r_hi, t_a, _) in cells:
        P, R, hpow = C.psi_tms(h_up, e_ta, a_terms, A0, B0)
        muM = mu_interval_mr(arb(r_lo), arb(r_hi))
        res = C.cell_bounds(P, R, hpow, h_up, base, ang, muM)
        T_in = -np.inf; T_out = -np.inf; V1_in = -np.inf; unresolved = 0; v2min = np.inf; smin = np.inf; axfail = 0
        ax_lo, ax_hi = float(res["v1x_lo"][0]), float(res["v1x_hi"][0])
        below = r_hi < xs_lo; above = r_lo > xs_hi
        work = [(base[a], res, a, 0) for a in range(ntheta)]
        while work:
            (a_, b_), rr, a, depth = work.pop()
            f = ang.factors(a_, b_)
            cls, xmin_lo, xmax_hi = box_class(r_lo, r_hi, f)
            Thi = rr["T0_hi"][a]; v1hi = rr["v1x_hi"][a]; v1lo = rr["v1x_lo"][a]; v2lo = rr["v2y_lo"][a]; slo = rr["s_lo"][a]
            V1hi = succ(v1hi * xmax_hi) if v1hi > 0 else succ(v1hi * xmin_lo)          # x q <= x_max q (q > 0) ; x q <= x_min q (q <= 0)
            ok_in = (cls != "out") and (Thi <= TARGETS["T_in"]) and (V1hi <= TARGETS["V1_in"])
            ok_out = (cls != "in") and (Thi <= TARGETS["T_out"])
            ok_y = v2lo >= TARGETS["m0"]
            ok_s = (slo >= TARGETS["kappa0"]) if r_hi >= TARGETS["R0"] else True
            on_axis = f["a_lo"] <= 0.0
            ok_ax = True
            if on_axis and below: ok_ax = v1hi < 0
            if on_axis and above: ok_ax = v1lo > 0
            need = (not ok_y) or (not ok_s) or (not ok_ax) or (cls == "in" and not ok_in) or (cls == "out" and not ok_out) or (cls == "straddle" and not (ok_in and ok_out))
            if need and depth < maxdepth:
                mid = (a_ + b_) / 2
                sub = C.cell_bounds(P, R, hpow, h_up, [(a_, mid), (mid, b_)], ang, muM)
                work.append(((a_, mid), sub, 0, depth + 1)); work.append(((mid, b_), sub, 1, depth + 1)); continue
            if need: unresolved += 1
            if not ok_ax: axfail += 1
            if on_axis:
                if below: glob["v1x_axis_below_max"] = max(glob["v1x_axis_below_max"], v1hi)
                if above: glob["v1x_axis_above_min"] = min(glob["v1x_axis_above_min"], v1lo)
            v2min = min(v2min, v2lo); smin = min(smin, slo)
            if cls in ("in", "straddle"): T_in = max(T_in, Thi); V1_in = max(V1_in, V1hi)
            if cls in ("out", "straddle"): T_out = max(T_out, Thi)
        row = dict(ci=ci, region=region, t_a=t_a, r_lo=r_lo, r_hi=r_hi, s_min=float(smin), v2y_min=float(v2min), v1x_axis_lo=ax_lo, v1x_axis_hi=ax_hi,
                   T0_max_in=float(T_in), T0_max_out=float(T_out), V1_max_in=float(V1_in), n_unresolved=unresolved, axis_sign_fail=axfail,
                   remP=float(P.r.max()), remR=float(R.r.max()))
        rows.append(row)
        glob["s_min"] = min(glob["s_min"], smin); glob["v2y_min"] = min(glob["v2y_min"], v2min)
        if r_hi >= TARGETS["R0"]: glob["s_min_far"] = min(glob["s_min_far"], smin)
        glob["T0_max_out"] = max(glob["T0_max_out"], T_out); glob["T0_max_in"] = max(glob["T0_max_in"], T_in); glob["V1_max_in"] = max(glob["V1_max_in"], V1_in)
        glob["n_unresolved"] += unresolved; glob["axis_sign_fail"] += axfail
        if (ci - c0) % 100 == 0:
            print("%s cell %d r=[%.4g, %.4g]: s_min %.4f V2/y min %.4f V1/x axis [%.4f, %.4f] T0 in/out %.3f/%.3f V1_in %.2f unres %d axfail %d (%.0fs)" % (
                region, ci, r_lo, r_hi, smin, v2min, ax_lo, ax_hi, T_in, T_out, V1_in, unresolved, axfail, time.time() - t0), flush=True)
        if (ci - c0) % 500 == 0 or ci == cells[-1][0]:
            complete = (c0 == 0 and (c1 is None or c1 >= nc_total) and ci == cells[-1][0])
            json.dump(dict(region=region, ntheta=ntheta, PAR=PAR, TARGETS=TARGETS, XSTAR=XSTAR, nc_total=nc_total, selection=[c0, c1], rows=rows, glob=glob,
                           done=(ci == cells[-1][0]), complete_region=complete, time=time.time() - t0, green=green, trial=trial, region_path=region_path), open(out, "w"))
    print("done %.0fs; %s (%d of %d cells; complete=%s): s_min %.5f (r_hi >= R0: %.5f), V2/y min %.5f, T0 max off-box %.4f, on-box %.4f, V1 max on-box %.3f, unresolved %d, axis-sign fails %d, axis V1/x: below max %.4f, above min %.4f" % (
        time.time() - t0, region, len(rows), nc_total, c0 == 0 and (c1 is None or c1 >= nc_total), glob["s_min"], glob["s_min_far"], glob["v2y_min"], glob["T0_max_out"], glob["T0_max_in"], glob["V1_max_in"], glob["n_unresolved"], glob["axis_sign_fail"], glob["v1x_axis_below_max"], glob["v1x_axis_above_min"]))


if __name__ == "__main__":
    a = sys.argv
    run(a[1], a[2], a[3], a[4], int(a[5]) if len(a) > 5 else 200, int(a[6]) if len(a) > 6 else 0, int(a[7]) if len(a) > 7 and a[7] != "-" else None, a[8] if len(a) > 8 else None)
