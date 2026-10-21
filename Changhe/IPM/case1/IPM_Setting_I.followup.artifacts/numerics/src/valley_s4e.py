"""What varies along the soft directions (18:50Z): for the k softest Ritz vectors v of runs/ritz_<tag>.pt (unit node vectors), form the
states z +- s v (b, c_l, C all moved), run the S4 (e) row on each (src/s4e_row.py: c_l, C, x*, g(P), h(P) - 1, identity, |F|_psi, Taylor coefficients
d3, d5, d7 of the axis function w at 0, w''(x*), B_3 estimators) and report the central derivative (f(z + s v) - f(z - s v)) / (2 s) per unit direction
and the second difference (f+ - 2 f0 + f-) / s^2. Along a genuine family direction the state-defined quantities (x*, g(P), d3, ...) move at first
order while the residual stays flat (valley scan); the table says which quantities the valley moves and by how much per unit c_l change.
Usage: python3 src/valley_s4e.py runs/ritz_<tag>.pt tag [k=2] [s=0.05]"""
import sys, os, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

LANE = '.'
KEYS = ['F_psi_2', 'F_psi_inf', 'c_l', 'C', 'xstar', 'gP', 'hP_minus_1', 'identity_defect', 'd3', 'd5', 'd7', 'wpp_at_xstar', 'B3_ibp', 'B3_orig', 'remainder7_fitted_exponent']


def s4e(path, tag):
    out = f'{LANE}/runs/s4e_{tag}.json'
    if not os.path.exists(out):
        subprocess.run(['python3', f'{LANE}/src/s4e_row.py', path, tag], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return json.load(open(out))


def main():
    rpath, tag = sys.argv[1], sys.argv[2]; k = int(sys.argv[3]) if len(sys.argv) > 3 else 2; s = float(sys.argv[4]) if len(sys.argv) > 4 else 0.05
    R = torch.load(rpath); Wv = R['Wv'].double().cpu().numpy(); kk = Wv.shape[1]; spath = R['state']
    model, x, d = ipn.load_state(spath); N, M = model.N, model.M; b, cl = model.unpack(x); cl = float(cl); C = float(d['C'])
    base_tag = os.path.basename(spath).replace('.npz', ''); f0 = s4e(spath, base_tag)
    out = dict(tag=tag, state=spath, s=s, base={kq: f0.get(kq) for kq in KEYS}, modes=[])
    print(f'{tag}: state {spath} c_l {cl:.10f} C {C:.8f} |F| {f0["F_psi_2"]:.4e}; s = {s}')
    for i in range(min(k, kk)):
        v = Wv[:, kk - 1 - i]; v = v / np.linalg.norm(v); V = torch.zeros(N + 1, M, dtype=torch.float64, device=model.dev); V[1:] = torch.tensor(v[:N * M].reshape(N, M), device=model.dev)
        rows = {}
        for sign, nm in ((1, 'p'), (-1, 'm')):
            bb = b + sign * s * V; cll = cl + sign * s * float(v[-2]); CC = C + sign * s * float(v[-1])
            t = f'vs_{tag}_m{i}_{nm}'; p = f'{LANE}/runs/{t}.npz'
            ipn.save_state(p, model, model.pack(bb, cll), extra=dict(tag=t, C=CC, formulation='psi_hybrid_valley_point', source=spath, direction=i, s=sign * s))
            rows[nm] = s4e(p, t)
        res = dict(i=i, dcl=float(v[-2]), dC=float(v[-1]), deriv={}, second={}, plus={}, minus={})
        print(f'  mode {i}: dc_l {v[-2]:+.3e} dC {v[-1]:+.3e} per unit direction; values at -s / 0 / +s, central derivative per unit, second difference / s^2, derivative per unit c_l:')
        for kq in KEYS:
            fp, fm, fz = rows['p'].get(kq), rows['m'].get(kq), f0.get(kq)
            if fp is None or fm is None or fz is None: continue
            dv = (fp - fm) / (2 * s); d2 = (fp - 2 * fz + fm) / s ** 2
            res['deriv'][kq] = dv; res['second'][kq] = d2; res['plus'][kq] = fp; res['minus'][kq] = fm
            per_cl = dv / v[-2] if abs(v[-2]) > 1e-12 else float('nan')
            print(f'    {kq:>28s}: {fm:+.8e} / {fz:+.8e} / {fp:+.8e}   d/ds {dv:+.4e}   d2 {d2:+.3e}   per unit c_l {per_cl:+.4e}')
        out['modes'].append(res)
    json.dump(out, open(f'{LANE}/runs/valley_s4e_{tag}.json', 'w'), indent=1); print(f'saved runs/valley_s4e_{tag}.json')


if __name__ == '__main__':
    main()
