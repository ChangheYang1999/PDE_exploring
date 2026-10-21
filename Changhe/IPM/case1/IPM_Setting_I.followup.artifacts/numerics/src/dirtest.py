"""Directional tests of a stored Jacobian J (verifier dtsens, item 3):
 (i) discrete-derivative test: R(t) = |F(z + t v) - F(z) - t J v| for t = 1e-3, 1e-2, 1e-1 along given directions (quadratic in t
     if J is the derivative of the discrete F in a smooth region); F with the Jacobian's own dt;
 (ii) continuum-time test: d_h(v) = (F_h(z + e v) - F_h(z - e v))/(2e) at dt = 0.01, 0.005, 0.0025 (dt_near = dt, to exclude the
     step switch) for the same directions: successive differences should fall by 16 (fourth order) if the sensitivity is resolved.
Directions: a low-mode smooth perturbation (Chebyshev T_2(2q-1) cos(2s)), a node cardinal direction (far y-axis node), the
Newton direction -J^-1 F, and the softest right singular vectors (from a *_softvecs_*.pt file if given).
Usage: python3 src/dirtest.py runs/J_<tag>.pt tag [softvecs.pt] [Npsi=480]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    jpath, tag = sys.argv[1], sys.argv[2]; rest = sys.argv[3:]
    vfile = next((a_ for a_ in rest if a_.endswith('.pt')), None); nums = [a_ for a_ in rest if not a_.endswith('.pt')]
    Npsi = int(nums[0]) if nums else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = J.shape[0]; N, M = model.N, model.M; dtJ = float(D['dt'])
    b, cl, C = ch.unpack(z)
    Fh = lambda zz, dt, dtn: ch.F_fixed(zz, dt=dt, dt_near=dtn)
    F0 = Fh(z, dtJ, 4 * dtJ)
    dirs = {}
    qn = model.q_np[1:]; sn = model.ang.s_np
    smooth = np.outer(np.polynomial.chebyshev.chebval(2 * qn - 1, [0, 0, 1]) - 1.0, np.cos(2 * sn)).ravel()   # vanishes at q = 0 (origin row fixed)
    v = torch.zeros(n, device='cuda'); v[:N * M] = torch.tensor(smooth, device='cuda'); dirs['smooth_(T2-1)cos2'] = v / v.norm()
    r, _, _ = model.radii(float(cl)); thd = model.ang.theta_np * 180 / np.pi
    rr = r[1:][:, None] * np.ones((1, M)); tt = thd[None, :] * np.ones((N, 1))
    j = int(np.argmin((np.log(rr / 2e3) ** 2 + ((tt - 88) / 10) ** 2).ravel())); v = torch.zeros(n, device='cuda'); v[j] = 1.0; dirs['cardinal_far_yaxis'] = v
    dz = -torch.linalg.solve(J, F0); dirs['newton'] = dz / dz.norm()
    if vfile:
        S = torch.load(vfile); scale = torch.ones(n); scale[-2] = 1.0 / 400.0
        V = S['Vsoft_unscaled'] if 'Vsoft_unscaled' in S else S['Vsoft'] * scale[:, None]      # legacy Vsoft: c_l per 1/400
        for i in range(min(3, V.shape[1])):
            v = V[:, i].cuda(); dirs[f'soft{i}'] = v / v.norm()
    out = dict(tag=tag, jpath=jpath, dtJ=dtJ, F0=float(F0.norm()), newton_step_norm=float(dz.norm()), dirs={})
    for name, v in dirs.items():
        t0 = time.time(); res = dict(Jv_norm=float((J @ v).norm()))
        # (i)
        for t in (1e-3, 1e-2, 1e-1):
            R = Fh(z + t * v, dtJ, 4 * dtJ) - F0 - t * (J @ v); res[f'R_{t:g}'] = float(R.norm())
        # (ii)
        e = 1e-5 if name != 'cardinal_far_yaxis' else 1e-5
        d = {}
        for dt in (0.01, 0.005, 0.0025):
            d[dt] = (Fh(z + e * v, dt, dt) - Fh(z - e * v, dt, dt)) / (2 * e)
        res['d_norms'] = {str(k): float(x.norm()) for k, x in d.items()}
        res['diff_01_005'] = float((d[0.01] - d[0.005]).norm()); res['diff_005_0025'] = float((d[0.005] - d[0.0025]).norm())
        res['ratio'] = res['diff_01_005'] / max(res['diff_005_0025'], 1e-300)
        dJ = (Fh(z + e * v, dtJ, 4 * dtJ) - Fh(z - e * v, dtJ, 4 * dtJ)) / (2 * e)          # matched residual (the Jacobian's own dt, dt_near)
        res['Jv_vs_d_matched'] = float((J @ v - dJ).norm()); res['Jv_vs_d_dtJ'] = float((J @ v - d[dtJ]).norm()) if dtJ in d else None
        out['dirs'][name] = res
        print(f'{name}: |Jv| {res["Jv_norm"]:.3e}; remainder R(t) t=1e-3/1e-2/1e-1: {res["R_0.001"]:.2e} {res["R_0.01"]:.2e} {res["R_0.1"]:.2e}; '
              f'd_h: |d_.01 - d_.005| {res["diff_01_005"]:.2e}, |d_.005 - d_.0025| {res["diff_005_0025"]:.2e}, ratio {res["ratio"]:.1f}; |Jv - d_matched| {res["Jv_vs_d_matched"]:.2e} ({time.time()-t0:.0f}s)', flush=True)
    json.dump(out, open(f'{LANE}/runs/dirtest_{tag}.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
