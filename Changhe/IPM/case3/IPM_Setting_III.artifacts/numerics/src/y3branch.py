"""Exploratory solver for the SECONDARY branch (pure y^3-leading: rho(0,y) ~ a_3 y^3, rho_y(0) = 0, no x^2 factor).
Centre conditions: b(0, theta) = 0 and the cubic-order identity c_l + c = 1/3 (c = psi_xy(0)); DW(0) = diag(2c_l - 1/3, 1/3).
System: rows b(0, theta_j) = 0 (M), identity c_l - 1/3 + c[b] = 0 (1), interior equations (N M), gauge mean b(inf) = beta (1);
unknowns (b, c_l): over-determined by one -> Gauss-Newton least squares (torch lstsq)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
class Y3(ipm3.IPM3):
    def system(self, b, cl, flds=None, gauge_value=1.0, target=None, mu=None, forced=False):
        if self.couple_gamma: self.set_gamma(1.0/cl); flds = None
        if flds is None: flds = self.fields(b)
        E = self.residual(b, cl, flds); N, M = self.N, self.M
        F = torch.empty((N+1)*M + 2, device=self.dev)
        F[0:M] = b[0, :]
        F[M] = cl - 1.0/3.0 + self.psi_xy0(flds)
        F[M+1:(N+1)*M+1] = E[1:].reshape(-1)
        F[-1] = (self.rad.ext1_R @ b).mean() - gauge_value
        return F, E, flds
    def jacobian(self, b, cl, flds=None, batch=None, defect=False, forced=False):
        if self.couple_gamma: self.set_gamma(1.0/cl)
        if flds is None: flds = self.fields(b)
        N, M = self.N, self.M; nb = (N+1)*M
        J = torch.zeros(nb + 2, nb + 1, device=self.dev)
        if batch is None: batch = max(1, int(6e8 // ((N + 1) * self.M2 * 8 * 12)))
        for k0 in range(0, nb, batch):
            k1 = min(nb, k0 + batch)
            I = torch.zeros(k1 - k0, nb, device=self.dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            delta = I.reshape(k1 - k0, N + 1, M); dflds = self.fields(delta)
            dE = self.linearized(b, cl, delta, flds, dflds); dc = self.psi_xy0(dflds)
            J[M+1:nb+1, k0:k1] = dE[:, 1:, :].reshape(k1 - k0, -1).T
            J[M, k0:k1] = dc
        for j in range(M): J[j, j] = 1.0
        J[nb+1, 0:nb] = (self.rad.ext1_R.reshape(-1, 1).expand(N + 1, M) / M).reshape(-1)
        h = 1e-6*max(1.0, abs(cl))
        Fp, _, _ = self.system(b, cl + h, gauge_value=0.0); Fm, _, _ = self.system(b, cl - h, gauge_value=0.0); self.set_gamma(1.0/cl)
        J[:, nb] = (Fp - Fm)/(2*h)
        return J
def gn(mdl, b, cl, beta, maxit=60, log=None):
    N, M = mdl.N, mdl.M; nb = (N+1)*M
    F, E, flds = mdl.system(b, cl, gauge_value=beta); nF = F.norm().item()
    for it in range(maxit):
        J = mdl.jacobian(b, cl, flds)
        du = torch.linalg.lstsq(J, -F.unsqueeze(1)).solution.squeeze(1)
        lam = 1.0
        for _ in range(25):
            bn = b + lam*du[:nb].reshape(N+1, M); cln = cl + lam*du[nb].item()
            Fn, En, fn = mdl.system(bn, cln, gauge_value=beta); nFn = Fn.norm().item()
            if nFn < (1 - 1e-4*lam)*nF: break
            lam *= 0.5
        msg = f"  gn it {it}: |F|2 {nF:.3e} -> {nFn:.3e} lam={lam:.3g} cl={cln:.8f} c={mdl.psi_xy0(fn).item():+.6f} cl+c-1/3={cln+mdl.psi_xy0(fn).item()-1/3:+.2e}"
        if log: log.write(msg+"\n"); log.flush()
        b, cl, F, E, flds, nF = bn, cln, Fn, En, fn, nFn
        if nF < 1e-12 or lam < 1e-6: break
    sv = torch.linalg.svdvals(J)
    return b, cl, dict(nF=nF, F=F, E=E, flds=flds, smin=sv[-1].item(), it=it+1)
if __name__ == '__main__':
    N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]; cls0 = [float(v) for v in sys.argv[4].split(',')]; beta = float(sys.argv[5])
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# y3 branch exploratory N={N} M={M} cl0s={cls0} beta={beta} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
    for cl0 in cls0:
        mdl = Y3(N=N, M=M, L=1.0, gamma=1/cl0, device=dev, couple_gamma=True)
        th = mdl.ang.theta[None, :]; s2 = mdl.rad.s2R[:, None]
        for amp in [1.0, 4.0]:
            b0 = beta*s2*(amp*(1 - torch.cos(2*th))/2*(1 - s2) + s2)      # ~ amp beta r^2 sin^2 th at the centre, -> beta at infinity
            b, cl, info = gn(mdl, b0, cl0, beta, log=log)
            c = mdl.psi_xy0(info['flds']).item()
            # between-node residual
            tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); thg = mdl.ang.theta_np; thm = 0.5*(thg[:-1]+thg[1:])
            rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
            ev = mdl.evaluate(b, cl, info['flds'], RR, TT); q = (np.abs(ev['R'])/ev['Nf']).max()
            bhat = mdl.ang.to_coef(b, 'EE')
            rr = np.logspace(-3, -1, 5); tt = mdl.rad.t_of_r(rr); Pr = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (Pr @ bhat).cpu().numpy()
            msg = (f"y3 cl0={cl0} amp={amp}: GN |F|2={info['nF']:.2e} it={info['it']} smin={info['smin']:.1e} -> cl={cl:.8f} c={c:+.8f} cl+c-1/3={cl+c-1/3:+.2e} "
                   f"offgrid|R|/Nf={q:.1e} b range [{b.min().item():.3f},{b.max().item():.3f}] centre: b0/r^2 at r=1e-3,1e-2,1e-1: {bk[0,0]/1e-6:.3f} {bk[2,0]/1e-4:.3f} {bk[4,0]/1e-2:.3f}; b1/b0 at r=1e-2: {bk[2,1]/bk[2,0]:+.3f} (pure y^3 needs -1)")
            print(msg, flush=True); log.write(msg+"\n"); log.flush()
            torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=1.0, p=mdl.p, branch='y3'), f'runs/{tag}_cl0{cl0}_amp{amp}.pt')
