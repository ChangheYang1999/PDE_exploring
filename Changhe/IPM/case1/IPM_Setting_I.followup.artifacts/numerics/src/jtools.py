"""Shared helpers for the follow-on tests that use a stored dense Jacobian of the hybrid Psi-map residual
(src/jac_dense.py output runs/J_<tag>.pt, or the Broyden-updated runs/J_<tag>_broyden.pt of src/dense_newton.py).
Conventions: J holds derivatives with respect to the UNSCALED unknowns z = (b nodes i >= 1, c_l, C); rows are
[0.02 Ehat at the 3 innermost radial nodes; b - b_psi at the other nodes (q = 1 row at r = 1e10); h(P) - 1; identity].
The accurate residual is charmap.Charac.F with dt = 0.01, dt_near = 0.04, Npsi = 480 (the Jacobians use the same dt and Npsi)."""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm

LANE = '.'
import os as _os
RES_KW = dict(dt=0.01, dt_near=0.04, far_psi=True, r_far=float(_os.environ.get('IPM_RFAR', '1e10')), n_coll=3, coll_scale=float(_os.environ.get('IPM_COLLSCALE', '0.02')))   # the discrete system: Npsi 480, dt 0.01 (07:30Z decision, the research record); IPM_RFAR overrides the far-row radius (14:58Z, r_far sensitivity test)


def load_J(jpath, Npsi_res=480):
    """Returns (J cuda, z0 cuda, model (Npsi_res), ch, D) with D the stored dict; model has the accurate inverse."""
    D = torch.load(jpath)
    spath = D['state'] if isinstance(D['state'], str) else str(D['state'])
    m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x)
    model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi_res)
    ch = cm.Charac(model)
    z0 = (D['z0'] if 'z0' in D else D['z']).cuda()
    return D['J'].cuda(), z0, model, ch, D


def cc_weights01(N):
    th = np.pi * np.arange(N + 1) / N
    w = np.zeros(N + 1)
    for j in range(N + 1):
        s = 0.0
        for kk in range(0, N + 1, 2):
            fac = 0.5 if (kk == 0 or kk == N) else 1.0
            ck = 2.0 / (1.0 - kk * kk) if kk != 1 else 0.0
            s += fac * ck * np.cos(kk * th[j])
        w[j] = 2.0 * s / N
    w[0] *= 0.5; w[-1] *= 0.5
    return 0.5 * w[::-1]


def s3_scalings(model, b, clf, C, n_coll=3, coll_scale=0.02):
    """SPEC S3 (a) norms for the hybrid Psi system.  Domain: grid L2 of delta H = delta b / b (Clenshaw-Curtis in q times
    uniform-in-s weights times theta'(s)); c_l column divided by the same norm of X.grad rho / rho; C column times C
    (delta H = dC / C).  Rows: Psi rows (b - b_psi)/b, inner Ehat rows as (W.grad rho - rho)/rho, each times sqrt(weight);
    h(P) and identity rows weight 1.  Returns (Dcol, Drow) tensors; J_s = Drow[:, None] * J * Dcol[None, :]."""
    N, M = model.N, model.M; n = N * M + 2
    wq = cc_weights01(N)[1:]; ws = (np.pi / (2 * M)) * model.ang.dtheta_ds_np
    Wgt = np.sqrt(np.outer(wq, ws)); bn = b[1:].cpu().numpy()
    g = model.geom(torch.tensor(clf, device=model.dev))
    Xg = ((3.0 + g['omega_w'])[1:, None] + g['S'][1:, None] * (model.Dq @ b)[1:] / b[1:]).cpu().numpy()
    ccl = float(np.sqrt(((Wgt * Xg) ** 2).sum()))
    # orthonormal coordinates y -> unscaled: delta b = (b / sqrt(w)) y, dc_l = y_cl / ccl, dC = C y_C  (verifier codereview item 1:
    # the first version had b*sqrt(w) and ccl, i.e. both inverted; every S3-norm table before 09:33Z used the inverted scaling)
    Dcol = np.r_[(bn / Wgt).ravel(), 1.0 / ccl, C]
    Drow_b = Wgt / bn
    q1 = (1.0 - model.q_np[1:n_coll + 1])[:, None]
    Drow_b[:n_coll] = Wgt[:n_coll] * q1 / (coll_scale * bn[:n_coll])
    Drow = np.r_[Drow_b.ravel(), 1.0, 1.0]
    return torch.tensor(Dcol, device=model.dev), torch.tensor(Drow, device=model.dev), Wgt


def lm_step(J, F, Delta, Pc=None, svd=None, s_cut=0.0, info=None):
    """Levenberg-Marquardt step dz = -V diag(s/(s^2 + mu)) U^T F with mu such that |dz|_inf <= Delta; Pc (n x n) a projector
    onto the allowed directions (J is replaced by J Pc and the step lies in range(Pc)); singular directions with s < s_cut are
    dropped (truncated Gauss-Newton: the Jacobian is not trusted below its error level there).  If info is a dict it receives
    the predicted decrease and the residual norm in the dropped subspace.  Returns dz, mu, singular values."""
    A = J if Pc is None else J @ Pc
    U, S, Vh = torch.linalg.svd(A) if svd is None else svd
    gU = U.T @ F
    keep = S > torch.maximum(S[0] * 1e-14, torch.tensor(s_cut, device=S.device, dtype=S.dtype))
    if info is not None:
        info['n_dropped'] = int((~keep).sum()); info['F_in_dropped'] = float(gU[~keep].norm()); info['F_in_kept'] = float(gU[keep].norm())
    def step(mu):
        f = torch.where(keep, S / (S * S + mu), torch.zeros_like(S))
        return -(Vh.T @ (f * gU))
    dz = step(0.0); mu = 0.0
    if dz.abs().max().item() > Delta:
        lo, hi = -30.0, 30.0
        while step(10.0 ** hi).abs().max().item() > Delta and hi < 300: hi += 30.0
        for _ in range(60 + int(hi / 30)):
            mid = 0.5 * (lo + hi)
            if step(10.0 ** mid).abs().max().item() > Delta: lo = mid
            else: hi = mid
        mu = 10.0 ** hi; dz = step(mu)
    if Pc is not None: dz = Pc @ dz
    if info is not None: info['predicted_F'] = float((F + A @ dz).norm()); info['mu'] = mu
    return dz, mu, S


def soft_vectors(Js, k=8, iters=40):
    """k softest right singular vectors of Js by block inverse iteration on Js^T Js (LU of Js); returns (sigma sorted, V)."""
    n = Js.shape[0]; LU = torch.linalg.lu_factor(Js); V = torch.randn(n, k + 2, device=Js.device, dtype=Js.dtype)
    for _ in range(iters):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
    JV = Js @ V; Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False); Vk = V @ Wk.T; order = torch.argsort(sk)
    return sk[order][:k], Vk[:, order][:, :k]


class Diag:
    """Structure diagnostics of a perturbation v (unscaled coordinates: delta b at nodes i >= 1, dc_l, dC) at a state."""
    def __init__(self, model, ch, b, clf, C):
        self.m, self.ch, self.b, self.clf, self.C = model, ch, b, clf, C
        N, M = model.N, model.M
        self.r, self.w, self.v = model.radii(clf); self.thd = model.ang.theta_np * 180 / np.pi
        self.st = ch.prepare(b, torch.tensor(clf, device=model.dev))
        rr = torch.tensor(self.r[1:N], device=model.dev); R, TH = torch.meshgrid(rr, model.ang.theta, indexing='ij')
        X = torch.stack([(R * torch.cos(TH)).reshape(-1), (R * torch.sin(TH)).reshape(-1)], 1)
        W1, W2, _ = ch.Wfield(self.st, X)
        self.Wr = (W1 * torch.cos(TH).reshape(-1) + W2 * torch.sin(TH).reshape(-1)).reshape(N - 1, M)
        self.Wt = (-W1 * torch.sin(TH).reshape(-1) + W2 * torch.cos(TH).reshape(-1)).reshape(N - 1, M)
        self.Wabs = torch.sqrt(self.Wr ** 2 + self.Wt ** 2)
        g = model.geom(torch.tensor(clf, device=model.dev)); self.S = g['S']
        self.rho = (torch.tensor(self.r[:N], device=model.dev) ** 3 * torch.tensor(self.w[:N], device=model.dev))[:, None] * (model.ang.cos ** 2 * model.ang.sin)[None, :]   # rho / b at nodes 0..N-1
        wq = cc_weights01(N); ws = (np.pi / (2 * M)) * model.ang.dtheta_ds_np
        self.Wgt2 = torch.tensor(np.outer(wq[1:N], ws), device=model.dev)          # nodes i = 1..N-1 (alignment)
        self.WgtN = torch.tensor(np.outer(wq[1:], ws), device=model.dev)           # nodes i = 1..N (weighted energies)
        self.xstar = float(ch.find_P(self.st)[0])
        # prefactor p/r = r^2 w at nodes 1..N-1, Pi = cos^2 sin and Pi' (theta derivative), geometry factors for the product rule
        self.p_over_r = (torch.tensor(self.r[1:N], device=model.dev) ** 2 * torch.tensor(self.w[1:N], device=model.dev))[:, None]
        cth, sth = model.ang.cos, model.ang.sin
        self.Pi = (cth ** 2 * sth)[None, :]; self.Pip = (cth * (cth ** 2 - 2 * sth ** 2))[None, :]
        self.omega_w = g['omega_w'][1:N, None]; self.S1 = g['S'][1:N, None]

    def report(self, v):
        """Diagnostics of the SHAPE part of v at fixed c_l (the physical effect of dc_l on the density at fixed position is not
        included; dc_l and dC are reported as components).  'radial'/'angular10'/'nearP_fraction' are fractions of the unscaled
        coordinate energy |v|^2; the '_w' versions are fractions of the weighted relative-field energy sum w |delta b / b|^2."""
        m = self.m; N, M = m.N, m.M
        vb = v[:N * M].reshape(N, M); tot = float((v ** 2).sum()); en = (vb ** 2).cpu().numpy(); rr = self.r[1:]
        out = dict(dcl=float(v[-2]), dC=float(v[-1]), cl_fraction=float(v[-2] ** 2 / tot), C_fraction=float(v[-1] ** 2 / tot))
        thd = self.thd
        xx = rr[:, None] * np.cos(np.deg2rad(thd))[None, :]; yy = rr[:, None] * np.sin(np.deg2rad(thd))[None, :]
        nearP = ((xx - self.xstar) ** 2 + yy ** 2) < 4
        def fractions(e, total, suffix):
            out['radial' + suffix] = {k_: float(e[s_].sum() / total) for k_, s_ in [('r<1', rr < 1), ('1-10', (rr >= 1) & (rr < 10)), ('10-100', (rr >= 10) & (rr < 100)), ('>100', rr >= 100)]}
            out['angular10' + suffix] = [float(e[:, (thd >= lo) & (thd < lo + 10)].sum() / total) for lo in range(0, 90, 10)]
            out['nearP_fraction' + suffix] = float(e[nearP].sum() / total)
        fractions(en, tot, '')
        enw = (self.WgtN * (vb / self.b[1:]) ** 2).cpu().numpy(); enw = np.nan_to_num(enw); fractions(enw, enw.sum() + 1e-300, '_w')
        # oscillation: sign changes of delta H = delta b / b along r = 5 (in theta) and along theta = 45 deg (in r); delta b and b
        # interpolated separately (the quotient is not representable)
        dB = torch.zeros(N + 1, M, device=m.dev); dB[1:] = vb
        q5 = m.q_of_r(np.array([5.0]), self.clf)[0]; thf = (np.arange(64) + 0.5) * np.pi / 128
        line_th = m.eval_EE(dB, np.full(64, q5), thf) / m.eval_EE(self.b, np.full(64, q5), thf)
        qs = m.q_of_r(np.geomspace(0.05, 500.0, 80), self.clf); line_r = m.eval_EE(dB, qs, np.full(80, np.pi / 4)) / m.eval_EE(self.b, qs, np.full(80, np.pi / 4))
        tol_th = 1e-8 * np.abs(line_th).max(); tol_r = 1e-8 * np.abs(line_r).max()
        out['sign_changes_r5'] = int(np.sum(np.sign(np.where(np.abs(line_th) < tol_th, 0, line_th))[1:] * np.sign(np.where(np.abs(line_th) < tol_th, 0, line_th))[:-1] < 0))
        out['sign_changes_th45'] = int(np.sum(np.sign(np.where(np.abs(line_r) < tol_r, 0, line_r))[1:] * np.sign(np.where(np.abs(line_r) < tol_r, 0, line_r))[:-1] < 0))
        # streamline alignment of delta rho = p Pi delta b (fixed c_l), gradient by the product rule at nodes i = 1..N-1:
        # (delta rho)_r = (p/r) Pi [(3 + omega_w) delta b + S D_q delta b],  (delta rho)_theta / r = (p/r) [Pi' delta b + Pi d_theta delta b]
        dBq = (m.Dq @ dB)[1:N]; dBth = m.ang.dtheta(dB, 'EE')[1:N]; dB1 = dB[1:N]
        fr = self.p_over_r * self.Pi * ((3.0 + self.omega_w) * dB1 + self.S1 * dBq)
        ft = self.p_over_r * (self.Pip * dB1 + self.Pi * dBth)
        num = self.Wr * fr + self.Wt * ft; den = self.Wabs * torch.sqrt(fr ** 2 + ft ** 2)
        good = torch.isfinite(num) & torch.isfinite(den)
        dsum = float((self.Wgt2 * den ** 2)[good].sum())
        out['streamline_alignment'] = float(torch.sqrt((self.Wgt2 * num ** 2)[good].sum() / dsum)) if dsum > 0 else float('nan')
        out['alignment_nonfinite_nodes'] = int((~good).sum())
        return out
