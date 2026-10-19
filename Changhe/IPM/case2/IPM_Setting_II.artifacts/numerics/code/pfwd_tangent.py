#!/usr/bin/env python3
"""R22 (2026-10-19): Newton on the fixed-datum exit map with an ANALYTIC tangent (the linearised transport equation integrated along the
base orbits) and the two strong exits / two datum zeros as explicit unknowns.

State equation (fixed-datum exit map, zeros theta_z = (z1, z2) explicit):  F_grid(g, z) = (g - T(g; z)) / scale,
    T(g; z)(X) = e^{-tau(X)} e^{p hi} A(theta_exit(X); z) / r^p,  orbits of a = (a_r, a_th) = (1/p + W_r / r, W_th / r), W = W[r^p g] (class-S law);
matching rows  F_match(g, z) = w_m (theta_e(g) - z),  theta_e = exit angles of the strong-manifold seeds (e^lr_g, 90 / 270 deg).
Tangent: delta W = W[r^p delta g] (linear); along each stored base orbit X_n the variational equation d(delta X)/dt = J(X) delta X + delta a(X),
J = grad (a_r, a_th) (from grid gradient fields, B-spline interpolated at the stored positions, stored once per Newton step), integrated by Heun's rule
with the base step; at the exit delta tau = -delta lr / a_r, delta theta_exit = delta theta + a_th delta tau;
    delta T = e^{-tau} e^{p hi} [ -delta tau A + A' delta theta_exit + dA/dz . delta z ] / r^p.
Newton-GMRES (Arnoldi, no restarts) on [delta u, delta z], u = g / scale; a step is accepted only if the TRUE residual norm decreases (backtracking).
Modes:  m1   validate the tangent against finite differences of T at the base (x-even directions);
        newton  Newton from a saved state with a modified datum (b1=... x-odd amplitude).
Usage: python3 code/pfwd_tangent.py state.npz TAG mode=m1|newton [b1=1e-3] [maxit=6] [kmax=30] [wm=0.05] [gm_tol=1e-2] [dt=0.01] [cap=3000] [eps=1e-4,1e-5]
Outputs: runs/pfwd/tan/TAG.log (JSON lines), TAG_it*.npz states.
"""
import sys, json, math, time, os
import numpy as np, torch
sys.path.insert(0, 'code')
from pfwd import fd_dlr
from pfwd_gnewton import GammaMap
torch.set_default_dtype(torch.float64)


class TangentMap(GammaMap):
    def __init__(self, *a, jmode='grid', hfd=0.25, **k):
        super().__init__(*a, **k)
        self.jmode = jmode; self.hfd = float(hfd)
        S = self.S
        self.seedLR = torch.full((1, 2), self.lr_g, device=self.dev); self.seedTH = torch.tensor([[math.pi / 2, 3 * math.pi / 2]], device=self.dev)
        self.N = S.Nr * S.Nth

    def set_scale_rowmax(self, g0):
        """residual scaling by the row maxima of a reference state (relative defect per radial row, as resid_norms); fixed during a solve."""
        self.scale = g0.max(dim=1, keepdim=True).values.clamp(min=1e-300).clone()

    # ---- datum and its derivatives (zeros explicit)
    def A_and_derivs(self, t, z):
        z1, z2 = z
        s1 = torch.sin(0.5 * (t - z1)); c1 = torch.cos(0.5 * (t - z1)); s2 = torch.sin(0.5 * (t - z2)); c2 = torch.cos(0.5 * (t - z2))
        F = self.Fexp(t); eF = torch.exp(F)
        # F'(t)
        Fp = torch.zeros_like(t)
        for j, a in enumerate(self.F_even):
            n = j + 1; Fp = Fp + float(a) * n * (torch.cos(n * t) if n % 2 == 1 else -torch.sin(n * t))
        for j, a in enumerate(self.F_odd):
            n = j + 1; Fp = Fp + float(a) * n * (-torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
        A = 4.0 * s1 ** 2 * s2 ** 2 * eF
        dA_dt = 4.0 * eF * (s1 * c1 * s2 ** 2 + s1 ** 2 * s2 * c2 + s1 ** 2 * s2 ** 2 * Fp)
        dA_dz1 = -4.0 * eF * s1 * c1 * s2 ** 2
        dA_dz2 = -4.0 * eF * s1 ** 2 * s2 * c2
        return A, dA_dt, dA_dz1, dA_dz2

    def _bs(self, F, clip=True):
        """B-spline evaluator for a grid field F [Nr, Nth] (batch 1), as the velocity fields in _fields.  clip=False: no hull limiter (LINEAR in F;
        used for the perturbation fields of the tangent, since the limiter is a nonlinear operation that breaks the Arnoldi relation)."""
        SB = self.SB
        Fb = F[None]; top = Fb[:, -1:].expand(-1, 2, -1)
        FE = SB.extend(Fb, top); C = SB.prefilter(FE)
        def ev(l_, t_):
            ci = (l_ - self.S.lo) / self.S.d; cj = t_ / self.S.dth
            if clip:
                return SB.eval_bs(C, FE, ci, cj)
            lim = SB.limiter; SB.limiter = False
            try:
                return SB.eval_bs(C, FE, ci, cj)
            finally:
                SB.limiter = lim
        return ev

    # ---- base: fields, orbits with stored positions, gradients, T, exits
    def base(self, g, z, store=True):
        S = self.S; t0 = time.time()
        Wr, Wt, rho = self.velocity(g)
        ar = ((1 / self.p) + Wr / S.r[None, :, None])[0]; at = (Wt / S.r[None, :, None])[0]          # [Nr, Nth]
        ev_ar = self._bs(ar); ev_at = self._bs(at)
        def rhs(l_, t_):
            return ev_ar(l_, t_), ev_at(l_, t_)
        # gradient fields on the grid (6th-order FD in lr, spectral in theta), B-spline interpolated along the orbits
        ev_J = [self._bs(fd_dlr(ar, S.d)), self._bs(S.d_theta(ar)), self._bs(fd_dlr(at, S.d)), self._bs(S.d_theta(at))]
        LR = torch.cat([self.LR, self.seedLR], 1).clone(); TH = torch.cat([self.TH, self.seedTH], 1).clone()
        M = LR.shape[1]
        Tt = torch.zeros_like(LR); live = LR < S.hi - 1e-12; dt = self.dt; it = 0
        pos = []  # per step: (LR, TH) before the step, and the step fraction
        fracs = []
        cap = max(self.orbit_cap, 20000)
        while bool(live.any()) and it < cap:
            k1 = rhs(LR, TH); k2 = rhs(LR + 0.5 * dt * k1[0], TH + 0.5 * dt * k1[1]); k3 = rhs(LR + 0.5 * dt * k2[0], TH + 0.5 * dt * k2[1]); k4 = rhs(LR + dt * k3[0], TH + dt * k3[1])
            dl = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); dth = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            over = live & (LR + dl >= S.hi)
            frac = torch.where(over, (S.hi - LR) / torch.clamp(dl, min=1e-300), torch.ones_like(dl))
            frac = torch.where(live, frac, torch.zeros_like(frac))
            if store:
                pos.append((LR.clone(), TH.clone())); fracs.append(frac.clone())
            LR = torch.where(live, LR + frac * dl, LR); TH = torch.where(live, TH + frac * dth, TH); Tt = torch.where(live, Tt + frac * dt, Tt)
            live = live & ~over; it += 1
        nsteps = it
        th_e = (float(torch.remainder(TH[0, -2], 2 * math.pi)), float(torch.remainder(TH[0, -1], 2 * math.pi)))
        A, dA_dt, dA_dz1, dA_dz2 = self.A_and_derivs(TH[:, :self.N], z)
        pref = torch.exp(-Tt[:, :self.N]) * math.exp(self.p * S.hi) / (S.r[:, None] ** self.p).expand(S.Nr, S.Nth).reshape(1, -1)
        Tg = (pref * A).reshape(S.Nr, S.Nth)
        info = dict(orbit_its=it, unfinished=int(live[:, :self.N].sum()), seeds_ok=bool(~live[:, -2:].any()), th_e_deg=[math.degrees(th_e[0]), math.degrees(th_e[1])], wall_base=round(time.time() - t0, 1))
        self.cur = dict(g=g, z=z, Wr=Wr, Wt=Wt, Tg=Tg, th_e=th_e, TH_exit=TH, Tt=Tt, pref=pref, A=A, dA_dt=dA_dt, dA_dz=(dA_dz1, dA_dz2), live_end=live, ev_ar=ev_ar, ev_at=ev_at)
        if store:
            # stack positions and evaluate J at them (stored once per Newton step): [nsteps, M]
            t1 = time.time()
            PL = torch.stack([p_[0][0] for p_ in pos], 0); PT = torch.stack([p_[1][0] for p_ in pos], 0); FR = torch.stack([f[0] for f in fracs], 0)
            del pos, fracs
            CH = 32                                                                                     # chunk the [nsteps, M] evaluations (memory)
            J = torch.empty(4, nsteps, M, device=self.dev)
            for c0 in range(0, nsteps, CH):
                pl, pt = PL[c0:c0 + CH], PT[c0:c0 + CH]
                if self.jmode == 'fdspline':                                                           # gradients of the realised (B-spline) velocity fields by central differences
                    hl = self.hfd * S.d; ht = self.hfd * S.dth
                    J[0, c0:c0 + CH] = (ev_ar(pl + hl, pt) - ev_ar(pl - hl, pt)) / (2 * hl); J[1, c0:c0 + CH] = (ev_ar(pl, pt + ht) - ev_ar(pl, pt - ht)) / (2 * ht)
                    J[2, c0:c0 + CH] = (ev_at(pl + hl, pt) - ev_at(pl - hl, pt)) / (2 * hl); J[3, c0:c0 + CH] = (ev_at(pl, pt + ht) - ev_at(pl, pt - ht)) / (2 * ht)
                else:
                    for q in range(4):
                        J[q, c0:c0 + CH] = ev_J[q](pl, pt)
            a_exit = (ev_ar(TH[:, :] * 0 + S.hi, TH)[0], ev_at(TH[:, :] * 0 + S.hi, TH)[0])          # a at the exit points (lr = hi)
            self.cur.update(PL=PL, PT=PT, FR=FR, J=J, nsteps=nsteps, a_exit=a_exit)
            info['wall_store'] = round(time.time() - t1, 1); info['nsteps'] = nsteps
            info['mem_GB'] = round((PL.numel() * 2 + FR.numel() + J.numel()) * 8 / 1e9, 2)
        return Tg, info

    def residual(self, g, z, wm):
        Tg, info = self.base(g, z, store=False)
        Fg = ((g - Tg) / self.scale).reshape(-1)
        Fm = wm * torch.tensor([self.cur['th_e'][0] - z[0], self.cur['th_e'][1] - z[1]], device=self.dev)
        return torch.cat([Fg, Fm]), info

    # ---- tangent action on (delta u, delta z); needs self.cur from base(store=True)
    def tangent(self, du, dz, wm):
        S = self.S; c = self.cur
        dg = du.reshape(S.Nr, S.Nth) * self.scale
        drho = S.r[:, None] ** self.p * dg
        dWr, dWt = self.SB.velocity(drho[None], self.pB)
        dar = (dWr / S.r[None, :, None])[0]; dat = (dWt / S.r[None, :, None])[0]
        ev_dar = self._bs(dar, clip=False); ev_dat = self._bs(dat, clip=False)
        PL, PT, FR, J, n = c['PL'], c['PT'], c['FR'], c['J'], c['nsteps']
        DA_r = torch.empty_like(PL); DA_t = torch.empty_like(PT)
        for c0 in range(0, n, 32):
            DA_r[c0:c0 + 32] = ev_dar(PL[c0:c0 + 32], PT[c0:c0 + 32]); DA_t[c0:c0 + 32] = ev_dat(PL[c0:c0 + 32], PT[c0:c0 + 32])
        M = PL.shape[1]; dt = self.dt
        dL = torch.zeros(M, device=self.dev); dT = torch.zeros(M, device=self.dev)
        # Heun along the stored orbit: f_n = J_n d_n + da_n ; predictor with f_n, corrector with J_{n+1}, da_{n+1} at the next stored point (or the exit point for the last step)
        for k in range(n):
            fr = FR[k]; h = dt * fr
            f1L = J[0, k] * dL + J[1, k] * dT + DA_r[k]; f1T = J[2, k] * dL + J[3, k] * dT + DA_t[k]
            if k + 1 < n:
                J0, J1, J2, J3, dr, dth = J[0, k + 1], J[1, k + 1], J[2, k + 1], J[3, k + 1], DA_r[k + 1], DA_t[k + 1]
            else:
                J0, J1, J2, J3, dr, dth = J[0, k], J[1, k], J[2, k], J[3, k], DA_r[k], DA_t[k]
            pL = dL + h * f1L; pT = dT + h * f1T
            f2L = J0 * pL + J1 * pT + dr; f2T = J2 * pL + J3 * pT + dth
            dL = dL + 0.5 * h * (f1L + f2L); dT = dT + 0.5 * h * (f1T + f2T)
        ar_e, at_e = c['a_exit']
        dtau = -dL / torch.clamp(ar_e, min=1e-12)
        dth_exit = dT + at_e * dtau
        pref, A, dA_dt, (dA_dz1, dA_dz2) = c['pref'][0], c['A'][0], c['dA_dt'][0], (c['dA_dz'][0][0], c['dA_dz'][1][0])
        dTg = pref * (-dtau[:self.N] * A + dA_dt * dth_exit[:self.N] + dA_dz1 * dz[0] + dA_dz2 * dz[1])
        dFg = (dg.reshape(-1) - dTg) / self.scale.expand(S.Nr, S.Nth).reshape(-1)
        dFm = wm * (dth_exit[self.N:] - torch.stack([dz[0], dz[1]]))
        return torch.cat([dFg, dFm]), dth_exit


def gmres(matvec, b, kmax=30, tol=1e-2, log=None, tsvd=0.0):
    """Arnoldi / GMRES without restart on A x = b; returns x, residual history, Hessenberg singular values.
    tsvd > 0: the final Hessenberg least-squares problem is solved by truncated SVD, dropping singular values below tsvd * sigma_max (regularised step)."""
    dev = b.device; n = b.numel()
    beta = float(torch.linalg.norm(b)); V = [b / beta]; H = torch.zeros(kmax + 1, kmax, device=dev)
    hist = []
    for j in range(kmax):
        w = matvec(V[j])
        for i in range(j + 1):
            H[i, j] = torch.dot(V[i], w); w = w - H[i, j] * V[i]
        for i in range(j + 1):                                        # second pass
            c = torch.dot(V[i], w); H[i, j] += c; w = w - c * V[i]
        H[j + 1, j] = torch.linalg.norm(w)
        e1 = torch.zeros(j + 2, device=dev); e1[0] = beta
        y = torch.linalg.lstsq(H[:j + 2, :j + 1], e1[:, None]).solution[:, 0]
        res = float(torch.linalg.norm(H[:j + 2, :j + 1] @ y - e1)) / beta
        hist.append(res)
        if log: log(json.dumps(dict(gmres_it=j + 1, rel_res=res, h_sub=float(H[j + 1, j]))))
        if res < tol or float(H[j + 1, j]) < 1e-14:
            break
        V.append(w / H[j + 1, j])
    k = len(hist)
    Hk = H[:k + 1, :k]; e1 = torch.zeros(k + 1, device=dev); e1[0] = beta
    U_, S_, Vh_ = torch.linalg.svd(Hk, full_matrices=False)
    sv = S_.cpu().numpy().tolist()
    if tsvd > 0:
        keep = S_ >= tsvd * S_[0]
        y = Vh_.T[:, keep] @ ((U_.T @ e1)[keep] / S_[keep])
        if log: log(json.dumps(dict(tsvd=tsvd, kept=int(keep.sum()), of=k, truncated_rel_res=float(torch.linalg.norm(Hk @ y - e1)) / beta)))
    x = sum(float(y[i]) * V[i] for i in range(k))
    return x, hist, sv


def main():
    fn, tag = sys.argv[1], sys.argv[2]
    kw = dict(a.split('=', 1) for a in sys.argv[3:])
    mode = kw.get('mode', 'm1'); dev = 'cuda' if torch.cuda.is_available() else 'cpu'
    os.makedirs('runs/pfwd/tan', exist_ok=True)
    logf = open('runs/pfwd/tan/%s.log' % tag, 'a')
    def log(line):
        print(line, flush=True); logf.write(line + '\n'); logf.flush()
    d = np.load(fn, allow_pickle=True); g = torch.tensor(d['g'], device=dev); lr = d['lr']; Nr, Nth = g.shape
    args = json.loads(str(d['args'])); p = float(args['p']); a_even = list(args['par'])
    b1 = float(kw.get('b1', '0')); F_odd = [b1] + [0.0] * 15
    wm = float(kw.get('wm', '0.05')); kmax = int(kw.get('kmax', '30')); gm_tol = float(kw.get('gm_tol', '1e-2')); maxit = int(kw.get('maxit', '6'))
    TM = TangentMap(Nr, Nth, float(lr[0]), float(lr[-1]), p, a_even, F_odd, dt=float(kw.get('dt', '0.01')), dev=dev, orbit_cap=int(kw.get('cap', '3000')), jmode=kw.get('jmode', 'grid'), hfd=float(kw.get('hfd', '0.25')))
    if kw.get('scale', 'rowmax') == 'rowmax':
        TM.set_scale_rowmax(g)
    z = [float(kw.get('z1', str(math.pi / 2))), float(kw.get('z2', str(3 * math.pi / 2)))]
    log(json.dumps(dict(tag=tag, file=fn, mode=mode, Nr=Nr, Nth=Nth, p=p, b1=b1, wm=wm, kmax=kmax, gm_tol=gm_tol, maxit=maxit, jmode=TM.jmode, hfd=TM.hfd, dt=TM.dt, z_deg=[math.degrees(z[0]), math.degrees(z[1])], start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))
    if mode == 'm1':
        # tangent against finite differences at the base (x-even smooth directions); also the seed-exit derivative
        Tg, info = TM.base(g, z, store=True); log(json.dumps(dict(base=info, defect_max=float(((Tg - g) / TM.scale).abs().max()), defect_rms=float(torch.sqrt((((Tg - g) / TM.scale) ** 2).mean())))))
        S = TM.S
        dirs = {}
        lrt = S.lr[:, None].expand(Nr, Nth); tht = S.th[None, :].expand(Nr, Nth)
        dirs['bump_mid'] = g * 0.01 * torch.cos(2 * tht) * torch.exp(-(lrt + 2) ** 2 / 2)              # x-even smooth, mid field
        dirs['bump_inner'] = g * 0.01 * torch.cos(2 * tht) * torch.exp(-(lrt + 6) ** 2 / 2)            # x-even, inner
        dirs['far_even'] = g * 0.01 * torch.sin(tht) * torch.exp(-(lrt - 6) ** 2 / 8)                   # x-even (sin th), far
        dirs['odd_mid'] = g * 0.01 * torch.cos(tht) * torch.exp(-(lrt + 2) ** 2 / 2)                    # x-odd direction (FD expected noisy)
        epss = [float(e) for e in kw.get('eps', '1e-4,1e-5').split(',')]
        sel = kw.get('dirs', ','.join(dirs.keys())).split(',')
        for name, dg in dirs.items():
            if name not in sel:
                continue
            du = (dg / TM.scale).reshape(-1)
            t_tan = time.time(); dF, dth_exit = TM.tangent(du, torch.zeros(2, device=dev), wm); log(json.dumps(dict(m1=name, wall_tangent=round(time.time() - t_tan, 1))))
            if kw.get('lintest', '1') == '1':
                dF2, _ = TM.tangent(2 * du, torch.zeros(2, device=dev), wm); dFr, _ = TM.tangent(du, torch.zeros(2, device=dev), wm)
                log(json.dumps(dict(m1=name, linearity_rel=float(torch.linalg.norm(dF2 - 2 * dF) / torch.linalg.norm(dF2)), repeat_rel=float(torch.linalg.norm(dFr - dF) / torch.linalg.norm(dF)))))
            dTg_tan = (du * TM.scale.expand(Nr, Nth).reshape(-1) - dF[:TM.N] * TM.scale.expand(Nr, Nth).reshape(-1)).reshape(Nr, Nth)   # dT = dg - dF*scale
            for eps in epss:
                Tg2, info2 = TM.base(g + eps * dg, z, store=False)
                dTg_fd = (Tg2 - Tg) / eps
                diff = dTg_fd - dTg_tan
                scal = dTg_fd.abs().amax(dim=1, keepdim=True) + 1e-300
                bands = {}
                for lo_, hi_ in ((-14, -8), (-8, -4), (-4, -2), (-2, 2), (2, 10.01)):
                    m = (S.lr >= lo_) & (S.lr < hi_)
                    bands['[%g,%g)' % (lo_, hi_)] = dict(rel_rms=float(torch.sqrt((diff[m] ** 2).sum() / (dTg_fd[m] ** 2).sum().clamp(min=1e-300))), fd_norm=float(torch.sqrt((dTg_fd[m] ** 2).mean())))
                dth_e_fd = [(info2['th_e_deg'][k] - info['th_e_deg'][k]) / eps for k in range(2)]
                dth_e_tan = [math.degrees(float(dth_exit[TM.N + k])) for k in range(2)]
                log(json.dumps(dict(m1=name, eps=eps, rel_rms_total=float(torch.linalg.norm(diff) / torch.linalg.norm(dTg_fd)), bands=bands, dthe_fd_deg_per_unit=dth_e_fd, dthe_tan_deg_per_unit=dth_e_tan, wall=info2['wall_base'])))
                TM.base(g, z, store=False)  # restore cur (A, pref) for the base; cheap enough? (re-trace) -- needed because base() overwrote self.cur without store
            Tg, info = TM.base(g, z, store=True)
        return
    if mode == 'lincol':
        # consistent linear response of the state (and zeros) to the datum coefficient b_1: solve J [du, dz] = -dF/db_1 with dF_grid/db_1 = -pref A cos(theta_exit) / scale
        Tg, binfo = TM.base(g, z, store=True); c = TM.cur; S = TM.S
        dT_db1 = (c['pref'][0] * c['A'][0] * torch.cos(c['TH_exit'][0, :TM.N])) / TM.scale.expand(Nr, Nth).reshape(-1)
        b = torch.cat([dT_db1, torch.zeros(2, device=dev)])                                  # -dF/db_1
        def mv(v):
            dF, _ = TM.tangent(v[:-2], v[-2:], wm); return dF
        t0 = time.time(); x, hist, sv = gmres(mv, b, kmax=kmax, tol=gm_tol, log=log, tsvd=float(kw.get('tsvd', '0')))
        dFlin, dth_exit = TM.tangent(x[:-2], x[-2:], wm)
        v = (x[:-2].reshape(Nr, Nth) * TM.scale)                                               # dg / db_1
        vodd = 0.5 * (v - v[:, TM.flip]); veven = 0.5 * (v + v[:, TM.flip])
        rowmax = g.max(dim=1, keepdim=True).values.clamp(min=1e-300)
        bands = {}
        for lo_, hi_ in ((-14, -8), (-8, -4), (-4, -2), (-2, 2), (2, 10.01)):
            m = (S.lr >= lo_) & (S.lr < hi_)
            bands['[%g,%g)' % (lo_, hi_)] = dict(odd_rel_rms=float(torch.sqrt(((vodd[m] / rowmax[m]) ** 2).mean())), even_rel_rms=float(torch.sqrt(((veven[m] / rowmax[m]) ** 2).mean())), odd_rel_max=float((vodd[m] / rowmax[m]).abs().max()))
        d0 = TM.diag(g); d1 = TM.diag(g + v)                                                     # W is linear in g: the response of the DW diagnostics is d1 - d0
        resp = {k: {kk: d1[k][kk] - d0[k][kk] for kk in d0[k]} for k in ('DW_lr-12', 'DW_lr-10')}
        resp['m1'] = d1['m1'] - d0['m1']; resp['c'] = d1['c'] - d0['c']
        log(json.dumps(dict(lincol='b1', gmres_final=hist[-1], gmres_its=len(hist), H_sv=[sv[0], sv[-1]], wall_gmres=round(time.time() - t0, 1), linear_model_residual=float(torch.linalg.norm(b - dFlin * 0 - (b - (dFlin + b - b))) ) if False else float(torch.linalg.norm(dFlin - b) / torch.linalg.norm(b)),
                            dz_deg_per_unit=[math.degrees(float(x[-2])), math.degrees(float(x[-1]))], dthe_deg_per_unit=[math.degrees(float(dth_exit[TM.N])), math.degrees(float(dth_exit[TM.N + 1]))],
                            x_norm=float(torch.linalg.norm(x)), odd_frac=float(torch.linalg.norm(vodd) / torch.linalg.norm(v)), bands=bands, response_rows=resp, base=binfo)))
        np.savez('runs/pfwd/tan/%s_resp_b1.npz' % tag, v=v.cpu().numpy(), x_tail=x[-2:].cpu().numpy(), lr=lr, th=TM.S.th.cpu().numpy(), p=p, b1=b1, hist=np.array(hist), sv=np.array(sv))
        log(json.dumps(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))); return
    if mode == 'lincheck':
        # range of validity of the linear response: for b_1 = eps, compare |F(g + eps v, z0 + eps dz; b_1 = eps)| (should be O(eps^2)) with |F(g, z0; b_1 = eps)| (O(eps))
        R = np.load(kw['resp'], allow_pickle=True); v = torch.tensor(R['v'], device=dev); dz = R['x_tail']
        for eps in [float(e) for e in kw.get('eps', '1e-6,1e-5,1e-4,1e-3').split(',')]:
            TM.F_odd = np.array([eps] + [0.0] * 15)
            F0, i0 = TM.residual(g, z, wm); F1, i1 = TM.residual((g + eps * v).clamp(min=0.0), [z[0] + eps * float(dz[0]), z[1] + eps * float(dz[1])], wm)
            Fodd1 = F1[:-2].reshape(Nr, Nth); Fodd1 = 0.5 * (Fodd1 - Fodd1[:, TM.flip])
            log(json.dumps(dict(lincheck=eps, normF_unperturbed=float(torch.linalg.norm(F0)), normF_corrected=float(torch.linalg.norm(F1)), ratio=float(torch.linalg.norm(F1) / torch.linalg.norm(F0)),
                                normF_corrected_grid_max=float(F1[:-2].abs().max()), normF_corrected_odd=float(torch.linalg.norm(Fodd1)), match_deg_unpert=[math.degrees(float(F0[-2]) / wm), math.degrees(float(F0[-1]) / wm)],
                                match_deg_corrected=[math.degrees(float(F1[-2]) / wm), math.degrees(float(F1[-1]) / wm)], th_e_unpert=i0['th_e_deg'], th_e_corrected=i1['th_e_deg'],
                                th_e_shift_realised_deg=[i1['th_e_deg'][k] - 90.0 - 180.0 * k for k in range(2)], th_e_shift_linear_deg=[eps * math.degrees(float(dz[k])) for k in range(2)], unfinished=i1['unfinished'])))
        log(json.dumps(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))); return
    # ---- Newton
    F, info = TM.residual(g, z, wm)
    nF = float(torch.linalg.norm(F)); log(json.dumps(dict(it=0, normF=nF, normF_grid=float(torch.linalg.norm(F[:-2])), match_deg=[math.degrees(float(F[-2]) / wm), math.degrees(float(F[-1]) / wm)], info=info)))
    u = (g / TM.scale).reshape(-1)
    for it in range(1, maxit + 1):
        Tg, binfo = TM.base(g, z, store=True)
        Fg = ((g - Tg) / TM.scale).reshape(-1); Fm = wm * torch.tensor([TM.cur['th_e'][0] - z[0], TM.cur['th_e'][1] - z[1]], device=dev); F = torch.cat([Fg, Fm]); nF = float(torch.linalg.norm(F))
        def mv(v):
            dF, _ = TM.tangent(v[:-2], v[-2:], wm); return dF
        t0 = time.time()
        x, hist, sv = gmres(mv, -F, kmax=kmax, tol=gm_tol, log=log, tsvd=float(kw.get('tsvd', '0')))
        log(json.dumps(dict(it=it, gmres_final=hist[-1], gmres_its=len(hist), H_sv_max=sv[0], H_sv_min=sv[-1], wall_gmres=round(time.time() - t0, 1), dz_deg=[math.degrees(float(x[-2])), math.degrees(float(x[-1]))], dx_norm=float(torch.linalg.norm(x)), base=binfo)))
        # true-residual check of the linear model (optional, cheap: one tangent application)
        dFlin, _ = TM.tangent(x[:-2], x[-2:], wm); log(json.dumps(dict(it=it, linear_model_residual=float(torch.linalg.norm(F + dFlin) / nF), dx_max=float(x[:-2].abs().max()), dx_rms=float(torch.sqrt((x[:-2] ** 2).mean())))))
        accepted = False; alpha = 1.0
        nbt = int(kw.get('nbt', '11'))
        for bt in range(nbt):
            u_try = u + alpha * x[:-2]; z_try = [z[0] + alpha * float(x[-2]), z[1] + alpha * float(x[-1])]
            g_try = (u_try.reshape(Nr, Nth) * TM.scale).clamp(min=0.0)
            F_try, info_try = TM.residual(g_try, z_try, wm); nF_try = float(torch.linalg.norm(F_try))
            pred = float(torch.linalg.norm(F + alpha * dFlin))
            log(json.dumps(dict(it=it, trial=bt, alpha=alpha, normF_try=nF_try, normF=nF, predicted_linear=pred, normF_grid_try=float(torch.linalg.norm(F_try[:-2])), match_deg_try=[math.degrees(float(F_try[-2]) / wm), math.degrees(float(F_try[-1]) / wm)], th_e_deg=info_try['th_e_deg'], z_try_deg=[math.degrees(z_try[0]), math.degrees(z_try[1])], unfinished=info_try['unfinished'])))
            if nF_try < nF and info_try['unfinished'] == 0:
                accepted = True; break
            alpha *= 0.5
        if not accepted:
            log(json.dumps(dict(it=it, accepted=False, reason='no decrease of the true residual in %d backtracking steps (alpha down to %g)' % (nbt, alpha * 2)))); break
        u, z, g = u_try, z_try, g_try
        np.savez('runs/pfwd/tan/%s_it%d.npz' % (tag, it), g=g.cpu().numpy(), lr=lr, th=TM.S.th.cpu().numpy(), z=np.array(z), p=p, b1=b1, a_even=np.array(a_even), normF=nF_try)
        log(json.dumps(dict(it=it, accepted=True, alpha=alpha, normF=nF_try, defect_max=float(F_try[:-2].abs().max()), defect_rms=float(torch.sqrt((F_try[:-2] ** 2).mean())), z_deg=[math.degrees(z[0]), math.degrees(z[1])], th_e_deg=info_try['th_e_deg'])))
    log(json.dumps(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))


if __name__ == '__main__':
    main()
