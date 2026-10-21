"""SPEC S3 (g) prescribed-data test with a stored dense Jacobian J (unscaled coordinates z = (delta b nodes, dc_l, dC)).
Section: the segment x = x* - 1, y in [0.5, 3] (Gauss-Legendre points); trace of a perturbation: delta H = delta rho / rho at
the section points at fixed physical position (T_b = interpolation of delta b divided by b; the c_l entry = d log rho / d c_l
at fixed node values, through w(r; k) and the node radii; C entry 0).  Profiles F_i: Legendre polynomials P_0..P_7 in the
section parameter, orthonormal in the section's L2.  For each i: v_i = argmin |J v| subject to T v = F_i (exact constraint
through the QR of T^T; least squares in the complement), reported with |v_i| (unscaled and S3-norm), |J v_i| (the linearized
residual, against |F| of the state and the FD column error), the c_l and C components, far-field / near-P fractions, the
streamline alignment, the h(P)-row and identity-row components of J v_i (source-motion identity), and the principal angles
between span{v_1..v_k} for k = 1, 2, 4, 8 are left to the cross-resolution script.  Saves the v_i for the overlap test.
Usage: python3 src/s3g_section.py runs/J_<tag>.pt tag [nsec=24] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def trace_operator(model, b, clf, xs_sec, ys_sec):
    """T (nsec x n): delta H at the section points from (delta b nodes i >= 1, dc_l, dC)."""
    N, M = model.N, model.M; n = N * M + 2
    r = np.sqrt(xs_sec ** 2 + ys_sec ** 2); th = np.arctan2(ys_sec, xs_sec)
    def interp_rows(cl):
        q = model.q_of_r(r, cl); Pq = ipn.interp_matrix(model.q_np, q, model.wq_np)              # (nsec, N+1)
        s = model.ang.s_of_theta(th); Sa = np.cos(np.outer(s, 2 * np.arange(M))) @ model.ang.A['EE'].cpu().numpy()   # (nsec, M) values -> values
        return Pq, Sa
    Pq, Sa = interp_rows(clf)
    bn = b.cpu().numpy()
    bsec = np.einsum('pi,ij,pj->p', Pq, bn, Sa)                                                 # b at the section points
    Tb = (Pq[:, 1:, None] * Sa[:, None, :]).reshape(len(r), N * M) / bsec[:, None]              # delta b -> delta b / b
    # c_l entry: d log rho / d c_l at fixed node values: rho = r^3 w(r; k) cos^2 sin b(q(r; k), theta)
    def logrho(cl):
        k = 1.0 / cl; Pq_, Sa_ = interp_rows(cl); bs = np.einsum('pi,ij,pj->p', Pq_, bn, Sa_)
        return np.log(bs) + (k - 3) / 2 * np.log1p((r / model.L) ** 2)
    h = 1e-5; tcl = (logrho(clf + h) - logrho(clf - h)) / (2 * h)
    T = np.concatenate([Tb, tcl[:, None], np.zeros((len(r), 1))], axis=1)
    return torch.tensor(T, device='cuda'), bsec


def main():
    jpath, tag = sys.argv[1], sys.argv[2]; nsec = int(sys.argv[3]) if len(sys.argv) > 3 else 24; Npsi = int(sys.argv[4]) if len(sys.argv) > 4 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = J.shape[0]; N, M = model.N, model.M
    b, cl, C = ch.unpack(z); clf = float(cl)
    dg = jt.Diag(model, ch, b, clf, float(C)); xstar = dg.xstar
    F = ch.F(z, **jt.RES_KW); nF = F.norm().item()
    # section and profiles
    gx, gw = np.polynomial.legendre.leggauss(nsec); ys = 1.75 + 1.25 * gx; xs = np.full(nsec, xstar - 1.0)
    T, bsec = trace_operator(model, b, clf, xs, ys)
    Pleg = np.polynomial.legendre.legvander(gx, 7)                                               # (nsec, 8)
    gwy = 1.25 * gw                                                                              # physical arclength weights (dy = 1.25 dxi)
    Fi = Pleg / np.sqrt((gwy[:, None] * Pleg ** 2).sum(0))[None, :]                              # orthonormal in L2(section, dy)
    Wsec = torch.tensor(np.sqrt(gwy), device='cuda')
    Tw = Wsec[:, None] * T; Fw = Wsec[:, None] * torch.tensor(Fi, device='cuda')                 # weighted so that |.|_2 = L2(section)
    Dcol, Drow, Wgt = jt.s3_scalings(model, b, clf, float(C))
    out = dict(tag=tag, jpath=jpath, n=n, N=N, M=M, L=model.L, beta=model.beta, c_l=clf, xstar=xstar, F2=nF, nsec=nsec, section=dict(x=float(xstar - 1), y=[0.5, 3.0]))
    print(f'{tag}: x* {xstar:.6f}, section x = {xstar-1:.4f}, |F| {nF:.3e}, b on section {bsec.min():.3f}..{bsec.max():.3f}', flush=True)
    # the pointwise trace rows on a short section are nearly dependent (spectral interpolant, 24 points in a narrow sector), so the
    # constraint is imposed on the first 8 Legendre coefficients of the trace: Tleg = Fw^T Tw (8 x n), Tleg v = e_i; the pointwise
    # defect |Tw v - Fw e_i| (the higher Legendre content of the trace) is reported as the retained trace
    sT = torch.linalg.svdvals(Tw); Tleg = Fw.T @ Tw; sL = torch.linalg.svdvals(Tleg)
    print(f'  singular values of the pointwise trace operator: {sT[0].item():.3e} .. {sT[-1].item():.3e}; of the 8-row Legendre trace: {sL[0].item():.3e} .. {sL[-1].item():.3e}', flush=True)
    out['trace_sv'] = dict(pointwise=[float(x_) for x_ in sT], legendre8=[float(x_) for x_ in sL])
    nL = Tleg.shape[0]
    Q, R = torch.linalg.qr(Tleg.T, mode='complete'); Q1, Q2 = Q[:, :nL], Q[:, nL:]; R = R[:nL, :nL]
    JQ2 = J @ Q2
    t0 = time.time(); U2, S2, Vh2 = torch.linalg.svd(JQ2, full_matrices=False); print(f'  svd of J Q2 ({time.time()-t0:.0f}s): s range {S2[0].item():.3e} .. {S2[-1].item():.3e}', flush=True)
    out['JQ2_smallest'] = [float(x_) for x_ in S2[-10:]]
    rows = []; Vs = []
    for i in range(8):
        e = torch.zeros(nL, device='cuda'); e[i] = 1.0; f = Fw[:, i]
        vp = Q1 @ torch.linalg.solve_triangular(R.T, e[:, None], upper=False)[:, 0]
        rhs = -(J @ vp); w = Vh2.T @ ((U2.T @ rhs) / S2); v = vp + Q2 @ w
        Jv = J @ v
        d_ = dict(i=i, v_norm=float(v.norm()), v_norm_S3=float((v / Dcol).norm()), Jv_norm=float(Jv.norm()), Jv_norm_S3=float((Drow * Jv).norm()),
                  Jv_over_v=float(Jv.norm() / v.norm()), legendre_defect=float((Tleg @ v - e).norm()), trace_defect_pointwise=float((Tw @ v - f).norm()),
                  Jv_hP_row=float(Jv[-2]), Jv_ident_row=float(Jv[-1]), Jv_inner_rows_max=float(Jv[:3 * M].abs().max()))
        d_.update(dg.report(v)); rows.append(d_); Vs.append(v.cpu())
        print(f'  F{i}: |v| {d_["v_norm"]:.3e} (S3 {d_["v_norm_S3"]:.3e}) |Jv| {d_["Jv_norm"]:.3e} (S3 {d_["Jv_norm_S3"]:.3e}) |Jv|/|v| {d_["Jv_over_v"]:.3e} dc_l {d_["dcl"]:+.2e} dC {d_["dC"]:+.2e} far {d_["radial"][">100"]:.2f} nearP {d_["nearP_fraction"]:.2f} align {d_["streamline_alignment"]:.3f} hProw {d_["Jv_hP_row"]:+.1e} ident {d_["Jv_ident_row"]:+.1e} ptdef {d_["trace_defect_pointwise"]:.2e}', flush=True)
    V = torch.stack(Vs, 1)
    # verifier (q1design, point 5): the cheapest data direction. With A = Tleg J^-1 (8 x n), beta(g)^2 = g^T (A A^T)^-1 g; the
    # eigenvectors of G = A A^T give the data directions g ordered by cost beta = 1/sqrt(lambda).
    A = torch.linalg.solve(J.T, Tleg.T).T                                                        # Tleg J^-1
    G = A @ A.T; lam, Ug = torch.linalg.eigh(G)
    out['G_eigenvalues'] = [float(x_) for x_ in lam]; out['beta_cheapest'] = float(1 / torch.sqrt(lam[-1])); out['beta_dearest'] = float(1 / torch.sqrt(lam[0]))
    out['g_cheapest'] = [float(x_) for x_ in Ug[:, -1]]
    g = Ug[:, -1]; vp = Q1 @ torch.linalg.solve_triangular(R.T, g[:, None], upper=False)[:, 0]
    rhs = -(J @ vp); w = Vh2.T @ ((U2.T @ rhs) / S2); vmin = vp + Q2 @ w; Jv = J @ vmin
    dmin = dict(i='cheapest', g=out['g_cheapest'], v_norm=float(vmin.norm()), v_norm_S3=float((vmin / Dcol).norm()), Jv_norm=float(Jv.norm()), Jv_norm_S3=float((Drow * Jv).norm()),
                Jv_hP_row=float(Jv[-2]), Jv_ident_row=float(Jv[-1])); dmin.update(dg.report(vmin)); out['cheapest'] = dmin
    print(f'  G eigenvalues (cost beta = 1/sqrt(lambda)): betas {" ".join("%.3e" % (1/np.sqrt(l)) for l in lam.cpu().numpy()[::-1])}; cheapest g = {np.round(Ug[:, -1].cpu().numpy(), 3)}; its v: |v| {dmin["v_norm"]:.3e} |Jv| {dmin["Jv_norm"]:.3e} dc_l {dmin["dcl"]:+.2e} dC {dmin["dC"]:+.2e} far {dmin["radial"][">100"]:.2f} nearP {dmin["nearP_fraction"]:.2f} align {dmin["streamline_alignment"]:.3f}', flush=True)
    Vs.append(vmin.cpu()); V = torch.stack(Vs, 1)
    # principal angles between span{v_1..v_k} and the softest right singular vectors are not needed here; save V for the
    # cross-resolution overlap test (evaluate delta H on a common grid in src/s3g_compare.py)
    out['rows'] = rows
    json.dump(out, open(f'{LANE}/runs/s3g_{tag}.json', 'w'), indent=1)
    torch.save(dict(V=V, xs=xs, ys=ys, Fi=Fi, gw=gwy, state=D['state'] if isinstance(D['state'], str) else str(D['state'])), f'{LANE}/runs/s3g_{tag}_vectors.pt')
    print('saved', f'runs/s3g_{tag}.json')


if __name__ == '__main__':
    main()
