"""Levenberg-Marquardt profile search for Setting A2.
Unknowns: Chebyshev-Fourier coefficients ca[M,N], cG[M,N] (per-angular-mode orthonormalized on the collocation grid)
and beta (optionally fixed). Equations (over-collocated least squares, ov x more rows than unknowns):
desingularized residuals R_a, R_G at the collocation nodes, row-weighted by 1/prefactor so the far field is O(1),
the two exact origin equations and the normalization a(0) = a0_target.
Radial maps: 'xi' (xi = (r^2-L^2)/(r^2+L^2), a2core.A2Model) or 't' (t = (1+r^2/L^2)^{-1/(2 beta)}, a2core_t.A2ModelT).
"""
import sys, time, json, math, argparse
import numpy as np, torch
sys.path.insert(0, 'code')
from a2core import A2Model, DT, cheb_gauss_nodes, cheb_T, orthonormal_basis
from a2core_t import A2ModelT

dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def sigmas_of_beta(beta):
    return 1.0 + 1.0 / beta, 1.0 + 1.0 / (2.0 * beta)


def make_model(mapname, N, M, L, beta, sigma_a, sigma_G, rad_eval=None, th_eval=None):
    if mapname == 'xi':
        return A2Model(N, M, L, sigma_a, sigma_G, device=dev, xi_eval=rad_eval, th_eval=th_eval)
    return A2ModelT(N, M, L, beta, sigma_a, sigma_G, device=dev, eta_eval=rad_eval, th_eval=th_eval)


def model_prefactors(model, mapname, rad, which):
    """prefactor P_l at radial coordinate values rad (xi or eta) for all l: [M, len(rad)]"""
    rad = np.asarray(rad, dtype=np.float64); l = np.arange(model.M)
    if mapname == 'xi':
        sg = model.sigma_a if which == 'a' else model.sigma_G
        return ((1 + rad[None, :]) / 2) ** l[:, None] * (1 - rad[None, :]) ** sg
    t = (1 + rad) / 2; b = model.beta
    e = model.e_a if which == 'a' else model.e_G
    return (1 - t[None, :] ** (2 * b)) ** l[:, None] * t[None, :] ** e


def rad_of_r(model, mapname, r):
    r = np.asarray(r, dtype=np.float64)
    if mapname == 'xi':
        return (r ** 2 - model.L ** 2) / (r ** 2 + model.L ** 2)
    return model.eta_of_r(r)


class LMProblem:
    def __init__(self, N, M, L, beta0, sigma_a=None, sigma_G=None, a0_target=1.0, w_origin=3.0, fixed_beta=None,
                 ortho=True, ortho_tol=1e-9, ov=2.0, mapname='t', Rw=30.0, wmax=None, ypen=None, pres=None, tail=None, t1=1e-5, patch=None, patch_n=None):
        sa, sG = sigmas_of_beta(beta0)
        self.sigma_a = sa if sigma_a is None else sigma_a
        self.sigma_G = sG if sigma_G is None else sigma_G
        self.N, self.M, self.L, self.mapname, self.beta_map = N, M, L, mapname, beta0
        self.Ne, self.Me = int(round(ov * N)), int(round(ov * M))
        th_eval = (np.arange(self.Me) + 0.5) * np.pi / (2 * self.Me)
        self.model = make_model(mapname, N, M, L, beta0, self.sigma_a, self.sigma_G, cheb_gauss_nodes(self.Ne), th_eval)
        self.a0_target, self.w_origin, self.fixed_beta, self.Rw = a0_target, w_origin, fixed_beta, Rw
        # row weights: ~1 for r < Rw, ~ 1/prefactor_0 (relative residual) for r >> Rw
        rt = self.model.rt
        self.wa_r = (1 + rt ** 2 / Rw ** 2) ** self.sigma_a
        self.wG_r = (1 + rt ** 2 / Rw ** 2) ** self.sigma_G
        self.wmax = wmax
        if wmax is not None:   # cap the far-field weights (absolute-residual regime beyond the cap)
            self.wa_r = torch.clamp(self.wa_r, max=wmax); self.wG_r = torch.clamp(self.wG_r, max=wmax)
        self.ortho = ortho
        if ortho:
            self.Ra_basis = orthonormal_basis(self.model, 'a', ortho_tol, row_weight=self.wa_r)
            self.RG_basis = orthonormal_basis(self.model, 'G', ortho_tol, row_weight=self.wG_r)
            self.na = [R.shape[1] for R in self.Ra_basis]; self.nG = [R.shape[1] for R in self.RG_basis]
            self.n_unknown = sum(self.na) + sum(self.nG) + (0 if fixed_beta is not None else 1)
        else:
            self.n_unknown = 2 * M * N + (0 if fixed_beta is not None else 1)
        # optional y-axis positivity penalty: ypen = (c0, w_pen): rows w_pen * relu(c0 - W2(0,y)/y) on a y-grid
        self.ypen = ypen
        if ypen is not None:
            yg = np.geomspace(1.0, 3000.0, 48)
            self.axis_model = make_model(mapname, N, M, L, beta0, self.sigma_a, self.sigma_G, rad_of_r(self.model, mapname, yg), np.array([np.pi / 2 - 1e-9]))
        # optional exact resonance constraint at P: pres = (xlo, xhi, w): W1(x*,0) = 0, W1'(x*,0) = beta+2 with
        # x* an extra unknown; W1 on the x-axis is Chebyshev-interpolated from a fixed axis grid on [xlo, xhi]
        self.pres = pres
        if pres is not None:
            xlo, xhi, wp = pres; nax = 40
            self.ax_nodes = 0.5 * (xlo + xhi) + 0.5 * (xhi - xlo) * np.cos(np.pi * (np.arange(nax) + 0.5) / nax)
            self.xaxis_model = make_model(mapname, N, M, L, beta0, self.sigma_a, self.sigma_G, rad_of_r(self.model, mapname, self.ax_nodes), np.array([1e-9]))
            self.ax_nodes_t = torch.tensor(self.ax_nodes, dtype=DT, device=dev)
            self.n_unknown += 1
        # optional exact first-tail matching rows: the weighted residual R/P_0 vanishes
        # identically at t = 0 (leading far-field balance built into the prefactors) and equals t R1(theta) + O(t^2); the rows
        # impose R1(theta_m) = 0 (next-order far-field balance) via Richardson extrapolation from t = t1 and 2 t1
        self.tail = tail; self.t1 = t1
        if tail is not None:
            eta_tail = np.array([2 * t1 - 1, 2 * (2 * t1) - 1])
            self.tail_model = make_model(mapname, N, M, L, beta0, self.sigma_a, self.sigma_G, eta_tail, th_eval)
        # optional localized Cartesian residual rows (external referee's diagnostic 2): patch = (xc, yc, rad, w): rows
        # w * R_Theta(X) / (S sqrt(n_patch)) with S = 100 (fixed scale) on a 12 x 12 polar product grid covering the disc of radius rad
        # about (xc, yc); the weight w is independent of N and of the row count, so the patch keeps its influence under refinement
        self.patch = patch
        if patch is not None:
            xc, yc, rad, wp = patch
            # patch_n: optional node count per direction (default 12 for the disc, 24 for the annulus); the row
            # weight w / (100 sqrt(n_patch)) is an equal-node RMS and does not change with the node count
            if rad > 0:      # disc of radius rad about (xc, yc): 12 x 12 polar product grid covering it
                rc = math.hypot(xc, yc); thc = math.atan2(yc, xc); npx = 12 if patch_n is None else int(patch_n)
                rr = rc + rad * np.cos(np.pi * (np.arange(npx) + 0.5) / npx); tt = thc + (rad / rc) * np.cos(np.pi * (np.arange(npx) + 0.5) / npx)
            else:            # rad <= 0: annular sector r in [xc, yc], all angles of the open quadrant: 24 x 24 product grid
                npx = 24 if patch_n is None else int(patch_n); r1, r2 = xc, yc
                rr = 0.5 * (r1 + r2) + 0.5 * (r2 - r1) * np.cos(np.pi * (np.arange(npx) + 0.5) / npx); tt = (np.arange(npx) + 0.5) * (np.pi / 2) / npx
            self.patch_model = make_model(mapname, N, M, L, beta0, self.sigma_a, self.sigma_G, rad_of_r(self.model, mapname, rr), tt)
            self.patch_scale = 100.0; self.patch_n = npx * npx
        self.rownorm = 1.0 / math.sqrt(2 * self.Ne * self.Me)
        self.wa = self.wa_r[:, None].expand(self.Ne, self.Me).reshape(-1) * self.rownorm
        self.wG = self.wG_r[:, None].expand(self.Ne, self.Me).reshape(-1) * self.rownorm

    def unpack(self, z):
        M, N = self.M, self.N
        if self.ortho:
            ca_rows, cG_rows = [], []; off = 0
            for l in range(M):
                ca_rows.append(self.Ra_basis[l] @ z[off:off + self.na[l]]); off += self.na[l]
            for l in range(M):
                cG_rows.append(self.RG_basis[l] @ z[off:off + self.nG[l]]); off += self.nG[l]
            ca = torch.stack(ca_rows); cG = torch.stack(cG_rows)
            beta = z[off] if self.fixed_beta is None else torch.tensor(self.fixed_beta, dtype=DT, device=dev)
            if getattr(self, 'pres', None) is not None:
                self.xstar_t = z[-1]
            return ca, cG, beta
        ca = z[:M * N].reshape(M, N); cG = z[M * N:2 * M * N].reshape(M, N)
        beta = z[2 * M * N] if self.fixed_beta is None else torch.tensor(self.fixed_beta, dtype=DT, device=dev)
        return ca, cG, beta

    def pack(self, ca, cG, beta):
        if self.ortho:
            parts = [torch.linalg.pinv(self.Ra_basis[l]) @ ca[l] for l in range(self.M)] + \
                    [torch.linalg.pinv(self.RG_basis[l]) @ cG[l] for l in range(self.M)]
        else:
            parts = [ca.reshape(-1), cG.reshape(-1)]
        if self.fixed_beta is None:
            parts.append(torch.tensor([beta], dtype=DT, device=dev))
        if getattr(self, 'pres', None) is not None:
            parts.append(torch.tensor([float(getattr(self, 'xstar_init', 0.5 * (self.pres[0] + self.pres[1])))], dtype=DT, device=dev))
        return torch.cat(parts)

    def F(self, z):
        ca, cG, beta = self.unpack(z)
        f = self.model.fields(ca, cG, beta)
        rows = [self.wa * f['Ra'].reshape(-1), self.wG * f['RG'].reshape(-1),
                self.w_origin * ((2 * beta - f['c'] + 2) * f['a0']).reshape(1),
                self.w_origin * ((2 * beta + 1) * f['G0'] - 2 * f['a0']).reshape(1),
                self.w_origin * (f['a0'] - self.a0_target).reshape(1)]
        if self.tail is not None:
            ft = self.tail_model.fields(ca, cG, beta)
            fa = ft['Ra'] / self.tail_model.Pa[0][:, None]; fG = ft['RG'] / self.tail_model.PG[0][:, None]
            R1a = (4 * fa[0] - fa[1]) / 2; R1G = (4 * fG[0] - fG[1]) / 2       # = t1 * R1(theta): the O(t) coefficient scaled by t1
            rows.append(self.tail * self.rownorm * R1a); rows.append(self.tail * self.rownorm * R1G)
        if self.patch is not None:
            fp = self.patch_model.fields(ca, cG, beta)
            RTh = (fp['x'] ** 2 * fp['y'] * fp['Ra']).reshape(-1)
            rows.append(self.patch[3] / (self.patch_scale * math.sqrt(self.patch_n)) * RTh)
        if self.ypen is not None:
            fa = self.axis_model.fields(ca, cG, beta)
            c0, wp = self.ypen
            rows.append(wp * torch.relu(c0 - fa['w2'][:, 0]))
        if self.pres is not None:
            fx = self.xaxis_model.fields(ca, cG, beta)
            W1ax = fx['W1'][:, 0]                      # W1 at the axis nodes
            xs = z[-1]
            # barycentric Lagrange interpolation (Chebyshev-Gauss nodes) and its derivative at xs
            nodes = self.ax_nodes_t; n = len(nodes)
            wts = torch.tensor([(-1.0) ** j * np.sin(np.pi * (j + 0.5) / n) for j in range(n)], dtype=DT, device=dev)
            diff = xs - nodes
            num = torch.sum(wts / diff * W1ax); den = torch.sum(wts / diff)
            W1s = num / den
            # derivative of the barycentric form
            dnum = -torch.sum(wts / diff ** 2 * W1ax); dden = -torch.sum(wts / diff ** 2)
            W1p = (dnum * den - num * dden) / den ** 2
            wp = self.pres[2]
            rows.append(wp * W1s.reshape(1)); rows.append(wp * (W1p - (beta + 2)).reshape(1))
        return torch.cat(rows)

    def jac(self, z, chunk=None):
        n = z.numel()
        if n <= 4000:
            return torch.func.jacfwd(self.F)(z)
        if chunk is None:
            chunk = 512 if n <= 8000 else 192     # memory-bounded forward-mode Jacobian (N176 with 1024 tangents used 68 GB)
        # chunked forward-mode Jacobian (memory-bounded): columns = jvp along unit tangents
        cols = []
        for i0 in range(0, n, chunk):
            idx = torch.arange(i0, min(i0 + chunk, n), device=z.device)
            V = torch.zeros((len(idx), n), dtype=z.dtype, device=z.device); V[torch.arange(len(idx)), idx] = 1.0
            Jc = torch.func.vmap(lambda v: torch.func.jvp(self.F, (z,), (v,))[1])(V)   # [chunk, m]
            cols.append(Jc.T)
        return torch.cat(cols, 1)

    def diagnostics(self, z):
        ca, cG, beta = self.unpack(z)
        f = self.model.fields(ca, cG, beta)
        Fv = self.F(z)
        Tinv = torch.linalg.pinv(self.model.T); Cinv = torch.linalg.pinv(self.model.C)
        res = {}
        for nm, fld, P0 in [('a', f['a'], self.model.Pa[0]), ('G', f['G'], self.model.PG[0])]:
            coef = Tinv @ (fld / P0[:, None])
            res[nm + '_rtail'] = float(coef[-2:].abs().max() / coef.abs().max())
            ang = Cinv @ fld.T
            res[nm + '_atail'] = float(ang[-2:].abs().max() / ang.abs().max())
        d = dict(beta=float(beta), a0=float(f['a0']), G0=float(f['G0']), c=float(f['c']),
                 xstar=(float(z[-1]) if self.pres is not None else float('nan')),
                 c_minus_2b2=float(f['c'] - 2 * beta - 2), Fnorm=float(Fv.norm()), Fmax=float(Fv.abs().max()),
                 Ra_max=float(f['Ra'].abs().max()), RG_max=float(f['RG'].abs().max()),
                 Ra_w_max=float((self.wa * f['Ra'].reshape(-1)).abs().max() / self.rownorm),
                 RG_w_max=float((self.wG * f['RG'].reshape(-1)).abs().max() / self.rownorm),
                 a_max=float(f['a'].abs().max()), G_max=float(f['G'].abs().max()), n_unknown=int(self.n_unknown))
        if self.tail is not None:
            ft = self.tail_model.fields(ca, cG, beta)
            fa = ft['Ra'] / self.tail_model.Pa[0][:, None]; fG = ft['RG'] / self.tail_model.PG[0][:, None]
            d['R1a_max'] = float(((4 * fa[0] - fa[1]) / (2 * self.t1)).abs().max()); d['R1G_max'] = float(((4 * fG[0] - fG[1]) / (2 * self.t1)).abs().max())
        if self.patch is not None:
            fp = self.patch_model.fields(ca, cG, beta); RTh = (fp['x'] ** 2 * fp['y'] * fp['Ra'])
            d['patch_RTheta_max'] = float(RTh.abs().max()); d['patch_RTheta_rms'] = float(RTh.pow(2).mean().sqrt())
            # misfit of the standard rows alone (without the patch rows), for like-for-like comparison with unpatched states
            npr = self.patch_n; d['Fnorm_nopatch'] = float(torch.cat([Fv[:2 * self.Ne * self.Me + 3], Fv[2 * self.Ne * self.Me + 3:][:(0 if self.tail is None else 2 * self.Me)]]).norm())
        d.update(res)
        return d


def lm(prob, z, maxit=200, lam=1e-2, tol=1e-13, verbose=True, log=None, svd_every=0, max_lam=1e12, stall_tol=1e-7):
    Fv = prob.F(z); cost = float(Fv.norm())
    hist = []; t0 = time.time(); stall = 0
    for it in range(maxit):
        J = prob.jac(z)
        JtJ = J.T @ J; g = J.T @ Fv
        D = torch.diag(JtJ).clamp_min(1e-30)
        accepted = False; dz = torch.zeros_like(z)
        for _ in range(30):
            A = JtJ + lam * torch.diag(D)
            try:
                dz = torch.linalg.solve(A, -g)
            except Exception:
                lam *= 10; continue
            z_new = z + dz
            F_new = prob.F(z_new); c_new = float(F_new.norm())
            if math.isfinite(c_new) and c_new < cost:
                rel = (cost - c_new) / cost
                z, Fv, cost = z_new, F_new, c_new
                lam = max(lam / 3.0, 1e-15); accepted = True
                stall = stall + 1 if rel < stall_tol else 0
                break
            lam *= 4.0
            if lam > max_lam:
                break
        d = prob.diagnostics(z); d.update(it=it, lam=lam, step=float(dz.norm()) if accepted else 0.0, t=time.time() - t0)
        if svd_every and (it % svd_every == 0):
            sv = torch.linalg.svdvals(J)
            d['sv_min5'] = [float(s) for s in sv[-5:]]; d['sv_max'] = float(sv[0])
        hist.append(d)
        if verbose:
            msg = (f"it {it:3d} |F|={d['Fnorm']:.3e} Fmax={d['Fmax']:.2e} beta={d['beta']:.6f} c-2b-2={d['c_minus_2b2']:+.2e} "
                   f"a0={d['a0']:.6f} G0={d['G0']:.5f} lam={lam:.1e} step={d['step']:.2e} "
                   f"tails a:{d['a_rtail']:.1e}/{d['a_atail']:.1e} G:{d['G_rtail']:.1e}/{d['G_atail']:.1e}")
            if 'sv_min5' in d: msg += f" svmin={d['sv_min5'][-1]:.2e}"
            if 'kappa' in d: msg += f" kappa={d['kappa']:+.5e}"
            if 'R1a_max' in d: msg += f" R1max={d['R1a_max']:.2e}/{d['R1G_max']:.2e}"
            if 'xstar' in d and d['xstar'] == d['xstar']: msg += f" x*={d['xstar']:.5f}"
            print(msg, flush=True)
            if log: log.write(msg + "\n"); log.flush()
        if not accepted or cost < tol or stall >= 20:
            break
    return z, hist


def fit_fields(prob, a_vals, G_vals, r_grid, th_grid, beta, r_fit=None, ridge=1e-6, mask=None):
    """Least-squares fit of grid values a_vals[len(r), len(th)], G_vals to prob's basis -> z.
    Rows are weighted by relative weights 1/P_0 (far field relative). If r_fit is given, rows with r > r_fit are
    dropped and replaced by a weak ridge toward q = 0 (pure prefactor decay) so that garbage far fields of the input
    do not pollute the fit."""
    m = prob.model; M, N = prob.M, prob.N
    r_grid = np.asarray(r_grid); rad = rad_of_r(m, prob.mapname, r_grid)
    Cm = np.cos(np.outer(th_grid, 2 * np.arange(M)))
    T = cheb_T(rad, N)
    keep = np.ones(len(r_grid), bool) if r_fit is None else (r_grid <= r_fit)
    if mask is not None:
        # a radial row is usable only if all its angular values are valid (angular transform needs full rows)
        keep = keep & np.all(mask, axis=1)
    out = []
    for vals, which in [(a_vals, 'a'), (G_vals, 'G')]:
        modes = np.linalg.lstsq(Cm, vals.T, rcond=None)[0]   # [l, i]
        P = model_prefactors(m, prob.mapname, rad, which)
        w = 1.0 / P[0]
        c = np.zeros((M, N))
        for l in range(M):
            A = (w[keep] * P[l][keep])[:, None] * T[keep]
            b = (w[keep] * modes[l][keep])
            if r_fit is not None:
                A = np.vstack([A, ridge * np.eye(N)]); b = np.concatenate([b, np.zeros(N)])
            s = np.linalg.norm(A, axis=0); s[s == 0] = 1
            c[l] = np.linalg.lstsq(A / s, b, rcond=1e-13)[0] / s
        out.append(torch.tensor(c, dtype=DT, device=dev))
    return prob.pack(out[0], out[1], beta)


def initial_guess(prob, beta0, Ra=None, RG=None, seed=None, noise=0.0, kind='gauss'):
    """a = a0 exp(-r^2/Ra^2)-like, G = G0 exp(-r^2/RG^2) with RG chosen so that c ~ 2 beta + 2 (c ~ G0 RG^2/8)."""
    a0 = prob.a0_target; G0 = 2 * a0 / (2 * beta0 + 1)
    if RG is None:
        # c = (1/2) int b_2/s ds = 2 beta + 2: Gaussian: c = G0 RG^2/8 ; algebraic (1+r^2/RG^2)^{-sigma_G}: c = G0 RG^2/(8 (sigma_G-1))
        RG = math.sqrt(8 * (2 * beta0 + 2) / abs(G0)) if kind == "gauss" else math.sqrt(8 * (2 * beta0 + 2) * (prob.sigma_G - 1) / abs(G0))
    if Ra is None: Ra = RG
    m = prob.model
    r = m.r; th = m.th
    if kind == 'gauss':
        fa = a0 * np.exp(-r ** 2 / Ra ** 2); fG = G0 * np.exp(-r ** 2 / RG ** 2)
    else:  # algebraic tails matching the far-field exponents
        fa = a0 * (1 + r ** 2 / Ra ** 2) ** (-prob.sigma_a); fG = G0 * (1 + r ** 2 / RG ** 2) ** (-prob.sigma_G)
    a_vals = np.repeat(fa[:, None], len(th), 1); G_vals = np.repeat(fG[:, None], len(th), 1)
    if noise > 0:
        rng = np.random.default_rng(seed or 0)
        a_vals *= 1 + noise * rng.standard_normal(a_vals.shape) * 0
        # smooth angular noise: add low-mode perturbations
        for l in range(1, min(4, prob.M)):
            amp = noise * rng.standard_normal() / l
            a_vals += amp * a0 * np.exp(-r ** 2 / Ra ** 2)[:, None] * (r ** 2 / (r ** 2 + Ra ** 2))[:, None] ** l * np.cos(2 * l * th)[None, :]
            amp = noise * rng.standard_normal() / l
            G_vals += amp * G0 * np.exp(-r ** 2 / RG ** 2)[:, None] * (r ** 2 / (r ** 2 + RG ** 2))[:, None] ** l * np.cos(2 * l * th)[None, :]
    return fit_fields(prob, a_vals, G_vals, r, th, beta0)


def refit(prob_old, z_old, prob_new, beta_new=None, r_fit=None):
    """Transfer a state to a new problem (different N, M, L, map, sigma or beta): evaluate old fields on the new grid."""
    ca, cG, beta = prob_old.unpack(z_old)
    beta = float(beta) if beta_new is None else beta_new
    r_new, th_new = prob_new.model.r, prob_new.model.th
    mo = prob_old.model
    rad_old = rad_of_r(mo, prob_old.mapname, r_new)
    tmp = make_model(prob_old.mapname, prob_old.N, prob_old.M, prob_old.L, prob_old.beta_map, prob_old.sigma_a,
                     prob_old.sigma_G, rad_old, th_new)
    f = tmp.fields(ca, cG, beta)
    return fit_fields(prob_new, f['a'].cpu().numpy(), f['G'].cpu().numpy(), r_new, th_new, beta, r_fit=r_fit)


def save_state(path, prob, z, hist=None, extra=None):
    ca, cG, beta = prob.unpack(z)
    np.savez(path, ca=ca.detach().cpu().numpy(), cG=cG.detach().cpu().numpy(), beta=float(beta), N=prob.N, M=prob.M,
             L=prob.L, sigma_a=prob.sigma_a, sigma_G=prob.sigma_G, a0_target=prob.a0_target, Ne=prob.Ne, Me=prob.Me,
             mapname=prob.mapname, beta_map=prob.beta_map, Rw=prob.Rw, w_origin=prob.w_origin, wmax=(prob.wmax if prob.wmax is not None else -1.0),
             ypen=(np.array(prob.ypen) if prob.ypen is not None else np.array([0.0, 0.0])),
             pres=(np.array(prob.pres) if prob.pres is not None else np.array([0.0, 0.0, 0.0])), tail=(prob.tail if prob.tail is not None else 0.0), t1=prob.t1, patch=(np.array(prob.patch) if getattr(prob, 'patch', None) is not None else np.array([0.0, 0.0, 0.0, 0.0])),
             xstar=(float(z[-1]) if prob.pres is not None else float('nan')),
             hist=json.dumps(hist or []), extra=json.dumps(extra or {}))


def load_state(path):
    return np.load(path, allow_pickle=True)


def problem_from_state(d, ov=None, fixed_beta=None):
    mapname = str(d['mapname']) if 'mapname' in d else 'xi'
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    ov = ov or float(d['Ne']) / N
    beta_map = float(d['beta_map']) if 'beta_map' in d else float(d['beta'])
    prob = LMProblem(N, M, L, beta_map, float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']),
                     float(d['w_origin']) if 'w_origin' in d else 3.0, fixed_beta, ov=ov, mapname=mapname,
                     Rw=float(d['Rw']) if 'Rw' in d else 30.0, wmax=(float(d['wmax']) if ('wmax' in d and float(d['wmax']) > 0) else None))
    z = prob.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), float(d['beta']))
    return prob, z


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--N', type=int, default=32); ap.add_argument('--M', type=int, default=8)
    ap.add_argument('--L', type=float, default=6.0); ap.add_argument('--beta0', type=float, default=3.0)
    ap.add_argument('--fixed_beta', type=float, default=None)
    ap.add_argument('--sigma_a', type=float, default=None); ap.add_argument('--sigma_G', type=float, default=None)
    ap.add_argument('--maxit', type=int, default=100); ap.add_argument('--rounds', type=int, default=1)
    ap.add_argument('--lam', type=float, default=1e-2); ap.add_argument('--a0', type=float, default=1.0)
    ap.add_argument('--Ra', type=float, default=None); ap.add_argument('--RG', type=float, default=None)
    ap.add_argument('--noise', type=float, default=0.0); ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--kind', type=str, default='gauss')
    ap.add_argument('--init', type=str, default=None, help='npz state to start from (re-fitted if sizes/map differ)')
    ap.add_argument('--name', type=str, default='run'); ap.add_argument('--svd_every', type=int, default=0)
    ap.add_argument('--w_origin', type=float, default=30.0)
    ap.add_argument('--Rw', type=float, default=30.0, help='interior radius for the residual row weights')
    ap.add_argument('--ov', type=float, default=2.0); ap.add_argument('--map', type=str, default='t')
    ap.add_argument('--r_fit', type=float, default=None, help='refit only on r <= r_fit (ridge beyond); use when changing beta/map')
    ap.add_argument('--wmax', type=float, default=None, help='cap on the far-field row weights (interior-only fit diagnostic)')
    ap.add_argument('--ypen', type=float, nargs=2, default=None, metavar=('C0', 'WPEN'), help='y-axis positivity penalty rows w*relu(c0 - W2(0,y)/y)')
    ap.add_argument('--pres', type=float, nargs=3, default=None, metavar=('XLO', 'XHI', 'W'), help='exact P resonance rows W1(x*,0)=0, W1\'(x*,0)=beta+2 with x* unknown in [XLO,XHI]')
    ap.add_argument('--tail', type=float, default=None, help='weight of the exact first-tail matching rows R1(theta)=0 at t=0 (next-order far-field balance)')
    ap.add_argument('--t1', type=float, default=1e-5)
    ap.add_argument('--patch', type=float, nargs=4, default=None, metavar=('XC', 'YC', 'RAD', 'W'), help='localized Cartesian residual rows W.grad Theta on a disc')
    ap.add_argument('--patch_n', type=int, default=None, help='nodes per direction of the patch/annulus product grid (default 12 disc / 24 annulus)')
    args = ap.parse_args()
    log = open(f'runs/{args.name}.log', 'a')
    log.write(f"# {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} args: {vars(args)}\n")
    beta0 = args.beta0 if args.fixed_beta is None else args.fixed_beta
    if args.init:
        d = load_state(args.init)
        prob_old, z_old = problem_from_state(d)
        if args.fixed_beta is None and args.beta0 == 3.0 and 'beta' in d:
            beta0 = float(d['beta'])
        prob = LMProblem(args.N, args.M, args.L, beta0, args.sigma_a, args.sigma_G, args.a0, args.w_origin, args.fixed_beta,
                         ov=args.ov, mapname=args.map, Rw=args.Rw, wmax=args.wmax, ypen=(tuple(args.ypen) if args.ypen else None), pres=(tuple(args.pres) if args.pres else None), tail=args.tail, t1=args.t1, patch=(tuple(args.patch) if args.patch else None), patch_n=args.patch_n)
        if args.pres: prob.xstar_init = 0.5 * (args.pres[0] + args.pres[1])
        z = refit(prob_old, z_old, prob, beta0, r_fit=args.r_fit)
    else:
        prob = LMProblem(args.N, args.M, args.L, beta0, args.sigma_a, args.sigma_G, args.a0, args.w_origin, args.fixed_beta,
                         ov=args.ov, mapname=args.map, Rw=args.Rw, wmax=args.wmax, ypen=(tuple(args.ypen) if args.ypen else None), pres=(tuple(args.pres) if args.pres else None), tail=args.tail, t1=args.t1, patch=(tuple(args.patch) if args.patch else None), patch_n=args.patch_n)
        z = initial_guess(prob, beta0, args.Ra, args.RG, seed=args.seed, noise=args.noise, kind=args.kind)
    print("initial:", prob.diagnostics(z)); log.write(str(prob.diagnostics(z)) + "\n")
    allhist = []
    for rnd in range(args.rounds):
        z, hist = lm(prob, z, maxit=args.maxit, lam=args.lam, log=log, svd_every=args.svd_every)
        allhist += hist
        save_state(f'runs/{args.name}.npz', prob, z, allhist, extra=vars(args))
        if rnd < args.rounds - 1 and args.fixed_beta is None and args.sigma_a is None:
            ca, cG, beta = prob.unpack(z); beta = float(beta)
            print(f"round {rnd}: rebuilding map/sigmas at beta={beta:.6f}")
            # 2026-10-22: the rebuilt problem keeps the tail rows, t1 and the weight cap of the command line (before this change the
            # rebuilt rounds dropped them; all quoted states were run with rounds = 1, and the N48 rounds = 3 runs of 5d had no tail rows or cap)
            prob_new = LMProblem(args.N, args.M, args.L, beta, None, None, args.a0, args.w_origin, args.fixed_beta,
                                 ov=args.ov, mapname=args.map, Rw=args.Rw, wmax=args.wmax, tail=args.tail, t1=args.t1)
            z = refit(prob, z, prob_new, beta); prob = prob_new
    print("final:", prob.diagnostics(z)); log.write("final: " + str(prob.diagnostics(z)) + "\n")
    save_state(f'runs/{args.name}.npz', prob, z, allhist, extra=vars(args))
