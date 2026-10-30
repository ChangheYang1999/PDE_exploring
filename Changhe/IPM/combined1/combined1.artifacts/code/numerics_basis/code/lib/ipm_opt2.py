"""E_2-proxy Gauss-Newton optimizer (lane c1-n1): residual components F, grad F, D^2 F from the symbolic polar layer (ipm_polar).

Objective (quarter-plane integrals times 4, measure dX = r^2 ds dtheta, restricted to r_cut <= r <= r_max):
  Phi(a) = sum_pts W [ wF (1 + hw r^2) F^2 + wG |grad F|^2 + wP omega^2 (F_xx^2 + 2 F_xy^2 + F_yy^2) ],  omega = (1+4r^2)^(2/5)
with default weights wF = 2^18, hw = 20/21 (||F||_H replaced by its Hardy bound ||rF||_2, scaled by hfac), wG = 2^14, wP = 1  (NORM-A2-E2 proxy).
F = T + N,  T = (c r d_r - 1) rho = kappa_p rho[G] - 2c rho[Gtilde]  (stable form),  N = -psi_y rho_x + psi_x rho_y.
Derivatives of N by Leibniz on the field tables; derivatives of T through the same series applied to G and Gtilde.
Linear constraints and the five Taylor equations are handled as in ipm_opt.Problem (shared code: this class extends it).
"""
import math, time
import numpy as np
import torch
import ipm_polar as PL
import ipm_eval as EV
import ipm_opt as OPT
import ipm_exact as X

DT = torch.float64
DERIVS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]          # F components
# Leibniz expansions of D^(i,j)(A B) for the needed orders
def leibniz(i, j):
    out = []
    for i1 in range(i+1):
        for j1 in range(j+1):
            out.append((math.comb(i, i1)*math.comb(j, j1), (i1, j1), (i-i1, j-j1)))
    return out
LEIB = {d: leibniz(*d) for d in DERIVS}
# N = -psi_y rho_x + psi_x rho_y : list of (sign, psi derivative, rho derivative)
NL = [(-1, (0, 1), (1, 0)), (1, (1, 0), (0, 1))]

class Problem2(OPT.Problem):
    def __init__(self, gens, c_exact, mesh, r_cut=0.02, r_max=1e4, wF=2.**18, hw=20/21, wG=2.**14, wP=1.0, device=None, fixed=(), wlog=0.0, wkap=0.0):
        # build the parent (gives constraints, origin jets, evaluator for R_f); then our own field tables
        super().__init__(gens, c_exact, mesh, objective='Jabs', r_cut=r_cut, r_max=r_max, fixed=fixed)
        self.wF, self.hw, self.wG, self.wP = wF, hw, wG, wP
        r = mesh.r[:, None]; sn = mesh.sin[None, :]
        maskr = ((mesh.r >= r_cut) & (mesh.r <= r_max)).to(DT)[:, None]*torch.ones_like(mesh.W)
        base = 4*mesh.W*r**2*maskr                                  # dX over R^2 (4 quadrants)
        omega2 = (1+4*r**2)**0.8*torch.ones_like(mesh.W)
        # wlog: weight of int F^2 ds dtheta (= int F^2 r^-2 dX, equal weight per dyadic annulus: controls the near field); 4 quadrants
        self.wlog, self.wkap = wlog, wkap
        self.wts = {(0, 0): base*wF*(1+hw*r**2)+4*mesh.W*maskr*wlog, (1, 0): base*wG, (0, 1): base*wG, (2, 0): base*wP*omega2, (1, 1): base*wP*omega2*2, (0, 2): base*wP*omega2}
        self.sqw = {d: torch.sqrt(w).reshape(-1) for d, w in self.wts.items()}
        # kappa penalty rows (linear in a): wkap * [(ln2-1/2)(rho_xx^2 + rho_xy^2) + (3 ln2 - 2)(rho_xy^2 + rho_yy^2)]/(16 pi) over R^2  (= wkap * kappa^2)
        c1, c2 = (math.log(2)-0.5)/(16*math.pi), (3*math.log(2)-2)/(16*math.pi)
        self.kap_rows = [(('rho', (2, 0)), base*wkap*c1), (('rho', (1, 1)), base*wkap*(c1+c2)), (('rho', (0, 2)), base*wkap*c2)] if wkap > 0 else []
        self.sqk = [(key, torch.sqrt(w).reshape(-1)) for key, w in self.kap_rows]
        self._build_tables()
    def _build_tables(self):
        mesh = self.mesh; t0 = time.time()
        allg = list(self.gens)+[g for g, _ in self.fixed]
        nleg = max([int(g['spec'][2]) for g in allg if g['spec'][0] in ('leg', 'legq', 'legqs')], default=0)
        Pleg = EV.legendre_t_jets(mesh.t, nleg, 8)
        series_cache = {}
        self.gslots = []        # per generator: dict key -> list of (typ, N, radial array);  keys ('rho',(i,j)), ('psi',(i,j)), ('T',(i,j))
        Nmax = 0
        for g, evg in zip(allg, self.ev_gens+self.ev_fixed):
            n = evg.n
            if n not in series_cache: series_cache[n] = PL.field_series(n, 3, 3)
            FS = series_cache[n]
            if evg.is_direct():
                G, Gt = evg.G_direct(mesh, PL.AMAX+1); G = G[:PL.AMAX+1]
            else:
                Yj, Ytj = evg.Y_jets(mesh, PL.AMAX, Pleg)
                G = PL.radial_primitives(evg.p, Yj, mesh); Gt = PL.radial_primitives(evg.p-1, Ytj, mesh)
            kappa = evg.kappa(self.cf)
            sl = {}
            for key, S in FS.items():
                sl[key] = PL.series_slots(S, G, mesh)
            for d in DERIVS:
                S = FS[('rho', d)]
                a1 = PL.series_slots(S, G, mesh); a2 = PL.series_slots(S, Gt, mesh)
                merged = {}
                for typ, N, arr in a1: merged[(typ, N)] = kappa*arr
                for typ, N, arr in a2: merged[(typ, N)] = merged.get((typ, N), 0)-2*self.cf*arr
                sl[('T', d)] = [(typ, N, arr) for (typ, N), arr in merged.items()]
            for key in sl:
                for typ, N, arr in sl[key]: Nmax = max(Nmax, N)
            self.gslots.append(sl)
        # composite fixed tail: sum of the fixed generators' slots times their coefficients
        self.tail = {}
        for k, (g, v) in enumerate(self.fixed):
            cf = float(X.qfloat(v)); sl = self.gslots[self.n+k]
            for key in sl:
                acc = self.tail.setdefault(key, {})
                for typ, N, arr in sl[key]:
                    acc[(typ, N)] = acc[(typ, N)]+cf*arr if (typ, N) in acc else cf*arr
        self.gslots = self.gslots[:self.n]
        self.tabs = PL.Tables(mesh, Nmax+1)
        self.keys = list(self.gslots[0].keys())
        torch.cuda.synchronize() if mesh.device.type == 'cuda' else None
        self.build_time = time.time()-t0
    # ---------------------------------------------------------- fields of a state
    def fields(self, a):
        mesh = self.mesh; a = np.asarray(a, float)
        out = {}
        for key in self.keys:
            acc = {k: v.clone() for k, v in self.tail.get(key, {}).items()}
            for i in range(self.n):
                if a[i] == 0: continue
                for typ, N, arr in self.gslots[i][key]:
                    k = (typ, N); acc[k] = acc[k]+a[i]*arr if k in acc else a[i]*arr
            tot = torch.zeros(mesh.Nr, mesh.Nt, dtype=DT, device=mesh.device)
            for (typ, N), arr in acc.items(): tot += arr[:, None]*self.tabs.tab[typ][N][None, :]
            out[key] = tot
        return out
    def F_components(self, Fd):
        """F and its derivatives (dict d -> (Nr,Nt)) from the state fields"""
        comp = {}
        for d in DERIVS:
            val = Fd[('T', d)].clone()
            for sgn, dp, dr in NL:
                for cf, d1, d2 in LEIB[d]:
                    val += sgn*cf*Fd[('psi', (dp[0]+d1[0], dp[1]+d1[1]))]*Fd[('rho', (dr[0]+d2[0], dr[1]+d2[1]))]
            comp[d] = val
        return comp
    def objective_parts(self, a):
        Fd = self.fields(a); comp = self.F_components(Fd)
        parts = {d: float(torch.sum(self.wts[d]*comp[d]**2)) for d in DERIVS}
        if self.kap_rows: parts['kappa'] = sum(float(torch.sum(w*Fd[key]**2)) for key, w in self.kap_rows)
        return parts, comp, Fd
    def objective_value2(self, a):
        parts, _, _ = self.objective_parts(a); return sum(parts.values())
    def field_matrix2(self, key, idx):
        mesh = self.mesh
        out = torch.zeros(mesh.Nr, mesh.Nt, len(idx), dtype=DT, device=mesh.device)
        for j, i in enumerate(idx):
            for typ, N, arr in self.gslots[i][key]: out[:, :, j] += arr[:, None]*self.tabs.tab[typ][N][None, :]
        return out
    def normal_equations(self, a, block=48, rchunk=106):
        """Gauss-Newton normal matrix G = J^T J and gradient g = J^T r for the E_2-proxy residual (plus kappa rows), accumulated over radial chunks
        of the mesh so that J is never stored (memory ~ chunk size x n).  Returns (G, g, phi = r^T r)."""
        Fd = self.fields(a); comp = self.F_components(Fd)
        n = self.n; dev = self.mesh.device; Nr, Nt = self.mesh.Nr, self.mesh.Nt
        G = torch.zeros(n, n, dtype=DT, device=dev); g = torch.zeros(n, dtype=DT, device=dev); phi = 0.0
        W2 = {d: self.wts[d] for d in DERIVS}; K2 = [(key, w) for key, w in self.kap_rows]
        for r0 in range(0, Nr, rchunk):
            rs = slice(r0, min(Nr, r0+rchunk)); nr = rs.stop-rs.start
            # residual rows of this chunk
            rows = [torch.sqrt(W2[d][rs])*comp[d][rs] for d in DERIVS]+[torch.sqrt(w[rs])*Fd[key][rs] for key, w in K2]
            rvec = torch.cat([x.reshape(-1) for x in rows], 0); phi += float((rvec*rvec).sum())
            # Jacobian of this chunk, generator block by block
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
                    Jparts.append((M*torch.sqrt(W2[d][rs])[:, :, None]).reshape(-1, nb))
                for key, w in K2:
                    Jparts.append((fm(key)*torch.sqrt(w[rs])[:, :, None]).reshape(-1, nb))
                Jc[:, b0:b0+nb] = torch.cat(Jparts, 0)
                del cache
            G += Jc.T@Jc; g += Jc.T@rvec
            del Jc
        return G, g, phi
    def gn_step2(self, a, lam, taylor=True, verbose=False):
        G, g, phi = self.normal_equations(a)
        A, b = self.constraint_matrix() if self.lin_rows else (np.zeros((0, self.n)), np.zeros(0))
        d = b-A@a
        if taylor:
            tv = self.taylor_values(a)[1:]; Jt = self.taylor_jacobian(a)[1:]
            A = np.vstack([A, Jt]); d = np.r_[d, -tv]
        At = torch.as_tensor(A, dtype=DT, device=self.device); dt = torch.as_tensor(d, dtype=DT, device=self.device)
        U, S, Vh = torch.linalg.svd(At, full_matrices=True)
        rank = int((S > S.max()*1e-13).sum()) if len(S) else 0
        Vr = Vh[:rank]; Z = Vh[rank:].T
        dp = Vr.T@((U[:, :rank].T@dt)/S[:rank])
        # minimize ||r + J(dp + Z eta)||^2:  (Z^T G Z) eta = -Z^T (g + G dp)
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
            if fnew < fcur: a = a_new; lam = max(lam/3, 1e-14); ok = True
            else: lam *= 10; ok = False
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} pred {pred:.3e} lam {lam:.1e} parts F {parts[(0,0)]:.3e} G {parts[(1,0)]+parts[(0,1)]:.3e} P {parts[(2,0)]+parts[(1,1)]+parts[(0,2)]:.3e} K {parts.get("kappa", 0):.3e} ({time.time()-t0:.1f}s)'
            if verbose: print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
            if ckpt and ok: np.save(ckpt, a)
        return a
