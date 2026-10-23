"""Free-c_l least-squares Q release with the radial map REBUILT from the current c_l at every Gauss-Newton step (lead 17:15Z item 2;
the earlier q_ls.py releases kept the map of the starting c_l, which fixes the far-field exponent at 1/c_l(start) and builds in a
residual floor |c_l g0 - 1|/(c_l g0 + 1) when c_l moves).  Unknowns: Chebyshev coefficients u of the mode functions (interpreted on
the current map), c_l.  Residual: all-node collocation rows + deflated centre row (c_l - 1 + c) gK + gauge row (as ipm3ql).  Jacobian:
analytic columns for u on the current model; the c_l column by central finite differences of the FULL residual with the model rebuilt
at c_l +- h (so the map dependence is included).  SVD least-squares step, backtracking on |F|_2.
  argv: start.pt tag [N M [maxit]] [clmin=1.02] [L=1.0] [fixcl=<value>]
  (start = forced or free QL state; regridded to N x M if given; the start map is the one of c_l(start), L(start)).
  clmin: lower bound for c_l in the line search (default 1.02; lead 18:06Z item 2 asks for 1.005).  L: outer map scale of the NEW model
  (default 1; lead 18:06Z item 4).  fixcl=<c_l>: hold c_l FIXED at that value (the c_l column is dropped; unknowns u only; the map is built
  from the fixed c_l): the fixed-c_l refinement protocol of the lead's 18:21Z note (1).
Saved: beta on the final map, u, cl, gamma = 1/cl (the actual far-field exponent of the saved function, since the map is rebuilt)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q, ipm3ql
torch.set_default_dtype(torch.float64); dev = 'cuda'
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

def regrid_modes(mdl_old, beta_old, mdl_new, floor=1e-14):
    """Regrid through the MODE VALUES b_k = sigma^k beta_k (well defined everywhere) instead of beta_k (garbage where sigma_old^k is below
    roundoff: those 'invisible' coefficients are never constrained by the least squares and interpolating them to a finer grid, where sigma^k is
    no longer negligible, produced starts with |F| ~ 1e6; 20:50Z).  beta_new_k = b_k(r_new) / sigma_new^k where sigma_new^k > floor, else 0."""
    from ipm3 import interp_matrix
    r_new = mdl_new.rad.rR.cpu().numpy(); t_old = mdl_old.rad.t_of_r(r_new)
    P = torch.tensor(interp_matrix(mdl_old.rad.tR_np, t_old, mdl_old.rad.wR_np), device=mdl_old.dev)
    k_old = mdl_old.kk; bk_old = (mdl_old.rad.sigR[:, None] ** k_old[None, :]) * beta_old                      # mode values on the old grid
    bk_new = P @ bk_old                                                                                         # interpolated mode values at the new radii
    tt_old = torch.tensor(t_old, device=mdl_old.dev); tt_new = mdl_new.rad.tR.to(mdl_old.dev)
    w_ratio = ((1 - tt_old) / 2) / ((1 - tt_new) / 2); bk_new = bk_new * w_ratio[:, None]                     # rho = y w b: same rho on the new map
    Mo, Mn = mdl_old.M, mdl_new.M; m = min(Mo, Mn); k = torch.arange(m, dtype=torch.float64, device=mdl_old.dev)
    sig_k = mdl_new.rad.sigR.to(mdl_old.dev)[:, None] ** k[None, :]
    beta_new = torch.zeros(len(r_new), Mn, device=mdl_old.dev)
    beta_new[:, :m] = torch.where(sig_k > floor, bk_new[:, :m] / torch.clamp(sig_k, min=floor), torch.zeros_like(sig_k))
    return beta_new.to(mdl_new.dev)

def regrid_fit(mdl_old, beta_old, mdl_new, floor=None):
    """Transfer a Q state to another grid: interpolate the MODE VALUES b_k = sigma^k beta_k (times w_old/w_new) to the new radii, then for each mode k
    find the Chebyshev coefficients c (degree N_new - k) by the minimum-norm least-squares fit of diag(sigma_new^k) Ext_k c to the interpolated mode
    values over ALL nodes (truncated SVD, relative cutoff 1e-12).  This is a regularised projection, not an exact transfer: it need not preserve the
    state's jets, gauge or residual exactly (for the fixed c_l = 1.2 96x24 state the start residual at 128x32 is 2.0e-4 against 1.7e-4 for the exact
    coefficient zero-padding that exists for nested grids at unchanged c_l and L; referee (e3)).  Reason for replacing ipm3s.regrid_s: that transfer
    interpolates beta_k itself and then inverts the ill-conditioned outer-node Vandermonde system (condition numbers 1e17 .. 1e18), which amplified the
    unconstrained coefficients of free least-squares states into starts with |F| ~ 1e6 (20:50Z).  The 'floor' argument is unused (kept for call
    compatibility)."""
    from ipm3 import interp_matrix
    r_new = mdl_new.rad.rR.cpu().numpy(); t_old = mdl_old.rad.t_of_r(r_new)
    P = torch.tensor(interp_matrix(mdl_old.rad.tR_np, t_old, mdl_old.rad.wR_np), device=mdl_old.dev)
    bk_old = (mdl_old.rad.sigR[:, None] ** mdl_old.kk[None, :]) * beta_old
    bk_new = P @ bk_old
    tt_old = torch.tensor(t_old, device=mdl_old.dev); tt_new = mdl_new.rad.tR.to(mdl_old.dev)
    bk_new = bk_new * (((1 - tt_old) / 2) / ((1 - tt_new) / 2))[:, None]
    Mn, N = mdl_new.M, mdl_new.N; m = min(mdl_old.M, Mn); sig = mdl_new.rad.sigR.to(mdl_old.dev)
    u_parts = []; beta_new = torch.zeros(N + 1, Mn, device=mdl_old.dev)
    for k in range(Mn):
        nk = N + 1 - k; coef = torch.zeros(nk, device=mdl_old.dev)
        if k < m:
            # minimum-norm least-squares fit IN THE MODE-VALUE SPACE: minimise || diag(sigma^k) Ext_k c - b_k || over all nodes (the inner nodes are
            # down-weighted by sigma^k automatically; invisible directions get the minimum-norm value, i.e. stay small)  [20:53Z; the earlier
            # beta-space fits with a sigma^k floor extrapolated wildly]
            sk = sig ** k; A = sk[:, None] * mdl_new.Ext[k].to(mdl_old.dev)
            U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ > 1e-12 * S_[0]
            coef = Vh_[keep].T @ ((U_[:, keep].T @ bk_new[:, k]) / S_[keep])
        u_parts.append(coef); beta_new[:, k] = mdl_new.Ext[k].to(mdl_old.dev) @ coef
    return beta_new.to(mdl_new.dev), torch.cat(u_parts).to(mdl_new.dev)

_cache = {}
OPT = dict(clmin=1.02, L=1.0, fixcl=None, y3=False, M2=None, fine=False, snap=0, tag='')
def model(N, M, cl, Lf):
    key = (N, M, round(cl, 12), OPT['L'], OPT['y3'], OPT['M2'], OPT['fine'])
    if key not in _cache:
        if len(_cache) > 6: _cache.clear()
        _cache[key] = ipm3ql.IPM3QL(N=N, M=M, L=OPT['L'], gamma=1 / cl, device=dev, Lf=Lf, centre=('y3id' if OPT['y3'] == 'id' else ('y3' if OPT['y3'] else 'identity')), M2=OPT['M2'], fine=OPT['fine'])
    return _cache[key]

def Ffull(N, M, u, cl, gK, Lf):
    q = model(N, M, cl, Lf); F, E, flds = q.system(u, cl, gK, mu=None, forced=False); return F, flds, q

def gn_free(N, M, u, cl, gK, Lf, maxit=60, tol=1e-12, log=None, h=1e-6, rcond=1e-13):
    F, flds, q = Ffull(N, M, u, cl, gK, Lf); nF = F.norm().item(); hist = []
    for it in range(maxit):
        J = q.jacobian(u, cl, gK, mu=None, forced=False, flds=flds)          # columns wrt u are exact on the current model
        if OPT['fixcl'] is None:
            Fp, _, _ = Ffull(N, M, u, cl + h, gK, Lf); Fm, _, _ = Ffull(N, M, u, cl - h, gK, Lf)
            J[:, -1] = (Fp - Fm) / (2 * h)                                      # c_l column including the map dependence
        else:
            J = J[:, :-1]                                                       # c_l fixed: unknowns u only
        U, S, Vh = torch.linalg.svd(J, full_matrices=False)
        coef = (U.T @ (-F)) / S; coef[S < rcond * S[0]] = 0.0; du = Vh.T @ coef
        if OPT['fixcl'] is not None: du = torch.cat([du, torch.zeros(1, device=du.device)])
        lam = 1.0; accepted = False
        for _ in range(30):
            un = u + lam * du[:-1]; cln = cl + lam * du[-1].item()
            if cln <= OPT['clmin']: lam *= 0.5; continue
            Fn, fn, qn = Ffull(N, M, un, cln, gK, Lf); nFn = Fn.norm().item()
            if nFn < (1 - 1e-4 * lam) * nF: accepted = True; break
            lam *= 0.5
        if not accepted:                      # referee (e2) item 13: never accept a failed trial; keep the last accepted state and stop
            msg = f"  qfree it {it}: LINE SEARCH FAILED (no decrease down to lam={lam:.2e}); keeping the last accepted state"
            if log: log.write(msg + "\n"); log.flush()
            break
        keep = S >= rcond * S[0]; smin_eff = S[keep][-1].item()
        a0 = qn.beta_full(un)[0, 0].item()
        msg = f"  qfree it {it}: |F|2 {nF:.3e} -> {nFn:.3e} (max {Fn.abs().max().item():.2e}) lam={lam:.3g} cl={cln:.10f} a0={a0:.8f} smin(above cutoff)={smin_eff:.2e} smax={S[0].item():.2e}"
        if log: log.write(msg + "\n"); log.flush()
        hist.append((nF, nFn, lam, cln, a0))
        u, cl, F, flds, q, nF = un, cln, Fn, fn, qn, nFn
        if OPT['snap'] and (it + 1) % OPT['snap'] == 0:          # snapshots along the drift (lead 19:13Z item 4)
            torch.save(dict(beta=q.beta_full(u).cpu(), u=u.cpu(), cl=cl, mu=None, gamma=1 / cl, gamma_map=1 / cl, N=N, M=M, L=OPT['L'], Lf=Lf, gK=gK, p=q.p,
                            rep='QL-free-map', step=it + 1, options=dict(OPT)), f"runs/{OPT['tag']}_step{it + 1:04d}.pt")
        if F.abs().max().item() < tol or lam < 1e-7: break
    return u, cl, dict(F=F, flds=flds, nF=F.abs().max().item(), nF2=nF, S=S, its=it + 1, hist=hist, model=q)

if __name__ == '__main__':
    pos = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
    OPT['clmin'] = float(kw.get('clmin', 1.02)); OPT['L'] = float(kw.get('L', 1.0)); OPT['fixcl'] = float(kw['fixcl']) if 'fixcl' in kw else None; OPT['M2'] = int(kw['M2']) if 'M2' in kw else None; OPT['fine'] = bool(int(kw.get('fine', 0))); OPT['snap'] = int(kw.get('snap', 0)); OPT['tag'] = pos[1]
    start = pos[0]; tag = pos[1]; st = torch.load(start, weights_only=False)
    N = int(pos[2]) if len(pos) > 2 else st['N']; M = int(pos[3]) if len(pos) > 3 else st['M']
    cl_start = st['cl']; gK = float(kw['gK']) if 'gK' in kw else st['gK']; Lf = st['Lf']; L_start = st.get('L', 1.0)   # gK=<value> overrides the saved coefficient gauge (true map-scale test at fixed physical K: gK' = gK (L/L')^(1-1/c_l); shift 3)
    cl0 = OPT['fixcl'] if OPT['fixcl'] is not None else cl_start
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_free (map rebuilt with c_l) from {start} at {N}x{M} {now()} options {kw}\n")
    qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=L_start, gamma=1 / cl_start, device=dev, Lf=Lf)
    q0 = model(N, M, cl0, Lf)
    same = (N, M) == (st['N'], st['M']) and abs(cl0 - cl_start) < 1e-14 and abs(OPT['L'] - L_start) < 1e-14
    if same:
        beta0 = st['beta'].to(dev)
        u = st['u'].to(dev) if ('u' in st and st['u'] is not None and len(st['u']) == q0.nu) else q0.beta_to_u(beta0)   # reuse the saved coefficients: beta_to_u is ill-conditioned (referee (e3))
    else:
        beta0, u = regrid_fit(qo, st['beta'].to(dev), q0)
    t0 = time.time()
    maxit = int(pos[4]) if len(pos) > 4 else 60
    u2, cl2, info = gn_free(N, M, u, cl0, gK, Lf, maxit=maxit, log=log)
    q = info['model']; beta = q.beta_full(u2); flds = info['flds']; c = q.psi_xy0(flds).item(); a0 = beta[0, 0].item()
    og = ipm3ql.between_node(q, beta, cl2, flds, 0.0); tail = ipm3ql.cheb_tail(q, u2)
    S = info['S']; keep = S >= 1e-13 * S[0]; smin_eff = S[keep][-1].item(); nnull = int((~keep).sum().item())
    A = 2 * cl2 - 1
    mu0 = st['mu'] if st.get('mu') is not None else 0.0
    m = (f"QFREE {'fixed-cl' if OPT['fixcl'] is not None else 'release'} {N}x{M} from {start} (start cl={cl_start}, Delta0={mu0/beta0[0,0].item():+.3e}; "
         f"map rebuilt with c_l; L={OPT['L']}, clmin={OPT['clmin']}, fixcl={OPT['fixcl']}; {time.time()-t0:.0f}s): "
         f"|F|max={info['nF']:.1e} |F|2={info['nF2']:.1e} its={info['its']} smin={smin_eff:.1e} ({nnull} invisible) smax={S[0].item():.1e} "
         f"cl={cl2:.10f} a0={a0:.10f} c={c:+.10f} cl+c-1={cl2+c-1:+.3e} a0/4A={a0/(4*A):.3f} cheb-tail(mode0,1)={tail[0]:.1e},{tail[1]:.1e} "
         f"between-node |R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}]")
    print(m, flush=True); log.write(m + "\n")
    torch.save(dict(beta=beta.cpu(), u=u2.cpu(), cl=cl2, mu=None, gamma=1 / cl2, gamma_map=1 / cl2, N=N, M=M, L=OPT['L'], Lf=Lf, gK=gK, p=q.p,
                    rep='QL-free-map', hist=info['hist'], options=dict(OPT), start=start), f'runs/{tag}.pt')
