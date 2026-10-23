"""
dr.py -- DYNAMIC RESCALING IN PSEUDO-TIME for IPM Setting III (lead 2026-10-21T05:16Z/05:30Z/05:58Z; verifier results 149, 151, 154),
in the smooth-by-construction Q basis of ipm3q/ipm3ql (rho = y w(t) b(t, theta), r^2 = L^2 sigma (1-t)^(-2P), sigma = (1+t)/2,
w = (1-t)/2, b = sum_k sigma^k beta_k(t) cos 2k theta, beta_k a Chebyshev polynomial of degree N-k with coefficients u_k; P = 1/(1-gamma),
gamma = far-field exponent).

Equation (DR):   d_tau rho = c_w rho - (c_x X + U[rho]) . grad rho,   U the canonical full-plane velocity (modal Green function).
With a FIXED map and weight this is the field equation   b_tau = -E_{c_x}[b] + (c_w - 1) b,   E_c := [(c X + U).grad rho - rho]/(y w)
(= residual_fine(beta, c, flds) of ipm3ql; verifier result 151 confirmed the sign and the form).
Slope normalisation (lead 05:16Z (2)):  d_tau rho_y(0) = (c_w - c_x - c) rho_y(0), c = psi_xy(0) from the canonical inverse at every stage;
holding rho_y(0) fixed means c_w = c_x + c.
Variant (A) (fixed target C = c_l*): c_x = C c_w  =>  c_w = -c/(C - 1) (positive iff c < 0), map exponent gamma = 1/C fixed (no moving map).
Steady state with c_w > 0: rho* = rho/c_w is an exact profile with c_l* = C and a0* = rho_y(0)/c_w; its residual is R* = -rho_tau/c_w^2.
Variant (B) (free c_l*, fixed cubic jet e): c_w = -f/(2e), c_x = c_w - c (verifier 149); implemented as an option (map NOT rebuilt:
with a fixed map the far-field exponent 1/C_map differs from 1/c_l* and the far field cannot be steady; see the report).
Coefficient update (verifier 151): F = -E + (c_w - 1) b is a FIELD derivative; project angularly (fine grid, truncation to M cos modes),
then per mode k fit the Chebyshev coefficients of beta_k' by least squares in the MODE-VALUE space, min || diag(sigma^k) V_k u_k' - F_k ||
over all N+1 Radau nodes (proj='ls'; rows with tiny sigma^k are harmless), or by the square collocation at the N+1-k outer nodes
(proj='sq'; division by sigma^k, ill-conditioned for large k, kept for comparison).
Time stepping: explicit RK4 with the step set from the spectral radius of the analytic Jacobian of the projected right-hand side
(recomputed periodically), or fixed dtau.  Logged against tau: c, c_w, c_x, c_l* = c_x/c_w, a0* = a0/c_w, node norms of b_tau and rho_tau on
compact sets r <= R, centre jets, far-field trace coefficients (gauge conservation), the sin 3theta tail coefficient b3 against the law of
result 154, the physical-time integral int_0^tau exp(-int_0^s (c_x - c_w)) ds, and the sampled between-node |R*|/N_f* of rho* (discrete inverse;
canonical re-evaluation by the verifier).
"""
import sys, math, time, json, numpy as np, torch
sys.path.insert(0, 'numerics/src')
import ipm3, ipm3s, ipm3q, ipm3ql
torch.set_default_dtype(torch.float64)
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


class DR(ipm3ql.IPM3QL):
    def __init__(self, N, M, C, L=1.0, device='cuda', M2=None, proj='ls', rcond=1e-13, variant='A', e_ref=None):
        M2 = 3 * M if M2 is None else M2
        super().__init__(N=N, M=M, L=L, gamma=1.0 / C, device=device, Lf=L, centre='identity', M2=M2, fine=True)
        self.C = float(C); self.variant = variant; self.e_ref = e_ref; self.proj_kind = proj
        sig = self.rad.sigR
        self.Proj = []
        for k in range(M):
            A = (sig[:, None] ** k) * self.Ext[k]                                  # (N+1, N+1-k): coefficients -> mode values b_k = sigma^k beta_k
            if proj == 'ls':
                U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ > rcond * S_[0]
                P = Vh_[keep].T @ ((1.0 / S_[keep])[:, None] * U_[:, keep].T)
            else:
                P = torch.zeros(N + 1 - k, N + 1, device=self.dev); P[:, k:] = torch.linalg.inv(A[k:, :])
            self.Proj.append(P)
        self.Af = self.angf.A['EE'][:M, :]                                         # fine values -> first M cos(2k theta) coefficients
        # centre and far-field extraction from Chebyshev coefficients
        j = torch.arange(N + 1, dtype=torch.float64, device=self.dev)
        self.Tm1 = torch.cos(math.pi * j)                                           # T_j(-1) = (-1)^j
        self.dTm1 = -torch.cos(math.pi * j) * j ** 2                                # T_j'(-1) = (-1)^(j+1) j^2
        self.T1 = torch.ones(N + 1, device=self.dev); self.dT1 = j ** 2             # T_j(1) = 1, T_j'(1) = j^2
        self.ellc2 = L ** 2 * 2.0 ** (-2 * self.p)                                  # r^2 = L^2 sigma (1-t)^(-2P) ~ L^2 2^(-2P) sigma at t = -1: sigma = r^2/ell_c^2 + O(r^4), ell_c = L 2^(-P) (verifier 145)
        self.delta = 1.0 - 1.0 / self.C                                             # 1 - gamma
        self.Dff = 0.5 * L ** self.delta                                            # rho ~ D r^gamma sum_k beta_k(1) sin th cos 2k th at infinity

    # ---- coefficient access ---------------------------------------------------------------------------------------------------------------
    def coef(self, u, k):
        return u[self.offs[k]:self.offs[k + 1]]

    def jets(self, u):
        """a0 = rho_y(0); cubic coefficients b_c (x^2 y), e_c (y^3) of rho = y [a0 + b_c x^2 + e_c y^2 + ...] (x^2 y and y^3 coefficients);
        rho = y w b, w = 1 - sigma, b = beta_0(t) + sigma beta_1(t) cos 2th + ..., beta_0(t) = a0 + 2 sigma beta_0'(-1) + ..., sigma = r^2/ell_c^2."""
        n0 = self.nk[0]; n1 = self.nk[1]
        c0 = self.coef(u, 0); c1 = self.coef(u, 1)
        a0 = (c0 * self.Tm1[:n0]).sum(); d0 = (c0 * self.dTm1[:n0]).sum(); b1 = (c1 * self.Tm1[:n1]).sum()
        bc = (2 * d0 - a0 + b1) / self.ellc2; ec = (2 * d0 - a0 - b1) / self.ellc2
        return a0, bc, ec

    def farfield(self, u):
        """beta_k(1), beta_k'(1) for k = 0..2; trace coefficients Theta = D sum_k beta_k(1) sin th cos 2k th: A1 = [sin th], A3 = [sin 3th];
        K = D sum_k (-1)^k beta_k(1) (y-axis amplitude); b3 = -D^2 (H_1 - H_2)/2, H_k = (k + delta/2) beta_k(1) + 2 beta_k'(1) (verifier 154)."""
        bk1 = []; dbk1 = []
        for k in range(min(3, self.M)):
            ck = self.coef(u, k); n = self.nk[k]
            bk1.append((ck * self.T1[:n]).sum()); dbk1.append((ck * self.dT1[:n]).sum())
        D = self.Dff
        A1 = D * (bk1[0] - 0.5 * bk1[1]); A3 = D * 0.5 * (bk1[1] - bk1[2])
        Kall = D * sum(((-1) ** k) * (self.coef(u, k) * self.T1[:self.nk[k]]).sum() for k in range(self.M))
        H = [(k + self.delta / 2) * bk1[k] + 2 * dbk1[k] for k in range(3)]
        b3 = -D ** 2 * (H[1] - H[2]) / 2
        return dict(A1=A1, A3=A3, K=Kall, b3=b3, bk1=bk1, dbk1=dbk1)

    # ---- rates ----------------------------------------------------------------------------------------------------------------------------
    def rates(self, c, u=None, flds=None):
        if self.variant == 'A':
            cw = -c / (self.C - 1.0); return cw, self.C * cw
        # variant B: fixed cubic jet e: e_tau = -2 c_w e - f (verifier 149; psi = c xy + d x^3 y + f x y^3 + ...), so c_w = -f/(2e), c_x = c_w - c
        a0, bc, ec = self.jets(u); f = self.stream_cubic(flds)[1]
        cw = -f / (2 * ec); return cw, cw - c

    def stream_cubic(self, flds):
        """d, f in psi = c x y + d x^3 y + f x y^3 + O(r^6) from the Lobatto mode functions: psi = r^2 w Psi~, Psi~ = sum_n PsiC_n(t) sin n th;
        r^2 sin 2th = 2xy, r^4 sin 4th = 4 x^3 y - 4 x y^3, r^4 sin 2th = 2 xy (x^2 + y^2); w = 1 - sigma, sigma = r^2/ell_c^2;
        PsiC_2(t) = P2 + 2 sigma P2', PsiC_4 = 2 sigma P4' (P4(-1) = 0)  =>  psi = 2xy P2 + (r^2/ell_c^2)[2xy (2P2' - P2) + 8 P4' (x^3 y - x y^3)/r^2 ... ]"""
        PsiC = flds['PsiC']                                                         # (N+1, M2) Lobatto values, modes n = 2, 4, ...
        DL = self.rad.DL
        P2 = PsiC[0, 0]; P2t = (DL[0, :] @ PsiC[:, 0]); P4t = (DL[0, :] @ PsiC[:, 1])      # d/dt at t = -1; d/dsigma = 2 d/dt
        # psi = r^2 (1 - s) [ (P2 + 2 s P2t) sin 2th + 2 s P4t sin 4th ],  s = r^2/ell_c^2
        #     = 2xy P2 + s r^2 [ (2 P2t - P2) sin 2th + 2 P4t sin 4th ]
        #     = 2xy P2 + (1/ell_c^2) [ (2 P2t - P2) 2xy (x^2 + y^2) + 2 P4t (4 x^3 y - 4 x y^3) ]
        d = (2 * (2 * P2t - P2) + 8 * P4t) / self.ellc2; f = (2 * (2 * P2t - P2) - 8 * P4t) / self.ellc2
        return d, f

    def exterior_moments(self, u, radii=(0.0, 1.0, 10.0, 100.0), ng=400):
        """I(R) = int_R^inf f_3(s) s^-2 ds, f_3 = sin 3theta Fourier coefficient of rho (the strain induced inside r < R by the density outside R;
        verifier 160; lead 06:09Z).  rho = r w sin th sum_k b_k cos 2k th, b_k = sigma^k beta_k, so f_3 = r w (b_1 - b_2)/2; with dr/r = Q dt/(1 - t^2) and
        w = (1-t)/2:  I(R) = int_{t(R)}^1 (b_1 - b_2) Q/(4 (1 + t)) dt  (Gauss-Legendre on [t(R), 1] with the Chebyshev representation).
        The full moment I(0) satisfies the strain identity c = -a0/4 + I(0) (lead's ANALYSIS; checked below)."""
        xg, wg = np.polynomial.legendre.leggauss(ng); xg = torch.tensor(xg, device=self.dev); wg = torch.tensor(wg, device=self.dev)
        out = {}
        for R in radii:
            tR = -1.0 if R <= 0 else float(self.rad.t_of_r(np.array([R]))[0])
            t = 0.5 * (1 - tR) * xg + 0.5 * (1 + tR); jac = 0.5 * (1 - tR)
            acs = torch.arccos(torch.clamp(t, -1.0, 1.0))
            vals = []
            for k in (1, 2):
                ck = self.coef(u, k); n = self.nk[k]; V = torch.cos(acs[:, None] * torch.arange(n, device=self.dev, dtype=torch.float64)[None, :])
                vals.append(((1 + t) / 2) ** k * (V @ ck))
            Q = (1 - t) / 2 + self.p * (1 + t)
            out[R] = (jac * (wg * (vals[0] - vals[1]) * Q / (4 * (1 + t))).sum()).item()
        return out

    # ---- right-hand side -------------------------------------------------------------------------------------------------------------------
    def project(self, F):
        Fk = F @ self.Af.T                                                          # (..., N+1, M)
        return torch.cat([Fk[..., :, k] @ self.Proj[k].T for k in range(self.M)], -1)

    def rhs(self, u, want=False):
        beta = self.beta_full(u); flds = self.fields(beta); c = self.psi_xy0(flds)
        cw, cx = self.rates(c, u, flds)
        E = self.residual_fine(beta, cx, flds); b = self._fine_b(beta)[0]
        F = -E + (cw - 1.0) * b
        du = self.project(F)
        if want:
            return du, dict(beta=beta, flds=flds, c=c, cw=cw, cx=cx, E=E, F=F, b=b)
        return du

    def jacobian_dr(self, u, batch=None):
        """analytic Jacobian of rhs(u) with respect to u (variant A)."""
        beta = self.beta_full(u); flds = self.fields(beta); c = self.psi_xy0(flds); cw, cx = self.rates(c, u, flds)
        b, rb_r, b_th = self._fine_b(beta); om = self.rad.omR[:, None]
        dEc = rb_r + (1 + om) * b                                                   # dE/dc_x at fixed b
        nu = self.nu; J = torch.zeros(nu, nu, device=self.dev)
        if batch is None: batch = max(1, int(4e8 // ((self.N + 1) * self.M2 * 8 * 12)))
        for k0 in range(0, nu, batch):
            k1 = min(nu, k0 + batch)
            I = torch.zeros(k1 - k0, nu, device=self.dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            dbeta = self.beta_full(I); dflds = self.fields(dbeta)
            dE = self.linearized_fine(beta, cx, dbeta, flds, dflds)                 # (B, N+1, M2) at fixed c_x
            dc = self.psi_xy0(dflds)                                                # (B,)
            if self.variant == 'A':
                dcw = -dc / (self.C - 1.0); dcx = self.C * dcw
            else:
                raise NotImplementedError('variant B Jacobian: use finite differences')
            db = self._fine_b(dbeta)[0]
            dF = -dE - dcx[:, None, None] * dEc[None] + (cw - 1.0) * db + dcw[:, None, None] * b[None]
            J[:, k0:k1] = self.project(dF).T
        return J

    def jacobian_fd(self, u, h=1e-7):
        nu = self.nu; J = torch.zeros(nu, nu, device=self.dev); F0 = self.rhs(u)
        for i in range(nu):
            up = u.clone(); up[i] += h; J[:, i] = (self.rhs(up) - F0) / h
        return J

    # ---- diagnostics -----------------------------------------------------------------------------------------------------------------------
    def norms(self, info, radii=(1.0, 10.0, 100.0)):
        """node norms of rho_tau = y w F and of rho on r <= R (fine angular grid), plus global; returns dict."""
        r = self.rad.rR; w = self.rad.wR; sinf = self.angf.sin
        rho_tau = (r * w)[:, None] * sinf[None, :] * info['F']; rho = (r * w)[:, None] * sinf[None, :] * info['b']
        out = {}
        for R in list(radii) + [float('inf')]:
            m = r <= R
            out[R] = (rho_tau[m].abs().max().item(), rho[m].abs().max().item(), info['F'][m].abs().max().item())
        return out

    def sampled_residual(self, info):
        """between-node |R*|/N_f* and |R*| of rho* = rho/c_w with c_l* = C (discrete inverse): fields are linear in beta."""
        cw = info['cw'].item() if torch.is_tensor(info['cw']) else info['cw']
        beta = info['beta'] / cw; flds = {k: v / cw for k, v in info['flds'].items()}
        tR = self.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = self.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
        rm = self.rad.rmap_np(tm); RR, TT = np.meshgrid(rm, thm, indexing='ij')
        ev = self.evaluate(beta, self.C, flds, RR, TT)
        q = np.abs(ev['R']) / ev['Nf']; qv = np.abs(ev['R']) / ev['Nv']
        bins = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e30)]
        out = []
        for lo, hi in bins:
            m = (RR >= lo) & (RR < hi)
            out.append((q[m].max(), qv[m].max(), np.abs(ev['R'][m]).max()) if m.any() else (float('nan'),) * 3)
        return out


def run(args):
    kw = dict(a.split('=', 1) for a in args if '=' in a)
    N = int(kw.get('N', 64)); M = int(kw.get('M', 16)); C = float(kw.get('C', 3.0)); L = float(kw.get('L', 1.0)); tag = kw['tag']
    tau_end = float(kw.get('tau_end', 50.0)); dt_user = float(kw.get('dtau', 0)); log_every = float(kw.get('log_every', 0.5))
    save_every = float(kw.get('save_every', 5.0)); jac_every = int(kw.get('jac_every', 2000)); proj = kw.get('proj', 'ls'); dev = kw.get('dev', 'cuda')
    safety = float(kw.get('safety', 0.7)); a0 = float(kw.get('a0', 1.0)); start = kw.get('start', None); M2 = int(kw['M2']) if 'M2' in kw else None
    mdl = DR(N, M, C, L=L, device=dev, M2=M2, proj=proj)
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# dr.py {now()} {kw}\n"); log.flush()
    if start is None:
        beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = a0; u = mdl.beta_to_u(beta0); tau = 0.0; Tphys = 0.0; b3_pred = 0.0
        log.write(f"# constant start b = {a0} (rho = {a0} y w(r)), L = {L}, far-field exponent gamma = 1/C = {1/C:.6f}\n")
    else:
        st = torch.load(start, weights_only=False)
        if 'tau' in st and st['N'] == N and st['M'] == M and abs(st.get('C', C) - C) < 1e-14:
            u = st['u'].to(dev); tau = st['tau']; Tphys = st.get('Tphys', 0.0); b3_pred = st.get('b3_pred', 0.0)
            log.write(f"# resumed from {start} at tau = {tau}\n")
        else:
            import q_free
            qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=st.get('L', 1.0), gamma=1 / st['cl'], device=dev, Lf=st.get('Lf', 1.0))
            beta0, u = q_free.regrid_fit(qo, st['beta'].to(dev), mdl); tau = 0.0; Tphys = 0.0; b3_pred = 0.0
            log.write(f"# start regridded from {start} (cl {st['cl']}, {st['N']}x{st['M']}) to {N}x{M} with map exponent 1/C\n")
    def spectral_radius(u):
        J = mdl.jacobian_dr(u); ev = torch.linalg.eigvals(J)
        re = ev.real; im = ev.imag.abs()
        rad = ev.abs().max().item(); remax = re.max().item()
        # RK4 stability: |lambda| dtau <= ~2.8 on the real axis, 2.83 on the imaginary; use 2.5
        return rad, remax, ev
    rad, remax, ev = spectral_radius(u)
    dtau = dt_user if dt_user > 0 else safety * 2.5 / rad
    log.write(f"# tau {tau:.4f}: Jacobian spectral radius {rad:.4e}, max Re {remax:+.4e}, dtau {dtau:.4e}\n"); log.flush()
    hdr = ("#   tau        c           c_w         c_x       a0*=a0/cw   |rho_tau|inf(r<=1,10,100,all)         |b_tau|inf   b_c/a0     e_c/a0    "
           "A1        A3        K         b3        b3_pred   Tphys   | a_tau      b_tau/a0    e_tau/a0    I_1        I_10       I_100      I_0-(c+a0/4)")
    log.write(hdr + "\n"); log.flush()
    du, info = mdl.rhs(u, want=True)
    next_log = tau; next_save = tau; step = 0; t0 = time.time(); last_u = u.clone(); last_tau = tau
    rate_hist = []; nhalf = 0; stopped_cw = False
    while tau < tau_end + 1e-12:
        if tau >= next_log - 1e-12:
            a0v, bc, ec = mdl.jets(u); ff = mdl.farfield(u); nm = mdl.norms(info)
            cw = info['cw'].item(); cx = info['cx'].item(); c = info['c'].item()
            msg = (f"{tau:9.4f} {c:+.8f} {cw:+.8f} {cx:+.8f} {a0v.item()/cw:+.6e} "
                   f"{nm[1.0][0]:.3e} {nm[10.0][0]:.3e} {nm[100.0][0]:.3e} {nm[float('inf')][0]:.3e}  {nm[float('inf')][2]:.3e} "
                   f"{(bc/a0v).item():+.5e} {(ec/a0v).item():+.5e} {ff['A1'].item():+.6f} {ff['A3'].item():+.3e} {ff['K'].item():+.6f} "
                   f"{ff['b3'].item():+.5e} {b3_pred:+.5e} {Tphys:.4e}")
            at, btt, ett = mdl.jets(du); Im = mdl.exterior_moments(u)
            msg += (f" | {at.item():+.2e} {(btt/a0v).item():+.4e} {(ett/a0v).item():+.4e} {Im[1.0]:+.3e} {Im[10.0]:+.3e} {Im[100.0]:+.3e} {Im[0.0] - (c + a0v.item()/4):+.1e}")
            log.write(msg + "\n"); log.flush(); next_log += log_every
        if tau >= next_save - 1e-12:
            sr = mdl.sampled_residual(info)
            log.write(f"#  tau {tau:.4f} sampled between-node of rho* (discrete inverse): |R*|/Nf [<.1 .1-1 1-100 >100] = " + " ".join(f"{s[0]:.2e}" for s in sr)
                      + " ; |R*|/Nv = " + " ".join(f"{s[1]:.2e}" for s in sr) + " ; |R*| = " + " ".join(f"{s[2]:.2e}" for s in sr)
                      + f" ; wall {time.time()-t0:.0f}s steps {step}\n"); log.flush()
            torch.save(dict(u=u.cpu(), beta=info['beta'].cpu(), cl=C, C=C, cw=info['cw'].item(), cx=info['cx'].item(), c=info['c'].item(), tau=tau, Tphys=Tphys,
                            b3_pred=b3_pred, N=N, M=M, L=L, gamma=1 / C, p=mdl.p, rep='DR-A', proj=proj, M2=mdl.M2, dtau=dtau, step=step, sampled=sr),
                       f'runs/{tag}_tau{tau:08.3f}.pt'.replace(' ', '0'))
            torch.save(dict(u=u.cpu(), beta=info['beta'].cpu(), cl=C, C=C, cw=info['cw'].item(), cx=info['cx'].item(), c=info['c'].item(), tau=tau, Tphys=Tphys,
                            b3_pred=b3_pred, N=N, M=M, L=L, gamma=1 / C, p=mdl.p, rep='DR-A', proj=proj, M2=mdl.M2, dtau=dtau, step=step, sampled=sr),
                       f'runs/{tag}_last.pt')
            next_save += save_every
        if tau >= tau_end - 1e-12: break
        # RK4 step
        k1 = du
        k2 = mdl.rhs(u + 0.5 * dtau * k1); k3 = mdl.rhs(u + 0.5 * dtau * k2); k4 = mdl.rhs(u + dtau * k3)
        un = u + dtau / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        dun, infon = mdl.rhs(un, want=True)
        if not torch.isfinite(dun).all() or dun.abs().max().item() > 1e3 * max(1.0, du.abs().max().item()):
            nhalf += 1
            log.write(f"# tau {tau:.4f}: blow-up detected (|du| {dun.abs().max().item():.3e}); halving dtau {dtau:.3e} -> {dtau/2:.3e} and restoring the last checkpoint (halving {nhalf})\n"); log.flush()
            dtau *= 0.5; u = last_u.clone(); tau = last_tau; du, info = mdl.rhs(u, want=True)
            if dtau < 1e-9 or nhalf > 6: log.write("# repeated blow-up: stop\n"); break
            continue
        if infon['cw'].item() <= 0.0:
            log.write(f"# tau {tau+dtau:.4f}: c_w = {infon['cw'].item():+.6e} <= 0 (c = {infon['c'].item():+.6e}): STOP (lead 05:30Z rule: record and stop); the state before the crossing is saved as {tag}_last.pt and {tag}_cw0.pt\n"); log.flush()
            torch.save(dict(u=u.cpu(), beta=info['beta'].cpu(), cl=C, C=C, cw=info['cw'].item(), cx=info['cx'].item(), c=info['c'].item(), tau=tau, Tphys=Tphys,
                            b3_pred=b3_pred, N=N, M=M, L=L, gamma=1 / C, p=mdl.p, rep='DR-A', proj=proj, M2=mdl.M2, dtau=dtau, step=step), f'runs/{tag}_cw0.pt')
            stopped_cw = True
            break
        # physical time and b3 law (trapezoid)
        cw0, cx0 = info['cw'].item(), info['cx'].item(); cw1, cx1 = infon['cw'].item(), infon['cx'].item()
        gap = 0.5 * ((cx0 - cw0) + (cx1 - cw1))
        rate_hist.append(gap * dtau); Tphys += dtau * math.exp(-sum(rate_hist))  # exp(-int_0^tau (c_x - c_w))
        ff0 = mdl.farfield(u); A1 = ff0['A1'].item(); gam = 1 / C
        Qsrc = A1 ** 2 * (1 - gam) / (4 * (gam + 3)); lam = (C - 1) * 0.5 * (cw0 + cw1)
        b3_pred = (b3_pred + dtau * Qsrc + 0.5 * dtau * lam * b3_pred) / (1 - 0.5 * dtau * lam)
        u, du, info = un, dun, infon; tau += dtau; step += 1
        if step % 200 == 0: last_u = u.clone(); last_tau = tau
        if step % jac_every == 0 and dt_user == 0:
            rad, remax, ev = spectral_radius(u); dnew = safety * 2.5 / rad
            log.write(f"# tau {tau:.4f}: Jacobian spectral radius {rad:.4e}, max Re {remax:+.4e} (count Re > 0: {(ev.real > 1e-10).sum().item()}), dtau {dtau:.4e} -> {dnew:.4e}\n"); log.flush()
            dtau = dnew
    a0v, bc, ec = mdl.jets(u); ff = mdl.farfield(u); nm = mdl.norms(info); cw = info['cw'].item(); cx = info['cx'].item(); c = info['c'].item()
    log.write(f"# FINAL state tau {tau:.4f}: c {c:+.8e} c_w {cw:+.8e} c_x {cx:+.8e} a0* {a0v.item()/cw if cw != 0 else float('nan'):+.6e} b_c/a0 {(bc/a0v).item():+.5e} e_c/a0 {(ec/a0v).item():+.5e} "
              f"|rho_tau|inf(r<=1) {nm[1.0][0]:.3e} K {ff['K'].item():+.6f} b3 {ff['b3'].item():+.5e} (law {b3_pred:+.5e}) Tphys {Tphys:.4e} stopped_at_cw0 {stopped_cw}\n")
    rad, remax, ev = spectral_radius(u)
    npos = (ev.real > 1e-10).sum().item()
    log.write(f"# END tau {tau:.4f} steps {step} wall {time.time()-t0:.0f}s; final Jacobian: spectral radius {rad:.4e}, max Re {remax:+.4e}, eigenvalues with Re > 1e-10: {npos}\n")
    top = ev[torch.argsort(-ev.real)][:8]
    log.write("# leading eigenvalues (by real part): " + " ".join(f"{z.real.item():+.4e}{z.imag.item():+.4e}j" for z in top) + "\n"); log.flush()
    return mdl, u, info


if __name__ == '__main__':
    run(sys.argv[1:])
