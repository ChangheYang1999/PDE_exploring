"""Where does the action of a GENERIC direction sit? Companion to rows_reweight (verifier 'rate' question (2)): at the state of a Ritz file, compute the
central action (s = 1e-4) of (a) the smooth test direction (1 - q) q cos(2 s) b, (b) a random direction, (c) the softest Ritz vector with its far-field
part (r > r_cut) removed, (d) the residual F itself; report the fraction of |action|^2 within distance 2 and 5 of P and the RMS per row near P against
elsewhere. Usage: python3 src/action_location.py runs/J_<tag>.pt runs/ritz_<tag>.pt tag [Npsi=480]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, rpath, tag = sys.argv[1], sys.argv[2], sys.argv[3]; Npsi = int(sys.argv[4]) if len(sys.argv) > 4 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = z.shape[0]; N, M = model.N, model.M
    del J; torch.cuda.empty_cache()
    b, cl, C = ch.unpack(z); cl = float(cl)
    s4 = f'{LANE}/runs/s4e_{os.path.basename(D["state"]).replace(".npz", "")}.json'
    xstar = float(json.load(open(s4))['xstar']) if os.path.exists(s4) else 8.5774
    r, w, v = model.radii(cl); th = model.ang.theta_np
    rr = np.repeat(r[1:], M); tt = np.tile(th, N); X = rr * np.cos(tt); Y = rr * np.sin(tt); dP = np.hypot(X - xstar, Y)
    near2 = np.concatenate([dP < 2, [True, False]]); near5 = np.concatenate([dP < 5, [True, False]])
    Fz = lambda zz: ch.F(zz, **jt.RES_KW); s = 1e-4
    R = torch.load(rpath); Wv = R['Wv'].cuda().double(); v0 = Wv[:, -1] / Wv[:, -1].norm()
    q = torch.tensor(model.q_np, device='cuda'); sj = torch.tensor(model.ang.s_np, device='cuda')
    Vs = torch.outer((1 - q) * q, torch.cos(2 * sj)) * b; Vs[0] = 0
    vs = torch.cat([Vs[1:].reshape(-1), torch.zeros(2, device='cuda', dtype=torch.float64)]); vs = vs / vs.norm()
    g = torch.Generator(device='cuda'); g.manual_seed(0); vr = torch.randn(n, generator=g, device='cuda', dtype=torch.float64); vr[-2:] = 0; vr = vr / vr.norm()
    vf = v0.clone(); mask = torch.tensor(np.concatenate([rr > 100, [False, False]]), device='cuda'); vf[mask] = 0; vf = vf / vf.norm()
    vn = v0.clone(); vn[~mask] = 0; vn[-2:] = v0[-2:]; vn = vn / vn.norm()
    F0 = Fz(z); out = dict(tag=tag, xstar=xstar, rows_near2=int(near2.sum()), rows_near5=int(near5.sum()), n=n, items=[])

    def report(name, d):
        d = d.detach().cpu().numpy(); tot = (d ** 2).sum() + 1e-300
        f2 = (d[near2] ** 2).sum() / tot; f5 = (d[near5] ** 2).sum() / tot
        rms_near = np.sqrt((d[near5] ** 2).mean()); rms_far = np.sqrt((d[~near5] ** 2).mean())
        out['items'].append(dict(name=name, norm=float(np.sqrt(tot)), frac_d_lt_2=float(f2), frac_d_lt_5=float(f5), rms_near5=float(rms_near), rms_elsewhere=float(rms_far)))
        print(f'  {name:>34s}: |action| {np.sqrt(tot):.3e}  fraction within 2 / 5 of P: {f2:.3f} / {f5:.3f}  rms per row near5 {rms_near:.2e} elsewhere {rms_far:.2e} (ratio {rms_near / (rms_far + 1e-300):.1f})', flush=True)

    print(f'{tag}: |F| {F0.norm().item():.4e}; rows within 2 / 5 of P: {near2.sum()} / {near5.sum()} of {n}')
    report('residual F itself', F0)
    for name, vv in (('softest Ritz vector', v0), ('softest, far field r>100 removed', vf), ('softest, only r>100 and params', vn), ('smooth test (1-q)q cos2s b', vs), ('random', vr)):
        d = (Fz(z + s * vv) - Fz(z - s * vv)) / (2 * s); report(name, d)
    json.dump(out, open(f'{LANE}/runs/actloc_{tag}.json', 'w'), indent=1); print(f'saved runs/actloc_{tag}.json')


if __name__ == '__main__':
    main()
