"""Smoothness probe of the discrete residual. The orbit integrator switches the step from dt to dt_near where the orbit is
within r_near of P, so F(z) is piecewise smooth in z (an orbit crossing the switch radius at a different step changes its
quadrature error by O(dt_near^5)). This probe measures the central difference d(s) = (F(z + s v) - F(z - s v))/(2 s) along given
directions for s = 1e-5 .. 1e-2 with (A) the discrete system jtools.RES_KW (ch.F, dt 0.01 / dt_near 0.04), (B) ch.F_fixed with the
same steps, (C) ch.F_fixed with dt_near = dt (no switch).  A smooth F gives |d(s) - d(s/10)| proportional to s^2 (cubic term);
switching noise of size eta gives differences growing like eta/s as s -> 0.  Also reports |F_A - F_B|, |F_A - F_C| at z.
Usage: python3 src/noise_probe.py runs/state.npz runs/softvecs.pt tag [Npsi=480] [ndirs=2]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    spath, vfile, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    Npsi = int(sys.argv[4]) if len(sys.argv) > 4 else 480; ndirs = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    m0, x0, d0 = ipn.load_state(spath); b0, cl = m0.unpack(x0); cl = float(cl); C = float(d0['C'])
    model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi); ch = cm.Charac(model)
    z = ch.pack(b0, cl, C); n = z.shape[0]; N, M = model.N, model.M
    # explicit schedule selection (the module default cm.TAU_SWITCH changed to 7.5 at 12:50Z; A and B are the OLD position switch)
    def FA(zz):
        cm.TAU_SWITCH = None; r = ch.F(zz, **jt.RES_KW); cm.TAU_SWITCH = 7.5; return r
    def FB(zz):
        cm.TAU_SWITCH = None; r = ch.F_fixed(zz, dt=jt.RES_KW['dt'], dt_near=jt.RES_KW['dt_near']); cm.TAU_SWITCH = 7.5; return r
    def FC(zz):
        cm.TAU_SWITCH = None; r = ch.F_fixed(zz, dt=jt.RES_KW['dt'], dt_near=jt.RES_KW['dt']); cm.TAU_SWITCH = 7.5; return r
    t0 = time.time(); A0, B0, C0 = FA(z), FB(z), FC(z)
    out = dict(tag=tag, state=spath, FA=float(A0.norm()), FB=float(B0.norm()), FC=float(C0.norm()), AB=float((A0 - B0).norm()), AC=float((A0 - C0).norm()), AC_inf=float((A0 - C0).abs().max()), dirs={})
    print(f'{tag}: |F_A| {out["FA"]:.4e} |F_B| {out["FB"]:.4e} |F_C| {out["FC"]:.4e}; |A - B| {out["AB"]:.2e} |A - C| {out["AC"]:.2e} (max {out["AC_inf"]:.2e}) ({time.time()-t0:.0f}s)', flush=True)
    S = torch.load(vfile); V = S['Vsoft_unscaled'].cuda().double()
    dirs = {f'soft{i}': V[:, i] / V[:, i].norm() for i in range(ndirs)}
    qn = model.q_np[1:]; sn = model.ang.s_np
    sm = np.outer(np.polynomial.chebyshev.chebval(2 * qn - 1, [0, 0, 1]) - 1.0, np.cos(2 * sn)).ravel()
    v = torch.zeros(n, device='cuda', dtype=torch.float64); v[:N * M] = torch.tensor(sm, device='cuda'); dirs['smooth'] = v / v.norm()
    ss = [1e-5, 1e-4, 1e-3, 1e-2]
    for name, v in dirs.items():
        res = {}
        for lab, Fn in (('A', FA), ('C', FC)):
            prev = None; row = []
            for s in ss:
                t0 = time.time(); d = (Fn(z + s * v) - Fn(z - s * v)) / (2 * s)
                e = dict(s=s, d=float(d.norm()), diff_prev=(float((d - prev).norm()) if prev is not None else None))
                # distribution of the change: how many rows carry the difference
                if prev is not None:
                    dd = (d - prev).abs(); e['diff_rows_above_1e-5'] = int((dd > 1e-5).sum()); e['diff_max'] = float(dd.max())
                row.append(e); prev = d
                print(f'  {name} F_{lab} s {s:g}: |d| {e["d"]:.4e}' + (f'  |d - d_prev| {e["diff_prev"]:.2e} (max row {e["diff_max"]:.1e}, rows > 1e-5: {e["diff_rows_above_1e-5"]})' if e['diff_prev'] is not None else '') + f' ({time.time()-t0:.0f}s)', flush=True)
            res[lab] = row
        out['dirs'][name] = res
    json.dump(out, open(f'{LANE}/runs/noise_{tag}.json', 'w'), indent=1); print(f'saved runs/noise_{tag}.json', flush=True)


if __name__ == '__main__':
    main()
