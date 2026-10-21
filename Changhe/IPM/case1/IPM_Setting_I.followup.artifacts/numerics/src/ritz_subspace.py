"""Exact-action Ritz values on a candidate soft subspace. The dense finite-difference Jacobian J has an operator error of
order 1e-2 to 1e-1 (dirtest), so its singular values below that level are not reliable; what can be measured exactly are directional
derivatives of the residual. This script takes a candidate subspace (the k_m softest right singular vectors of the stored matrix in
the node norm, c_l per 1/400, plus optionally the vectors of a *_softvecs_*.pt file), orthonormalizes it (QR in unscaled coordinates),
computes the exact central actions d_j = (F(z + s q_j) - F(z - s q_j))/(2 s) with the smooth residual (jtools.RES_KW, Npsi), and
reports the singular values of D = [d_j] (upper bounds for the smallest singular values of the true Jacobian: sigma_i(J) <= sigma_i(D)
+ |E|, |E| about 1e-5 at s = 1e-4), the Ritz vectors' c_l and C components and far-field fractions, and the per-direction actions.
Usage: python3 src/ritz_subspace.py runs/J_<tag>.pt tag [k_matrix=24] [softvecs.pt] [s=1e-4] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, tag = sys.argv[1], sys.argv[2]; rest = sys.argv[3:]
    vfile = next((a for a in rest if a.endswith('.pt')), None); nums = [a for a in rest if not a.endswith('.pt')]
    km = int(nums[0]) if len(nums) > 0 else 24; s = float(nums[1]) if len(nums) > 1 else 1e-4; Npsi = int(nums[2]) if len(nums) > 2 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = J.shape[0]; N, M = model.N, model.M
    b, cl, C = ch.unpack(z)
    scale = torch.ones(n, device='cuda', dtype=torch.float64); scale[-2] = 1.0 / 400.0
    Js = J * scale[None, :]
    t0 = time.time(); sk, Vk = jt.soft_vectors(Js, km, iters=60); V = scale[:, None] * Vk; V = V / V.norm(dim=0, keepdim=True)
    print(f'{tag}: matrix-softest {km} singular values (scaled): {" ".join("%.2e" % v for v in sk.cpu().numpy())} ({time.time()-t0:.0f}s)', flush=True)
    if vfile:
        S = torch.load(vfile); V2 = (S['Vsoft_unscaled'] if 'Vsoft_unscaled' in S else S['V']).cuda().double(); V = torch.cat([V2, V], 1)
    Q, R = torch.linalg.qr(V); keep = R.diagonal().abs() > 1e-6; Q = Q[:, keep]; k = Q.shape[1]
    print(f'  candidate subspace dimension {k} (dropped {int((~keep).sum())} dependent)', flush=True)
    Fz = lambda zz: ch.F(zz, **jt.RES_KW); F0 = Fz(z)
    Dm = torch.zeros(n, k, device='cuda', dtype=torch.float64); acts = []
    for j in range(k):
        t0 = time.time(); q = Q[:, j]; d = (Fz(z + s * q) - Fz(z - s * q)) / (2 * s); Dm[:, j] = d; acts.append(float(d.norm()))
        Jq = J @ q
        print(f'  q{j}: exact action {acts[-1]:.3e}  matrix |Jq| {Jq.norm().item():.3e}  dc_l {q[-2].item():+.2e} dC {q[-1].item():+.2e} ({time.time()-t0:.0f}s)', flush=True)
    U, sv, Wt = torch.linalg.svd(Dm, full_matrices=False)
    ritz = sv.cpu().numpy()[::-1]; Wv = Q @ Wt.T   # Ritz vectors (columns, matching sv order)
    r, _, _ = model.radii(float(cl)); rr = np.repeat(r[1:], M)
    rows = []
    for i in range(min(10, k)):
        w = Wv[:, k - 1 - i]; wb = w[:N * M].cpu().numpy(); e = wb ** 2; tot = float((w ** 2).sum())
        rows.append(dict(i=i, ritz=float(ritz[i]), dcl=float(w[-2]), dC=float(w[-1]), far=float(e[rr > 100].sum() / tot), near=float(e[rr < 1].sum() / tot), mid=float(e[(rr >= 1) & (rr <= 100)].sum() / tot)))
        print(f'  Ritz {i}: sigma {ritz[i]:.3e} dc_l {rows[-1]["dcl"]:+.2e} dC {rows[-1]["dC"]:+.2e} energy r<1 {rows[-1]["near"]:.2f} 1..100 {rows[-1]["mid"]:.2f} r>100 {rows[-1]["far"]:.2f}', flush=True)
    # the component of F0 in the span of the exact actions (how much of the residual is reachable at first order within the subspace)
    Ud = U[:, sv > 1e-12]; proj = float((Ud.T @ F0).norm())
    print(f'  |F| {F0.norm().item():.4e}; component of F in span(D) {proj:.3e}; Ritz values ascending: {" ".join("%.3e" % v for v in ritz)}', flush=True)
    out = dict(tag=tag, jpath=jpath, k=k, s=s, Npsi=Npsi, tau_switch=cm.TAU_SWITCH, F=float(F0.norm()), F_in_spanD=proj, matrix_sigma=sk.cpu().numpy().tolist(), actions=acts, ritz=ritz.tolist(), ritz_vectors=rows)
    torch.save(dict(Q=Q.cpu(), D=Dm.cpu(), Wv=Wv.cpu(), state=D['state'] if isinstance(D['state'], str) else str(D['state'])), f'{LANE}/runs/ritz_{tag}.pt')
    json.dump(out, open(f'{LANE}/runs/ritz_{tag}.json', 'w'), indent=1); print(f'saved runs/ritz_{tag}.json', flush=True)


if __name__ == '__main__':
    main()
