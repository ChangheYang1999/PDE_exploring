"""
ipm3q.py -- smooth-by-construction representation with MODE-DEPENDENT collocation (lead's 15:56Z item 6).

Uses the IPM3S machinery (r^2 = L^2 (1+t)/(1-t)^(2p), w = (1-t)/2, b = sum_k sigma^k beta_k(t) cos 2k theta, sigma = (1+t)/2),
but the unknowns of angular mode k are the values of beta_k at the N+1-k OUTER Radau nodes t_k..t_N (a polynomial of degree
N-k); beta_k at the k inner nodes is the polynomial extrapolation (irrelevant there since sigma^k ~ 0).  The equations of mode
k are the cos(2k theta) coefficients E_k(t_i) of the residual E (exact angular transform of the grid residual) collocated at
the same outer nodes i >= k (for k = 0 at i = 1..N, with the centre identity (c_l - 1 + c) beta_0(-1) = 0 as the i = 0 row).
Plus the gauge row (y-axis far-field value b(1, pi/2) = sum_k (-1)^k beta_k(1) = gauge_value).  Square: unknowns
sum_k (N+1-k) + c_l, rows sum_k (N+1-k) + 1.  Forced mode: extra unknown mu, forcing mu y phi with phi/w = ((1-t)/2)^3,
and c_l fixed.
"""
import sys, math, time, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import ipm3, ipm3s
from ipm3 import interp_matrix

torch.set_default_dtype(torch.float64)


class IPM3Q(ipm3s.IPM3S):
    def __init__(self, N, M, L=1.0, gamma=0.5, p=None, device='cpu', M2=None):
        super().__init__(N=N, M=M, L=L, gamma=gamma, p=p, device=device, M2=M2)
        # extrapolation matrices: for mode k, values at outer nodes t_k..t_N -> values at all N+1 nodes
        tR = self.rad.tR_np
        self.Ext = []          # Chebyshev evaluation matrices: coefficients of degree N-k -> values at all N+1 nodes
        self.Pinv = []         # values at the N+1-k outer nodes -> coefficients (square inverse)
        self.nk = []
        acs = np.arccos(tR)
        for k in range(M):
            deg = N - k
            Vk = np.cos(np.outer(acs, np.arange(deg + 1)))                      # (N+1, N+1-k)
            self.Ext.append(torch.tensor(Vk, device=self.dev))
            self.Pinv.append(torch.tensor(np.linalg.inv(Vk[k:, :]), device=self.dev))   # outer-node values -> coefficients
            self.nk.append(N + 1 - k)
        self.nu = sum(self.nk)                                                   # number of beta unknowns
        self.offs = np.concatenate([[0], np.cumsum(self.nk)])

    def forcing_shape(self):
        """same forcing as ipm3.IPM3: phi = (1 + r^2/L^2)^-2, returned as phi/w on the Radau grid (w = (1-t)/2)."""
        r = self.rad.rR
        return (1 + r ** 2 / self.L ** 2) ** (-2) / self.rad.wR

    # ---- unknown vector <-> full beta array ----------------------------------------------------
    def beta_full(self, u):
        """u: (..., nu) -> beta (..., N+1, M).  The unknowns of mode k are the MODE VALUES b_k(t_i) = sigma_i^k beta_k(t_i)
        at the outer nodes i >= k (well scaled); beta_k = b_k / sigma^k there, extrapolated to the inner nodes."""
        cols = []
        for k in range(self.M):
            ck = u[..., self.offs[k]:self.offs[k + 1]]                            # Chebyshev coefficients of beta_k (degree N-k)
            cols.append(ck @ self.Ext[k].T)                                       # values at all nodes
        return torch.stack(cols, -1)

    def beta_to_u(self, beta):
        return torch.cat([beta[k:, k] @ self.Pinv[k].T for k in range(self.M)])

    # ---- residual in mode space, selected rows ------------------------------------------------
    def mode_rows(self, E):
        """E (..., N+1, M) grid residual -> selected mode-space rows (..., nu): mode k at nodes i >= k (k = 0: i >= 0,
        where the i = 0 entry is replaced by the caller)."""
        Ehat = E @ self.ang.A['EE'].T                                            # (..., N+1, M) cos coefficients
        return torch.cat([Ehat[..., k:, k] for k in range(self.M)], -1)

    def system(self, u, cl, gauge_value, mu=None, forced=False, flds=None):
        beta = self.beta_full(u)
        if flds is None:
            flds = self.fields(beta)
        E = self.residual(beta, cl, flds)
        a0 = beta[0, 0]
        c = self.psi_xy0(flds)
        if forced:
            E = E - mu * self.forcing_shape()[:, None]
        R = self.mode_rows(E)
        R = R.clone()
        R[0] = (cl - 1 + c) * a0 - (mu if forced else 0.0)                       # centre identity row (mode 0, node 0)
        g = self.gauge_row(beta, gauge_value)
        return torch.cat([R, g.unsqueeze(0)]), E, flds

    def jacobian(self, u, cl, gauge_value, mu=None, forced=False, flds=None, batch=None):
        beta = self.beta_full(u)
        if flds is None:
            flds = self.fields(beta)
        nu = self.nu
        J = torch.zeros(nu + 1, nu + 1, device=self.dev)
        if batch is None:
            batch = max(1, int(6e8 // ((self.N + 1) * self.M2 * 8 * 12)))
        c0 = self.psi_xy0(flds); a0 = beta[0, 0]
        for k0 in range(0, nu, batch):
            k1 = min(nu, k0 + batch)
            I = torch.zeros(k1 - k0, nu, device=self.dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            dbeta = self.beta_full(I)                                             # (B, N+1, M)
            dflds = self.fields(dbeta)
            dE = self.linearized(beta, cl, dbeta, flds, dflds)                     # (B, N+1, M)
            dR = self.mode_rows(dE)                                               # (B, nu)
            dc = self.psi_xy0(dflds)                                              # (B,)
            dR[:, 0] = dc * a0 + (cl - 1 + c0) * dbeta[:, 0, 0]
            J[:nu, k0:k1] = dR.T
            # gauge row: linear in beta
            bk1 = (self.rad.ext1_R @ dbeta.permute(1, 0, 2).reshape(self.N + 1, -1)).reshape(k1 - k0, self.M)   # beta_k(1)
            J[nu, k0:k1] = (bk1 * torch.cos(math.pi * self.kk)[None, :]).sum(1)
        if forced:
            # column for mu
            J[:nu, nu] = -self.mode_rows(self.forcing_shape()[:, None].expand(self.N + 1, self.M))
            J[0, nu] = -1.0
        else:
            # column for c_l (p fixed): explicit derivative of E wrt c_l
            b, rb_r, b_th = self.b_values(beta)
            dEc = rb_r + (1 + self.rad.omR)[:, None] * b
            J[:nu, nu] = self.mode_rows(dEc)
            J[0, nu] = a0
        return J

    def newton(self, u, cl, gauge_value, mu=None, forced=False, maxit=60, tol=1e-12, log=None, verbose=False):
        F, E, flds = self.system(u, cl, gauge_value, mu, forced); nF = F.abs().max().item()
        for it in range(maxit):
            J = self.jacobian(u, cl, gauge_value, mu, forced, flds)
            du = torch.linalg.solve(J, -F)
            lam = 1.0
            for _ in range(30):
                un = u + lam * du[:-1]
                cln, mun = (cl, mu + lam * du[-1].item()) if forced else (cl + lam * du[-1].item(), mu)
                Fn, En, fn = self.system(un, cln, gauge_value, mun, forced); nFn = Fn.abs().max().item()
                if nFn < (1 - 1e-4 * lam) * nF:
                    break
                lam *= 0.5
            msg = f"  q-newton it {it}: |F| {nF:.3e} -> {nFn:.3e} lam={lam:.3g} cl={cln:.10f} mu={mun} a0={self.beta_full(un)[0,0].item():.8f}"
            if verbose: print(msg, flush=True)
            if log: log.write(msg + "\n"); log.flush()
            u, cl, mu, F, E, flds, nF = un, cln, mun, Fn, En, fn, nFn
            if nF < tol or lam < 1e-7:
                break
        return u, cl, mu, dict(F=F, E=E, flds=flds, nF=nF, J=J, its=it + 1)


def between_node(mdl, beta, cl, flds, mu=0.0):
    tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    rm = mdl.rad.rmap_np(tm); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(beta, cl, flds, RR, TT)
    phi = (1 + RR ** 2 / mdl.L ** 2) ** (-2)
    Rf = ev['R'] - mu * ev['y'] * phi
    q = np.abs(Rf) / ev['Nf']
    return [q[(RR >= lo) & (RR < hi)].max() if ((RR >= lo) & (RR < hi)).any() else float('nan') for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e30)]]


if __name__ == '__main__':
    mode = sys.argv[1]; N = int(sys.argv[2]); M = int(sys.argv[3]); cl = float(sys.argv[4]); gK = float(sys.argv[5]); tag = sys.argv[6]
    dev = 'cuda'; log = open(f'runs/{tag}.log', 'a'); log.write(f"# ipm3q {mode} N={N} M={M} cl={cl} gK={gK} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
    mdl = IPM3Q(N=N, M=M, L=1.0, gamma=1 / cl, device=dev)
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = gK
    u0 = mdl.beta_to_u(beta0)
    if mode == 'forced':
        u, cl, mu, info = mdl.newton(u0, cl, gK, mu=0.0, forced=True, log=log)
        beta = mdl.beta_full(u); flds = info['flds']; c = mdl.psi_xy0(flds).item(); a0 = beta[0, 0].item()
        K, Lcan = mdl.K_of_state(beta, cl); og = between_node(mdl, beta, cl, flds, mu)
        sv = torch.linalg.svdvals(info['J'])
        msg = (f"Q forced N={N} M={M} cl={cl} gK={gK}: |F|={info['nF']:.1e} its={info['its']} smin={sv[-1].item():.1e} mu={mu:+.10f} a0={a0:.10f} c={c:+.10f} "
               f"Delta={cl+c-1:+.8f} K={K:.6f} Lcan={Lcan:.5g} between-node |R_f|/Nf [<.1,.1-1,1-100,>100]={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}")
    else:
        u, cl, mu, info = mdl.newton(u0, cl, gK, forced=False, log=log, maxit=80)
        beta = mdl.beta_full(u); flds = info['flds']; c = mdl.psi_xy0(flds).item(); a0 = beta[0, 0].item()
        K, Lcan = mdl.K_of_state(beta, cl); og = between_node(mdl, beta, cl, flds, 0.0)
        sv = torch.linalg.svdvals(info['J'])
        msg = (f"Q unforced N={N} M={M} start cl={sys.argv[4]} gK={gK}: |F|={info['nF']:.1e} its={info['its']} smin={sv[-1].item():.1e} -> cl={cl:.10f} a0={a0:.10f} c={c:+.10f} "
               f"cl+c-1={cl+c-1:+.1e} K={K:.6f} Lcan={Lcan:.5g} between-node |R|/Nf [<.1,.1-1,1-100,>100]={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}")
    print(msg, flush=True); log.write(msg + "\n")
    torch.save(dict(beta=beta.cpu(), cl=cl, mu=mu, gamma=1 / cl, N=N, M=M, L=1.0, p=mdl.p, rep='Q'), f'runs/{tag}.pt')
