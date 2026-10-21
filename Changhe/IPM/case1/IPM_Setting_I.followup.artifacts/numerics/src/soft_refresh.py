"""Soft-subspace refresh of a stored dense Jacobian at a (converged) state: for the k softest right singular vectors v_i of J
(node norm, c_l per 1/400), compute the central directional derivative d_i = (F(z + s v_i) - F(z - s v_i))/(2 s) of the residual
(jtools.RES_KW) and replace J's action on span{v_i} by it (rank-one updates J <- J + (d_i - J v_i) v_i^T with orthonormal v_i).
Repeat for `rounds` rounds (new soft directions can emerge after the update).  Saves runs/J_<tag>_refreshed.pt (same keys as the
input plus 'refresh' = the log of |J v| vs |d| per round) for svd_report / s3g_section / constrained_newton.
Usage: python3 src/soft_refresh.py runs/J_<tag>.pt runs/state.npz outtag [k=8] [rounds=3] [s=0.02] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, spath, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    k = int(sys.argv[4]) if len(sys.argv) > 4 else 8; rounds = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    s_ = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-4   # 1e-4: the cubic term (s^2/6) F''' is then below 1e-7 and the roundoff 2.5e-6 (runs/noise_dnC.json)
    Npsi = int(sys.argv[7]) if len(sys.argv) > 7 else 480
    D = torch.load(jpath); J = D['J'].cuda(); n = J.shape[0]
    m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x); C = float(d['C'])
    model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi); ch = cm.Charac(model)
    z = ch.pack(b, cl, C)
    Fz = lambda zz: ch.F(zz, **jt.RES_KW); F0 = Fz(z)
    scale = torch.ones(n, device='cuda'); scale[-2] = 1.0 / 400.0
    print(f'{tag}: state {spath} |F| {F0.norm().item():.3e}; J from {jpath} (built at {D["state"]})', flush=True)
    # the c_l and C columns of jac_dense are one-sided with increments eps/400 and eps (the c_l one is tiny: roundoff-limited);
    # recompute both centrally with the residual used here (also puts them at the refresh state)
    FJ = lambda zz: ch.F_fixed(zz, dt=jt.RES_KW['dt'], dt_near=jt.RES_KW['dt_near'])
    for col, h in ((n - 2, 1e-5), (n - 1, 1e-3)):
        e = torch.zeros(n, device='cuda'); e[col] = h; newcol = (FJ(z + e) - FJ(z - e)) / (2 * h)
        print(f'  column {"c_l" if col == n - 2 else "C"}: stored norm {J[:, col].norm().item():.4e}, central {newcol.norm().item():.4e}, |diff| {(J[:, col] - newcol).norm().item():.3e}', flush=True)
        J[:, col] = newcol
    log = []; Vall = torch.zeros(n, 0, device='cuda')
    for rd in range(rounds):
        Js = J * scale[None, :]
        sk, Vk = jt.soft_vectors(Js, k)
        V = (scale[:, None] * Vk); V = V / V.norm(dim=0, keepdim=True)        # unscaled unit directions
        # orthonormalize against the directions already refreshed (so that earlier exact actions are kept)
        if Vall.shape[1] > 0:
            V = V - Vall @ (Vall.T @ V); V = V - Vall @ (Vall.T @ V)
            keep = V.norm(dim=0) > 1e-6; V = V[:, keep]
            if V.shape[1] == 0: print('  no new independent soft directions; stop', flush=True); break
        # rank-revealing orthonormal basis of the projected block (SVD; drop directions below 1e-8 of the largest)
        Uq, sq, _ = torch.linalg.svd(V, full_matrices=False); Q = Uq[:, sq > 1e-8 * sq[0]]
        if Vall.shape[1] > 0:
            Q = Q - Vall @ (Vall.T @ Q); Q, _ = torch.linalg.qr(Q)
            assert float((Vall.T @ Q).abs().max()) < 1e-10, 'new directions not orthogonal to the refreshed ones'
        row = []
        for i in range(Q.shape[1]):
            v = Q[:, i]; t0 = time.time()
            dF = (Fz(z + s_ * v) - Fz(z - s_ * v)) / (2 * s_)
            Jv = J @ v; row.append(dict(round=rd, i=i, candidate_sigma_scaled=float(sk[i]) if i < len(sk) else None, Jq_over_q_scaled=float(Jv.norm() / (v / scale).norm()), Jv=float(Jv.norm()), d=float(dF.norm()), diff=float((dF - Jv).norm()), dcl=float(v[-2]), dC=float(v[-1])))
            J = J + torch.outer(dF - Jv, v)
            print(f'  round {rd} v{i}: candidate sigma(scaled) {row[-1]["candidate_sigma_scaled"]}, |Jq|/|q|_scaled {row[-1]["Jq_over_q_scaled"]:.3e}, |Jv| {row[-1]["Jv"]:.3e} -> |d| {row[-1]["d"]:.3e} (|d - Jv| {row[-1]["diff"]:.3e}; dc_l {row[-1]["dcl"]:+.2e} dC {row[-1]["dC"]:+.2e}) ({time.time()-t0:.0f}s)', flush=True)
        log += row; Vall = torch.cat([Vall, Q], 1)
    out = dict(D); out['J'] = J.cpu(); out['refresh'] = log; out['refresh_state'] = spath; out['z0'] = z.cpu(); out['state'] = spath; out['F0'] = F0.cpu()
    out['provenance'] = dict(original_J=jpath, original_dt=D.get('dt'), original_Npsi=D.get('Npsi'), original_state=D.get('state'))
    out['dt'] = jt.RES_KW['dt']; out['Npsi'] = Npsi; out['refresh_res_kw'] = dict(jt.RES_KW); out['refresh_s'] = s_
    torch.save(out, f'{LANE}/runs/J_{tag}_refreshed.pt'); json.dump(log, open(f'{LANE}/runs/refresh_{tag}.json', 'w'), indent=1)
    Js = J * scale[None, :]; S = torch.linalg.svdvals(Js).cpu().numpy()
    print(f'after refresh: smallest singular values (node, c_l per 1/400): {" ".join("%.3e" % v for v in S[-12:][::-1])}; saved runs/J_{tag}_refreshed.pt', flush=True)


if __name__ == '__main__':
    main()
