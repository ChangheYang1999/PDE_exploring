"""Exact (quadrature-free in xi) centre integral c_H = int_0^inf g_xixi(0, t) dt of a Q-basis density, by the verifier's axis primitive (result 190, lead-checked
09:13Z): on the y-axis d_y V_2(0, y) = int_y^inf g_xixi(0, t) dt = K(t(y)) with K(t) = -H(t) - J(1) + J(t), H = w sum_k (-1)^k sigma^k beta_k (so g(0, y) = y H),
J(t) = int_{-1}^t J' ds, J' = sum_k k^2 (-1)^k Q sigma^(k-1) beta_k, Q = w + 2P sigma.  Hence c_H = K(-1) = -a0 - J(1), J(1) = sum_k k^2 (-1)^k int_{-1}^1 Q b_k/sigma dt
with b_k = sigma^k beta_k the (degree-N polynomial) mode functions; the integrand is a polynomial of degree N, integrated exactly by Gauss-Legendre with 2N points.
The centre defect is D = c + c_H - 1.  This is an independent check of the finite-difference centre row of hs_solve (fixed step: error 5e-7 at 64x16).
Usage: python3 src/hs_axis_exact.py runs/hsA_*.pt ..."""
import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve
torch.set_default_dtype(torch.float64)

def centre_exact(m, u):
    rad = m.rad; N = m.N
    tq, wq = np.polynomial.legendre.leggauss(2 * N + 2)
    PR = hs_solve.bary_interp_matrix_torch(rad.tR_np, rad.wR_np, tq, m.dev)              # Radau values -> Gauss points (exact for degree <= N)
    bkR, _ = m.b_modes(m.beta_full(u), 'R'); bk = PR @ bkR                                # (nq, M) mode functions b_k = sigma^k beta_k
    t = torch.tensor(tq, device=m.dev); sig = (1 + t) / 2; Q = rad.Q(t); W = torch.tensor(wq, device=m.dev)
    k = m.kk.double(); sgn = (-1.0) ** k
    J1 = ((W * Q / sig)[:, None] * bk * (k ** 2 * sgn)[None, :]).sum()                   # k = 0 term vanishes (k^2 = 0); b_k/sigma finite for k >= 1
    a0 = m.jets(u)[0]
    return (-a0 - J1).item(), a0.item()

if __name__ == '__main__':
    ver = {'hsA_c3.0_N48': 3.395e-4, 'hsA_c3.0_N64': -2.909e-4, 'hsA_c3.0_N96': -1.779e-5, 'hsA_c3.0_N128': 1.026e-5,
           'hsD_c3.0_N64_keep': 4.487832440052405e-7, 'hsD_c3.0_N96_keep': 2.700193685622116e-8, 'hsD_c3.0_N64_keep_fine': -4.352319099443923e-5, 'hsD_c3.0_N64_keep_cfree': 7.436642710995469e-7}
    print("# exact axis-primitive centre defect D = c + c_H - 1 (c_H = -a0 - J(1)) vs the lane's FD-based value (key centre_defect_single, fixed step 1e-5) and the verifier's exact values where sent (187/09:11Z)")
    for f in sys.argv[1:]:
        st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']
        P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)                                   # the map was built from c_start; for free-c states c_map != c
        hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev)
        cH, a0 = centre_exact(m, u); D = c + cH - 1; tag = f.split('/')[-1][:-3]
        fd = st.get('centre_defect_single', float('nan')); v = ver.get(tag)
        print(f"{tag:28s} {N:3d}x{M:<3d} c {c:.7f} P {m.p:.7f}: D_exact {D:+.10e}  D_FD {fd:+.4e} (diff {D-fd:+.2e})" + (f"  verifier {v:+.10e} (diff {D-v:+.2e})" if v is not None else ""))
