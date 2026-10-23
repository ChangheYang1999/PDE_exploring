"""
Lead's request 15:36Z item 2: smoothness at the origin imposed by CONSTRAINTS, unforced problem, c_l free.
For a smooth rho, b = sum_k bhat_k(r) cos(2k theta) with bhat_k(r) = r^(2k) x (smooth function of r^2).  In the map
r ~ L (1+t) 2^(-p) near t = -1 (r is analytic in t with r'(−1) != 0), this means: the Taylor coefficients of bhat_k(t) at
t = -1 of orders j < 2k vanish, and the odd-order coefficients j <= J vanish (for every k <= K0).  Rows:
    (D_R^j bhat_k)(t = -1) = 0   for  j < 2k   or  (j odd and j <= J),   k = 0..K0.
Added to the unforced system (continuity, identity, interior, gauge) with unknowns (b, c_l): over-determined; solved by
Gauss-Newton (lstsq) with backtracking.  Report the minimal residual (the max over the PDE rows and over the constraint
rows separately), c_l and a_0, against (N, M, J).  Label: tests C^(J+1)-type smoothness at the origin, not C^inf.
"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3

torch.set_default_dtype(torch.float64)
dev = 'cuda'


def constraint_matrix(mdl, J, K0):
    """rows acting on b (flattened (N+1, M)): Taylor-coefficient constraints at t = -1 for modes k <= K0."""
    N, M = mdl.N, mdl.M
    DR = mdl.rad.DR
    Dpow = [torch.eye(N + 1, device=dev)]
    for j in range(1, max(J, 2 * K0) + 1):
        Dpow.append(Dpow[-1] @ DR)
    A = mdl.ang.A['EE']                               # values -> cos coefficients (M x M)
    rows = []
    labels = []
    for k in range(0, K0 + 1):
        for j in range(0, max(J, 2 * K0) + 1):
            if j < 2 * k or (j % 2 == 1 and j <= J):
                if j == 0 and k == 0:
                    continue                          # bhat_0(-1) = a_0 is free
                # row: (Dpow[j][0, :] on t) x (A[k, :] on theta)
                rows.append(torch.outer(Dpow[j][0, :], A[k, :]).reshape(-1))
                labels.append((k, j))
    C = torch.stack(rows)
    C = C / C.norm(dim=1, keepdim=True)              # normalise each constraint row (D^j entries grow like N^(2j))
    return C, labels


def gn_solve(mdl, b, cl, beta, Cmat, maxit=150, log=None, wc=1.0, lm=False):
    """Gauss-Newton (lm=False) or Levenberg-Marquardt (lm=True, adaptive damping) on the weighted over-determined
    system [F_pde; wc * C b]."""
    N, M = mdl.N, mdl.M; nb = (N + 1) * M
    def Ffull(b, cl):
        mdl.set_gamma(1.0 / cl)
        F, E, flds = mdl.system(b, cl, gauge_value=beta)
        return torch.cat([F, wc * (Cmat @ b.reshape(-1))]), flds
    F, flds = Ffull(b, cl); nF = F.norm().item(); damp = 1e-3
    for it in range(maxit):
        Jb = mdl.jacobian(b, cl, flds)
        J = torch.zeros(nb + 1 + Cmat.shape[0], nb + 1, device=dev)
        J[:nb + 1, :] = Jb
        J[nb + 1:, :nb] = wc * Cmat
        if lm:
            JtJ = J.T @ J; g = J.T @ F
            accepted = False
            for _ in range(20):
                A = JtJ + damp * torch.diag(torch.diag(JtJ)); du = torch.linalg.solve(A, -g)
                bn = b + du[:nb].reshape(N + 1, M); cln = cl + du[nb].item()
                if cln > 1.0:
                    Fn, fn = Ffull(bn, cln); nFn = Fn.norm().item()
                    if nFn < nF:
                        accepted = True; damp = max(damp / 3, 1e-12); break
                damp *= 4
            if not accepted:
                break
            lam = damp
        else:
            du = torch.linalg.lstsq(J, -F.unsqueeze(1)).solution.squeeze(1)
            lam = 1.0
            for _ in range(30):
                bn = b + lam * du[:nb].reshape(N + 1, M); cln = cl + lam * du[nb].item()
                if cln <= 1.0:
                    lam *= 0.5; continue
                Fn, fn = Ffull(bn, cln); nFn = Fn.norm().item()
                if nFn < (1 - 1e-4 * lam) * nF:
                    break
                lam *= 0.5
        msg = f"  {'lm' if lm else 'gn'} it {it}: |F|2 {nF:.3e} -> {nFn:.3e} (pde rows max {Fn[:nb+1].abs().max().item():.2e}, constraint rows max {Fn[nb+1:].abs().max().item():.2e}) {'damp' if lm else 'lam'}={lam:.3g} cl={cln:.8f} a0={bn[0,0].item():.6f}"
        if log: log.write(msg + "\n"); log.flush()
        decrease = nF - nFn
        b, cl, F, flds, nF = bn, cln, Fn, fn, nFn
        if (not lm and lam < 1e-7) or nF < 1e-12 or (lm and decrease < 1e-13 * max(1.0, nF)):
            break
    return b, cl, F, flds, it + 1


if __name__ == '__main__':
    start = sys.argv[1]; tag = sys.argv[2]
    pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[3].split(',')]
    Js = [int(v) for v in sys.argv[4].split(',')]; K0 = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    wc = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0; lm = (len(sys.argv) > 7 and sys.argv[7] == 'lm')
    st = torch.load(start)
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# smoothness-by-constraints GN from {start} pairs {pairs} J {Js} K0 {K0} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
    mo = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
    b0 = st['b'].to(dev); cl0 = st['cl']
    for (N, M) in pairs:
        for J in Js:
            mdl = ipm3.IPM3(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev, couple_gamma=True); mdl.gauge = 'inf'
            b = ipm3.regrid(mo, b0, mdl); beta = (mdl.rad.ext1_R @ b).mean().item()
            Cmat, labels = constraint_matrix(mdl, J, K0)
            t0 = time.time()
            b, cl, F, flds, its = gn_solve(mdl, b, cl0, beta, Cmat, log=log, maxit=300, wc=wc, lm=lm)
            nb = (N + 1) * M
            c = mdl.psi_xy0(flds).item(); a0 = b[0, 0].item()
            # between-node unforced residual
            tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
            rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
            ev = mdl.evaluate(b, cl, flds, RR, TT); q = np.abs(ev['R']) / ev['Nf']
            og = [q[(RR >= lo) & (RR < hi)].max() for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e30)]]
            msg = (f"N={N} M={M} J={J} K0={K0} wc={wc} {'LM' if lm else 'GN'} ({Cmat.shape[0]} constraint rows): its={its} |F|2={F.norm().item():.3e} pde rows max={F[:nb+1].abs().max().item():.2e} "
                   f"constraint rows max={F[nb+1:].abs().max().item():.2e} cl={cl:.8f} c={c:+.8f} cl+c-1={cl+c-1:+.1e} a0={a0:.6f} "
                   f"between-node |R|/Nf [<.1,.1-1,1-100,>100]={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e} time {time.time()-t0:.0f}s")
            print(msg, flush=True); log.write(msg + "\n"); log.flush()
            torch.save(dict(b=b.cpu(), cl=cl, gamma=1 / cl, N=N, M=M, L=1.0, p=mdl.p, J=J, K0=K0), f'runs/{tag}_N{N}M{M}_J{J}.pt')
