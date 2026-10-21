"""Anatomy of the softest exact-action directions (verifier 'softmodes' suggestions, 14:01Z): for the k softest Ritz vectors of a
runs/ritz_<tag>.pt file (columns of Wv ordered by the SVD of D: softest last) at the state of the Jacobian file,
 (1) step sweep of the exact central action at s = 3e-5, 1e-4, 3e-4, 1e-3 (validates the Ritz value against roundoff and cubic terms);
 (2) split of the action into the shape part (delta b only), the C part and the c_l part (each applied alone), with the norms of the
     parts: shows how the identity term delta b of the Psi rows is cancelled by the velocity / parameter feedback;
 (3) sensitivity of the action to r_far (1e8, 1e12 instead of 1e10) and to the inverse resolution Npsi (360, 720 instead of 480), at s = 1e-4.
Usage: python3 src/mode_anatomy.py runs/ritz_<tag>.pt runs/J_<tag>.pt tag [k=3] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    rpath, jpath, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    k = int(sys.argv[4]) if len(sys.argv) > 4 else 3; Npsi = int(sys.argv[5]) if len(sys.argv) > 5 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = z.shape[0]; N, M = model.N, model.M
    R = torch.load(rpath); Wv = R['Wv'].cuda().double(); kk = Wv.shape[1]
    Fz = lambda zz, **kw: ch.F(zz, **{**jt.RES_KW, **kw})
    F0 = Fz(z); out = dict(tag=tag, ritz_file=rpath, jpath=jpath, F=float(F0.norm()), modes=[])
    print(f'{tag}: |F| {F0.norm().item():.4e}; TAU_SWITCH {cm.TAU_SWITCH}', flush=True)
    for i in range(k):
        v = Wv[:, kk - 1 - i]; v = v / v.norm(); res = dict(i=i, dcl=float(v[-2]), dC=float(v[-1]), shape_norm=float(v[:N * M].norm()))
        t0 = time.time(); sweep = {}
        for s in (3e-5, 1e-4, 3e-4, 1e-3):
            d = (Fz(z + s * v) - Fz(z - s * v)) / (2 * s); sweep[str(s)] = float(d.norm())
        res['sweep'] = sweep
        print(f'  mode {i}: dc_l {res["dcl"]:+.3e} dC {res["dC"]:+.3e} |shape| {res["shape_norm"]:.4f}; action sweep ' + ' '.join(f's={a}:{b:.3e}' for a, b in sweep.items()) + f' ({time.time()-t0:.0f}s)', flush=True)
        # parts
        s = 1e-4; parts = {}
        vb = v.clone(); vb[-2] = 0; vb[-1] = 0
        vc = torch.zeros_like(v); vc[-1] = v[-1]
        vl = torch.zeros_like(v); vl[-2] = v[-2]
        dfull = (Fz(z + s * v) - Fz(z - s * v)) / (2 * s)
        for name, vv in (('shape', vb), ('C', vc), ('c_l', vl)):
            if vv.norm() == 0: parts[name] = dict(norm=0.0, action=0.0); continue
            d = (Fz(z + s * vv) - Fz(z - s * vv)) / (2 * s); parts[name] = dict(norm=float(vv.norm()), action=float(d.norm()), cos_with_full=float((d @ dfull) / (d.norm() * dfull.norm() + 1e-300)))
        res['parts'] = parts; res['full_action'] = float(dfull.norm())
        print(f'    parts: ' + '; '.join(f'{a}: |part| {b["norm"]:.3e} action {b["action"]:.3e}' for a, b in parts.items()) + f'; full action {res["full_action"]:.3e}; identity term |delta b| {res["shape_norm"]:.3e}', flush=True)
        # sensitivity to r_far and Npsi
        sens = {}
        for rf in (1e8, 1e12):
            d = (Fz(z + s * v, r_far=rf) - Fz(z - s * v, r_far=rf)) / (2 * s); sens[f'r_far={rf:g}'] = float(d.norm())
        for npsi in (360, 720):
            m2 = ipn.Model(N, M, model.L, device='cuda', beta=model.beta, nmodes=model.nmodes, Mq=model.Mq, Npsi=npsi); ch2 = cm.Charac(m2)
            d = (ch2.F(z + s * v, **jt.RES_KW) - ch2.F(z - s * v, **jt.RES_KW)) / (2 * s); sens[f'Npsi={npsi}'] = float(d.norm())
            sens[f'|F|@Npsi={npsi}'] = float(ch2.F(z, **jt.RES_KW).norm())
            del m2, ch2
        res['sensitivity'] = sens
        print(f'    sensitivity (s 1e-4): ' + ' '.join(f'{a}:{b:.3e}' for a, b in sens.items()), flush=True)
        out['modes'].append(res)
    json.dump(out, open(f'{LANE}/runs/anatomy_{tag}.json', 'w'), indent=1); print(f'saved runs/anatomy_{tag}.json', flush=True)


if __name__ == '__main__':
    main()
