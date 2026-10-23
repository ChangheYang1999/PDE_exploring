"""Overlap of the dilation direction with the near-null singular vectors of the hydrostatic residual rows (verifier 08:49Z: do not identify the smallest
singular vector with the dilation by its order; measure it).  Dilation g_l(X) = l g(X/l) (keeps g_y(0) = 1, scales K by l^(1 - 1/c)); its derivative at
l = 1 is d = g - X.grad g.  In the Q basis (g = y w b, w = (1 - t)/2, r d/dr = gmap(t) d/dt with gmap = (1 - t^2)/Q) the derivative of the mode
functions is exact and does not mix angular modes: D b_k(t) = -gmap(t) [b_k'(t) - b_k(t)/(1 - t)].  The coefficient vector v of d is obtained by the
model's per-mode LS projection.  Reported per state: |J_h v| / (smax |v|) (how far from a null direction of the residual rows J_h at the stall), the
overlap of v with the smallest right singular vector, with the span of singular values below 1e-13 smax and below 1e-8 smax, and the checks
a0-row . v = 0 and K-row . v = (1 - 1/c) K.
Usage: python3 src/hs_dilation_overlap.py runs/hsA_c3.0_N64.pt [more .pt]"""
import sys, time, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve
torch.set_default_dtype(torch.float64)

def dilation_coeffs(m, u):
    beta = m.beta_full(u); bkR, bkR_t = m.b_modes(beta, 'R'); t = m.rad.tR; Q = m.rad.Q(t); gmap = (1 - t ** 2) / Q
    Dk = -gmap[:, None] * (bkR_t - bkR / (1 - t)[:, None])                  # (N+1, M) mode values of the dilation derivative (0 at t = -1)
    return torch.cat([Dk[:, k] @ m.Proj[k].T for k in range(m.M)]), Dk

if __name__ != '__main__': sys.argv = sys.argv[:1]                      # importable (hs_export_spectra uses dilation_coeffs) without running the analysis
for f in sys.argv[1:]:
    t0 = time.time(); st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']
    io = st.get('inverse_options', {}); P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=io.get('n_in', 24), n_tail=io.get('n_tail', 80), fine=io.get('fine', False), hstep=io.get('hstep', 'x'))   # map from c_start (free-c states)
    hsm.centre_mode = io.get('centre', 'drop'); hsm.build_maps(); m = hsm.m; u = st['u'].to(m.dev)
    v, Dk = dilation_coeffs(m, u)
    # projection defect of the dilation field (how well the basis represents it)
    bv = m.b_modes(m.beta_full(v), 'R')[0]; pdef = ((bv - Dk).abs().max() / Dk.abs().max()).item()
    J = hsm.jacobian(u, c, False); nrows_extra = 3 if hsm.centre_mode == 'keep' else 2; JR = J[:-nrows_extra]
    U, S, Vh = torch.linalg.svd(JR, full_matrices=False); smax = S[0].item()
    vn = v / v.norm(); Jv = (JR @ vn).norm().item() / smax
    ov = (Vh @ vn)                                                            # components of the unit dilation vector along right singular vectors
    o_last = ov[-1].abs().item(); sub13 = S < 1e-13 * smax; sub8 = S < 1e-8 * smax; sub4 = S < 1e-4 * smax
    o13 = ov[sub13].norm().item(); o8 = ov[sub8].norm().item(); o4 = ov[sub4].norm().item()
    a0row = J[-nrows_extra]; Krow = J[-nrows_extra + 1]; K = m.farfield(u)['K'].item()
    # the same on the VISIBLE coefficient subspace (per-mode right singular vectors of the coefficient -> mode-value map with s >= 1e-8 smax, as in dr.run's
    # spectral_radius): J_h restricted to V_vis separates the degeneracy of the discrete hydrostatic map from the weakly visible coefficient directions of the basis
    Vs = []
    for k in range(m.M):
        A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ >= 1e-8 * S_[0]
        Vk = torch.zeros(m.nu, int(keep.sum()), device=m.dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[keep].T; Vs.append(Vk)
    V = torch.cat(Vs, 1); JV = JR @ V; Uv, Sv, Vhv = torch.linalg.svd(JV, full_matrices=False); svmax = Sv[0].item()
    vv = V.T @ vn; vis_frac = vv.norm().item(); vvn = vv / vv.norm(); ovv = Vhv @ vvn
    nv13 = int((Sv < 1e-13 * svmax).sum()); nv8 = int((Sv < 1e-8 * svmax).sum()); nv4 = int((Sv < 1e-4 * svmax).sum())
    ov13 = ovv[Sv < 1e-13 * svmax].norm().item(); ov8 = ovv[Sv < 1e-8 * svmax].norm().item(); ov4 = ovv[Sv < 1e-4 * svmax].norm().item()
    print(f"    visible subspace dim {V.shape[1]} of nu {m.nu}: J_h V singular values s_min/smax {Sv[-1].item()/svmax:.1e} s_2/smax {Sv[-2].item()/svmax:.1e}  count s<1e-13 smax {nv13}, <1e-8 {nv8}, <1e-4 {nv4}  "
          f"| dilation: fraction in V_vis {vis_frac:.6f}, overlap with v_smin {ovv[-1].abs().item():.3f}, with span s<1e-13 {ov13:.3f}, <1e-8 {ov8:.3f}, <1e-4 {ov4:.3f}  |J_h V vv|/(smax) {(JV @ vvn).norm().item()/svmax:.2e}")
    print(f"{f:32s} {N:3d}x{M:<3d} c {c:.3f}: |J_h v|/(smax|v|) {Jv:.2e}  s_min/smax {S[-1].item()/smax:.1e} s_2/smax {S[-2].item()/smax:.1e}  overlap(v, v_smin) {o_last:.3f}  "
          f"overlap(v, span s<1e-13 smax [{int(sub13.sum())}]) {o13:.3f}  (s<1e-8 [{int(sub8.sum())}]) {o8:.3f}  (s<1e-4 [{int(sub4.sum())}]) {o4:.3f}  |  a0row.v {(a0row @ v).item():+.1e} (exp 0)  Krow.v/((1-1/c)K) {(Krow @ v).item()/((1 - 1/c) * K):.6f} (exp 1)  proj.defect {pdef:.1e}  [{time.time()-t0:.0f}s]")
