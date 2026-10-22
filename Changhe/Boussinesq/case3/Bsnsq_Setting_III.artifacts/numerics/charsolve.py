"""
Characteristic (semi-Lagrangian) formulation of the B2 profile problem.
Unknowns: cG (coefficients of G in the spline x cos basis), cF (coefficients of F, cF[0,0] = 1 fixed).
Given cG: beta = 2(c - 1) with c = Psi_xy(0) = c_op . cG;  W = beta X + U from the modal inverse (U(0) = 0).
Backward characteristics from every collocation point X0 to the centre (|X| < r_in), then
   Theta(X0) = e^{(beta-2) T} Theta_loc(X_end),
   Omega(X0) = e^{-T} Omega_loc(X_end) + int_{-T}^0 e^t Theta_x(X(t)) dt,
with Theta_x from the current cF, and the second-order centre jet Theta_loc, Omega_loc from the Taylor recursion.
Residuals: F_char - F(cF) and G_char - G(cG) at the collocation points (weighted by radial envelopes).
"""
import sys, os, time, math
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from numpy.polynomial.legendre import leggauss

torch.set_default_dtype(DT)


class CharModel:
    def __init__(self, basis, L, r_in=1e-3, dt=0.02, max_steps=20000, device='cuda', jet_order=2):
        self.b = basis
        self.L = L
        self.r_in = r_in
        self.dt = dt
        self.max_steps = max_steps
        self.dev = device
        self.jet_order = jet_order
        b = basis
        # Lagrange interpolation data on Gauss nodes per interval (reference interval [-1,1])
        xg, _ = leggauss(b.ng_coll if hasattr(b, 'ng_coll') else 3)
        ng = len(b.t_coll) // b.Nt
        self.ng = ng
        xi = np.array(leggauss(ng)[0])
        wbar = np.array([1.0 / np.prod([xi[j] - xi[m] for m in range(ng) if m != j]) for j in range(ng)])
        self.xi = torch.tensor(xi, dtype=DT, device=device)
        self.wbar = torch.tensor(wbar, dtype=DT, device=device)
        self.edges = torch.tensor(b.edges, dtype=DT, device=device)
        self.grade = b.grade
        self.K = b.K
        self.ks = torch.arange(1, b.K + 1, dtype=DT, device=device)
        self.kk = torch.arange(0, b.K, dtype=DT, device=device)

    # ---------------------------------------------------------------- interpolation
    def interp(self, t, nodal):
        """nodal: (Nc, M) values at the collocation nodes; t: (Nq,) query points in [0,1). Returns (Nq, M)."""
        b = self.b
        Nt = b.Nt
        u = torch.clamp(t, 0.0, 1.0 - 1e-15)
        idx = torch.clamp((Nt * u ** (1.0 / self.grade)).floor().long(), 0, Nt - 1)
        a = self.edges[idx]; bb = self.edges[idx + 1]
        xi = 2 * (u - a) / (bb - a) - 1
        diff = xi[:, None] - self.xi[None, :]
        small = diff.abs() < 1e-14
        diff = torch.where(small, torch.full_like(diff, 1e-14), diff)
        lw = self.wbar[None, :] / diff
        ell = lw / lw.sum(1, keepdim=True)
        ell = torch.where(small.any(1, keepdim=True), small.to(DT), ell)
        gidx = idx[:, None] * self.ng + torch.arange(self.ng, device=t.device)[None, :]      # (Nq, ng)
        vals = nodal[gidx]                                                                  # (Nq, ng, M)
        return torch.einsum('qg,qgm->qm', ell, vals)

    # ---------------------------------------------------------------- set state
    def set_state(self, cF, cG, geom=None):
        """Precompute nodal modal data for W and Theta_x from (cF, cG). beta from c."""
        b = self.b
        c = None
        if geom is None:
            # need beta first: c_op depends on geometry (through beta!) -> iterate: c_op depends on the map r(t;beta)
            # and the decay factor; so geometry must be built with the beta consistent with cG. Caller passes geom.
            raise ValueError('geom required')
        g = geom
        self.g = g
        c = (g.c_op @ cG).item()
        self.beta = 2 * (c - 1)          # dynamical beta from the centre condition
        beta = self.beta
        self.beta_basis = g.beta
        K, Nc, Nb = b.K, b.Nc, b.Nb
        # modal Psi_k, Psi_k' at nodes (K, Nc)
        Psi = torch.einsum('kia,a->ki', g.Psi_op, cG)
        dPsi = torch.einsum('kia,a->ki', g.dPsi_op, cG)
        # Omega_k at nodes: Omega_1 = r (g_0 - g_2/2), Omega_k = (r/2)(g_{k-1} - g_{k+1})
        gk = torch.einsum('kia,ka->ki', g.R0k, cG.reshape(K, Nb))           # (K, Nc) g_k values
        Om = torch.zeros(K, Nc, dtype=DT, device=self.dev)
        r = g.r
        for k in range(1, K + 1):
            lo = gk[k - 1] * (1.0 if k == 1 else 0.5)
            hi = 0.5 * gk[k + 1] if k + 1 < K else torch.zeros_like(lo)
            Om[k - 1] = r * (lo - hi)
        ddPsi = -dPsi / r + (self.ks[:, None] ** 2) * Psi / r ** 2 - Om
        # F modal nodal values and r-derivatives
        fk = torch.einsum('kia,ka->ki', g.R0k, cF.reshape(K, Nb))
        dfk = torch.einsum('kia,ka->ki', g.R1k, cF.reshape(K, Nb))
        # store bounded scaled quantities for interpolation: Psi/r^2, Psi'/r, Psi''
        self.nodal = torch.cat([(Psi / r ** 2).T, (dPsi / r).T, ddPsi.T, fk.T, dfk.T], 1)      # (Nc, 5K)
        self.cF, self.cG = cF, cG
        # centre jet coefficients
        self._centre_jet(cG, gk, g)

    def _centre_jet(self, cG, gk, g):
        b = self.b
        beta = self.beta
        wq = b.w_quad_t * g.drdtq
        rq = g.rq
        K, Nb = b.K, b.Nb
        mk = b.mk
        # Omega_k at quadrature nodes for k=2,3,4 (from g modes)
        def gq(k):
            m = int(mk[k]); return g.Wq[m] @ cG[k * Nb:(k + 1) * Nb] / rq     # g_k at quad nodes (Wq includes factor rho)
        def Omq(k):
            lo = gq(k - 1) * (1.0 if k == 1 else 0.5)
            hi = 0.5 * gq(k + 1) if k + 1 < K else 0.0
            return rq * (lo - hi)
        h20 = 0.25 * (wq * Omq(2) / rq).sum()                 # h_{2,0} = (1/4) int Omega_2/rho
        h30 = (1.0 / 6.0) * (wq * Omq(3) / rq ** 2).sum() if K > 3 else torch.zeros((), dtype=DT, device=self.dev)
        h40 = (1.0 / 8.0) * (wq * Omq(4) / rq ** 3).sum() if K > 4 else torch.zeros((), dtype=DT, device=self.dev)
        G0 = cG[0]                                            # g_0(0) = G(0,0)
        # g_1'(0): g_1 = t * D * spline -> d/dr at 0 = (dt/dr)(0) * spline(0) = cG[Nb] * (dt/dr at 0)
        dtdr0 = (2.0 / self.beta_basis) / self.L              # t = 1 - (L/(r+L))^{2/beta_basis} -> dt/dr(0)
        g1p = cG[Nb] * dtdr0 if K > 1 else torch.zeros((), dtype=DT, device=self.dev)
        om22 = 0.5 * g1p                                      # Omega_2 ~ (1/2) g_1'(0) r^2
        h11_ = -G0 / 8.0                                      # h_{1,1}
        h21 = -om22 / 12.0                                    # h_{2,1}
        c = -2 * h20
        h01 = c
        h10 = h11_ - h30
        h02 = h11_ + 3 * h30
        h11 = -2 * h21 + 4 * h40
        b0 = 4.0 / beta
        f01 = 4 * h02 / (beta + c)
        f10 = (2 * h11 - 3 * h10 * f01) / (beta - 2)
        g01 = (2 * f01 + 2 * h02 * b0) / (2 * beta + 1)
        g10 = (4 * f10 + h11 * b0 - 3 * h10 * g01) / (1.5 * beta - 2)
        self.jet = dict(c=c, b0=b0, f01=f01, f10=f10, g01=g01, g10=g10, h01=h01, h10=h10, h02=h02, h11=h11)

    # ---------------------------------------------------------------- velocity and Theta_x at arbitrary points
    def rhs(self, X, need_thx=True):
        """X: (Nq,2). Returns W (Nq,2) and Theta_x (Nq,)."""
        beta, L, K = self.beta, self.L, self.K
        x, y = X[:, 0], X[:, 1]
        sx = torch.sign(x); sx = torch.where(sx == 0, torch.ones_like(sx), sx)
        xa = x.abs()
        r = torch.sqrt(xa ** 2 + y ** 2)
        phi = torch.atan2(xa, -y)
        t = 1 - (L / (r + L)) ** (2.0 / self.beta_basis)
        vals = self.interp(t, self.nodal)                       # (Nq, 5K)
        Psi, dPsi, ddPsi, fk, dfk = vals[:, :K] * r[:, None] ** 2, vals[:, K:2 * K] * r[:, None], vals[:, 2 * K:3 * K], vals[:, 3 * K:4 * K], vals[:, 4 * K:]
        kphi_s = torch.sin(phi[:, None] * self.ks[None, :]); kphi_c = torch.cos(phi[:, None] * self.ks[None, :])
        Psir = (dPsi * kphi_s).sum(1)
        Psiphi = (self.ks[None, :] * Psi * kphi_c).sum(1)
        s, cph = torch.sin(phi), torch.cos(phi)
        U2 = s * Psir + cph / r * Psiphi
        U1 = cph * Psir - s / r * Psiphi
        W1 = beta * xa + U1
        W2 = beta * y + U2
        W = torch.stack([sx * W1, W2], 1)
        if not need_thx:
            return W, None
        ck = torch.cos(phi[:, None] * self.kk[None, :]); sk = torch.sin(phi[:, None] * self.kk[None, :])
        F = (fk * ck).sum(1)
        Fr = (dfk * ck).sum(1)
        Fphi = -(self.kk[None, :] * fk * sk).sum(1)
        F1 = F + 0.5 * (r * s ** 2 * Fr + s * cph * Fphi)        # F + s F_s
        Thx = 2 * x * F1                                        # odd in x
        return W, Thx

    # ---------------------------------------------------------------- characteristics
    def run(self, X0, verbose=False):
        """Backward characteristics from X0 (Nq,2). Returns Theta, Omega at X0, plus diagnostics."""
        beta = self.beta
        dt = self.dt
        Nq = X0.shape[0]
        X = X0.clone()
        tt = torch.zeros(Nq, dtype=DT, device=self.dev)        # elapsed backward time T
        q = torch.zeros(Nq, dtype=DT, device=self.dev)         # int_{-T}^0 e^{t} Theta_x dt  (t negative)
        done = torch.zeros(Nq, dtype=torch.bool, device=self.dev)
        rin = self.r_in
        def f(Xs, ts):
            W, Thx = self.rhs(Xs)
            return -W, torch.exp(-ts) * Thx          # d/dT X = -W ; d/dT q = e^{-T} Theta_x  (t = -T)
        steps = 0
        for step in range(self.max_steps):
            act = ~done
            if not act.any():
                break
            Xa = X[act]; ta = tt[act]
            k1, q1 = f(Xa, ta)
            k2, q2 = f(Xa + 0.5 * dt * k1, ta + 0.5 * dt)
            k3, q3 = f(Xa + 0.5 * dt * k2, ta + 0.5 * dt)
            k4, q4 = f(Xa + dt * k3, ta + dt)
            Xn = Xa + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            qn = q[act] + dt / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
            X[act] = Xn; q[act] = qn; tt[act] = ta + dt
            rn = torch.sqrt(Xn[:, 0] ** 2 + Xn[:, 1] ** 2)
            newly = rn < rin
            idx = torch.nonzero(act)[:, 0]
            done[idx[newly]] = True
            steps += 1
        self.steps_used = steps
        self.n_unfinished = int((~done).sum())
        # local jet at X_end
        J = self.jet
        xe, ye = X[:, 0], X[:, 1]
        se = xe ** 2
        Th_loc = se * (1 + J['f01'] * ye + J['f10'] * se)
        Om_loc = xe * (J['b0'] + J['g01'] * ye + J['g10'] * se)
        Theta = torch.exp((beta - 2) * tt) * Th_loc
        Omega = torch.exp(-tt) * Om_loc + q
        return Theta, Omega, tt, X


