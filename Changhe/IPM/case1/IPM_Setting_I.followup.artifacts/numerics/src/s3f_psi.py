"""SPEC S3 (f) in the Psi (P-regular) formulation: first-order costs from a stored dense Jacobian J of the hybrid Psi residual
(src/jac_dense.py; derivatives with respect to the unscaled unknowns (b nodes, c_l, C)):
   alpha_cl  = 1/|J^-T e_cl|,   alpha_C = 1/|J^-T e_C|,
   alpha_B3  = 1/|J^-T grad B_3|  (ibp and orig forms; grad_b B_3 along the axis footprints of unit node perturbations, with the
                                   lead's caution that node-localized footprints near the axis at small x give estimator artefacts),
   alpha_B3(smooth) = min over the span of K smooth directions (low Chebyshev x Fourier modes of delta b) of |J v| / |grad B_3 . v|
                      (an upper bound on alpha_B3 that avoids localized perturbations),
and the overlaps of grad B_3 with the softest right singular vectors.  Also |J^T F|/(|J| |F|) at the state.
Usage: python3 src/s3f_psi.py runs/J_<tag>.pt runs/state.npz outtag [Npsi_res=480] [Ksmooth=12]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '../lead/b3_functional/b3infl')
import numpy as np, torch, ipm_newton as ipn, charmap as cm, b3core
from s3f_alpha import axis_tables, axis_from_psit

LANE = '.'


def main():
    jpath, spath, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    Npsi_res = int(sys.argv[4]) if len(sys.argv) > 4 else 480
    Ks = int(sys.argv[5]) if len(sys.argv) > 5 else 12
    D = torch.load(jpath); J = D['J'].cuda(); n = J.shape[0]
    m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x); clf = float(cl); C = float(d['C'])
    model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi_res)
    N, M = model.N, model.M
    ch = cm.Charac(model); z = ch.pack(b, cl, C)
    F = ch.F(z, dt=0.01, dt_near=0.04, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)
    out = dict(tag=tag, N=N, M=M, L=model.L, beta=model.beta, Npsi_res=Npsi_res, n=n, c_l=clf, C=C, F2=float(F.norm()), Finf=float(F.abs().max()))
    out['stationarity'] = float((J.T @ F).norm() / (J.norm() * F.norm()))
    # c_l and C columns of J recomputed centrally with the accurate residual
    Ff = lambda zz: ch.F_fixed(zz, dt=0.01, dt_near=0.04)
    for col, h in ((n - 2, 1e-5), (n - 1, 1e-3)):
        e = torch.zeros(n, device='cuda'); e[col] = h; J[:, col] = (Ff(z + e) - Ff(z - e)) / (2 * h)
    # grad B_3: axis footprints (linear in b at fixed c_l) of unit node perturbations, through the accurate inverse
    tab = axis_tables(model, clf)
    g = model.geom(torch.tensor(clf, device='cuda')); fl = model.fields(b, torch.tensor(clf, device='cuda'), g)
    f0, fp0, fpp0 = axis_from_psit(model, tab, fl['psit_n'])
    xs = tab['xs']; w0 = clf * xs - f0.cpu().numpy(); wp0 = clf - fp0.cpu().numpy(); wpp0 = -fpp0.cpu().numpy()
    Bo0, Bi0, dd = b3core.b3_one(xs, w0, wp0, wpp0, clf, both=True)
    out['B3_orig'] = float(Bo0); out['B3_ibp'] = float(Bi0); out['xstar'] = float(dd['xs'])
    A = torch.zeros(3, N * M, len(xs), device='cuda')
    for start in range(0, N * M, 256):
        idx = torch.arange(start, min(start + 256, N * M), device='cuda'); B = idx.numel()
        Eb = torch.zeros(B, N + 1, M, device='cuda'); Eb[torch.arange(B, device='cuda'), idx // M + 1, idx % M] = 1.0
        flb = model.fields(b[None] + Eb, torch.tensor(clf, device='cuda'), g)
        fB, fpB, fppB = axis_from_psit(model, tab, flb['psit_n'])
        A[0, start:start + B] = -(fB - f0[None]); A[1, start:start + B] = -(fpB - fp0[None]); A[2, start:start + B] = -(fppB - fpp0[None])
    A = A.cpu().numpy()
    grad_i = np.zeros(n); grad_o = np.zeros(n); wscale = np.max(np.abs(w0)); t0 = time.time()
    for j in range(N * M):
        dw, dwp, dwpp = A[0, j], A[1, j], A[2, j]; amp = np.max(np.abs(dw)) + 1e-300; e = 1e-6 * wscale / amp
        Bop, Bip, _ = b3core.b3_one(xs, w0 + e * dw, wp0 + e * dwp, wpp0 + e * dwpp, clf, both=True)
        Bom, Bim, _ = b3core.b3_one(xs, w0 - e * dw, wp0 - e * dwp, wpp0 - e * dwpp, clf, both=True)
        grad_i[j] = (Bip - Bim) / (2 * e); grad_o[j] = (Bop - Bom) / (2 * e)
    print(f'grad B_3 over b columns done ({time.time()-t0:.0f}s)', flush=True)
    for s_, h in ((n - 2, 1e-5),):
        vals = []
        for sgn in (+1, -1):
            clh = clf + sgn * h; tabh = axis_tables(model, clh); gh = model.geom(torch.tensor(clh, device='cuda')); flh = model.fields(b, torch.tensor(clh, device='cuda'), gh)
            fh, fph, fpph = axis_from_psit(model, tabh, flh['psit_n'])
            vals.append(b3core.b3_one(xs, clh * xs - fh.cpu().numpy(), clh - fph.cpu().numpy(), -fpph.cpu().numpy(), clh, both=True))
        grad_o[n - 2] = (vals[0][0] - vals[1][0]) / (2 * h); grad_i[n - 2] = (vals[0][1] - vals[1][1]) / (2 * h)
    # (B_3 does not depend on C: w is independent of the amplitude normalization at fixed b and c_l)
    gi = torch.tensor(grad_i, device='cuda'); go = torch.tensor(grad_o, device='cuda')
    LU = torch.linalg.lu_factor(J)
    def JmT(v): return torch.linalg.lu_solve(*LU, v[:, None], adjoint=True)[:, 0]
    e_cl = torch.zeros(n, device='cuda'); e_cl[n - 2] = 1; e_C = torch.zeros(n, device='cuda'); e_C[n - 1] = 1
    out['alpha_cl'] = float(1 / JmT(e_cl).norm()); out['alpha_C'] = float(1 / JmT(e_C).norm())
    out['alpha_B3_ibp'] = float(1 / JmT(gi).norm()); out['alpha_B3_orig'] = float(1 / JmT(go).norm())
    out['grad_norm_ibp'] = float(gi.norm()); out['grad_norm_orig'] = float(go.norm()); out['grad_cl_ibp'] = float(gi[n - 2])
    # smooth-subspace version: low Chebyshev (in q) x Fourier (in s) modes of delta b, Ks radial x Ks angular, plus e_cl
    qn = model.q_np[1:]; sn = model.ang.s_np
    T_q = np.polynomial.chebyshev.chebvander(2 * qn - 1, Ks - 1)                                # (N, Ks)
    T_s = np.cos(np.outer(sn, 2 * np.arange(Ks)))                                                 # (M, Ks)
    Vs = np.einsum('ik,jl->ijkl', T_q, T_s).reshape(N * M, Ks * Ks)
    Vs = np.concatenate([np.vstack([Vs, np.zeros((2, Ks * Ks))]), e_cl.cpu().numpy()[:, None]], axis=1)   # (n, Ks^2 + 1)
    Vs = torch.tensor(Vs, device='cuda'); Vs, _ = torch.linalg.qr(Vs)
    JV = J @ Vs; gV = Vs.T @ gi
    # min |J v| / |g . v| over v in span: generalized problem: minimize |JV y| subject to gV . y = 1  -> y = (JV^T JV)^-1 gV / (gV^T (JV^T JV)^-1 gV)
    Gm = JV.T @ JV; y = torch.linalg.solve(Gm, gV); out['alpha_B3_ibp_smooth'] = float(1 / torch.sqrt(gV @ y))
    gVo = Vs.T @ go; yo = torch.linalg.solve(Gm, gVo); out['alpha_B3_orig_smooth'] = float(1 / torch.sqrt(gVo @ yo))
    # softest right singular vectors and their overlap with grad B_3
    V = torch.randn(n, 10, device='cuda')
    for _ in range(40):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
    JVk = J @ V; Uk, sk, Wk = torch.linalg.svd(JVk, full_matrices=False); Vk = V @ Wk.T; order = torch.argsort(sk)
    out['soft'] = [dict(sigma=float(sk[i]), v_dot_gradB3_ibp=float(Vk[:, i] @ gi), v_cl=float(Vk[n - 2, i]), v_C=float(Vk[n - 1, i])) for i in order[:8]]
    json.dump(out, open(f'{LANE}/runs/s3fpsi_{tag}.json', 'w'), indent=1)
    np.savez(f'{LANE}/runs/s3fpsi_{tag}_grad.npz', grad_ibp=grad_i, grad_orig=grad_o)
    print(json.dumps({k_: v_ for k_, v_ in out.items() if k_ != 'soft'}, indent=1))
    for s_ in out['soft']: print('  soft', s_)


if __name__ == '__main__':
    main()
