"""Rigorous 2D bounds for the trial velocity field (lead request N1', notes/global_flow.md section 10), by Taylor models in t = log r
on the certificate's radial sub-cells and interval ranges of the angular factors on angular cells.

Quantities (polar; psi_n = stream modes (sin 2n theta), psi_r,n their r-derivatives):
  s     = X.V/r^2 = c_l - r^-2 sum_n 2n psi_n cos(2n theta)
  V_2/y = s + r^-1 sum_n psi_r,n C_n(theta),   C_n = 2 cos^2 theta U_{n-1}(cos 2theta) = cos theta sin(2n theta)/sin theta
  V_1/x = s - r^-1 sum_n psi_r,n S_n(theta),   S_n = 2 sin^2 theta U_{n-1}(cos 2theta) = sin theta sin(2n theta)/cos theta
  T_0   = -(1 + c_l) + a (V_1/x - s) + b (V_2/y - s) + mu(r) s,   mu(r) = gamma' + (a + b - gamma')/(1 + (r/R_m)^p)
(derivation: U = grad^perp psi, U_r = -psi_theta/r, U_theta = psi_r; sin(2n th)/sin th = 2 sum_{j<n} cos((2j+1) th),
 sin(2n th)/cos th = 2 sum_{j<n} (-1)^{n-1-j} sin((2j+1) th); Lipschitz constants 2n, 2n^2 + 2n, 2n^2 + 2n.)
Per radial sub-cell: TMs of P_n = 2n psi_n / r^2 and R_n = psi_r,n / r in sigma = t - t_a (Certifier machinery, cert_resid.py);
per angular cell [th_a, th_b]: factor enclosures [f(th_c) +/- Lip * (th_b - th_a)/2]; the mode sums give polynomials in sigma with
mid-rad coefficients (matmul over modes), Bernstein coefficients on [0, h] give two-sided ranges. Box classification of the
polar cell against B_1 = [x1, x2] x [0, y2] with angular bisection of straddling cells.
Usage: python3 cert_flow.py green.npz trial.npz region(middle|outer|inner) out.json [ntheta] [ci_start ci_end]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb
from midrad import MR, mr_matmul, succ, U, ETA
from cert_resid import Certifier, TMArr, tm_exp, mag
from flint import arb, ctx

PAR = dict(a=129 / 20, b=307 / 100, gp=1129 / 1000, Rm=6.0, p=4, box=(4.80, 6.82, 2.85), kappa=0.2)


def bern_range(coef, hpow_mr, Bern):
    """coef: MR (A, Q+1) polynomial coefficients in sigma on [0, h]; hpow_mr: MR (Q+1,) enclosures of h^i; returns (lo, hi) arrays (A,)."""
    ah = coef * MR(hpow_mr.m[None, :], hpow_mr.r[None, :])
    b = mr_matmul(ah, MR(Bern.m.T, Bern.r.T))
    lo = (b.m - b.r).min(-1); hi = (b.m + b.r).max(-1)
    return np.nextafter(lo, -np.inf), np.nextafter(hi, np.inf)


class FlowCertifier(Certifier):
    def psi_tms(self, h_up, e_ta, a_terms, A0, B0):
        """TMs (over modes n) of P_n = 2n psi_n e^{-2t} and R_n = psi_r,n e^{-t} on the sub-cell; returns (P, R, hpow)."""
        Q = self.Q; n = self.n
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

    @staticmethod
    def angular_factors2(th_a, th_b, n):
        """Second-order Taylor data at the cell centre th_c for the three factor families f in {cos(2n th), C_n, S_n}:
        returns dict f -> (F0, F1, F2, rem) with F_k = f^{(k)}(th_c)/k! as MR arrays (Nf,) and rem >= max |f^{(3)}| d^3/6, d = half width.
        D_n(th) = sin(2n th)/sin th = 2 sum_{j<n} cos((2j+1) th), E_n(th) = sin(2n th)/cos th = 2 sum_{j<n} (-1)^{n-1-j} sin((2j+1) th);
        C_n = cos th D_n, S_n = sin th E_n; |D_n^{(k)}|, |E_n^{(k)}| <= 2 sum_{j<n} (2j+1)^k <= 2n, 2n^2, (8/3) n^3, 4 n^4 (k = 0..3)."""
        th_c = 0.5 * (th_a + th_b); d = 0.5 * (th_b - th_a) * (1 + 4 * U) + ETA
        nn = n.astype(float); jj = np.arange(int(n.max())); w = 2 * jj + 1.0
        cj, sj = np.cos(w * th_c), np.sin(w * th_c)
        def cums(v): return np.concatenate([[0.0], np.cumsum(v)])
        D0 = 2 * cums(cj)[n]; D1 = -2 * cums(w * sj)[n]; D2 = -2 * cums(w ** 2 * cj)[n]
        sgn = (-1.0) ** jj
        alt0 = cums(sgn * sj); alt1 = cums(sgn * w * cj); alt2 = cums(sgn * w ** 2 * sj)
        pre = 2.0 * (-1.0) ** (nn - 1)
        E0 = pre * alt0[n]; E1 = pre * alt1[n]; E2 = -pre * alt2[n]
        c, s_ = np.cos(th_c), np.sin(th_c)
        C0 = c * D0; C1 = -s_ * D0 + c * D1; C2 = 0.5 * (-c * D0 - 2 * s_ * D1 + c * D2)
        S0 = s_ * E0; S1 = c * E0 + s_ * E1; S2 = 0.5 * (-s_ * E0 + 2 * c * E1 + s_ * E2)
        K0 = np.cos(2 * nn * th_c); K1 = -2 * nn * np.sin(2 * nn * th_c); K2 = -0.5 * (2 * nn) ** 2 * np.cos(2 * nn * th_c)
        def fl(scale): return succ(scale * (8 * nn + 8) * U * (1 + np.abs(nn * th_c)) + 4 * ETA)
        rem_cos = succ((2 * nn) ** 3 * d ** 3 / 6 * (1 + 8 * U))
        rem_CS = succ((2 * nn + 6 * nn ** 2 + 8 * nn ** 3 + 4 * nn ** 4) * d ** 3 / 6 * (1 + 8 * U))
        mk = lambda v, sc: MR(v, fl(sc))
        return dict(cos=(mk(K0, 1.0), mk(K1, 2 * nn), mk(K2, 2 * nn ** 2), rem_cos),
                    C=(mk(C0, 2 * nn), mk(C1, 2 * nn ** 2 + 2 * nn), mk(C2, 2 * nn ** 3 + 2 * nn ** 2 + nn), rem_CS),
                    S=(mk(S0, 2 * nn), mk(S1, 2 * nn ** 2 + 2 * nn), mk(S2, 2 * nn ** 3 + 2 * nn ** 2 + nn), rem_CS), d=d)

    def poly_range_sub(self, coef, h_up, K):
        """Two-sided range over [0, h] of MR polynomials (A, Q+1) by Bernstein on K equal sub-intervals (re-centred); returns lo, hi (A,)."""
        from math import comb as _comb
        Q = self.Q; A = coef.m.shape[0]; hk = succ(h_up / K); hkP = self.mr_powers(hk, Q)
        lo = np.full(A, np.inf); hi = np.full(A, -np.inf)
        for kk in range(K):
            a = kk * hk; apow = [MR.exact(1.0)]
            for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
            cm = np.zeros_like(coef.m); cr = np.zeros_like(coef.r)
            for j in range(Q + 1):
                acc = MR(np.zeros(A), np.zeros(A))
                for i in range(j, Q + 1): acc = acc + coef[..., i] * MR.exact(float(_comb(i, j))) * apow[i - j]
                cm[:, j] = acc.m; cr[:, j] = acc.r
            l_, h_ = bern_range(MR(cm, cr), hkP, self.Bern)
            lo = np.minimum(lo, l_); hi = np.maximum(hi, h_)
        return lo, hi

    def cell_bounds(self, P, R, hpow, h_up, th_edges, e_ta, mu_lohi, K=2):
        """Two-sided ranges over the 2D cells [0,h] x [th_a, th_b] of s, V2/y, V1/x, T0 (dict of arrays (A,)), by second-order angular
        Taylor models (3 sigma-polynomials per quantity, tensor Bernstein over eta in [-d, d] and sigma in K sub-intervals)."""
        Q = self.Q; n = self.n; A = len(th_edges) - 1; Nf = self.Nf
        fac = [self.angular_factors2(th_edges[a], th_edges[a + 1], n) for a in range(A)]
        def stackF(fam, k):
            return MR(np.stack([f[fam][k].m for f in fac]), np.stack([f[fam][k].r for f in fac]))
        dvec = np.array([f["d"] for f in fac])
        remcos = np.stack([f["cos"][3] for f in fac]); remCS = np.stack([f["C"][3] for f in fac])
        cl = self.c_l; a_, b_ = PAR["a"], PAR["b"]
        mu_m = 0.5 * (mu_lohi[0] + mu_lohi[1]); mu_r = succ(0.5 * (mu_lohi[1] - mu_lohi[0]) * (1 + 4 * U) + ETA); muM = MR(mu_m, mu_r)
        def sums(fam, TM):
            out = [mr_matmul(stackF(fam, k), TM.c) for k in range(3)]
            supTM = TM.sup(hpow)
            remF = remcos if fam == "cos" else remCS
            facmag = succ(mag(stackF(fam, 0)) + mag(stackF(fam, 1)) * dvec[:, None] + mag(stackF(fam, 2)) * dvec[:, None] ** 2 + remF)
            rem = succ((remF @ supTM + facmag @ TM.r) * (1 + (Nf + 4) * U))
            return out, rem
        SP, remP = sums("cos", P); SC, remC = sums("C", R); SS, remS = sums("S", R)
        def tensor_range(q0, q1, q2, rem):
            dM = MR(dvec, succ(U * dvec))
            dM = MR(dM.m[:, None], dM.r[:, None])
            b0 = q0 - q1 * dM + q2 * dM * dM; b1 = q0 - q2 * dM * dM; b2 = q0 + q1 * dM + q2 * dM * dM
            lo = np.full(A, np.inf); hi = np.full(A, -np.inf)
            for bk in (b0, b1, b2):
                l_, h_ = self.poly_range_sub(bk, h_up, K); lo = np.minimum(lo, l_); hi = np.maximum(hi, h_)
            return np.nextafter(lo - rem, -np.inf), succ(hi + rem)
        def const(cval):
            z = MR(np.zeros((A, Q + 1)), np.zeros((A, Q + 1))); z.m[:, 0] = cval.m; z.r[:, 0] = succ(cval.r + U * abs(cval.m)); return z
        s_q = [const(cl) - SP[0], MR(-SP[1].m, SP[1].r), MR(-SP[2].m, SP[2].r)]
        s_lo, s_hi = tensor_range(*s_q, remP)
        v2_q = [s_q[k] + SC[k] for k in range(3)]; v2_lo, v2_hi = tensor_range(*v2_q, succ(remP + remC))
        v1_q = [s_q[k] - SS[k] for k in range(3)]; v1_lo, v1_hi = tensor_range(*v1_q, succ(remP + remS))
        aM = MR.exact(a_); bM = MR.exact(b_)
        T_q = [(SS[k] * MR.exact(-1.0)) * aM + SC[k] * bM + s_q[k] * muM for k in range(3)]
        T_q[0] = T_q[0] - const(MR(1.0 + cl.m, succ(cl.r + 2 * U * (1 + abs(cl.m)))))
        T_lo, T_hi = tensor_range(*T_q, succ(a_ * remS + b_ * remC + mag(muM) * remP))
        return dict(s_lo=s_lo, s_hi=s_hi, v2y_lo=v2_lo, v2y_hi=v2_hi, v1x_lo=v1_lo, v1x_hi=v1_hi, T0_lo=T_lo, T0_hi=T_hi)


def mu_interval(r_lo, r_hi):
    a, b, gp, Rm, p = PAR["a"], PAR["b"], PAR["gp"], PAR["Rm"], PAR["p"]
    f = lambda r: gp + (a + b - gp) / (1 + (r / Rm) ** p)
    return (np.nextafter(f(r_hi) * (1 - 8 * U), -np.inf), np.nextafter(f(r_lo) * (1 + 8 * U), np.inf))     # decreasing in r


def box_class(r_lo, r_hi, th_a, th_b):
    """'in', 'out' or 'straddle' for the polar cell against B_1 = [x1, x2] x [0, y2] (x = r cos th, y = r sin th, th in [0, pi/2])."""
    x1, x2, y2 = PAR["box"]
    x_lo = r_lo * np.cos(th_b) * (1 - 4 * U); x_hi = r_hi * np.cos(th_a) * (1 + 4 * U)
    y_lo = r_lo * np.sin(th_a) * (1 - 4 * U); y_hi = r_hi * np.sin(th_b) * (1 + 4 * U)
    if x_lo >= x1 and x_hi <= x2 and y_hi <= y2: return "in"
    if x_hi < x1 or x_lo > x2 or y_lo > y2: return "out"
    return "straddle"


TARGETS = dict(m0=0.9, T_out=-0.22, T_in=1.30, V1_in=-13.0, kappa0=3.0, R0=20.0)


def cell_iter(C, region, path):
    """Yield (ci, h_up, e_ta (MR), a_terms, A0, B0, r_lo, r_hi, t_a) for the region's sub-cells."""
    if region == "middle":
        for ci in range(C.nc):
            h = C.tb[ci + 1] - C.tb[ci]; h_up = h.mag()
            r_lo = float(np.nextafter(C.e_ta.m[ci] - C.e_ta.r[ci], -np.inf)); r_hi = float(succ((C.e_ta.m[ci] + C.e_ta.r[ci]) * succ(1 + h_up + h_up * h_up)))
            yield ci, h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], r_lo, r_hi, float(C.tb.m[ci])
    else:
        from cert_resid_regions import recentre_terms
        d = np.load(path); tau = MR(d["tau"], d["tau_rad"]); A = MR(d["A_mid"], d["A_rad"]); B = MR(d["B_mid"], d["B_rad"])
        alphas = d["alphas"]; base_m = d["base_mid"]; base_r = d["base_rad"]; nc = len(d["tau"]) - 1
        base_t = float(d["t0"]) if region == "outer" else float(d["tmin"]); base_r_ = float(d["t0_rad"]) if region == "outer" else float(d["tmin_rad"])
        for ci in range(nc):
            h = tau[ci + 1] - tau[ci]; h_up = h.mag()
            tau_a = arb(float(d["tau"][ci]), float(d["tau_rad"][ci])); ta = arb(base_t, base_r_) + tau_a
            e = ta.exp(); e_ta = MR.from_arb([e])[0]
            a_terms = recentre_terms(alphas, base_m, base_r, tau_a, d["alphas_rad"] if "alphas_rad" in d.files else None)
            r_lo = float(np.nextafter(e_ta.m - e_ta.r, -np.inf)); r_hi = float(succ((e_ta.m + e_ta.r) * succ(1 + h_up + h_up * h_up)))
            yield ci, h_up, e_ta, a_terms, A[ci], B[ci], r_lo, r_hi, float(ta.mid())


def run(green, trial, region, out, ntheta=200, c0=0, c1=None, region_path=None, maxdepth=7):
    C = FlowCertifier(green, trial, Q=12)
    ctx.prec = 128
    th_base = np.linspace(0.0, np.pi / 2, ntheta + 1)
    rows = []; t0 = time.time()
    glob = dict(s_min=np.inf, s_min_far=np.inf, v2y_min=np.inf, T0_max_out=-np.inf, T0_max_in=-np.inf, V1_max_in=-np.inf, n_unresolved=0, v1x_axis_sign_fail=[])
    x1, x2, y2 = PAR["box"]
    cells = list(cell_iter(C, region, region_path))
    if c1 is not None: cells = [c for c in cells if c0 <= c[0] < c1]
    else: cells = [c for c in cells if c[0] >= c0]
    for (ci, h_up, e_ta, a_terms, A0, B0, r_lo, r_hi, t_a) in cells:
        P, R, hpow = C.psi_tms(h_up, e_ta, a_terms, A0, B0)
        mu_lohi = mu_interval(r_lo, r_hi)
        res = C.cell_bounds(P, R, hpow, h_up, th_base, e_ta, mu_lohi)
        # per angular cell: classify; refine where a target fails (or straddling) up to maxdepth
        T_in = -np.inf; T_out = -np.inf; V1_in = -np.inf; unresolved = 0; v2min = np.inf; smin = np.inf
        work = [(th_base[a], th_base[a + 1], res, a, 0) for a in range(ntheta)]
        while work:
            th_a, th_b, rr, a, depth = work.pop()
            cls = box_class(r_lo, r_hi, th_a, th_b)
            Thi = rr["T0_hi"][a]; v1hi = rr["v1x_hi"][a]; v2lo = rr["v2y_lo"][a]; slo = rr["s_lo"][a]
            V1hi = succ(v1hi * (r_hi * np.cos(th_a) if v1hi > 0 else r_lo * np.cos(th_b)) * (1 + 4 * U))
            ok_in = (cls != "out") and (Thi <= TARGETS["T_in"]) and (V1hi <= TARGETS["V1_in"])
            ok_out = (cls != "in") and (Thi <= TARGETS["T_out"])
            ok_y = v2lo >= TARGETS["m0"]
            need = (not ok_y) or (cls == "in" and not ok_in) or (cls == "out" and not ok_out) or (cls == "straddle" and not (ok_in and ok_out))
            if need and depth < maxdepth:
                mid = 0.5 * (th_a + th_b)
                sub = C.cell_bounds(P, R, hpow, h_up, np.array([th_a, mid, th_b]), e_ta, mu_lohi)
                work.append((th_a, mid, sub, 0, depth + 1)); work.append((mid, th_b, sub, 1, depth + 1)); continue
            if need: unresolved += 1
            v2min = min(v2min, v2lo); smin = min(smin, slo)
            if cls in ("in", "straddle"): T_in = max(T_in, Thi); V1_in = max(V1_in, V1hi)
            if cls in ("out", "straddle"): T_out = max(T_out, Thi)
        # axis sign of V_1 (theta cell [0, dth]): V1/x range on the first angular cell contains the axis value
        ax_lo, ax_hi = float(res["v1x_lo"][0]), float(res["v1x_hi"][0])
        row = dict(ci=ci, region=region, t_a=t_a, r_lo=r_lo, r_hi=r_hi, s_min=float(smin), v2y_min=float(v2min), v1x_axis_lo=ax_lo, v1x_axis_hi=ax_hi,
                   T0_max_in=float(T_in), T0_max_out=float(T_out), V1_max_in=float(V1_in), n_unresolved=unresolved, remP=float(P.r.max()), remR=float(R.r.max()))
        rows.append(row)
        glob["s_min"] = min(glob["s_min"], smin); glob["v2y_min"] = min(glob["v2y_min"], v2min)
        if r_lo >= TARGETS["R0"]: glob["s_min_far"] = min(glob["s_min_far"], smin)
        glob["T0_max_out"] = max(glob["T0_max_out"], T_out); glob["T0_max_in"] = max(glob["T0_max_in"], T_in); glob["V1_max_in"] = max(glob["V1_max_in"], V1_in)
        glob["n_unresolved"] += unresolved
        if (ci - c0) % 100 == 0:
            print("%s cell %d r=[%.4g, %.4g]: s_min %.4f V2/y min %.4f V1/x axis [%.4f, %.4f] T0 in/out %.3f/%.3f V1_in %.2f unres %d (%.0fs)" % (
                region, ci, r_lo, r_hi, smin, v2min, ax_lo, ax_hi, T_in, T_out, V1_in, unresolved, time.time() - t0), flush=True)
        if (ci - c0) % 500 == 0 or ci == cells[-1][0]:
            json.dump(dict(region=region, ntheta=ntheta, PAR=PAR, TARGETS=TARGETS, rows=rows, glob=glob, done=(ci == cells[-1][0]), time=time.time() - t0), open(out, "w"))
    print("done %.0fs; %s: s_min %.5f (r >= R0: %.5f), V2/y min %.5f, T0 max off-box %.4f, T0 max on-box %.4f, V1 max on-box %.3f, unresolved cells %d" % (
        time.time() - t0, region, glob["s_min"], glob["s_min_far"], glob["v2y_min"], glob["T0_max_out"], glob["T0_max_in"], glob["V1_max_in"], glob["n_unresolved"]))


if __name__ == "__main__":
    a = sys.argv
    run(a[1], a[2], a[3], a[4], int(a[5]) if len(a) > 5 else 200, int(a[6]) if len(a) > 6 else 0, int(a[7]) if len(a) > 7 and a[7] != "-" else None, a[8] if len(a) > 8 else None)
