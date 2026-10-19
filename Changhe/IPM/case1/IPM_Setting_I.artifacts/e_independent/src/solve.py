"""
solve.py -- Newton solver for the discretised Setting I system (see ipm1.py).

Unknowns: b on the Radau grid ((N+1) x M, flattened row-major) and c_l.
Equations:
  rows at t=-1 (r=0):     b(-1, theta_j) - 1 = 0        (normalisation a(0)=1 and continuity at the centre)
  rows at t_i, i=1..N:    E[b, c_l](t_i, theta_j) = 0   (the a-equation divided by w)
  last row:               3 c_l - 1 - c[b] = 0,  c = psi_xy(0) from the modal Green function (SPEC N1)
Homotopy (optional): E -> E - (1-eps) S0, identity -> identity - (1-eps) s0, where (S0, s0) are the residuals of the
starting point, so that eps=0 is solved exactly by the starting point and eps=1 is the true problem.
"""
import math, time
import numpy as np
import torch
import ipm1


class Newton:
    def __init__(self, mdl: 'ipm1.IPM1', chunk=2048, verbose=True):
        self.m = mdl
        self.N, self.M = mdl.N, mdl.M
        self.n = (self.N + 1) * self.M
        self.chunk = chunk
        self.verbose = verbose
        dev = mdl.dev
        rad, ang = mdl.rad, mdl.ang
        self.S = rad.SR if hasattr(rad, 'SR') else ((1 - rad.tR ** 2) / rad.QR)   # r d/dr = S d/dt (disk or compactified)
        I_M = torch.eye(self.M, device=dev)
        I_N = torch.eye(self.N + 1, device=dev)
        self.Dt_big = torch.kron(rad.DR, I_M)              # flattened radial derivative
        self.Dth_big = torch.kron(I_N, ang.Dth['EE'])      # flattened angular derivative (EE)
        self._linmaps()
        if hasattr(mdl, 'k_tail'):
            self._k_maps = mdl.k_tail

    def _linmaps(self):
        """Dense matrices of the linear maps b -> Ur/r, Uth/r, coefU (flattened), and the functional c[b]."""
        m, n = self.m, self.n
        dev = m.dev
        Lam = {k: torch.empty(n, n, device=dev) for k in ['Ur_over_r', 'Uth_over_r', 'coefU']}
        cvec = torch.empty(n, device=dev)
        t0 = time.time()
        for s in range(0, n, self.chunk):
            e = min(n, s + self.chunk)
            B = torch.zeros(e - s, n, device=dev)
            B[torch.arange(e - s), torch.arange(s, e)] = 1.0
            F = m.fields(B.reshape(e - s, self.N + 1, self.M))
            for k in Lam:
                Lam[k][:, s:e] = F[k].reshape(e - s, n).T
            cvec[s:e] = m.psi_xy0(F)
        self.Lam = Lam
        self.cvec = cvec
        if self.verbose:
            print(f"[Newton] linear maps built: n={n}, {time.time()-t0:.1f}s", flush=True)

    # -----------------------------------------------------------------------------------------
    def residual_full(self, b, cl, flds=None, hom=None):
        """Full residual vector (n+1,) incl. normalisation rows and identity row."""
        m = self.m
        if hasattr(m, 'k_tail'):
            m.k_tail = 1.0 / cl                     # disk closure: tail exponent consistent with the current c_l
            if abs(m.k_tail - getattr(self, '_k_maps', m.k_tail)) > 2e-3:
                self._linmaps(); self._k_maps = m.k_tail
        if flds is None:
            flds = m.fields(b)
        E = m.residual(b, cl, flds)                     # (N+1, M)
        c = m.psi_xy0(flds)
        ident = 3 * cl - 1 - c
        if hom is not None:
            eps, S0, s0 = hom[0], hom[1], hom[2]
            E = E - (1 - eps) * S0
            ident = ident - (1 - eps) * s0      # pass s0 = 0 to keep the identity exact along the path
        E = E.clone()
        E[0, :] = b[0, :] - 1.0
        return torch.cat([E.reshape(-1), ident.reshape(1)]), flds

    def jacobian(self, b, cl, flds):
        m, n = self.m, self.n
        dev = m.dev
        bf = b.reshape(-1)
        bt = (m.rad.DR @ b)
        Sbt = (self.S[:, None] * bt).reshape(-1)
        bth = m.ang.dtheta(b, 'EE').reshape(-1)
        Ur = flds['Ur_over_r'].reshape(-1)
        Uth = flds['Uth_over_r'].reshape(-1)
        om = m.omegaR[:, None].expand(self.N + 1, self.M).reshape(-1)
        A0 = cl * om + Ur * om + (3 * cl - 1) + flds['coefU'].reshape(-1)
        J = torch.empty(n + 1, n + 1, device=dev)
        Jb = ((cl + Ur) * self.S[:, None].expand(self.N + 1, self.M).reshape(-1))[:, None] * self.Dt_big
        Jb += Uth[:, None] * self.Dth_big
        Jb += torch.diag(A0)
        Jb += Sbt[:, None] * self.Lam['Ur_over_r']
        Jb += bth[:, None] * self.Lam['Uth_over_r']
        Jb += (bf * om)[:, None] * self.Lam['Ur_over_r'] + bf[:, None] * self.Lam['coefU']
        # normalisation rows (t=-1): first M rows
        Jb[:self.M, :] = 0.0
        Jb[torch.arange(self.M), torch.arange(self.M)] = 1.0
        J[:n, :n] = Jb
        if hasattr(m, 'k_tail'):
            # c_l column by central finite differences (tail exponent depends on c_l)
            h = 1e-6 * max(1.0, abs(cl))
            Fp, _ = self.residual_full(b, cl + h); Fm, _ = self.residual_full(b, cl - h)
            m.k_tail = 1.0 / cl
            J[:, n] = (Fp - Fm) / (2 * h)
            J[n, :n] = -self.cvec
            return J
        dcl = (Sbt + om * bf + 3 * bf)
        dcl[:self.M] = 0.0
        J[:n, n] = dcl
        J[n, :n] = -self.cvec
        J[n, n] = 3.0
        return J

    def solve(self, b, cl, hom=None, tol=1e-11, maxit=30, damp_min=1e-3, lm=0.0, log=None, fix_cl=False):
        """Newton with backtracking line search.  Returns (b, cl, info)."""
        m = self.m
        b = b.clone()
        F, flds = self.residual_full(b, cl, hom=hom)
        nz = (lambda v: v[:-1].abs().max().item()) if fix_cl else (lambda v: v.abs().max().item())
        nrm = nz(F)
        hist = [nrm]
        if self.verbose:
            print(f"[Newton] it 0  |F|_inf={nrm:.3e}  c_l={cl:.10f}", flush=True)
        for it in range(1, maxit + 1):
            if nrm < tol:
                break
            J = self.jacobian(b, cl, flds)
            if lm > 0:
                J += lm * torch.eye(J.shape[0], device=m.dev)
            try:
                if fix_cl:
                    d = torch.zeros_like(F)
                    d[:-1] = torch.linalg.solve(J[:-1, :-1], -F[:-1])
                else:
                    d = torch.linalg.solve(J, -F)
            except Exception as ex:
                print("[Newton] linear solve failed:", ex)
                return b, cl, dict(converged=False, hist=hist, reason='linsolve')
            db = d[:-1].reshape(self.N + 1, self.M)
            dcl = d[-1].item()
            alpha = 1.0
            while True:
                bn = b + alpha * db
                cln = cl + alpha * dcl
                Fn, fldsn = self.residual_full(bn, cln, hom=hom)
                nn = nz(Fn)
                if nn < nrm * (1 - 1e-4 * alpha) or alpha < damp_min:
                    break
                alpha *= 0.5
            b, cl, F, flds, nrm = bn, cln, Fn, fldsn, nn
            hist.append(nrm)
            if self.verbose:
                print(f"[Newton] it {it}  |F|_inf={nrm:.3e}  c_l={cl:.10f}  alpha={alpha:.3g}  |d|={d.abs().max().item():.2e}", flush=True)
            if log is not None:
                log.write(f"it {it} F {nrm:.6e} cl {cl:.12f} alpha {alpha}\n"); log.flush()
            if not math.isfinite(nrm):
                return b, cl, dict(converged=False, hist=hist, reason='nan')
        return b, cl, dict(converged=(nrm < tol), hist=hist, nrm=nrm)


def continuation(newton: Newton, b0, cl0, eps_list, tol=1e-11, maxit=30, verbose=True, keep_identity=False):
    """Homotopy from the starting point (b0, cl0) (exact solution at eps=0) to the true problem at eps=1."""
    m = newton.m
    F0, flds0 = newton.residual_full(b0, cl0)       # true residual of the start
    E0 = m.residual(b0, cl0, flds0)
    s0 = (3 * cl0 - 1 - m.psi_xy0(flds0))
    if keep_identity:
        s0 = s0 * 0.0
    S0 = E0.clone(); S0[0, :] = 0.0
    b, cl = b0.clone(), cl0
    results = []
    for eps in eps_list:
        b_try, cl_try, info = newton.solve(b, cl, hom=(eps, S0, s0), tol=tol, maxit=maxit)
        if verbose:
            Fh, fl = newton.residual_full(b_try, cl_try, hom=(eps, S0, s0))
            J = newton.jacobian(b_try, cl_try, fl)
            sv = torch.linalg.svdvals(J)
            print(f"[cont] eps={eps:.4f} converged={info['converged']} c_l={cl_try:.10f} |F|={info.get('nrm', float('nan')):.2e}"
                  f"  smin(J)={sv[-1].item():.3e} smax={sv[0].item():.3e}  max|b|={b_try.abs().max().item():.3f}  b(inf)max={(m.rad.ext1_R @ b_try).abs().max().item():.3f}", flush=True)
        results.append((eps, cl_try, info['converged'], info.get('nrm', float('nan'))))
        if not info['converged']:
            return b, cl, results, False
        b, cl = b_try, cl_try
    return b, cl, results, True


def arclength(newton: Newton, b0, cl0, eps0, S0, s0, ds=0.05, nsteps=200, eps_stop=1.0, tol=1e-10, maxit=25,
              amp_stop=1e4, verbose=True, log=None, ds_max=0.5, svd_every=1, save_at=None, save_fn=None):
    """
    Pseudo-arclength continuation in the homotopy parameter eps.  Unknown vector z = (b, c_l, eps).
    Equations: G(b, c_l; eps) = 0 (n+1 rows) and the arclength condition tau . (z - z_prev) - ds = 0.
    Returns list of (eps, c_l, max|b|, smin) along the branch and the final (b, cl, eps).
    """
    m = newton.m
    n = newton.n
    dev = m.dev

    def G(b, cl, eps):
        F, fl = newton.residual_full(b, cl, hom=(eps, S0, s0))
        return F, fl

    def dG_deps(b, cl):
        # derivative of residual wrt eps: + S0 (E rows except t=-1) and + s0
        d = torch.cat([S0.reshape(-1), torch.tensor([s0], device=dev)])
        return d

    z = torch.cat([b0.reshape(-1), torch.tensor([cl0, eps0], device=dev)])
    # initial tangent: solve J dz/deps = -dG/deps, then tangent = (dz/deps, 1) normalised, oriented eps increasing
    F, fl = G(b0, cl0, eps0)
    J = newton.jacobian(b0, cl0, fl)
    dzde = torch.linalg.solve(J, -dG_deps(b0, cl0))
    tau = torch.cat([dzde, torch.tensor([1.0], device=dev)])
    # weight the arclength so that eps and c_l count, b counts with 1/sqrt(n) scaling
    wts = torch.cat([torch.full((n,), 1.0 / math.sqrt(n), device=dev), torch.tensor([1.0, 1.0], device=dev)])
    tau = tau / torch.sqrt(((tau * wts) ** 2).sum())
    out = []
    for step in range(nsteps):
        zp = z + ds * tau
        # Newton corrector on augmented system
        for it in range(maxit):
            b = zp[:n].reshape(newton.N + 1, newton.M); cl = zp[n].item(); eps = zp[n + 1].item()
            F, fl = G(b, cl, eps)
            arc = ((zp - z) * wts * tau * wts).sum() - ds
            Fa = torch.cat([F, arc.reshape(1)])
            if Fa.abs().max().item() < tol:
                break
            J = newton.jacobian(b, cl, fl)
            Ja = torch.zeros(n + 2, n + 2, device=dev)
            Ja[:n + 1, :n + 1] = J
            Ja[:n + 1, n + 1] = dG_deps(b, cl)
            Ja[n + 1, :] = tau * wts * wts
            dz = torch.linalg.solve(Ja, -Fa)
            zp = zp + dz
        conv = Fa.abs().max().item() < tol
        if not conv:
            ds *= 0.5
            if verbose:
                print(f"[arc] step {step}: corrector failed (|F|={Fa.abs().max().item():.2e}); ds -> {ds:.3g}", flush=True)
            if ds < 1e-6:
                break
            continue
        # new tangent
        b = zp[:n].reshape(newton.N + 1, newton.M); cl = zp[n].item(); eps = zp[n + 1].item()
        F, fl = G(b, cl, eps)
        J = newton.jacobian(b, cl, fl)
        Ja = torch.zeros(n + 2, n + 2, device=dev)
        Ja[:n + 1, :n + 1] = J; Ja[:n + 1, n + 1] = dG_deps(b, cl); Ja[n + 1, :] = tau * wts * wts
        rhs = torch.zeros(n + 2, device=dev); rhs[-1] = 1.0
        tau_new = torch.linalg.solve(Ja, rhs)
        tau_new = tau_new / torch.sqrt(((tau_new * wts) ** 2).sum())
        if (tau_new * wts * tau * wts).sum() < 0:
            tau_new = -tau_new
        tau = tau_new
        z = zp
        if step % svd_every == 0:
            smin = torch.linalg.svdvals(J)[-1].item()
            sgn_det = torch.linalg.slogdet(J)[0].item()
        else:
            smin = float('nan'); sgn_det = 0.0
        amp = b.abs().max().item()
        binf = (m.rad.ext1_R @ b).abs().max().item()
        out.append((eps, cl, amp, binf, smin, ds))
        if save_at is not None and save_fn is not None and len(out) >= 2:
            e_prev = out[-2][0]
            for e_s in save_at:
                if e_prev < e_s <= eps:
                    save_fn(e_s, b, cl, eps)
        if verbose:
            print(f"[arc] step {step:3d} eps={eps:.6f} c_l={cl:.8f} max|b|={amp:.4g} b(inf)max={binf:.4g} smin={smin:.2e} ds={ds:.3g} tau_eps={tau[-1].item():+.3f} tau_cl={tau[-2].item():+.3f}", flush=True)
        if log is not None:
            log.write(f"{eps:.8f} {cl:.10f} {amp:.6e} {binf:.6e} {smin:.4e} {ds:.4e} {tau[-1].item():+.5f} {sgn_det:+.0f}\n"); log.flush()
        if eps >= eps_stop or amp > amp_stop or eps < -0.5:
            break
        # adapt step
        if it <= 2:
            ds = min(ds * 1.5, ds_max)
    return out, (b, cl, eps)


def levenberg_marquardt(newton: Newton, b, cl, lam=1e-3, maxit=200, tol=1e-12, verbose=True, log=None, fix_cl=False, every=10):
    """Damped Gauss-Newton on the full square system F(b, c_l) = 0 (rows: E, normalisation, identity).
    Solves (J^T J + lam D) d = -J^T F with D = diag(J^T J); lam adapted (decrease on success, increase on failure).
    Returns (b, cl, info) with the history of |F|_inf and |F|_2."""
    m = newton.m
    b = b.clone()
    F, flds = newton.residual_full(b, cl)
    if fix_cl:
        F = F.clone(); F[-1] = 0.0
    nrm2 = (F ** 2).sum().item(); hist = [(F.abs().max().item(), math.sqrt(nrm2), lam)]
    for it in range(1, maxit + 1):
        J = newton.jacobian(b, cl, flds)
        if fix_cl:
            J = J.clone(); J[-1, :] = 0; J[:, -1] = 0; J[-1, -1] = 1.0
        JtJ = J.T @ J
        g = J.T @ F
        D = torch.diag(JtJ).clamp_min(1e-30)
        accepted = False
        for _ in range(12):
            A = JtJ + lam * torch.diag(D)
            d = torch.linalg.solve(A, -g)
            db = d[:-1].reshape(newton.N + 1, newton.M); dcl = 0.0 if fix_cl else d[-1].item()
            Fn, fldsn = newton.residual_full(b + db, cl + dcl)
            if fix_cl:
                Fn = Fn.clone(); Fn[-1] = 0.0
            n2 = (Fn ** 2).sum().item()
            if n2 < nrm2:
                b = b + db; cl = cl + dcl; F, flds, nrm2 = Fn, fldsn, n2
                lam = max(lam / 3, 1e-15); accepted = True
                break
            lam *= 4
        hist.append((F.abs().max().item(), math.sqrt(nrm2), lam))
        if verbose and (it % every == 0 or not accepted):
            print(f"[LM] it {it:4d} |F|_inf={hist[-1][0]:.3e} |F|_2={hist[-1][1]:.3e} lam={lam:.1e} c_l={cl:.8f} max|b|={b.abs().max().item():.4g} min b={b[1:].min().item():.3g} accepted={accepted}", flush=True)
        if log is not None:
            log.write(f"{it} {hist[-1][0]:.6e} {hist[-1][1]:.6e} {lam:.3e} {cl:.12f}\n"); log.flush()
        if not accepted or hist[-1][0] < tol:
            break
    return b, cl, dict(hist=hist, converged=hist[-1][0] < tol, nrm_inf=hist[-1][0], nrm_2=hist[-1][1])


def levenberg_marquardt_hom(newton: Newton, b, cl, hom=None, lam=1e-3, maxit=200, tol=1e-12, verbose=False):
    """LM on the (possibly homotopy-modified) square system; same as levenberg_marquardt but with hom passed through."""
    m = newton.m
    b = b.clone()
    F, flds = newton.residual_full(b, cl, hom=hom)
    nrm2 = (F ** 2).sum().item(); hist = [(F.abs().max().item(), math.sqrt(nrm2), lam)]
    for it in range(1, maxit + 1):
        J = newton.jacobian(b, cl, flds)
        JtJ = J.T @ J; g = J.T @ F; D = torch.diag(JtJ).clamp_min(1e-30)
        accepted = False
        for _ in range(14):
            d = torch.linalg.solve(JtJ + lam * torch.diag(D), -g)
            db = d[:-1].reshape(newton.N + 1, newton.M); dcl = d[-1].item()
            Fn, fldsn = newton.residual_full(b + db, cl + dcl, hom=hom)
            n2 = (Fn ** 2).sum().item()
            if n2 < nrm2:
                b = b + db; cl = cl + dcl; F, flds, nrm2 = Fn, fldsn, n2
                lam = max(lam / 3, 1e-15); accepted = True
                break
            lam *= 4
        hist.append((F.abs().max().item(), math.sqrt(nrm2), lam))
        if verbose:
            print(f"[LMh] it {it} |F|_inf={hist[-1][0]:.3e} lam={lam:.1e} c_l={cl:.8f}", flush=True)
        if not accepted or hist[-1][0] < tol:
            break
    return b, cl, dict(hist=hist, converged=hist[-1][0] < tol, nrm_inf=hist[-1][0], nrm=hist[-1][0])


def levenberg_marquardt_reduced(newton: Newton, b, cl, lam=1e-6, maxit=200, tol=1e-12, verbose=True, every=10):
    """LM on the true equations with the normalisation unknowns b(0, theta_j) FIXED at 1 (rows/columns 0..M-1 removed), so the
    normalisation cannot drift. Unknowns: b at rows >= 1 and c_l; equations: collocation rows >= 1 and the identity row."""
    m = newton.m; M = newton.M; n = newton.n
    keep = torch.arange(M, n + 1, device=m.dev)         # free unknowns and the corresponding equations (identity last)
    b = b.clone(); b[0, :] = 1.0
    F, flds = newton.residual_full(b, cl); Fr = F[keep]
    nrm2 = (Fr ** 2).sum().item(); hist = [(Fr.abs().max().item(), math.sqrt(nrm2), lam)]
    for it in range(1, maxit + 1):
        J = newton.jacobian(b, cl, flds)[keep][:, keep]
        JtJ = J.T @ J; g = J.T @ Fr; D = torch.diag(JtJ).clamp_min(1e-30)
        accepted = False
        for _ in range(14):
            d = torch.linalg.solve(JtJ + lam * torch.diag(D), -g)
            bt = b.clone(); bt.reshape(-1)[M:] += d[:-1]; clt = cl + d[-1].item()
            Fn, fldsn = newton.residual_full(bt, clt); Frn = Fn[keep]
            n2 = (Frn ** 2).sum().item()
            if n2 < nrm2:
                b, cl, Fr, flds, nrm2 = bt, clt, Frn, fldsn, n2
                lam = max(lam / 3, 1e-16); accepted = True
                break
            lam *= 4
        hist.append((Fr.abs().max().item(), math.sqrt(nrm2), lam))
        if verbose and (it % every == 0 or not accepted):
            print(f"[LMr] it {it:4d} |F|_inf={hist[-1][0]:.3e} |F|_2={hist[-1][1]:.3e} lam={lam:.1e} c_l={cl:.10f} accepted={accepted}", flush=True)
        if not accepted or hist[-1][0] < tol:
            break
    return b, cl, dict(hist=hist, converged=hist[-1][0] < tol, nrm_inf=hist[-1][0], nrm_2=hist[-1][1], nrm=hist[-1][0])
