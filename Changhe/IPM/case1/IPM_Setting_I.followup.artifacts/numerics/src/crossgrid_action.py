"""Cross-grid test of the near-null directions (replaces the full (144,56) Jacobian, which the time budget excludes).
The k softest right singular vectors of the refreshed Jacobian at a converged (N0,M0) state (file *_softvecs_node_cl400.pt,
'Vsoft_unscaled': unit vectors in node norm, c_l and C components in natural units) are interpolated to a target grid (N1,M1)
at the same compactification scale L (b part by the Chebyshev x Fourier interpolant in (q, s), i.e. ipm_newton.project_state
applied to b + delta b minus its value at b; c_l and C components copied), orthonormalized (QR), and the exact central directional
derivatives d_j = (F(z1 + s q_j) - F(z1 - s q_j))/(2 s) of the target residual (jtools.RES_KW, Npsi) are computed at the projected
state z1.  Reported: per-direction actions |d_j|, the singular values of D = [d_j] (Rayleigh-Ritz values of J_1 on span Q: by
interlacing, the i-th smallest of them is an upper bound for the i-th smallest singular value of J_1), the same on the source grid
for calibration (actions of the source residual along the same vectors at the source state), the action along a smooth low-mode
direction on both grids, and the cubic-term check (s and 10 s for q_0).  Interpretation: Ritz values on the fine grid that stay at
the source level (<= 1e-3 per unit vector against about 50 for a smooth generic direction) show that the near-null subspace
persists under refinement; large values are inconclusive (the fine soft subspace may differ from the interpolated one).
Usage: python3 src/crossgrid_action.py runs/state.npz runs/softvecs.pt N1 M1 beta L1 tag [k=10] [s=1e-4] [Npsi=480] [--no-source]
"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def smooth_dir(model, n):
    qn = model.q_np[1:]; sn = model.ang.s_np
    sm = np.outer(np.polynomial.chebyshev.chebval(2 * qn - 1, [0, 0, 1]) - 1.0, np.cos(2 * sn)).ravel()
    v = torch.zeros(n, device='cuda', dtype=torch.float64); v[:model.N * model.M] = torch.tensor(sm, device='cuda'); return v / v.norm()


def actions(ch, z, Q, s, label):
    Fz = lambda zz: ch.F(zz, **jt.RES_KW)
    F0 = Fz(z); D = torch.zeros(Q.shape, device='cuda', dtype=torch.float64); rows = []
    for j in range(Q.shape[1]):
        t0 = time.time(); q = Q[:, j]
        d = (Fz(z + s * q) - Fz(z - s * q)) / (2 * s); D[:, j] = d
        rows.append(dict(j=j, action=float(d.norm()), dcl=float(q[-2]), dC=float(q[-1])))
        print(f'  {label} q{j}: |d| {rows[-1]["action"]:.3e} (dc_l {rows[-1]["dcl"]:+.2e} dC {rows[-1]["dC"]:+.2e}) ({time.time()-t0:.0f}s)', flush=True)
    sv = torch.linalg.svdvals(D).cpu().numpy()
    print(f'  {label}: |F| {F0.norm().item():.3e}; Ritz singular values of J Q (ascending): {" ".join("%.3e" % v for v in sv[::-1])}', flush=True)
    return F0, D, rows, sv


def main():
    spath, vfile = sys.argv[1], sys.argv[2]; N1, M1, beta, L1 = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]); tag = sys.argv[7]
    nums = [a for a in sys.argv[8:] if not a.startswith('--') and (sys.argv[sys.argv.index(a) - 1] != '--target_state')]
    target_state = sys.argv[sys.argv.index('--target_state') + 1] if '--target_state' in sys.argv else None   # evaluate the actions at this fine state instead of the projected source state
    k = int(nums[0]) if len(nums) > 0 else 10; s = float(nums[1]) if len(nums) > 1 else 1e-4; Npsi = int(nums[2]) if len(nums) > 2 else 480
    do_source = '--no-source' not in sys.argv
    m0, x0, d0 = ipn.load_state(spath); b0, cl = m0.unpack(x0); cl = float(cl); C = float(d0['C'])
    S = torch.load(vfile); V0 = S['Vsoft_unscaled'][:, :k].cuda().double(); n0 = V0.shape[0]; N0, M0 = m0.N, m0.M
    assert n0 == N0 * M0 + 2 and abs(L1 - m0.L) < 1e-12, 'same compactification scale L required (moving-node term otherwise)'
    out = dict(tag=tag, state=spath, softvecs=vfile, source=(N0, M0, m0.beta, m0.L), target=(N1, M1, beta, L1), k=k, s=s, Npsi=Npsi, res_kw=dict(jt.RES_KW), tau_switch=cm.TAU_SWITCH)
    print(f'{tag}: state {spath} ({N0},{M0}) -> ({N1},{M1},{beta}) L {L1}; k {k} s {s:g} Npsi {Npsi}', flush=True)
    # ---- source grid (calibration) ----
    if do_source:
        model0 = ipn.Model(N0, M0, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi); ch0 = cm.Charac(model0)
        z0 = ch0.pack(b0, cl, C)
        Q0, R0 = torch.linalg.qr(V0); out['source_qr_diag'] = R0.diagonal().cpu().numpy().tolist()
        F00, D0, rows0, sv0 = actions(ch0, z0, Q0, s, 'source')
        out['source'] = dict(F=float(F00.norm()), rows=rows0, ritz=sv0[::-1].tolist())
        d_sm = actions(ch0, z0, smooth_dir(model0, n0)[:, None], s, 'source smooth')[2][0]['action']; out['source']['smooth_action'] = d_sm
        d10 = (ch0.F(z0 + 10 * s * Q0[:, 0], **jt.RES_KW) - ch0.F(z0 - 10 * s * Q0[:, 0], **jt.RES_KW)) / (20 * s)
        out['source']['q0_action_at_10s'] = float(d10.norm()); out['source']['q0_diff_s_10s'] = float((d10 - D0[:, 0]).norm())
        print(f'  source q0: action at s {D0[:, 0].norm().item():.3e}, at 10 s {d10.norm().item():.3e}, difference {out["source"]["q0_diff_s_10s"]:.2e} (cubic term)', flush=True)
        del model0, ch0
    # ---- target grid ----
    model1 = ipn.Model(N1, M1, L1, device='cuda', beta=beta, Npsi=Npsi); ch1 = cm.Charac(model1); n1 = N1 * M1 + 2
    x1 = ipn.project_state(m0, x0, model1); b1, _ = model1.unpack(x1); z1 = ch1.pack(b1, cl, C)
    if target_state:
        mT, xT, dT = ipn.load_state(target_state); bT, clT = mT.unpack(xT); z1 = ch1.pack(bT, float(clT), float(dT['C'])); out['target_state'] = target_state
        print(f'  actions evaluated at the fine state {target_state} (c_l {float(clT):.10f}, C {float(dT["C"]):.8f}); directions interpolated at the source c_l', flush=True)
    V1 = torch.zeros(n1, k, device='cuda', dtype=torch.float64)
    for j in range(k):
        db0 = torch.zeros(N0 + 1, M0, device='cuda', dtype=torch.float64); db0[1:] = V0[:N0 * M0, j].reshape(N0, M0)
        x0p = m0.pack(b0 + db0, cl); b1p, _ = model1.unpack(ipn.project_state(m0, x0p, model1))
        V1[:N1 * M1, j] = (b1p - b1)[1:].reshape(-1); V1[-2, j] = V0[-2, j]; V1[-1, j] = V0[-1, j]
    norms1 = V1.norm(dim=0); out['interp_norms'] = norms1.cpu().numpy().tolist()
    Q1, R1 = torch.linalg.qr(V1); out['target_qr_diag'] = R1.diagonal().cpu().numpy().tolist()
    G = (V1 / norms1).T @ (V1 / norms1); out['target_max_offdiag_cos'] = float((G - torch.eye(k, device='cuda', dtype=torch.float64)).abs().max())
    print(f'  interpolated norms {" ".join("%.3f" % v for v in norms1.cpu().numpy())}; max |cos| between interpolated directions {out["target_max_offdiag_cos"]:.3f}', flush=True)
    F10, D1, rows1, sv1 = actions(ch1, z1, Q1, s, 'target')
    out['target'] = dict(F=float(F10.norm()), F_inf=float(F10.abs().max()), hP=float(F10[-2]), ident=float(F10[-1]), rows=rows1, ritz=sv1[::-1].tolist())
    # actions along the interpolated (un-orthonormalized, unit) vectors themselves: D1 R1^-1 scaled
    Dv = (D1 @ R1) / norms1[None, :]; out['target']['actions_along_interpolated_unit_vectors'] = Dv.norm(dim=0).cpu().numpy().tolist()   # V1 = Q1 R1, so J V1 = D1 R1 (verifier review3 fixed an inverted reconstruction, 13:06Z)
    print(f'  target: actions along the interpolated unit vectors v_j/|v_j|: {" ".join("%.3e" % v for v in out["target"]["actions_along_interpolated_unit_vectors"])}', flush=True)
    d_sm = actions(ch1, z1, smooth_dir(model1, n1)[:, None], s, 'target smooth')[2][0]['action']; out['target']['smooth_action'] = d_sm
    d10 = (ch1.F(z1 + 10 * s * Q1[:, 0], **jt.RES_KW) - ch1.F(z1 - 10 * s * Q1[:, 0], **jt.RES_KW)) / (20 * s)
    out['target']['q0_action_at_10s'] = float(d10.norm()); out['target']['q0_diff_s_10s'] = float((d10 - D1[:, 0]).norm())
    print(f'  target q0: action at s {D1[:, 0].norm().item():.3e}, at 10 s {d10.norm().item():.3e}, difference {out["target"]["q0_diff_s_10s"]:.2e} (cubic term)', flush=True)
    # where does the target action live (radial shells / near P)?
    r1, _, _ = model1.radii(cl); rr = np.repeat(r1[1:], M1)
    for j in range(min(3, k)):
        d = D1[:N1 * M1, j].cpu().numpy(); e = d ** 2; tot = e.sum() + float(D1[-2, j]) ** 2 + float(D1[-1, j]) ** 2
        fr = dict(r_lt_1=float(e[rr < 1].sum() / tot), r_1_10=float(e[(rr >= 1) & (rr < 10)].sum() / tot), r_10_100=float(e[(rr >= 10) & (rr < 100)].sum() / tot), r_gt_100=float(e[rr >= 100].sum() / tot), hP_row=float(D1[-2, j] ** 2 / tot), ident_row=float(D1[-1, j] ** 2 / tot))
        out['target'][f'q{j}_action_distribution'] = fr
        print(f'  target q{j} action distribution: ' + ' '.join(f'{a} {b:.2f}' for a, b in fr.items()), flush=True)
    torch.save(dict(Q1=Q1.cpu(), D1=D1.cpu(), V1=V1.cpu(), z1=z1.cpu()), f'{LANE}/runs/crossgrid_{tag}.pt')
    json.dump(out, open(f'{LANE}/runs/crossgrid_{tag}.json', 'w'), indent=1)
    print(f'saved runs/crossgrid_{tag}.json', flush=True)


if __name__ == '__main__':
    main()
