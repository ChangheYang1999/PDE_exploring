"""ProblemN1 (lane numerics_agent_1): ipm_opt2.Problem2 with
  (a) only the ACTIVE derivative components (those with a nonzero weight) evaluated in the objective and the Gauss-Newton Jacobian
      (pure L^2 runs cost one component instead of six),
  (b) an optional extra annulus weight (reweighting experiments, section 16 of the prompt),
  (c) norms_report(a): the standard FLOAT norms G0, G1, P2, rF, sup|F| and ||F||_(ds dtheta) from the full components, for logging,
  (d) optimize2 with per-step norm logging and checkpoints.
Objective (quarter-plane mesh times 4, dX = r^2 ds dtheta on r_cut <= r <= r_max):
  sum W [ wF (1 + hw r^2) F^2 + wlog F^2 / r^2 + wmid 1_{annulus} F^2 + wG |grad F|^2 + wP omega^2 |D^2 F|^2 ] + wkap kappa^2-rows.
Linear rows (exact) and the five quadratic Taylor rows are handled as in ipm_opt.Problem / ipm_opt2.Problem2 (null-space GN + SQP projection)."""
import math, time, os
import numpy as np
import torch
import ipm_opt2 as O2
DT = torch.float64
DERIVS = O2.DERIVS; LEIB = O2.LEIB; NL = O2.NL

class ProblemN1(O2.Problem2):
    def __init__(self, gens, c_exact, mesh, r_cut=0.02, r_max=1e4, wF=1.0, hw=0.0, wG=0.0, wP=0.0, wlog=0.0, wkap=0.0, wmid=0.0, mid_range=(4., 8.), wXs=0.0, sig2=1.75):
        super().__init__(gens, c_exact, mesh, r_cut=r_cut, r_max=r_max, wF=wF, hw=hw, wG=wG, wP=wP, wlog=wlog, wkap=wkap)
        r = mesh.r[:, None]
        maskr = ((mesh.r >= r_cut) & (mesh.r <= r_max)).to(DT)[:, None]*torch.ones_like(mesh.W)
        self.base = 4*mesh.W*r**2*maskr
        self.wmid, self.mid_range = wmid, tuple(mid_range)
        if wmid > 0:
            ann = ((mesh.r >= mid_range[0]) & (mesh.r < mid_range[1])).to(DT)[:, None]*torch.ones_like(mesh.W)
            self.wts[(0, 0)] = self.wts[(0, 0)]+wmid*self.base*ann
        self.wXs, self.sig2 = wXs, sig2
        self.Xs2 = (1+r**2)**sig2*torch.ones_like(mesh.W)          # <X>^(2 sigma): the L^2 proxy of the strong-norm weight
        if wXs > 0: self.wts[(0, 0)] = self.wts[(0, 0)]+wXs*self.base*self.Xs2
        self.active = [d for d in DERIVS if float(self.wts[d].max()) > 0]
        if (0, 0) not in self.active: self.active = [(0, 0)]+self.active
        self.sqw = {d: torch.sqrt(w).reshape(-1) for d, w in self.wts.items()}
    # ---------------------------------------------------------- components
    def F_components(self, Fd, derivs=None):
        comp = {}
        for d in (derivs if derivs is not None else self.active):
            val = Fd[('T', d)].clone()
            for sgn, dp, dr in NL:
                for cf, d1, d2 in LEIB[d]:
                    val += sgn*cf*Fd[('psi', (dp[0]+d1[0], dp[1]+d1[1]))]*Fd[('rho', (dr[0]+d2[0], dr[1]+d2[1]))]
            comp[d] = val
        return comp
    def objective_parts(self, a, derivs=None):
        Fd = self.fields(a); comp = self.F_components(Fd, derivs)
        parts = {d: float(torch.sum(self.wts[d]*comp[d]**2)) for d in self.active}
        if self.kap_rows: parts['kappa'] = sum(float(torch.sum(w*Fd[key]**2)) for key, w in self.kap_rows)
        return parts, comp, Fd
    def objective_value2(self, a):
        parts, _, _ = self.objective_parts(a); return sum(parts.values())
    def norms_report(self, a=None, comp=None, Fd=None):
        """FLOAT norms on the mesh (0 <= r_cut <= r <= r_max, four quadrants): G0 = ||F||_2, G1 = ||grad F||_2, P2 = ||omega D^2 F||_2,
        rF = ||rF||_2, Flog = ||F||_(ds dtheta), supF = sampled max |F|, and the squared-L2 fraction on the mid annulus."""
        if comp is None or Fd is None or any(d not in comp for d in DERIVS):
            Fd = self.fields(a); comp = self.F_components(Fd, DERIVS)
        mesh = self.mesh; r = mesh.r[:, None]; base = self.base; om2 = (1+4*r**2)**0.8
        F = comp[(0, 0)]
        G0sq = float(torch.sum(base*F**2))
        ann = ((mesh.r >= self.mid_range[0]) & (mesh.r < self.mid_range[1])).to(DT)[:, None]
        out = {'G0': math.sqrt(G0sq), 'G1': math.sqrt(float(torch.sum(base*(comp[(1, 0)]**2+comp[(0, 1)]**2)))),
               'P2': math.sqrt(float(torch.sum(base*om2*(comp[(2, 0)]**2+2*comp[(1, 1)]**2+comp[(0, 2)]**2)))),
               'rF': math.sqrt(float(torch.sum(base*r**2*F**2))), 'Flog': math.sqrt(float(torch.sum(4*mesh.W*F**2))),
               'supF': float(F.abs().max()), 'mid_frac': float(torch.sum(base*ann*F**2))/G0sq if G0sq > 0 else 0.0,
               'XsF': math.sqrt(float(torch.sum(base*self.Xs2*F**2)))}
        if Fd is not None:   # (B-L2) screen (c1-n1 diag2 formulas, FLOAT on the mesh): theta = sup(|grad rho| - rho_y)/2, kappa_HS route
            rx, ry = Fd[('rho', (1, 0))], Fd[('rho', (0, 1))]; rxx, rxy, ryy = Fd[('rho', (2, 0))], Fd[('rho', (1, 1))], Fd[('rho', (0, 2))]
            th = float(((torch.sqrt(rx**2+ry**2)-ry)/2).max())
            Drx2 = float(torch.sum(base*(rxx**2+rxy**2))); Dry2 = float(torch.sum(base*(rxy**2+ryy**2)))
            kap = math.sqrt(((math.log(2)-0.5)*Drx2+(3*math.log(2)-2)*Dry2)/(16*math.pi))
            out.update({'theta': th, 'kappa': kap, 'beta0': self.cf+1-th-kap, 'R_L2': out['G0']/(self.cf+1-th-kap)})
        return out
    # ---------------------------------------------------------- normal equations over the active components
    def normal_equations(self, a, block=48, rchunk=106):
        Fd = self.fields(a); comp = self.F_components(Fd)
        n = self.n; dev = self.mesh.device; Nr, Nt = self.mesh.Nr, self.mesh.Nt
        G = torch.zeros(n, n, dtype=DT, device=dev); g = torch.zeros(n, dtype=DT, device=dev); phi = 0.0
        W2 = {d: self.wts[d] for d in self.active}; K2 = [(key, w) for key, w in self.kap_rows]
        for r0 in range(0, Nr, rchunk):
            rs = slice(r0, min(Nr, r0+rchunk)); nr = rs.stop-rs.start
            rows = [torch.sqrt(W2[d][rs])*comp[d][rs] for d in self.active]+[torch.sqrt(w[rs])*Fd[key][rs] for key, w in K2]
            rvec = torch.cat([x.reshape(-1) for x in rows], 0); phi += float((rvec*rvec).sum())
            Jc = torch.zeros(len(rvec), n, dtype=DT, device=dev)
            for b0 in range(0, n, block):
                idx = list(range(b0, min(n, b0+block))); nb = len(idx)
                cache = {}
                def fm(key):
                    if key not in cache:
                        out = torch.zeros(nr, Nt, nb, dtype=DT, device=dev)
                        for j, i in enumerate(idx):
                            for typ, N, arr in self.gslots[i][key]: out[:, :, j] += arr[rs, None]*self.tabs.tab[typ][N][None, :]
                        cache[key] = out
                    return cache[key]
                Jparts = []
                for d in self.active:
                    M = fm(('T', d)).clone()
                    for sgn, dp, dr in NL:
                        for cf, d1, d2 in LEIB[d]:
                            kp = ('psi', (dp[0]+d1[0], dp[1]+d1[1])); kr = ('rho', (dr[0]+d2[0], dr[1]+d2[1]))
                            M += sgn*cf*(Fd[kp][rs][:, :, None]*fm(kr)+Fd[kr][rs][:, :, None]*fm(kp))
                    Jparts.append((M*torch.sqrt(W2[d][rs])[:, :, None]).reshape(-1, nb))
                for key, w in K2:
                    Jparts.append((fm(key)*torch.sqrt(w[rs])[:, :, None]).reshape(-1, nb))
                Jc[:, b0:b0+nb] = torch.cat(Jparts, 0)
                del cache
            G += Jc.T@Jc; g += Jc.T@rvec
            del Jc
        return G, g, phi
    # ---------------------------------------------------------- driver
    def optimize2(self, a0, steps=20, lam0=1e-6, taylor=True, log=None, ckpt=None, verbose=True, lam_min=1e-14, report_every=1, stop_file=None):
        a = np.array(a0, float); lam = lam0; hist = []
        for it in range(1, steps+1):
            if stop_file and os.path.exists(stop_file):
                msg = f'STOP file seen at it {it}'; print(msg, flush=True)
                if log: open(log, 'a').write(msg+'\n')
                break
            t0 = time.time()
            a_new, pred, fcur = self.gn_step2(a, lam, taylor=taylor)
            if taylor: a_new = self.taylor_project(a_new)
            parts, comp, Fd = self.objective_parts(a_new); fnew = sum(parts.values())
            if fnew < fcur: a = a_new; lam = max(lam/3, lam_min); ok = True
            else: lam *= 10; ok = False
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} pred {pred:.3e} lam {lam:.1e} parts ' + ' '.join(f'{k}:{v:.3e}' for k, v in parts.items())
            if ok and (it % report_every == 0):
                nr = self.norms_report(a, comp if all(d in comp for d in DERIVS) else None, Fd)
                msg += ' | ' + ' '.join(f'{k} {v:.5e}' for k, v in nr.items()); hist.append(dict(it=it, obj=fnew, **nr))
            msg += f' ({time.time()-t0:.1f}s)'
            if verbose: print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            if ckpt and ok: np.save(ckpt, a)
        return a, hist

# ---------------------------------------------------------------- exact line search along the GN direction (lane numerics_agent_1 addition)
def _rows(prob, a):
    """all weighted residual rows at a: list of (sqrt-weight (Nr,Nt), value (Nr,Nt)) for the active F components and the kappa rows"""
    Fd = prob.fields(a); comp = prob.F_components(Fd)
    rows = [(torch.sqrt(prob.wts[d]), comp[d]) for d in prob.active]+[(torch.sqrt(w), Fd[key]) for key, w in prob.kap_rows]
    return rows, comp, Fd

def line_search_step(prob, a, delta, tmax=4.0):
    """F(a + t delta) is exactly quadratic in t for every row (F is quadratic in the coefficients, the kappa rows linear):
    F(t) = F0 + t L + t^2 Q with L = (F(a+d) - F(a-d))/2, Q = (F(a+d) + F(a-d))/2 - F0.  The objective along the line is the quartic
    phi(t) = c0 + c1 t + c2 t^2 + c3 t^3 + c4 t^4; its minimizer over 0 < t <= tmax is found from the real roots of phi'.  Returns (t, phi(t), phi(0))."""
    R0, _, _ = _rows(prob, a); Rp, _, _ = _rows(prob, a+delta); Rm, _, _ = _rows(prob, a-delta)
    c = [0.0]*5
    for (sw, f0), (_, fp), (_, fm) in zip(R0, Rp, Rm):
        L = (fp-fm)/2; Q = (fp+fm)/2-f0
        w2 = sw*sw
        ip = lambda u, v: float(torch.sum(w2*u*v))
        c[0] += ip(f0, f0); c[1] += 2*ip(f0, L); c[2] += ip(L, L)+2*ip(f0, Q); c[3] += 2*ip(L, Q); c[4] += ip(Q, Q)
    phi = lambda t: c[0]+c[1]*t+c[2]*t*t+c[3]*t**3+c[4]*t**4
    roots = np.roots([4*c[4], 3*c[3], 2*c[2], c[1]]) if c[4] != 0 else np.roots([3*c[3], 2*c[2], c[1]])
    cands = [float(r.real) for r in roots if abs(r.imag) < 1e-9*max(1.0, abs(r.real)) and 0 < r.real <= tmax]
    cands += list(np.geomspace(1e-5, tmax, 400))           # log-spaced grid safeguard (the GN step may be far too long)
    tbest = min(cands, key=phi)
    if not (phi(tbest) < c[0]*(1-1e-12)): tbest = 0.0      # no decrease along the line: reject (caller raises lam)
    return tbest, phi(tbest), c[0]

def optimize_ls(self, a0, steps=20, lam0=1e-8, taylor=True, log=None, ckpt=None, verbose=True, lam_min=1e-14, lam_max=1e-2, report_every=1, stop_file=None, tmax=2.0):
    """GN/LM direction + exact quartic line search + Taylor projection; lam adapts to the accepted step fraction t."""
    a = np.array(a0, float); lam = lam0; hist = []
    for it in range(1, steps+1):
        if stop_file and os.path.exists(stop_file):
            msg = f'STOP file seen at it {it}'; print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            break
        t0 = time.time()
        a_gn, pred, fcur = self.gn_step2(a, lam, taylor=taylor)
        delta = a_gn-a
        t, phit, phi0 = line_search_step(self, a, delta, tmax=tmax)
        if t > 0:
            a_new = a+t*delta
            if taylor: a_new = self.taylor_project(a_new)
            parts, comp, Fd = self.objective_parts(a_new); fnew = sum(parts.values())
            if fnew < fcur: a = a_new; ok = True
            else: ok = False
        else:
            ok = False; fnew = fcur; parts = {}; comp = None; Fd = None
        if t >= 0.9 and ok: lam = max(lam/3, lam_min)
        elif not ok or t <= 0: lam = min(lam*10, lam_max)
        elif t < 0.3: lam = min(lam*min(100.0, 0.5/t), lam_max)      # overshoot: raise the damping in proportion
        msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} t {t:.3f} phi(t) {phit:.6e} pred {pred:.3e} lam {lam:.1e} parts ' + ' '.join(f'{k}:{v:.3e}' for k, v in parts.items())
        if ok and (it % report_every == 0):
            nr = self.norms_report(a, comp if all(d in comp for d in DERIVS) else None, Fd)
            msg += ' | ' + ' '.join(f'{k} {v:.5e}' for k, v in nr.items()); hist.append(dict(it=it, obj=fnew, t=t, **nr))
        msg += f' ({time.time()-t0:.1f}s)'
        if verbose: print(msg, flush=True)
        if log: open(log, 'a').write(msg+'\n')
        if ckpt and ok: np.save(ckpt, a)
    return a, hist
ProblemN1.optimize_ls = optimize_ls

# ---------------------------------------------------------------- vectorized state fields (lane numerics_agent_1 addition): the slot lists are stacked once
def _build_fast(self):
    """per key and trig type: M (S, Nr, C) stacked radial arrays of the contributing generators of each angular slot N (zero-padded),
    I (S, C) generator indices, T (S, Nt) the angular rows; fields_fast(a) = sum_typ (einsum('snc,sc->sn', M, a[I]).T @ T) per key."""
    dev = self.mesh.device; Nr = self.mesh.Nr
    self.fast = {}
    for key in self.keys:
        per_typ = {}
        for i in range(self.n):
            for typ, N, arr in self.gslots[i][key]:
                per_typ.setdefault(typ, {}).setdefault(N, []).append((i, arr))
        self.fast[key] = {}
        for typ, slots in per_typ.items():
            Ns = sorted(slots); S = len(Ns); C = max(len(slots[N]) for N in Ns)
            Ms = []; Is = np.zeros((S, C), dtype=np.int64)
            for s_, N in enumerate(Ns):
                cols = torch.stack([arr for _, arr in slots[N]], 1)                    # (Nr, c)
                if cols.shape[1] < C: cols = torch.cat([cols, torch.zeros(Nr, C-cols.shape[1], dtype=DT, device=dev)], 1)
                Ms.append(cols); Is[s_, :len(slots[N])] = [i for i, _ in slots[N]]
            M = torch.stack(Ms, 0); I = torch.as_tensor(Is, device=dev)
            T = self.tabs.tab[typ][torch.as_tensor(Ns, device=dev)]
            self.fast[key][typ] = (M, I, T)
    self.fields_slow = self.fields
    self.fields = self.fields_fast
def fields_fast(self, a):
    mesh = self.mesh; at = torch.as_tensor(np.asarray(a, float), dtype=DT, device=mesh.device)
    out = {}
    for key in self.keys:
        tot = torch.zeros(mesh.Nr, mesh.Nt, dtype=DT, device=mesh.device)
        for typ, (M, I, T) in self.fast[key].items():
            rad = torch.einsum('snc,sc->sn', M, at[I])
            tot += rad.T@T
        for (typ, N), arr in self.tail.get(key, {}).items(): tot += arr[:, None]*self.tabs.tab[typ][N][None, :]
        out[key] = tot
    return out
ProblemN1._build_fast = _build_fast; ProblemN1.fields_fast = fields_fast
_orig_init = ProblemN1.__init__
def _init_fast(self, *a, **kw):
    _orig_init(self, *a, **kw)
    if os.environ.get('IPM_FAST_FIELDS', '1') == '1': self._build_fast()
ProblemN1.__init__ = _init_fast

# ---------------------------------------------------------------- multi-damping exact line search (lane numerics_agent_1 addition)
def gn_dir_from_normal(self, a, lam, G, g, taylor=True):
    """GN/LM direction in the constraint null space from precomputed normal equations (G, g): the body of Problem2.gn_step2 after the
    normal equations.  Returns (delta, predicted decrease of the quadratic model)."""
    A, b = self.constraint_matrix() if self.lin_rows else (np.zeros((0, self.n)), np.zeros(0))
    d = b-A@a
    if taylor:
        tv = self.taylor_values(a)[1:]; Jt = self.taylor_jacobian(a)[1:]
        A = np.vstack([A, Jt]); d = np.r_[d, -tv]
    At = torch.as_tensor(A, dtype=DT, device=self.device); dt = torch.as_tensor(d, dtype=DT, device=self.device)
    if not hasattr(self, '_svd_cache') or self._svd_cache[0] is not taylor or self._svd_cache[1].shape != At.shape or not torch.equal(self._svd_cache[1], At):
        U, S, Vh = torch.linalg.svd(At, full_matrices=True)
        rank = int((S > S.max()*1e-13).sum()) if len(S) else 0
        self._svd_cache = (taylor, At.clone(), U, S, Vh, rank)
    _, _, U, S, Vh, rank = self._svd_cache
    Vr = Vh[:rank]; Z = Vh[rank:].T
    dp = Vr.T@((U[:, :rank].T@dt)/S[:rank])
    GZ = Z.T@(G@Z); gZ = Z.T@(g+G@dp)
    colnorm = torch.sqrt(torch.diagonal(GZ).clamp(min=0)); colnorm[colnorm == 0] = 1
    GZs = GZ/colnorm[:, None]/colnorm[None, :]; gZs = gZ/colnorm
    out = []
    lams = lam if hasattr(lam, '__len__') else [lam]
    evals, evecs = torch.linalg.eigh(GZs)                      # the scaled reduced normal matrix is numerically indefinite (eigenvalues down to -1e-6):
    proj = evecs.T@gZs                                          # solve the damped system in the eigenbasis and drop non-positive eigenpairs (descent directions only)
    for lm in lams:
        dmp = evals+lm; keep = dmp > 0
        coef = torch.zeros_like(proj); coef[keep] = proj[keep]/dmp[keep]
        eta = -(evecs@coef)
        eta = eta/colnorm
        delta = dp+Z@eta
        pred = float(-(2*delta@g+delta@(G@delta)))
        out.append((delta.cpu().numpy(), pred))
    return out if hasattr(lam, '__len__') else out[0]

def optimize_mls(self, a0, steps=20, lam0=1e-8, taylor=True, log=None, ckpt=None, verbose=True, lam_min=1e-12, lam_max=1e-1, report_every=1, stop_file=None, tmax=2.0, lam_factors=(0.1, 0.3, 1.0, 3.0, 10.0)):
    """each step: normal equations once; for lam in lam*lam_factors: GN direction and exact quartic line search; take the best (lam, t);
    the accepted lam becomes the center of the next step's set."""
    a = np.array(a0, float); lam = lam0; hist = []
    for it in range(1, steps+1):
        if stop_file and os.path.exists(stop_file):
            msg = f'STOP file seen at it {it}'; print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            break
        t0 = time.time()
        G, g, fcur = self.normal_equations(a)
        lams = [min(max(lam*f, lam_min), lam_max) for f in lam_factors]
        dirs = gn_dir_from_normal(self, a, lams, G, g, taylor=taylor)
        best = None; cands = []
        for lm, (delta, pred) in zip(lams, dirs):
            t, phit, phi0 = line_search_step(self, a, delta, tmax=tmax)
            if t > 0: cands.append((phit, lm, t, delta, pred))
        good = [cnd for cnd in cands if cnd[2] >= 0.3]            # prefer well-scaled directions (line fraction >= 0.3): tiny fractions mean the direction overshoots
        if good: best = min(good, key=lambda cnd: cnd[0])
        elif cands: best = min(cands, key=lambda cnd: cnd[0]); lam = min(lam*10, lam_max)
        if best is None:
            lam = min(lam*100, lam_max); ok = False; fnew = fcur; parts = {}; comp = None; Fd = None; tb = 0.0; lmb = lam; pred = 0.0
        else:
            phit, lmb, tb, delta, pred = best
            ok = False
            for tt in ([tb, tb/2, tb/4, tb/8, tb/16] if taylor else [tb]):      # the Taylor projection spoils long steps: backtrack on the projected point
                a_new = a+tt*delta
                if taylor: a_new = self.taylor_project(a_new)
                parts, comp, Fd = self.objective_parts(a_new); fnew = sum(parts.values())
                if fnew < fcur: a = a_new; ok = True; lam = lmb; tb = tt; break
            if not ok: lam = min(lmb*10, lam_max)
        msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} lam {lmb:.1e} t {tb:.3f} pred {pred:.3e} parts ' + ' '.join(f'{k}:{v:.3e}' for k, v in parts.items())
        if ok and (it % report_every == 0):
            nr = self.norms_report(a, comp if (comp is not None and all(d in comp for d in DERIVS)) else None, Fd)
            msg += ' | ' + ' '.join(f'{k} {v:.5e}' for k, v in nr.items()); hist.append(dict(it=it, obj=fnew, lam=lmb, t=tb, **nr))
        msg += f' ({time.time()-t0:.1f}s)'
        if verbose: print(msg, flush=True)
        if log: open(log, 'a').write(msg+'\n')
        if ckpt and ok: np.save(ckpt, a)
    return a, hist
ProblemN1.gn_dir_from_normal = gn_dir_from_normal; ProblemN1.optimize_mls = optimize_mls

# ---------------------------------------------------------------- general residual rows (lane numerics_agent_1): pointwise linear combinations of the F components
# A row spec is (weight field w (Nr,Nt), {d: coefficient field c_d (Nr,Nt) or float}); the row is sqrt(w) * sum_d c_d comp[d].  The near-field
# Sobolev surrogate of coordinator 2026-11-02T19:56Z item 4a, wQ2 * ||<D>^2 (W F)||_2^2 with W = (1 + r^2/r0^2)^(sigma/2) and
# ||<D>^2 g||^2 = int (g^2 + 2|grad g|^2 + |D^2 g|_F^2) dX, is six such rows (g, g_x, g_y, g_xx, g_xy, g_yy) built by Leibniz from F, grad F, D^2 F.
def add_sobolev2_rows(self, wQ2, sig=1.0, r0=0.25):
    mesh = self.mesh; r = mesh.r[:, None]*torch.ones_like(mesh.W); cs = mesh.cos[None, :]*torch.ones_like(mesh.W); sn = mesh.sin[None, :]*torch.ones_like(mesh.W)
    x = r*cs; y = r*sn; base = self.base
    A = 1+r**2/r0**2; W = A**(sig/2)
    W1 = sig*r/r0**2*A**(sig/2-1)                                              # dW/dr
    W2 = sig/r0**2*A**(sig/2-1)+sig*(sig/2-1)*2*r**2/r0**4*A**(sig/2-2)          # d2W/dr2
    Wx = W1*x/r; Wy = W1*y/r
    Wxx = W2*x**2/r**2+W1*y**2/r**3; Wyy = W2*y**2/r**2+W1*x**2/r**3; Wxy = (W2-W1/r)*x*y/r**2
    rows = [(wQ2*base, {(0, 0): W}),
            (2*wQ2*base, {(1, 0): W, (0, 0): Wx}), (2*wQ2*base, {(0, 1): W, (0, 0): Wy}),
            (wQ2*base, {(2, 0): W, (1, 0): 2*Wx, (0, 0): Wxx}), (2*wQ2*base, {(1, 1): W, (0, 1): Wx, (1, 0): Wy, (0, 0): Wxy}), (wQ2*base, {(0, 2): W, (0, 1): 2*Wy, (0, 0): Wyy})]
    if not hasattr(self, 'rowspecs'): self.rowspecs = []
    self.rowspecs += rows
    self.active = sorted(set(self.active)|{d for _, cd in rows for d in cd}, key=lambda d: (sum(d), d))
    self.sob2 = (wQ2, sig, r0, W)
def _row_values(self, comp):
    return [torch.sqrt(w)*sum(cd[d]*comp[d] for d in cd) for w, cd in getattr(self, 'rowspecs', [])]
_orig_objective_parts = ProblemN1.objective_parts
def objective_parts_rows(self, a, derivs=None):
    parts, comp, Fd = _orig_objective_parts(self, a, derivs)
    rs = getattr(self, 'rowspecs', [])
    if rs:
        parts['sob2'] = sum(float(torch.sum(rv**2)) for rv in self._row_values(comp))
    return parts, comp, Fd
_orig_normal_equations = ProblemN1.normal_equations
def normal_equations_rows(self, a, block=48, rchunk=106):
    rs = getattr(self, 'rowspecs', [])
    if not rs: return _orig_normal_equations(self, a, block, rchunk)
    Fd = self.fields(a); comp = self.F_components(Fd)
    n = self.n; dev = self.mesh.device; Nr, Nt = self.mesh.Nr, self.mesh.Nt
    G = torch.zeros(n, n, dtype=DT, device=dev); g = torch.zeros(n, dtype=DT, device=dev); phi = 0.0
    W2 = {d: self.wts[d] for d in self.active if float(self.wts[d].max()) > 0}; K2 = [(key, w) for key, w in self.kap_rows]
    for r0_ in range(0, Nr, rchunk):
        rsl = slice(r0_, min(Nr, r0_+rchunk)); nr = rsl.stop-rsl.start
        rows = [torch.sqrt(W2[d][rsl])*comp[d][rsl] for d in W2]+[torch.sqrt(w[rsl])*Fd[key][rsl] for key, w in K2]
        rows += [torch.sqrt(w[rsl])*sum((cd[d][rsl] if torch.is_tensor(cd[d]) else cd[d])*comp[d][rsl] for d in cd) for w, cd in rs]
        rvec = torch.cat([x.reshape(-1) for x in rows], 0); phi += float((rvec*rvec).sum())
        Jc = torch.zeros(len(rvec), n, dtype=DT, device=dev)
        for b0 in range(0, n, block):
            idx = list(range(b0, min(n, b0+block))); nb = len(idx)
            cache = {}
            def fm(key):
                if key not in cache:
                    out = torch.zeros(nr, Nt, nb, dtype=DT, device=dev)
                    for j, i in enumerate(idx):
                        for typ, N, arr in self.gslots[i][key]: out[:, :, j] += arr[rsl, None]*self.tabs.tab[typ][N][None, :]
                    cache[key] = out
                return cache[key]
            Md = {}
            for d in self.active:
                M = fm(('T', d)).clone()
                for sgn, dp, dr in NL:
                    for cf, d1, d2 in LEIB[d]:
                        kp = ('psi', (dp[0]+d1[0], dp[1]+d1[1])); kr = ('rho', (dr[0]+d2[0], dr[1]+d2[1]))
                        M += sgn*cf*(Fd[kp][rsl][:, :, None]*fm(kr)+Fd[kr][rsl][:, :, None]*fm(kp))
                Md[d] = M
            Jparts = [(Md[d]*torch.sqrt(W2[d][rsl])[:, :, None]).reshape(-1, nb) for d in W2]
            Jparts += [(fm(key)*torch.sqrt(w[rsl])[:, :, None]).reshape(-1, nb) for key, w in K2]
            for w, cd in rs:
                M = sum((cd[d][rsl][:, :, None] if torch.is_tensor(cd[d]) else cd[d])*Md[d] for d in cd)
                Jparts.append((M*torch.sqrt(w[rsl])[:, :, None]).reshape(-1, nb))
            Jc[:, b0:b0+nb] = torch.cat(Jparts, 0)
            del cache, Md
        G += Jc.T@Jc; g += Jc.T@rvec
        del Jc
    return G, g, phi
_orig_norms_report = ProblemN1.norms_report
def norms_report_rows(self, a=None, comp=None, Fd=None):
    out = _orig_norms_report(self, a, comp, Fd)
    if comp is None or Fd is None or any(d not in comp for d in DERIVS):
        Fd = self.fields(a); comp = self.F_components(Fd, DERIVS)
    # mesh values of N_2 = ||<D>^2 (W F)||_2 at P-Q2 (sigma 1, r0 1/4) and P-Q1 (sigma 7/5, r0 1/4), FLOAT, r <= r_max (no far part)
    mesh = self.mesh; r = mesh.r[:, None]*torch.ones_like(mesh.W); cs = mesh.cos[None, :]*torch.ones_like(mesh.W); sn = mesh.sin[None, :]*torch.ones_like(mesh.W); x = r*cs; y = r*sn
    for name, sig, r0 in (('N2_PQ2', 1.0, 0.25), ('N2_PQ1', 1.4, 0.25)):
        A = 1+r**2/r0**2; W = A**(sig/2); W1 = sig*r/r0**2*A**(sig/2-1); W2_ = sig/r0**2*A**(sig/2-1)+sig*(sig/2-1)*2*r**2/r0**4*A**(sig/2-2)
        Wx = W1*x/r; Wy = W1*y/r; Wxx = W2_*x**2/r**2+W1*y**2/r**3; Wyy = W2_*y**2/r**2+W1*x**2/r**3; Wxy = (W2_-W1/r)*x*y/r**2
        F = comp[(0, 0)]; g = W*F; gx = W*comp[(1, 0)]+Wx*F; gy = W*comp[(0, 1)]+Wy*F
        gxx = W*comp[(2, 0)]+2*Wx*comp[(1, 0)]+Wxx*F; gxy = W*comp[(1, 1)]+Wx*comp[(0, 1)]+Wy*comp[(1, 0)]+Wxy*F; gyy = W*comp[(0, 2)]+2*Wy*comp[(0, 1)]+Wyy*F
        out[name] = math.sqrt(float(torch.sum(self.base*(g**2+2*(gx**2+gy**2)+gxx**2+2*gxy**2+gyy**2))))
        out[name+'_WF'] = math.sqrt(float(torch.sum(self.base*g**2))); out[name+'_D2'] = math.sqrt(float(torch.sum(self.base*(gxx**2+2*gxy**2+gyy**2))))
    return out
ProblemN1.add_sobolev2_rows = add_sobolev2_rows; ProblemN1._row_values = _row_values
ProblemN1.objective_parts = objective_parts_rows; ProblemN1.normal_equations = normal_equations_rows; ProblemN1.norms_report = norms_report_rows
