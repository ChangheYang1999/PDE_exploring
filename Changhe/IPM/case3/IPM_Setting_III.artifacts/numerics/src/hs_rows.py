"""hs_rows.py -- the far-field compatibility quantities C_p(Theta) (4P(b)(ix)) and the axis core constant m_0 (4P(b)(x)) as LINEAR FUNCTIONALS of the Q-basis
coefficient vector u (row vectors in coefficient space), for use as extra least-squares rows C_p = 0, m_0 = 0 in hs_solve (lead 11:16Z optional item).
C_p: Theta = D sin(theta) sum_k beta_k(1) cos 2k theta is linear in beta_k(1) = sum_j u_kj (T_j(1) = 1 in the local basis), so C_p = sum_k beta_k(1) C_p[e_k]
with C_p[e_k] the form-1 value (hs_cp, S = 1e4) of the single-mode trace.  m_0: with the exact axis primitive K_u(t) (hs_m0.AxisPrimitive, linear in the mode
values) m_0(u) = int_0^1 K_u ds + int_1^S [K_u - Q(u) s^(p-1)/(1-p)] ds - Q(u)/(p(1-p)), truncated at S = 1e12 (truncation error O(A_2 S^(2p-1)) = O(1e-4 A_2)),
Q(u) = p K(u) + Theta_u''(pi/2) linear in beta_k(1).  Rows are built on the identity basis in batches of mode-value columns.  Test: python3 src/hs_rows.py <pt>."""
import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs_cp, hs_m0
from ipm3 import interp_matrix
torch.set_default_dtype(torch.float64)
C = np.polynomial.chebyshev

def mode_value_rows(m):
    """matrix B (N+1, M, nu): mode values b_k(t_i) of the unit coefficient vectors (b_k = sigma^k beta_k)."""
    I = torch.eye(m.nu, device=m.dev); beta = m.beta_full(I)                                            # (nu, N+1, M)
    bkR = (m.rad.sigR[None, :, None] ** m.kk[None, None, :]) * beta                                       # (nu, N+1, M)
    return bkR.permute(1, 2, 0).contiguous()                                                              # (N+1, M, nu)

def beta1_rows(m):
    """matrix (M, nu): beta_k(1) of the unit vectors (= sum over the coefficients of mode k)."""
    R = torch.zeros(m.M, m.nu, device=m.dev)
    for k in range(m.M): R[k, m.offs[k]:m.offs[k + 1]] = 1.0
    return R

def cp_row(m, c, S=1e4):
    """row vector (nu,) with row . u = C_p(Theta_u) (form 1 at upper limit S), and the K row and Q row (nu,) for reference."""
    p = 1.0 / c; D = m.Dff; M = m.M; vals = []; Ks = []; Qs = []
    xg, wg = np.polynomial.legendre.leggauss(24)
    def integ(fun, S, smin=1e-10, panels=400):
        edges = np.linspace(np.log(smin), np.log(S), panels + 1); tot = 0.0
        for a, b_ in zip(edges[:-1], edges[1:]):
            x = 0.5 * (b_ - a) * xg + 0.5 * (a + b_); s = np.exp(x); tot += 0.5 * (b_ - a) * (wg * s * fun(s)).sum()
        return tot
    for k in range(M):
        e = np.zeros(M); e[k] = 1.0; Th, Th1, Th2 = hs_cp.theta_funcs(e, D); K = Th(np.pi / 2); Q = p * K + Th2(np.pi / 2)
        def F_all(s):
            r2 = 1 + s ** 2; r = np.sqrt(r2); th = np.arctan(s); T0, T1, T2 = Th(th), Th1(th), Th2(th)
            F1 = p * r ** (p - 2) * s * T0 + r ** (p - 2) * T1; F2 = p * (p - 2) * r ** (p - 4) * s ** 2 * T0 + p * r ** (p - 2) * T0 + (2 * p - 2) * r ** (p - 4) * s * T1 + r ** (p - 4) * T2
            return r ** p * T0, F1, F2
        def q_polar(s):                                                                            # polar form of f_xixi (cancellation-free; hs_cp form 3, 14:25Z)
            r2 = 1 + s ** 2; r = np.sqrt(r2); th = np.arctan(s); T0, T1, T2 = Th(th), Th1(th), Th2(th); c_, s_ = np.cos(th), np.sin(th)
            return r ** (p - 2) * (p * (p - 1) * c_ ** 2 * T0 + p * s_ ** 2 * T0 + 2 * (1 - p) * s_ * c_ * T1 + s_ ** 2 * T2)
        vals.append(integ(lambda s: s * (q_polar(s) - Q * s ** (p - 2)), S, smin=1e-12) - Q * 1e-12 ** p / p); Ks.append(K); Qs.append(Q)
        # (the hsH_* states of 4P(b)(xv) were produced with the Cartesian form q = p(p-1) F - 2(p-1) s F' + s^2 F'', whose cancellation error at S = 1e4 is
        #  about 1.1e-6 K: their exact S = 1e4 cutoff C_p is 1.13e-6 K, not 1e-9 K; verifier 229)
    B1 = beta1_rows(m); v = torch.tensor(vals, device=m.dev); Kv = torch.tensor(Ks, device=m.dev); Qv = torch.tensor(Qs, device=m.dev)
    return v @ B1, Kv @ B1, Qv @ B1

def m0_row(m, c, S=1e12, per_decade=20, ngl=16, batch=256):
    """row vector (nu,) with row . u = m_0(u) (truncated at S); uses the primitive K_u(t) = -H_u(t) - J_u(1) + J_u(t) on the identity basis."""
    rad = m.rad; N = m.N; M = m.M; P = rad.p; p = 1.0 / c; dev = m.dev; nu = m.nu
    Bv = mode_value_rows(m).cpu().numpy()                                                                 # (N+1, M, nu)
    k = np.arange(M); sgn = (-1.0) ** k; n = N + 3; tc = np.cos(np.pi * (2 * np.arange(n) + 1) / (2 * n))
    # quadrature in s: [0, 1e-8] (K ~ const) + log panels on [1e-8, S]
    xg, wg = np.polynomial.legendre.leggauss(ngl); s0 = 1e-8
    edges = s0 * 10.0 ** (np.arange(0, int(round(per_decade * np.log10(S / s0))) + 1) / per_decade)
    a = np.log(edges[:-1]); b = np.log(edges[1:]); X = 0.5 * (b - a)[:, None] * xg[None, :] + 0.5 * (a + b)[:, None]; Sq = np.exp(X).reshape(-1)
    Wq = ((0.5 * (b - a))[:, None] * wg[None, :] * np.exp(X)).reshape(-1)                                  # ds = s dx
    tq = rad.t_of_r(Sq); PRq = interp_matrix(rad.tR_np, tq, rad.wR_np); PRc = interp_matrix(rad.tR_np, tc, rad.wR_np); PR0 = interp_matrix(rad.tR_np, np.array([-1.0]), rad.wR_np)
    wq_ = (1 - tq) / 2; sigc = (1 + tc) / 2; wc = (1 - tc) / 2; Qmc = wc + 2 * P * sigc
    _, Krow, Qrow = cp_row(m, c); Qrow = Qrow.cpu().numpy()
    row = np.zeros(nu)
    for k0 in range(0, nu, batch):
        k1 = min(nu, k0 + batch); Bb = Bv[:, :, k0:k1]                                                     # (N+1, M, nb)
        bq = np.einsum('qi,imn->qmn', PRq, Bb); Hq = wq_[:, None] * np.einsum('qmn,m->qn', bq, sgn)       # H at the s-quadrature points (nq, nb)
        bc = np.einsum('qi,imn->qmn', PRc, Bb); Jpc = Qmc[:, None] * np.einsum('qmn,m->qn', bc[:, 1:, :], (k[1:] ** 2 * sgn[1:])) / sigc[:, None]   # J' at Chebyshev points (n, nb)
        cJp = C.chebfit(tc, Jpc, N + 1); cJ = C.chebint(cJp, lbnd=-1.0); J1 = C.chebval(1.0, cJ); Jq = C.chebval(tq, cJ).T if cJ.ndim == 2 else C.chebval(tq, cJ)
        # chebval with 2-D coefficients returns shape (nb, nq) -> transpose to (nq, nb)
        Kq = -Hq - J1[None, :] + Jq                                                                        # (nq, nb)
        # K at s = 0 (t = -1): -H(-1) - J(1) + 0
        b0 = np.einsum('qi,imn->qmn', PR0, Bb)[0]; H0 = 1.0 * np.einsum('mn,m->n', b0, sgn); K0 = -H0 - J1
        sub = np.where(Sq > 1.0, Sq ** (p - 1) / (1 - p), 0.0)                                            # subtract Q s^(p-1)/(1-p) for s > 1
        I = (Wq[:, None] * Kq).sum(0) + K0 * s0 - Qrow[k0:k1] * (Wq * sub).sum() - Qrow[k0:k1] / (p * (1 - p))
        row[k0:k1] = I
    return torch.tensor(row, device=dev), Krow, torch.tensor(Qrow, device=dev)

def m0_value(m, u, c, Qrow, S=1e12):
    """accurate value of the truncated functional m_0(u) = V_2(0, S) - Q(u) S^p/(p(1-p)) via the axis primitive on the actual mode values (the row . u product
    loses ~7 digits by cancellation in the local coefficient basis: cancellation ratio 1e7 at 48x12, 12:44Z test); Q(u) = Qrow . u."""
    ap = hs_m0.AxisPrimitive(m, u); p = 1.0 / c; _, V2_e, _ = ap.V2_axis(ymax=S); Q = float(Qrow @ u)
    return float(V2_e[-1]) - Q * S ** p / (p * (1 - p))

if __name__ == '__main__':
    for f in sys.argv[1:]:
        st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
        hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
        rc, rK, rQ = cp_row(m, c); d = hs_cp.cp_of_state(m, u, c)
        rm, _, _ = m0_row(m, c); o = hs_m0.analyse(f, verbose=False)
        print(f"{f.split('/')[-1][:-3]:28s} C_p row.u {float(rc @ u):+.6e} vs cp_of_state form1 S=1e4 {d['forms'][1e4][0]:+.6e};  K row.u {float(rK @ u):+.8f} vs {d['K']:+.8f};  Q row.u {float(rQ @ u):+.8f} vs {d['Q']:+.8f};  m_0 row.u {float(rm @ u):+.6f} vs F-fit {o['m0']:+.6f} / direct {o.get('m0_direct', float('nan')):+.6f}")
