"""Two-grid preconditioned Newton-Krylov on a fine grid (variant of twogrid.py): the stiff part of the fine system is solved
with right-preconditioned GMRES on J_f M^-1, M^-1 = Pro (J_c)^+_cut Res + (I - Pro Res) (coarse part: TRUNCATED pseudo-inverse of the coarse dense Jacobian (singular
directions below s_cut dropped, so the coarse near-kernel does not dominate the preconditioner) between the interpolation operators
(Res: fine -> coarse node values, Pro: coarse -> fine; c_l and C copied). Matvecs by central finite differences of the smooth fine
residual (jtools.RES_KW); line search on the same residual. The fine soft subspace is not touched (the residual stagnates there, as on
the coarse grid), so the result is the fine grid's stagnation state, for the cross-grid action test at a stationary-stiff state.
Usage: python3 src/twogrid2.py runs/J_<coarse>.pt runs/coarse_state.npz N M beta L tag [maxit=4] [gmres=30] [s_cut=1e-3] [Npsi=480] [--fine_state path]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt, run_newton as rn
from twogrid import interp_ops
import run_psi_newton as rpn

LANE = jt.LANE


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    fine_state = sys.argv[sys.argv.index('--fine_state') + 1] if '--fine_state' in sys.argv else None
    jpath, cstate = args[0], args[1]
    Nf, Mf, beta, L = int(args[2]), int(args[3]), float(args[4]), float(args[5]); tag = args[6]
    maxit = int(args[7]) if len(args) > 7 else 4; mg = int(args[8]) if len(args) > 8 else 30
    s_cut = float(args[9]) if len(args) > 9 else 1e-3; Npsi = int(args[10]) if len(args) > 10 else 480
    log = open(f'{LANE}/runs/{tag}.log', 'a')
    def P(*s):
        msg = ' '.join(str(v) for v in s); print(msg, flush=True); log.write(msg + '\n'); log.flush()
    D = torch.load(jpath); Jc = D['J'].cuda().double(); nc = Jc.shape[0]
    mc, xc, dc = ipn.load_state(cstate); C0 = float(dc['C'])
    mf = ipn.Model(Nf, Mf, L, device='cuda', beta=beta, Npsi=Npsi); ch = cm.Charac(mf)
    if fine_state:
        m1, x1, d1 = ipn.load_state(fine_state); bf, clf = m1.unpack(x1); C0 = float(d1['C'])
    else:
        xf = ipn.project_state(mc, xc, mf); bf, clf = mf.unpack(xf)
    z = ch.pack(bf, clf, C0); n = z.numel()
    Res_b, Pro_b = interp_ops(mc, mf, float(clf)); Res_b = Res_b.double(); Pro_b = Pro_b.double()
    P(f'# twogrid2 {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}: fine ({Nf},{Mf},{beta}) L={L} n={n}; coarse J {jpath} (n_c={nc}); s_cut {s_cut}; TAU_SWITCH {cm.TAU_SWITCH}; RES_KW {jt.RES_KW}')
    # truncated pseudo-inverse of the coarse Jacobian in the scaled coordinates (c_l per 1/400)
    t0 = time.time(); scale = torch.ones(nc, device='cuda', dtype=torch.float64); scale[-2] = 1.0 / 400.0
    U, S, Vh = torch.linalg.svd(Jc * scale[None, :]); keep = S > s_cut
    P(f'  coarse SVD: smax {S[0].item():.3e}, kept {int(keep.sum())} of {nc} directions (s > {s_cut}); smallest kept {S[keep][-1].item():.3e} ({time.time()-t0:.0f}s)')
    Uk = U[:, keep]; Sk = S[keep]; Vk = Vh[keep].T
    def Jc_pinv(r):   # r: coarse residual-space vector -> coarse step in UNSCALED coordinates
        return scale * (Vk @ ((Uk.T @ r) / Sk))
    def Res(v): return torch.cat([Res_b @ v[:n - 2], v[n - 2:]])
    def Pro(y): return torch.cat([Pro_b @ y[:nc - 2], y[nc - 2:]])
    def Minv_left(v): return Pro(Jc_pinv(Res(v)))
    # additive two-level preconditioner (13:45Z): coarse pseudo-inverse on the coarse-representable part plus the identity on the
    # fine-only complement (the Psi rows have unit diagonal), used as a RIGHT preconditioner so that GMRES minimizes the true residual
    def Minv(v):
        rv = Res(v); return Pro(Jc_pinv(rv)) + (v - Pro(rv))
    Fz = lambda zz: ch.F(zz, **jt.RES_KW)
    F = Fz(z); nF = F.norm().item()
    hist = []
    for it in range(maxit):
        t0 = time.time(); bb, cll, CC = ch.unpack(z)
        P(f'it {it}: |F|_2 {nF:.4e} |F|_inf {F.abs().max().item():.3e} h(P)-1 {F[-2].item():+.3e} ident {F[-1].item():+.3e} c_l {cll.item():.10f} C {CC.item():.8f}')
        hist.append(dict(it=it, F2=nF, Finf=F.abs().max().item(), cl=cll.item(), C=CC.item(), hP1=F[-2].item(), ident=F[-1].item()))
        def Aop(y):   # right-preconditioned operator J_f M^-1
            v = Minv(y); e = 1e-4 / v.norm().item()
            return (Fz(z + e * v) - Fz(z - e * v)) / (2 * e)
        y, rh, rv = rpn.gmres(Aop, -F, m=mg, tol=1e-3, P=P); dz = Minv(y)
        lam = 1.0; nFn = nF
        for _ in range(6):
            zn = z + lam * dz; Fn = Fz(zn); nFn = Fn.norm().item()
            if nFn < nF: break
            lam *= 0.5
        P(f'   gmres its {len(rh)-1} rel res {rh[-1]/rh[0]:.2e}; |dz|_2 {dz.norm().item():.3e} |dz|_inf {dz.abs().max().item():.3e} dc_l {dz[-2].item():+.3e} dC {dz[-1].item():+.3e} lam {lam} |F| -> {nFn:.4e} ({time.time()-t0:.0f}s)')
        if nFn >= nF: P('   no decrease; stop'); break
        z, F, nF = zn, Fn, nFn
        bb, cll, CC = ch.unpack(z)
        ipn.save_state(f'{LANE}/runs/{tag}.npz', mf, mf.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_twogrid2', it=it + 1, F2=nF, Finf=F.abs().max().item()))
        if (hist[-1]['F2'] - nF) / hist[-1]['F2'] < 1e-2: P('   relative decrease below 1 percent; stop'); break
    bb, cll, CC = ch.unpack(z)
    ipn.save_state(f'{LANE}/runs/{tag}.npz', mf, mf.pack(bb, cll), extra=dict(tag=tag, C=CC.item(), formulation='psi_hybrid_twogrid2', F2=nF, Finf=F.abs().max().item()))
    hist.append(dict(it='final', F2=nF, Finf=F.abs().max().item(), cl=cll.item(), C=CC.item(), hP1=F[-2].item(), ident=F[-1].item()))
    json.dump(dict(tag=tag, hist=hist, s_cut=s_cut, gmres=mg), open(f'{LANE}/runs/{tag}_hist.json', 'w'), indent=1)
    try:
        st = rn.stagnation(mf, mf.pack(bb, cll)); P(f'stagnation: {json.dumps(st)}')
    except Exception as e: P('stagnation failed:', e)
    P('done')


if __name__ == '__main__':
    main()
