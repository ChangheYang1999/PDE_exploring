"""Constrained LM-Newton on the hybrid Psi-map residual with a stored dense Jacobian (Broyden-updated between steps):
minimize |F(z)| over z subject to a linear constraint, either
   --cl VALUE          c_l frozen at VALUE (S4 (b) fixed-c_l continuation at the discrete level; the minimal residual against the
                       offset from the converged c_l is the nonlinear version of alpha_cl and the Q1 test along c_l), or
   --vec FILE IDX AMP  a prescribed amplitude AMP along the stored unit vector IDX of FILE (runs/*_softvecs.pt, key Vsoft, scaled
                       coordinates with c_l per 1/400, as saved by dense_newton / svd_report): v.(z - z_ref) = AMP.
The LM step is taken in the complement of the constrained direction (projector), trust region in |dz|_inf.
Reports per iteration |F|_2, |F|_inf, h(P) - 1, identity, c_l, C; at the end the row distribution of the residual, the
stagnation data, B_3 (lead's tool, both forms with medians), and saves runs/<tag>.npz (+ _hist.json).
Usage: python3 src/constrained_newton.py runs/J_<tag>.pt tag (--cl VALUE | --vec FILE IDX AMP) [--maxit 15] [--Delta 0.05] [--Npsi 480] [--z0 runs/state.npz]"""
import sys, os, time, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, run_newton as rn, jtools as jt

LANE = jt.LANE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('jpath'); ap.add_argument('tag')
    ap.add_argument('--cl', type=float, default=None); ap.add_argument('--vec', nargs=3, default=None)
    ap.add_argument('--maxit', type=int, default=15); ap.add_argument('--Delta', type=float, default=0.05); ap.add_argument('--Npsi', type=int, default=480)
    ap.add_argument('--z0', default=None, help='start state (npz with C); default: the Jacobian state')
    ap.add_argument('--tol', type=float, default=1e-3, help='stop when |F| decreases by less than this fraction in two consecutive steps')
    ap.add_argument('--free', action='store_true', help='no constraint (plain LM-Newton with the stored J), e.g. to re-solve with another dt')
    ap.add_argument('--scut', type=float, default=0.0, help='drop singular directions with s < scut (unscaled J units) from the step')
    ap.add_argument('--rebuild_cols', action='store_true', help='recompute the c_l and C columns centrally with the accurate residual first')
    ap.add_argument('--dt', type=float, default=None, help='override the residual orbit step dt (dt_near = 4 dt); default jtools.RES_KW')
    a = ap.parse_args()
    log = open(f'{LANE}/runs/{a.tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    J, zJ, model, ch, D = jt.load_J(a.jpath, a.Npsi); n = J.shape[0]; N, M = model.N, model.M
    z = zJ.clone()
    if a.z0 is not None:
        m0, x0, d0 = ipn.load_state(a.z0); b0, cl0 = m0.unpack(x0); z = ch.pack(b0, cl0, float(d0['C']))
    kw = dict(jt.RES_KW)
    if a.dt is not None: kw['dt'] = a.dt; kw['dt_near'] = 4 * a.dt
    Fz = lambda zz: ch.F(zz, **kw)
    scale = torch.ones(n, device='cuda'); scale[-2] = 1.0 / 400.0
    # constraint direction u (unit, unscaled coordinates) and the projector Pc = I - u u^T
    if a.free:
        u = torch.zeros(n, device='cuda'); cons = f'none (free LM-Newton, dt {kw["dt"]})'
    elif a.cl is not None:
        u = torch.zeros(n, device='cuda'); u[-2] = 1.0; z[-2] = a.cl; cons = f'c_l = {a.cl:.10f}'
    else:
        S = torch.load(a.vec[0]); idx = int(a.vec[1]); amp = float(a.vec[2])
        u = S['Vsoft_unscaled'][:, idx].cuda() if 'Vsoft_unscaled' in S else (scale * S['Vsoft'][:, idx].cuda())
        u = u / u.norm(); z = z + amp * u; cons = f'v{idx} of {a.vec[0]} amplitude {amp}'
    Pc = torch.eye(n, device='cuda') - torch.outer(u, u)
    P(f'# constrained_newton {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} J {a.jpath} (n {n}); constraint {cons}; grid ({N},{M},{model.beta}) L {model.L} Npsi {a.Npsi} residual {kw}')
    if a.rebuild_cols:
        FJ = lambda zz: ch.F_fixed(zz, dt=kw['dt'], dt_near=kw['dt_near'])
        for col, h in ((n - 2, 1e-5), (n - 1, 1e-3)):
            e = torch.zeros(n, device='cuda'); e[col] = h; J[:, col] = (FJ(z + e) - FJ(z - e)) / (2 * h)
        P(f'   c_l and C columns recomputed centrally: norms {J[:, n-2].norm().item():.3e}, {J[:, n-1].norm().item():.3e}')
    Jcur = J.clone(); Delta = a.Delta
    F = Fz(z); nF = F.norm().item(); hist = []; nprev = [nF]
    for it in range(a.maxit):
        t0 = time.time(); bb, cll, CC = ch.unpack(z)
        P(f'it {it}: |F|_2 {nF:.4e} |F|_inf {F.abs().max().item():.3e} h(P)-1 {F[-2].item():+.3e} ident {F[-1].item():+.3e} c_l {cll.item():.10f} C {CC.item():.8f}')
        hist.append(dict(it=it, F2=nF, Finf=F.abs().max().item(), cl=cll.item(), C=CC.item(), hP1=F[-2].item(), ident=F[-1].item()))
        if nF < 1e-10: break
        if len(nprev) >= 3 and nprev[-3] - nF < a.tol * nprev[-3]: P('   stalled (relative decrease below tol over two steps); stop'); break
        info = {}; dz, mu, S_ = jt.lm_step(Jcur, F, Delta, Pc=Pc, s_cut=a.scut, info=info)
        lam = 1.0
        for _ in range(6):
            zn = z + lam * dz; Fn = Fz(zn); nFn = Fn.norm().item()
            if nFn < nF: break
            lam *= 0.5
        P(f'   LM mu {mu:.2e} Delta {Delta:.2e} |dz|_inf {dz.abs().max().item():.3e} dc_l {dz[-2].item():+.2e} dC {dz[-1].item():+.3e} lam {lam} |F| -> {nFn:.4e} (predicted {info["predicted_F"]:.3e}; dropped {info["n_dropped"]} dirs carrying |F| {info["F_in_dropped"]:.3e}; smallest kept s {S_[S_ > max(a.scut, 1e-14 * S_[0].item())][-1].item() if (S_ > max(a.scut, 1e-14 * S_[0].item())).any() else float("nan"):.2e}) ({time.time()-t0:.0f}s)')
        if nFn < nF and lam == 1.0: Delta = min(2 * Delta, 1.0)
        elif nFn >= nF: Delta = Delta / 4
        if nFn >= nF:
            if Delta < 1e-6: P('   trust radius collapsed; stop'); break
            continue
        dz_t = lam * dz; dF = Fn - F
        Jcur = Jcur + torch.outer(dF - Jcur @ dz_t, dz_t) / (dz_t @ dz_t)
        z, F, nF = zn, Fn, nFn; nprev.append(nF)
    bb, cll, CC = ch.unpack(z)
    # residual distribution over row groups
    Fb = F[3 * M:n - 2].reshape(N - 3, M).abs().cpu().numpy(); r, _, _ = model.radii(float(cll)); rr = r[4:]
    dist = dict(inner_coll_rows_max=float(F[:3 * M].abs().max()), hP=float(F[-2]), ident=float(F[-1]),
                psi_rows_max={k_: float(Fb[s_].max()) if s_.any() else None for k_, s_ in [('r<1', rr < 1), ('1-10', (rr >= 1) & (rr < 10)), ('10-100', (rr >= 10) & (rr < 100)), ('>100', rr >= 100)]})
    st = rn.stagnation(model, model.pack(bb, cll))
    # stationarity of the constrained least-squares problem: A^T F with A = Jcur Pc (the constrained direction removed), Broyden J
    A_ = Jcur @ Pc; AtF = A_.T @ F; stat = float(AtF.norm() / (A_.norm() * F.norm()))
    # removable residual in the linear model: |Q^T F| with Q an orthonormal basis of the numerically resolved range of A (rank threshold 1e-10 smax)
    Ua, Sa, _ = torch.linalg.svd(A_); rk = int((Sa > 1e-10 * Sa[0]).sum()); QtF = float((Ua[:, :rk].T @ F).norm())
    P(f'stationarity (A = J_broyden P_c): |A^T F|/(|A|_F |F|) {stat:.3e}; removable |Q^T F| {QtF:.3e} of |F| {nF:.3e} (rank {rk} of {n})')
    out = dict(tag=a.tag, constraint=cons, F2=nF, Finf=float(F.abs().max()), c_l=cll.item(), C=CC.item(), hist=hist, residual_rows=dist, stagnation=st, stationarity_AtF=stat, removable_QtF=QtF, rank=rk)
    P(f'final: |F|_2 {nF:.4e} |F|_inf {out["Finf"]:.3e} c_l {cll.item():.10f} C {CC.item():.8f}; rows {json.dumps(dist)}; stagnation {json.dumps(st)}')
    ipn.save_state(f'{LANE}/runs/{a.tag}.npz', model, model.pack(bb, cll), extra=dict(tag=a.tag, C=CC.item(), formulation='psi_hybrid_constrained', constraint=cons, F2=nF))
    try:
        import b3_axis
        o, _ = b3_axis.b3_of_state(model, model.pack(bb, cll), verbose=False); out['B3'] = o
        P(f'B_3: orig {o["B3_orig"]:.4f} ibp {o["B3_ibp"]:.4f}; medians orig {o["median_orig"]:.4f} [{o["orig_min"]:.3f},{o["orig_max"]:.3f}] ibp {o["median_ibp"]:.4f} [{o["ibp_min"]:.3f},{o["ibp_max"]:.3f}]; x* {o["xstar"]:.6f} g* {o["gstar"]:.5f}')
    except Exception as ex:
        P(f'B_3 failed: {ex}')
    json.dump(out, open(f'{LANE}/runs/{a.tag}_hist.json', 'w'), indent=1); P('done')


if __name__ == '__main__':
    main()
