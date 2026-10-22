"""Dense Levenberg-Marquardt least squares for the B2 profile problem (see bq3core.py)."""
import sys, time, json, argparse, os
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT, fields_at

torch.set_default_dtype(DT)


def unpack(z, K, Nb, beta_free, beta_fixed):
    """z = [cF without cF[0,0], cG, (beta)] -> cF, cG, beta"""
    N = K * Nb
    cF = torch.cat([torch.ones(1, dtype=DT, device=z.device), z[:N - 1]])
    cG = z[N - 1:2 * N - 1]
    beta = z[2 * N - 1] if beta_free else torch.tensor(beta_fixed, dtype=DT, device=z.device)
    return cF, cG, float(beta)


def weights(NF, NG, b, fl, RF=None, RG=None, gamma=0.0, eps=0.05):
    """w = 1/(N + fl * radial envelope of N), optionally times Lawson factor (q + eps*max q)^gamma with q = |R|/N."""
    def wfun(N, R):
        Nm = N.reshape(b.Nc, b.Nphi)
        env = Nm.max(1, keepdim=True).values
        env = torch.maximum(env, 1e-300 * torch.ones_like(env))
        w = (1.0 / (Nm + fl * env)).reshape(-1)
        if gamma > 0 and R is not None:
            q = (R.abs() / (N + fl * env.expand(b.Nc, b.Nphi).reshape(-1)))
            fac = (q + eps * q.max()) ** gamma
            fac = fac / fac.mean()
            w = w * torch.sqrt(fac)
        return w
    return wfun(NF, RF), wfun(NG, RG)


def cons_obj(g, cG, beta, wc):
    if wc <= 0:
        return 0.0
    return (wc ** 2) * ((g.c_op @ cG - (1 + beta / 2)) ** 2 + (cG[0] - 4.0 / beta) ** 2)


def evaluate(basis, L, cF, cG, beta, geom_cache={}):
    key = (round(beta, 14), L, id(basis))
    if key not in geom_cache:
        geom_cache.clear()
        geom_cache[key] = Geometry(basis, beta, L)
    g = geom_cache[key]
    p = Problem(g)
    f = p.fields(cF, cG)
    RF, RG, NF, NG = p.residuals(cF, cG, f)
    return g, p, f, RF, RG, NF, NG


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--beta', type=float, default=3.0)
    ap.add_argument('--free', action='store_true', help='beta free')
    ap.add_argument('--L', type=float, default=1.0)
    ap.add_argument('--Nt', type=int, default=60)
    ap.add_argument('--deg', type=int, default=5)
    ap.add_argument('--K', type=int, default=20)
    ap.add_argument('--Nphi', type=int, default=40)
    ap.add_argument('--mreg', type=int, default=2)
    ap.add_argument('--ngc', type=int, default=3)
    ap.add_argument('--iters', type=int, default=50)
    ap.add_argument('--fl', type=float, default=0.1, help='weight floor fraction of radial envelope')
    ap.add_argument('--lam', type=float, default=1e-2)
    ap.add_argument('--init', type=str, default='')
    ap.add_argument('--out', type=str, default='state.npz')
    ap.add_argument('--log', type=str, default='')
    ap.add_argument('--seed_amp', type=float, default=0.0, help='random perturbation amplitude of initial guess')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--dbeta', type=float, default=1e-5)
    ap.add_argument('--reweight_every', type=int, default=1)
    ap.add_argument('--maxtime', type=float, default=3600.0)
    ap.add_argument('--tik', type=float, default=0.0, help='Tikhonov weight mu on |coeff|^2 (relative to max diag JtJ)')
    ap.add_argument('--init_c', action='store_true', help='initial guess with g_1 mode giving c = 1 + beta/2')
    ap.add_argument('--lam_min', type=float, default=1e-12)
    ap.add_argument('--grade', type=float, default=1.0, help='knot grading exponent (knots = linspace^grade)')
    ap.add_argument('--wc', type=float, default=0.0, help='weight of centre constraint rows (c = 1+beta/2, G(0) = 4/beta)')
    ap.add_argument('--irls', type=float, default=0.0, help='Lawson exponent gamma: weights *= (q + eps max q)^gamma, q = |R|/N')
    ap.add_argument('--irls_eps', type=float, default=0.05)
    args = ap.parse_args()
    dev = 'cuda'
    t_start = time.time()
    basis = Basis(args.Nt, args.deg, args.K, args.Nphi, ng_coll=args.ngc, m_reg=args.mreg, device=dev, grade=args.grade)
    K, Nb = basis.K, basis.Nb
    N = K * Nb
    beta = args.beta
    # initial guess
    if args.init:
        d = np.load(args.init)
        cF0 = torch.tensor(d['cF'], dtype=DT, device=dev); cG0 = torch.tensor(d['cG'], dtype=DT, device=dev)
        if cF0.numel() != N:
            # transplant between bases by least squares on point values of F and G
            b_old = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']) if 'ngc' in d else 3, m_reg=int(d['mreg']), device=dev, grade=float(d['grade']) if 'grade' in d else 1.0)
            g_old = Geometry(b_old, float(d['beta']), float(d['L']))
            # evaluate old fields at new collocation points: build a Geometry for the new basis and use its points
            g_new = Geometry(basis, beta if not args.free else float(d['beta']), args.L)
            from bq3core import Basis as _B
            # evaluate old representation at new points by direct formula
            Fold, Gold = eval_fields_at(b_old, float(d['beta']), float(d['L']), cF0, cG0, g_new.x, g_new.y)
            Dt = ((1 - basis.t_coll_t) ** (beta + 2))[:, None].expand(basis.Nc, basis.Nphi).reshape(-1)
            w = 1.0 / Dt
            cF0 = torch.linalg.lstsq(g_new.Phi0F * w[:, None], (Fold * w)[:, None], driver='gels').solution[:, 0]
            cG0 = torch.linalg.lstsq(g_new.Phi0G * w[:, None], (Gold * w)[:, None], driver='gels').solution[:, 0]
            cF0 = cF0 / cF0[0]
        if args.free:
            beta = float(d['beta'])
    else:
        cF0 = torch.zeros(N, dtype=DT, device=dev); cG0 = torch.zeros(N, dtype=DT, device=dev)
        cF0[:Nb] = 1.0
        cG0[:Nb] = 4.0 / beta
        if args.init_c and K > 1:
            g0 = Geometry(basis, beta, args.L)
            # c = -(1/4) int g_1 dr with g_1 = -gamma t D(t)  ->  c = (gamma/4) int t D dr
            tq = basis.t_quad_t; wq = basis.w_quad_t * g0.drdtq
            # g_1 = D_G * sum_{j>=1} c B_j ~ D_G (1 - B_0): c = -(1/4) int g_1 dr
            Bq, _ = basis._design(basis.t_quad)
            Bq = torch.tensor(Bq, dtype=DT, device=dev)
            I = (wq * (1 - tq) ** g0.pG * (1 - Bq[:, 0])).sum().item()
            gamma = 4 * (1 + beta / 2) / I
            cG0[Nb + 1:2 * Nb] = -gamma
            print(f"# init_c: gamma={gamma:.6f}, int t D dr = {I:.6f}, c_op check = {(g0.c_op @ cG0).item():.6f}")
    if args.seed_amp > 0:
        gen = torch.Generator(device='cpu').manual_seed(args.seed)
        cF0 = cF0 + args.seed_amp * torch.randn(N, generator=gen, dtype=DT).to(dev)
        cG0 = cG0 + args.seed_amp * torch.randn(N, generator=gen, dtype=DT).to(dev)
        cF0[0] = 1.0
    z = torch.cat([cF0[1:], cG0] + ([torch.tensor([beta], dtype=DT, device=dev)] if args.free else []))
    lam = args.lam
    logf = open(args.log, 'a') if args.log else None

    def log(s):
        print(s, flush=True)
        if logf:
            logf.write(s + '\n'); logf.flush()

    log(f"# solve.py start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} args {vars(args)} Nb={Nb} Nc={basis.Nc} Npts={basis.Nc*basis.Nphi} Nunk={z.numel()}")
    cF, cG, beta = unpack(z, K, Nb, args.free, args.beta)
    g, p, f, RF, RG, NF, NG = evaluate(basis, args.L, cF, cG, beta)
    wF, wG = weights(NF, NG, basis, args.fl)
    obj = ((wF * RF) ** 2).sum() + ((wG * RG) ** 2).sum() + cons_obj(g, cG, beta, args.wc)
    for it in range(args.iters):
        if time.time() - t_start > args.maxtime:
            log("# maxtime reached"); break
        t0 = time.time()
        if it % args.reweight_every == 0:
            wF, wG = weights(NF, NG, basis, args.fl, RF, RG, args.irls, args.irls_eps)
            obj = ((wF * RF) ** 2).sum() + ((wG * RG) ** 2).sum() + cons_obj(g, cG, beta, args.wc)
            if args.tik > 0 and it > 0:
                obj = obj + mu * (z ** 2).sum()
        J = p.jacobian(cF, cG, f)                       # (2Npts, 2N)
        J = J[:, 1:]                                    # drop cF[0,0]
        if args.free:
            # finite-difference column for beta
            gp, pp, fp, RFp, RGp, _, _ = evaluate(basis, args.L, cF, cG, beta + args.dbeta, geom_cache={})
            gm, pm, fm, RFm, RGm, _, _ = evaluate(basis, args.L, cF, cG, beta - args.dbeta, geom_cache={})
            colb = torch.cat([(RFp - RFm), (RGp - RGm)]) / (2 * args.dbeta)
            J = torch.cat([J, colb[:, None]], 1)
        w = torch.cat([wF, wG])
        R = torch.cat([RF, RG])
        if args.wc > 0:
            Nun = J.shape[1]
            rows = torch.zeros(2, Nun, dtype=DT, device=dev)
            rows[0, N - 1:2 * N - 1] = g.c_op
            rows[1, N - 1] = 1.0
            Rc = torch.stack([g.c_op @ cG - (1 + beta / 2), cG[0] - 4.0 / beta])
            if args.free:
                rows[0, -1] = -0.5
                rows[1, -1] = 4.0 / beta ** 2
            J = torch.cat([J, rows], 0)
            R = torch.cat([R, Rc])
            w = torch.cat([w, args.wc * torch.ones(2, dtype=DT, device=dev)])
        Jw = J * w[:, None]
        rw = R * w
        JtJ = Jw.T @ Jw
        Jtr = Jw.T @ rw
        dg = torch.diagonal(JtJ).clone()
        dg = torch.maximum(dg, 1e-30 * dg.max())
        if args.tik > 0:
            mu = args.tik * dg.max()
            JtJ = JtJ + mu * torch.eye(JtJ.shape[0], dtype=DT, device=dev)
            Jtr = Jtr + mu * z
        del Jw, J
        accepted = False
        for trial in range(12):
            Mreg = JtJ + lam * torch.diag(dg)
            try:
                Lc = torch.linalg.cholesky(Mreg)
                delta = -torch.cholesky_solve(Jtr[:, None], Lc)[:, 0]
            except Exception as e:
                lam *= 10; continue
            znew = z + delta
            cFn, cGn, betan = unpack(znew, K, Nb, args.free, args.beta)
            if betan <= 2.0 + 1e-9 or betan > 50:
                lam *= 10; continue
            gn, pn, fn, RFn, RGn, NFn, NGn = evaluate(basis, args.L, cFn, cGn, betan, geom_cache={})
            objn = ((wF * RFn) ** 2).sum() + ((wG * RGn) ** 2).sum() + cons_obj(gn, cGn, betan, args.wc)
            if args.tik > 0:
                objn = objn + mu * (znew ** 2).sum()
            if objn < obj:
                accepted = True
                z = znew; cF, cG, beta = cFn, cGn, betan
                g, p, f, RF, RG, NF, NG = gn, pn, fn, RFn, RGn, NFn, NGn
                lam = max(lam / 3, args.lam_min)
                obj = objn
                break
            else:
                lam *= 4
        nrmF = (RF / (NF + 1e-300)).abs()
        nrmG = (RG / (NG + 1e-300)).abs()
        cval = (g.c_op @ cG).item()
        # region report: r<1, 1<=r<10, r>=10
        rr = g.rr
        def regmax(v, lo, hi):
            m = (rr >= lo) & (rr < hi)
            return v[m].max().item() if m.any() else float('nan')
        log(f"it {it:3d} acc={int(accepted)} lam={lam:.1e} obj={obj.item():.6e} beta={beta:.8f} c-(1+beta/2)={cval-(1+beta/2):+.3e} "
            f"max|RF/NF|={nrmF.max().item():.3e} max|RG/NG|={nrmG.max().item():.3e} "
            f"[r<1 {regmax(nrmF,0,1):.2e}/{regmax(nrmG,0,1):.2e}; 1-10 {regmax(nrmF,1,10):.2e}/{regmax(nrmG,1,10):.2e}; "
            f"10-1e3 {regmax(nrmF,10,1e3):.2e}/{regmax(nrmG,10,1e3):.2e}; >1e3 {regmax(nrmF,1e3,1e99):.2e}/{regmax(nrmG,1e3,1e99):.2e}] "
            f"|cF|={cF.abs().max().item():.2e} |cG|={cG.abs().max().item():.2e} dt={time.time()-t0:.1f}s")
        np.savez(args.out, cF=cF.cpu().numpy(), cG=cG.cpu().numpy(), beta=beta, L=args.L, Nt=args.Nt, deg=args.deg,
                 K=args.K, Nphi=args.Nphi, mreg=args.mreg, ngc=args.ngc, grade=args.grade, obj=obj.item(), fl=args.fl,
                 maxRF=nrmF.max().item(), maxRG=nrmG.max().item(), c=cval)
        if not accepted and lam > 1e8:
            log("# stalled (lam > 1e8)"); break
    log(f"# done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} elapsed {time.time()-t_start:.0f}s")


def eval_fields_at(b, beta, L, cF, cG, x, y, rmap='r'):
    from bq3core import fields_at
    return fields_at(b, beta, L, rmap, cF, cG, x, y)


if __name__ == '__main__':
    main()
