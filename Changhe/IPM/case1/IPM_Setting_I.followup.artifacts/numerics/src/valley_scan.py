"""Finite-amplitude scan of the residual along the softest directions of a (refreshed) Jacobian at a state (SPEC S7 'nonlinear
continuation at finite amplitude', here one-dimensional): for the k softest right singular vectors v_i (node norm, c_l per 1/400;
back-transformed to unit unscaled directions) evaluate |F(z + s v_i)| for s in +-{0.01, 0.03, 0.1, 0.3, 1, 3} and report |F|_2,
|F|_inf, the h(P) and identity rows, c_l and C along the scan, the quadratic fit |F|^2 = a + b s + c s^2 near s = 0 (curvature c
against sigma^2) and the remainder |F(z + s v) - F(z) - s J v| (noise floor if not quadratic).
Usage: python3 src/valley_scan.py runs/J_<tag>_refreshed.pt tag [k=4] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, tag = sys.argv[1], sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 4; Npsi = int(sys.argv[4]) if len(sys.argv) > 4 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = J.shape[0]
    Fz = lambda zz: ch.F(zz, **jt.RES_KW); F0 = Fz(z); nF0 = F0.norm().item()
    scale = torch.ones(n, device='cuda'); scale[-2] = 1.0 / 400.0
    sk, Vk = jt.soft_vectors(J * scale[None, :], k)
    out = dict(tag=tag, jpath=jpath, F0=nF0, dirs=[])
    print(f'{tag}: |F(z)| {nF0:.4e}; c_l {z[-2].item():.10f} C {z[-1].item():.8f}; softest scaled sigmas {[float(x) for x in sk]}', flush=True)
    amps = [-3, -1, -0.3, -0.1, -0.03, -0.01, 0.01, 0.03, 0.1, 0.3, 1, 3]
    for i in range(k):
        v = scale * Vk[:, i]; v = v / v.norm(); Jv = J @ v
        rows = []
        for s_ in amps:
            F = Fz(z + s_ * v); R = F - F0 - s_ * Jv
            rows.append(dict(s=s_, F2=float(F.norm()), Finf=float(F.abs().max()), hP=float(F[-2]), ident=float(F[-1]), remainder=float(R.norm()), cl=float(z[-2] + s_ * v[-2]), C=float(z[-1] + s_ * v[-1])))
        ss = np.array([r['s'] for r in rows]); f2 = np.array([r['F2'] for r in rows]) ** 2
        sel = np.abs(ss) <= 0.1; cf = np.polyfit(ss[sel], f2[sel], 2)
        d_ = dict(i=i, sigma_scaled=float(sk[i]), Jv_norm=float(Jv.norm()), dcl=float(v[-2]), dC=float(v[-1]), rows=rows, quad_fit_a_b_c=[float(cf[2]), float(cf[1]), float(cf[0])],
                  s_min_fit=float(-cf[1] / (2 * cf[0])) if cf[0] > 0 else None, F2min_fit=float(np.sqrt(max(cf[2] - cf[1] ** 2 / (4 * cf[0]), 0))) if cf[0] > 0 else None)
        out['dirs'].append(d_)
        print(f'  v{i}: sigma_scaled {d_["sigma_scaled"]:.3e} |Jv| {d_["Jv_norm"]:.3e} dc_l {d_["dcl"]:+.2e} dC {d_["dC"]:+.2e}; |F| along s: ' + ' '.join(f'{r["s"]:+g}:{r["F2"]:.3e}' for r in rows) + f'; remainder at s=+-0.01/0.1/1: {rows[6]["remainder"]:.1e}/{rows[8]["remainder"]:.1e}/{rows[10]["remainder"]:.1e}; quad fit min at s {d_["s_min_fit"]} with |F| {d_["F2min_fit"]}', flush=True)
    json.dump(out, open(f'{LANE}/runs/valley_{tag}.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
