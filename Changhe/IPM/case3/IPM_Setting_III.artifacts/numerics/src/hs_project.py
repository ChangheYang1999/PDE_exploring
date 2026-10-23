"""
hs_project.py -- project a saved hydrostatic trial state (N_c x M_c) onto a finer basis (N_f x M_f) of the SAME c (same radial map r^2 = sigma (1 - t)^(-2P),
P = c/(c - 1), L = 1), to be used as the start of a finer solve (hs_solve.py start=<file>): a START-DEPENDENCE test of the Gauss-Newton stalls at fixed size.
Method: the coarse mode values b_k(t) = sigma^k beta_k(t) (degree-N_c polynomials in t, exactly represented by their Radau values) are interpolated
barycentrically to the fine Radau nodes (exact in exact arithmetic); modes k >= M_c are zero; the fine coefficients are the least-squares projection
DR.project of the angular values b(t_i, theta_j) = sum_k b_k(t_i) cos 2k theta_j on the fine model's 3 M_f angles (the same projection as simple_start).
Check printed: max |g_proj - g_coarse| / (1 + r)^p on the hs_cauchy point set (should be at the rcond level ~1e-8, since the coarse space is a subspace).
usage: python3 src/hs_project.py <coarse.pt> N_f M_f <out.pt>
"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve, hs_cauchy
from ipm3 import interp_matrix
torch.set_default_dtype(torch.float64)

def main(src, Nf, Mf, out):
    st = torch.load(src, weights_only=False); Nc, Mc, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    assert Nf >= Nc and Mf >= Mc, 'projection onto a finer basis only'
    hc = hs_solve.HSModel(Nc, Mc, c_map, n_in=4, n_tail=4); mc = hc.m; uc = st['u'].to(mc.dev)
    hf = hs_solve.HSModel(Nf, Mf, c_map, n_in=4, n_tail=4); mf = hf.m
    assert abs(mc.p - mf.p) < 1e-14, 'same map exponent required (same c)'                   # the outer Radau radius differs with N; the map r(t) does not
    betac = mc.beta_full(uc)                                                                   # (Nc+1, Mc)
    bkR_c = (mc.rad.sigR[:, None] ** mc.kk[None, :]) * betac                                  # coarse mode values at coarse Radau nodes
    PR = torch.tensor(interp_matrix(mc.rad.tR_np, mf.rad.tR_np, mc.rad.wR_np), device=mc.dev)  # coarse Radau -> fine Radau (exact for degree <= Nc)
    bk_f = PR @ bkR_c                                                                          # (Nf+1, Mc)
    th = torch.tensor(mf.angf.theta_np, device=mf.dev); kk = torch.arange(Mc, device=mf.dev, dtype=torch.float64)
    Cmat = torch.cos(2.0 * th[None, :] * kk[:, None])                                          # (Mc, M2_f)
    F = bk_f @ Cmat                                                                            # b(t_i, theta_j) on the fine angles
    uf = mf.project(F)
    # check on the hs_cauchy common points
    gec = hs.GEval(mc, betac); gef = hs.GEval(mf, mf.beta_full(uf)); X, Y, R = hs_cauchy.points(); p = 1.0 / c
    gc, gxc, gyc = gec(X, Y); gf, gxf, gyf = gef(X, Y)
    dg = np.abs(gf - gc) / (1 + R) ** p; dgr = np.hypot(gxf - gxc, gyf - gyc) / (1 + R) ** (p - 1)
    a0c, bcc, ecc = [z.item() for z in mc.jets(uc)]; a0f, bcf, ecf = [z.item() for z in mf.jets(uf)]
    print(f"projected {src} ({Nc}x{Mc}) -> {Nf}x{Mf}: max |dg|/(1+r)^p {dg.max():.2e}, max |d grad g|/(1+r)^(p-1) {dgr.max():.2e} on {len(R)} points; "
          f"jets coarse a0 {a0c:.6f} E {ecc/a0c:.6f} B {bcc:.6f} | fine a0 {a0f:.6f} E {ecf/a0f:.6f} B {bcf:.6f}; max|u_f| {uf.abs().max().item():.3e}")
    torch.save(dict(u=uf.cpu(), beta=mf.beta_full(uf).cpu(), c=c, cl=c, C=c, N=Nf, M=Mf, L=1.0, gamma=1 / c, p=mf.p, basis='local', rcond=1e-8,
                    rep=f'projection of {src} onto {Nf}x{Mf} (hs_project.py; start for a start-dependence test)', source=src, result=None,
                    map_exponent_P=mf.p, tail_exponent=1 / c, tk=mf.rad.tR_np.copy(), proj_check=dict(max_dg_weighted=float(dg.max()), max_dgrad_weighted=float(dgr.max()))), out)
    print('saved', out)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
