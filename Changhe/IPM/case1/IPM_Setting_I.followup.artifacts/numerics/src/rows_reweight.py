"""Row-reweighting test on the stored exact-action matrices (verifier 'softref' (c)): for a Ritz file runs/ritz_<tag>.pt (Q orthonormal
candidate directions, D = central actions of the smooth residual at s = 1e-4, columns matching Q), multiply the residual rows in a physical
neighbourhood of P (|X - P| < R; node rows i = 1..N, j = 0..M-1 in F order) and the h(P) - 1 row by lambda and recompute the singular values of
the reweighted D. If the soft directions' residual content sits near P, upweighting those rows lifts the small values; if the directions are
null near P as well, the values do not move. This diagnoses sensitivity to row balance; it does not prove a regularity selection (verifier).
Usage: python3 src/rows_reweight.py runs/ritz_<tag>.pt tag [R=2,5] [lambdas=1,10,100,1000]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

LANE = '.'


def main():
    rpath, tag = sys.argv[1], sys.argv[2]
    Rs = [float(a) for a in (sys.argv[3].split(',') if len(sys.argv) > 3 else ['2', '5'])]
    lams = [float(a) for a in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['1', '10', '100', '1000'])]
    Rz = torch.load(rpath); D = Rz['D'].double().cpu().numpy(); Q = Rz['Q'].double().cpu().numpy(); spath = Rz['state']
    model, x, d = ipn.load_state(spath, device='cpu'); N, M = model.N, model.M; b, cl = model.unpack(x); cl = float(cl)
    s4 = f'{LANE}/runs/s4e_{os.path.basename(spath).replace(".npz", "")}.json'
    xstar = float(json.load(open(s4))['xstar']) if os.path.exists(s4) else 8.5774
    r, w, v = model.radii(cl); th = model.ang.theta_np
    rr = np.repeat(r[1:], M); tt = np.tile(th, N); X = rr * np.cos(tt); Y = rr * np.sin(tt); dP = np.hypot(X - xstar, Y)
    n = D.shape[0]; assert n == N * M + 2, (n, N, M)
    base = np.linalg.svd(D, compute_uv=False)[::-1]
    out = dict(tag=tag, state=spath, xstar=xstar, base_ritz=base[:12].tolist(), tests=[])
    print(f'{tag}: state {spath}; base Ritz values: ' + ' '.join(f'{s:.3e}' for s in base[:10]))
    # residual content of the soft directions near P: fraction of |D q_j|^2 in the near-P rows for the 4 softest Ritz vectors
    U, sv, Wt = np.linalg.svd(D, full_matrices=False); Dr = D @ Wt.T   # columns = actions of the Ritz vectors (softest last)
    for R in Rs:
        rows = np.concatenate([dP < R, [True, False]])   # node rows near P plus the h(P) row
        nrows = int(rows.sum())
        frac = [(float((Dr[rows, -1 - i] ** 2).sum() / ((Dr[:, -1 - i] ** 2).sum() + 1e-300))) for i in range(4)]
        print(f'  R = {R:g}: {nrows} rows (incl. h(P)); fraction of the 4 softest Ritz actions in these rows: ' + ' '.join(f'{f:.3e}' for f in frac) + f'  (row fraction {nrows / n:.3e})')
        for lam in lams:
            Dl = D.copy(); Dl[rows] *= lam; sl = np.linalg.svd(Dl, compute_uv=False)[::-1]
            out['tests'].append(dict(R=R, nrows=nrows, lam=lam, ritz=sl[:12].tolist(), frac_near_P_softest4=frac))
            print(f'    lambda = {lam:g}: ' + ' '.join(f'{s:.3e}' for s in sl[:10]))
    # the identity row alone and the h(P) row alone
    for name, idx in (('h(P) row', n - 2), ('identity row', n - 1)):
        fr = [float(Dr[idx, -1 - i] ** 2 / ((Dr[:, -1 - i] ** 2).sum() + 1e-300)) for i in range(4)]
        lifted = {}
        for lam in (100.0, 1e4):
            Dl = D.copy(); Dl[idx] *= lam; lifted[str(lam)] = np.linalg.svd(Dl, compute_uv=False)[::-1][:4].tolist()
        out['tests'].append(dict(row=name, frac_softest4=fr, lifted=lifted))
        print(f'  {name}: fraction of the 4 softest actions {" ".join(f"{f:.2e}" for f in fr)}; smallest 4 after x100: ' + ' '.join(f'{s:.2e}' for s in lifted['100.0']) + '; x1e4: ' + ' '.join(f'{s:.2e}' for s in lifted['10000.0']))
    json.dump(out, open(f'{LANE}/runs/reweight_{tag}.json', 'w'), indent=1); print(f'saved runs/reweight_{tag}.json')


if __name__ == '__main__':
    main()
