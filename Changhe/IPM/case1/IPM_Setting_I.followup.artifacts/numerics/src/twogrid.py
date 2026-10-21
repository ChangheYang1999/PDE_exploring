"""Two-grid preconditioned Newton-Krylov for the hybrid Psi-map residual on a fine grid, using the dense Jacobian of the
same system on a coarse grid (src/jac_dense.py) as the preconditioner: M^-1 = Pro J_c^-1 Res, with Res the evaluation of the
fine interpolant at the coarse nodes and Pro the evaluation of the coarse interpolant at the fine nodes (b-components; c_l and
C components copied; all in the scaled coordinates with the c_l column per 1/400).  GMRES on M^-1 J_f (left preconditioning),
matvecs by central finite differences of the fine residual.
Usage: python3 src/twogrid.py runs/J_<coarse>.pt runs/coarse_state.npz N M beta L tag [maxit=8] [gmres=30] [Npsi=480]
The fine state is the projection of the coarse state (ipm_newton.project_state)."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, run_newton as rn

LANE = '.'


def interp_ops(mc, mf, cl):
    """Res: fine b-values (Nf*Mf) -> coarse b-values (Nc*Mc); Pro: coarse -> fine.  Node sets: i >= 1 (q = 0 excluded).
    Built from the 1-D barycentric matrices in q (same q nodes for equal L; for different L the radii are matched) and the
    cos(2 m s) interpolation in the mapped angle."""
    def op(m_from, m_to):
        r_to, _, _ = m_to.radii(cl)
        q_in_from = m_from.q_of_r(np.minimum(r_to, 1e300), cl); q_in_from[-1] = 1.0
        Pq = ipn.interp_matrix(m_from.q_np, q_in_from, m_from.wq_np)                 # (Nto+1, Nfrom+1)
        s_to = m_from.ang.s_of_theta(m_to.ang.theta_np)
        mm = np.arange(m_from.M)
        Sa = np.cos(np.outer(s_to, 2 * mm)) @ m_from.ang.A['EE'].cpu().numpy()      # (Mto, Mfrom): values -> values
        # far-field amplitude factor for different L: b_to = b_from * w_from / w_to
        k = 1.0 / cl
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio = ((1.0 + (r_to / m_from.L) ** 2) / (1.0 + (r_to / m_to.L) ** 2)) ** ((k - 3.0) / 2.0)
        ratio[-1] = (m_to.L / m_from.L) ** (k - 3.0)
        Pq = Pq * ratio[:, None]
        # drop row/col of q = 0 (b = 1 fixed): the perturbation at q = 0 is zero
        Pq1 = Pq[1:, 1:]
        return torch.tensor(np.kron(Pq1, Sa), device=m_to.dev)                        # (Nto*Mto, Nfrom*Mfrom)
    return op(mf, mc), op(mc, mf)


def main():
    jpath, cstate = sys.argv[1], sys.argv[2]
    Nf, Mf, beta, L = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]); tag = sys.argv[7]
    maxit = int(sys.argv[8]) if len(sys.argv) > 8 else 8; mg = int(sys.argv[9]) if len(sys.argv) > 9 else 30
    Npsi = int(sys.argv[10]) if len(sys.argv) > 10 else 480
    log = open(f'{LANE}/runs/{tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    D = torch.load(jpath); Jc = D['J'].cuda()          # derivatives with respect to the unscaled unknowns
    mc, xc, dc = ipn.load_state(cstate); C0 = float(dc['C'])
    mf = ipn.Model(Nf, Mf, L, device='cuda', beta=beta, Npsi=Npsi)
    xf = ipn.project_state(mc, xc, mf); bf, clf = mf.unpack(xf)
    ch = cm.Charac(mf); z = ch.pack(bf, clf, C0); n = z.numel(); nc = Jc.shape[0]
    Res_b, Pro_b = interp_ops(mc, mf, float(clf))
    P(f'# twogrid {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}: fine ({Nf},{Mf},{beta}) L={L} n={n}; coarse J from {jpath} (n_c={nc})')
    LUc = torch.linalg.lu_factor(Jc)
    def Res(v):   # fine residual-space vector -> coarse (rows: b rows then h(P), identity)
        return torch.cat([Res_b @ v[:n - 2], v[n - 2:]])
    def Pro(y):   # coarse step (unscaled coordinates) -> fine step
        return torch.cat([Pro_b @ y[:nc - 2], y[nc - 2:]])
    def Minv(v):
        return Pro(torch.linalg.lu_solve(*LUc, Res(v)[:, None])[:, 0])
    Fz = lambda zz: ch.F(zz, dt=0.005, dt_near=0.02, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)
    FzJ = lambda zz: ch.F(zz, dt=0.01, dt_near=0.04, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)
    F = Fz(z); nF = F.norm().item()
    for it in range(maxit):
        t0 = time.time(); bb, cll, CC = ch.unpack(z)
        P(f'it {it}: |F|_2 {nF:.3e} |F|_inf {F.abs().max().item():.3e} h(P)-1 {F[-2].item():+.3e} ident {F[-1].item():+.3e} c_l {cll.item():.10f} C {CC.item():.8f}')
        if nF < 1e-10: break
        def Aop(v):
            e = 1e-4 / v.norm().item()
            return Minv((FzJ(z + e * v) - FzJ(z - e * v)) / (2 * e))
        rhs = Minv(-F)
        # GMRES from run_psi_newton
        import run_psi_newton as rpn
        dz, rh, rv = rpn.gmres(Aop, rhs, m=mg, tol=1e-3, P=P)
        lam = 1.0
        for _ in range(6):
            zn = z + lam * dz; Fn = Fz(zn); nFn = Fn.norm().item()
            if nFn < nF: break
            lam *= 0.5
        P(f'   gmres its {len(rh)-1} rel res {rh[-1]/rh[0]:.2e}; |dz|_inf {dz.abs().max().item():.3e} dc_l {dz[-2].item():+.3e} dC {dz[-1].item():+.3e} lam {lam} |F| -> {nFn:.3e} ({time.time()-t0:.0f}s)')
        if nFn >= nF: P('   no decrease; stop'); break
        z, F, nF = zn, Fn, nFn
        bb, cll, CC = ch.unpack(z)
        ipn.save_state(f'{LANE}/runs/{tag}_it{it+1}.npz', mf, mf.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_twogrid', it=it + 1))
    bb, cll, CC = ch.unpack(z)
    ipn.save_state(f'{LANE}/runs/{tag}.npz', mf, mf.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_twogrid'))
    st = rn.stagnation(mf, mf.pack(bb, cll)); P(f'stagnation: {json.dumps(st)}'); P('done')


if __name__ == '__main__':
    main()
