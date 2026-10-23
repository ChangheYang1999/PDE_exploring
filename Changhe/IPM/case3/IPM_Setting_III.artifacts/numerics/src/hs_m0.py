"""Axis core constant m_0 of the saved hydrostatic trial states (lead 11:16Z optional diagnostic; FINAL_REPORT 3.77 pending).  Diagnostic of TRIAL STATES only.
Exact axis primitive (verifier result 190, lead-checked): on the y-axis
    d_y V_2(0, y) = int_y^inf g_xixi(0, t) dt = K(t(y)),   K(t) = -H(t) - J(1) + J(t),   H(t) = w sum_k (-1)^k b_k(t)  (g(0, y) = y H),
    J(t) = int_{-1}^t J'(s) ds,   J'(t) = sum_{k>=1} k^2 (-1)^k Q_map(t) b_k(t)/sigma(t),   Q_map = w + 2 P sigma,   b_k = sigma^k beta_k (degree-N polynomials),
so V_2(0, y) = int_0^y K(t(s)) ds (s = radius along the axis, t(s) = rad.t_of_r(s)).  J' is a polynomial of degree N: it is sampled at N + 3 Chebyshev points
(mode values b_k interpolated barycentrically from the Radau nodes, exact for degree <= N) and integrated exactly as a Chebyshev series.
With the far-field trace Theta (hs_cp), p = 1/c, K = Theta(pi/2) (= 1), Q = p K + Theta''(pi/2):  g_xixi(0, y) ~ Q y^(p-2), so V_2(0, y) = Q y^p/(p(1-p)) + m_0 + o(1),
    m_0 := lim_{y -> inf} [V_2(0, y) - Q y^p/(p (1 - p))]   (exists for c > 2; at c = 2 the degree-0 far-field term gives a B log y growth instead).
The trial state's axis expansion has the exponents e_j = 1 - j (1 - p) (g(0, y) = sum_j c_j y^(e_j), from w = O(r^(p-1)) and b_k polynomial in w), so
F(y) := V_2(0, y) - Q y^p/(p(1-p)) = m_0 + sum_{j>=2} A_j y^(e_j) for c > 2; m_0 is read off by least squares in the basis {1, y^(e_2), y^(e_3), ...} on a log grid of y.
Axis residual: R_h(0, y) = v G' - G with v = c y + V_2(0, y), G = g(0, y), G' = g_y(0, y); N_f = |v G'| + |G| (g_xi = 0 on the axis).  With the expansion,
R_h = m_0 p K y^(p-1) + (terms y^(3p-2) and smaller at c = 3), N_f ~ 2 K y^p, so y R_h/N_f -> m_0 p/2 (= m_0/6 at c = 3; lead 11:16Z).  Both sides are printed.
Checks: V_2(0, y) from the primitive against hs.hydro_V (FD g_xixi, r-scaled step) at 7 radii; (1-p) y^(1-p) K(t(y)) -> Q; barycentric vs direct mode evaluation.
Usage: python3 src/hs_m0.py runs/hsE_c3.0_N96_hr.pt ...   [--ymax 1e12]"""
import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs, hs_cp
from ipm3 import interp_matrix
torch.set_default_dtype(torch.float64)
C = np.polynomial.chebyshev

class AxisPrimitive:
    def __init__(self, m, u):
        self.m = m; rad = m.rad; self.rad = rad; N = m.N; self.P = rad.p
        bkR, _ = m.b_modes(m.beta_full(u), 'R'); self.bkR = bkR.cpu().numpy()                      # (N+1, M) mode values b_k at the Radau nodes
        self.k = np.arange(m.M); self.sgn = (-1.0) ** self.k
        n = N + 3; tc = np.cos(np.pi * (2 * np.arange(n) + 1) / (2 * n))                           # Chebyshev points (first kind), exclude +-1
        Jp = self.Jprime(tc); self.cJp = C.chebfit(tc, Jp, N + 1); self.cJ = C.chebint(self.cJp, lbnd=-1.0); self.J1 = float(C.chebval(1.0, self.cJ))
        self.fit_err = float(np.abs(C.chebval(tc, self.cJp) - Jp).max() / (np.abs(Jp).max() + 1e-300))
    def modes(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=np.float64)); return interp_matrix(self.rad.tR_np, t, self.rad.wR_np) @ self.bkR                # (npts, M)
    def H(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=np.float64)); w = (1 - t) / 2; return w * (self.modes(t) * self.sgn[None, :]).sum(1)
    def Jprime(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=np.float64)); sig = (1 + t) / 2; w = (1 - t) / 2; Qm = w + 2 * self.P * sig
        bk = self.modes(t); return Qm * (bk[:, 1:] * (self.k[1:] ** 2 * self.sgn[1:])[None, :]).sum(1) / sig
    def K(self, t):
        return -self.H(t) - self.J1 + C.chebval(np.asarray(t, dtype=np.float64), self.cJ)
    def K_of_s(self, s):
        return self.K(self.rad.t_of_r(np.maximum(np.asarray(s, dtype=np.float64), 1e-300)))
    def V2_axis(self, ymax=1e12, per_decade=20, ngl=16, s0=1e-8):
        """cumulative V_2(0, y) = int_0^y K(t(s)) ds at the log-spaced panel edges y_j = s0 10^(j/per_decade); returns (y_edges, V2_edges, K at edges)."""
        xg, wg = np.polynomial.legendre.leggauss(ngl)
        edges = s0 * 10.0 ** (np.arange(0, int(round(per_decade * np.log10(ymax / s0))) + 1) / per_decade)
        a = np.log(edges[:-1]); b = np.log(edges[1:]); X = 0.5 * (b - a)[:, None] * xg[None, :] + 0.5 * (a + b)[:, None]; S = np.exp(X)
        Kv = self.K_of_s(S.reshape(-1)).reshape(S.shape); panel = (0.5 * (b - a))[:, None] * (wg[None, :] * S * Kv)      # ds = s dx
        V = np.concatenate([[self.K_of_s([0.0])[0] * s0], self.K_of_s([0.0])[0] * s0 + np.cumsum(panel.sum(1))])        # int_0^s0 K ds ~ K(0) s0
        return edges, V, self.K_of_s(edges)

def fit_m0(y, F, p, nterms, lo, hi):
    msk = (y >= lo) & (y <= hi); e = [1 - j * (1 - p) for j in range(2, 2 + nterms - 1)]
    A = np.stack([np.ones(msk.sum())] + [y[msk] ** ej for ej in e], 1)
    coef, *_ = np.linalg.lstsq(A, F[msk], rcond=None); res = np.abs(A @ coef - F[msk]).max()
    return coef, e, res

def analyse(f, ymax=1e12, verbose=True):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); p = 1.0 / c; tag = f.split('/')[-1][:-3]
    ap = AxisPrimitive(m, u); d = hs_cp.cp_of_state(m, u, c); K, Q = d['K'], d['Q']
    # exact second axis coefficient (referee m0ref): G = y H, H = w S(t), S = sum_k (-1)^k b_k; w = z/2 - (1-p) z^2/8 + ..., z = (L/r)^(1-p), S(t) = S(1) - 2 w S'(1) + ...
    # => c_1 = L^(1-p) S(1)/2 (= K), c_2 = L^(2(1-p)) [-(1-p) S(1)/8 - S'(1)/2] with b_k'(1) = k beta_k(1)/2 + beta_k'(1)
    S1 = sum(((-1) ** k) * float(m.beta_at(u, k, [1.0])[0][0]) for k in range(M)); S1p = sum(((-1) ** k) * (k * float(m.beta_at(u, k, [1.0])[0][0]) / 2 + float(m.beta_at(u, k, [1.0])[1][0])) for k in range(M))
    L = m.rad.L; c2_exact = L ** (2 * (1 - p)) * (-(1 - p) * S1 / 8 - S1p / 2); K_exact = L ** (1 - p) * S1 / 2
    out = dict(tag=tag, N=N, M=M, c=c, p=p, P=P, K=K, Q=Q, J1=ap.J1, c2_exact=c2_exact, K_exact=K_exact, cH=ap.K_of_s([0.0])[0], centre_defect=c + ap.K_of_s([0.0])[0] - 1, fit_err_Jp=ap.fit_err)
    # (1) check against hs.hydro_V
    ge = hs.GEval(m, m.beta_full(u)); ych = np.array([1e-2, 1e-1, 1.0, 10.0, 100.0, 1e3, 1e4]); zeros = np.zeros_like(ych)
    _, V2fd = hs.hydro_V(ge, zeros, ych, n_in=64, n_tail=200, hrel=1e-5, hstep='r')
    y_e, V2_e, K_e = ap.V2_axis(ymax=ymax)
    V2ex = np.array([ap.V2_axis(ymax=yy)[1][-1] for yy in ych]) if False else np.interp(np.log(ych), np.log(y_e), V2_e)        # edges include exact decades
    out['check_hydroV'] = [(float(yy), float(a), float(b), float(a - b)) for yy, a, b in zip(ych, V2ex, V2fd)]
    # hydro_V with a resolved inner quadrature (n_in 1024) at y = 1e3, 1e4: the default inner Gauss rule (64 points on [0, y]) cannot resolve the core t ~ 1 when y >> 1
    ybig = np.array([1e3, 1e4]); _, V2big = hs.hydro_V(ge, np.zeros(2), ybig, n_in=1024, n_tail=400, hrel=1e-5, hstep='r')
    out['check_hydroV_fine'] = [(float(yy), float(a), float(b), float(a - b)) for yy, a, b in zip(ybig, np.interp(np.log(ybig), np.log(y_e), V2_e), V2big)]
    # independent check of K(t(y)) = int_y^inf g_xixi(0, t) dt: composite Gauss in log t of the FD g_xixi (r-scaled step) from y to 1e14 plus the analytic tail Q t^(p-2)
    def K_direct(yy, ngl=24, per_decade=10):
        edges = np.exp(np.linspace(np.log(yy), np.log(1e14), int(per_decade * np.log10(1e14 / yy)) + 1)); xg, wg = np.polynomial.legendre.leggauss(ngl)
        a = np.log(edges[:-1]); b = np.log(edges[1:]); X = 0.5 * (b - a)[:, None] * xg[None, :] + 0.5 * (a + b)[:, None]; T = np.exp(X).reshape(-1)
        h = 1e-5 * (1 + T); _, gxp, _ = ge(h, T); _, gxm, _ = ge(-h, T); gxx = ((gxp - gxm) / (2 * h)).reshape(X.shape)
        return float(((0.5 * (b - a))[:, None] * wg[None, :] * np.exp(X) * gxx).sum() + Q * 1e14 ** (p - 1) / (1 - p))
    out['check_K_direct'] = [(float(yy), float(ap.K_of_s([yy])[0]), K_direct(yy)) for yy in [1e-2, 1.0, 1e2, 1e4, 1e6]]
    # direct (non-barycentric) mode evaluation of K at a few t as a second check
    tt = np.array([-0.9, -0.3, 0.3, 0.9]); sig = (1 + tt) / 2; w = (1 - tt) / 2
    Hd = w * sum(((-1) ** k) * sig ** k * m.beta_at(u, k, tt)[0] for k in range(M)); out['check_H_direct'] = float(np.abs(Hd - ap.H(tt)).max() / np.abs(Hd).max())
    # (1b) direct regularized core integral m_0 = int_0^inf [s g_xixi(0, s) - Q s^(p-1)] ds (referee m0ref: independent of the primitive and of V_2), FD g_xixi,
    #      composite log-Gauss on [1e-8, S] (the piece [0, 1e-8] is O(1e-8)); I(S) at S = 1e9 .. 1e12 extrapolated with the tail exponents {2p-1, 3p-2}
    if c > 2 + 1e-9:
        def I_direct(S, per_decade=20, ngl=16):
            edges = np.exp(np.linspace(np.log(1e-8), np.log(S), int(per_decade * np.log10(S / 1e-8)) + 1)); xg, wg = np.polynomial.legendre.leggauss(ngl)
            a = np.log(edges[:-1]); b = np.log(edges[1:]); X = 0.5 * (b - a)[:, None] * xg[None, :] + 0.5 * (a + b)[:, None]; T = np.exp(X).reshape(-1)
            h = 1e-5 * (1 + T); _, gxp, _ = ge(h, T); _, gxm, _ = ge(-h, T); gxx = ((gxp - gxm) / (2 * h)).reshape(X.shape); TT = T.reshape(X.shape)
            return float(((0.5 * (b - a))[:, None] * wg[None, :] * TT * (TT * gxx - Q * TT ** (p - 1))).sum()) - Q * 1e-8 ** p / p
        Ss = np.array([1e9, 1e10, 1e11, 1e12]); Is = np.array([I_direct(S) for S in Ss]); A = np.stack([np.ones(4), Ss ** (2 * p - 1), Ss ** (3 * p - 2)], 1)
        cf, *_ = np.linalg.lstsq(A, Is, rcond=None); out['m0_direct'] = float(cf[0]); out['m0_direct_I'] = [(float(S), float(I)) for S, I in zip(Ss, Is)]
    # (2) F(y) and the fit
    F = V2_e - Q * y_e ** p / (p * (1 - p)); out['F_samples'] = [(float(yy), float(F[np.argmin(np.abs(np.log(y_e / yy)))])) for yy in [1e2, 1e4, 1e6, 1e8, 1e10, ymax]]
    out['Qcheck'] = [(float(yy), float((1 - p) * yy ** (1 - p) * K_e[np.argmin(np.abs(np.log(y_e / yy)))] / Q)) for yy in [1e4, 1e6, 1e8, 1e10, ymax]]
    if c > 2 + 1e-9:
        fits = []
        for (lo, hi, nt) in [(1e2, ymax, 4), (1e2, ymax, 5), (1e3, ymax, 4), (1e4, ymax, 3), (1e4, ymax, 4), (1e1, ymax, 6)]:
            coef, e, res = fit_m0(y_e, F, p, nt, lo, hi); fits.append((lo, hi, nt, float(coef[0]), float(coef[1]), float(res)))
        out['fits'] = fits; out['m0'] = fits[0][3]
    else:   # c = 2: log growth expected: F = m + B_log log y + A_3 y^(-1/2) + A_4 y^(-1)
        msk = (y_e >= 1e2); A = np.stack([np.ones(msk.sum()), np.log(y_e[msk]), y_e[msk] ** (-0.5), y_e[msk] ** (-1.0), y_e[msk] ** (-1.5)], 1)
        coef, *_ = np.linalg.lstsq(A, F[msk], rcond=None); out['fit_c2'] = dict(m=float(coef[0]), B_log=float(coef[1]), res=float(np.abs(A @ coef - F[msk]).max()))
        out['m0'] = float('nan')
    # (3) axis residual vs prediction
    ya = 10.0 ** np.arange(1, 1 + int(np.log10(ymax)))[:12]; za = np.zeros_like(ya); g, gx, gy = ge(za, ya)
    V2a = np.interp(np.log(ya), np.log(y_e), V2_e); v = c * ya + V2a; R = v * gy - g; Nf = np.abs(v * gy) + np.abs(g)
    out['axis_rows'] = [(float(yy), float(r), float(n), float(yy * r / n)) for yy, r, n in zip(ya, R, Nf)]; out['pred_yR_Nf'] = float(out['m0'] * p / 2) if c > 2 + 1e-9 else float('nan')
    # (4) exponent decomposition of the axis far field and of the axis residual (c > 2): G(0, y) = sum_j c_j y^(e_j), e_j = 1 - j(1-p); R_h(0, y) = sum_j r_j y^(-j(1-p))
    #     (the residual's exponent set {e_j, j >= 2} u {e_i + e_j - 1} u {e_j - 1} is {-j(1-p), j >= 1} when 1 - p = 1/c ... in general it is {1 - j(1-p)} u {-j(1-p)}; both are used)
    if c > 2 + 1e-9:
        yg = y_e[(y_e >= 1e3)]; gG, _, gyG = ge(np.zeros_like(yg), yg); V2g = np.interp(np.log(yg), np.log(y_e), V2_e); Rg = (c * yg + V2g) * gyG - gG
        eG = [1 - j * (1 - p) for j in range(1, 6)]; AG = np.stack([yg ** e for e in eG], 1); cG, *_ = np.linalg.lstsq(AG, gG, rcond=None)
        out['G_coeffs'] = dict(exps=eG, coeffs=[float(x) for x in cG], res=float(np.abs(AG @ cG - gG).max()), c2_star=float(K * Q / ((1 - p) * (c - 1))))
        eR = sorted(set([round(1 - j * (1 - p), 12) for j in range(2, 8)] + [round(-j * (1 - p), 12) for j in range(1, 8)]), reverse=True)[:8]
        AR = np.stack([yg ** e for e in eR], 1); cR, *_ = np.linalg.lstsq(AR, Rg, rcond=None)
        out['R_coeffs'] = dict(exps=eR, coeffs=[float(x) for x in cR], res=float(np.abs(AR @ cR - Rg).max()))
        i1 = eR.index(round(2 * p - 1, 12)); i2 = eR.index(round(p - 1, 12))
        out['R_2p1'] = float(cR[i1]); out['R_2p1_pred'] = float((1 - c) * cG[1] + K * Q / (1 - p)); out['R_p1'] = float(cR[i2]); out['m0_from_R'] = float(cR[i2] / (p * K))
        out['R_2p1_pred_exact'] = float((1 - c) * c2_exact + K * Q / (1 - p))
        alt = []                                                                             # variation of window and order (referee m0ref): y >= 1e4 with 6 terms, y >= 1e3 with 6 terms, y >= 1e5 with 5 terms
        for ymin, nt in [(1e4, 6), (1e3, 6), (1e5, 5)]:
            msk = yg >= ymin; A2 = np.stack([yg[msk] ** e for e in eR[:nt]], 1); A2n = A2 / np.abs(A2).max(0); c2_, *_ = np.linalg.lstsq(A2n, Rg[msk], rcond=None); c2_ = c2_ / np.abs(A2).max(0)
            alt.append((ymin, nt, float(c2_[i1]), float(c2_[i2] / (p * K))))
        out['R_fit_alt'] = alt; out['m0_from_R_spread'] = float(max(a[3] for a in alt + [(0, 0, 0, out['m0_from_R'])]) - min(a[3] for a in alt + [(0, 0, 0, out['m0_from_R'])]))
    if verbose:
        print(f"\n=== {tag}  {N}x{M}  c = {c:.6f}  p = {p:.6f}  P_map = {P:.6f}  K = {K:+.8f}  Q = {Q:+.8f}  J(1) = {ap.J1:+.8e}  c_H = int_0^inf g_xixi(0,t) dt = {out['cH']:+.8e}  centre defect c + c_H - 1 = {out['centre_defect']:+.3e}  (Chebyshev fit of J': rel err {ap.fit_err:.1e}; H direct vs barycentric {out['check_H_direct']:.1e})")
        print("  check V_2(0, y): primitive vs hs.hydro_V (n_in 64, n_tail 200, r-scaled FD step):  " + "  ".join(f"y={yy:g}: {a:+.8e} / {b:+.8e} (d {dd:+.1e})" for yy, a, b, dd in out['check_hydroV']))
        print("  Q check (1-p) y^(1-p) K(t(y)) / Q at y = " + ", ".join(f"{yy:.0e}: {v:.6f}" for yy, v in out['Qcheck']) + "   (-> 1 at the rate y^(p-1))")
        print("  F(y) = V_2(0, y) - Q y^p/(p(1-p)) at y = " + ", ".join(f"{yy:.0e}: {v:+.8f}" for yy, v in out['F_samples']))
        if c > 2 + 1e-9:
            print("  fits F = m_0 + A_2 y^(e_2) + ... (e_j = 1 - j(1-p)):  " + "  |  ".join(f"[{lo:.0e},{hi:.0e}] {nt} terms: m_0 {m0:+.8f} A_2 {a2:+.5f} maxres {res:.1e}" for lo, hi, nt, m0, a2, res in out['fits']))
            print(f"  m_0 = {out['m0']:+.8f}  ->  predicted lim y R_h/N_f on the axis = m_0 p/2 = {out['pred_yR_Nf']:+.8f}  (|m_0|/6 = {abs(out['m0'])/6:.8f} at c = 3)")
        else:
            fc = out['fit_c2']; print(f"  c = 2: F = m + B_log log y + A_3 y^(-1/2) + A_4 y^(-1) + A_5 y^(-3/2) on y >= 1e2:  m {fc['m']:+.8f}  B_log {fc['B_log']:+.8f}  maxres {fc['res']:.1e}   (B_log = axis curvature coefficient of the degree-0 far-field term; no finite m_0 unless B_log = 0)")
        print("  check (resolved inner rule) V_2(0, y) primitive vs hs.hydro_V (n_in 1024, n_tail 400):  " + "  ".join(f"y={yy:g}: {a:+.8e} / {b:+.8e} (d {dd:+.1e})" for yy, a, b, dd in out['check_hydroV_fine']))
        print("  check K(t(y)) = int_y^inf g_xixi(0,t) dt, primitive vs direct log-Gauss of FD g_xixi (+ analytic tail beyond 1e14):  " + "  ".join(f"y={yy:g}: {a:+.8e} / {b:+.8e}" for yy, a, b in out['check_K_direct']))
        print("  axis residual (exact V_2):  y, R_h(0,y), N_f, y R_h/N_f:  " + "  ".join(f"[{yy:.0e}: {r:+.3e}, {n:.3e}, {q:+.6f}]" for yy, r, n, q in out['axis_rows']))
        if 'G_coeffs' in out:
            Gc = out['G_coeffs']; Rc = out['R_coeffs']
            print("  axis far field G(0, y) = sum_j c_j y^(e_j) fitted on y >= 1e3: " + ", ".join(f"y^({e:+.4f}): {cc:+.6f}" for e, cc in zip(Gc['exps'], Gc['coeffs'])) + f"  (maxres {Gc['res']:.1e}; c_1 should be K = {K:+.6f}; cancellation of the y^(2p-1) residual term needs c_2 = c_2* = K Q/((1-p)(c-1)) = {Gc['c2_star']:+.6f})")
            print("  axis residual R_h(0, y) = sum r_j y^(f_j) fitted on y >= 1e3: " + ", ".join(f"y^({e:+.4f}): {cc:+.6f}" for e, cc in zip(Rc['exps'], Rc['coeffs'])) + f"  (maxres {Rc['res']:.1e})")
            print(f"  -> y^(2p-1) coefficient {out['R_2p1']:+.6f} (predicted (1-c) c_2 + K Q/(1-p) = {out['R_2p1_pred']:+.6f}: the uncancelled second far-field term of the trial, which dominates y R_h/N_f ~ y^(p) at large y);"
                  f"  y^(p-1) coefficient {out['R_p1']:+.6f} = m_0 p K -> m_0 = {out['m0_from_R']:+.6f} (from the F(y) fit: {out['m0']:+.6f})")
            print(f"  exact c_2 = L^(2(1-p)) [-(1-p) S(1)/8 - S'(1)/2] = {c2_exact:+.6f} (fitted {Gc['coeffs'][1]:+.6f}; K exact {K_exact:+.8f}); r_2 prediction with exact c_2: {out['R_2p1_pred_exact']:+.6f}")
            print("  R-fit variation (ymin, terms, r_2, m_0): " + "; ".join(f"({ym:.0e}, {nt}, {r2:+.6f}, {m0:+.6f})" for ym, nt, r2, m0 in out['R_fit_alt']) + f"  -> spread of m_0 from R: {out['m0_from_R_spread']:.2e}")
            print(f"  DIRECT regularized core integral m_0 = int_0^inf [s g_xixi(0,s) - Q s^(p-1)] ds (FD g_xixi, independent of the primitive): I(S) at S = 1e9..1e12: " + ", ".join(f"{I:+.6f}" for _, I in out['m0_direct_I']) + f"  -> extrapolated m_0 = {out['m0_direct']:+.6f}  (F fit {out['m0']:+.6f}, R fit {out['m0_from_R']:+.6f})")
    return out

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; ymax = float(sys.argv[sys.argv.index('--ymax') + 1]) if '--ymax' in sys.argv else 1e12
    print("# axis core constant m_0 of hydrostatic TRIAL STATES (lead 11:16Z; diagnostic only, nothing about solutions); exact axis primitive (verifier 190); ymax = %g" % ymax)
    rows = []
    for f in args:
        o = analyse(f, ymax=ymax); rows.append(o)
    print("\n# summary: state, NxM, c, K, Q, c_H centre defect, m_0 (fit [1e2,ymax] 4 terms), spread over fits, predicted m_0 p/2, measured y R_h/N_f at y = 1e4 / 1e6 / 1e8")
    for o in rows:
        ar = {int(round(np.log10(yy))): q for yy, _, _, q in o['axis_rows']}
        spread = (max(ft[3] for ft in o['fits']) - min(ft[3] for ft in o['fits'])) if 'fits' in o else float('nan')
        print(f"{o['tag']:30s} {o['N']:3d}x{o['M']:<3d} {o['c']:.1f} K {o['K']:+.6f} Q {o['Q']:+.6f} defect {o['centre_defect']:+.2e}  m_0 {o['m0']:+.7f} (spread {spread:.1e}; from R {o.get('m0_from_R', float('nan')):+.5f}; direct {o.get('m0_direct', float('nan')):+.5f})  pred {o['pred_yR_Nf']:+.7f}  meas {ar.get(4, float('nan')):+.7f} / {ar.get(6, float('nan')):+.7f} / {ar.get(8, float('nan')):+.7f}")
