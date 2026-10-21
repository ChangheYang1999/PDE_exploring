"""Newton-Krylov on the Psi-map formulation (src/charmap.py): unknowns (b, c_l, C), residual
   [b - C eta_P[W]/(r^2 w cos^2) at the nodes with r < inf ; Ehat at q = 1 ; h(P) - 1 ; 3 c_l - 1 - psi_xy(0)].
Matrix-free GMRES with forward-mode JVPs (torch.func.jvp), inexact Newton with backtracking.
Usage:
  python3 src/run_psi_newton.py --N 120 --M 48 --beta 0.9 --L 8 --seed x3 --tag psi_n120m48 [--maxit 8] [--gmres 40] [--gtol 1e-3]
  --seed can be 'x3' or a saved state (collocation runs/*.npz or a psi state with 'C').
Outputs runs/<tag>.npz (b, c_l, C, grid), runs/<tag>.log, runs/<tag>_diag.json.
"""
import sys, os, time, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch
import ipm_newton as ipn, charmap as cm, run_newton as rn

LANE = '.'


def gmres(Aop, rhs, m=40, tol=1e-3, x0=None, P=print):
    """Right-preconditioner-free GMRES(m), one cycle (restart handled by caller).  Aop: v -> A v."""
    n = rhs.numel(); dev = rhs.device
    x = torch.zeros_like(rhs) if x0 is None else x0.clone()
    r = rhs - Aop(x) if x0 is not None else rhs.clone()
    beta = r.norm().item()
    V = torch.zeros(m + 1, n, device=dev, dtype=rhs.dtype); H = torch.zeros(m + 1, m, device=dev, dtype=rhs.dtype)
    V[0] = r / beta
    res_hist = [beta]
    for j in range(m):
        t0 = time.time()
        w = Aop(V[j])
        for i in range(j + 1):                       # modified Gram-Schmidt
            H[i, j] = torch.dot(w, V[i]); w = w - H[i, j] * V[i]
        for i in range(j + 1):                       # reorthogonalize once
            c = torch.dot(w, V[i]); H[i, j] += c; w = w - c * V[i]
        H[j + 1, j] = w.norm()
        if H[j + 1, j].item() > 1e-300: V[j + 1] = w / H[j + 1, j]
        e1 = torch.zeros(j + 2, device=dev, dtype=rhs.dtype); e1[0] = beta
        y = torch.linalg.lstsq(H[:j + 2, :j + 1], e1[:, None]).solution[:, 0]
        res = (H[:j + 2, :j + 1] @ y - e1).norm().item()
        res_hist.append(res)
        P(f'      gmres {j+1}: rel res {res/beta:.3e} ({time.time()-t0:.1f}s)')
        if res / beta < tol or H[j + 1, j].item() <= 1e-300:
            break
    x = x + V[:j + 1].T @ y
    # Ritz pairs of the Arnoldi Hessenberg (approximate eigenpairs of A on the Krylov space)
    ritz_vecs = []
    try:
        Hm = H[:j + 1, :j + 1]
        ev, ew = torch.linalg.eig(Hm)
        order = torch.argsort(ev.abs())
        ritz = ev[order].cpu().numpy()
        P('      ritz (smallest |.|): ' + ' '.join('%.3e%+.1ej' % (v.real, v.imag) for v in ritz[:8]) + '  largest |.| %.3e' % np.abs(ritz[-1]))
        for kk in range(min(4, len(order))):
            vec = (V[:j + 1].T @ ew[:, order[kk]].real); vec = vec / vec.norm()
            ritz_vecs.append((complex(ritz[kk]), vec))
    except Exception as ex:
        P(f'      ritz failed: {ex}')
    return x, res_hist, ritz_vecs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, required=True); ap.add_argument('--M', type=int, required=True)
    ap.add_argument('--L', type=float, default=8.0); ap.add_argument('--beta', type=float, default=0.9); ap.add_argument('--nmodes', type=int, default=None)
    ap.add_argument('--seed', default='x3'); ap.add_argument('--tag', required=True)
    ap.add_argument('--maxit', type=int, default=8); ap.add_argument('--gmres', type=int, default=40); ap.add_argument('--gtol', type=float, default=1e-3)
    ap.add_argument('--dt', type=float, default=0.005); ap.add_argument('--dt_near', type=float, default=0.02); ap.add_argument('--tau_max', type=float, default=14.0)
    ap.add_argument('--cl', type=float, default=None); ap.add_argument('--jvp', default='fd'); ap.add_argument('--eps', type=float, default=1e-4)
    ap.add_argument('--dt_jac', type=float, default=None, help='coarser dt for the GMRES matvecs (dt_near scaled by the same factor)')
    ap.add_argument('--far_psi', action='store_true', help='Psi rows also at q = 1 (placed at r_far) instead of the collocation rows there'); ap.add_argument('--r_far', type=float, default=1e10); ap.add_argument('--n_coll', type=int, default=0, help='innermost radial nodes with collocation rows (hybrid)'); ap.add_argument('--coll_scale', type=float, default=1.0, help='row scaling of the hybrid collocation rows')
    ap.add_argument('--soft_cut', type=float, default=1e-3, help='Ritz values below this are treated as soft directions (deflated + 1D search)'); ap.add_argument('--soft_step', type=float, default=0.02)
    ap.add_argument('--elim_cl', action='store_true', help='eliminate c_l through the identity (unknowns b, C; rows psi, q=1, h(P)-1)')
    ap.add_argument('--scl', type=float, default=1.0, help='column scaling of the c_l unknown (GMRES solves J D y = -F, D = diag(1,..,1/scl,1))')
    a = ap.parse_args()
    log = open(f'{LANE}/runs/{a.tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    P(f'# run_psi_newton {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} args {vars(a)}')
    t00 = time.time()
    model = ipn.Model(a.N, a.M, a.L, device='cuda', beta=a.beta, nmodes=a.nmodes)
    C0 = None
    if a.seed == 'x3':
        x = rn.seed_from_x3(model, cl=a.cl)
    else:
        m0, x0, d0 = ipn.load_state(a.seed)
        x = ipn.project_state(m0, x0, model)
        if a.cl is not None: x[-1] = a.cl
        if 'C' in d0.files: C0 = float(d0['C'])
    b, cl = model.unpack(x)
    r, w_, v_ = model.radii(float(cl))
    ch = cm.Charac(model)
    if C0 is None:
        st = ch.prepare(b, cl); xstar, hP, wpP, hpP = ch.find_P(st)
        k = 1.0 / float(cl)
        C0 = float(xstar) ** 2 * (1 + (float(xstar) / a.L) ** 2) ** ((k - 3) / 2) * model.eval_EE(b, model.q_of_r(np.array([float(xstar)]), float(cl)), np.array([0.0]))[0]
    if a.elim_cl:
        z = ch.pack2(b, C0); cl_cur = torch.as_tensor(float(cl), device=model.dev)
    else:
        z = ch.pack(b, cl, C0)
    n = z.numel()
    P(f'grid N={a.N} M={a.M} L={a.L} beta={a.beta} nmodes={model.nmodes}: n = {n}; seed {a.seed}; C0 = {C0:.8f}; elim_cl {a.elim_cl}; setup {time.time()-t00:.1f}s')
    if a.elim_cl:
        state = dict(cl=cl_cur)
        def Fz(zz):
            r_, cl_ = ch.F2(zz, state['cl'], dt=a.dt, dt_near=a.dt_near, tau_max=a.tau_max); return r_
        def FzJ(zz):
            if a.dt_jac is None: return Fz(zz)
            fac = a.dt_jac / a.dt
            r_, cl_ = ch.F2(zz, state['cl'], dt=a.dt_jac, dt_near=a.dt_near * fac, tau_max=a.tau_max); return r_
        def current_cl(zz):
            bb, _ = ch.unpack2(zz); return ch.cl_of_b(bb, state['cl'])
    else:
        Fz = lambda zz: ch.F(zz, dt=a.dt, dt_near=a.dt_near, tau_max=a.tau_max, far_psi=a.far_psi, r_far=a.r_far, n_coll=a.n_coll, coll_scale=a.coll_scale)
        if a.dt_jac is not None:
            fac = a.dt_jac / a.dt
            FzJ = lambda zz: ch.F(zz, dt=a.dt_jac, dt_near=a.dt_near * fac, tau_max=a.tau_max, far_psi=a.far_psi, r_far=a.r_far, n_coll=a.n_coll, coll_scale=a.coll_scale)
        else:
            FzJ = Fz
    hist = []
    F = Fz(z); nF = F.norm().item()
    npsi = a.N * a.M if a.far_psi else (a.N - 1) * a.M
    for it in range(a.maxit):
        t0 = time.time()
        if a.elim_cl:
            b, C = ch.unpack2(z); cl = current_cl(z); state['cl'] = cl.detach()
            P(f'nk it {it}: |F|_2 {nF:.3e} |F|_inf {F.abs().max().item():.3e}  [psi rows {F[:npsi].abs().max().item():.2e}, q=1 rows {F[npsi:-1].abs().max().item():.2e}, h(P)-1 {F[-1].item():+.3e}]  c_l {cl.item():.10f}  C {C.item():.8f}')
            hist.append(dict(it=it, F2=nF, Finf=F.abs().max().item(), hP1=F[-1].item(), cl=cl.item(), C=C.item()))
        else:
            b, cl, C = ch.unpack(z)
            q1txt = f'q=1 rows {F[npsi:-2].abs().max().item():.2e}, ' if not a.far_psi else ''
            P(f'nk it {it}: |F|_2 {nF:.3e} |F|_inf {F.abs().max().item():.3e}  [psi rows {F[:npsi].abs().max().item():.2e}, {q1txt}h(P)-1 {F[-2].item():+.3e}, ident {F[-1].item():+.3e}]  c_l {cl.item():.10f}  C {C.item():.8f}')
            hist.append(dict(it=it, F2=nF, Finf=F.abs().max().item(), hP1=F[-2].item(), ident=F[-1].item(), cl=cl.item(), C=C.item()))
        if F.abs().max().item() < 1e-11: break
        Dsc = torch.ones_like(z)
        if not a.elim_cl: Dsc[-2] = 1.0 / a.scl
        if a.jvp == 'ad':
            Aop = lambda v: torch.func.jvp(FzJ, (z,), (Dsc * v,))[1]
        else:
            def Aop(v):
                vv = Dsc * v; nv = vv.norm().item(); e = a.eps / nv
                return (FzJ(z + e * vv) - FzJ(z - e * vv)) / (2 * e)
        dy, rh, rv = gmres(Aop, -F, m=a.gmres, tol=a.gtol, P=P)
        # soft directions: Ritz values below soft_cut (relative to the largest Ritz value) are removed from the step and
        # handled by a one-dimensional search (the step along them is otherwise dominated by the nonlinearity)
        soft_dirs = []
        for (theta, vec) in rv:
            if abs(theta) < a.soft_cut:
                soft_dirs.append(vec)
        dy_c = dy.clone()
        for vec in soft_dirs:
            dy_c = dy_c - (vec @ dy_c) * vec
        if soft_dirs:
            P(f'   {len(soft_dirs)} soft Ritz direction(s) deflated from the step: |dy| {dy.norm().item():.3e} -> {dy_c.norm().item():.3e}; '
              + '; '.join(f'theta {abs(th):.2e}, dc_l comp {v[-2].item()/a.scl:+.3e}, dC comp {v[-1].item():+.3e}' for th, v in rv[:len(soft_dirs)]))
            for kk, vec in enumerate(soft_dirs):
                vb = (Dsc * vec)[:a.N * a.M].reshape(a.N, a.M).cpu().numpy(); en = vb ** 2; tot = float((Dsc * vec).norm() ** 2)
                rr_ = r[1:]; thd_ = model.ang.theta_np * 180 / np.pi
                rad = {k_: float(en[m_].sum() / tot) for k_, m_ in [('r<1', rr_ < 1), ('1-10', (rr_ >= 1) & (rr_ < 10)), ('10-100', (rr_ >= 10) & (rr_ < 100)), ('>100', rr_ >= 100)]}
                ang = {k_: float(en[:, m_].sum() / tot) for k_, m_ in [('<10deg', thd_ < 10), ('10-80', (thd_ >= 10) & (thd_ < 80)), ('>80', thd_ >= 80)]}
                i1 = int(np.argmax(np.abs(vb).max(1)))
                P(f'      soft vec {kk}: radial energy {rad}; angular {ang}; max |v_b| {np.abs(vb).max():.3f} at r = {rr_[i1]:.3g}')
                torch.save(dict(v_soft=vec.cpu(), theta=abs(rv[kk][0]), it=it, Dsc=Dsc.cpu()), f'{LANE}/runs/{a.tag}_softvec_it{it}_{kk}.pt')
        dz = Dsc * dy_c
        lam = 1.0
        for _ in range(6):
            zn = z + lam * dz; Fn = Fz(zn); nFn = Fn.norm().item()
            if nFn < nF: break
            lam *= 0.5
        if soft_dirs and nFn < nF:
            # 1D search along the softest direction (scaled coordinates): parabola through s = -h, 0, h in |F|^2
            vs = Dsc * soft_dirs[0]; vs = vs / vs.norm()
            hstep = a.soft_step
            f0 = nFn ** 2; fp = Fz(zn + hstep * vs).norm().item() ** 2; fm = Fz(zn - hstep * vs).norm().item() ** 2
            curv = (fp - 2 * f0 + fm) / hstep ** 2; slope = (fp - fm) / (2 * hstep)
            s_opt = -slope / curv if curv > 0 else 0.0
            s_opt = max(-4 * hstep, min(4 * hstep, s_opt))
            Ft = Fz(zn + s_opt * vs); nFt = Ft.norm().item()
            P(f'   soft 1D search: |F|^2 at s = -h, 0, +h (h = {hstep}): {fm:.4e} {f0:.4e} {fp:.4e}; curvature {curv:.3e} slope {slope:+.3e}; s_opt {s_opt:+.3e}; |F|_2 -> {nFt:.3e}; dc_l along v {vs[-2].item()*s_opt:+.3e}')
            if nFt < nFn:
                zn, Fn, nFn = zn + s_opt * vs, Ft, nFt
            torch.save(dict(v_soft=soft_dirs[0].cpu(), theta=abs(rv[0][0]), curvature=curv, slope=slope, s_opt=s_opt, it=it), f'{LANE}/runs/{a.tag}_soft_it{it}.pt')
        dcl_txt = f'dC {dz[-1].item():+.3e}' if a.elim_cl else f'dc_l {dz[-2].item():+.3e} dC {dz[-1].item():+.3e}'
        P(f'   step: gmres its {len(rh)-1}, final rel res {rh[-1]/rh[0]:.2e}; |dz|_inf {dz.abs().max().item():.3e} {dcl_txt}; lam {lam}; |F|_2 {nF:.3e} -> {nFn:.3e}  ({time.time()-t0:.1f}s)')
        if nFn >= nF:
            P('   no decrease; stop'); break
        z, F, nF = zn, Fn, nFn
        if a.elim_cl:
            bb_, C_ = ch.unpack2(z); cl_ = current_cl(z)
        else:
            bb_, cl_, C_ = ch.unpack(z)
        ipn.save_state(f'{LANE}/runs/{a.tag}_it{it+1}.npz', model, model.pack(bb_, cl_), extra=dict(tag=a.tag, C=C_.item(), formulation='psi', it=it + 1))
    if a.elim_cl:
        b, C = ch.unpack2(z); cl = current_cl(z)
    else:
        b, cl, C = ch.unpack(z)
    # diagnostics: collocation residual of the Psi solution, stagnation data
    E, ident = model.residual(b, cl)
    E = E.cpu().numpy(); r, w, v = model.radii(float(cl))
    rel = np.abs(E[1:]) * (1 - model.q_np[1:, None]) / np.abs(b[1:].cpu().numpy())
    P(f'final: c_l = {cl.item():.10f}  C = {C.item():.8f}  identity {ident.item():.3e}  collocation |Ehat|_inf (r<inf) {np.abs(E[1:-1]).max():.3e}  |R|/|rho| max {rel.max():.3e}')
    for lo, hi in [(0, 1), (1, 5), (5, 10), (10, 100), (100, 1e4), (1e4, 1e300)]:
        s_ = (r[1:] >= lo) & (r[1:] < hi)
        if s_.any(): P(f'   collocation |R|/|rho| in [{lo:g},{hi:g}): max {rel[s_].max():.3e}')
    xx = model.pack(b, cl)
    st = rn.stagnation(model, xx)
    P(f'stagnation: {json.dumps(st)}')
    ipn.save_state(f'{LANE}/runs/{a.tag}.npz', model, xx, extra=dict(tag=a.tag, C=C.item(), formulation='psi'))
    json.dump(dict(args=vars(a), hist=hist, c_l=cl.item(), C=C.item(), identity=ident.item(), stagnation=st,
                   colloc_Ehat_inf=float(np.abs(E[1:-1]).max()), colloc_rel_max=float(rel.max())), open(f'{LANE}/runs/{a.tag}_diag.json', 'w'), indent=1)
    P(f'done in {time.time()-t00:.1f}s')


if __name__ == '__main__':
    main()
