"""Problem3 (lane c1-n1): Problem2 (E_2-balanced proxy) plus explicit weak-pairing rows (theory_v02 NORM-T-WEAK-v1, a = 0):
  I_k(a) = int_{R^2} F(a) phi_k dX,  phi_k = y t^k u0^2,  t = r^2/(1+r^2), u0 = 1/(1+r^2),  k in pair_k,
entering the least-squares objective as rows sqrt(wpair) I_k (I_k is quadratic in the coefficients; the rows are handled by Gauss-Newton like the
kappa rows).  The mesh integral is restricted to r_cut <= r <= r_max (no far correction: for the candidates of this lane the part beyond 1e4 is
below 1e-12).  Everything else (constraints, Taylor rows, chunked normal equations) is inherited from ipm_opt2.Problem2."""
import math, time, os
import numpy as np
import torch
import ipm_opt2 as O2
DT = torch.float64
DERIVS = O2.DERIVS; LEIB = O2.LEIB; NL = O2.NL

class Problem3(O2.Problem2):
    def __init__(self, gens, c_exact, mesh, wpair=0.0, pair_k=tuple(range(9)), pair_mode='penalty', **kw):
        # pair_mode 'penalty': rows sqrt(w_k) I_k in the least-squares objective;  'constraint': the pairings I_k = 0 are imposed as linearized
        # constraint rows (Newton on the quadratic functionals, like the Taylor rows) inside the null-space Gauss-Newton step; no weights needed.
        super().__init__(gens, c_exact, mesh, **kw)
        self.pair_mode = pair_mode
        r = mesh.r[:, None]; sn = mesh.sin[None, :]
        maskr = ((mesh.r >= self.r_cut) & (mesh.r <= self.r_max)).to(DT)[:, None]*torch.ones_like(mesh.W)
        base = 4*mesh.W*r**2*maskr
        u0 = 1/(1+r**2); t = r**2*u0; y = r*sn
        self.wpair = wpair; self.pair_k = tuple(pair_k)
        # pair_k entries: an integer k (first-mode probe phi_k = y t^k u0^2) or a pair (n, K) (angular probe phi_(n,K) = r v^2 t^K sin(n theta), N4-160; n odd, 2K+1 >= n)
        self.pair_k = tuple((int(q[0]), int(q[1])) if hasattr(q, '__len__') else int(q) for q in pair_k)
        ws = list(wpair) if hasattr(wpair, '__len__') else [wpair]*len(self.pair_k)       # per-row weights allowed
        assert len(ws) == len(self.pair_k)
        th = mesh.theta[None, :]
        def probe(q):
            if hasattr(q, '__len__'): n, K = q; return base*r*u0**2*t**K*torch.sin(n*th)
            return base*y*t**q*u0**2
        self.pair = [(probe(q), w) for q, w in zip(self.pair_k, ws)] if (max(ws) > 0 or pair_mode == 'constraint') else []   # phi dX (Nr, Nt)
        self.last_Jp = None
        self.last_Ik = None
    def pairings(self, F):
        return [float(torch.sum(phi*F)) for phi, _ in self.pair]
    def objective_parts(self, a):
        parts, comp, Fd = super().objective_parts(a)
        if self.pair:
            Ik = self.pairings(comp[(0, 0)]); self.last_Ik = Ik
            parts['pair'] = sum(w*I*I for (phi, w), I in zip(self.pair, Ik)) if self.pair_mode == 'penalty' else 0.0
        return parts, comp, Fd
    def normal_equations(self, a, block=48, rchunk=106):
        Fd = self.fields(a); comp = self.F_components(Fd)
        n = self.n; dev = self.mesh.device; Nr, Nt = self.mesh.Nr, self.mesh.Nt
        G = torch.zeros(n, n, dtype=DT, device=dev); g = torch.zeros(n, dtype=DT, device=dev); phi = 0.0
        W2 = {d: self.wts[d] for d in DERIVS}; K2 = [(key, w) for key, w in self.kap_rows]
        npair = len(self.pair)
        Ik = self.pairings(comp[(0, 0)]) if npair else []
        Jp = torch.zeros(npair, n, dtype=DT, device=dev)
        for r0 in range(0, Nr, rchunk):
            rs = slice(r0, min(Nr, r0+rchunk)); nr = rs.stop-rs.start
            rows = [torch.sqrt(W2[d][rs])*comp[d][rs] for d in DERIVS]+[torch.sqrt(w[rs])*Fd[key][rs] for key, w in K2]
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
                for d in DERIVS:
                    M = fm(('T', d)).clone()
                    for sgn, dp, dr in NL:
                        for cf, d1, d2 in LEIB[d]:
                            kp = ('psi', (dp[0]+d1[0], dp[1]+d1[1])); kr = ('rho', (dr[0]+d2[0], dr[1]+d2[1]))
                            M += sgn*cf*(Fd[kp][rs][:, :, None]*fm(kr)+Fd[kr][rs][:, :, None]*fm(kp))
                    if d == (0, 0) and npair:
                        for k, (ph, w) in enumerate(self.pair):
                            Jp[k, b0:b0+nb] += (ph[rs][:, :, None]*M).sum((0, 1))
                    Jparts.append((M*torch.sqrt(W2[d][rs])[:, :, None]).reshape(-1, nb))
                for key, w in K2:
                    Jparts.append((fm(key)*torch.sqrt(w[rs])[:, :, None]).reshape(-1, nb))
                Jc[:, b0:b0+nb] = torch.cat(Jparts, 0)
                del cache
            G += Jc.T@Jc; g += Jc.T@rvec
            del Jc
        if self.pair_mode == 'penalty':
            for k, (ph, w) in enumerate(self.pair):
                G += w*torch.outer(Jp[k], Jp[k]); g += w*Ik[k]*Jp[k]; phi += w*Ik[k]**2
        self.last_Ik = Ik; self.last_Jp = Jp
        return G, g, phi
    def gn_step2(self, a, lam, taylor=True, verbose=False):
        if self.pair_mode != 'constraint' or not self.pair:
            return super().gn_step2(a, lam, taylor=taylor, verbose=verbose)
        G, g, phi = self.normal_equations(a)
        A, b = self.constraint_matrix() if self.lin_rows else (np.zeros((0, self.n)), np.zeros(0))
        d = b-A@a
        if taylor:
            tv = self.taylor_values(a)[1:]; Jt = self.taylor_jacobian(a)[1:]
            A = np.vstack([A, Jt]); d = np.r_[d, -tv]
        Jp = self.last_Jp.cpu().numpy(); Ik = np.array(self.last_Ik)
        nrm = np.linalg.norm(Jp, axis=1); nrm[nrm == 0] = 1
        A = np.vstack([A, Jp/nrm[:, None]]); d = np.r_[d, -Ik/nrm]            # linearized pairing rows, unit-normalized
        At = torch.as_tensor(A, dtype=DT, device=self.device); dt = torch.as_tensor(d, dtype=DT, device=self.device)
        U, S, Vh = torch.linalg.svd(At, full_matrices=True)
        rank = int((S > S.max()*1e-13).sum()) if len(S) else 0
        Vr = Vh[:rank]; Z = Vh[rank:].T
        dp = Vr.T@((U[:, :rank].T@dt)/S[:rank])
        GZ = Z.T@(G@Z); gZ = Z.T@(g+G@dp)
        colnorm = torch.sqrt(torch.diagonal(GZ).clamp(min=0)); colnorm[colnorm == 0] = 1
        GZs = GZ/colnorm[:, None]/colnorm[None, :]; gZs = gZ/colnorm
        GZs = GZs+lam*torch.eye(GZs.shape[0], dtype=DT, device=self.device)
        try:
            L = torch.linalg.cholesky(GZs); eta = -torch.cholesky_solve(gZs[:, None], L)[:, 0]
        except Exception:
            eta = -torch.linalg.lstsq(GZs, gZs[:, None]).solution[:, 0]
        eta = eta/colnorm
        delta = dp+Z@eta
        pred = float(-(2*delta@g+delta@(G@delta)))
        return a+delta.cpu().numpy(), pred, phi
    def optimize2(self, a0, steps=20, lam0=1e-6, taylor=True, log=None, ckpt=None, verbose=True):
        a = np.array(a0, float); lam = lam0
        for it in range(1, steps+1):
            t0 = time.time()
            a_new, pred, fcur = self.gn_step2(a, lam, taylor=taylor)
            if taylor: a_new = self.taylor_project(a_new)
            parts, _, _ = self.objective_parts(a_new); fnew = sum(parts.values())
            stepnorm = ''
            if os.environ.get('IPM_STEPNORM'):      # R-TANGENT (theory_v03/v04/v06 request 4): density L^2 norm of the step on the mesh (FLOAT), ||rho(a_new) - rho(a)||_2 = ||rho(a_new - a)||_2 (linear in a)
                mesh = self.mesh; rr = mesh.r[:, None]; base = 4*mesh.W*rr**2
                drho = self.fields(a_new - a)[('rho', (0, 0))]; dn = math.sqrt(float(torch.sum(base*drho**2)))
                dcoef = float(np.linalg.norm(a_new - a)); stepnorm = f' dRho2 {dn:.3e} dCoef {dcoef:.3e}'
            if fnew < fcur: a = a_new; lam = max(lam/3, 1e-14); ok = True
            else: lam *= 10; ok = False
            Imax = max(abs(x) for x in self.last_Ik) if self.last_Ik else 0.0
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} pred {pred:.3e} lam {lam:.1e}' + stepnorm + f' parts F {parts[(0,0)]:.3e} G {parts[(1,0)]+parts[(0,1)]:.3e} P {parts[(2,0)]+parts[(1,1)]+parts[(0,2)]:.3e} K {parts.get("kappa", 0):.3e} PAIR {parts.get("pair", 0):.3e} max|I_k| {Imax:.3e} I_0 {self.last_Ik[0] if self.last_Ik else 0:+.3e} ({time.time()-t0:.1f}s)'
            if verbose: print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            if ckpt and ok: np.save(ckpt, a)
        return a
