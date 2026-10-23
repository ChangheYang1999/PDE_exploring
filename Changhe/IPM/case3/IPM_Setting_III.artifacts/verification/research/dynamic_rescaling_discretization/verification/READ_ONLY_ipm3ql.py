"""
ipm3ql.py -- smooth-by-construction Q representation (ipm3q.py: r^2 = L^2 (1+t)/(1-t)^(2p), w = (1-t)/2,
b = sum_k sigma^k beta_k(t) cos 2k theta, beta_k a Chebyshev polynomial of degree N-k) with OVER-DETERMINED collocation:
the cos(2k theta) coefficient of the residual is required at ALL N+1 Radau nodes for every mode k (rows (N+1) M, the
mode-0 centre row replaced by the centre identity, plus the gauge row), unknowns sum_k (N+1-k) coefficients plus c_l (or mu).
Solved by Gauss-Newton with an SVD least-squares step.  Rows at nodes where sigma_i^k is tiny are then harmless (they are
satisfied by every smooth state up to roundoff), which removes the near-singular rows of the square version (NUM_REPORT 4J(c)).
Options: forcing width Lf separate from the grid length L (phi = (1 + r^2/Lf^2)^-2); unforced centre row either
(c_l - 1 + c) a_0 = 0 ('product') or the deflated (c_l - 1 + c) gK = 0 ('identity', excludes the spurious a_0 = 0 states).
"""
import sys, math, time, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import ipm3, ipm3s, ipm3q

torch.set_default_dtype(torch.float64)


class IPM3QL(ipm3q.IPM3Q):
    def __init__(self, N, M, L=1.0, gamma=0.5, p=None, device='cpu', Lf=None, centre='identity', M2=None, fine=False):
        super().__init__(N=N, M=M, L=L, gamma=gamma, p=p, device=device, M2=M2)
        self.Lf = L if Lf is None else Lf
        self.centre = centre
        self.fine = fine                      # collocate the residual at ALL M2 fine angles (angular oversampling; referee 4L(e)(iii))
        thf = self.angf.theta
        self.S_OO_ff = torch.sin(thf[:, None] * self.nf[None, :]); self.Sd_OO_ff = self.nf[None, :] * torch.cos(thf[:, None] * self.nf[None, :])

    # ---- residual on the fine angular grid (Radau radii x M2 angles) ----------------------------------------------
    def _fine_fields(self, flds):
        rad, angf = self.rad, self.angf
        Psi = flds['PsiC_R'] @ self.S_OO_ff.T; rPsi_r = flds['rPsiC_r'] @ self.S_OO_ff.T; Psi_th = flds['PsiC_R'] @ self.Sd_OO_ff.T
        v = rad.wR[:, None]; G = (2 + rad.omR)[:, None] * Psi + rPsi_r
        cosf, sinf = angf.cos[None, :], angf.sin[None, :]
        return dict(Ur_r=-v * Psi_th, Uth_r=v * G, U2y=v * (G * cosf / sinf - Psi_th))

    def _fine_b(self, beta):
        bk, bk_t = self.b_modes(beta, 'R')
        return bk @ self.C_f.T, self.rad.gR[:, None] * (bk_t @ self.C_f.T), bk @ self.Cd_f.T

    def residual_fine(self, beta, cl, flds):
        b, rb_r, b_th = self._fine_b(beta); F = self._fine_fields(flds); om = self.rad.omR[:, None]
        A0 = cl - 1 + F['U2y'] + (cl + F['Ur_r']) * om
        return (cl + F['Ur_r']) * rb_r + F['Uth_r'] * b_th + A0 * b

    def linearized_fine(self, beta, cl, delta, flds, dflds):
        b, rb_r, b_th = self._fine_b(beta); d, rd_r, d_th = self._fine_b(delta)
        F = self._fine_fields(flds); dF = self._fine_fields(dflds); om = self.rad.omR[:, None]
        A0 = cl - 1 + F['U2y'] + (cl + F['Ur_r']) * om
        return (cl + F['Ur_r']) * rd_r + dF['Ur_r'] * rb_r + F['Uth_r'] * d_th + dF['Uth_r'] * b_th + A0 * d + (dF['U2y'] + om * dF['Ur_r']) * b

    def forcing_shape(self):
        r = self.rad.rR
        return (1 + r ** 2 / self.Lf ** 2) ** (-2) / self.rad.wR

    def all_rows(self, E):
        if self.fine:
            return E.reshape(*E.shape[:-2], -1)                                  # pointwise rows at (N+1) x M2 fine angles; row 0 = (i=0, j=0)
        Ehat = E @ self.ang.A['EE'].T                                            # (..., N+1, M) cos coefficients
        return Ehat.reshape(*Ehat.shape[:-2], -1)                                # row index i*M + k; row 0 = (i=0, k=0)

    def nrows(self):
        return (self.N + 1) * (self.M2 if self.fine else self.M)

    def system(self, u, cl, gauge_value, mu=None, forced=False, flds=None):
        beta = self.beta_full(u)
        if flds is None:
            flds = self.fields(beta)
        E = self.residual_fine(beta, cl, flds) if self.fine else self.residual(beta, cl, flds)
        a0 = beta[0, 0]; c = self.psi_xy0(flds)
        if forced:
            E = E - mu * self.forcing_shape()[:, None]
        R = self.all_rows(E).clone()
        if forced:
            R[0] = (cl - 1 + c) * a0 - mu
        elif self.centre == 'identity':
            R[0] = (cl - 1 + c) * gauge_value
        elif self.centre == 'y3':
            R[0] = a0 * gauge_value                                               # secondary branch: rho_y(0) = 0 imposed (y^3-leading)
        elif self.centre == 'y3id':
            R[0] = (3 * (cl + c) - 1) * gauge_value                               # secondary branch, shift 3: the y^3 origin identity 3(c_l + c) = 1 imposed; a0 = 0 then follows from the rows ((c_l + c - 1) a0 = 0 with c_l + c - 1 = -2/3)
        else:
            R[0] = (cl - 1 + c) * a0
        g = self.gauge_row(beta, gauge_value)
        return torch.cat([R, g.unsqueeze(0)]), E, flds

    def jacobian(self, u, cl, gauge_value, mu=None, forced=False, flds=None, batch=None):
        beta = self.beta_full(u)
        if flds is None:
            flds = self.fields(beta)
        nu = self.nu; nr = self.nrows()
        J = torch.zeros(nr + 1, nu + 1, device=self.dev)
        if batch is None:
            batch = max(1, int(6e8 // ((self.N + 1) * self.M2 * 8 * 12)))
        c0 = self.psi_xy0(flds); a0 = beta[0, 0]
        for k0 in range(0, nu, batch):
            k1 = min(nu, k0 + batch)
            I = torch.zeros(k1 - k0, nu, device=self.dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            dbeta = self.beta_full(I)
            dflds = self.fields(dbeta)
            dE = self.linearized_fine(beta, cl, dbeta, flds, dflds) if self.fine else self.linearized(beta, cl, dbeta, flds, dflds)
            dR = self.all_rows(dE)                                                # (B, nr)
            dc = self.psi_xy0(dflds)
            if self.centre == 'y3' and not forced:
                dR[:, 0] = dbeta[:, 0, 0] * gauge_value
            elif self.centre == 'y3id' and not forced:
                dR[:, 0] = 3 * dc * gauge_value
            elif forced or self.centre != 'identity':
                dR[:, 0] = dc * a0 + (cl - 1 + c0) * dbeta[:, 0, 0]
            else:
                dR[:, 0] = dc * gauge_value
            J[:nr, k0:k1] = dR.T
            bk1 = (self.rad.ext1_R @ dbeta.permute(1, 0, 2).reshape(self.N + 1, -1)).reshape(k1 - k0, self.M)
            J[nr, k0:k1] = (bk1 * torch.cos(math.pi * self.kk)[None, :]).sum(1)
        if forced:
            J[:nr, nu] = -self.all_rows(self.forcing_shape()[:, None].expand(self.N + 1, self.M2 if self.fine else self.M))
            J[0, nu] = -1.0
        else:
            b, rb_r, b_th = self._fine_b(beta)[:3] if self.fine else self.b_values(beta)
            dEc = rb_r + (1 + self.rad.omR)[:, None] * b
            J[:nr, nu] = self.all_rows(dEc)
            J[0, nu] = gauge_value if self.centre == 'identity' else (0.0 if self.centre == 'y3' else (3 * gauge_value if self.centre == 'y3id' else a0))
        return J

    def gn(self, u, cl, gauge_value, mu=None, forced=False, maxit=60, tol=1e-12, log=None, verbose=False, rcond=1e-13):
        """Gauss-Newton with SVD least-squares steps and backtracking on |F|_2.  Returns the last Jacobian's singular values."""
        F, E, flds = self.system(u, cl, gauge_value, mu, forced); nF = F.norm().item(); hist = []
        S = None
        for it in range(maxit):
            J = self.jacobian(u, cl, gauge_value, mu, forced, flds)
            U, S, Vh = torch.linalg.svd(J, full_matrices=False)
            coef = (U.T @ (-F)) / S
            coef[S < rcond * S[0]] = 0.0
            du = Vh.T @ coef
            lam = 1.0; accepted = False
            for _ in range(30):
                un = u + lam * du[:-1]
                cln, mun = (cl, mu + lam * du[-1].item()) if forced else (cl + lam * du[-1].item(), mu)
                if cln <= 1.0:
                    lam *= 0.5; continue
                Fn, En, fn = self.system(un, cln, gauge_value, mun, forced); nFn = Fn.norm().item()
                if nFn < (1 - 1e-4 * lam) * nF:
                    accepted = True; break
                lam *= 0.5
            if not accepted:
                if log: log.write(f"  ql-gn it {it}: LINE SEARCH FAILED (no decrease down to lam={lam:.2e}); keeping the last accepted state\n"); log.flush()
                break
            msg = (f"  ql-gn it {it}: |F|2 {nF:.3e} -> {nFn:.3e} (max {Fn.abs().max().item():.2e}) lam={lam:.3g} cl={cln:.10f} mu={mun} "
                   f"a0={self.beta_full(un)[0,0].item():.8f} smin={S[-1].item():.2e} smax={S[0].item():.2e}")
            if verbose: print(msg, flush=True)
            if log: log.write(msg + "\n"); log.flush()
            hist.append((nF, nFn, lam))
            u, cl, mu, F, E, flds, nF = un, cln, mun, Fn, En, fn, nFn
            if F.abs().max().item() < tol or lam < 1e-7:
                break
        return u, cl, mu, dict(F=F, E=E, flds=flds, nF=F.abs().max().item(), nF2=nF, S=S, its=it + 1, hist=hist)


def between_node(mdl, beta, cl, flds, mu=0.0):
    tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    rm = mdl.rad.rmap_np(tm); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(beta, cl, flds, RR, TT)
    phi = (1 + RR ** 2 / mdl.Lf ** 2) ** (-2)
    Rf = ev['R'] - mu * ev['y'] * phi
    q = np.abs(Rf) / ev['Nf']
    return [q[(RR >= lo) & (RR < hi)].max() if ((RR >= lo) & (RR < hi)).any() else float('nan') for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e30)]]


def cheb_tail(mdl, u):
    """max |coefficient| of the top 10 percent of the Chebyshev coefficients of mode 0 and mode 1, relative to the largest."""
    out = []
    for k in (0, 1):
        ck = u[mdl.offs[k]:mdl.offs[k + 1]].abs().cpu().numpy(); n = len(ck)
        out.append(ck[int(0.9 * n):].max() / max(ck.max(), 1e-300))
    return out
