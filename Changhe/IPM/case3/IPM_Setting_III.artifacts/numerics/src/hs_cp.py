"""Far-field compatibility diagnostic C_p(Theta) of the saved hydrostatic trial states (lead 10:47Z item 2; FINAL_REPORT 3.74(d), 3.76).
Representation: g = y w sum_k sigma^k beta_k(t) cos 2k theta, r = L sqrt(sigma)/(2w)^P, P = c/(c-1), p = 1/c = 1 - 1/P.  Leading trace at infinity (exact
limit of the representation): Theta(theta) = lim r^(-p) g = D sin(theta) sum_k beta_k(1) cos(2k theta), D = L^(1/P)/2 (= DR.Dff), K = Theta(pi/2).
With f = r^p Theta, F(s) = f(1, s) = (1 + s^2)^(p/2) Theta(atan s), q(s) = f_xixi(1, s) = p(p-1) F - 2(p-1) s F' + s^2 F'' and Q = p K + Theta''(pi/2)
(f_xixi(0, y) = Q y^(p-2)):  C_p(Theta) = int_0^inf s (q(s) - Q s^(p-2)) ds  (form 1)  = (p+1)(p+2) FP int_0^inf s F(s) ds  (form 2; FP subtracts
K S^(p+2)/(p+2) + Q S^p/(2p) at the upper end).  Both forms are computed at upper limits S = 1e3, 1e4, 1e5 (convergence check); form 1 uses
int_0^S s q ds - Q S^p/p with s q smooth.  F', F'' analytic: F' = p r^(p-2) s Th + r^(p-2) Th', F'' = p(p-2) r^(p-4) s^2 Th + p r^(p-2) Th +
(2p-2) r^(p-4) s Th' + r^(p-4) Th'' (r^2 = 1 + s^2, Th = Theta(atan s)).  The trace is first checked against the evaluator (r^(-p) g at r = 1e4, 1e6).
Also (option --window): the sampled |R_h|/N_f in a thin window around the vertical axis (theta = pi/2 - delta, delta = 0.01, 0.03, 0.05) for r = 10 .. 1e4,
with the log-log slope over 100 <= r <= 1e4 (3.74(d): a cusp term of degree 2p - 1 not representable in the trigonometric trial space would leave a
normalised residual decaying no faster than about r^(p-1) |C_p| near the axis).  Diagnostic of the trial states only.
Usage: python3 src/hs_cp.py [--window] runs/hsA_c3.0_N64.pt ..."""
import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs
torch.set_default_dtype(torch.float64)

def theta_funcs(bk1, D):
    k = np.arange(len(bk1)); b = np.asarray(bk1)
    def Th(th):
        th = np.asarray(th, dtype=np.float64)[..., None]; return D * (np.sin(th) * b * np.cos(2 * k * th)).sum(-1)
    def Th1(th):
        th = np.asarray(th, dtype=np.float64)[..., None]; return D * (b * (np.cos(th) * np.cos(2 * k * th) - 2 * k * np.sin(th) * np.sin(2 * k * th))).sum(-1)
    def Th2(th):
        th = np.asarray(th, dtype=np.float64)[..., None]; return D * (b * (-(1 + 4 * k ** 2) * np.sin(th) * np.cos(2 * k * th) - 4 * k * np.cos(th) * np.sin(2 * k * th))).sum(-1)
    return Th, Th1, Th2

def cp_of_state(m, u, c):
    bk1 = [float(m.beta_at(u, k, [1.0])[0][0]) for k in range(m.M)]; D = m.Dff; p = 1.0 / c           # ALL M modes (DR.farfield returns k = 0..2 only)
    Th, Th1, Th2 = theta_funcs(bk1, D); K = Th(np.pi / 2); Q = p * K + Th2(np.pi / 2)
    def F_all(s):
        r2 = 1 + s ** 2; r = np.sqrt(r2); th = np.arctan(s); T0, T1, T2 = Th(th), Th1(th), Th2(th)
        F = r ** p * T0; F1 = p * r ** (p - 2) * s * T0 + r ** (p - 2) * T1
        F2 = p * (p - 2) * r ** (p - 4) * s ** 2 * T0 + p * r ** (p - 2) * T0 + (2 * p - 2) * r ** (p - 4) * s * T1 + r ** (p - 4) * T2
        return F, F1, F2
    # log-spaced composite Gauss-Legendre in x = log s
    xg, wg = np.polynomial.legendre.leggauss(24)
    def integ(fun, S, smin=1e-10, panels=400):
        edges = np.linspace(np.log(smin), np.log(S), panels + 1); tot = 0.0
        for a, b_ in zip(edges[:-1], edges[1:]):
            x = 0.5 * (b_ - a) * xg + 0.5 * (a + b_); s = np.exp(x); tot += 0.5 * (b_ - a) * (wg * s * fun(s)).sum()      # ds = s dx
        return tot
    # form 3 (14:25Z, after verifier 229): f_xixi of f = r^p Theta(theta) in POLAR form, f_xixi = r^(p-2) [p(p-1) cos^2 Theta + p sin^2 Theta + 2(1-p) sin cos Theta' +
    # sin^2 Theta''] (at theta = pi/2 this is Q r^(p-2)); the Cartesian form q = p(p-1) F - 2(p-1) s F' + s^2 F'' cancels three terms of size s^p K to leave
    # Q s^(p-2) and loses ~ s^2 x 1e-16 relative precision, which integrates to errors 1e-7 (S = 1e4) .. 3e-4 (S = 1e5) in forms 1 and 2 (the '3e-4 offset
    # from the verifier's 100-digit values' of (ix)); the polar bracket has no such cancellation.  Subtracted integrand s (q - Q s^(p-2)); the tail beyond S is
    # O(S^(p-2)) (Theta is a trigonometric polynomial, so q - Q s^(p-2) = O(s^(p-4)) near the axis): S = 1e6 gives the complete value to about 1e-10.
    def q_polar(s):
        r2 = 1 + s ** 2; r = np.sqrt(r2); th = np.arctan(s); T0, T1, T2 = Th(th), Th1(th), Th2(th); c_, s_ = np.cos(th), np.sin(th)
        return r ** (p - 2) * (p * (p - 1) * c_ ** 2 * T0 + p * s_ ** 2 * T0 + 2 * (1 - p) * s_ * c_ * T1 + s_ ** 2 * T2)
    out = {}
    for S in [1e3, 1e4, 1e5, 1e6]:
        q = lambda s: (lambda F, F1, F2: p * (p - 1) * F - 2 * (p - 1) * s * F1 + s ** 2 * F2)(*F_all(s))
        I1 = integ(lambda s: s * q(s), S) - Q * S ** p / p
        I2 = (p + 1) * (p + 2) * (integ(lambda s: s * F_all(s)[0], S) - K * S ** (p + 2) / (p + 2) - Q * S ** p / (2 * p))
        I3 = integ(lambda s: s * (q_polar(s) - Q * s ** (p - 2)), S, smin=1e-12) - Q * 1e-12 ** p / p
        out[S] = (I1, I2, I3)
    return dict(K=K, Q=Q, p=p, D=D, forms=out, Th=Th, q_polar=q_polar)

def trace_check(m, u, c, Th):
    ge = hs.GEval(m, m.beta_full(u)); p = 1.0 / c; res = []
    for r in [1e4, 1e6]:
        th = np.array([0.2, 0.6, 1.0, 1.4, np.pi / 2 - 1e-3]); X = r * np.cos(th); Y = r * np.sin(th); g, _, _ = ge(X, Y)
        res.append((r, np.abs(r ** (-p) * g / Th(th) - 1).max()))
    return res

def window(m, u, c, hrel=1e-5):
    ge = hs.GEval(m, m.beta_full(u)); p = 1.0 / c; rs = np.logspace(1, 4, 13); rows = []
    for dlt in [0.01, 0.03, 0.05]:
        th = np.pi / 2 - dlt; X = rs * np.cos(th); Y = rs * np.sin(th); V1, V2 = hs.hydro_V(ge, X, Y, n_in=32, n_tail=100, hrel=hrel, hstep='r'); g, gx, gy = ge(X, Y)
        R = (c * X + V1) * gx + (c * Y + V2) * gy - g; Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g); qv = np.abs(R) / Nf
        msk = rs >= 100; slope, logA = np.polyfit(np.log(rs[msk]), np.log(qv[msk]), 1)
        rows.append((dlt, qv, slope, np.exp(logA)))
    return rs, rows

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; do_window = '--window' in sys.argv
    print("# C_p(Theta) of the saved hydrostatic trial states (lead 10:47Z item 2); trace check = max over 5 angles of |r^(-p) g / Theta - 1| at r = 1e4, 1e6 (expected O(r^(-1/P)) from the next far-field term)")
    print("# state                        NxM     c    p      K           Q           C_p form1 (S=1e3 / 1e4 / 1e5)                 C_p form2 (S=1e3 / 1e4 / 1e5)                 C_p/K (form1, S=1e5)   trace check r=1e4 / 1e6   || form 3 (polar, cancellation-free) C_p (S=1e3 / 1e4 / 1e5 / 1e6)   C_p/K complete (form 3, S=1e6)")
    for f in args:
        st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
        hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
        d = cp_of_state(m, u, c); tc = trace_check(m, u, c, d['Th']); f1 = [d['forms'][S][0] for S in (1e3, 1e4, 1e5)]; f2 = [d['forms'][S][1] for S in (1e3, 1e4, 1e5)]
        tag = f.split('/')[-1][:-3]
        f3 = [d['forms'][S][2] for S in (1e3, 1e4, 1e5, 1e6)]
        print(f"{tag:30s} {N:3d}x{M:<3d} {c:.1f}  {d['p']:.4f} {d['K']:+.6f} {d['Q']:+.6f}  " + " / ".join(f"{x:+.6e}" for x in f1) + "   " + " / ".join(f"{x:+.6e}" for x in f2) + f"   {f1[-1]/d['K']:+.6f}        {tc[0][1]:.2e} / {tc[1][1]:.2e}   || " + " / ".join(f"{x:+.9e}" for x in f3) + f"   {f3[-1]/d['K']:+.9e}")
        if do_window:
            rs, rows = window(m, u, c)
            print(f"#   window (theta = pi/2 - delta), |R_h|/N_f at r = " + " ".join(f"{r:.0e}" for r in rs) + f";  p - 1 = {d['p'] - 1:+.4f}")
            for dlt, qv, slope, A in rows:
                print(f"#   delta {dlt:.2f}: " + " ".join(f"{v:.1e}" for v in qv) + f"   log-log slope over 100 <= r <= 1e4: {slope:+.3f}, prefactor {A:.3e} (|R_h|/N_f ~ A r^slope)")
