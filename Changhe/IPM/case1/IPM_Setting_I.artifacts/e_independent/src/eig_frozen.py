"""Frozen-velocity linear eigenproblem: with U (hence Ur/r, Uth/r, coefU) frozen from a given b, the equation
   E = c_l [S b_t + (omega+3) b] + [Ur/r S b_t + Uth/r b_th + (Ur/r omega - 1 + coefU) b] = 0
is linear in b and linear in c_l:  A b = -c_l B b.  Rows at t=-1: continuity b(0,theta_j)-b(0,theta_0)=0 for j>=1 (A), 0 (B);
the j=0 row at t=-1 is the degenerate equation itself: (coefU(0) - 1) b0 + 3 c_l b0 = 0, i.e. the identity 3c_l - 1 - c = 0."""
import sys, numpy as np, torch, scipy.linalg as sla
sys.path.insert(0, 'src')
import ipm1, solve

def frozen_eigs(m, nw, b_frozen, cl_hint=None):
    flds = m.fields(b_frozen)
    n = nw.n; N, M = m.N, m.M
    S = nw.S[:, None].expand(N + 1, M).reshape(-1)
    om = m.omegaR[:, None].expand(N + 1, M).reshape(-1)
    Ur = flds['Ur_over_r'].reshape(-1); Uth = flds['Uth_over_r'].reshape(-1); cU = flds['coefU'].reshape(-1)
    B = S[:, None] * nw.Dt_big + torch.diag(om + 3)
    A = (Ur * S)[:, None] * nw.Dt_big + Uth[:, None] * nw.Dth_big + torch.diag(Ur * om - 1 + cU)
    # rows at t=-1: j=0 keep (degenerate equation = identity), j>=1 continuity
    for j in range(1, M):
        A[j, :] = 0; A[j, j] = 1; A[j, 0] = -1; B[j, :] = 0
    An = A.cpu().numpy(); Bn = B.cpu().numpy()
    w, V = sla.eig(An, -Bn)
    return w, V, flds

if __name__ == '__main__':
    dev = 'cuda'
    N, M, L = int(sys.argv[1]) if len(sys.argv) > 1 else 48, int(sys.argv[2]) if len(sys.argv) > 2 else 10, 1.0
    for cl0 in [1.5, 2.0, 3.0]:
        gamma = 1 / cl0
        m = ipm1.IPM1(N=N, M=M, L=L, gamma=gamma, device=dev)
        nw = solve.Newton(m, verbose=False)
        r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
        s2 = r ** 2 / (L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
        c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
        A = (3 * cl0 - 1 - c1) / cs
        b0 = one + A * s2
        w, V, flds = frozen_eigs(m, nw, b0)
        real = np.isfinite(w) & (np.abs(w.imag) < 1e-6 * (1 + np.abs(w.real)))
        wr = np.sort(w[real].real)
        sel = wr[(wr > 0.3) & (wr < 20)]
        print(f"c_l0={cl0}: frozen U from b0=1+{A:.3f}s2 (identity gives c_l={(1+m.psi_xy0(flds).item())/3:.4f}); "
              f"real eigenvalues c_l in (0.3,20): {np.array2string(sel, precision=4, max_line_width=250)}", flush=True)
        # eigenvectors: for eigenvalues in (1, 20): normalised b(0)=1, report max|b|, min b, b(inf) range
        for lam in sel[(sel > 1.0)][:8]:
            k = np.argmin(np.abs(w - lam)); v = V[:, k].real
            v = v / v[0]
            vb = torch.tensor(v, device=dev).reshape(N + 1, M)
            binf = (m.rad.ext1_R @ vb)
            print(f"      c_l={lam:.5f}: max|b|={np.abs(v).max():.3g} min b={v.min():.3g} b(inf)={binf.min().item():.3g}..{binf.max().item():.3g}  b(0,theta) spread={v[:M].max()-v[:M].min():.1e}")
