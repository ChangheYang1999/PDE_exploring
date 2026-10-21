"""Operator-channel test on the resolved soft directions (verifier 'rate' (3)): at a frozen state z and frozen directions v (Ritz vectors m of
runs/ritz_<tag>.pt), compute d_eta(v) = (F_eta(z + e v) - F_eta(z - e v)) / (2 e), e = 1e-4, for the baseline operator and for the variants
(a) both orbit steps halved (dt 0.005, dt_near 0.02), (b) Npsi 720, (c) tau_max 18 (tail formula unchanged); report |d| inside / outside the
masks |X - P| < 2, 5, |P_R (d_eta - d_base)| and the correlation of d_eta with d_base. Reading (verifier): small differences bound the sensitivity of the
action to those numerical channels at this state; large ones identify a relevant channel; neither establishes or refutes a continuum reading.
Usage: python3 src/opchannel.py runs/J_<tag>.pt runs/ritz_<tag>.pt tag [modes=2,5,9] [e=1e-4]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, rpath, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    modes = [int(a) for a in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['2', '5', '9'])]; e = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-4
    J, z, model, ch, D0 = jt.load_J(jpath, 480); del J; torch.cuda.empty_cache(); n = z.shape[0]; N, M = model.N, model.M
    b, cl, C = ch.unpack(z); cl = float(cl)
    s4 = f'{LANE}/runs/s4e_{os.path.basename(D0["state"]).replace(".npz", "")}.json'; xstar = float(json.load(open(s4))['xstar'])
    r, w, v = model.radii(cl); th = model.ang.theta_np
    rr = np.repeat(r[1:], M); tt = np.tile(th, N); X = rr * np.cos(tt); Y = rr * np.sin(tt); dP = np.hypot(X - xstar, Y)
    masks = {2: np.concatenate([dP < 2, [True, False]]), 5: np.concatenate([dP < 5, [True, False]])}
    R = torch.load(rpath); Wv = R['Wv'].cuda().double(); kk = Wv.shape[1]
    m720 = ipn.Model(N, M, model.L, device='cuda', beta=model.beta, nmodes=model.nmodes, Mq=model.Mq, Npsi=720); ch720 = cm.Charac(m720)
    variants = {'base': (ch, {}), 'dt/2': (ch, dict(dt=0.005, dt_near=0.02)), 'Npsi720': (ch720, {}), 'tau18': (ch, dict(tau_max=18.0))}
    out = dict(tag=tag, state=D0['state'], e=e, modes=[])
    print(f'{tag}: |F| base {ch.F(z, **jt.RES_KW).norm().item():.4e}; variants: ' + ', '.join(f'{k}: |F| {c.F(z, **{**jt.RES_KW, **kw}).norm().item():.4e}' for k, (c, kw) in variants.items() if k != 'base'), flush=True)
    for m in modes:
        vv = Wv[:, kk - 1 - m]; vv = vv / vv.norm(); res = dict(mode=m, variants={})
        d = {}
        for name, (c, kw) in variants.items():
            Fz = lambda zz: c.F(zz, **{**jt.RES_KW, **kw})
            d[name] = ((Fz(z + e * vv) - Fz(z - e * vv)) / (2 * e)).cpu().numpy()
        db = d['base']
        for name, dd in d.items():
            diff = dd - db; corr = float((dd @ db) / (np.linalg.norm(dd) * np.linalg.norm(db) + 1e-300))
            row = dict(norm=float(np.linalg.norm(dd)), corr_with_base=corr, in2=float(np.linalg.norm(dd[masks[2]])), in5=float(np.linalg.norm(dd[masks[5]])), out5=float(np.linalg.norm(dd[~masks[5]])),
                       diff_norm=float(np.linalg.norm(diff)), diff_in2=float(np.linalg.norm(diff[masks[2]])), diff_in5=float(np.linalg.norm(diff[masks[5]])), diff_out5=float(np.linalg.norm(diff[~masks[5]])))
            res['variants'][name] = row
            print(f'  mode {m} (Ritz {m + 1}) {name:>8s}: |d| {row["norm"]:.3e} (in2 {row["in2"]:.2e} in5 {row["in5"]:.2e} out5 {row["out5"]:.2e}); |d - d_base| {row["diff_norm"]:.2e} (in2 {row["diff_in2"]:.2e} in5 {row["diff_in5"]:.2e} out5 {row["diff_out5"]:.2e}); corr {corr:.6f}', flush=True)
        out['modes'].append(res)
    json.dump(out, open(f'{LANE}/runs/opchannel_{tag}.json', 'w'), indent=1); print(f'saved runs/opchannel_{tag}.json')


if __name__ == '__main__':
    main()
