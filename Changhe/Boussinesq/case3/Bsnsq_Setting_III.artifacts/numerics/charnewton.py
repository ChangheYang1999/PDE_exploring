"""
Batched characteristic residual R(cG) and LM solver.
  cG (coefficients of G) -> beta = 2(c-1), W; backward characteristics from the residual points;
  F_char -> cF by weighted linear LS;  G_char = e^{-T} Omega_loc + M cF  (M accumulated along trajectories);
  R = w_G * (G_char - G(cG)).
"""
import sys, os, time, math, argparse
import numpy as np, torch, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from numpy.polynomial.legendre import leggauss
torch.set_default_dtype(DT)


def code_hashes():
    d = os.path.dirname(os.path.abspath(__file__))
    return np.array([f + ':' + hashlib.sha256(open(os.path.join(d, f), 'rb').read()).hexdigest() for f in ['bq3core.py', 'charnewton.py', 'fixedsrc.py', 'picard_beta.py', 'constvel.py'] if os.path.exists(os.path.join(d, f))])


class BSplineTorch:
    """Evaluate the p+1 nonzero clamped B-splines and derivatives at query points (Cox-de Boor)."""
    def __init__(self, knots, deg, device):
        self.T = torch.tensor(knots, dtype=DT, device=device)
        self.p = deg
        self.Nb = len(knots) - deg - 1
        self.dev = device

    def eval(self, t):
        """t: (...,) in [0,1). Returns span index (...,) [first basis index], N (..., p+1), dN (..., p+1)."""
        T, p = self.T, self.p
        tt = torch.clamp(t, 0.0, 1.0 - 1e-15)
        # span i such that T[i] <= t < T[i+1], with p <= i <= Nb-1
        i = torch.searchsorted(T, tt.reshape(-1).contiguous(), right=True) - 1
        i = torch.clamp(i, p, self.Nb - 1).reshape(tt.shape)
        shp = tt.shape
        N = torch.zeros(shp + (p + 1,), dtype=DT, device=self.dev)
        N[..., 0] = 1.0
        left = torch.zeros(shp + (p + 1,), dtype=DT, device=self.dev)
        right = torch.zeros(shp + (p + 1,), dtype=DT, device=self.dev)
        Nprev = None
        for j in range(1, p + 1):
            left[..., j] = tt - T[i + 1 - j]
            right[..., j] = T[i + j] - tt
            saved = torch.zeros(shp, dtype=DT, device=self.dev)
            Nnew = torch.zeros_like(N)
            if j == p:
                Nprev = N.clone()
            for r in range(j):
                denom = right[..., r + 1] + left[..., j - r]
                temp = N[..., r] / denom
                Nnew[..., r] = saved + right[..., r + 1] * temp
                saved = left[..., j - r] * temp
            Nnew[..., j] = saved
            N = Nnew
        # derivatives from degree p-1 basis Nprev (first p entries): N'_{i-p+r} = p (Nprev[r-1]/(T[i+r]-T[i+r-p]) - Nprev[r]/(T[i+r+1]-T[i+r+1-p]))
        dN = torch.zeros_like(N)
        for r in range(p + 1):
            a = torch.zeros(shp, dtype=DT, device=self.dev); b = torch.zeros(shp, dtype=DT, device=self.dev)
            if r >= 1:
                d1 = T[i + r] - T[i + r - p]
                a = Nprev[..., r - 1] / torch.where(d1 == 0, torch.ones_like(d1), d1)
            if r <= p - 1:
                d2 = T[i + r + 1] - T[i + r + 1 - p]
                b = Nprev[..., r] / torch.where(d2 == 0, torch.ones_like(d2), d2)
            dN[..., r] = p * (a - b)
        return i - p, N, dN


class CharResidual:
    def __init__(self, basis, L, beta_basis, Nphi_res=16, r_in=1e-3, dt=0.02, max_steps=20000, device='cuda', fl=0.1,
                 beta_fixed=None, wc=100.0, eps=1.0, cG_ext=None, rmap='r', include_RF=True):
        self.rmap = rmap
        self.include_RF = include_RF
        self.beta_fixed = beta_fixed
        self.wc = wc
        self.eps = eps            # homotopy: W from U_rel[eps*Omega + (1-eps)*Omega_ext]
        self.cG_ext = cG_ext
        self.b = basis
        self.L = L
        self.beta_basis = beta_basis
        self.dev = device
        self.r_in, self.dt, self.max_steps = r_in, dt, max_steps
        self.g = Geometry(basis, beta_basis, L, rmap=rmap)   # representation geometry (collocation nodes = interp nodes)
        # residual points: same radii, fewer angles
        self.bres = Basis(basis.Nt, basis.deg, basis.K, Nphi_res, ng_coll=len(basis.t_coll) // basis.Nt, m_reg=basis.m_reg,
                          device=device, grade=basis.grade)
        self.gres = Geometry(self.bres, beta_basis, L, rmap=rmap)
        self.X0 = torch.stack([self.gres.x, self.gres.y], 1)      # (Nq, 2)
        self.Nq = self.X0.shape[0]
        self.K, self.Nb = basis.K, basis.Nb
        self.ng = len(basis.t_coll) // basis.Nt
        xi = leggauss(self.ng)[0]
        wbar = np.array([1.0 / np.prod([xi[j] - xi[m] for m in range(self.ng) if m != j]) for j in range(self.ng)])
        self.xi = torch.tensor(xi, dtype=DT, device=device); self.wbar = torch.tensor(wbar, dtype=DT, device=device)
        # monomial coefficients of the Lagrange basis polynomials on [-1,1]: ell_j(xi) = sum_n Lmono[j,n] xi^n
        V = np.vander(xi, increasing=True)                      # V[i,n] = xi_i^n ; ell_j(xi_i) = delta_ij -> Lmono = inv(V)^T
        self.Lmono = torch.tensor(np.linalg.inv(V).T.copy(), dtype=DT, device=device)   # (ng, ng): [j, n]
        self.pk = torch.tensor([2.0 + (k % 2) for k in range(1, self.K + 1)], dtype=DT, device=device)  # Psi_k / r^{pk} smooth in r^2
        self.edges = torch.tensor(basis.edges, dtype=DT, device=device)
        self.grade = basis.grade
        self.ks = torch.arange(1, self.K + 1, dtype=DT, device=device)
        self.kk = torch.arange(0, self.K, dtype=DT, device=device)
        self.spl = BSplineTorch(basis.knots, basis.deg, device)
        self.active = self.g.active                                  # (K*Nb,) bool
        self.mask_k = self.g.mask_k                                  # (K, Nb) float
        # weights for the fits/residuals: radial envelope D(t) at residual points
        tres = self.bres.t_coll_t
        self.DresF = ((1 - tres) ** self.g.pF)[:, None].expand(self.bres.Nc, Nphi_res).reshape(-1)
        self.DresG = ((1 - tres) ** self.g.pG)[:, None].expand(self.bres.Nc, Nphi_res).reshape(-1)
        self.wF = 1.0 / self.DresF
        self.wG = 1.0 / self.DresG
        # pseudo-inverse for the F fit: cF = P (wF * F_char)
        A = (self.gres.Phi0F * self.wF[:, None])[:, self.active]
        self.P = torch.linalg.pinv(A, rtol=1e-12)
        AG = (self.gres.Phi0G * self.wG[:, None])[:, self.active]
        self.PG = torch.linalg.pinv(AG, rtol=1e-12)                 # fit of a transported G -> coefficients (active)
        self.c_op_act = self.g.c_op[self.active]
        self.free_a0 = True        # fixed beta: the temperature amplitude a0 is slaved by ell(a0 G_char) = 1 + beta/2
        self.fl = fl

    # ------------------------------------------------------------- interpolation (batched)
    def interp(self, t, nodal, deriv=False, grid=None):
        """Piecewise Lagrange interpolation on the Gauss nodes of each knot interval.
        t: (B, Nq); nodal: (B, Nc, M) -> values (B, Nq, M) [and d/dt (B, Nq, M) if deriv].
        Uses precomputed monomial coefficients of the Lagrange basis on the reference interval (no 1/(xi - xi_j)).
        grid: optional descriptor dict(Nt, edges, grade, ng, Lmono) of ANOTHER radial grid (the fixed source block's own basis)."""
        if grid is None:
            Nt, edges, grade, ng, Lmono = self.b.Nt, self.edges, self.grade, self.ng, self.Lmono
        else:
            Nt, edges, grade, ng, Lmono = grid['Nt'], grid['edges'], grid['grade'], grid['ng'], grid['Lmono']
        u = torch.clamp(t, 0.0, 1.0 - 1e-15)
        idx = torch.clamp((Nt * u ** (1.0 / grade)).floor().long(), 0, Nt - 1)
        a = edges[idx]; bb = edges[idx + 1]
        xi = 2 * (u - a) / (bb - a) - 1                                                   # (B, Nq)
        gidx = idx[..., None] * ng + torch.arange(ng, device=t.device)                   # (B, Nq, ng)
        B = nodal.shape[0]
        vals = torch.gather(nodal, 1, gidx.reshape(B, -1, 1).expand(-1, -1, nodal.shape[2])).reshape(B, t.shape[1], ng, -1)
        coef = torch.einsum('jn,bqjm->bqnm', Lmono, vals)                                # monomial coeffs (B,Nq,ng,M)
        # Horner
        p = coef[:, :, -1, :]
        dp = torch.zeros_like(p)
        for n in range(ng - 2, -1, -1):
            dp = dp * xi[..., None] + p
            p = p * xi[..., None] + coef[:, :, n, :]
        if not deriv:
            return p
        dxidt = 2.0 / (bb - a)
        return p, dp * dxidt[..., None]

    # ------------------------------------------------------------- state from cG batch
    def prepare(self, cG_unk):
        """cG_unk: (B, N) unknown coefficients. The velocity uses cG = eps*cG_unk + (1-eps)*cG_ext.
        Computes beta (B,), nodal data (B, Nc, 3K), jets."""
        g, b = self.g, self.b
        K, Nb, Nc = self.K, self.Nb, b.Nc
        Bn = cG_unk.shape[0]
        # fixed SOURCE-VELOCITY block (fixedsrc.make_source_block): the source f stays in its seed representation; only its
        # strain / centre Taylor data enter here, its velocity is added in self.velocity (interpolated in the seed's own t)
        src = getattr(self, 'src', None)
        lam_s = src['lam'] if src is not None else 0.0
        if self.beta_fixed is not None:
            # exact centre constraint: project the unknown coefficients onto {c_unk + lam c_f = 1 + beta/2} along d = c_op (active part)
            d = g.c_op * self.active.to(DT)
            target = 1 + self.beta_fixed / 2 - (lam_s * src['c'] if src is not None else 0.0)
            cG_unk = cG_unk + d[None] * ((target - cG_unk @ g.c_op) / (g.c_op @ d))[:, None]
        self.cG_proj = cG_unk
        if self.eps != 1.0 and self.cG_ext is not None:
            cG = self.eps * cG_unk + (1 - self.eps) * self.cG_ext[None]
        else:
            cG = cG_unk
        if getattr(self, 'cG_f', None) is not None:
            # manufactured problems: fixed additive vorticity source in the velocity only (W from Omega_mixed + Omega_f)
            cG = cG + self.cG_f[None]
        c = cG @ g.c_op
        if src is not None:
            c = c + lam_s * src['c']
        beta = 2 * (c - 1) if self.beta_fixed is None else torch.full_like(c, self.beta_fixed)
        self.c_last = c
        Psi = torch.einsum('kia,ba->bki', g.Psi_op, cG)                    # (B, K, Nc)
        r = g.r
        S = Psi / (r[None, None, :] ** self.pk[None, :, None])              # S_k = Psi_k / r^{2 + (k mod 2)}
        nodal = S.transpose(1, 2).contiguous()                             # (B, Nc, K)
        # jets
        wq = b.w_quad_t * g.drdtq; rq = g.rq
        def gq(k):
            return (cG[:, k * Nb:(k + 1) * Nb] @ g.Wq_k[k].T) / rq
        def Omq(k):
            lo = gq(k - 1) * (1.0 if k == 1 else 0.5)
            hi = 0.5 * gq(k + 1) if k + 1 < K else 0.0
            return rq * (lo - hi)
        h20 = 0.25 * (Omq(2) / rq) @ wq
        h30 = (1.0 / 6.0) * (Omq(3) / rq ** 2) @ wq if K >= 3 else torch.zeros(Bn, dtype=DT, device=self.dev)
        h40 = (1.0 / 8.0) * (Omq(4) / rq ** 3) @ wq if K >= 4 else torch.zeros(Bn, dtype=DT, device=self.dev)
        G0 = cG[:, 0]
        g1p = g.g1prime0(cG) if K > 1 else torch.zeros(Bn, dtype=DT, device=self.dev)
        if src is not None:
            # centre Taylor data of the source stream function (linear functionals computed once in the seed geometry)
            h20 = h20 + lam_s * src['h20']; h30 = h30 + lam_s * src['h30']; h40 = h40 + lam_s * src['h40']
            G0 = G0 + lam_s * src['G0']; g1p = g1p + lam_s * src['g1p']
        om22 = 0.5 * g1p
        h11_ = -G0 / 8.0
        h21 = -om22 / 12.0
        h01 = -2 * h20
        h10 = h11_ - h30
        h02 = h11_ + 3 * h30
        h11 = -2 * h21 + 4 * h40
        b0 = 4.0 / beta
        f01 = 4 * h02 / (beta + h01)
        f10 = (2 * h11 - 3 * h10 * f01) / (beta - 2)
        g01 = (2 * f01 + 2 * h02 * b0) / (2 * beta + 1)
        g10 = (4 * f10 + h11 * b0 - 3 * h10 * g01) / (1.5 * beta - 2)
        # y^2 terms (astra review 14:52Z): e = y^3 coefficient of H = -2 h21 - 4 h40
        e3 = -2 * h21 - 4 * h40
        f02 = (3 * h02 * f01 + 6 * e3) / (3 * beta + 2)
        g02 = (2 * f02 + h02 * g01 + 3 * e3 * b0) / (3 * beta + h01 + 1)
        jet = dict(b0=b0, f01=f01, f10=f10, g01=g01, g10=g10, c=h01, f02=f02, g02=g02)
        return beta, nodal, jet

    # ------------------------------------------------------------- velocity (batched)
    def velocity(self, X, beta, nodal):
        """X: (B, Nq, 2) -> W (B, Nq, 2), plus (r, phi, t, x) for reuse"""
        K, L = self.K, self.L
        x, y = X[..., 0], X[..., 1]
        sx = torch.where(x < 0, -torch.ones_like(x), torch.ones_like(x))
        xa = x.abs()
        r = torch.sqrt(xa ** 2 + y ** 2)
        phi = torch.atan2(xa, -y)
        t = self.g.t_of_r(r)
        S, dSdt = self.interp(t, nodal, deriv=True)                       # (B, Nq, K)
        _, drdt = self.g.r_of_t(t)
        rp = r[..., None] ** self.pk                                       # r^{pk}
        Psi = rp * S
        dPsi = self.pk * rp / r[..., None] * S + rp * dSdt / drdt[..., None]   # exact derivative of the interpolant
        ks = self.ks
        kphi_s = torch.sin(phi[..., None] * ks); kphi_c = torch.cos(phi[..., None] * ks)
        Psir = (dPsi * kphi_s).sum(-1)
        Psiphi = (ks * Psi * kphi_c).sum(-1)
        src = getattr(self, 'src', None)
        if src is not None:
            # fixed source-velocity block (fixedsrc.make_source_block): S_k^f interpolated on the SOURCE basis's own radial grid and in
            # the SEED geometry's own t (where it is smooth), same piecewise-Lagrange scheme, own mode count K_src; added to Psi_r, Psi_phi
            tS = src['g'].t_of_r(r)
            Sf, dSf = self.interp(tS, src['nodal'].expand(X.shape[0], -1, -1), deriv=True, grid=src['grid'])
            _, drdtS = src['g'].r_of_t(tS)
            pkS, ksS = src['pk'], src['ks']
            rpS = r[..., None] ** pkS
            PsiS = rpS * Sf
            dPsiS = pkS * rpS / r[..., None] * Sf + rpS * dSf / drdtS[..., None]
            Psir = Psir + src['lam'] * (dPsiS * torch.sin(phi[..., None] * ksS)).sum(-1)
            Psiphi = Psiphi + src['lam'] * (ksS * PsiS * torch.cos(phi[..., None] * ksS)).sum(-1)
        s, cph = torch.sin(phi), torch.cos(phi)
        U2 = s * Psir + cph / r * Psiphi
        U1 = cph * Psir - s / r * Psiphi
        W = torch.stack([sx * (beta[:, None] * xa + U1), beta[:, None] * y + U2], -1)
        return W, (r, phi, t, x)

    def thx_basis(self, aux):
        """Theta_x of all F basis functions at points: returns span (B,Nq) and values (B, Nq, K, p+1):
        Theta_x^{(k,j)} = 2x[ F + (r s^2/2) F_r + (s c/2) F_phi ] with F = fac_k(t) B_j(t) cos k phi.  Vectorised over k."""
        r, phi, t, x = aux
        K = self.K; p = self.b.deg; g = self.g
        span, Nv, dNv = self.spl.eval(t)                           # (B,Nq), (B,Nq,p+1)
        _, drdt = g.r_of_t(t)
        facs, dfacs = [], []
        for k in range(K):
            f_, df_ = g.radial_factor(k, t, g.pF)
            facs.append(f_); dfacs.append(df_)
        fac = torch.stack(facs, -1); dfac = torch.stack(dfacs, -1)                        # (B,Nq,K)
        s, cph = torch.sin(phi), torch.cos(phi)
        jidx = span[..., None] + torch.arange(p + 1, device=self.dev)                      # (B,Nq,p+1)
        # mask: spline index must be active for mode k: mask_k[k, j]
        maskKL = self.mask_k[:, jidx]                                                      # (K, B, Nq, p+1)
        maskKL = maskKL.permute(1, 2, 0, 3)                                                # (B,Nq,K,p+1)
        kphi = phi[..., None] * self.kk
        ck, sk = torch.cos(kphi), torch.sin(kphi)                   # (B,Nq,K)
        F = (fac * ck)[..., None] * Nv[..., None, :] * maskKL        # (B,Nq,K,p+1)
        Fr = ((dfac * ck)[..., None] * Nv[..., None, :] + (fac * ck)[..., None] * dNv[..., None, :]) / drdt[..., None, None] * maskKL
        Fphi = -(self.kk * fac * sk)[..., None] * Nv[..., None, :] * maskKL
        F1 = F + 0.5 * ((r * s ** 2)[..., None, None] * Fr + (s * cph)[..., None, None] * Fphi)
        return span, 2 * x[..., None, None] * F1

    # ------------------------------------------------------------- residual
    def run(self, cG, return_all=False, use_graph=None):
        """cG: (B, N). Returns R (B, Nq) weighted residual of the G equation, and diagnostics.
        use_graph: capture one RK4 step in a CUDA graph and replay it (default: self.use_graph)."""
        if use_graph is None:
            use_graph = getattr(self, 'use_graph', False)
        Bn = cG.shape[0]
        beta, nodal, jet = self.prepare(cG)
        Nq, K, Nb, p = self.Nq, self.K, self.Nb, self.b.deg
        dt = self.dt
        X = self.X0[None].expand(Bn, -1, -1).clone()
        T = torch.zeros(Bn, Nq, dtype=DT, device=self.dev)
        M = torch.zeros(Bn, Nq, K * Nb, dtype=DT, device=self.dev)
        done = torch.zeros(Bn, Nq, dtype=torch.bool, device=self.dev)
        rin = self.r_in
        idx_base = (torch.arange(K, device=self.dev) * Nb)[None, None, :, None]
        ar_p = torch.arange(p + 1, device=self.dev)[None, None, None, :]

        def stage(Xs, Ts):
            W, aux = self.velocity(Xs, beta, nodal)
            span, thx = self.thx_basis(aux)
            idx = idx_base + span[..., None, None] + ar_p
            contrib = torch.exp(-Ts)[..., None, None] * thx
            return -W, idx.reshape(Bn, Nq, -1), contrib.reshape(Bn, Nq, -1)

        def step():
            act = (~done).to(DT)
            k1, i1, c1 = stage(X, T)
            k2, i2, c2 = stage(X + 0.5 * dt * k1, T + 0.5 * dt)
            k3, i3, c3 = stage(X + 0.5 * dt * k2, T + 0.5 * dt)
            k4, i4, c4 = stage(X + dt * k3, T + dt)
            Xn = X + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            a3 = (act * dt / 6)[..., None]
            M.scatter_add_(2, i1, a3 * c1); M.scatter_add_(2, i2, 2 * a3 * c2)
            M.scatter_add_(2, i3, 2 * a3 * c3); M.scatter_add_(2, i4, a3 * c4)
            X.copy_(torch.where(act[..., None] > 0, Xn, X))
            T.add_(act * dt)
            rn = torch.sqrt(X[..., 0] ** 2 + X[..., 1] ** 2)
            done.copy_(done | (rn < rin))

        steps = 0
        if use_graph:
            # capture on a side stream after warm-up on copies of the state (state restored afterwards)
            X_bak, T_bak, M_bak, done_bak = X.clone(), T.clone(), M.clone(), done.clone()
            s = torch.cuda.Stream()
            s.wait_stream(torch.cuda.current_stream())
            with torch.cuda.stream(s):
                for _ in range(2):
                    step()
            torch.cuda.current_stream().wait_stream(s)
            graph = torch.cuda.CUDAGraph()
            with torch.cuda.graph(graph):
                step()
            X.copy_(X_bak); T.copy_(T_bak); M.copy_(M_bak); done.copy_(done_bak)
            check_every = 25
            for it in range(self.max_steps):
                graph.replay()
                steps += 1
                if steps % check_every == 0 and bool(done.all()):
                    break
        else:
            for it in range(self.max_steps):
                if bool(done.all()):
                    break
                step()
                steps += 1
        self.steps_used = steps; self.n_unfinished = int((~done).sum())
        xe, ye = X[..., 0], X[..., 1]
        se = xe ** 2
        Th_loc = se * (1 + jet['f01'][:, None] * ye + jet['f10'][:, None] * se + jet['f02'][:, None] * ye ** 2)
        Om_loc = xe * (jet['b0'][:, None] + jet['g01'][:, None] * ye + jet['g10'][:, None] * se + jet['g02'][:, None] * ye ** 2)
        Theta = torch.exp((beta[:, None] - 2) * T) * Th_loc
        F_char = Theta / self.X0[None, :, 0] ** 2
        cF = torch.zeros(Bn, K * Nb, dtype=DT, device=self.dev)
        if getattr(self, 'cF_fixed', None) is None:
            cF[:, self.active] = (self.P @ (self.wF[None] * F_char).T).T               # (B, N)
        else:
            # custom evaluation (axis_ode.py): use a GIVEN unit-amplitude temperature representation instead of re-fitting F_char on the
            # residual set (the residual set may be arbitrary points then)
            cF = self.cF_fixed[None].expand(Bn, -1).clone()
        G_char = (torch.exp(-T) * Om_loc + torch.einsum('bqj,bj->bq', M, cF)) / self.X0[None, :, 0]
        if getattr(self, 'custom_points', False):
            return None, dict(beta=beta, cF=cF, F_char=F_char, G_char=G_char, T=T, jet=jet)
        a0 = torch.ones(Bn, dtype=DT, device=self.dev)
        if self.beta_fixed is not None and getattr(self, 'free_a0', False):
            # transported fields are linear in a0; choose a0 so that the strain of the (fitted) transported vorticity
            # equals 1 + beta/2 (astra stall1: the missing scalar compatibility equation of the fixed-beta homotopy)
            ell_char = (self.PG @ (self.wG[None] * G_char).T).T @ self.c_op_act          # (B,)
            src = getattr(self, 'src', None)
            a0 = (1 + self.beta_fixed / 2 - (src['lam'] * src['c'] if src is not None else 0.0)) / ell_char   # total strain incl. the source (astra fixedsrc1)
            F_char = a0[:, None] * F_char; G_char = a0[:, None] * G_char; cF = a0[:, None] * cF
        self.a0_last = a0
        G_rep = (self.gres.Phi0G @ self.cG_proj.T).T          # represented G of the (projected) unknown coefficients
        F_rep = (self.gres.Phi0F @ cF.T).T
        RF = self.wF[None] * (F_char - F_rep)
        RG = self.wG[None] * (G_char - G_rep)
        R = torch.cat([RF, RG], 1) if self.include_RF else RG      # temperature-fit residual in the objective (astra review)
        if self.beta_fixed is not None and self.wc > 0:
            R = torch.cat([R, self.wc * (self.c_last - (1 + self.beta_fixed / 2))[:, None]], 1)
        if return_all:
            return R, dict(beta=beta, cF=cF, F_char=F_char, G_char=G_char, G_rep=G_rep, F_rep=F_rep, T=T, jet=jet, RF=RF, RG=RG, a0=a0)
        return R


def lm_solve(res, cG0, iters=20, lam=1e-3, batch=24, h=1e-6, log=print, save=None, maxtime=3e4, lam_min=1e-10, tik=0.0,
             dfloor=1e-3, maxstep=None, broyden_every=1, tik_k=0.0):
    """broyden_every = n: full FD Jacobian every n iterations, Broyden rank-1 updates in between.
    tik_k > 0: mode-dependent Tikhonov weight tik * (1 + (k/tik_k)^2) on the coefficients of angular mode k."""
    t_start = time.time()
    act = res.active
    cG = cG0.clone(); cG[~act] = 0.0
    N = cG.numel(); Na = int(act.sum())
    idx_act = torch.nonzero(act)[:, 0]
    R, info = res.run(cG[None], return_all=True)
    R = R[0]
    obj = (R ** 2).sum().item()
    log(f"# start obj={obj:.6e} beta={info['beta'].item():.8f} steps={res.steps_used} Na={Na}")
    last_accepted = True; R_prev = None; delta_last = None
    for it in range(iters):
        if time.time() - t_start > maxtime:
            log('# maxtime'); break
        t0 = time.time()
        full = (it % broyden_every == 0) or (it == 0) or ('J' not in dir()) or (not last_accepted)
        if full:
            J = torch.zeros(R.numel(), Na, dtype=DT, device=cG.device)
            for s0 in range(0, Na, batch):
                s1 = min(Na, s0 + batch)
                E = torch.zeros(s1 - s0, N, dtype=DT, device=cG.device)
                E[torch.arange(s1 - s0), idx_act[s0:s1]] = h
                Rp = res.run(cG[None] + E)
                J[:, s0:s1] = ((Rp - R[None]) / h).T
        else:
            # Broyden update with the last accepted step (delta_last, R - R_prev)
            yv = R - R_prev
            J = J + torch.outer(yv - J @ delta_last, delta_last) / (delta_last @ delta_last)
        tJ = time.time() - t0
        JtJ = J.T @ J; Jtr = J.T @ R
        dg = torch.diagonal(JtJ).clone(); dg = torch.maximum(dg, dfloor * dg.max())
        if tik > 0:
            kmode = (idx_act // res.Nb).to(DT)
            wk = (1 + (kmode / tik_k) ** 2) if tik_k > 0 else torch.ones_like(kmode)
            JtJ = JtJ + tik * dg.max() * torch.diag(wk)
            Jtr = Jtr + tik * dg.max() * (wk * cG[act])
        accepted = False
        trial_log = []
        gnorm = Jtr.norm().item(); relgrad = gnorm / max(1e-300, torch.linalg.matrix_norm(J, 2).item() * math.sqrt(obj))
        for trial in range(15):
            try:
                Lc = torch.linalg.cholesky(JtJ + lam * torch.diag(dg))
                delta = -torch.cholesky_solve(Jtr[:, None], Lc)[:, 0]
            except Exception:
                lam *= 10; continue
            if maxstep is not None and delta.abs().max() > maxstep:
                lam *= 4; continue
            cGn = cG.clone(); cGn[act] = cG[act] + delta
            Rn, infon = res.run(cGn[None], return_all=True)
            Rn = Rn[0]
            objn = (Rn ** 2).sum().item()
            pred = obj - ((R + J @ delta) ** 2).sum().item()          # decrease predicted by the linear model
            gain = (obj - objn) / pred if pred != 0 else float('nan')
            trial_log.append(f"lam={lam:.1e} |d|={delta.norm().item():.2e} pred={pred:.3e} act={obj - objn:.3e} gain={gain:.3f}")
            if tik > 0:
                objn_cmp = objn + tik * dg.max().item() * (wk * cGn[act] ** 2).sum().item()
                obj_cmp = obj + tik * dg.max().item() * (wk * cG[act] ** 2).sum().item()
            else:
                objn_cmp, obj_cmp = objn, obj
            if not math.isfinite(objn) or infon['beta'].item() <= 2.0:
                lam *= 10; continue
            if objn_cmp < obj_cmp:
                accepted = True
                R_prev = R
                if res.beta_fixed is not None:
                    cGn = res.cG_proj[0].clone()
                delta_last = (cGn - cG)[act]            # true stored increment (projected when beta is fixed)
                cG, R, info, obj = cGn, Rn, infon, objn
                lam = max(lam / 3, lam_min)
                break
            lam *= 4
        last_accepted = accepted
        sv = torch.linalg.svdvals(J)
        nF = info['RF'][0].abs(); nG = info['RG'][0].abs()
        rr = res.gres.rr
        def reg(v, lo, hi):
            m = (rr >= lo) & (rr < hi)
            return v[m].max().item() if m.any() else float('nan')
        regs = ' '.join(f"{reg(nG, lo, hi):.2e}/{reg(nF, lo, hi):.2e}" for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1e99)])
        log(f"it {it:3d} acc={int(accepted)} J={'full' if full else 'broyden'} lam={lam:.1e} obj={obj:.6e} beta={info['beta'].item():.8f} a0={info['a0'].item():.5f} "
            f"max|wRG|={nG.max().item():.3e} rms={math.sqrt(obj/R.numel()):.3e} max|wRF|={nF.max().item():.3e} "
            f"|cG|max={cG.abs().max().item():.3e} sv[max/min2/min]={sv[0].item():.2e}/{sv[-2].item():.2e}/{sv[-1].item():.2e} "
            f"tJ={tJ:.0f}s dt={time.time()-t0:.0f}s unfinished={res.n_unfinished} regionsG/F[r<1,1-10,10-100,>100]={regs}")
        log(f"   relgrad=|J^T R|/(|J| |R|)={relgrad:.3e} trials: " + ' ; '.join(trial_log))
        if save:
            np.savez(save, cG=cG.cpu().numpy(), cF=info['cF'][0].cpu().numpy(), beta=info['beta'].item(), L=res.L,
                     beta_basis=res.beta_basis, beta_fixed=(res.beta_fixed if res.beta_fixed is not None else -1.0), Nt=res.b.Nt, deg=res.b.deg, K=res.K, Nphi=res.b.Nphi, mreg=res.b.m_reg,
                     ngc=res.ng, grade=res.grade, obj=obj, r_in=res.r_in, dt=res.dt, sv=sv.cpu().numpy(), eps=res.eps, rmap=res.rmap,
                     cG_ext=(res.cG_ext.cpu().numpy() if res.cG_ext is not None else np.zeros(0)), code_sha256=code_hashes(), scheme='mask', a0=info['a0'].item(),
                     saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        if not accepted and lam > 1e8:
            log('# stalled'); break
    return cG, info


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--beta_basis', type=float, default=3.0)
    ap.add_argument('--L', type=float, default=1.0)
    ap.add_argument('--Nt', type=int, default=40)
    ap.add_argument('--deg', type=int, default=5)
    ap.add_argument('--K', type=int, default=16)
    ap.add_argument('--Nphi', type=int, default=32)
    ap.add_argument('--Nphi_res', type=int, default=16)
    ap.add_argument('--ngc', type=int, default=7)
    ap.add_argument('--grade', type=float, default=1.5)
    ap.add_argument('--r_in', type=float, default=1e-3)
    ap.add_argument('--dt', type=float, default=0.02)
    ap.add_argument('--iters', type=int, default=20)
    ap.add_argument('--batch', type=int, default=24)
    ap.add_argument('--lam', type=float, default=1e-3)
    ap.add_argument('--tik', type=float, default=0.0)
    ap.add_argument('--dfloor', type=float, default=1e-3)
    ap.add_argument('--maxstep', type=float, default=None)
    ap.add_argument('--broyden_every', type=int, default=1)
    ap.add_argument('--tik_k', type=float, default=0.0)
    ap.add_argument('--rmap', type=str, default='r', choices=['r', 'r2'])
    ap.add_argument('--graph', type=int, default=1, help='use CUDA graph replay for the RK4 step')
    ap.add_argument('--no_RF', action='store_true', help='exclude the temperature-fit residual from the objective')
    ap.add_argument('--init', type=str, default='')
    ap.add_argument('--c0', type=float, default=2.5, help='initial centre strain (sets beta0 = 2(c0-1))')
    ap.add_argument('--beta_fixed', type=float, default=None, help='fix beta; c = 1 + beta/2 becomes a constraint row')
    ap.add_argument('--wc', type=float, default=0.0, help='penalty weight of the centre row (0: exact projection only)')
    ap.add_argument('--eps', type=float, default=1.0, help='homotopy parameter (1 = B2-P)')
    ap.add_argument('--ext', type=str, default='', help='npz with cG_ext (external vorticity coefficients) for the homotopy')
    ap.add_argument('--ext_gauss', type=str, default='', help='external vorticity A x exp(-(x^2+(y-y0)^2)/(2 s^2)) as "A,y0,s"; A<0 means: choose A for c = c0')
    ap.add_argument('--linear0', action='store_true', help='solve the eps=0 linear problem only: cG = fit(G_char[W_ext]) and report')
    ap.add_argument('--out', type=str, default='runs/char.npz')
    ap.add_argument('--log', type=str, default='')
    ap.add_argument('--maxtime', type=float, default=3e4)
    args = ap.parse_args()
    dev = 'cuda'
    logf = open(args.log, 'a') if args.log else None
    def log(s):
        print(s, flush=True)
        if logf: logf.write(s + '\n'); logf.flush()
    log(f"# charnewton start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
    b = Basis(args.Nt, args.deg, args.K, args.Nphi, ng_coll=args.ngc, m_reg=2, device=dev, grade=args.grade)
    cG_ext = None
    if args.ext:
        cG_ext = torch.tensor(np.load(args.ext)['cG'], dtype=DT, device=dev)
    res = CharResidual(b, args.L, args.beta_basis, Nphi_res=args.Nphi_res, r_in=args.r_in, dt=args.dt, device=dev,
                       beta_fixed=args.beta_fixed, wc=args.wc, eps=args.eps, cG_ext=cG_ext, rmap=args.rmap, include_RF=not args.no_RF)
    res.use_graph = bool(args.graph)
    if args.ext_gauss:
        A, y0, sg = [float(v) for v in args.ext_gauss.split(',')]
        g0 = res.g
        Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
        wfit = 1.0 / Dt
        Gt = torch.exp(-(g0.x ** 2 + (g0.y - y0) ** 2) / (2 * sg ** 2))
        cfit = torch.linalg.lstsq(g0.Phi0G * wfit[:, None], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
        c_unit = (g0.c_op @ cfit).item()
        if A < 0:
            A = args.c0 / c_unit
        cG_ext = A * cfit
        res.cG_ext = cG_ext
        log(f"# ext_gauss: A={A:.5f} y0={y0} s={sg} c_unit={c_unit:.5f} c_ext={(g0.c_op @ cG_ext).item():.5f} fit err {((g0.Phi0G @ cfit - Gt) * wfit).abs().max().item():.2e}")
    K, Nb = b.K, b.Nb
    if args.init:
        d = np.load(args.init)
        cG0 = torch.tensor(d['cG'], dtype=DT, device=dev)
        assert cG0.numel() == K * Nb
    else:
        cG0 = torch.zeros(K * Nb, dtype=DT, device=dev)
        beta0 = 2 * (args.c0 - 1) if args.beta_fixed is None else args.beta_fixed
        c0 = args.c0 if args.beta_fixed is None else 1 + args.beta_fixed / 2
        # G = (4/beta0) D_G(t) (1 + lam * y/sqrt(r^2+L^2)) -> modes 0 and 1 (y/r = -cos phi); lam from c0
        g0 = res.g
        xs, ys, rs = g0.x, g0.y, g0.rr
        Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
        base = (4.0 / beta0) * Dt
        wfit = 1.0 / Dt
        def fit(vals):
            return torch.linalg.lstsq(g0.Phi0G * wfit[:, None], (vals * wfit)[:, None], driver='gels').solution[:, 0]
        c_base = (g0.c_op @ fit(base)).item()
        c_asym = (g0.c_op @ fit(base * ys / torch.sqrt(rs ** 2 + args.L ** 2))).item()
        lam = (c0 - c_base) / c_asym
        cG0 = fit(base * (1 + lam * ys / torch.sqrt(rs ** 2 + args.L ** 2)))
        log(f"# dipole init: lam={lam:.4f} (Omega>0 in x>0 iff |lam|<=1), c_base={c_base:.4f}, c_asym={c_asym:.4f}")
    log(f"# N={K*Nb} Nq={res.Nq} c0={(res.g.c_op @ cG0).item():.6f} eps={res.eps}")
    if args.linear0:
        # eps = 0: W is given by cG_ext; one characteristic pass gives G_char; fit it.
        res.eps = 0.0
        R, info = res.run(cG0[None], return_all=True)
        wG = res.wG
        PG = torch.linalg.pinv((res.gres.Phi0G * wG[:, None])[:, res.active], rtol=1e-12)
        cGfit = torch.zeros(K * Nb, dtype=DT, device=dev); cGfit[res.active] = PG @ (wG * info['G_char'][0])
        Gfit = res.gres.Phi0G @ cGfit
        log(f"# linear0: beta={info['beta'].item():.8f} max|wRF|={info['RF'][0].abs().max().item():.3e} "
            f"G fit err (weighted) {(wG * (Gfit - info['G_char'][0])).abs().max().item():.3e} c_fit={(res.g.c_op @ cGfit).item():.6f} "
            f"G_char(0)~{info['G_char'][0][:res.bres.Nphi].mean().item():.5f} vs 4/beta={4/info['beta'].item():.5f}")
        np.savez(args.out, cG=cGfit.cpu().numpy(), cF=info['cF'][0].cpu().numpy(), beta=info['beta'].item(), L=res.L,
                 beta_basis=res.beta_basis, beta_fixed=-1.0, Nt=res.b.Nt, deg=res.b.deg, K=res.K, Nphi=res.b.Nphi, mreg=res.b.m_reg,
                 ngc=res.ng, grade=res.grade, obj=0.0, r_in=res.r_in, dt=res.dt, eps=0.0, cG_ext=res.cG_ext.cpu().numpy(), rmap=res.rmap)
        # residual of this state at eps = 1 (B2-P) as a diagnostic
        res.eps = 1.0
        R1, info1 = res.run(cGfit[None], return_all=True)
        log(f"# linear0 state evaluated at eps=1: beta={info1['beta'].item():.6f} max|wRG|={R1[0].abs().max().item():.3e} rms={R1[0].pow(2).mean().sqrt().item():.3e}")
        sys.exit(0)
    cG, info = lm_solve(res, cG0, iters=args.iters, lam=args.lam, batch=args.batch, log=log, save=args.out,
                        maxtime=args.maxtime, tik=args.tik, dfloor=args.dfloor, maxstep=args.maxstep, broyden_every=args.broyden_every, tik_k=args.tik_k)
    log(f"# done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
