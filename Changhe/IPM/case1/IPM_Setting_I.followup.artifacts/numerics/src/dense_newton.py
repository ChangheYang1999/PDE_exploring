"""Newton on the hybrid Psi-map residual with a stored dense Jacobian (src/jac_dense.py) and Broyden rank-one updates between
Jacobian evaluations; then the SVD of the Jacobian (SPEC S3 in the Psi formulation), the soft vectors, stagnation data and
B_3 (src/b3_axis.py).  The residual used for the iteration is the accurate one (charmap.F with dt = 0.005), the Jacobian is
the finite-difference one at dt = 0.01 (its columns are in the scaled coordinates: c_l column per 1/400).
Usage: python3 src/dense_newton.py runs/J_<tag>.pt outtag [maxit=12] [nsv=20]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, run_newton as rn

LANE = '.'


def main():
    jpath, tag = sys.argv[1], sys.argv[2]
    maxit = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    nsv = int(sys.argv[4]) if len(sys.argv) > 4 else 20
    Npsi_res = int(sys.argv[5]) if len(sys.argv) > 5 else 480     # fine radial grid for the Poisson modes in the residual
    log = open(f'{LANE}/runs/{tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    D = torch.load(jpath)
    model0, x, d = ipn.load_state(D['state']); b, cl = model0.unpack(x)
    # the residual uses the mixed-resolution inverse (modes on Npsi_res nodes): the coarse-inverse Jacobian is only approximate
    model = ipn.Model(model0.N, model0.M, model0.L, device='cuda', beta=model0.beta, nmodes=model0.nmodes, Mq=model0.Mq, Npsi=Npsi_res)
    if 'Npsi' in D and int(D['Npsi']) != model0.Npsi: model0 = ipn.Model(model0.N, model0.M, model0.L, device='cuda', beta=model0.beta, nmodes=model0.nmodes, Mq=model0.Mq, Npsi=int(D['Npsi']))
    ch = cm.Charac(model)
    J = D['J'].to(model.dev); scale = D['scale'].to(model.dev); z = D['z0'].to(model.dev); n = z.numel()
    N, M = model.N, model.M
    Fz = lambda zz: ch.F(zz, dt=0.01, dt_near=0.04, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)   # dt 0.01 = the Jacobian's dt (the research record 07:30Z)
    FzJ = lambda zz: ch.F_fixed(zz, dt=D['dt'], dt_near=4 * D['dt'])
    P(f'# dense_newton {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} J from {jpath} (coarse inverse Npsi = {model0.Npsi}): n = {n}; grid ({N},{M},{model.beta}) L = {model.L}; residual with Npsi = {Npsi_res}')
    # J holds derivatives with respect to the UNSCALED unknowns (jac_dense divides by eps*scale). Recompute the c_l and C
    # columns by central differences with proper increments (the one-sided c_l increment in jac_dense was eps/400 = 2.5e-8).
    for col, h in ((n - 2, 1e-5), (n - 1, 1e-3)):
        e = torch.zeros(n, device=model.dev); e[col] = h
        J[:, col] = (FzJ(z + e) - FzJ(z - e)) / (2 * h)
    P(f'   c_l column recomputed (central, h = 1e-5, accurate inverse): norm {J[:, n-2].norm().item():.3e}; C column (h = 1e-3): norm {J[:, n-1].norm().item():.3e}')
    # FD noise floor estimate: the step-size switch at |X - P| = 0.5 makes F non-smooth at the RK local-error level
    e = torch.zeros(n, device=model.dev); e[n // 2] = D['eps']
    col_fd2 = (FzJ(z + e) - FzJ(z - e)) / (2 * D['eps'])
    P(f'   FD check on one b-column: one-sided (stored) vs central differ by {(J[:, n // 2] - col_fd2).norm().item():.3e} (column norm {J[:, n // 2].norm().item():.3e})')
    Jcur = J.clone()
    Delta = 0.05
    F = Fz(z); nF = F.norm().item()
    hist = []
    for it in range(maxit):
        t0 = time.time()
        bb, cll, CC = ch.unpack(z)
        P(f'it {it}: |F|_2 {nF:.3e} |F|_inf {F.abs().max().item():.3e}  h(P)-1 {F[-2].item():+.3e} ident {F[-1].item():+.3e}  c_l {cll.item():.10f}  C {CC.item():.8f}')
        hist.append(dict(it=it, F2=nF, Finf=F.abs().max().item(), cl=cll.item(), C=CC.item(), hP1=F[-2].item(), ident=F[-1].item()))
        if nF < 1e-10: break
        # Levenberg-Marquardt step through the SVD of the current Jacobian: dz = -V diag(s/(s^2 + mu)) U^T F, mu such that
        # |dz|_inf <= Delta (trust radius, adaptive); the near-null directions (the c_l family) are thereby damped
        U_, S_, Vh_ = torch.linalg.svd(Jcur); gU = U_.T @ F
        def lmstep(mu): return -(Vh_.T @ (S_ / (S_ * S_ + mu) * gU))
        dz = lmstep(0.0)
        if dz.abs().max().item() > Delta:
            lo, hi = -30.0, 30.0
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if lmstep(10.0 ** mid).abs().max().item() > Delta: lo = mid
                else: hi = mid
            mu = 10.0 ** hi; dz = lmstep(mu)
        else:
            mu = 0.0
        lam = 1.0
        for _ in range(6):
            zn = z + lam * dz; Fn = Fz(zn); nFn = Fn.norm().item()
            if nFn < nF: break
            lam *= 0.5
        P(f'   LM: mu {mu:.2e} Delta {Delta:.2e} smallest s {S_[-3:].cpu().numpy()}')
        if nFn < nF and lam == 1.0: Delta = min(2 * Delta, 1.0)
        elif nFn >= nF: Delta = Delta / 4
        P(f'   |dz|_inf {dz.abs().max().item():.3e} dc_l {dz[-2].item():+.3e} dC {dz[-1].item():+.3e} lam {lam} |F| -> {nFn:.3e} ({time.time()-t0:.0f}s)')
        if nFn >= nF:
            if Delta < 1e-6: P('   trust radius collapsed; stop'); break
            P('   no decrease; trust radius reduced'); continue
        # Broyden good update: J <- J + (dF - J dz) dz^T / (dz^T dz), with dz the step actually taken (unscaled coordinates)
        dz_t = lam * dz; dF = Fn - F
        Jcur = Jcur + torch.outer(dF - Jcur @ dz_t, dz_t) / (dz_t @ dz_t)
        z, F, nF = zn, Fn, nFn
        bb, cll, CC = ch.unpack(z)
        ipn.save_state(f'{LANE}/runs/{tag}_it{it+1}.npz', model, model.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_dense', it=it + 1))
    bb, cll, CC = ch.unpack(z)
    ipn.save_state(f'{LANE}/runs/{tag}.npz', model, model.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_dense', F2=nF, Finf=F.abs().max().item()))
    # the Broyden-updated Jacobian (secant approximation at the final state) and the final accurate residual, for the follow-on
    # scripts (fixed-c_l continuation, S3 (g) test); its small singular values are not those of the exact Jacobian
    torch.save(dict(J=Jcur.cpu(), F=F.cpu(), z=z.cpu(), scale=scale.cpu(), state=f'{LANE}/runs/{tag}.npz', Npsi_res=Npsi_res, dt=0.01, eps=D['eps'], N=N, M=M, beta=model.beta, L=model.L, C=CC.item(), Npsi=int(D['Npsi']) if 'Npsi' in D else model0.Npsi), f'{LANE}/runs/J_{tag}_broyden.pt')
    P(f'saved runs/J_{tag}_broyden.pt (Broyden-updated Jacobian, final residual)')
    # diagnostics at the final state
    E, ident = model.residual(bb, cll); E = E.cpu().numpy(); r, w, v = model.radii(float(cll))
    rel = np.abs(E[1:]) * (1 - model.q_np[1:, None]) / np.abs(bb[1:].cpu().numpy())
    P(f'final: c_l = {cll.item():.10f} C = {CC.item():.8f} |F|_2 {nF:.3e}; collocation |R|/|rho| max {rel.max():.3e} (r<1: {rel[r[1:]<1].max():.2e}, 1-10: {rel[(r[1:]>=1)&(r[1:]<10)].max():.2e}, 10-100: {rel[(r[1:]>=10)&(r[1:]<100)].max():.2e}, >100: {rel[r[1:]>=100].max():.2e})')
    st = rn.stagnation(model, model.pack(bb, cll)); P(f'stagnation: {json.dumps(st)}')
    # stationarity measure (SPEC S3 (b)): |J^T F| / (|J| |F|) with the Broyden-updated Jacobian at the final state
    JtF = Jcur.T @ F; P(f'stationarity |J^T F|/(|J|_F |F|) = {(JtF.norm() / (Jcur.norm() * F.norm())).item():.3e}  (|J|_2 approx {torch.linalg.matrix_norm(Jcur, 2).item():.3e})')
    # SVD of the FD Jacobian at the INITIAL state (not the converged one), in scaled coordinates: J_s = J diag(scale), i.e. the
    # c_l column in units of 1/400 (stated); singular values below the FD noise floor (about 1e-4 per column) are unresolved.
    Js = J * scale[None, :]
    t0 = time.time(); S = torch.linalg.svdvals(Js).cpu().numpy()
    P(f'SVD of J at the initial state (FD, c_l column per 1/400) {time.time()-t0:.0f}s: smax {S[0]:.4e}; smallest {" ".join("%.3e" % s for s in S[-nsv:][::-1])}')
    counts = {t: int((S < t).sum()) for t in (1e-8, 1e-6, 1e-4, 1e-3, 1e-2)}
    P(f'   counts below thresholds {counts}')
    # softest right vectors (block inverse iteration) and their structure
    LU = torch.linalg.lu_factor(Js); V = torch.randn(n, 8, device=model.dev)
    for _ in range(40):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
    JV = Js @ V; Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False); Vk = V @ Wk.T; order = torch.argsort(sk)
    soft = []
    thd = model.ang.theta_np * 180 / np.pi; rr = r[1:]
    for i in order[:6]:
        vec = Vk[:, i]; vb = (scale * vec)[:N * M].reshape(N, M).cpu().numpy(); en = vb ** 2; tot = float((scale * vec).norm() ** 2)
        rad = {k_: float(en[m_].sum() / tot) for k_, m_ in [('r<1', rr < 1), ('1-10', (rr >= 1) & (rr < 10)), ('10-100', (rr >= 10) & (rr < 100)), ('>100', rr >= 100)]}
        ang = {k_: float(en[:, m_].sum() / tot) for k_, m_ in [('<10', thd < 10), ('10-80', (thd >= 10) & (thd < 80)), ('>80', thd >= 80)]}
        soft.append(dict(sigma=float(sk[i]), dcl=float(vec[-2] / 400), dC=float(vec[-1]), radial=rad, angular=ang))
        P(f'   soft: sigma {float(sk[i]):.3e} dc_l {float(vec[-2]/400):+.3e} dC {float(vec[-1]):+.3e} radial {rad} angular {ang}')
    torch.save(dict(Vsoft=Vk[:, order[:8]].cpu(), ssoft=sk[order[:8]].cpu()), f'{LANE}/runs/{tag}_softvecs.pt')
    json.dump(dict(hist=hist, c_l=cll.item(), C=CC.item(), F2=nF, stagnation=st, smax=float(S[0]), smallest=[float(s_) for s_ in S[-nsv:][::-1]],
                   counts=counts, soft=soft, colloc_rel_max=float(rel.max())), open(f'{LANE}/runs/{tag}_diag.json', 'w'), indent=1)
    # B_3 by the lead's tool on the final state
    try:
        import b3_axis
        out, _ = b3_axis.b3_of_state(model, model.pack(bb, cll), verbose=False)
        P(f'B_3 (lead tool, my axis data): orig {out["B3_orig"]:.4f} ibp {out["B3_ibp"]:.4f}; medians orig {out["median_orig"]:.4f} ibp {out["median_ibp"]:.4f} [{out["ibp_min"]:.3f}, {out["ibp_max"]:.3f}]; x* {out["xstar"]:.6f} g* {out["gstar"]:.5f}')
        json.dump(out, open(f'{LANE}/runs/b3_{tag}.json', 'w'), indent=1)
    except Exception as ex:
        P(f'B_3 failed: {ex}')
    P('done')


if __name__ == '__main__':
    main()
