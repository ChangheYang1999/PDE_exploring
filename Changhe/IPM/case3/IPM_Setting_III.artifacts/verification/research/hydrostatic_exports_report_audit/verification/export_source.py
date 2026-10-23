"""Export, per HS state, the quantities the verifier needs to recompute the 4P(b)(ii)/(viii) claims independently of the lane's code (verifier 09:34Z: 'producer
SVD matrices still OPEN for independent recomputation'): the residual vector F at the stall (rows: collocation points in the model's order, then a0 - 1, K - 1
[, centre row]), the collocation points (X, Y), the singular values of the residual rows J_h in the full coefficient space (S_full), the singular values of
J_h V on the visible coefficient subspace (S_vis) with the per-mode kept dimensions, the per-mode projected dilation vector v, the three residual fractions
and the normalised gradient.  Dense Jacobians are not exported (size); they are reproducible from the state and the model options.  Output:
artifacts/data/hs/spectra/<tag>.npz and a META.json.  Usage: python3 src/hs_export_spectra.py runs/hsA_c3.0_N64.pt ..."""
import sys, json, hashlib, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve, hs_dilation_overlap as hdo
torch.set_default_dtype(torch.float64)
meta = {}
for f in sys.argv[1:]:
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; io = st.get('inverse_options', {}); P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=io.get('n_in', 24), n_tail=io.get('n_tail', 80), fine=io.get('fine', False), hstep=io.get('hstep', 'x'))
    centre = io.get('centre', 'drop'); hsm.centre_mode = centre; hsm.centre_exact = (io.get('centre_row', '') == 'exact axis primitive'); hsm.build_maps(); m = hsm.m; u = st['u'].to(m.dev)
    F, info = hsm.residual(u, c, centre); J = hsm.jacobian(u, c, False); nex = 3 if centre == 'keep' else 2; JR = J[:-nex]
    U, S, Vh = torch.linalg.svd(JR, full_matrices=False); keep = S >= 1e-13 * S[0]
    Uf, Sf, Vhf = torch.linalg.svd(J, full_matrices=False); keepf = Sf >= 1e-13 * Sf[0]
    nF = F.norm().item(); fr = dict(kept=(Uf[:, keepf].T @ F).norm().item() / nF, dropped=(Uf[:, ~keepf].T @ F).norm().item() / nF, outside=(F - Uf @ (Uf.T @ F)).norm().item() / nF, grad=(J.T @ F).norm().item() / (Sf[0].item() * nF))
    Vs = []; dims = []
    for k in range(m.M):
        A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); kp = S_ >= 1e-8 * S_[0]
        Vk = torch.zeros(m.nu, int(kp.sum()), device=m.dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[kp].T; Vs.append(Vk); dims.append(int(kp.sum()))
    V = torch.cat(Vs, 1); Sv = torch.linalg.svdvals(JR @ V)
    v, Dk = hdo.dilation_coeffs(m, u)
    tag = f.split('/')[-1][:-3]; out = f'artifacts/data/hs/spectra/{tag}.npz'
    np.savez(out, F=F.cpu().numpy(), X=hsm.X, Y=hsm.Y, S_full=S.cpu().numpy(), S_full_with_norm_rows=Sf.cpu().numpy(), S_vis=Sv.cpu().numpy(), vis_dims_per_mode=np.array(dims), offs=np.array(m.offs), dilation_v=v.cpu().numpy(), u=st['u'].numpy(), tk=m.rad.tR_np, c=c, c_map=c_map, P=P)
    meta[tag] = dict(N=N, M=M, c=c, P=P, c_map=c_map, rows=int(J.shape[0]), unknowns=int(J.shape[1]), centre=centre, hstep=io.get('hstep', 'x'), n_full_below_1em13=int((~keep).sum()), n_vis_below_1em13=int((Sv < 1e-13 * Sv[0]).sum()), n_vis_below_1em8=int((Sv < 1e-8 * Sv[0]).sum()),
                     residual_fractions=fr, F_norm=nF, F_max=F.abs().max().item(), state_sha256=hashlib.sha256(open(f, 'rb').read()).hexdigest(), npz=out.replace('artifacts/', ''))
    print(tag, 'exported', {k: (round(v, 6) if isinstance(v, float) else v) for k, v in meta[tag].items() if k in ('rows', 'unknowns', 'n_full_below_1em13', 'n_vis_below_1em13', 'n_vis_below_1em8')}, {k: round(v, 5) for k, v in fr.items()})
json.dump(dict(description='HS stall diagnostics export (NUM_REPORT 4P(b)(ii), (viii)); norms: Euclidean in the coefficient vector u and in the unweighted row vector F; S_full = singular values of the residual rows J_h (collocation rows only), S_full_with_norm_rows = of J incl. the a0 and K (and centre) rows (the solver cutoff 1e-13 refers to these); S_vis = singular values of J_h V, V = per-mode right singular vectors of the coefficient -> mode-value map sigma^k Ext_k with s >= 1e-8 of that mode largest; dilation_v = per-mode LS projection of g - X.grad g; F ordering: collocation points (X, Y) then a0 - 1, K - 1 [, centre row]; rebuild the model with c_map = P/(P-1), not with the final c', states=meta), open('artifacts/data/hs/spectra/META.json', 'w'), indent=1)
print('META written')
